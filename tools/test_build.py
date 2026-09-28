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
