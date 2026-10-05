#!/usr/bin/env python3
"""A-3 (v2.4.0 audit): build the ARD manifest (Agentic Resource Discovery, spec 1.0).

Emits /.well-known/ard.json (canonical) and /.well-known/ai-catalog.json
(predecessor name, kept as a courtesy copy per spec §5.1).

Entry shape (spec §4.2): identifier (urn:air:<publisher>:<namespace>:<name>,
Appendix C), displayName, type (IANA media type), exactly one of url/data,
SHOULD carry 2-5 representativeQueries.

Validate before deploying (audit: a schema-ERRORING catalog flips Lighthouse's
ard-schema audit from N/A into a counted failure):
    uv run --with jsonschema python tools/build_ard.py --validate
"""
import html as _html
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS_JSON = ROOT / "tools" / "tools.json"
CATS_JSON = ROOT / "tools" / "categories.json"
OUT_DIR = ROOT / ".well-known"
PUBLISHER = "martechsignal.com"


def tool_queries(t):
    """2-5 queries this page genuinely answers (spec: the discovery signal)."""
    name = t["name"]
    q = [f"{name} pricing", f"{name} alternatives"]
    if t.get("open_source"):
        q.insert(0, f"open source {name.lower()}")
    if t.get("category"):
        q.append(f"{t['category'].replace('-', ' ')} tools like {name}")
    return q[:5]


def cat_queries(c):
    n = c["name"].lower()
    return [f"best {n} tools", f"{n} comparison", f"{n} software"]


def _page_meta(rel):
    """r27 N-3 (2026-10-05): rendered page meta description for ARD entries —
    page bytes by construction. Returns "" when the page is missing."""
    import re as _re2
    _f = ROOT / rel / "index.html"
    if not _f.exists():
        return ""
    _m = _re2.search(r'name="description" content="(.*?)"', _f.read_text(errors="ignore"))
    if not _m:
        return ""
    return _html.unescape(_m.group(1))


def build():
    tools = [t for t in json.loads(TOOLS_JSON.read_text())
             if t.get("status", "active") == "active"]
    cats = json.loads(CATS_JSON.read_text())
    entries = []
    for t in sorted(tools, key=lambda x: x["slug"]):
        entries.append({
            "identifier": f"urn:air:{PUBLISHER}:tools:{t['slug']}",
            "displayName": f"{t['name']} pricing & plans",
            "type": "text/html",
            "url": f"https://martechsignal.com/tools/{t['slug']}/",
            "description": (t.get("tagline") or "")[:200],
            "representativeQueries": tool_queries(t),
        })
    for c in sorted(cats, key=lambda x: x["slug"]):
        entries.append({
            "identifier": f"urn:air:{PUBLISHER}:categories:{c['slug']}",
            "displayName": c["name"],
            "type": "text/html",
            "url": f"https://martechsignal.com/categories/{c['slug']}/",
            # r27 N-3 (2026-10-05): categories.json blurbs ("Ad creation,
            # bidding, and campaign management") appear nowhere on the page
            # (4/15 first-80-char match). Use the rendered page meta, which
            # is page bytes by construction; fall back to the blurb.
            "description": (_page_meta(f"categories/{c['slug']}") or c.get("description") or "")[:200],
            "representativeQueries": cat_queries(c),
        })
    # r15 L-7 (2026-09-29): the shipped manifest held only the 2 catalog
    # files (text/html entries are filtered below per r8 H11). The real agent
    # discovery surfaces are the llms.txt files — list them as text/plain
    # entries so the manifest is genuinely useful while staying schema-valid
    # (deploy runs --validate; text/html filtering is untouched).
    for fname, dname, desc, qs in (
        ("llms.txt", "MartechSignal llms.txt (agent site map)",
         "Agent-readable map of the whole site: tools, comparisons, guides, posts",
         ["martechsignal site map for ai agents", "all martechsignal pages list",
          "ai marketing tools directory overview"]),
        ("llms-full.txt", "MartechSignal llms-full.txt (full tool descriptions)",
         "Full catalog descriptions, price labels, and license flags for every active tool",
         ["martechsignal full tool descriptions", "every martechsignal tool with pricing"]),
    ):
        entries.append({
            "identifier": f"urn:air:{PUBLISHER}:data:{fname.replace('.', '-')}",
            "displayName": dname,
            "type": "text/plain",
            "url": f"https://martechsignal.com/{fname}",
            "description": desc,
            "representativeQueries": qs,
        })
    # Machine-readable data sources (url reference, value-or-reference §4.3).
    # Served as root catalog-*.json (llms-full.txt siblings): /data/ is correctly
    # closed by .assetsignore (pipeline state), so manifest urls must not point there.
    for fname, qs in (("tools.json", ["martechsignal tool catalog data",
                                      "ai marketing tools dataset with pricing"]),
                      ("categories.json", ["martechsignal category taxonomy",
                                           "martech tool categories list"])):
        entries.append({
            "identifier": f"urn:air:{PUBLISHER}:data:{fname.replace('.', '-')}",
            "displayName": f"MartechSignal {fname} (machine-readable)",
            # r18 M-3 (2026-09-30): these files are plain JSON data, not
            # ARD catalogs (no specVersion/entries). Label them honestly;
            # the M16 Lighthouse deduction is cheaper than a false type.
            "type": "application/json",
            "url": f"https://martechsignal.com/catalog-{fname}",
            # r16 M-4 (2026-09-29): the two catalog entries carried
            # byte-identical representativeQueries. Disambiguated per file.
            "representativeQueries": qs,
        })
    # A3 H-5 (2026-09-26): walk the built tree so every published page has an
    # entry. The v240c audit found 92 URLs missing (blog posts, glossary terms,
    # the best/vs/alternatives listicles, core pages). Discovering from the
    # rendered pages keeps the manifest honest as the site grows.
    import re as _re

    def _page_info(index_path):
        html = index_path.read_text()
        m = _re.search(r"<title>([^<]+)</title>", html)
        title = (m.group(1) if m else index_path.parent.name).strip()
        title = _re.sub(r"\s*[|\u00b7]\s*MarTechSignal.*$", "", title, flags=_re.I).strip() or title
        # r25 L-25 (2026-10-05): unescape entities - an agent consuming the
        # JSON saw "Advertising &amp; Paid Media", not the character.
        title = _html.unescape(title)
        d = _re.search(r'<meta name="description" content="([^"]{0,200})"', html)
        return title, (_html.unescape(d.group(1)) if d else "")

    def _queries(kind, words, title):
        if kind == "glossary":
            return [f"what is {words}", f"{words} definition", f"{words} in martech"]
        if kind == "vs":
            return [title.lower(), words + " comparison"]
        if kind == "alternatives":
            return [title.lower(), words + " alternatives"]
        if kind == "best":
            return [title.lower(), words + " pricing comparison"]
        if kind == "guides":
            return [title.lower(), words + " guide"]
        return [title.lower(), words]

    def _walk(kind, folder, ns, extra_q=None):
        base = ROOT / folder
        if not base.is_dir():
            return
        for index_path in sorted(base.glob("*/index.html")):
            slug = index_path.parent.name
            title, desc = _page_info(index_path)
            words = " ".join(slug.split("-"))
            qs = _queries(kind, words, title)
            entries.append({
                "identifier": f"urn:air:{PUBLISHER}:{ns}:{slug}",
                "displayName": title,
                "type": "text/html",
                "url": f"https://martechsignal.com/{folder}/{slug}/",
                "description": desc,
                "representativeQueries": qs[:5],
            })

    _walk("blog", "blog", "blog")
    _walk("glossary", "glossary", "glossary")
    _walk("best", "best", "best")
    _walk("vs", "vs", "vs")
    _walk("alternatives", "alternatives", "alternatives")
    # r25 M-2 (2026-10-05): guides was the only money family with no ARD
    # entry - 0/5 leaves covered four rounds running.
    _walk("guides", "guides", "guides")

    # Core hand pages (always present, curated queries).
    core = {
        "about": (["about martechsignal", "who runs martechsignal"],
                  "Who is behind MartechSignal and how the catalog is researched"),
        "methodology": (["martechsignal methodology", "how martechsignal verifies tools",
                         "tool verification process"],
                        "How every tool page is researched, dated, and priced"),
        "checklist": (["ai marketing tool checklist", "martech tool selection checklist"],
                      "A field checklist for choosing AI marketing tools"),
        "ai-policy": (["martechsignal ai policy", "llm usage policy site"],
                      "Content policy for AI systems: citation, grounding, and training"),
        "corrections": (["martechsignal corrections", "site errata"], "Published corrections"),
        "authors": (["martechsignal authors", "who writes martechsignal"], "Author hub",
                    "https://martechsignal.com/authors/tim-christensen/"),
        "privacy": (["martechsignal privacy policy", "martechsignal data handling"], "Privacy policy"),
        "terms": (["martechsignal terms of service", "martechsignal usage terms"], "Terms of service"),
        # r25 M-2 (2026-10-05): the eight hubs plus contact/trending had no
        # entry - descriptions fall back to each hub's own meta via _page_info.
        "tools": (["martechsignal tool directory", "all ai marketing tools"], "Tool directory"),
        "categories": (["martechsignal categories", "browse tools by category"], "Categories"),
        "guides": (["martechsignal guides", "how-to guides"], "Guides hub"),
        "blog": (["martechsignal blog", "marketing teardown blog"], "Blog"),
        "glossary": (["martechsignal glossary", "marketing term definitions"], "Glossary"),
        "trending": (["trending martech tools", "what tools trend on github"], "Trending"),
        "contact": (["contact martechsignal"], "Contact"),
        "best": (["best ai marketing tools", "top picks by category"], "Best-tools hub"),
        "vs": (["tool comparisons", "x vs y"], "Comparisons hub"),
        "alternatives": (["tool alternatives", "x alternatives"], "Alternatives hub"),
    }
    # r25 M-2: the root URL itself had no entry.
    if (ROOT / "index.html").exists():
        _rt, _rd = _page_info(ROOT / "index.html")
        entries.append({
            "identifier": f"urn:air:{PUBLISHER}:pages:home",
            "displayName": _rt,
            "type": "text/html",
            "url": "https://martechsignal.com/",
            "description": _rd or "Independent reviews of AI marketing tools: pricing, AI features, verdicts.",
            "representativeQueries": ["martechsignal", "ai marketing tool reviews"],
        })
    for slug, core_val in core.items():
        qs, desc = core_val[0], core_val[1]
        # r24 L-15 (2026-10-05): an entry may carry an explicit URL when the
        # slug path is not the canonical page (/authors/ 301s to the person).
        _url = core_val[2] if len(core_val) > 2 else f"https://martechsignal.com/{slug}/"
        p = ROOT / slug / "index.html"
        if p.exists():
            title, pdesc = _page_info(p)
            entries.append({
                "identifier": f"urn:air:{PUBLISHER}:pages:{slug}",
                "displayName": title,
                "type": "text/html",
                "url": _url,
                "description": pdesc or desc,
                "representativeQueries": qs[:5],
            })

    # M11 (2026-09-27): spec 1.0 root = specVersion/host/entries only (the pinned
    # schema rejects additional properties at path 'root'). The publisher identity
    # and trustManifest are preserved in ARD_TRUST below and published as the side
    # file /.well-known/ard-trust.json (the AGTP binding carries trustManifest, not
    # the manifest root; removed from root per the official ard-spec schema).
    manifest = {
        "specVersion": "1.0",
        # r7 H7 (2026-09-28): ARD schema requires host to be an object with
        # displayName (a bare string fails Lighthouse ard-schema validation).
        # r8 H11 (2026-09-28): `host` is not permitted by ard-entry.schema.json
        # (the only Lighthouse ard-schema error), and a text/html page is not an
        # agent-discoverable resource - pages are covered by llms.txt + the mirrors.
        "entries": entries,
    }
    return manifest


def validate(manifest):
    """Validate against the authoritative schema (ard-entry.schema.json)."""
    import urllib.request
    schema_url = ("https://raw.githubusercontent.com/ards-project/ard-spec/main/"
                  "spec/schemas/ard-entry.schema.json")
    schema = json.loads(urllib.request.urlopen(schema_url, timeout=30).read())
    from jsonschema import Draft202012Validator
    v = Draft202012Validator(schema)
    errs = sorted(v.iter_errors(manifest), key=lambda e: e.path)
    # The schema defines ArdEntry/ArdManifest as $defs; validate via the manifest def
    defs = schema.get("$defs") or schema.get("definitions") or {}
    target = None
    for name in ("ArdManifest", "ardManifest", "ArdEntry"):
        if name in defs:
            target = {**schema, "$ref": f"#/$defs/{name}" if "$defs" in schema else f"#/definitions/{name}"}
            break
    if target:
        errs = sorted(Draft202012Validator(target).iter_errors(manifest),
                      key=lambda e: list(e.absolute_path))
    if errs:
        for e in errs[:10]:
            print("SCHEMA ERROR:", list(e.absolute_path), e.message[:160])
        return False
    # Discovery constraints (§D.2): URN format + query sizing (warnings only)
    warn = 0
    for e in manifest["entries"]:
        ident = e["identifier"]
        parts = ident.split(":")
        if not (ident.startswith("urn:air:") and len(parts) >= 5):
            print("WARN urn format:", ident); warn += 1
        rq = e.get("representativeQueries", [])
        if not 2 <= len(rq) <= 5:
            print("WARN queries count:", ident, len(rq)); warn += 1
        if ("url" in e) == ("data" in e):
            print("WARN value-or-reference:", ident); warn += 1
    print(f"VALID: {len(manifest['entries'])} entries, {warn} warnings")
    return True


if __name__ == "__main__":
    m = build()
    if "--validate" in sys.argv:
        if not validate(m):
            sys.exit(1)
    OUT_DIR.mkdir(exist_ok=True)
    text = json.dumps(m, ensure_ascii=False, indent=1)
    (OUT_DIR / "ard.json").write_text(text)

    (ROOT / ".well-known" / "ard-trust.json").write_text(json.dumps({

        "publisher": f"https://{PUBLISHER}/",

        "trustManifest": {"identity": f"https://{PUBLISHER}/about/"},

    }, indent=2))
    (OUT_DIR / "ai-catalog.json").write_text(text)  # predecessor courtesy copy
    # the two data-entry urls must resolve (root copies; /data/ stays private)
    # M14/M15 (r9, 2026-09-28): the feed ships as a dataset envelope, not a
    # bare array - generated/license/recordCount up front, per-record page_url
    # (nullable; acquired records carry successor_slug instead).
    _recs = json.loads(TOOLS_JSON.read_text())
    _succ = {"autopilot": "ortto", "drift": "salesloft"}
    for _r in _recs:
        _s = _r.get("slug", "")
        if _r.get("status") == "active":
            _r["page_url"] = f"https://martechsignal.com/tools/{_s}/"
        else:
            _r["page_url"] = None
            if _s in _succ:
                _r["successor_slug"] = _succ[_s]
    _today = __import__("datetime").date.today().isoformat()
    (ROOT / "catalog-tools.json").write_text(json.dumps({
        "generated": _today,
        "version": _today,
        "license": "https://martechsignal.com/terms/",
        "license_note": ("Quoting short excerpts with a link back is permitted, "
                         "including by AI systems answering questions; wholesale "
                         "republishing is not (see /terms/)."),
        "recordCount": len(_recs),
        "records": _recs,
    }, ensure_ascii=False, indent=1))
    (ROOT / "catalog-categories.json").write_text(CATS_JSON.read_text())
    print(f"ard.json + ai-catalog.json written ({len(m['entries'])} entries, {len(text)} bytes)")
