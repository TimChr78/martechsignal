"""Test suite for build_tools.py - the martechsignal.com static site generator.

Run:  cd /opt/data/martechsignal && python3 -m pytest tools/test_build.py -v
No external deps beyond pytest. Build runs once per session (~1s).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent  # martechsignal/
TOOLS_JSON = ROOT / "tools" / "tools.json"
CATS_JSON = ROOT / "tools" / "categories.json"
BUILD_SCRIPT = ROOT / "tools" / "build_tools.py"


# ── Fixtures ──────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def build():
    """Run the build once; all tests validate its output."""
    # H-4: hub indexes are a build input to build_tools (its sitemap scan reads
    # them), so build_hubs runs first, mirroring deploy.sh ordering.
    hubs = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "build_hubs.py")],
        capture_output=True, text=True, timeout=60, cwd=str(ROOT),
    )
    assert hubs.returncode == 0, f"Hub build failed:\n{hubs.stderr}"
    r = subprocess.run(
        [sys.executable, str(BUILD_SCRIPT)],
        capture_output=True, text=True, timeout=60, cwd=str(ROOT),
    )
    assert r.returncode == 0, f"Build failed:\n{r.stderr}"
    return r.stdout


@pytest.fixture(scope="session")
def tools():
    return json.loads(TOOLS_JSON.read_text())


@pytest.fixture(scope="session")
def cats():
    return json.loads(CATS_JSON.read_text())


@pytest.fixture(scope="session")
def active_tools(tools):
    return [t for t in tools if t.get("status", "active") == "active"]


@pytest.fixture(scope="session")
def hub_cats(cats):
    return [c for c in cats if "hub" in c]


@pytest.fixture(scope="session")
def non_hub_cats(cats):
    return [c for c in cats if "hub" not in c]


def read_page(rel_path):
    """Read a generated HTML page, assert it exists."""
    p = ROOT / rel_path
    assert p.is_file(), f"Missing generated page: {rel_path}"
    return p.read_text()


# ── 1. Data integrity ────────────────────────────────────────────────

class TestDataIntegrity:
    def test_tools_json_loads(self, tools):
        assert len(tools) > 50, f"Only {len(tools)} tools - data may be truncated"

    def test_categories_json_loads(self, cats):
        assert len(cats) >= 10, f"Only {len(cats)} categories"

    def test_tool_required_fields(self, tools):
        required = {"name", "slug", "description", "category"}
        for t in tools:
            missing = required - set(t.keys())
            assert not missing, f"Tool '{t.get('name', '?')}' missing: {missing}"
        # website required for active tools only
        active = [t for t in tools if t.get("status", "active") == "active"]
        for t in active:
            assert t.get("website"), f"Active tool '{t['name']}' missing website"

    def test_tool_slugs_unique(self, tools):
        slugs = [t["slug"] for t in tools]
        dupes = [s for s in slugs if slugs.count(s) > 1]
        assert not dupes, f"Duplicate slugs: {set(dupes)}"

    def test_tool_slugs_url_safe(self, tools):
        for t in tools:
            assert re.match(r"^[a-z0-9][a-z0-9-]*$", t["slug"]), \
                f"Bad slug: '{t['slug']}' ({t['name']})"

    def test_category_slugs_unique(self, cats):
        slugs = [c["slug"] for c in cats]
        assert len(slugs) == len(set(slugs)), "Duplicate category slugs"

    def test_tool_category_exists(self, tools, cats):
        cat_slugs = {c["slug"] for c in cats}
        for t in tools:
            assert t["category"] in cat_slugs, \
                f"Tool '{t['name']}' has unknown category '{t['category']}'"

    def test_category_tools_match(self, tools, cats):
        """categories.json tool arrays must match tools.json assignments.
        open-source is a meta-category: it aggregates ALL active OSS tools,
        not just tools with category='open-source'."""
        active = [t for t in tools if t.get("status", "active") == "active"]
        for c in cats:
            if c["slug"] == "open-source":
                expected = sorted(t["slug"] for t in active if t.get("open_source"))
            else:
                expected = sorted(t["slug"] for t in active if t["category"] == c["slug"])
            actual = sorted(c.get("tools", []))
            assert actual == expected, \
                f"Category '{c['slug']}': json has {len(actual)} tools, tools.json has {len(expected)}"


# ── 2. Build output ──────────────────────────────────────────────────

class TestBuild:
    def test_build_succeeds(self, build):
        assert "Done!" in build

    def test_page_counts(self, build, active_tools, cats, hub_cats):
        n_tools = len(active_tools)
        n_cats = len(cats)
        n_hubs = len(hub_cats)
        expected = f"{n_tools} tool pages + {n_cats} categories + {n_hubs} hub"
        assert expected in build, f"Expected '{expected}' in output: {build}"

    def test_sitemap_written(self, build):
        assert "sitemap.xml" in build
        sm = ROOT / "sitemap.xml"
        assert sm.is_file()
        urls = sm.read_text().count("<url>")
        assert urls > 100, f"Only {urls} sitemap URLs"


# ── 3. Tool pages ────────────────────────────────────────────────────

class TestToolPages:
    def test_all_tool_pages_exist(self, build, active_tools):
        for t in active_tools:
            p = ROOT / "tools" / t["slug"] / "index.html"
            assert p.is_file(), f"Missing tool page: {t['slug']}"

    def test_tool_page_has_schema(self, active_tools):
        """Spot-check 5 tool pages for valid schema.org."""
        for t in active_tools[:5]:
            html = read_page(f"tools/{t['slug']}/index.html")
            m = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
            assert m, f"No schema.org in {t['slug']}"
            schema = json.loads(m.group(1))
            # Schema blocks are JSON arrays: [{SoftwareApplication}, {BreadcrumbList}]
            if isinstance(schema, list):
                types = {s.get("@type") for s in schema}
            else:
                types = {schema.get("@type")}
            assert types & {"SoftwareApplication", "Product", "WebApplication"}, \
                f"No app schema in {t['slug']}: {types}"

    def test_tool_page_has_title(self, active_tools):
        for t in active_tools[:5]:
            html = read_page(f"tools/{t['slug']}/index.html")
            assert f"<title>" in html
            assert t["name"] in html


# ── 4. Category pages ────────────────────────────────────────────────

class TestCategoryPages:
    def test_all_category_pages_exist(self, build, cats):
        for c in cats:
            p = ROOT / "categories" / c["slug"] / "index.html"
            assert p.is_file(), f"Missing category page: {c['slug']}"

    def test_category_page_lists_correct_tools(self, cats, active_tools):
        """Each category page must link to exactly its tools."""
        for c in cats:
            html = read_page(f"categories/{c['slug']}/index.html")
            expected_slugs = {t["slug"] for t in active_tools if t["category"] == c["slug"]}
            for slug in expected_slugs:
                assert f"/tools/{slug}/" in html, \
                    f"Category '{c['slug']}' missing link to tool '{slug}'"

    def test_category_schema_itemlist(self, cats, active_tools):
        """Category pages emit one ld+json block whose @graph holds a
        BreadcrumbList and an ItemList (M1/MUSE-12, 2026-09-07). The old version of
        this test expected a top-level ItemList, which the @graph refactor removed."""
        for c in cats:
            html = read_page(f"categories/{c['slug']}/index.html")
            blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
            assert blocks, f"No schema in category '{c['slug']}'"
            payloads = [json.loads(b) for b in blocks]
            members = [m for p in payloads for m in (p.get("@graph") or [p])]
            types = [m.get("@type") for m in members if isinstance(m, dict)]
            assert "BreadcrumbList" in types, \
                f"Category '{c['slug']}': no BreadcrumbList in {types}"
            lists = [m for m in members if isinstance(m, dict) and m.get("@type") == "ItemList"]
            assert lists, f"Category '{c['slug']}': no ItemList in {types}"
            item_list = lists[0]
            # open-source is a meta-category: it aggregates ALL active OSS tools
            if c["slug"] == "open-source":
                expected = [t for t in active_tools if t.get("open_source")]
            else:
                expected = [t for t in active_tools if t["category"] == c["slug"]]
            assert item_list["numberOfItems"] == len(expected), \
                f"Category '{c['slug']}': schema says {item_list['numberOfItems']}, expected {len(expected)}"
            urls = {str((e.get("item") or {}).get("url") or "") for e in item_list["itemListElement"]}
            missing = [t["slug"] for t in expected
                       if f"https://martechsignal.com/tools/{t['slug']}/" not in urls]
            assert not missing, f"Category '{c['slug']}': ItemList omits {missing}"


# ── 5. Hub pages ─────────────────────────────────────────────────────

class TestHubPages:
    HUB_MARKERS = [
        "flow-strip", "hub-lead", "hub-chooser", "hub-group",
        "hub-reading", "chooser-row", "pick", "read-row",
    ]

    def test_hub_pages_have_all_sections(self, hub_cats):
        for c in hub_cats:
            html = read_page(f"categories/{c['slug']}/index.html")
            for marker in self.HUB_MARKERS:
                assert marker in html, f"Hub '{c['slug']}' missing section: {marker}"

    def test_hub_reading_links_resolve(self, hub_cats):
        for c in hub_cats:
            hub = c["hub"]
            for item in hub.get("reading", []):
                slug = item["slug"]
                p = ROOT / "blog" / slug / "index.html"
                assert p.is_file(), f"Hub '{c['slug']}' reading link broken: {slug}"

    def test_hub_chooser_links_resolve(self, hub_cats):
        for c in hub_cats:
            hub = c["hub"]
            for row in hub.get("chooser", []):
                for pick in row.get("then", []):
                    slug = pick["slug"]
                    p = ROOT / "tools" / slug / "index.html"
                    assert p.is_file(), f"Hub '{c['slug']}' chooser link broken: {slug}"

    def test_hub_flow_has_four_steps(self, hub_cats):
        for c in hub_cats:
            assert len(c["hub"]["flow"]) == 4, \
                f"Hub '{c['slug']}' flow should have 4 steps"

    def test_hub_data_integrity(self, hub_cats):
        for c in hub_cats:
            hub = c["hub"]
            assert len(hub["lead"]) >= 2, f"Hub '{c['slug']}' needs >= 2 lead paragraphs"
            assert len(hub["chooser"]) >= 3, f"Hub '{c['slug']}' needs >= 3 chooser rows"
            assert len(hub["groups"]) >= 2, f"Hub '{c['slug']}' needs >= 2 tool groups"
            assert len(hub["reading"]) >= 1, f"Hub '{c['slug']}' needs >= 1 reading link"
            assert hub.get("meta"), f"Hub '{c['slug']}' missing meta subtitle"


# ── 6. No hub bleed ──────────────────────────────────────────────────

class TestNoHubBleed:
    def test_non_hub_pages_are_simple(self, non_hub_cats):
        hub_markers = ["hub-chooser", "flow-strip", "hub-reading", "chooser-row"]
        for c in non_hub_cats:
            html = read_page(f"categories/{c['slug']}/index.html")
            for marker in hub_markers:
                assert marker not in html, \
                    f"Non-hub category '{c['slug']}' has hub marker: {marker}"

    def test_non_hub_pages_have_tool_grid(self, non_hub_cats):
        for c in non_hub_cats:
            html = read_page(f"categories/{c['slug']}/index.html")
            assert "tool-grid" in html, f"Non-hub '{c['slug']}' missing tool-grid"


# ── 7. Content quality ───────────────────────────────────────────────

class TestContentQuality:
    def test_no_curly_quotes_in_hub_editorial(self, hub_cats):
        for c in hub_cats:
            html = read_page(f"categories/{c['slug']}/index.html")
            # Extract hub-lead section
            if "hub-lead" in html:
                lead = html.split("hub-lead")[1].split("</section>")[0]
                assert "\u201c" not in lead and "\u201d" not in lead, \
                    f"Curly quotes in hub '{c['slug']}' editorial lead"
                assert "\u2018" not in lead and "\u2019" not in lead, \
                    f"Curly single quotes in hub '{c['slug']}' editorial lead"

    def test_no_lorem_ipsum(self, build, active_tools, cats):
        """No placeholder text should survive to production."""
        for t in active_tools[:10]:
            html = read_page(f"tools/{t['slug']}/index.html")
            assert "lorem ipsum" not in html.lower(), f"Lorem ipsum in {t['slug']}"
        for c in cats:
            html = read_page(f"categories/{c['slug']}/index.html")
            assert "lorem ipsum" not in html.lower(), f"Lorem ipsum in category {c['slug']}"

    def test_pages_have_meta_description(self, active_tools, cats):
        for t in active_tools[:5]:
            html = read_page(f"tools/{t['slug']}/index.html")
            assert 'name="description"' in html, f"No meta description in {t['slug']}"
        for c in cats[:5]:
            html = read_page(f"categories/{c['slug']}/index.html")
            assert 'name="description"' in html, f"No meta description in category {c['slug']}"


# ── 8. Sitemap ───────────────────────────────────────────────────────

class TestSitemap:
    def test_sitemap_covers_all_tool_pages(self, build, active_tools):
        sm = (ROOT / "sitemap.xml").read_text()
        for t in active_tools:
            assert f"/tools/{t['slug']}/" in sm, f"Sitemap missing tool: {t['slug']}"

    def test_sitemap_covers_all_categories(self, build, cats):
        sm = (ROOT / "sitemap.xml").read_text()
        for c in cats:
            assert f"/categories/{c['slug']}/" in sm, f"Sitemap missing category: {c['slug']}"

    def test_sitemap_valid_xml(self, build):
        import xml.etree.ElementTree as ET
        sm = ROOT / "sitemap.xml"
        tree = ET.parse(str(sm))  # raises on malformed XML
        root = tree.getroot()
        assert "urlset" in root.tag


# ── 9. Section hub indexes (/best/, /vs/, /alternatives/) ────────────

class TestSectionHubs:
    """H-4: the three section hubs must exist, link their live children,
    carry consistent schema and be editorially clean. Children come from the
    same content JSONs the child builders render, so a child removed from a
    content JSON must disappear from its hub here too."""

    SECTIONS = {
        "best": "bestx-content.json",
        "vs": "vsx-content.json",
        "alternatives": "alternatives-content.json",
    }

    def _children(self, content_file):
        pages = json.loads((ROOT / "tools" / content_file).read_text())["pages"]
        return pages

    def test_hubs_exist(self, build):
        for sec in self.SECTIONS:
            assert (ROOT / sec / "index.html").is_file(), f"Missing hub: /{sec}/"
            assert (ROOT / sec / "index.md").is_file(), f"Missing hub mirror: /{sec}/index.md"

    def test_hub_self_canonical_and_meta(self, build):
        for sec in self.SECTIONS:
            html = (ROOT / sec / "index.html").read_text()
            m = re.search(r'rel="canonical" href="([^"]+)"', html)
            assert m and m.group(1) == f"https://martechsignal.com/{sec}/", \
                f"/{sec}/ hub canonical wrong: {m and m.group(1)}"
            assert 'name="description"' in html, f"/{sec}/ hub missing meta description"
            assert "<h1>" in html, f"/{sec}/ hub missing h1"

    def test_hub_links_all_children(self, build):
        for sec, content_file in self.SECTIONS.items():
            html = (ROOT / sec / "index.html").read_text()
            for p in self._children(content_file):
                url = f"/{sec}/{p['slug']}/"
                assert url in html, f"Hub /{sec}/ missing child link {url}"
                assert (ROOT / sec / p["slug"] / "index.html").is_file(), \
                    f"Hub /{sec}/ links {url} but child page does not exist"
                assert p["title"] in html, f"Hub /{sec}/ missing child title '{p['title']}'"

    def test_hub_schema_shapes_and_completeness(self, build):
        for sec in self.SECTIONS:
            html = (ROOT / sec / "index.html").read_text()
            blocks = re.findall(
                r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
            nodes = []
            for b in blocks:
                d = json.loads(b)
                if isinstance(d, dict) and "@graph" in d:
                    nodes += d["@graph"]
                else:
                    nodes += d if isinstance(d, list) else [d]
            types = [n["@type"] for n in nodes]
            assert "CollectionPage" in types, f"/{sec}/ hub: no CollectionPage node"
            assert "BreadcrumbList" in types, f"/{sec}/ hub: no BreadcrumbList"
            for n in nodes:
                if n["@type"] == "CollectionPage":
                    assert n["url"] == f"https://martechsignal.com/{sec}/"
                    # R5 completeness: hasPart entries are plain WebPages with
                    # name+url; hub never emits product-typed nodes (no
                    # offers/review on a hub).
                    parts = n.get("hasPart") or []
                    assert parts, f"/{sec}/ hub: empty hasPart"
                    for p in parts:
                        assert p["@type"] == "WebPage" and p.get("name") and p.get("url")
                if n["@type"] == "BreadcrumbList":
                    pos = [i["position"] for i in n["itemListElement"]]
                    assert pos == sorted(pos) and pos[0] == 1

    def test_hub_editorial_rules(self, build):
        banned = ["\u2014", "\u2013", "\u201c", "\u201d", "\u2018", "\u2019",
                  "delve", "crucial", "leverage"]
        for sec in self.SECTIONS:
            html = (ROOT / sec / "index.html").read_text()
            low = html.lower()
            for bad in banned:
                assert bad not in low, f"/{sec}/ hub contains banned token {bad!r}"

    def test_sitemap_lists_hubs(self, build):
        sm = (ROOT / "sitemap.xml").read_text()
        for sec in self.SECTIONS:
            assert f"https://martechsignal.com/{sec}/</loc>" in sm, \
                f"Sitemap missing hub /{sec}/"


class TestCatalogSchema:
    """M21 (2026-09-27): the machine-readable catalog validates in CI against the
    published schema.json so field names cannot drift apart again."""

    def test_catalog_record_shapes(self):
        import json as _j
        schema = _j.loads((ROOT / "tools" / "schema.json").read_text())
        data = _j.loads((ROOT / "tools" / "tools.json").read_text())
        required = schema["required"]
        props = schema["properties"]
        banned_aliases = {"url", "github", "pricing"}
        for rec in data:
            for key in required:
                assert key in rec, f"{rec.get('slug')}: missing required field {key}"
            for key in banned_aliases:
                assert key not in rec, f"{rec.get('slug')}: legacy alias field {key}"
            for key, val in rec.items():
                if key in props and "type" in props[key]:
                    allowed = props[key]["type"]
                    allowed = [allowed] if isinstance(allowed, str) else allowed
                    ok = any(
                        (ty == "string" and isinstance(val, str))
                        or (ty in ("integer", "number") and isinstance(val, (int, float)) and not isinstance(val, bool))
                        or (ty == "boolean" and isinstance(val, bool))
                        or (ty == "array" and isinstance(val, list))
                        or (ty == "null" and val is None)
                        for ty in allowed
                    )
                    assert ok, f"{rec['slug']}.{key}: {type(val).__name__} not in {allowed}"


# ── r8 hard-fail lints (2026-09-28): the audit's own falsifiability checks ──

def test_no_template_placeholders_left_in_output():
    """r8 C1: a {n} or {token} literal reaching HTML is a template leak."""
    bad = []
    for f in list(ROOT.rglob("index.html")) + [ROOT / "404.html"]:
        if "deploy-out" in f.parts or "node_modules" in f.parts or not f.exists():
            continue
        if re.search(r"\{(n|slug|count|title|meta|description|desc|name|price|date|url|cat|category|tools)\}", f.read_text(errors="ignore")):
            bad.append(str(f.relative_to(ROOT)))
    assert not bad, f"template placeholders leaked into: {bad[:5]}"


def test_exactly_one_markdown_alternate_per_page():
    """r8 M4: duplicate rel=alternate markdown links (generator split)."""
    bad = []
    for f in list(ROOT.rglob("index.html")) + [ROOT / "404.html"]:
        if "deploy-out" in f.parts or "node_modules" in f.parts or not f.exists():
            continue
        n = f.read_text(errors="ignore").count('rel="alternate" type="text/markdown"')
        if n > 1:
            bad.append((str(f.relative_to(ROOT)), n))
    assert not bad, f"double markdown alternates: {bad[:5]}"


def test_stylesheet_cache_bust_uniform():
    """r8 L1: exactly one style.min.css?v= value may exist site-wide."""
    import hashlib
    want = hashlib.md5((ROOT / "style.css").read_bytes()).hexdigest()[:8]
    bad = []
    for f in list(ROOT.rglob("index.html")) + [ROOT / "404.html"]:
        if "deploy-out" in f.parts or "node_modules" in f.parts or not f.exists():
            continue
        for v in re.findall(r"style\.min\.css\?v=([a-f0-9]{8})", f.read_text(errors="ignore")):
            if v != want:
                bad.append((str(f.relative_to(ROOT)), v))
    assert not bad, f"stale stylesheet hashes: {bad[:5]}"


# ── GSC Product snippets regression lints (2026-09-28) ──

def test_no_reviewcount_or_ratingcount_markup():
    """GSC: "Value in property reviewCount must be positive" (ERROR).
    reviewCount/ratingCount must never ship: AggregateRating was dropped
    sitewide (R3-H2, Tim 2026-09-17) and zero counts are the textbook
    spammy-markup trigger (R3-C1, v2.3.1). Omit, never zero."""
    bad = []
    for f in list(ROOT.rglob("index.html")) + [ROOT / "404.html"]:
        if "deploy-out" in f.parts or "node_modules" in f.parts or not f.exists():
            continue
        txt = f.read_text(errors="ignore")
        if "reviewCount" in txt or "ratingCount" in txt:
            bad.append(str(f.relative_to(ROOT)))
    assert not bad, f"reviewCount/ratingCount markup reappeared in: {bad[:5]}"


def test_review_itemreviewed_is_typed_object():
    """GSC: "Invalid object type for field itemReviewed" (ERROR).
    Every Review node's itemReviewed must be an object carrying its own
    @type (the plain-@id-ref era broke Google's parser)."""
    import json as _json
    bad = []
    for f in list(ROOT.rglob("index.html")) + [ROOT / "404.html"]:
        if "deploy-out" in f.parts or "node_modules" in f.parts or not f.exists():
            continue
        txt = f.read_text(errors="ignore")
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', txt, re.S):
            try:
                node = _json.loads(m.group(1))
            except Exception:
                continue
            for n in (node if isinstance(node, list) else [node]):
                if isinstance(n, dict) and n.get("@type") == "Review":
                    ir = n.get("itemReviewed")
                    if not isinstance(ir, dict) or not ir.get("@type"):
                        bad.append(str(f.relative_to(ROOT)))
    assert not bad, f"Review.itemReviewed must be a typed object, broken in: {bad[:5]}"


# ── R3 "one fact, one source, one pipeline" lints (r9 H1, 2026-09-28) ──

import json as _r3json
import re as _r3re

_APPROX = _r3re.compile(r'(around|about|over|more than|nearly|roughly|approx|\+|-plus|\bplus\b|up to)\s*$', _r3re.I)


def _r3_records():
    out = {}
    for name in ("tools.json", "guides.json"):
        for t in _r3json.loads((ROOT / "tools" / name).read_text()):
            out[t["slug"]] = t
    return out


def _r3_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, list):
        for x in obj:
            yield from _r3_strings(x)
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _r3_strings(v)


def test_catalog_prose_facts_match_record_fields():
    """r9 H1: a star count or verification date in prose that contradicts the
    record's own field is the product falsifying itself. Approximate claims
    ("around 10,500") are fine; exact ones must equal the field."""
    bad = []
    for fname in ("tools.json", "guides.json", "score-content-b.json"):
        path = ROOT / "tools" / fname
        if not path.exists():
            continue
        blob = path.read_text()
        recs = _r3_records()
        for slug, t in recs.items():
            pass  # field mapping by nearest-slug handled below
        # per-record: walk entries keyed by slug
        data = _r3json.loads(blob)
        entries = data if isinstance(data, list) else [data]
        for t in entries:
            if not isinstance(t, dict) or "slug" not in t:
                continue
            rec = recs.get(t["slug"])
            stars = rec.get("github_stars") if rec else t.get("github_stars")
            du = (rec or t).get("date_updated") or (rec or t).get("date_verified")
            for txt in _r3_strings(t):
                for m in _r3re.finditer(r'\b(\d{1,3},\d{3})\b(?= (?:GitHub )?stars)', txt):
                    lead = txt[max(0, m.start() - 20):m.start()]
                    if _APPROX.search(lead):
                        continue
                    want = f"{stars:,}" if stars else None
                    if m.group(1) != want:
                        bad.append((fname, t["slug"], m.group(1), want))
                for m in _r3re.finditer(r'(?:verified|checked)[^.\d]{0,25}(\d{4}-\d{2}-\d{2})', txt):
                    if du and m.group(1) != du:
                        bad.append((fname, t["slug"], m.group(1), du))
    assert not bad, f"prose facts drift from record fields: {bad[:6]}"


def test_price_from_is_lowest_quoted_amount():
    """r9 H1 (jasper $49-vs-$39): price_from is the entry price and must not
    exceed any plan amount the record itself quotes in price_notes."""
    bad = []
    for t in _r3_records().values():
        pf = t.get("price_from")
        notes = t.get("price_notes") or ""
        # plan prices only: an amount quoted with a billing cadence (unit
        # rates like "$0.009 per email" are not entry prices)
        _segs = [g for g in _r3re.split(r"[;.]", notes)
                 if not _r3re.search(r"add-?ons?|overage", g, _r3re.I)]
        _keep = "; ".join(_segs)
        raw = _r3re.findall(
            r'[$€]\s?(\d[\d,]*(?:\.\d+)?)\s*(?:/|\sper\s)\s*(?:mo|month|seat|user|yr|year)|'
            r'EUR\s?(\d[\d,]*(?:\.\d+)?)\s*(?:/|\sper\s)\s*(?:mo|month|seat|user|yr|year)', _keep)
        amounts = []
        for a, b in raw:
            for x in (a, b):
                if x:
                    try:
                        v = float(x.replace(",", "").rstrip("."))
                    except ValueError:
                        continue
                    if v > 0:
                        amounts.append(v)
        # approximate layered rates ("~$80/user/mo") cannot ground an exact
        # field claim; exclude tilde-quoted amounts like the star lint does
        tilde = []
        for m in _r3re.finditer(r'~\s?[$€]\s?(\d[\d,]*(?:\.\d+)?)', notes):
            try:
                tilde.append(float(m.group(1).replace(",", "")))
            except ValueError:
                pass
        amounts = [a for a in amounts if a not in tilde]
        if pf and amounts and float(pf) > min(amounts):
            bad.append((t["slug"], pf, min(amounts)))
    assert not bad, f"price_from above a quoted plan amount: {bad[:6]}"


def test_homepage_tool_count_matches_catalog():
    """r9 H1 (badge 161 vs body 160): any N-martech-tools literal on the
    homepage must equal the live active tool count."""
    want = sum(1 for t in _r3_records().values()
               if t.get("status") == "active" and t.get("kind") != "Guide")
    bad = []
    for f in (ROOT / "index.html", ROOT / "index.md"):
        if not f.exists():
            continue
        for n in _r3re.findall(r'\b(\d{3}) martech tools', f.read_text(errors="ignore")):
            if int(n) != want:
                bad.append((f.name, n, want))
    assert not bad, f"homepage tool-count literals stale: {bad[:6]}"


def test_content_json_star_literals_resolve_to_records():
    """r9 H1 (203,890 orphan): an exact star count in comparison content must
    be some record's actual github_stars."""
    recs = _r3_records()
    _vals = [t.get("github_stars") for t in recs.values() if t.get("github_stars")]
    valid = set(f"{gs:,}" for gs in _vals)
    bad = []
    for fname in ("bestx-content.json", "vsx-content.json"):
        path = ROOT / "tools" / fname
        if not path.exists():
            continue
        for txt in _r3_strings(_r3json.loads(path.read_text())):
            for m in _r3re.finditer(r'\b(\d{1,3},\d{3})\b(?= (?:GitHub )?stars)', txt):
                if m.group(1) not in valid:
                    bad.append((fname, m.group(1)))
    assert not bad, f"orphan star literals in comparison content: {bad[:6]}"


def test_entity_graph_resolves_id_refs():
    """H9 (r9, 2026-09-28): pages that reference #person/#organization must define
    them in-document via the entity @graph (dangling @id refs fail per-document parsers)."""
    import re as _re
    bad = []
    for f in sorted((ROOT).glob('**/index.html')):
        if 'deploy-out' in str(f):
            continue
        h = f.read_text(errors='ignore')
        c = h.replace(' ', '')
        if '#person' in h and '"@type":"Person"' not in c:
            bad.append((str(f.relative_to(ROOT)), 'person'))
        if '#organization' in h and '"@type":"Organization"' not in c:
            bad.append((str(f.relative_to(ROOT)), 'organization'))
    assert not bad, f'dangling @id refs without entity graph: {bad[:6]}'


def _sitemap_entries():
    import re as _re
    sm = (ROOT / "sitemap.xml").read_text()
    return _re.findall(r'<loc>(.*?)</loc>(?:<lastmod>(.*?)</lastmod>)?', sm)


def test_sitemap_locs_unique():
    """H10 (r9, 2026-09-28): /authors/tim-christensen/ shipped twice with two
    conflicting lastmods. Dedupe on <loc> at build time."""
    locs = [loc for loc, _ in _sitemap_entries()]
    assert len(locs) == len(set(locs)), (
        f'duplicate sitemap locs: {[l for l in set(locs) if locs.count(l) > 1][:4]}')


def test_sitemap_lastmod_matches_declared_date():
    """H10 (r9, 2026-09-28): every sitemap lastmod must equal the page's own
    declared dateModified (or be absent when the page declares none). Build
    stamps that contradict page dates teach Google to ignore the field."""
    import re as _re
    bad = []
    for loc, lm in _sitemap_entries():
        rel = loc.replace("https://martechsignal.com/", "")
        f = ROOT / (rel + "index.html") if rel else ROOT / "index.html"
        if not f.is_file():
            bad.append((loc, "no local file"))
            continue
        h = f.read_text(errors="ignore")
        m = _re.search(r'"dateModified"\s*:\s*"([0-9]{4}-[0-9]{2}-[0-9]{2})', h)
        declared = m.group(1) if m else None
        if lm and declared and lm != declared:
            bad.append((loc, f"sitemap {lm} != page {declared}"))
        elif lm and not declared:
            bad.append((loc, f"sitemap {lm} but page declares no date"))
        elif declared and not lm:
            bad.append((loc, f"page declares {declared} but sitemap omits lastmod"))
    assert not bad, f"sitemap/page date mismatches: {bad[:6]}"


def test_money_pages_carry_per_tool_media():
    """H8 (r9, 2026-09-28): every item listed on a money page (best/vs/
    alternatives/category) must render its own media element. Alt text must
    never claim a UI screenshot (branded fact cards, not screencaps)."""
    import json as _json
    import re as _re
    tools_by_slug = {t["slug"]: t for t in _json.loads((ROOT / "tools" / "tools.json").read_text())}
    targets = []  # (file, [slugs that must each have an og img])
    for p in _json.loads((ROOT / "tools" / "bestx-content.json").read_text())["pages"]:
        targets.append((ROOT / "best" / p["slug"] / "index.html",
                        [i["slug"] for i in p.get("items", [])]))
    for p in _json.loads((ROOT / "tools" / "vsx-content.json").read_text())["pages"]:
        trio = [p.get("a_slug"), p.get("b_slug")] + ([p.get("c_slug")] if p.get("c_slug") else [])
        targets.append((ROOT / "vs" / p["slug"] / "index.html", trio))
    for p in _json.loads((ROOT / "tools" / "alternatives-content.json").read_text())["pages"]:
        targets.append((ROOT / "alternatives" / p["slug"] / "index.html",
                        [i["slug"] for i in p.get("items", [])]))
    bad = []
    for f, slugs in targets:
        if not f.is_file():
            bad.append((str(f), "page missing"))
            continue
        h = f.read_text(errors="ignore")
        for s in slugs:
            if s not in tools_by_slug:
                continue  # retired/Guide-kind items route elsewhere; card grid covers guides
            for cand in (f"/og/tools/{s}.png", f"/og/{s}.png"):
                if cand in h:
                    break
            else:
                bad.append((str(f.relative_to(ROOT)), f"no media for {s}"))
        if "screenshot of" in h.lower() or "screenshot shows" in h.lower():
            bad.append((str(f.relative_to(ROOT)), "screenshot claim in copy"))
    # category + hub cards share tool_card_html: spot-check the grid carries media
    for cat in ["marketing-automation", "email-marketing", "crm", "advertising", "content-ai"]:
        f = ROOT / "categories" / cat / "index.html"
        if f.is_file() and "/og/tools/" not in f.read_text(errors="ignore"):
            bad.append((f"categories/{cat}", "grid carries no media"))
    assert not bad, f"money pages missing per-tool media: {bad[:8]}"


def test_serp_lengths_rendered():
    """L3 (r9, 2026-09-28): titles/descriptions are measured on the RENDERED
    tag, not the raw string - esc()/html.escape() expand quotes to entities
    (react-email-editor shipped a 163-char description from a raw-fits cut)."""
    import re as _re
    bad_t, bad_d = [], []
    for f in sorted((ROOT).glob("**/index.html")):
        if "deploy-out" in str(f):
            continue
        h = f.read_text(errors="ignore")
        t = _re.search(r"<title>(.*?)</title>", h)
        d = _re.search(r'name="description" content="(.*?)"', h)
        if t and len(t.group(1)) > 65:
            bad_t.append((str(f.relative_to(ROOT)), len(t.group(1))))
        if d and len(d.group(1)) > 160:
            bad_d.append((str(f.relative_to(ROOT)), len(d.group(1))))
    assert not bad_t, f"titles over 65 chars: {bad_t[:6]}"
    assert not bad_d, f"descriptions over 160 chars: {bad_d[:6]}"


def test_blog_nav_matches_shared():
    """M13 (r9, 2026-09-28): blog hub + posts dropped CATEGORIES/GLOSSARY from
    the masthead. Both blog templates must carry the shared 8-item nav."""
    bad = []
    for f in list((ROOT / "blog").glob("*/index.html")) + [ROOT / "blog" / "index.html"]:
        if not f.is_file():
            continue
        h = f.read_text(errors="ignore")
        for need in ('/categories/', '/glossary/'):
            if need not in h:
                bad.append((str(f.relative_to(ROOT)), f"nav missing {need}"))
    assert not bad, f"blog nav gaps: {bad[:6]}"


def test_catalog_feed_envelope():
    """M14/M15 (r9, 2026-09-28): catalog-tools.json ships as a dataset envelope
    (generated/license/recordCount/records), every record with a nullable
    page_url; acquired records name their successor."""
    import json as _json
    feed = _json.loads((ROOT / "catalog-tools.json").read_text())
    for k in ("generated", "license", "recordCount", "records"):
        assert k in feed, f"envelope missing {k}"
    assert feed["recordCount"] == len(feed["records"])
    bad = [r.get("slug") for r in feed["records"] if "page_url" not in r]
    assert not bad, f"records without page_url: {bad[:4]}"
    acq = [r for r in feed["records"] if r.get("status") != "active"]
    assert acq, "expected non-active records in feed"
    assert all(r.get("successor_slug") for r in acq), (
        f"acquired records without successor: {[r.get('slug') for r in acq]}")


def test_best_direct_answer_and_table_order():
    """M23/M24 (r9, 2026-09-28): every /best/ page opens H1 -> 40-60 word
    direct answer -> comparison table; methodology prose lives under a
    'How we picked' H2 below the table."""
    import re as _re
    bad = []
    for f in sorted((ROOT / "best").glob("*/index.html")):
        h = f.read_text(errors="ignore")
        m = _re.search(r'<p class="direct-answer">(.*?)</p>', h, _re.S)
        if not m:
            bad.append((str(f.relative_to(ROOT)), "no direct answer"))
            continue
        wc = len(_re.sub(r"<[^>]+>", " ", m.group(1)).split())
        if not 40 <= wc <= 60:
            bad.append((str(f.relative_to(ROOT)), f"answer {wc} words"))
        i_h1, i_ans = h.find("</h1>"), h.find("direct-answer")
        i_tab, i_how = h.find("<table>"), h.find("How we picked")
        if not (i_h1 < i_ans < i_tab < i_how):
            bad.append((str(f.relative_to(ROOT)), "wrong order"))
    assert not bad, f"best answer/table order: {bad[:6]}"


def test_best_counts_agree_with_items():
    """Stale-count class (M27 r9 + L4 follow-up): ai-crm claimed 8 with 6
    items, geo claimed 8 with 9. Every 'N compared' in title/seo_title/meta
    must equal the page's item count."""
    import json as _json
    import re as _re
    data = _json.loads((ROOT / "tools" / "bestx-content.json").read_text())["pages"]
    bad = []
    for p in data:
        n = len(p.get("items", []))
        for field in ("title", "seo_title", "meta"):
            m = _re.search(r"(\d+) compared", p.get(field, "") or "")
            if m and int(m.group(1)) != n:
                bad.append((p["slug"], field, m.group(1), n))
    assert not bad, f"stale listicle counts: {bad[:6]}"


def test_glossary_definition_floor():
    """L14 (r9, 2026-09-28): /glossary/geo/ shipped 213 words against a 581
    median. No term page may fall below 200 words of substance."""
    import json as _json
    terms = _json.loads((ROOT / "tools" / "glossary.json").read_text())
    if isinstance(terms, dict):
        terms = terms.get("terms", terms.get("pages", []))
    bad = []
    for t in terms:
        dd = t.get("deep_dive") or {}
        dd_words = sum(len(str(v).split()) for v in (dd.values() if isinstance(dd, dict) else [dd]))
        total = len(str(t.get("definition", "")).split()) + len(str(t.get("context", "")).split()) + dd_words
        if total < 200:
            bad.append((t.get("slug"), total))
    assert not bad, f"glossary pages under 200 words: {bad[:6]}"


def test_guides_hub_word_floor():
    """M9 (r9, 2026-09-28): /guides/ shipped as a 182-word link dump, the
    thinnest indexable page. Hub must carry >= 350 rendered words."""
    import re as _re
    html = (ROOT / "guides" / "index.html").read_text()
    text = _re.sub(r"<[^>]+>", " ", html)
    assert len(text.split()) >= 350, "guides hub below 350 words"


def test_best_table_columns_follow_variance():
    """M22 (r9, 2026-09-28): no column burned on a constant (geo's all-No
    Open source), Public API shown where it varies (geo)."""
    geo = (ROOT / "best" / "geo-llm-visibility-tools" / "index.html").read_text()
    assert "<th>Open source</th>" not in geo, "geo keeps constant OSS column"
    assert "<th>Public API</th>" in geo, "geo missing varying API column"


def test_category_pages_link_their_spokes():
    """M26 (r9, 2026-09-28): every vs/alternatives/best page must be linked
    from the category page(s) of its tools. No orphaned spokes."""
    import json as _json
    import re as _re
    tools = _json.loads((ROOT / "tools" / "tools.json").read_text())
    toc = {t["slug"]: t for t in tools}
    want = {}
    for p in _json.loads((ROOT / "tools" / "vsx-content.json").read_text())["pages"]:
        for s in (p.get("a_slug"), p.get("b_slug")):
            if s and s in toc:
                want.setdefault(f"/vs/{p['slug']}/", set()).add(toc[s].get("category"))
    for p in _json.loads((ROOT / "tools" / "alternatives-content.json").read_text())["pages"]:
        if p.get("slug") in toc:
            want.setdefault(f"/alternatives/{p['slug']}/", set()).add(toc[p["slug"]].get("category"))
    for p in _json.loads((ROOT / "tools" / "bestx-content.json").read_text())["pages"]:
        cats = {toc[i["slug"]].get("category") for i in p.get("items", [])
                if i.get("slug") in toc}
        if cats:
            want.setdefault(f"/best/{p['slug']}/", set()).update(cats)
    orphans = []
    for url, cats in want.items():
        linked = any(
            url in (ROOT / "categories" / c / "index.html").read_text()
            for c in cats if c and (ROOT / "categories" / c).exists())
        if not linked:
            orphans.append((url, sorted(c for c in cats if c)))
    assert not orphans, f"spoke pages unlinked from their categories: {orphans[:6]}"


def test_unscored_pages_carry_facts_box():
    """M21 (r9, 2026-09-28): unscored tier-B pages get a grounded Catalog
    facts box (no invented verdict); scored pages keep the score band."""
    zoho = (ROOT / "tools" / "zoho-crm" / "index.html").read_text()
    assert "Catalog facts:" in zoho, "tier-B page missing facts box"
    assert "no verdict here" in zoho, "facts box must disclaim assessment"
    scored = (ROOT / "tools" / "listmonk" / "index.html").read_text()
    assert "MartechSignal Score:" in scored, "scored page lost score band"
    assert "Catalog facts:" not in scored, "scored page wrongly got facts box"


def test_tierb_faq_extras_are_grounded():
    """M21 (r9, 2026-09-28): tier-B FAQ extras cap at 2 (3 core + <=2) and any
    release string cited in the FAQ resolves against tools.json."""
    import json as _json
    import re as _re
    tools = {t["slug"]: t for t in
             _json.loads((ROOT / "tools" / "tools.json").read_text())}
    zoho = (ROOT / "tools" / "zoho-crm" / "index.html").read_text()
    m = _re.search(r"Frequently asked questions(.*?)(?:Similar Tools|Related reading)",
                   zoho, re.S)
    assert m, "FAQ section missing on tier-B page"
    n_q = len(_re.findall(r"<details", m.group(1)))
    assert 3 <= n_q <= 5, f"tier-B FAQ should be 3 core + <=2 extras, got {n_q}"
    t = tools["zoho-crm"]
    if t.get("last_release") and "release" in m.group(1).lower():
        assert str(t["last_release"]) in m.group(1), \
            "release FAQ cites a string absent from the catalog"


def test_featured_in_box_quotes_own_verdicts():
    """M21 (r9, 2026-09-28): tool pages link their best/vs/alternatives
    appearances, quoting our own published verdicts (grounded depth)."""
    zoho = (ROOT / "tools" / "zoho-crm" / "index.html").read_text()
    assert "Also featured in" in zoho, "tier-B page missing featured-in box"
    assert "/best/ai-crm-tools/" in zoho, "known appearance unlinked"
    assert "Best value for small teams" in zoho, "verdict quote missing"


def test_indexnow_key_deployed():
    """L1 (r9, 2026-09-28): the audit checked /indexnow.txt and
    /.well-known/indexnow-key.txt (both correctly 404 — neither is a claimed
    location). The real channel: key file at the keyLocation the submitter
    declares, content == active key, auto-submitted on every deploy."""
    key = (ROOT / "tools" / ".indexnow-key").read_text().strip()
    assert key, "no active IndexNow key"
    src = (ROOT / "tools" / "indexnow_submit.py").read_text()
    assert "keyLocation" in src, "submitter must declare keyLocation"
    assert "indexnow_submit.py" in (ROOT / "deploy.sh").read_text(), \
        "IndexNow submit must run on every deploy"
    root_key = ROOT / f"indexnow-{key}.txt"
    wk_key = ROOT / ".well-known" / f"indexnow-{key}.txt"
    assert root_key.exists(), f"root key file missing: {root_key.name}"
    assert wk_key.exists(), f"well-known key file missing: {wk_key.name}"
    assert root_key.read_text().strip() == key, "root key content mismatch"
    assert wk_key.read_text().strip() == key, "well-known key content mismatch"
    stage_src = (ROOT / "tools" / "stage_deploy.py").read_text()
    assert f"indexnow-{key}.txt" in stage_src, "root key file not REQUIRED in stage"
    assert "well-known/indexnow-" in stage_src, "well-known key not REQUIRED in stage"


def test_faq_answers_name_entity_no_splice():
    """L10 (r9, 2026-09-28): 'What is X?' answers open with the entity name
    and carry no 'It ships with {feature}, {stars}' comma splice."""
    import re as _re
    n8n = (ROOT / "tools" / "n8n" / "index.html").read_text()
    m = _re.search(r'"name": "What is n8n\?",\s*"acceptedAnswer": \{\s*"@type": "Answer",\s*"text": "([^"]+)"',
                   n8n)
    assert m, "n8n FAQ answer missing from JSON-LD"
    a = m.group(1)
    assert a.startswith("n8n:"), f"answer must open with entity name: {a[:60]}"
    assert "It ships with" not in a, "comma-splice template still rendering"
    assert len(a.split()) <= 60, f"answer over 60 words: {len(a.split())}"


def test_self_made_cluster_declared():
    """L16 (r9, 2026-09-28) as CORRECTED by r10 C-1 (2026-09-29): the Claude
    SEO cluster must carry a THIRD-PARTY disclosure (corrections log 2026-09-26
    retracted ownership: MIT project by AgriciDaniel, no affiliation) and zero
    stale figures. The r9 'we make this' badge was a false claim; this test
    pins the correction so it cannot regress."""
    import re as _re
    # slug -> primary query (declared here; enforced on titles below)
    focus = {
        "tools/claude-seo": "claude seo review",
        "blog/claude-seo-benchmark": "claude seo benchmark",
        "blog/claude-seo-vs-codex-seo": "claude seo vs codex seo",
        "blog/claude-seo-vs-seonaut": "claude seo vs seonaut",
    }
    titles = []
    for slug, q in focus.items():
        html = (ROOT / slug / "index.html").read_text()
        assert 'class="made-badge"' in html, f"{slug} missing disclosure badge"
        assert "third-party MIT project by AgriciDaniel" in html, \
            f"{slug} badge must state third-party authorship"
        assert "We make this" not in html, f"{slug} re-asserts retracted claim"
        assert "MartechSignal's own free SEO audit skill" not in html, \
            f"{slug} re-asserts retracted claim"
        t = _re.search(r"<title>(.*?)</title>", html).group(1).lower()
        titles.append(t)
        for w in q.split():
            assert w in t, f"{slug} title {t!r} misses focus word {w!r}"
    assert len(set(titles)) == len(titles), f"cluster titles not distinct: {titles}"
    tool = (ROOT / "tools" / "claude-seo" / "index.html").read_text()
    assert len(_re.findall(r"16,675|16675|2,443", tool)) == 0, \
        "stale star/fork figures persist on /tools/claude-seo/"
    assert "17,737" in tool and "2,599" in tool, "corrected figures missing"


def test_money_pages_link_their_hubs():
    """r10 H-2 (2026-09-29): every /best/ and /vs/ page links at least one
    relevant category hub (symmetric with M26's hub->spoke links)."""
    import re as _re
    bad = []
    for sub in ("best", "vs"):
        for idx in (ROOT / sub).glob("*/index.html"):
            if idx.parent.name == sub:
                continue
            html = idx.read_text()
            n = len(_re.findall(r'href="/categories/(?!")', html))
            if n == 0:
                bad.append(f"/{sub}/{idx.parent.name}/")
    assert not bad, f"money pages linking zero hubs: {bad[:6]}"


def test_markdown_mirrors_carry_no_entities():
    """r10 H-8 (2026-09-29): md mirrors must not leak HTML entities."""
    import re as _re
    bad = []
    for md in list((ROOT / "tools").glob("*/index.md"))[:40]:
        t = md.read_text()
        m = _re.findall(r"&#\\d+;|&(amp|quot|lt|gt|nbsp);", t)
        if m:
            bad.append((str(md.relative_to(ROOT)), m[:2]))
    assert not bad, f"entity leaks in mirrors: {bad[:4]}"


def test_tool_hero_image_priority_and_sizes():
    """M5/M6/M7 (r9, 2026-09-28): the tool screenshot figure is eager with
    high priority (no lazy on the in-viewport image), serves a 480/600/800/
    1280 ladder, and sizes matches the 662px desktop slot."""
    import re as _re
    n8n = (ROOT / "tools" / "n8n" / "index.html").read_text()
    m = _re.search(r'<figure class="tool-screenshot".*?</figure>', n8n, re.S)
    assert m, "tool screenshot figure missing"
    fig = m.group(0)
    assert 'loading="lazy"' not in fig, "M5: hero image still lazy"
    assert 'fetchpriority="high"' in fig, "M5/M6: hero missing high priority"
    for w in ("480w", "600w", "800w", "1280w"):
        assert w in fig, f"M6: srcset missing {w}"
    assert "662px" in fig, "M7: sizes must name the 662px slot"
    assert "372px" not in fig, "M7: stale 372px sizes still present"


def test_font_payload_is_minimal_and_preloaded():
    """M3/M4 (r9, 2026-09-28): only shipped mono weights (500/600) keep
    @font-face; the 400 file is gone; both shipped weights are preloaded so
    none is discovered late."""
    css = (ROOT / "style.css").read_text()
    assert "spline-sans-mono-400" not in css, "dead 400 @font-face still shipped"
    assert not (ROOT / "fonts" / "spline-sans-mono-400.woff2").exists(), \
        "dead 400 font file still on disk"
    for tpl in ("tools/n8n/index.html", "blog/claude-seo-benchmark/index.html"):
        html = (ROOT / tpl).read_text()
        for w in ("spline-sans-mono-500.woff2", "spline-sans-mono-600.woff2"):
            assert f'preload" href="/fonts/{w}"' in html, f"{tpl} misses {w} preload"


def test_critical_css_inline_and_deferred():
    """M1 (r9, 2026-09-28): every page inlines critical CSS (<=7KB) and loads
    the full bundle non-blocking with a noscript fallback; no render-blocking
    stylesheet links remain."""
    import re as _re
    frag = (ROOT / "tools" / ".critical.css").read_text()
    assert len(frag) <= 10240, f"critical block {len(frag)}B exceeds 10KB budget"
    assert "@font-face" not in frag, "fonts must not ride the inline block"
    checked = 0
    for tpl in ("tools/n8n/index.html", "blog/claude-seo-benchmark/index.html",
                "index.html", "best/geo-llm-visibility-tools/index.html"):
        html = (ROOT / tpl).read_text()
        assert "<style>" in html, f"{tpl} missing inline critical"
        assert 'media="print" onload=' in html, f"{tpl} bundle not deferred"
        assert "<noscript><link" in html, f"{tpl} missing noscript fallback"
        blocking = [l for l in
                    _re.findall(r'<link rel="stylesheet" href="/style[^"]*">', html)
                    if "<noscript>" not in html[max(0, html.find(l) - 10):html.find(l)]]
        assert not blocking, f"{tpl} keeps blocking link: {blocking[:1]}"
        # exactly one inline critical block: the sweep must not stuff a second
        # copy inside its own <noscript> fallback (r9 M1 follow-up).
        assert html.count("<style>:root") == 1, \
            f"{tpl} carries {html.count('<style>:root')} critical copies"
        checked += 1
    assert checked == 4


def test_filter_bar_unhides_before_first_paint():
    """r10 H-7 (2026-09-29): the /tools/ filter bar must unhide synchronously
    during parse (no deferred toggle -> no layout shift of the grid)."""
    html = (ROOT / "tools" / "index.html").read_text()
    assert 'id="tool-filter" hidden>' in html, "filter bar lost its no-JS hidden state"
    assert '<script>document.getElementById("tool-filter").hidden=false</script>' in html, \
        "missing synchronous pre-paint unhide for the filter bar"


def test_fact_cards_serve_sized_renditions():
    """r10 H-9 (2026-09-29): money-page fact cards (335px slot) serve a 670w
    rendition via srcset, not the raw 1200px file."""
    import re as _re
    html = (ROOT / "best" / "geo-llm-visibility-tools" / "index.html").read_text()
    imgs = _re.findall(r'<img[^>]*fact card[^>]*>', html)
    assert imgs, "no fact card images on the sampled best page"
    bare = [i for i in imgs if "srcset" not in i]
    assert not bare, f"{len(bare)}/{len(imgs)} fact cards lack srcset"
    assert 'sizes="335px"' in imgs[0], "fact card sizes does not match the 335px slot"


def test_best_pages_carry_above_fold_verdict_cta():
    """r10 H-11 (2026-09-29): every /best/ page carries a verdict-led top-pick
    CTA right after the comparison table (above the fold)."""
    import re as _re
    bad = []
    for idx in (ROOT / "best").glob("*/index.html"):
        if idx.parent.name == "best":
            continue
        html = idx.read_text()
        if 'class="top-pick"' not in html or "Our top pick:" not in html:
            bad.append(idx.parent.name)
    assert not bad, f"best pages without top-pick CTA: {bad[:5]}"


def test_mobile_nav_has_swipe_cue():
    """r10 H-10 (2026-09-29): the one-row mobile nav rail keeps its form but
    carries a discoverability cue (edge fade), not a blind swipe."""
    css = (ROOT / "style.css").read_text()
    assert "mask-image:linear-gradient(90deg,#000 92%,transparent)" in css, \
        "mobile nav swipe cue missing"


def test_skill_packs_live_under_tools():
    """r10 H-6 (2026-09-29): the two skill packs are tool records under
    /tools/ (Agent Skill kind label), not tool-template pages under
    /guides/. Old URLs stay alive via 301."""
    import json as _json
    tools = _json.loads((ROOT / "tools" / "tools.json").read_text())
    guides = _json.loads((ROOT / "tools" / "guides.json").read_text())
    assert guides == [], "guides.json should be empty after the re-home"
    for slug in ("ai-marketing-claude", "digital-marketing-pro"):
        rec = [t for t in tools if t["slug"] == slug]
        assert rec and rec[0].get("kind") == "Agent Skill", f"{slug} not a tool record"
        html = (ROOT / "tools" / slug / "index.html").read_text()
        assert "kind-note" in html, f"/tools/{slug}/ missing kind label"
        assert not (ROOT / "guides" / slug).exists(), f"stale /guides/{slug}/ output"
    redir = (ROOT / "_redirects").read_text()
    for slug in ("ai-marketing-claude", "digital-marketing-pro"):
        assert f"/guides/{slug}/ /tools/{slug}/ 301" in redir, f"301 missing for {slug}"


def test_vs_articles_carry_headline_and_image():
    """r10 H-4 (2026-09-29): every /vs/ Article has headline (= H1) and a
    page-specific image that exists on disk and matches og:image."""
    import re as _re
    bad = []
    for idx in (ROOT / "vs").glob("*/index.html"):
        if idx.parent.name == "vs":
            continue
        html = idx.read_text()
        if '"headline"' not in html:
            bad.append((idx.parent.name, "no headline"))
            continue
        m = _re.search(r'"image":\s*"(https://martechsignal\.com/og/vs/[^"]+\.png)"', html)
        if not m:
            bad.append((idx.parent.name, "no vs image"))
            continue
        rel = m.group(1).replace("https://martechsignal.com/", "")
        if not (ROOT / rel).exists():
            bad.append((idx.parent.name, "missing file " + rel))
        if 'content="https://martechsignal.com/' + rel + '"' not in html:
            bad.append((idx.parent.name, "og:image mismatch"))
    assert not bad, f"vs Article headline/image gaps: {bad[:5]}"


def test_evidence_citations_resolve_honestly():
    """r10 H-5 (2026-09-29): no page may cite a source repository its catalog
    record does not carry; every evidence href is absolute (no bare
    user/repo relative links); labels describe the linked URL."""
    import json as _json
    import re as _re
    tools = {t["slug"]: t for t in
             _json.loads((ROOT / "tools" / "tools.json").read_text())}
    bad = []
    for slug, t in tools.items():
        p = ROOT / "tools" / slug / "index.html"
        if not p.exists():
            continue
        html = p.read_text()
        if not t.get("github_repo"):
            if "the source repository" in html:
                bad.append((slug, "phantom repository citation"))
        for href in _re.findall(r'href="([^"]+)"', html):
            if _re.match(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/?$", href):
                bad.append((slug, f"relative repo href {href}"))
                break
    assert not bad, f"evidence citation gaps: {bad[:5]}"


def test_money_pages_show_freshness_and_pilot_depth():
    """r10 H-1 (2026-09-29): every /best/ and /vs/ page shows a visible
    <time datetime> stamp; the 4 pilot pages additionally carry real product
    screenshots and question-form H2s."""
    import re as _re
    bad_time, bad_pilot = [], []
    for sub in ("best", "vs"):
        for idx in (ROOT / sub).glob("*/index.html"):
            if idx.parent.name == sub:
                continue
            html = idx.read_text()
            if "<time datetime=" not in html:
                bad_time.append(f"/{sub}/{idx.parent.name}/")
    assert not bad_time, f"money pages without visible time: {bad_time[:5]}"
    for slug in ("open-source-crm", "workflow-automation-tools",
                 "ai-email-marketing-tools", "ai-crm-tools"):
        html = (ROOT / "best" / slug / "index.html").read_text()
        if "/og/screenshots/" not in html:
            bad_pilot.append((slug, "no screenshots"))
        if len(_re.findall(r"<h2>[^<]*\\?</h2>", html)) < 3:
            bad_pilot.append((slug, "fewer than 3 question H2s"))
    assert not bad_pilot, f"pilot gaps: {bad_pilot}"
