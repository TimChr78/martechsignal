"""Test suite for build_tools.py — the martechsignal.com static site generator.

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
        assert len(tools) > 50, f"Only {len(tools)} tools — data may be truncated"

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
        for c in cats:
            html = read_page(f"categories/{c['slug']}/index.html")
            m = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
            assert m, f"No schema in category '{c['slug']}'"
            schema = json.loads(m.group(1))
            assert schema["@type"] == "ItemList"
            # open-source is a meta-category: counts ALL active OSS tools
            if c["slug"] == "open-source":
                expected_count = len([t for t in active_tools if t.get("open_source")])
            else:
                expected_count = len([t for t in active_tools if t["category"] == c["slug"]])
            assert schema["numberOfItems"] == expected_count, \
                f"Category '{c['slug']}': schema says {schema['numberOfItems']}, expected {expected_count}"


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
