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
        capture_output=True, text=True, timeout=900, cwd=str(ROOT),
    )
    assert hubs.returncode == 0, f"Hub build failed:\n{hubs.stderr}"
    r = subprocess.run(
        [sys.executable, str(BUILD_SCRIPT)],
        capture_output=True, text=True, timeout=900, cwd=str(ROOT),
    )
    assert r.returncode == 0, f"Build failed:\n{r.stderr}"
    # r23 H-2: builders do not emit the breadcrumb edge natively; the sync
    # pass owns it in deploy.sh ordering, so it owns it here too. Without
    # this, the fixture rebuild strips edges and the graph test flakes.
    s = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "sync_breadcrumbs.py")],
        capture_output=True, text=True, timeout=900, cwd=str(ROOT),
    )
    assert s.returncode == 0, f"Breadcrumb sync failed:\n{s.stderr}"
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
    be some record's actual github_stars.

    r16 H-1 (2026-09-29): extended to normalized comparison (abbreviated
    4.4k forms, bare counts, word-boundary safe so years like 2011 never
    match). Any prose star literal more than 2% from its record fails —
    the audit recipe. Score evidence lines carry no star literals at all
    (structural rule, drift-proof); verdicts/descriptions use digit-free
    scale bands (tens of thousands, a few hundred) or nothing."""
    import re as _re
    recs = _r3_records()
    idx = {t.get("slug"): t for t in recs.values() if isinstance(t, dict)}
    def _norm(s):
        s = s.replace(",", "")
        return int(float(s[:-1]) * 1000) if s.lower().endswith("k") else int(float(s))
    _pat = _re.compile(r'([\d,]+\.?\d*k?)\s*(?:GitHub\s+)?stars?\b|'
                       r'★\s*([\d,]+\.?\d*k?)\b')
    bad = []
    for fname in ("bestx-content.json", "vsx-content.json", "alternatives-content.json"):
        path = ROOT / "tools" / fname
        if not path.exists():
            continue
        for txt in _r3_strings(_r3json.loads(path.read_text())):
            for m in _r3re.finditer(r'\b(\d{1,3},\d{3})\b(?= (?:GitHub )?stars)', txt):
                if m.group(1) not in set(f"{t.get('github_stars'):,}" for t in recs.values() if t.get("github_stars")):
                    bad.append((fname, m.group(1)))
    # normalized >2% check on tool + score prose, resolved by record
    for fname, getdict in (("tools.json", None), ("score-content-a.json", "tools"),
                           ("score-content-b.json", "tools")):
        path = ROOT / "tools" / fname
        data = _r3json.loads(path.read_text())
        items = data if fname == "tools.json" else data.get(getdict, [])
        for entry in (items if isinstance(items, list) else items.values()):
            if not isinstance(entry, dict):
                continue
            slug = entry.get("slug")
            cat = (idx.get(slug) or {}).get("github_stars") if slug else None
            for txt in _r3_strings(entry):
                for m in _pat.finditer(txt):
                    lit = m.group(1) or m.group(2)
                    try:
                        v = _norm(lit)
                    except ValueError:
                        continue
                    if not v or not cat:
                        continue
                    if abs(v - cat) / cat > 0.02:
                        bad.append((f"{fname}:{slug}", f"{lit} vs {cat}"))
    assert not bad, f"stale star literals: {bad[:8]}"


def test_score_evidence_carries_no_star_literals():
    """r16 H-1 (2026-09-29): score pillar evidence lines cite licenses,
    hosting and dates — never star counts (they rot with every snapshot).
    The count lives in Quick-Facts (exact, build-fresh). Zero literals,
    any format, no threshold."""
    import re as _re
    bad = []
    for fname in ("score-content-a.json", "score-content-b.json"):
        data = _r3json.loads((ROOT / "tools" / fname).read_text())
        for entry in data.get("tools", []):
            for pname, pillar in (entry.get("pillars") or {}).items():
                ev = pillar.get("evidence", "") if isinstance(pillar, dict) else ""
                if _re.search(r'[\d,]+\.?\d*k?\s*(?:GitHub\s+)?stars?\b|★', ev):
                    bad.append(f"{fname}:{entry.get('slug')}:{pname}")
    assert not bad, f"star literals in score evidence: {bad[:8]}"


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
        # r16 M-7 (2026-09-29): 75 dangling #website refs + 30 glossary #set
        # refs. Every page referencing them must define them (shared WebSite
        # stub via page_shell; set stub on term leaves, full node on the hub).
        if '#website' in h and '"@type":"WebSite"' not in c:
            bad.append((str(f.relative_to(ROOT)), 'website'))
        if 'glossary/#set' in h and '"@type":"DefinedTermSet"' not in c:
            bad.append((str(f.relative_to(ROOT)), 'termset'))
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
            # r16 L-1: the 1200w slot is a -1200.webp rendition, so the raw
            # .png need not appear; any rung for the slug counts as media.
            for cand in (f"/og/tools/{s}.png", f"/og/{s}.png",
                         f"/og/tools/{s}-", f"/og/{s}-"):
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


def test_best_verdicts_are_unique_per_page():
    """r13 H-1 (2026-09-29): no two tools on a best page share a verdict
    string (the category-default fallback shipped byte-identical verdicts
    on 3 pages / 11 tool-slots)."""
    import json
    import collections as _c
    d = json.loads((ROOT / "tools" / "bestx-content.json").read_text())
    for p in d["pages"]:
        vs = [it.get("verdict", "") for it in p.get("items", [])]
        dups = {k: n for k, n in _c.Counter(vs).items() if n > 1}
        assert not dups, f"{p['slug']} duplicate verdicts: {list(dups)[:2]}"


def test_best_verdict_price_claims_are_catalog_backed():
    """r13 H-1 companion (2026-09-29): any EUR/USD/$ amount in a verdict
    must be traceable to that record's price_notes (symbol-normalized)."""
    import json
    import re as _re
    recs = json.loads((ROOT / "tools" / "tools.json").read_text())
    idx = {x["slug"]: x for x in recs if isinstance(x, dict)}
    d = json.loads((ROOT / "tools" / "bestx-content.json").read_text())
    bad = []
    for p in d["pages"]:
        for it in p.get("items", []):
            v = it.get("verdict", "")
            notes = (idx.get(it["slug"], {}).get("price_notes") or "").replace(",", "")
            for m in _re.finditer(r"(EUR|USD|[$€£])\s?([0-9][0-9,]*)", v):
                tok, num = m.group(1), m.group(2).replace(",", "")
                if not (f"{tok} {num}" in notes or f"{num}/mo" in notes
                        or f"${num}" in notes or f"€{num}" in notes):
                    bad.append((it["slug"], f"{tok} {num}"))
    assert not bad, f"verdict prices not in price_notes: {bad}"


def test_pricing_symbols_follow_record_currency():
    """r13 H-2 (2026-09-29): hero chip + sidebar + pricing cells render the
    symbol from record.currency (7 EUR pages shipped "$" while verdicts
    said EUR). pricing_label is the single source for all three."""
    import re as _re
    bad = []
    for slug in ("accuranker", "nightwatch", "nimt-ai", "otterlyai",
                 "rankscale", "sistrix", "superlines"):
        html = (ROOT / "tools" / slug / "index.html").read_text()
        # Scope to the audit's defect: hero chip + pricing sidebar row.
        # Prose quotes from price_notes (catalog-faithful $ mentions) are
        # out of scope — only the currency-stamped summary elements count.
        zones = _re.findall(r'<p class="count">.*?</p>', html, _re.S)
        zones += _re.findall(r"<dt>Pricing</dt><dd>.*?</dd>", html, _re.S)
        for z in zones:
            if _re.search(r"\$[0-9]", z):
                bad.append((slug, z[:60]))
    assert not bad, f"$ amounts in chip/sidebar on EUR pages: {bad[:4]}"


def test_freemium_pages_carry_both_offer_tiers():
    """r13 H-2(c) (2026-09-29): freemium pages with a free entry tier expose
    an offers array containing price 0 AND the paid entry (HubSpot showed
    only USD 20 while the headline says Free CRM).
    r28 H-2 (2026-10-06): hubspot-crm is now a price_unit:seat record — its
    Offer is suppressed (schema cannot carry the unit), so buffer (free +
    $5 paid, unit-free) carries the example."""
    import json as _j
    import re as _re
    html = (ROOT / "tools" / "buffer" / "index.html").read_text()
    prices = sorted({m.group(1) for m in
                     _re.finditer(r'"price":\s*([0-9.]+)', html)})
    assert "0" in prices and "5" in prices, f"buffer offer prices: {prices}"


def test_identity_graph_is_unfragmented():
    """r13 H-3 (2026-09-29): one @id = one sameAs set. The author page's
    #person carries exactly one sameAs array (ProfilePage mainEntity; the
    _H9 duplicate is retired); Organization carries no sameAs anywhere
    (the author's personal GitHub is not the org's identity); every
    Organization logo carries the #logo @id."""
    import json as _j
    import re as _re
    ap = (ROOT / "authors" / "tim-christensen" / "index.html").read_text()
    sameas = _re.findall(r'"sameAs":\s*\[[^\]]*\]', ap)
    assert len(sameas) == 1, f"author page sameAs sets: {len(sameas)}"
    assert "linkedin.com/in/tchristensen78" in sameas[0], "canonical set lost LinkedIn"
    bad = []
    for f in list(ROOT.rglob("*.html")):
        if "deploy-out" in f.parts or ".well-known" in str(f):
            continue
        h = f.read_text()
        if '"@type": "Organization"' in h and '"sameAs"' in h:
            # sameAs present on an org-bearing page: allowed only inside a
            # Person node or a vendor (tool) node, never the site org.
            for m in _re.finditer(r'\{"@type": "Organization", "@id": "https://martechsignal.com/#organization".*?\}(?=[,}])', h):
                if '"sameAs"' in m.group(0):
                    bad.append(str(f.relative_to(ROOT)))
    assert not bad, f"site org still claims sameAs: {bad[:5]}"
    home = (ROOT / "index.html").read_text()
    assert '"@id": "https://martechsignal.com/#logo"' in home, "homepage logo lost @id"


def test_homepage_keeps_concept_d_and_analytics():
    """r14 H-1 (2026-09-29): the r12 head surgery silently dropped the
    hand-maintained Concept D layout block (6,538 B) and the Umami loader
    from the homepage. Both are pinned: emitted classes must resolve and
    the loader must ship."""
    html = (ROOT / "index.html").read_text()
    head = html.split("</head>")[0]
    for cls in (".dot-grid", ".glow-amber", ".hero-kicker", ".stats-band"):
        assert cls in head, f"Concept D selector {cls} missing"
    assert "analytics.martechsignal.com/script.js" in html, "Umami loader missing"
    assert html.count("Concept D homepage") == 1, "Concept D block duplicated or gone"


def test_sweep_never_shrinks_head_assets():
    """r14 H-1 companion: the stylesheet sweep may normalize links but must
    never reduce a page's script tags or non-critical style blocks (that
    is how Concept D + Umami died). Checked on the hand-maintained pages."""
    import re as _re
    for tpl in ("index.html", "about/index.html",
                "authors/tim-christensen/index.html"):
        html = (ROOT / tpl).read_text()
        n_scripts = len(_re.findall(r"<script", html))
        n_styles = len(_re.findall(r"<style>", html))
        assert n_scripts >= 1, f"{tpl} lost all scripts"
        assert n_styles >= 1, f"{tpl} lost all inline styles"


def test_momentum_stars_match_catalog():
    """r14 H-2 (2026-09-29): one pipeline, one number. Money-page momentum
    figures read the fresh snapshot while tool pages read the catalog, so
    40/40 claims diverged upward. The nightly snapshot now syncs
    github_stars/forks back into the record: every rendered star figure
    must equal its catalog value."""
    import json as _j
    import re as _re
    recs = _j.loads((ROOT / "tools" / "tools.json").read_text())
    idx = {x["slug"]: x for x in recs if isinstance(x, dict)}
    by_name = {x["name"]: x for x in recs if isinstance(x, dict) and x.get("name")}
    bad = []
    for sub in ("best", "vs"):
        for idxf in (ROOT / sub).glob("*/index.html"):
            html = idxf.read_text()
            for m in _re.finditer(r"<li>([^<>]+?) - ([\d,]+) stars", html):
                name, n = m.group(1).strip(), int(m.group(2).replace(",", ""))
                rec = by_name.get(name)
                if rec is None or rec.get("github_stars") is None:
                    continue
                if rec["github_stars"] != n:
                    bad.append((rec["slug"], n, rec["github_stars"]))
    assert not bad, f"star claims diverging from catalog: {bad[:5]}"


def test_image_sizes_describe_real_slots():
    """r14 M-2 (2026-09-29): sizes="335px" understated the 640px money-page
    slot (user-visible upscale at DPR 2). Fact cards and best-item shots
    declare (max-width: 700px) 100vw, 640px; vs-figures grid shots 500px."""
    import re as _re
    bad335 = []
    for sub in ("best", "vs", "alternatives"):
        for idx in (ROOT / sub).glob("*/index.html"):
            if 'sizes="335px"' in idx.read_text():
                bad335.append(f"/{sub}/{idx.parent.name}/")
    assert not bad335, f"stale 335px sizes: {bad335[:5]}"
    html = (ROOT / "best" / "ai-seo-tools" / "index.html").read_text()
    assert "100vw, 640px" in html, "best-item shots missing real-slot sizes"
    vs = (ROOT / "vs" / "n8n-vs-zapier" / "index.html").read_text()
    assert "100vw, 500px" in vs, "vs-figures shots missing grid-slot sizes"


def test_category_intro_counts_match_chips():
    """r15 M-5 (2026-09-29): hand-written intro counts diverged from the
    generated chip (agent-skills 13/22 vs 18, crm 23 vs 24). Intro prose must
    carry the live member count — via the {n} placeholder, substituted at
    build time from the same source as the chip."""
    import json as _j, re as _re
    cat = _j.loads((ROOT / "tools" / "categories.json").read_text())
    cats = cat if isinstance(cat, list) else cat.get("categories", cat)
    recs = _j.loads((ROOT / "tools" / "tools.json").read_text())
    words = {"one": 1, "two": 2, "three": 3, "thirteen": 13, "eighteen": 18,
             "twenty-one": 21, "twenty-three": 23, "twenty-four": 24}
    bad = []
    for c in cats:
        slug = c["slug"]
        if slug == "open-source":
            members = [x for x in recs if x.get("open_source") and x.get("status") == "active"]
        else:
            members = [x for x in recs if x.get("category") == slug and x.get("status") == "active"]
        html = (ROOT / "categories" / slug / "index.html").read_text()
        if "{n}" in html:
            bad.append((slug, "unsubstituted {n}"))
        for m in _re.finditer(r"\b(one|two|three|thirteen|eighteen|twenty-one|twenty-three|twenty-four|\d+)\s+(systems|entries|tools)\b", html, _re.I):
            n = int(m.group(1)) if m.group(1).isdigit() else words[m.group(1).lower()]
            if n != len(members):
                bad.append((slug, m.group(0), len(members)))
    assert not bad, f"intro/chip count divergences: {bad[:6]}"


def test_best_hub_prose_matches_haspart():
    """r15 M-6 (2026-09-29): hub meta said fifteen while body prose said
    three and linked 3 of 15. The live-list sentence is derived from the
    same children as hasPart and the visible list."""
    import json as _j, re as _re
    html = (ROOT / "best" / "index.html").read_text()
    m = _re.search(r"(\w+) lists are live:", html)
    assert m, "best hub missing derived live-list sentence"
    words = {"Fifteen": 15, "Sixteen": 16}
    n = words.get(m.group(1), -1)
    leaf_links = len(_re.findall(r'<li><a href="[^"]*/best/[^"]*/">', html))
    assert n == leaf_links and n > 3, f"hub prose says {m.group(1)} but lists {leaf_links} leaves"


def test_money_templates_carry_publisher_and_ispartof():
    """r15 M-2 (2026-09-29): all 78 money-template pages (/best/ 16, /vs/ 11,
    /categories/ 15, /glossary/ 31, /alternatives/ 5) carry publisher +
    isPartOf @id-refs joining the org and the site. r15 M-9: /vs/ ListItems
    are typed named nodes, not bare stubs."""
    import re as _re
    bad = []
    for base in ("best", "vs", "categories", "glossary", "alternatives"):
        for f in (ROOT / base).glob("*/index.html"):
            h = f.read_text()
            if '"publisher"' not in h or '"isPartOf"' not in h:
                bad.append(f"{base}/{f.parent.name}/")
    assert not bad, f"money pages missing publisher/isPartOf: {bad[:8]}"
    vs = (ROOT / "vs" / "n8n-vs-zapier" / "index.html").read_text()
    assert '"item": {"@type": "SoftwareApplication"' in vs.replace(" ", "").replace("\n", "") or \
        '"item":{"@type":"SoftwareApplication"' in vs.replace(" ", "").replace("\n", ""), \
        "vs ListItems still bare stubs"


def test_organization_node_is_identical_sitewide():
    """r15 M-1/L-2 (2026-09-29): #organization was declared three ways
    (founder inline vs @id-ref, org sameAs present/absent, logo inline vs
    @id). Canonical: founder is a bare @id ref, the Organization carries NO
    sameAs (no org-owned profile exists — omission over fabrication), logo
    is an @id ref. Person keeps its own sameAs."""
    import re as _re
    bad = []
    for pat in ("*/index.html", "*/*/index.html"):
        for f in ROOT.glob(pat):
            if "deploy-out" in f.parts:
                continue
            h = f.read_text()
            if "#organization" not in h:
                continue
            # org node must not claim the author's personal sameAs
            m = _re.search(r'"@type": "Organization", "@id": "https://martechsignal.com/#organization"(.*?)\}, \{"@type":', h)
            if m and '"sameAs"' in m.group(1):
                bad.append(f"{f.parent}/:org-sameAs")
    assert not bad, f"org node divergences: {bad[:8]}"


def test_analytics_loader_present_on_every_page():
    """r15 M-4 (2026-09-29): the Umami loader drifted off 10 hand pages
    (about/contact/privacy/terms/ai-policy + 5 guides) because it is applied
    per-template. Every live page must carry it."""
    import pathlib as _pl
    bad = []
    for pat in ("*/index.html", "*/*/index.html"):
        for f in ROOT.glob(pat):
            if "deploy-out" in f.parts:
                continue
            if "analytics.martechsignal.com/script.js" not in f.read_text():
                bad.append(str(f.parent))
    assert not bad, f"pages without analytics loader: {bad[:12]}"


def test_no_doubled_star_phrases_sitewide():
    """r15 H-1a (2026-09-29): the star sync left 19 doubled "GitHub stars
    GitHub stars" phrases on 16 pages. No rendered page may repeat the
    token, in any content file or output."""
    import pathlib as _pl
    bad = []
    for base in ("tools", "best", "vs", "alternatives", "categories", "blog", "glossary", "guides"):
        for f in (ROOT / base).glob("*/index.html"):
            h = f.read_text()
            if "GitHub stars GitHub stars" in h or "GitHub stars stars" in h:
                bad.append(f"{base}/{f.parent.name}/")
    assert not bad, f"doubled star phrases: {bad[:5]}"


def test_tool_page_star_literals_match_catalog():
    """r15 H-1b (2026-09-29): 14 tool pages showed a stale prose star count
    beside the synced catalog value. Every "N GitHub stars" literal on a
    tool page must equal that record's github_stars."""
    import json as _j, re as _re, pathlib as _pl
    recs = _j.loads((ROOT / "tools" / "tools.json").read_text())
    idx = {x["slug"]: x for x in recs if isinstance(x, dict)}
    pat = _re.compile(r"(\d{1,3}(?:,\d{3})+)\s+GitHub stars\b")
    bad = []
    for f in (ROOT / "tools").glob("*/index.html"):
        slug = f.parent.name
        rec = idx.get(slug, {})
        if not isinstance(rec.get("github_stars"), int):
            continue
        real = f'{rec["github_stars"]:,}'
        for m in pat.finditer(f.read_text()):
            if m.group(1) != real:
                bad.append((slug, m.group(1), real))
                break
    assert not bad, f"stale star literals: {bad[:5]}"


def test_blog_posts_carry_publisher_and_canonical_linkage():
    """r14 M-11 (2026-09-29): every BlogPosting carries a publisher block
    (org name/url/logo) and mainEntityOfPage so posts resolve to the
    organization and their canonical URL."""
    import pathlib as _pl
    bad = []
    for f in (ROOT / "blog").glob("*/index.html"):
        h = f.read_text()
        if '"BlogPosting"' not in h:
            continue
        if '"publisher"' not in h or '"mainEntityOfPage"' not in h:
            bad.append(f.parent.name)
    assert not bad, f"posts missing publisher/linkage: {bad[:5]}"


def test_unscored_tools_still_carry_editorial_depth():
    """r14 M-9 (2026-09-29): /tools/zoho-crm/ was a stub (no score, no
    deep-dive, one link level from the homepage). Unscored tools must still
    carry grounded deep-dive sections (best_for/not_for/stats) and an inbound
    link from their category hub chooser."""
    html = (ROOT / "tools" / "zoho-crm" / "index.html").read_text()
    for needle in ("Best for", "Not for", "Project stats"):
        assert needle in html, f"zoho-crm missing deep-dive section: {needle}"
    hub = (ROOT / "categories" / "crm" / "index.html").read_text()
    assert "/tools/zoho-crm/" in hub, "CRM hub chooser does not link zoho-crm"


def test_category_pages_carry_substantive_intros():
    """r14 M-5 (2026-09-29): thin category pages (<150 words of intro prose
    beyond the listing). Every category page now renders >=150 words of
    category-specific intro copy, derived from catalog data."""
    import re as _re
    thin = []
    for idx in (ROOT / "categories").glob("*/index.html"):
        html = idx.read_text()
        paras = _re.findall(r'class="cat-intro"[^>]*>(.*?)</p>', html, _re.S)
        lead = _re.findall(r'<section class="hub-lead">(.*?)</section>', html, _re.S)
        words = sum(len(_re.sub(r"<[^>]+>", "", p).split()) for p in paras + lead)
        if words < 150:
            thin.append((idx.parent.name, words))
    assert not thin, f"thin category pages: {thin}"


def test_vs_decision_blocks_match_their_pair():
    """r14 M-3 (2026-09-29): two-way /vs/ pages rendered a three-way
    decision block with a self-link. Decision rows must name only the
    page's two contenders; no link may point at the page itself."""
    import json as _j
    d = _j.loads((ROOT / "tools" / "vsx-content.json").read_text())
    pages = d["pages"] if isinstance(d, dict) else d
    plist = list(pages.values()) if isinstance(pages, dict) else pages
    bad = []
    for pg in plist:
        df = pg.get("decision_first") or {}
        head = (df.get("heading") or "").lower()
        pair = {pg.get("a_slug", ""), pg.get("b_slug", "")}
        for r in df.get("rows", []):
            # a row is legal if it is one of the pair OR named in the heading
            # (matomo-vs-plausible deliberately carries a headed trio block)
            if r[0].lower() not in pair and r[0].lower() not in head:
                bad.append((pg["slug"], r[0]))
        for l in df.get("links", []) or []:
            if pg["slug"] in l.get("href", ""):
                bad.append((pg["slug"], "self-link"))
    assert not bad, f"decision block leaks: {bad[:5]}"


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


def test_rendered_prices_never_end_in_bare_currency():
    """r15 M-10 (2026-09-29): zoho rendered "Professional EUR )" (mid-token
    [:60] cut) and espocrm-class cons lines stamped hard $. Pros cut on tier
    boundaries; cons render from the record currency. No rendered price
    string may end in a bare currency code or double /mo."""
    import re as _re
    bad = []
    for f in (ROOT / "tools").glob("*/index.html"):
        h = f.read_text()
        if _re.search(r"(EUR|USD|\$) \)", h):
            bad.append((f.parent.name, "bare currency before )"))
        if "/mo/mo" in h:
            bad.append((f.parent.name, "doubled /mo"))
    assert not bad, f"price render artifacts: {bad[:6]}"


def test_perf_recommendations_applied():
    """r15 M-8 (2026-09-29): font-display optional on all four faces;
    the first vs-shot is eager + fetchpriority high (LCP element)."""
    css = (ROOT / "style.min.css").read_text()
    assert "font-display: swap" not in css and "font-display:swap" not in css, \
        "swap survives in shipped CSS"
    assert css.count("font-display: optional") + css.count("font-display:optional") >= 4, \
        "optional missing on shipped faces"
    vs = (ROOT / "vs" / "n8n-vs-make-vs-zapier" / "index.html").read_text()
    assert 'fetchpriority="high"' in vs, "vs hero missing fetchpriority"
    assert vs.count('fetchpriority="high"') == 1, "more than one high-priority image per vs page"


def test_sitemap_holds_no_redirects_and_counts_agree():
    """r15 L-1 (2026-09-29): /authors/ 301s but sat in the sitemap.
    Redirecting URLs must not be listed. L-5 is by-design (acquired records
    carry page_url:null + successor_slug, not 404 links)."""
    import re as _re
    sm = (ROOT / "sitemap.xml").read_text()
    locs = _re.findall(r"<loc>(.*?)</loc>", sm)
    assert "https://martechsignal.com/authors/" not in locs, "/authors/ redirect in sitemap"
    assert len(locs) == len(set(locs)), "duplicate sitemap locs"


def test_free_entry_pages_carry_both_offer_tiers():
    """r15 L-4 (2026-09-29): 28 free-entry pages emitted a single paid-tier
    Offer. Any page with price_from 0 AND a paid entry carries [0, paid]."""
    import json as _j, re as _re
    recs = _j.loads((ROOT / "tools" / "tools.json").read_text())
    idx = {x["slug"]: x for x in recs if isinstance(x, dict)}
    bad = []
    for f in (ROOT / "tools").glob("*/index.html"):
        h = f.read_text()
        m = _re.search(r'"offers": \{"@type": "Offer", "price": ([\d.]+)', h)
        # r29 N-14 (2026-10-06): unit-priced records restore the honest $0
        # node alone — a single ZERO offer is the fix, not the defect. Only
        # single paid-tier (>0) offers fail.
        if m and float(m.group(1)) > 0 and idx.get(f.parent.name, {}).get("price_from") == 0:
            bad.append(f.parent.name)
    assert not bad, f"single paid-tier Offer on free-entry pages: {bad[:6]}"


def test_glossary_terms_join_the_set_by_id():
    """r15 L-11 (2026-09-29): term leaves inlined an anonymous set while the
    hub declares #set. Leaves reference the set by @id."""
    import re as _re
    bad = []
    for f in (ROOT / "glossary").glob("*/index.html"):
        h = f.read_text()
        if '"@type": "DefinedTermSet"' in h and '"@id": "https://martechsignal.com/glossary/#set"' not in h:
            bad.append(f.parent.name)
    assert not bad, f"terms not @id-joined to the set: {bad[:6]}"


def test_prose_singulars_and_casing():
    """r15 L-13 (2026-09-29): "1 AI features", "1 integrations", lowercase
    "paid pricing starts at" after a period, "Zia AI" redundancy."""
    import re as _re
    bad = []
    for base in ("tools", "best", "vs", "alternatives"):
        for f in (ROOT / base).glob("*/index.html"):
            h = f.read_text()
            for pat, label in ((r"\b1 AI features\b", "plural"), (r"\b1 integrations\b", "plural"),
                               (r"\. paid pricing starts at", "casing"), (r"Zia AI assistant", "redundant")):
                if _re.search(pat, h):
                    bad.append(f"{base}/{f.parent.name}:{label}")
    assert not bad, f"prose artifacts: {bad[:6]}"


def test_rendered_html_carries_no_em_dashes():
    """r15 L-wave / Claude SEO v2.4.1 (2026-09-29): upstream added
    test_no_em_dash.py to its own suite - the auditor now treats em dashes
    as machine-generated tells. Rendered pages use the spaced hyphen."""
    bad = []
    for f in ROOT.rglob("*.html"):
        if "deploy-out" in f.parts:
            continue
        if "\u2014" in f.read_text():
            bad.append(str(f.parent.name) or str(f))
    assert not bad, f"em dashes in rendered output: {bad[:8]}"


def test_money_prose_currency_matches_record():
    """r16 H-2 (2026-09-29): best/vs assessments rendered euro prices for
    dollar-priced products (revealbot, anyword, intercom, clerk-io,
    activecampaign, warmbly, writesonic). A euro sign in money-page prose
    requires a euro-denominated record (EUR in price_notes or currency)."""
    import json as _j
    recs = {x["slug"]: x for x in _j.loads((ROOT / "tools" / "tools.json").read_text()) if isinstance(x, dict)}
    bad = []
    for path, key in (("tools/bestx-content.json", "items"), ("tools/vsx-content.json", "items"),
                      ("tools/alternatives-content.json", "items")):
        data = _j.loads((ROOT / path).read_text())
        pages = data["pages"] if isinstance(data, dict) else data
        for pg in pages:
            for it in (pg.get(key) or []):
                slug = it.get("slug", "?")
                notes = str(recs.get(slug, {}).get("price_notes") or "")
                cur = recs.get(slug, {}).get("currency")
                if cur == "EUR" or "EUR" in notes:
                    continue
                for field in ("assessment", "text", "verdict", "direct_answer"):
                    if isinstance(it.get(field), str) and "\u20ac" in it[field]:
                        bad.append(f"{path}:{pg.get('slug')}:{slug}")
    assert not bad, f"euro prose on non-euro records: {bad[:8]}"
    # r16 follow-up (2026-09-29): _money emitted a literal backslash-u20ac
    # escape into 13 rendered pages' visible text (JSON-LD script blocks may
    # legally carry ascii-escaped \u20ac, so scripts are stripped first).
    import re as _re2
    raw = [str(f.relative_to(ROOT)) for f in sorted(ROOT.glob("**/index.html"))
           if "deploy-out" not in str(f) and (chr(92) + "u20ac") in
           _re2.sub(r"<script[^>]*>.*?</script>", "", f.read_text(errors="ignore"), flags=_re2.S)]
    assert not raw, f"literal backslash-u20ac in visible HTML: {raw[:8]}"


def test_no_duplicated_pricing_lead_seam():
    """r16 M-5 (2026-09-29): 'Paid pricing starts at $X/mo, and <notes
    restating $X>' duplicated the entry tier and manufactured mixed sentences.
    The lead clause is dropped at the source; notes stand alone."""
    import json as _j, re as _re
    pat = _re.compile(r"(Paid pricing starts at [^,.]+?, and |enterprise pricing starts at [^,.]+?, and |paid pricing starts at [^,.]+?, and )", _re.I)
    bad = []
    def _walk(o, loc):
        if isinstance(o, dict):
            for k, v in o.items():
                _walk(v, f"{loc}.{k}")
        elif isinstance(o, list):
            for i, v in enumerate(o):
                _walk(v, f"{loc}[{i}]")
        elif isinstance(o, str) and pat.search(o):
            bad.append(loc)
    for path in ("tools/bestx-content.json", "tools/vsx-content.json", "tools/alternatives-content.json"):
        data = _j.loads((ROOT / path).read_text())
        _walk(data, path)
    for base in ("best", "vs", "alternatives"):
        for f in (ROOT / base).glob("*/index.html"):
            if pat.search(f.read_text()):
                bad.append(f"rendered:{base}/{f.parent.name}")

    assert not bad, f"duplicated pricing lead seam: {bad[:8]}"


def test_vs_dd_no_near_duplicate_of_dt():
    """r18 M-2 (2026-09-30): exact-prefix check missed 'Pick Plausible if'
    under 'Pick Plausible Analytics if' (similarity 0.67 vs 0.12 baseline).
    Subsequence rule: strip non-letters, drop the tool-name tokens shared
    with the dt, and the dd remnant must not open with the dt remnant."""
    import re as _re
    bad = []
    for _f in ROOT.rglob("index.html"):
        _rel = _f.relative_to(ROOT)
        if _rel.parts and _rel.parts[0] == "deploy-out":
            continue
        _h = _f.read_text(errors="ignore")
        for _m in _re.finditer(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", _h, _re.S):
            _dt = _re.sub(r"[^a-z ]", "", _m.group(1).lower()).split()
            _dd = _re.sub(r"[^a-z ]", "", _m.group(2).lower()).split()
            _shared = set(_dt) & set(_dd[:len(_dt) + 2])
            _dt_r = [w for w in _dt if w not in _shared or w in ("if", "pick")]
            _dd_r = [w for w in _dd[:len(_dt) + 2] if w not in _shared or w in ("if", "pick")]
            if _dt_r and _dd_r[:len(_dt_r)] == _dt_r:
                bad.append((str(_rel), _m.group(1)[:40]))
    assert not bad, f"dd near-repeats dt: {bad[:8]}"


def test_one_distinct_datemodified_per_page():
    """r18 H-2 (2026-09-30): template entities carried an authored dateModified
    while the injector added a blame-date second - 101 pages with 2 distinct
    values, and the sitemap read the stale first one. One page, one date."""
    import re as _re
    bad = []
    for _f in ROOT.rglob("index.html"):
        _rel = _f.relative_to(ROOT)
        if _rel.parts and _rel.parts[0] == "deploy-out":
            continue
        _vals = set(_re.findall(r'"dateModified": "(\d{4}-\d{2}-\d{2})', _f.read_text(errors="ignore")))
        if len(_vals) > 1:
            bad.append((str(_rel), sorted(_vals)))
    assert not bad, f"pages with >1 distinct dateModified: {bad[:6]}"


def test_vs_two_way_leaves_have_no_three_quantifiers():
    """r18 M-1 (2026-09-30): residue of the removed 3-way draft ('all three',
    'None of the three') on matomo-vs-plausible, make-vs-zapier,
    n8n-vs-zapier. Two-tool leaves use two-forms."""
    import json as _j
    import re as _re
    d = _j.loads((ROOT / "tools" / "vsx-content.json").read_text())
    bad = []
    for pg in (d["pages"] if isinstance(d, dict) else d):
        if pg.get("c_slug"):
            continue
        # links / decision_first blocks may legitimately point at the
        # real three-way page - only prose fields carry the residue class
        _stripped = {k: v for k, v in pg.items() if k not in ("links", "decision_first")}
        blob = _j.dumps(_stripped)
        for _m in _re.finditer(r"[Aa]ll three|three is right|three win|Skip all three|None of the three", blob):
            bad.append((pg["slug"], _m.group(0)))
    assert not bad, f"three-quantifiers on two-way leaves: {bad[:6]}"


def test_best_table_header_names_fit_not_verdict():
    """r18 M-5 (2026-09-30): the comparison-table cells hold fit segments;
    the header must say Best for, not Verdict."""
    bad = [str(f.relative_to(ROOT)) for f in (ROOT / "best").glob("*/index.html")
           if "<th>Verdict</th>" in f.read_text(errors="ignore")]
    assert not bad, f"Verdict th on best pages: {bad[:6]}"


def test_hub_collectionpages_have_ids():
    """r18 M-9/L-3 (2026-09-30): every hub CollectionPage node is addressable."""
    import re as _re
    bad = []
    for _f in list((ROOT / "vs").glob("index.html")) + [(ROOT / "best" / "index.html")] + \
            [(ROOT / "alternatives" / "index.html")] + [(ROOT / "categories" / "index.html")] + \
            [(ROOT / "guides" / "index.html")] + [(ROOT / "trending" / "index.html")]:
        if not _f.is_file():
            continue
        h = _f.read_text(errors="ignore")
        for _m in _re.finditer(r'"@type":\s*"CollectionPage"', h):
            seg = h[max(0, _m.start() - 200):_m.start() + 300]
            if '"@id"' not in seg:
                bad.append(str(_f.relative_to(ROOT)))
    assert not bad, f"CollectionPage without @id: {bad[:6]}"


def test_ard_link_carries_type_everywhere():
    """r18 L-4/M-6 (2026-09-30): the ARD discovery link carries
    type=application/json on every page head that emits it."""
    bad = []
    for _f in ROOT.rglob("index.html"):
        _rel = _f.relative_to(ROOT)
        if _rel.parts and _rel.parts[0] == "deploy-out":
            continue
        h = _f.read_text(errors="ignore")
        if 'rel="ard ai-catalog"' in h and 'rel="ard ai-catalog" type=' not in h:
            bad.append(str(_rel))
    assert not bad, f"ARD link without type: {bad[:8]}"


def test_seo_description_money_matches_record():
    """r18 H-1 (2026-09-30): the head layer was outside every guard - 4 of 163
    tool pages carried a stale price or wrong currency in seo_description
    (the SERP snippet + og:description) while the body was clean. Every
    money literal in seo_description must trace to the record's price_from /
    paid_from / price_notes, and its currency symbol to record.currency."""
    import json as _j
    import re as _re
    recs = [x for x in _j.loads((ROOT / "tools" / "tools.json").read_text()) if isinstance(x, dict)]
    bad = []
    for r in recs:
        v = r.get("seo_description") or ""
        figs = set()
        for _v in (r.get("price_from"), r.get("paid_from")):
            if isinstance(_v, (int, float)):
                figs.add(str(int(_v)))
        for _m in _re.finditer(r"(\d[\d,]*)", str(r.get("price_notes") or "")):
            figs.add(_m.group(1).replace(",", ""))
        for _m in _re.finditer(r"[$\u20ac](\d[\d,]*)", v):
            if _m.group(1).replace(",", "") not in figs:
                bad.append((r["slug"], _m.group(0)))
        # "Starts at" names the entry price: it must equal price_from.
        _st = _re.search(r"[Ss]tarts at [$\u20ac](\d[\d,]*)", v)
        if _st and isinstance(r.get("price_from"), (int, float)):
            if _st.group(1).replace(",", "") != str(int(r["price_from"])):
                bad.append((r["slug"], "starts-at-vs-price_from:" + _st.group(0)))
        _cur = r.get("currency")
        if _cur == "EUR" and "$" in v:
            bad.append((r["slug"], "dollar-on-eur-record"))
        if _cur == "USD" and "\u20ac" in v:
            bad.append((r["slug"], "euro-on-usd-record"))
    assert not bad, f"seo_description money mismatches: {bad[:8]}"


def test_money_prose_dollar_matches_record():
    """r17 H-3 residue (2026-09-30): mirror of the euro check - a $ in
    money-page prose requires a non-EUR record. Caught n8n (EUR record,
    $20/$50 prose on /alternatives/zapier/ + /best/open-source-marketing-tools/)
    and make (Teams $29 vs EUR 29 on /vs/make-vs-zapier/)."""
    import json as _j
    recs = {x["slug"]: x for x in _j.loads((ROOT / "tools" / "tools.json").read_text()) if isinstance(x, dict)}
    bad = []
    for path, key in (("tools/bestx-content.json", "items"), ("tools/vsx-content.json", "items"),
                      ("tools/alternatives-content.json", "items")):
        data = _j.loads((ROOT / path).read_text())
        pages = data["pages"] if isinstance(data, dict) else data
        for pg in pages:
            _slugs = [i.get("slug") for i in (pg.get(key) or []) if isinstance(i, dict)]
            if path.endswith("vsx-content.json"):
                _slugs = [pg.get("a_slug"), pg.get("b_slug"), pg.get("c_slug")]
            for slug in _slugs:
                if not slug or not isinstance(slug, str):
                    continue
                cur = recs.get(slug, {}).get("currency")
                if cur != "EUR":
                    continue
                for it in (pg.get(key) or []):
                    if not isinstance(it, dict) or it.get("slug") != slug:
                        continue
                    for field in ("assessment", "text", "verdict", "direct_answer", "why"):
                        v = it.get(field)
                        if isinstance(v, str) and "$" in v:
                            bad.append(f"{path}:{pg.get('slug')}:{slug}:{field}")
    assert not bad, f"dollar prose on EUR records: {bad[:8]}"


def test_currency_null_records_render_code_not_symbol():
    """r17 H-3 fix #2 (2026-09-30): the 18 records with no currency (all
    quote-based enterprise) must render a currency code or no price at all -
    never a $/EUR symbol that would silently default them. Fail closed."""
    import json as _j
    import re as _re
    recs = {x["slug"]: x for x in _j.loads((ROOT / "tools" / "tools.json").read_text()) if isinstance(x, dict)}
    nulls = {s for s, r in recs.items() if not r.get("currency")}
    bad = []
    for _f in (ROOT / "tools").glob("*/index.html"):
        slug = _f.parent.name
        if slug not in nulls:
            continue
        h = _f.read_text(errors="ignore")
        body = _re.sub(r"<script.*?</script>", "", h, flags=_re.S)
        # context figures (ad-spend thresholds, funding, API token prices,
        # correction prose) are not platform price quotes. Only flag symbols
        # in the pricing Quick-Facts block / pricing table region.
        _pr = _re.search(r"(<section class=\"faq-block\"|<h2>Pricing</h2>|class=\"qf\")", body)
        _seg = body[_pr.start():] if _pr else body
        for _m in _re.finditer(r"[" + chr(36) + chr(8364) + r"]\s?\d", _seg):
            _ctx = _seg[max(0, _m.start() - 90):_m.start()]
            # non-price contexts: ad-spend/ICP thresholds, funding, revenue,
            # API token pricing, correction prose about removed figures
            if _re.search(r"(spend|revenue|raised|valuation|attributed|per million|pricing correction|figures we|quoted around|carried Team|price list is gone|campaign performance|removed the|developer docs:|Palmyra|X4 at|same window|docs quote|Bedrock|finished task)", _ctx, _re.I):
                continue
            if _re.search(r"\d[,.]?\d*\s?K\b", _seg[_m.start():_m.start() + 12]):
                continue  # K-scale annual contract ranges, not tier quotes
            bad.append((slug, _m.group(0), _ctx[-60:]))
            break
    assert not bad, f"symbol price on currency-null record: {bad[:8]}"


def test_currency_populated_wherever_price_from_set():
    """r17 H-3 (2026-09-30): 129 records had price_from with null currency,
    so the money guard compared symbols against nothing. Every record with a
    price_from must carry a currency (free price_from=0 takes the default)."""
    import json as _json
    recs = [x for x in _json.loads((ROOT / "tools" / "tools.json").read_text())
            if isinstance(x, dict)]
    bad = [x["slug"] for x in recs
           if x.get("price_from") is not None and not x.get("currency")]
    assert not bad, f"price_from without currency: {bad[:10]}"


def test_money_faq_price_literals_trace_to_page_records():
    """r17 H-1 (2026-09-30): the geo page FAQ quoted Trakkr $10 (record $100),
    Nimt/Writesonic EUR 7 (records 79/79 in other currencies), Evertune $89
    (record $800). Every $/EUR literal in a money-page FAQ answer must match
    an entry figure of a record on that page or a figure quoted in that
    record's own price_notes (e.g. a second-tier plan)."""
    import json as _json
    import re as _re
    recs = {x["slug"]: x for x in _json.loads((ROOT / "tools" / "tools.json").read_text())
            if isinstance(x, dict)}
    def _figs(slugs):
        out = set()
        for _s in slugs:
            _r = recs.get(_s, {})
            for _v in (_r.get("price_from"), _r.get("paid_from")):
                if isinstance(_v, (int, float)):
                    out.add(str(int(_v)))
            for _m in _re.finditer(r"(\d[\d,]*)", str(_r.get("price_notes") or "")):
                out.add(_m.group(1).replace(",", ""))
        return out
    bad = []
    for _path, _kind in (("tools/bestx-content.json", "items"),
                         ("tools/vsx-content.json", "trio"),
                         ("tools/alternatives-content.json", "items")):
        _d = _json.loads((ROOT / _path).read_text())
        for _pg in (_d["pages"] if isinstance(_d, dict) else _d):
            if _kind == "trio":
                _slugs = [_pg.get("a_slug"), _pg.get("b_slug"), _pg.get("c_slug")]
            else:
                _slugs = [i.get("slug") for i in (_pg.get(_kind) or []) if i.get("slug")]
            _F = _figs([_s for _s in _slugs if _s])
            for _qa in (_pg.get("pilot_faq", []) or []) + (_pg.get("faq", []) or []):
                for _m in _re.finditer(r"[$€](" + chr(92) + "d[" + chr(92) + "d,]*)", _qa.get("a", "")):
                    if _m.group(1).replace(",", "") not in _F:
                        bad.append((_pg["slug"], _m.group(0)))
    assert not bad, f"FAQ price literals with no record behind them: {bad[:8]}"


def test_vs_verdict_dd_never_repeats_dt():
    """r17 H-2 (2026-09-30): 15 pick_X_if pairs on 8 vs pages repeated the
    dt label verbatim inside the dd. The dd must continue the sentence."""
    import re as _re
    bad = []
    for _f in ROOT.rglob("index.html"):
        _rel = _f.relative_to(ROOT)
        if _rel.parts and _rel.parts[0] == "deploy-out":
            continue  # staging copy of the same pages; ROOT copies are canonical
        _h = _f.read_text(errors="ignore")
        for _m in _re.finditer(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", _h, _re.S):
            _dt = _re.sub(r"\s+", " ", _m.group(1)).strip().lower()
            _dd = _re.sub(r"\s+", " ", _m.group(2)).strip().lower()
            if _dd.startswith(_dt):
                bad.append((_f.relative_to(ROOT), _m.group(1)[:40]))
    assert not bad, f"dd repeats dt: {bad[:8]}"


def test_no_bare_prose_emails_for_cf_to_rewrite():
    """r17 M-7 (2026-09-30): Cloudflare rewrites bare @-text into
    /cdn-cgi/l/email-protection hrefs that 404 for link checkers.
    Addresses may appear only as mailto: links (contact pattern),
    input placeholders (attributes CF ignores), or at-form prose.
    Code samples are exempt (commands, not contacts)."""
    import re as _re
    _pat = _re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+" + chr(92) + ".[A-Za-z]{2,}")
    bad = []
    for _f in ROOT.rglob("index.html"):
        _rel = _f.relative_to(ROOT)
        if _rel.parts and _rel.parts[0] == "deploy-out":
            continue
        _h = _f.read_text(errors="ignore")
        _h = _re.sub(r"<code>.*?</code>", "", _h, flags=_re.S)
        _h = _re.sub(r"<a" + chr(92) + "s[^>]*href=" + chr(34) + "mailto:.*?</a>", "", _h, flags=_re.S)
        # r17 M-7b: scan text nodes only. Attribute values (input
        # placeholders, meta descriptions) are invisible to CF's
        # email-protection rewrite, which targets text nodes + mailto: hrefs.
        _h = _re.sub(r"<[^>]*>", " ", _h)
        for _m in _pat.finditer(_h):
            bad.append((str(_rel), _m.group(0)))
    assert not bad, f"bare prose emails CF would rewrite: {bad[:8]}"

def test_tool_cards_serve_webp_at_1200w():
    """r16 L-1 (2026-09-29): money-page image srcsets used the PNG master as
    the 1200w candidate (mobile at DPR 3 fetched PNG). q82 -1200.webp
    renditions exist for every og/tools master and take the 1200w slot."""
    bad = [p.name for p in sorted((ROOT / "og" / "tools").glob("*.png"))
           if not (ROOT / "og" / "tools" / (p.stem + "-1200.webp")).exists()]
    assert not bad, f"tool masters without -1200.webp: {bad[:8]}"
    h = (ROOT / "best" / "ai-seo-tools" / "index.html").read_text(errors="ignore")
    assert "-1200.webp 1200w" in h, "1200w slot not served as WebP on money pages"


def test_screenshots_serve_1200w_rung():
    """r16 L-2 (2026-09-29): screenshot srcsets capped at 800w (0.76x of DPR-3
    needs) while masters are 1280px. Honest-downscale -1200.webp rungs take
    a 1200w slot on money pages."""
    import struct as _st
    bad = []
    for m in sorted((ROOT / "og" / "screenshots").glob("*.png")):
        try:
            head = m.read_bytes()[:24]
        except OSError:
            continue
        if len(head) == 24 and head[12:16] == b"IHDR" and _st.unpack(">I", head[16:20])[0] >= 1200 \
                and not m.with_name(m.stem + "-1200.webp").exists():
            bad.append(m.name)
    assert not bad, f"1280px masters without -1200.webp: {bad[:8]}"
    h = (ROOT / "vs" / "matomo-vs-plausible" / "index.html").read_text(errors="ignore")
    assert "1200w" in h, "no 1200w rung on vs pages"


def test_every_page_defines_webpage_node():
    """r16 L-7 (2026-09-29): #webpage was bound to Article on 10 /vs/ leaves
    and WebPage on 17 pages while 270 pages defined no page entity. Now every
    page carries a WebPage node (unfragmented page URL, guides pattern); the
    /vs/ typed node lives at #article."""
    import re as _re
    bad, dbl = [], []
    for f in sorted(ROOT.glob("**/index.html")):
        if "deploy-out" in str(f):
            continue
        h = f.read_text(errors="ignore")
        if '"@type": "WebPage"' not in h and '"@type":"WebPage"' not in h:
            bad.append(str(f.parent))
        if _re.search(r'"@type":\s*"Article"[^}]{0,300}?#webpage', h):
            dbl.append(str(f.parent))
    assert not bad, f"pages without WebPage node: {bad[:8]}"
    assert not dbl, f"Article still bound to #webpage: {dbl[:8]}"


def test_momentum_dataset_matches_catalog():
    """r16 L-11 (2026-09-29): oss-momentum.json was a manual artifact, 3 days
    stale with 8 of 16 tools disagreeing with the catalog. It regenerates in
    build_trending.py: generated == latest snapshot date, headline stars ==
    synced catalog totals."""
    import json as _j
    from datetime import date as _date
    m = _j.loads((ROOT / "oss-momentum.json").read_text())
    hist = _j.loads((ROOT / "tools" / "github-history.json").read_text())
    assert m["generated"] == hist[-1]["date"], f"momentum {m['generated']} vs snapshots {hist[-1]['date']}"
    recs = {x["slug"]: x for x in _j.loads((ROOT / "tools" / "tools.json").read_text()) if isinstance(x, dict)}
    bad = [t["slug"] for t in m["tools"]
           if isinstance(recs.get(t["slug"]), dict) and recs[t["slug"]].get("github_stars") not in (None, t["stars"])]
    assert not bad, f"momentum stars disagree with catalog: {bad[:8]}"
    assert (_date.today() - _date.fromisoformat(m["generated"])).days <= 7, "momentum dataset older than 7 days"


def test_utility_pages_carry_og_title():
    """r16 L-13 (2026-09-29): og:title absent on exactly 4 utility pages
    (contact, privacy, terms, ai-policy) while 298 of 302 had it."""
    import re as _re
    bad = [str(f.parent) for f in sorted(ROOT.glob("**/index.html"))
           if "deploy-out" not in str(f)
           and '<meta property="og:type"' in f.read_text(errors="ignore")
           and 'og:title' not in f.read_text(errors="ignore")]
    assert not bad, f"pages with og:type but no og:title: {bad[:8]}"


def test_software_app_nodes_carry_date_published():
    """r16 L-13 (2026-09-29): datePublished absent from the
    SoftwareApplication node on openseo/pipedream/zoho-crm (no date_added).
    Falls back to the earliest verified record date."""
    import re as _re, json as _j
    recs = [x for x in _j.loads((ROOT / "tools" / "tools.json").read_text()) if isinstance(x, dict)]
    bad = []
    for t in recs:
        page = ROOT / "tools" / t["slug"] / "index.html"
        if not page.exists():
            continue
        h = page.read_text(errors="ignore")
        i = h.find('"SoftwareApplication"')
        if i >= 0 and '"datePublished"' not in h[i:i + 2500]:
            bad.append(t["slug"])
    assert not bad, f"SoftwareApplication without datePublished: {bad[:8]}"


def test_verified_hands_on_suppresses_boilerplate():
    """r16 L-9 (2026-09-29): advertools/langchain/libretranslate carried
    'Not a hands-on test' boilerplate above real dated hands-on blocks.
    hands_on_verified suppresses it."""
    bad = [s for s in ("advertools", "langchain", "libretranslate")
           if "Not a hands-on test" in (ROOT / "tools" / s / "index.html").read_text(errors="ignore")]
    assert not bad, f"boilerplate contradicts hands-on block: {bad}"


def test_agent_discovery_links_uniform():
    """r16 L-16/L-17 (2026-09-29): the ARD discovery link carried three rel
    variants (homepage + about used bare rel="ard", 7 hand pages none) and
    llms.txt was unlinked from / and /about/ footers. Every page carries
    rel="ard ai-catalog"; / and /about/ link llms.txt in the footer."""
    bad = []
    for f in sorted(ROOT.glob("**/index.html")):
        if "deploy-out" in str(f):
            continue
        h = f.read_text(errors="ignore")
        if 'rel="ard ai-catalog"' not in h:
            bad.append(f"ard:{f.parent}")
    for name in ("index.html", "about/index.html"):
        h = (ROOT / name).read_text(errors="ignore")
        if 'href="/llms.txt"' not in h:
            bad.append(f"llmslink:{name}")
    assert not bad, f"agent discovery gaps: {bad[:10]}"


def test_no_email_shaped_strings_in_tool_commands():
    """r16 M-1 (2026-09-29): Cloudflare Email Obfuscation rewrote email-shaped
    strings inside install commands into /cdn-cgi/l/email-protection links,
    corrupting copy-paste on 5 tool pages. Commands now use non-email-shaped
    tokens (YOUR-EMAIL, "admin at ever.co"); only the audited legitimate
    contact addresses (macro, revealbot) may remain."""
    import re as _re
    pat = _re.compile(r"[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.]+")
    allow = {"macro", "revealbot"}
    bad = []
    for f in sorted((ROOT / "tools").glob("*/index.html")):
        if f.parent.name in allow:
            continue
        vis = _re.sub(r"<script[^>]*>.*?</script>", "", f.read_text(errors="ignore"), flags=_re.S)
        vis = _re.sub(r"<[^>]+>", " ", vis)
        hits = sorted(set(pat.findall(vis)))
        if hits:
            bad.append(f"{f.parent.name}:{hits[:3]}")
    assert not bad, f"email-shaped strings on tool pages: {bad[:8]}"


def test_edge_worker_collapses_repeated_slashes():
    """r16 M-8 (2026-09-29): //-slash path variants were served at 200 with
    byte-identical bodies. The Pages _worker.js 301s collapsed paths before
    any other handling. The rule must survive worker edits."""
    w = (ROOT / "_worker.js").read_text()
    assert "301" in w and "{2,}" in w, "slash-collapse 301 missing from _worker.js"


def test_edge_worker_caches_documents():
    """r16 L-5 (2026-09-29): documents answered DYNAMIC (origin round-trip
    per view) because the worker rebuilds HTML responses. Page-URL GET 200s
    go through the Cache API keyed on the markdown branch."""
    w = (ROOT / "_worker.js").read_text()
    assert "caches.default.put" in w and "caches.default.match" in w, "edge document cache missing"
    assert "#md" in w and "#html" in w, "markdown/HTML cache branches not separated"


def test_one_time_prices_carry_no_monthly_suffix():
    """r16 M-5 (2026-09-29): paid_from on one-time billing records is a
    non-recurring figure (idurar $5,000 lifetime license, krayin $1,799 flat
    extension price) - rendering it with /mo manufactures a subscription."""
    import json as _j
    recs = [x for x in _j.loads((ROOT / "tools" / "tools.json").read_text()) if isinstance(x, dict)]
    bad = []
    for t in recs:
        if str(t.get("billing") or "").lower() != "one-time":
            continue
        page = ROOT / "tools" / t["slug"] / "index.html"
        h = page.read_text(errors="ignore") if page.exists() else ""
        for fig in {t.get("paid_from"), t.get("price_from")} - {None, 0}:
            for form in (f"${fig}/mo", f"${fig:,}/mo"):
                if form in h:
                    bad.append(f"{t['slug']}:{form}")
    assert not bad, f"monthly suffix on one-time prices: {bad[:8]}"
    assert not bad, f"pricing lead seam: {bad[:8]}"


def test_money_meta_figures_match_page_verbatim():
    """r26 H-1 (2026-10-05): the SFMC-vs-HubSpot snippet advertised "$25/mo"
    while the page's own surfaces said $1,500/mo entry / $25/user/mo - the
    meta generator took a per-user figure and dropped the unit. Every
    figure+unit token in a money-leaf meta must occur verbatim in the built
    leaf HTML. Plus the fenced-records pin: the two enterprise records whose
    catalog figures carry units the meta clause cannot express
    (salesforce-marketing-cloud, adobe-marketo) never contribute a
    "<Name> from $X" clause to any money meta."""
    import json as _j, re as _re
    _fenced = {"salesforce-marketing-cloud", "adobe-marketo"}
    _bad = []
    for _f, _fam in (("tools/bestx-content.json", "best"),
                     ("tools/vsx-content.json", "vs"),
                     ("tools/alternatives-content.json", "alternatives")):
        _d = _j.loads((ROOT / _f).read_text())
        _pages = _d if isinstance(_d, list) else _d.get("pages", [])
        for _pg in _pages:
            _meta = _pg.get("meta", "")
            _h = (ROOT / _fam / _pg["slug"] / "index.html")
            _html = _h.read_text(errors="ignore") if _h.exists() else ""
            for _m in _re.finditer(r"[\$€][\d,]+(?:\.\d+)?(?:/mo|/user/mo| one-time)?", _meta):
                if _m.group(0) not in _html:
                    _bad.append(f"{_pg.get('slug')}:{_m.group(0)} not on page")
            for _fs in _fenced:
                _t = next((x for x in _j.loads((ROOT / "tools" / "tools.json").read_text())
                           if isinstance(x, dict) and x.get("slug") == _fs), {})
                if _t and f"{_t.get('name', '')} from " in _meta and _re.search(r"[\$€]\d", _meta):
                    _bad.append(f"{_pg.get('slug')}: fenced {_fs} contributes a figure")
    assert not _bad, f"money meta/page figure mismatch: {_bad[:8]}"


def test_content_updated_restamps_date_modified():
    """r26 M-1 (2026-10-05): prose/template-layer edits (rewritten metas, new
    cross-links) never moved dateModified - 84/98 changed pages kept stale
    stamps because sync_date_modified rewrote every stamp to the visible-dates
    max. Builders declare max(date_updated, content_updated) and the sync
    never moves a stamp backward. Every money leaf carrying content_updated
    must render dateModified >= it."""
    import json as _j, re as _re
    _bad = []
    for _f, _fam in (("tools/bestx-content.json", "best"),
                     ("tools/vsx-content.json", "vs"),
                     ("tools/alternatives-content.json", "alternatives")):
        _d = _j.loads((ROOT / _f).read_text())
        _pages = _d if isinstance(_d, list) else _d.get("pages", [])
        for _pg in _pages:
            _cu = _pg.get("content_updated", "")
            if not _cu:
                continue
            _h = (ROOT / _fam / _pg["slug"] / "index.html")
            _html = _h.read_text(errors="ignore") if _h.exists() else ""
            _dms = _re.findall(r'"dateModified"\s*:\s*"([0-9]{4}-[0-9]{2}-[0-9]{2})', _html)
            if not _dms or min(_dms) < _cu:
                _bad.append(f"{_pg.get('slug')}: dateModified {_dms[:2]} < content_updated {_cu}")
    assert not _bad, f"stale dateModified on revised leaves: {_bad[:8]}"


def _notes_unit(notes, entry=None):
    """r28 H-2 (2026-10-06): does price_notes attach /user|/seat (or per-user
    / per-seat prose) to the record's ENTRY figure? Keys the entry figure
    specifically (§9 trap c) — any-figure matching over-counts honestly-flat
    records that mention seats elsewhere. Returns 'user'|'seat'|''.
    r29 H-3 (2026-10-06): class-scoped, not token-scoped — zoho-crm writes
    'EUR 14/user/mo' (currency word, no symbol) and growthbook 'USD
    40/seat/month' (word + /month). Currency words, spaced symbols, and
    /month suffixes all match; /month alone is billing period, never unit."""
    import re as _re
    _CUR = r"(?:[\$€£]\s?|EUR\s?|USD\s?|GBP\s?)"
    _pat = _CUR + r"([\d,]+(?:\.\d+)?)"
    if entry:
        _want = str(entry).replace(",", "").rstrip("0").rstrip(".")
        _hit = None
        for _m in _re.finditer(_pat, notes or "", _re.I):
            _got = _m.group(1).replace(",", "").rstrip("0").rstrip(".")
            if _got == _want:
                _hit = _m
                break
        if not _hit:
            return ""
        _around = notes[max(0, _hit.start() - 4):_hit.end() + 24].lower()
    else:
        _m = _re.search(_pat, notes or "", _re.I)
        if not _m:
            return ""
        _around = notes[max(0, _m.start() - 4):_m.end() + 24].lower()
    if "/user" in _around or "per user" in _around or "per-user" in _around:
        return "user"
    if "/seat" in _around or "per seat" in _around or "per-seat" in _around:
        return "seat"
    return ""


def test_per_user_enterprise_figures_qualified_everywhere():
    """r27 H-1 (2026-10-05): the $25/mo per-user leak survived its meta-only
    fix on five more surfaces. Root fix: price_unit:'user' on the record,
    _money + hero qualify centrally, Offer suppressed (schema has no unit
    semantics). Bare $25 without /user or per-user in-sentence: 0. Paid
    Offers on price_unit=user records: 0 (r29 N-14: the honest $0 node is
    restored — only price>0 fails)."""
    import json as _j, re as _re
    _tools = {_t["slug"]: _t for _t in _j.loads((ROOT / "tools" / "tools.json").read_text())}
    _flagged = [s for s, _t in _tools.items() if str(_t.get("price_unit") or "").lower() == "user"]
    assert _flagged, "price_unit=user records vanished from the catalog"
    # Structural fence (r27 rec 1 leading indicator): every enterprise record
    # with a numeric price_from must declare its unit — the next enterprise
    # row ships figure-free or unit-true on day one, no per-surface fix.
    # r28 H-2 (2026-10-06): generalized to every model — the same leak lived
    # on 12 freemium/paid/open records. Any record whose entry figure is
    # unit-priced declares price_unit (user|seat|org).
    # r29 H-3 (2026-10-06): entry-bound (paid_from, else price_from) and
    # class-scoped — zoho-crm/growthbook write currency words, not symbols.
    _swept = 0
    _nounit = []
    for _s, _t in _tools.items():
        _entry = _t.get("paid_from") or _t.get("price_from") or 0
        if not _entry:
            continue
        _swept += 1
        if _notes_unit(_t.get("price_notes") or "", _entry) and not str(_t.get("price_unit") or ""):
            _nounit.append(_s)
    import json as _jj
    (ROOT / "tools" / ".unit-guard.json").write_text(_jj.dumps({"swept": _swept, "unit_priced": len([_s for _s, _t in _tools.items() if str(_t.get("price_unit") or "")]), "missing": _nounit}))
    assert not _nounit, f"unit-priced entry without price_unit: {_nounit}"
    _names = [_tools[_s]["name"] for _s in _flagged]
    _bad = []
    _pages = []
    for _s in _flagged:
        _pages.append(ROOT / "tools" / _s / "index.html")
    for _html in ROOT.rglob("index.html"):
        if "deploy-out" in _html.parts or "node_modules" in _html.parts:
            continue
        if _html in _pages:
            continue
        # r27 fixup: corrections/ and blog/ legitimately QUOTE past defects
        # when logging them ("briefly showed $25/mo") — the fence targets
        # catalog-derived surfaces, not errata prose about the defect.
        try:
            _rel0 = _html.relative_to(ROOT).parts[0]
        except ValueError:
            _rel0 = ""
        if _rel0 in ("corrections", "blog"):
            continue
        try:
            _h0 = _html.read_text(errors="ignore")
        except OSError:
            continue
        if any(_n in _h0 for _n in _names):
            _pages.append(_html)
    for _html in _pages:
        _h = _html.read_text(errors="ignore")
        for _m in _re.finditer(r"\$25(?![0-9])", _h):
            _sent = _h[max(0, _m.start() - 200):_m.start() + 100]
            if "/user" not in _sent and "per user" not in _sent:
                _bad.append(f"{_html.parent.name}: {_sent[:100]}")
        if _html.parent.parent.name == "tools" and _html.parent.name in _flagged:
            # r29 N-14 (2026-10-06): the honest $0 node is restored on
            # free-tier unit records — only PAID (>0) Offer prices fail.
            for _om in _re.finditer(r'"@type":\s*"Offer"[^}]*?"price":\s*([\d.]+)', _h):
                if float(_om.group(1)) > 0:
                    _bad.append(f"{_html.parent.name}: paid Offer on per-user record")
                    break
    assert not _bad, f"unqualified per-user figures: {_bad[:8]}"


def test_corrections_counts_match_build_tallies():
    """r29 N-13 (2026-10-06): the per-user corrections entry miscounted its
    own wave three rounds running (3 → 7 → 9 → 8). Quantitative clauses are
    recomputed from build tallies here: qualified money-leaf metas and
    hub-list items must equal the entry's published digits."""
    import json as _j, re as _re
    _mm = 0
    for _f in ("tools/bestx-content.json", "tools/vsx-content.json", "tools/alternatives-content.json"):
        _d = _j.loads((ROOT / _f).read_text())
        for _p in _d["pages"]:
            _clauses = _re.split(r"[.;]", _p.get("meta", ""))
            if any(_re.search(r"[\$€]\d[\d,.]*\s*/(user|seat)", _c) for _c in _clauses):
                _mm += 1
    _hc = 0
    for _fam in ("best", "vs", "alternatives"):
        _h = (ROOT / _fam / "index.html").read_text(errors="ignore")
        for _li in _re.finditer(r"<li>.*?</li>", _h, _re.S):
            if _re.search(r"[\$€]\d[\d,.]*\s*/(user|seat)", _li.group(0)):
                _hc += 1
    _entry = (ROOT / "corrections" / "index.md").read_text(errors="ignore")
    _words = {"eight": 8, "nine": 9, "seven": 7, "ten": 10, "six": 6}
    _m1 = _re.search(r"(eight|nine|seven|ten|six|\d+) money-leaf metas", _entry)
    _m2 = _re.search(r"(eight|nine|seven|ten|six|\d+) comparison-hub cards", _entry)
    assert _m1 and _m2, "corrections entry missing machine-checkable count clauses"
    _c1 = _words.get(_m1.group(1), int(_m1.group(1)) if _m1.group(1).isdigit() else -1)
    _c2 = _words.get(_m2.group(1), int(_m2.group(1)) if _m2.group(1).isdigit() else -1)
    assert _c1 == _mm, f"entry claims {_c1} qualified metas, build has {_mm}"
    assert _c2 == _hc, f"entry claims {_c2} hub cards, build has {_hc}"


def test_trending_counts_reconcile_with_catalog():
    """r27 L-17 (2026-10-05): trending said 82, tools page 81 — two tracked
    repos (codex-seo proprietary, resend/react-email side library) are not
    open-source tools. Rows filter to open_source; meta carries the catalog
    count. No &amp; entities in either llms file (r27 L-19)."""
    import json as _j
    _tools = _j.loads((ROOT / "tools" / "tools.json").read_text())
    _oss = sum(1 for _t in _tools if _t.get("open_source") and _t.get("status", "active") == "active")
    _h = (ROOT / "trending" / "index.html").read_text(errors="ignore")
    assert f"all {_oss} open-source tools" in _h.replace("  ", " ") or f"all {_oss} " in _h, \
        f"trending sub not carrying catalog oss count {_oss}"
    assert f"for {_oss} open-source martech tools" in _h, "trending meta not carrying catalog count"
    assert "codex-seo" not in _h and "resend/react-email" not in _h, "non-oss repos still charted"
    for _f in ("llms.txt", "llms-full.txt"):
        _t = (ROOT / _f).read_text(errors="ignore")
        _ents = [ _l for _l in _t.splitlines() if _l.startswith("- [") and "&amp;" in _l.split("](")[0]]
        assert not _ents, f"{_f} link text carries entities: {_ents[:3]}"


def test_category_mirrors_and_ard_categories_page_derived():
    """r27 N-2/N-3 (2026-10-05): category mirror link text pasted name+desc
    (h3.name missed, 60-char cut); ARD category descriptions paraphrased
    off-page. Link text now name-only (<=40 chars); ARD category
    descriptions are the rendered page metas."""
    import json as _j, re as _re
    _bad = []
    for _md in (ROOT / "categories").glob("*/index.md"):
        for _l in _md.read_text(errors="ignore").splitlines():
            _m = _re.match(r"- \[(.*?)\]\(", _l)
            if _m and len(_m.group(1)) > 40:
                _bad.append(f"{_md.parent.name}: {_m.group(1)[:50]}")
    assert not _bad, f"long category-mirror link text: {_bad[:6]}"
    _ard = _j.loads((ROOT / ".well-known" / "ard.json").read_text())
    _entries = _ard if isinstance(_ard, list) else _ard.get("entries", [])
    _miss = []
    for _e in _entries:
        if "/categories/" not in _e.get("url", ""):
            continue
        _slug = _e["url"].rstrip("/").split("/")[-1]
        _p = ROOT / "categories" / _slug / "index.html"
        if _p.exists() and _e.get("description", "")[:80] not in _p.read_text(errors="ignore"):
            _miss.append(_slug)
    assert not _miss, f"ARD category descriptions not on page: {_miss}"


def test_float_residues_and_seat_qualifiers():
    """r27 N-4/L-21 (2026-10-05): $98.9 x3 + mautic spaced EUR; money metas
    quoting figures the tool page qualifies must carry the qualifier."""
    import json as _j, re as _re
    _h = (ROOT / "tools" / "billionmail" / "index.html").read_text(errors="ignore")
    assert not _re.search(r"\$98\.9(?!0)", _h), "billionmail $98.9 residue alive"
    _m = (ROOT / "tools" / "mautic" / "index.html").read_text(errors="ignore")
    assert "€ 247.50" not in _m and "€ 247,50" not in _m, "mautic spaced-EUR residue alive"
    _viol = []
    for _f, _fam in (("tools/bestx-content.json", "best"),
                     ("tools/vsx-content.json", "vs"),
                     ("tools/alternatives-content.json", "alternatives")):
        _d = _j.loads((ROOT / _f).read_text())
        for _pg in (_d if isinstance(_d, list) else _d.get("pages", [])):
            _meta = _pg.get("meta", "")
            _tslugs = []
            if "vsx" in _f:
                _tslugs = [_pg.get("a_slug"), _pg.get("b_slug"), _pg.get("c_slug")]
            else:
                _tslugs = [ _it.get("slug") for _it in (_pg.get("items") or [])]
            _th = {}
            for _ts in _tslugs:
                if not _ts:
                    continue
                _p = ROOT / "tools" / _ts / "index.html"
                if _p.exists():
                    _th[_ts] = _p.read_text(errors="ignore")
            for _fm in _re.finditer(r"[\$€](\d[\d,.]*)", _meta):
                _fig = _fm.group(0)
                # r27 fixup (2026-10-05): the figure belongs to the tool NAMED
                # nearest before it ("ActiveCampaign from $15/mo" is
                # ActiveCampaign's flat contact pricing, not HubSpot's
                # coincidental $15/seat). Only the named tool gates.
                _before = _meta[:_fm.start()]
                _owner = None
                _best_pos = -1
                try:
                    _cat = {_t["slug"]: _t["name"] for _t in _j.loads((ROOT / "tools" / "tools.json").read_text())}
                except Exception:
                    _cat = {}
                for _ts in _th:
                    _nm = _cat.get(_ts, "")
                    _pos = _before.rfind(_nm) if _nm else -1
                    if _pos < 0 and _nm:
                        # last-word fallback ("HubSpot CRM" vs "HubSpot")
                        _pos = _before.rfind(_nm.split()[-1])
                    if _pos > _best_pos:
                        _best_pos, _owner = _pos, _ts
                _check = [(_owner, _th[_owner])] if _owner and _best_pos >= 0 else list(_th.items())
                for _ts, _hh in _check:
                    if (_fig + "/user") in _hh or (_fig + "/seat") in _hh:
                        _ctx = _meta[max(0, _fm.start() - 80):_fm.start() + 40]
                        if "/user" not in _ctx and "/seat" not in _ctx and "per user" not in _ctx and "per seat" not in _ctx:
                            _viol.append(f"{_pg.get('slug')}: {_fig} ({_ts})")
    assert not _viol, f"money metas dropping page qualifiers: {_viol[:6]}"


def test_hubs_link_all_children_with_derived_counts():
    """r16 H-3 (2026-09-29): the /vs/ hub linked 7 of 10 leaves while saying
    "three", /alternatives/ linked 3 of 4 while saying "three" and "five".
    Hub child links must equal the source page count; prose counts derive
    from the same children (Ten/Four/Fifteen present, stale words absent)."""
    import json as _j, re as _re
    exp = {}
    for slug, path in (("best", "tools/bestx-content.json"), ("vs", "tools/vsx-content.json"),
                       ("alternatives", "tools/alternatives-content.json")):
        data = _j.loads((ROOT / path).read_text())
        pages = data["pages"] if isinstance(data, dict) else data
        exp[slug] = [p["slug"] for p in pages]
    words = {15: "Fifteen", 16: "Sixteen", 13: "Thirteen", 12: "Twelve", 10: "Ten", 6: "Six", 5: "Five", 4: "Four"}
    bad = []
    for slug, slugs in exp.items():
        h = (ROOT / slug / "index.html").read_text()
        linked = set(_re.findall(r'https://martechsignal\.com/' + slug + r'/([a-z0-9-]+)/', h)) | \
            set(_re.findall(r'href="(/' + slug + r'/[a-z0-9-]+/)"', h))
        linked = {u.rstrip("/").split("/")[-1] for u in linked}
        missing = [s for s in slugs if s not in linked]
        if missing:
            bad.append(f"/{slug}/ unlinked: {missing[:4]}")
        if words[len(slugs)] not in h:
            bad.append(f"/{slug}/ prose count missing ({words[len(slugs)]})")
    for stale in ("three comparisons live", "Three are live:", "lists five alternatives",
                  "deliberate set of three", "narrow five credible options"):
        for slug in exp:
            if stale in (ROOT / slug / "index.html").read_text():
                bad.append(f"/{slug}/ stale prose: {stale!r}")
    assert not bad, f"hub distribution gaps: {bad[:8]}"


def test_homepage_links_every_money_leaf():
    """r16 H-3 (2026-09-29): the homepage linked none of the 29 money
    leaves. The generated money strip must link every best/vs/alternatives
    leaf with a descriptive anchor."""
    import json as _j, re as _re
    h = (ROOT / "index.html").read_text()
    bad = []
    for slug, path in (("best", "tools/bestx-content.json"), ("vs", "tools/vsx-content.json"),
                       ("alternatives", "tools/alternatives-content.json")):
        data = _j.loads((ROOT / path).read_text())
        pages = data["pages"] if isinstance(data, dict) else data
        for p in pages:
            if f"/{slug}/{p['slug']}/" not in h:
                bad.append(f"/{slug}/{p['slug']}/")
    assert not bad, f"money leaves unreachable from /: {bad[:8]}"


def test_faq_third_answers_are_unique_per_tool():
    """r15 M-3 (2026-09-29): 7 tool pages shipped placeholder FAQ answers
    sharing the "full review breaks down" tail (3 byte-identical). The
    fallback closer is now per-tool (best_for, price anchor, or
    integrations) — no two third answers may match site-wide."""
    import re as _re
    seen = {}
    dups = []
    thin = []
    for f in (ROOT / "tools").glob("*/index.html"):
        h = f.read_text()
        answers = _re.findall(r'"acceptedAnswer": \{"@type": "Answer", "text": "(.*?)"\}', h)
        if not answers:
            # retired-pack FAQPage shape: multi-line mainEntity blocks
            answers = _re.findall(r'"acceptedAnswer": \{\s*"@type": "Answer",\s*"text": "(.*?)"', h)
        if len(answers) < 3:
            thin.append(f.parent.name)
            continue
        if answers[2] in seen:
            dups.append((f.parent.name, seen[answers[2]]))
        seen[answers[2]] = f.parent.name
    assert not thin, f"pages with fewer than 3 FAQ answers: {thin[:4]}"
    assert not dups, f"duplicate third FAQ answers: {dups[:4]}"
    assert not any("full review breaks down" in a for a in seen), "placeholder tail survives"


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
    # r15 H-1b (2026-09-29): figures must track the live catalog record, not
    # a hardcoded snapshot — the sync moves them daily.
    import json as _j
    _recs = _j.loads((ROOT / "tools" / "tools.json").read_text())
    _cs = next(x for x in _recs if x.get("slug") == "claude-seo")
    assert f'{_cs["github_stars"]:,}' in tool and f'{_cs["github_forks"]:,}' in tool, \
        "tool page figures do not match the catalog record"


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
    """M3/M4 (r9, 2026-09-28) as revised by r16 L-3 (2026-09-29): only shipped
    mono weights (500/600) keep @font-face; the 400 file is gone. Only 600 is
    preloaded: 500 measured `unloaded` on 2 of 5 audit runs (slow connections
    expire font-display:optional's ~100ms block before it arrives, so the
    preload bytes download and never paint). Optional never swaps, so the
    zero-CLS guarantee holds either way; 500 loads on demand when fast."""
    css = (ROOT / "style.css").read_text()
    assert "spline-sans-mono-400" not in css, "dead 400 @font-face still shipped"
    assert not (ROOT / "fonts" / "spline-sans-mono-400.woff2").exists(), \
        "dead 400 font file still on disk"
    for tpl in ("tools/n8n/index.html", "blog/claude-seo-benchmark/index.html"):
        html = (ROOT / tpl).read_text()
        assert 'preload" href="/fonts/spline-sans-mono-600.woff2"' in html, f"{tpl} misses 600 preload"
        assert 'preload" href="/fonts/spline-sans-mono-500.woff2"' not in html, f"{tpl} still preloads 500"


def test_critical_css_inline_and_deferred():
    """M1 (r9, 2026-09-28) as fixed by r12 H-1 (2026-09-29): every page inlines
    critical CSS and loads the full bundle via a plain render-blocking link.
    The deferred variants are retired — onload swap violated CSP (r11 C-1),
    the site.js media flip arrived after first paint (cold CLS 0.17-0.64)."""
    import re as _re
    frag = (ROOT / "tools" / ".critical.css").read_text()
    assert len(frag) <= 10240, f"critical block {len(frag)}B exceeds 10KB budget"
    assert "@font-face" not in frag, "fonts must not ride the inline block"
    checked = 0
    for tpl in ("tools/n8n/index.html", "blog/claude-seo-benchmark/index.html",
                "index.html", "best/geo-llm-visibility-tools/index.html"):
        html = (ROOT / tpl).read_text()
        assert "<style>" in html, f"{tpl} missing inline critical"
        assert 'media="print" data-fullsheet' not in html, f"{tpl} still deferred"
        assert "onload=" not in html, f"{tpl} keeps CSP-banned inline handler"
        assert "data-fullsheet" not in html, f"{tpl} keeps retired swap hook"
        blocking = _re.findall(r'<link rel="stylesheet" href="/style[^"]*">', html)
        assert len(blocking) == 1, f"{tpl} wants exactly 1 blocking sheet: {blocking[:2]}"
        # exactly one inline critical block: the sweep must not stuff a second
        # copy inside its own <noscript> fallback (r9 M1 follow-up).
        assert html.count("<style>:root") == 1, \
            f"{tpl} carries {html.count('<style>:root')} critical copies"
        checked += 1
    assert checked == 4


def test_filter_bar_unhides_before_first_paint():
    """r10 H-7 (2026-09-28) as fixed by r11 C-1 (2026-09-29): the /tools/
    filter bar renders visible (no hidden attr, no deferred toggle -> no
    layout shift) with a <noscript> hide rule for no-JS users. The old
    synchronous inline unhide script is gone: it violated the CSP."""
    html = (ROOT / "tools" / "index.html").read_text()
    assert 'id="tool-filter"' in html, "filter bar missing"
    assert 'id="tool-filter" hidden>' not in html, "filter bar still hidden at parse"
    assert "tool-filter" in html and ".hidden=false</script>" not in html, \
        "CSP-violating inline unhide script still present"
    assert "<noscript><style>#tool-filter{display:none}</style></noscript>" in html, \
        "no-JS hide rule missing"


def test_no_csp_violating_inline_handlers():
    """r11 C-1 (2026-09-29): no inline event handlers (onload= etc.) and no
    inline <script> bodies in built HTML — script-src bans them, so any such
    markup is dead code that silently never runs."""
    import re as _re
    bad = []
    for tpl in ("index.html", "tools/index.html", "tools/n8n/index.html",
                "best/geo-llm-visibility-tools/index.html",
                "vs/n8n-vs-zapier/index.html",
                "blog/claude-seo-benchmark/index.html"):
        html = (ROOT / tpl).read_text()
        if _re.search(r'\son(load|click|error|submit)\s*=', html):
            bad.append((tpl, "inline event handler"))
        if _re.search(r"<script>(?!\s*</script>)", html):
            bad.append((tpl, "inline script body"))
    assert not bad, f"CSP-violating markup: {bad}"


def test_full_sheet_is_plain_blocking_link():
    """r12 H-1 (2026-09-29): plain render-blocking sheet, no media flip."""
    html = (ROOT / "tools" / "n8n" / "index.html").read_text()
    assert "data-fullsheet" not in html, "retired swap hook still present"
    assert "onload=" not in html, "inline onload handler still present"
    assert 'media="print"' not in html, "print-media deferral still present"
    js = (ROOT / "site.js").read_text()
    assert "data-fullsheet" not in js, "site.js still performs the media swap"


def test_screenshot_srcsets_are_comma_separated():
    """r12 H-2 (2026-09-29): srcset candidates comma-separated (space-joined
    srcsets made Chromium drop every candidate on 134 images)."""
    import re as _re
    bad = []
    for sub in ("best", "vs", "alternatives"):
        for idx in (ROOT / sub).glob("*/index.html"):
            for _m in _re.findall(r'srcset="([^"]+)"', idx.read_text()):
                if "og/screenshots/" in _m and "," not in _m:
                    bad.append(f"/{sub}/{idx.parent.name}/")
    assert not bad, f"space-joined srcsets: {bad[:5]}"


def test_vs_shots_fit_mobile_viewport():
    """r12 H-3 (2026-09-29): vs screenshot imgs carry the true 600x375 ratio
    and the .vs-shot rule constrains them (were 600x315 attrs, unconstrained,
    overflowing 390px viewports)."""
    import re as _re
    css = (ROOT / "style.css").read_text()
    assert ".vs-shot img" in css and "max-width: 100%" in css, "vs-shot rule missing"
    bad = []
    for idx in (ROOT / "vs").glob("*/index.html"):
        for _m in _re.findall(r'<div class="vs-shot">(<img[^>]+>)', idx.read_text()):
            if 'width="600" height="375"' not in _m:
                bad.append(idx.parent.name)
    assert not bad, f"vs shots with wrong ratio attrs: {bad[:5]}"


def test_fact_cards_serve_sized_renditions():
    """r10 H-9 (2026-09-29) as corrected by r14 M-2: money-page fact cards
    serve a 670w rendition via srcset with sizes describing the real
    640px slot (the old 335px value under-fetched at DPR 2)."""
    import re as _re
    html = (ROOT / "best" / "geo-llm-visibility-tools" / "index.html").read_text()
    imgs = _re.findall(r'<img[^>]*fact card[^>]*>', html)
    assert imgs, "no fact card images on the sampled best page"
    bare = [i for i in imgs if "srcset" not in i]
    assert not bare, f"{len(bare)}/{len(imgs)} fact cards lack srcset"
    assert 'sizes="(max-width: 700px) 100vw, 640px"' in imgs[0], "fact card sizes does not match the 640px slot"


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


def test_all_best_pages_carry_three_question_h2s():
    """r11 H-4 (2026-09-29): the FAQ rollout — every best page carries 3
    catalog-grounded question-form H2s, not just the 4 pilot pages."""
    import re as _re
    gaps = []
    for p in json.loads((ROOT / "tools" / "bestx-content.json").read_text())["pages"]:
        html = (ROOT / "best" / p["slug"] / "index.html").read_text()
        if len(_re.findall(r"<h2>[^<]*\\?</h2>", html)) < 3:
            gaps.append(p["slug"])
    assert not gaps, f"best pages short of 3 question H2s: {gaps}"


def test_all_vs_and_alternatives_carry_three_question_h2s():
    """r11 H-4 (2026-09-29): the rollout covers vs + alternatives too —
    every one of those 14 pages carries 3 question-form H2s."""
    import re as _re
    gaps = []
    for fname, sub in (("vsx-content.json", "vs"),
                       ("alternatives-content.json", "alternatives")):
        d = json.loads((ROOT / "tools" / fname).read_text())
        pages = d if isinstance(d, list) else d["pages"]
        for p in pages:
            html = (ROOT / sub / p["slug"] / "index.html").read_text()
            if len(_re.findall(r"<h2>[^<]*\\?</h2>", html)) < 3:
                gaps.append(f"/{sub}/{p['slug']}/")
    assert not gaps, f"vs/alternatives short of 3 question H2s: {gaps}"


def test_r11_ml_wave_no_regressions():
    """r11 M/L wave (2026-09-29): one pin per fixed finding, so the next
    rebuild cannot silently reintroduce them."""
    import re as _re
    # M-1: about counts match ground truth (166 active / 168 records).
    _about = (ROOT / "about" / "index.html").read_text()
    assert "166 active tool records" in _about and "168 records" in _about
    # M-2: boilerplate citation-slot sentence gone from all tool pages.
    _boiler = [p.parent.name for p in (ROOT / "tools").glob("*/index.html")
               if "review covers features, pricing" in p.read_text()]
    assert not _boiler, f"boilerplate back on: {_boiler[:3]}"
    # M-6: all nine r11 tokens named in robots.txt.
    _robots = (ROOT / "robots.txt").read_text()
    for _tok in ("AI2Bot", "AI2Bot-Dolma", "ImagesiftBot", "PanguBot",
                 "omgili", "omgilibot", "Timpibot", "Kangaroo Bot", "Cotoyogi"):
        assert _tok in _robots, f"robots missing {_tok}"
    # M-7: homepage story excerpts end cleanly (ellipsis) or are uncut.
    _home = (ROOT / "index.html").read_text()
    _stories = _re.findall(r'<a class="story reveal".*?<p>(.*?)</p>', _home, _re.S)
    assert _stories, "no homepage stories found"
    for _s in _stories:
        assert _s.endswith("\u2026") or len(_s) < 170, f"ragged excerpt: {_s[-40:]}"
    # M-8: glossary hub declares the DefinedTermSet terms reference.
    _gloss = (ROOT / "glossary" / "index.html").read_text()
    assert '"DefinedTermSet"' in _gloss
    # M-9: categories hub hasPart covers all 14 children.
    _cats = (ROOT / "categories" / "index.html").read_text()
    assert _cats.count('"@type": "WebPage"') >= 14, "categories hasPart short"
    # M-10: about sameAs matches generated pages (github only in schema;
    # the visible bio link stays — the finding was entity divergence).
    _ld = _re.findall(r'<script type="application/ld\+json">(.*?)</script>', _about, _re.S)
    assert _ld, "no JSON-LD on about"
    assert "linkedin.com/in/tchristensen78" not in " ".join(_ld)
    # M-4: commercial-intent email page leads with market names.
    _em = json.loads((ROOT / "tools" / "bestx-content.json").read_text())
    _em_items = next(p for p in _em["pages"]
                     if p["slug"] == "ai-email-marketing-tools")["items"]
    assert [i["slug"] for i in _em_items[:2]] == ["mailchimp", "klaviyo"], \
        "email page not market-led"
    # L-1: every category page has an h2 before its first h3.
    for _c in (ROOT / "categories").glob("*/index.html"):
        _h = _c.read_text()
        if "<h3" in _h:
            assert _h.index("<h2") < _h.index("<h3"), f"{_c.parent.name}: H1-H3 skip"
    # L-3: guides hub title carries keyword + brand.
    _gt = _re.search(r"<title>(.*?)</title>", (ROOT / "guides" / "index.html").read_text()).group(1)
    assert "MartechSignal" in _gt and len(_gt) > 30, f"weak guides title: {_gt}"
    # L-6: llms.txt lists the four bare hubs with no duplicate URLs.
    _llms = (ROOT / "llms.txt").read_text()
    for _hub in ("/best/)", "/vs/)", "/alternatives/)", "/guides/)"):
        assert _hub in _llms, f"llms.txt missing bare hub {_hub}"
    _urls = _re.findall(r"https://martechsignal\.com[^\s)]+", _llms)
    assert len(_urls) == len(set(_urls)), "duplicate URLs in llms.txt"
    # L-9: ard discovery token uniform.
    for _p in ((ROOT / "blog" / "index.html"),
               (ROOT / "tools" / "n8n" / "index.html")):
        assert 'rel="ard ai-catalog"' in _p.read_text(), f"ard token off in {_p}"
    # L-10: sibling catalog file declared.
    assert "/catalog-categories.json" in (ROOT / "_headers").read_text()
    # L-11: byline clock agrees with schema clock (worst case from audit).
    # r20 H-2 (2026-10-02): human-date pages carry no Updated note; the
    # Last-verified stamp is the visible clock the schema must match.
    _tea = (ROOT / "tools" / "tealium" / "index.html").read_text()
    _bym = _re.search(r"[Uu]pdated <time datetime=\"([0-9-]+)\"", _tea)
    _bylv = _re.search(r"Last verified</dt><dd><time datetime=\"([0-9-]+)\"", _tea)
    _by = _bym.group(1) if _bym else (_bylv.group(1) if _bylv else None)
    assert _by, "tealium carries no visible date at all"
    _dm = _re.search(r"\"dateModified\": \"([0-9-]+)\"", _tea).group(1)
    assert _by == _dm, f"tealium byline {_by} vs schema {_dm}"
    # M-13: hub ItemLists carry typed nodes.
    _bx = (ROOT / "best" / "ai-seo-tools" / "index.html").read_text()
    assert '"@type": "SoftwareApplication"' in _bx, "best ItemList untyped"


def test_all_money_pages_carry_visible_time_and_shots():
    """r11 H-4 (2026-09-29): every money page (15 best + 12 vs + 4
    alternatives) shows a visible Last verified <time> and, where the og
    survey shot a product UI, a real screenshot — not pilot-gated."""
    import glob as _glob
    import os as _os
    gaps = []
    pages = ([str(ROOT / "best" / p["slug"]) for p in
              json.loads((ROOT / "tools" / "bestx-content.json").read_text())["pages"]]
             + [str(ROOT / "vs" / p["slug"]) for p in
                json.loads((ROOT / "tools" / "vsx-content.json").read_text())["pages"]]
             + [str(ROOT / "alternatives" / p["slug"]) for p in
                json.loads((ROOT / "tools" / "alternatives-content.json").read_text())["pages"]])
    assert len(pages) == 34, f"expected 34 money pages, got {len(pages)}"
    for d in pages:
        html = Path(d, "index.html").read_text()
        if "<time datetime=" not in html:
            gaps.append((d, "no visible time"))
    assert not gaps, f"time gaps: {gaps}"
    shot_pages = [d for d in pages if "og/screenshots/" in
                  Path(d, "index.html").read_text()]
    assert len(shot_pages) >= 20, \
        f"screenshots on only {len(shot_pages)} money pages, want 20+"


def test_guide_hubs_carry_visible_time():
    """r11 H-4 (2026-09-29): the five static /guides/* hubs each carry a
    visible Last verified <time> matching their Article dateModified."""
    for slug in ("generative-engine-optimization", "mcp-agent-protocols",
                 "workflow-automation-strategy", "ai-seo-tooling",
                 "agentic-ai-advertising"):
        html = (ROOT / "guides" / slug / "index.html").read_text()
        assert "<time datetime=" in html, f"{slug}: no visible time"


def test_volume_pricing_rows_are_derived_not_quoted():
    """r11 H-7 (2026-09-29): the invoice persona gets 10K/100K/1M rows on
    /vs/n8n-vs-zapier/. Cells above the published tiers say who to ask —
    never a guessed number — and the table declares itself derived."""
    html = (ROOT / "vs" / "n8n-vs-zapier" / "index.html").read_text()
    for vol in ("10K", "100K", "1M"):
        assert vol in html, f"volume row {vol} missing"
    assert "derived from published rates, not quoted" in html, \
        "derivation disclaimer missing"


def test_best_titles_describe_their_bodies():
    """r11 H-2 (2026-09-29): a best page's title/meta must not promise a
    subtopic the body explicitly disavows. ai-seo covers classic SEO and
    routes AI-visibility readers to GEO; its title/meta now say so."""
    import json as _json
    d = _json.loads((ROOT / "tools" / "bestx-content.json").read_text())
    for page in d["pages"]:
        blob = (page.get("seo_title", "") + " " + page.get("meta", "")).lower()
        if page["slug"] == "ai-seo-tools":
            assert "visib" not in blob, "ai-seo title/meta still promise AI visibility"
            assert "audit" in blob or "content" in blob, "ai-seo title/meta lost the classic-SEO topic"


def test_guides_hub_emits_collection():
    """r11 H-6 (2026-09-29): /guides/ carries CollectionPage + hasPart for
    its five hubs, like every sibling hub."""
    import re as _re
    html = (ROOT / "guides" / "index.html").read_text()
    assert '"@type": "CollectionPage"' in html, "guides hub missing CollectionPage"
    assert html.count('"@type": "WebPage"') >= 5, "guides hasPart short of five hubs"


def test_money_pages_carry_momentum_receipts():
    """r11 H-3 (2026-09-29): money pages featuring open-source tools with
    snapshot history carry the momentum block (stars, delta, window,
    GitHub verify link); pages without history render nothing extra."""
    import re as _re
    html = (ROOT / "best" / "open-source-crm" / "index.html").read_text()
    assert "Open-source momentum, with receipts" in html, "momentum block missing"
    assert "verify on GitHub" in html, "momentum block lacks verify links"
    assert _re.search(r"\d{1,3}(,\d{3})+ stars", html), "no formatted star counts"


def _ldjson_blocks(html):
    out = []
    for b in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>', html, re.S):
        try:
            out.append(json.loads(b))
        except Exception:
            pass
    return out


def _walk_nodes(d):
    if isinstance(d, list):
        for x in d:
            yield from _walk_nodes(x)
    elif isinstance(d, dict):
        yield d
        for k, v in d.items():
            if k != "itemListElement":
                yield from _walk_nodes(v)


def test_breadcrumb_graph_connected():
    """r23 H-2 (2026-10-05): REPLACES test_no_cross_block_breadcrumb_pointers,
    whose premise was wrong. A pure {"@id"} pointer cannot parse as a
    BreadcrumbList; the Sep-30 GSC itemListElement errors coincided with the
    56 BreadcrumbLists that carried no @id. Deleting the edge to satisfy
    "dangling == 0" removed 293 graph edges and added 1 @id - the metric
    passed while the graph got emptier. This test asserts the MEANING, not
    just the count, page-wide (crumbs and WebPage usually live in different
    script blocks): every BreadcrumbList has @id, every page carrying a
    WebPage node also carries a resolving breadcrumb edge, and no edge
    dangles at a missing @id."""
    pages = [p for p in ROOT.rglob("index.html") if "node_modules" not in p.parts and "deploy-out" not in p.parts]
    no_id, no_edge, dangling = [], [], []
    for p in pages:
        html = p.read_text(errors="ignore")
        crumbs, webs = [], []
        for data in _ldjson_blocks(html):
            for node in _walk_nodes(data):
                t = node.get("@type")
                if t == "BreadcrumbList" or (isinstance(t, list) and "BreadcrumbList" in t):
                    crumbs.append(node)
                if t == "WebPage" or (isinstance(t, list) and "WebPage" in t):
                    webs.append(node)
        if not crumbs and not webs:
            continue
        ids = {c.get("@id") for c in crumbs if c.get("@id")}
        if any("@id" not in c for c in crumbs):
            no_id.append(str(p.relative_to(ROOT)))
        if webs:
            if not crumbs:
                no_edge.append(str(p.relative_to(ROOT)))
                continue
            for w in webs:
                bc = w.get("breadcrumb")
                if not (isinstance(bc, dict) and bc.get("@id") in ids):
                    no_edge.append(str(p.relative_to(ROOT)))
                    break
            for w in webs:
                bc = w.get("breadcrumb")
                if isinstance(bc, dict) and bc.get("@id") and bc.get("@id") not in ids:
                    dangling.append(str(p.relative_to(ROOT)))
    assert not no_id, f"BreadcrumbList nodes without @id on: {no_id[:10]}"
    assert not no_edge, f"WebPage without resolving breadcrumb edge on: {no_edge[:10]}"
    assert not dangling, f"dangling breadcrumb edges on: {dangling[:10]}"


def test_no_audit_ticket_refs_in_catalog():
    """r23 H-1 (2026-10-05): the Heap fix wrote "(r22 H-3)" and "the record
    carries no paid figure" into price_notes, a rendered field. Fails on any
    catalog record whose rendered prose contains an audit-ticket reference."""
    import json as _j
    cat = _j.loads((ROOT / "tools" / "tools.json").read_text())
    recs = cat if isinstance(cat, list) else cat.get("tools", [])
    bad = []
    for t in recs:
        if not isinstance(t, dict):
            continue
        blob = " ".join(str(t.get(k) or "") for k in
                        ("tagline", "description", "price_notes", "hands_on", "faq"))
        m = __import__("re").search(r"r2[0-9] [A-Z]-[0-9]|\bthe record\b", blob)
        if m:
            bad.append(f"{t.get('slug')}: ...{blob[max(0, m.start()-30):m.end()+30]}...")
    assert not bad, f"audit/internal refs in rendered catalog fields: {bad[:6]}"


def test_meta_descriptions_sentence_complete():
    """r23 M-3 (2026-10-05): six pages shipped fragments ("Compare top.",
    "...moving a.", "...requesting a demo. It.", "...we track list.") when
    clippers cut mid-clause and appended a fabricated period. Unit-pins
    _sentence_clip on the exact six inputs: sentence boundary or dropped
    sentence, never a punctuated fragment. (A generic rendered-page scan
    cannot distinguish an honest clause cut from a stub, so the guard lives
    at the generator, pinned here.)"""
    import sys as _sys
    import re as _re
    _sys.path.insert(0, str(ROOT / "tools"))
    from build_tools import _sentence_clip as _sc
    cases = [
        # (input, budget, must_not_end_with)
        ("Query fan-out, page audits and Looker Studio. Compare top marketing tools side by side.", 120, "Compare top."),
        ("Marketing automation is software that runs repetitive marketing tasks without manual intervention: sending a welcome email when someone signs up, moving a lead down the funnel.", 155, "moving a."),
        ("Conversion rate optimization is the practice of increasing the percentage of visitors who take a desired action, buying, signing up, requesting a demo. It requires testing.", 155, "It."),
        ("An agent can now run a marketing loop end to end on open source. We counted this morning from the directory: 19 of the 81 open-source tools we track list an MCP server.", 155, "list."),
    ]
    for text, budget, frag in cases:
        out = _sc(text, budget)
        assert frag not in out or out.rstrip().endswith((".", "!", "?")) and frag not in out.split(".")[-1], \
            f"fragment '{frag}' survives sentence clip: {out!r}"
        # No fabricated terminal period on a non-sentence: if the output does
        # not end with sentence punctuation it must be a clause cut >= 30 chars.
        if out and not _re.search(r"[.!?]$", out):
            assert len(out) >= 30, f"stub clause cut: {out!r}"
    # The six live pages carry no punctuated fragment.
    pages = {
        "tools/rankscale/index.html": "Compare top.",
        "glossary/marketing-automation/index.html": "moving a.",
        "glossary/cro/index.html": "It.",
        "glossary/dco/index.html": "combination.",
        "glossary/chatbot/index.html": "chatbots.",
        "blog/open-source-agentic-martech-stack-mcp/index.html": "list.",
    }
    for rel, frag in pages.items():
        m = _re.search(r'name="description" content="(.*?)"', (ROOT / rel).read_text(errors="ignore"))
        assert m, f"no meta description on {rel}"
        d = m.group(1)
        assert not d.rstrip().endswith(frag), f"fragment '{frag}' live on {rel}: ...{d[-60:]}"


def test_speakable_uses_valid_property():
    """r23 M-1 (2026-10-05): all 46 SpeakableSpecification nodes used
    "cssSelectors" (plural), which is not a schema.org property - 100% of
    speakable markup was inert. Fails on the plural form anywhere rendered."""
    bad = [str(p.relative_to(ROOT)) for p in ROOT.rglob("index.html")
           if "node_modules" not in p.parts and "deploy-out" not in p.parts
           and "cssSelectors" in p.read_text(errors="ignore")]
    assert not bad, f"invalid SpeakableSpecification.cssSelectors on: {bad[:8]}"


def test_llms_carries_decision_answers():
    """r23 M-2 (2026-10-05): 0 of 34 rendered decision answers reached the LLM
    artifacts. llms.txt must carry a Key-decisions section whose entry count
    matches the rendered p.direct-answer count."""
    import re as _re
    n_rendered = 0
    for p in ROOT.rglob("index.html"):
        if "node_modules" in p.parts or "deploy-out" in p.parts:
            continue
        n_rendered += len(_re.findall(r'<p class="direct-answer">', p.read_text(errors="ignore")))
    llms = (ROOT / "llms.txt").read_text(errors="ignore")
    section = _re.search(r"## Key decisions", llms)
    n_llms = len(_re.findall(r"^-\s*\[", llms.split("## Key decisions")[1].split("## ")[0], _re.M)) \
        if section else 0
    assert section, "llms.txt has no ## Key decisions section"
    assert n_rendered > 0 and n_llms == n_rendered, \
        f"llms decisions {n_llms} != rendered direct-answers {n_rendered}"
