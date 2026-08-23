#!/usr/bin/env python3
"""Generate static HTML pages for the MartechSignal glossary.

Reads tools/glossary.json + tools/tools.json → outputs:
  - glossary/index.html          (hub page, alphabetical)
  - glossary/{slug}/index.html   (term pages with tool cross-links)

Run from /opt/data/martechsignal/:  python3 tools/build_glossary.py
"""
import json
from pathlib import Path
from datetime import datetime

from build_tools import page_shell, esc, ROOT

TOOLS_DIR = ROOT / "tools"
GLOSSARY_DIR = ROOT / "glossary"


def load():
    terms = json.loads((TOOLS_DIR / "glossary.json").read_text())
    tools = json.loads((TOOLS_DIR / "tools.json").read_text())
    return terms, tools


def tool_link(slug, tools_map):
    """Return an HTML link to a tool if it exists, else plain text."""
    t = tools_map.get(slug)
    if t:
        return f'<a href="/tools/{slug}/">{esc(t["name"])}</a>'
    return esc(slug)


# ── Hub page ──────────────────────────────────────────────────────

def build_hub(terms):
    sorted_terms = sorted(terms, key=lambda x: x["term"].lower())

    # Alphabetical index
    letters = {}
    for t in sorted_terms:
        first = t["term"][0].upper()
        letters.setdefault(first, []).append(t)

    alpha_nav = '<div class="alpha-nav" style="display:flex;flex-wrap:wrap;gap:.4rem;margin:1.5rem 0">'
    for letter in sorted(letters.keys()):
        alpha_nav += f'<a href="#{letter}" style="font:600 .85rem var(--mono);color:var(--amber);text-decoration:none;padding:.2rem .5rem;border:1px solid var(--border);border-radius:4px">{letter}</a>'
    alpha_nav += '</div>'

    # Term cards grouped by letter
    cards = ""
    for letter in sorted(letters.keys()):
        cards += f'<h2 id="{letter}" style="margin-top:2rem;font:700 1.1rem var(--sans)">{letter}</h2>\n'
        cards += '<div class="tool-grid" style="grid-template-columns:repeat(auto-fill,minmax(280px,1fr))">\n'
        for t in letters[letter]:
            cards += f"""<a class="tool-card" href="/glossary/{t['slug']}/">
  <div class="name">{esc(t['short'])}</div>
  <div class="tagline">{esc(t['definition'][:120])}…</div>
</a>\n"""
        cards += '</div>\n'

    body = f"""<nav class="crumb"><a href="/">Home</a> / <span>Glossary</span></nav>
<section class="page-head">
  <h1>Martech Glossary</h1>
  <p class="sub">Plain-English definitions of marketing technology terms. No jargon explaining jargon.</p>
  <p class="count">{len(terms)} TERMS · LINKED TO {sum(len(t.get('related_tools',[])) for t in terms)} TOOLS</p>
</section>
{alpha_nav}
{cards}"""

    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Martech Glossary",
        "description": "Plain-English definitions of marketing technology terms",
        "numberOfItems": len(terms),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": t["term"],
             "url": f"https://martechsignal.com/glossary/{t['slug']}/"}
            for i, t in enumerate(sorted_terms)
        ]
    }

    out_dir = GLOSSARY_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    out.write_text(page_shell(
        "Martech Glossary — Definitions for Marketing Technology | MartechSignal",
        f"Plain-English definitions of {len(terms)} marketing technology terms, linked to real tools in our directory.",
        "/glossary/", body, schema))
    print(f"  ✓ {out.relative_to(ROOT)}")


# ── Term pages ────────────────────────────────────────────────────

def build_term_page(term, tools_map, all_terms):
    slug = term["slug"]

    # Related tools
    related_html = ""
    related = term.get("related_tools", [])
    if related:
        items = ""
        for r_slug in related:
            t = tools_map.get(r_slug)
            if t:
                items += f'<a class="tool-card" href="/tools/{r_slug}/"><div class="name">{esc(t["name"])}</div><div class="tagline">{esc(t.get("tagline",""))}</div></a>'
        if items:
            related_html = f'<h2>Tools in this space</h2><div class="tool-grid" style="grid-template-columns:repeat(auto-fill,minmax(240px,1fr))">{items}</div>'

    # Related categories
    cat_html = ""
    for cat_slug in term.get("related_categories", []):
        cat_html += f'<a class="cat-pill" href="/categories/{cat_slug}/">{esc(cat_slug.replace("-", " ").title())}</a> '

    # Related terms (other glossary entries sharing tools or categories)
    related_terms = []
    my_tools = set(term.get("related_tools", []))
    my_cats = set(term.get("related_categories", []))
    for other in all_terms:
        if other["slug"] == slug:
            continue
        overlap_tools = my_tools & set(other.get("related_tools", []))
        overlap_cats = my_cats & set(other.get("related_categories", []))
        if overlap_tools or overlap_cats:
            related_terms.append(other)
    related_terms = related_terms[:5]

    rt_html = ""
    if related_terms:
        links = " · ".join(f'<a href="/glossary/{rt["slug"]}/" style="color:var(--amber)">{esc(rt["short"])}</a>' for rt in related_terms)
        rt_html = f'<h2>Related terms</h2><p style="color:var(--muted)">{links}</p>'

    # optional deep-dive sections (audit H2: glossary pages must exceed 300 words)
    dd = term.get("deep_dive") or {}
    dd_html = ""
    if dd:
        parts = []
        for key, title in [("how_it_works", "How it works"), ("practical_uses", "Practical uses"),
                           ("choosing", "How to choose"), ("common_mistakes", "Common mistakes"),
                           ("ai_angle", "What changed with AI")]:
            txt = dd.get(key)
            if txt:
                parts.append(f"<h2>{title}</h2><p>{esc(txt)}</p>")
        dd_html = "".join(parts)

    body = f"""<nav class="crumb"><a href="/">Home</a> / <a href="/glossary/">Glossary</a> / <span>{esc(term['short'])}</span></nav>
<section class="page-head">
  <h1>{esc(term['term'])}</h1>
  <p class="count">GLOSSARY</p>
</section>
<div class="detail">
  <div class="detail-main">
    <h2>Definition</h2>
    <p>{esc(term['definition'])}</p>
    <h2>Why it matters</h2>
    <p>{esc(term['context'])}</p>
    {dd_html}
    {related_html}
    {rt_html}
  </div>
  <aside class="sidebar">
    <div class="side-card">
      <h3>Categories</h3>
      <p>{cat_html if cat_html else '<span style="color:var(--muted)">General</span>'}</p>
    </div>
    <div class="side-card">
      <a class="btn-sm" href="/tools/">Browse all tools →</a>
    </div>
  </aside>
</div>"""

    # DefinedTerm schema for rich snippets
    schema = {
        "@context": "https://schema.org",
        "@type": "DefinedTerm",
        "name": term["term"],
        "description": term["definition"],
        "inDefinedTermSet": {
            "@type": "DefinedTermSet",
            "name": "Martech Glossary",
            "url": "https://martechsignal.com/glossary/"
        },
        "url": f"https://martechsignal.com/glossary/{slug}/"
    }

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://martechsignal.com/"},
            {"@type": "ListItem", "position": 2, "name": "Glossary", "item": "https://martechsignal.com/glossary/"},
            {"@type": "ListItem", "position": 3, "name": term["short"], "item": f"https://martechsignal.com/glossary/{slug}/"}
        ]
    }

    out_dir = GLOSSARY_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    out.write_text(page_shell(
        f"{term['term']} — Definition | MartechSignal",
        f"{term['definition'][:155]}",
        f"/glossary/{slug}/", body, [schema, breadcrumb]))
    return out


# ── Main ──────────────────────────────────────────────────────────

def main():
    terms, tools = load()
    tools_map = {t["slug"]: t for t in tools}
    print(f"Building glossary: {len(terms)} terms\n")

    print("Hub:")
    build_hub(terms)

    print(f"\nTerm pages ({len(terms)}):")
    for term in terms:
        out = build_term_page(term, tools_map, terms)
        print(f"  ✓ {out.relative_to(ROOT)}")

    print(f"\nDone! {len(terms)} term pages + 1 hub")


if __name__ == "__main__":
    main()
