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

from build_tools import page_shell, esc, ROOT, _category_display, _json_block_dates


def _meta_155(text):
    """L3 (r9, 2026-09-28): page_shell escapes the meta into the tag, so a raw
    [:155] cut renders longer when the definition carries & or quotes
    (utm-parameters shipped 163). Shrink until the escaped text fits.

    r23 M-3 (2026-10-05): word-boundary cut + fabricated period shipped
    "...moving a." / "...requesting a demo. It." to four glossary leaves.
    Sentence boundary first via _sentence_clip; when nothing fits, fall back
    to the term name (always true) instead of punctuating a fragment.

    r24 H-1: sentences_only - clause cuts still fail a strict instrument.
    """
    from build_tools import _sentence_clip as _sc, esc as _esc
    text = " ".join((text or "").split())
    cut = _sc(text, 155, sentences_only=True)
    while cut and len(_esc(cut)) > 155:
        cut = _sc(cut, len(cut) - 10, sentences_only=True)
    return cut

TOOLS_DIR = ROOT / "tools"
GLOSSARY_DIR = ROOT / "glossary"

# r7 H12 (2026-09-28): category -> commercial page map, so every glossary entry
# links outward to the comparison layer and its topic hub.
_BEST_FOR = {
    "analytics": "marketing-analytics-tools",
    "workflow-automation": "workflow-automation-tools",
    "crm": "ai-crm-tools",
    "marketing-automation": "ai-marketing-automation-tools",
    "geo-llm-visibility": "geo-llm-visibility-tools",
    "seo": "ai-seo-tools",
    "content-ai": "ai-content-copywriting-tools",
    "email-marketing": "ai-email-marketing-tools",
    "advertising": "ai-advertising-tools",
    "personalization": "ai-personalization-tools",
    "social-media": "ai-social-media-tools",
    "chatbots": "ai-chatbot-tools",
    "open-source": "open-source-marketing-tools",
    "agent-skills": "agent-skills-tools",
}
_GUIDES_FOR = {
    "geo-llm-visibility": (("generative-engine-optimization", "GEO guide"),),
    "workflow-automation": (("mcp-agent-protocols", "MCP and agent protocols"),
                            ("workflow-automation-strategy", "Automation strategy")),
    "marketing-automation": (("workflow-automation-strategy", "Automation strategy"),),
    "seo": (("ai-seo-tooling", "AI SEO tooling"),),
    "content-ai": (("ai-seo-tooling", "AI SEO tooling"),),
    "advertising": (("agentic-ai-advertising", "Agentic advertising"),),
}


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

def build_hub(terms, term_dates=None):
    sorted_terms = sorted(terms, key=lambda x: x["term"].lower())

    # Alphabetical index
    letters = {}
    for t in sorted_terms:
        first = t["term"][0].upper()
        letters.setdefault(first, []).append(t)

    alpha_nav = '<div class="alpha-nav" style="display:flex;flex-wrap:wrap;gap:.4rem;margin:1.5rem 0">'
    for letter in sorted(letters.keys()):
        alpha_nav += f'<a href="#{letter}" style="font:600 .85rem var(--mono);color:var(--amber);text-decoration:none;padding:.2rem .5rem;border:1px solid var(--line2);border-radius:4px">{letter}</a>'
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

    body = f"""<nav class="crumb"><a href="/">Home</a><span class="crumb-sep" aria-hidden="true">/</span><span>Glossary</span></nav>
<section class="page-head">
  <h1>Martech Glossary</h1>
  <p class="sub">Plain-English definitions of marketing technology terms. No jargon explaining jargon.</p>
  <p class="count">{len(terms)} TERMS · LINKED TO {sum(len(t.get('related_tools',[])) for t in terms)} TOOLS</p>
</section>
{alpha_nav}
{cards}"""

    # r11 M-8 (2026-09-29): every term page references this set via
    # inDefinedTermSet, but /glossary/ only emitted an ItemList — the set
    # itself was declared nowhere. @graph carries both nodes.
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "DefinedTermSet",
             "@id": "https://martechsignal.com/glossary/#set",
             "url": "https://martechsignal.com/glossary/",
             "name": "Martech Glossary",
             # r16 M-7 (2026-09-29): the audit's fix — the set declares its
             # size so consumers know the coverage without crawling.
             "numberOfItems": len(terms),
             # r15 M-2 (2026-09-29): money-template graphs join publisher + site.
             "publisher": {"@id": "https://martechsignal.com/#organization"},
             "isPartOf": {"@id": "https://martechsignal.com/#website"},
             "description": "Plain-English definitions of marketing technology terms"},
            {"@type": "ItemList",
             "name": "Martech Glossary",
             "description": "Plain-English definitions of marketing technology terms",
             "publisher": {"@id": "https://martechsignal.com/#organization"},
             "isPartOf": {"@id": "https://martechsignal.com/#website"},
             "numberOfItems": len(terms),
             **({"dateModified": max(d for d in (term_dates or {}).values() if d)}
                if term_dates and any((term_dates or {}).values()) else {}),
             "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "name": t["term"],
                  "url": f"https://martechsignal.com/glossary/{t['slug']}/"}
                 for i, t in enumerate(sorted_terms)
             ]},
        ],
    }

    out_dir = GLOSSARY_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    out.write_text(page_shell(
        "Marketing Technology Glossary | MartechSignal",
        f"Plain-English definitions of {len(terms)} marketing technology terms, linked to real tools in our directory.",
        "/glossary/", body, schema))
    print(f"  ✓ {out.relative_to(ROOT)}")


# ── Term pages ────────────────────────────────────────────────────

# r8 C2 (2026-09-28): hand-curated primary sources per entry. Every URL here
# was verified live (HTTP 200, 2026-09-28) before it was written down; terms
# with no citable standard lean on the catalog's own verified vendor fields.
_TERM_SOURCES = {
    "ai-search-visibility": (("llms.txt spec", "https://llmstxt.org/"),
                             ("Google Search Central", "https://developers.google.com/search/docs")),
    "aeo": (("llms.txt spec", "https://llmstxt.org/"),),
    "geo": (("llms.txt spec", "https://llmstxt.org/"),
            ("Google Search Central", "https://developers.google.com/search/docs")),
    "seo": (("Google Search Central", "https://developers.google.com/search/docs"),),
    "deliverability": (("RFC 5321 (SMTP)", "https://datatracker.ietf.org/doc/rfc5321/"),),
    "cdp": (("CDP Institute", "https://www.cdpinstitute.org/"),),
    "utm-parameters": (("Google campaign URL builder", "https://ga-dev-tools.google/campaign-url-builder/"),),
    "mcp": (("Model Context Protocol", "https://modelcontextprotocol.io/"),),
    "programmatic-advertising": (("IAB Tech Lab", "https://www.iabtechlab.com/"),),
    "dsp": (("IAB Tech Lab", "https://www.iabtechlab.com/"),),
    "dco": (("IAB Tech Lab", "https://www.iabtechlab.com/"),),
    "first-party-data": (("IAB Tech Lab", "https://www.iabtechlab.com/"),),
    "cro": (("Nielsen Norman Group", "https://www.nngroup.com/"),),
    "customer-journey": (("Nielsen Norman Group", "https://www.nngroup.com/"),),
    "chatbot": (("Nielsen Norman Group", "https://www.nngroup.com/"),),
}


def build_term_page(term, tools_map, all_terms, term_date=None):
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
        cat_html += f'<a class="cat-pill" href="/categories/{cat_slug}/">{esc(_category_display(cat_slug))}</a> '
        # r7 H12 (2026-09-28): the definitional layer reached 0 commercial pages
        # across 30 entries. Each entry now reaches its /best/ comparison and the
        # relevant topic hub.
        _b = _BEST_FOR.get(cat_slug)
        if _b:
            cat_html += f'<a class="cat-pill" href="/best/{_b}/">Best {_category_display(cat_slug)} tools</a> '
        for _gslug, _gname in _GUIDES_FOR.get(cat_slug, ()):
            cat_html += f'<a class="cat-pill" href="/guides/{_gslug}/">{esc(_gname)}</a> '

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

    # M10: value flows back - link the term to posts that use it in practice
    posts_html = ""
    seen = term.get("related_posts") or []
    if seen:
        plinks = " · ".join(
            f'<a href="/blog/{p["slug"]}/" style="color:var(--amber)">{esc(p["title"])}</a>'
            for p in seen
        )
        posts_html = f'<h2>Seen in the wild</h2><p style="color:var(--muted)">{plinks}</p>'

    # optional deep-dive sections (audit H2: glossary pages must exceed 300 words)
    dd = term.get("deep_dive") or {}
    dd_html = ""
    if dd:
        parts = []
        for key, title in [("how_it_works", "How it works"), ("practical_uses", "Practical uses"),
                           ("choosing", "How to choose"), ("the_numbers", "The numbers"),
                           ("common_mistakes", "Common mistakes"),
                           ("ai_angle", "What changed with AI")]:
            txt = dd.get(key)
            if txt:
                parts.append(f"<h2>{title}</h2><p>{esc(txt)}</p>")
        dd_html = "".join(parts)

    # r8 C2 (2026-09-28): every entry cites its sources - the standard/spec where
    # one exists (verified live), plus vendor pages from the catalog's own
    # verified website fields. No invented URLs.
    _parts = [f'<a href="{esc(u)}" rel="noopener">{esc(n)}</a>' for n, u in _TERM_SOURCES.get(slug, ())]
    for _rs in (term.get("related_tools") or []):
        _t = tools_map.get(_rs)
        if _t and _t.get("website") and len(_parts) < 4:
            _parts.append(f'<a href="{esc(_t["website"])}" rel="noopener">{esc(_t["name"])}</a>')
    sources_html = ('<p class="meta out-links">Sources: ' + ' · '.join(_parts) + '</p>') if _parts else ''

    body = f"""<nav class="crumb"><a href="/">Home</a><span class="crumb-sep" aria-hidden="true">/</span><a href="/glossary/">Glossary</a><span class="crumb-sep" aria-hidden="true">/</span><span>{esc(term['short'])}</span></nav>
<section class="page-head">
  <h1>{esc(term['term'])}</h1>
  <p class="count">GLOSSARY</p>
  {f'<p class="meta">Definition last updated <time datetime="{term_date}">{term_date}</time></p>' if term_date else ''}
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
    {posts_html}
    {sources_html}
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

    # DefinedTerm schema for rich snippets.
    # r16 M-7 (2026-09-29): the leaf referenced glossary/#set without
    # defining it (30 dangling refs). @graph carries the term plus the set
    # stub; the hub holds the full node with numberOfItems.
    schema = {
        "@context": "https://schema.org",
        "@graph": [{
            "@type": "DefinedTerm",
            "name": term["term"],
            "description": term["definition"],
            **({"dateModified": term_date} if term_date else {}),
            # r16 L-8 (2026-09-29): leaves carried only dateModified.
            # datePublished falls back to the term date so naive parsers
            # can date the entry.
            **({"datePublished": term_date} if term_date else {}),
            "inDefinedTermSet": {
                "@id": "https://martechsignal.com/glossary/#set",
                "@type": "DefinedTermSet",
                "name": "MartechSignal Glossary",
                # r17 L-4: the stub previously carried only @id, so the join
                # landed on an empty node on leaves; state the set size here
                # (same number the hub node derives).
                "numberOfItems": len(all_terms)
            },
            # r16 L-8: author inlined with name (single-block parsers see
            # no author name in a bare @id reference).
            "author": {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/"},
            # r15 M-2 (2026-09-29): money-template graphs join publisher + site.
            "publisher": {"@id": "https://martechsignal.com/#organization"},
            "isPartOf": {"@id": "https://martechsignal.com/#website"},
            "url": f"https://martechsignal.com/glossary/{slug}/"
        }, {
            "@type": "DefinedTermSet",
            "@id": "https://martechsignal.com/glossary/#set",
            "url": "https://martechsignal.com/glossary/",
            "name": "Martech Glossary"
        }]
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
    # Title: prefer short form for long terms (audit L1: glossary titles hit 90ch)
    title_term = term["term"] if len(term["term"]) <= 40 else term.get("short") or term["term"]
    title = f"{title_term} | Definition | MartechSignal"
    if len(title) > 60:
        # Drop the "| MartechSignal" suffix (canonical/brand already in the page)
        title = f"{title_term} | Definition"
    if len(title) > 60 and " (" in title_term:
        # Strip parenthetical acronym, e.g. 'Customer Relationship Management (CRM)' -> 'CRM'
        title_term2 = term.get("short") or title_term.split(" (")[0]
        title = f"{title_term2} | Definition | MartechSignal"
        if len(title) > 60:
            title = f"{title_term2} | Definition"
    # A2 L9 (2026-09-26): related terms had no mutual linking structure.
    import re as _re, html as _html
    _tok = set(_re.findall(r'[a-z]{4,}', (term.get('term', '') + ' ' + (term.get('short') or '')).lower()))
    _see = []
    for _o in all_terms:
        if _o.get('slug') == term.get('slug'):
            continue
        _ot = set(_re.findall(r'[a-z]{4,}', (_o.get('term', '') + ' ' + (_o.get('short') or '')).lower()))
        if len(_tok & _ot) >= 1:
            _see.append(_o)
        if len(_see) >= 3:
            break
    if _see:
        _links = ''.join(f'<li><a href="/glossary/{_o["slug"]}/">{_html.escape(_o.get("short") or _o["term"])}</a></li>' for _o in _see)
        body += '<section class="seealso"><h2>See also</h2><ul>' + _links + '</ul></section>'
    out.write_text(page_shell(
        title,
        # r23 M-3: never ship an empty meta; the term name is always true.
        _meta_155(term["definition"]) or f"{term['term']}: definition in the MartechSignal glossary.",
        f"/glossary/{slug}/", body, [schema, breadcrumb], og_image=f"og/glossary/{slug}.png"))
    return out


# ── Main ──────────────────────────────────────────────────────────

def main():
    terms, tools = load()
    tools_map = {t["slug"]: t for t in tools}
    print(f"Building glossary: {len(terms)} terms\n")

    # H10 (r9, 2026-09-28): per-term edit dates from glossary.json blame so
    # lastmod reflects real definition edits, not build day.
    term_dates = _json_block_dates("tools/glossary.json", 4)

    print("Hub:")
    build_hub(terms, term_dates)

    print(f"\nTerm pages ({len(terms)}):")
    for term in terms:
        out = build_term_page(term, tools_map, terms, term_dates.get(term["slug"]))
        print(f"  ✓ {out.relative_to(ROOT)}")

    print(f"\nDone! {len(terms)} term pages + 1 hub")


if __name__ == "__main__":
    main()
