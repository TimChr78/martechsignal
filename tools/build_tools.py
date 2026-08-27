#!/usr/bin/env python3
"""Generate static HTML pages for the MartechSignal tool directory.

Reads tools/tools.json + tools/categories.json → outputs:
  - tools/index.html          (directory hub)
  - tools/{slug}.html         (tool profiles)
  - categories/{slug}.html    (category listings)

Run from /opt/data/martechsignal/:  python3 tools/build_tools.py
"""
import json, os, html, re
import sys
from pathlib import Path
from datetime import datetime
sys.path.insert(0, str(Path(__file__).resolve().parent))
import suggest_links

ROOT = Path(__file__).resolve().parent.parent  # martechsignal/
TOOLS_DIR = ROOT / "tools"
CATS_DIR = ROOT / "categories"

def load():
    tools = json.loads((TOOLS_DIR / "tools.json").read_text())
    cats = json.loads((TOOLS_DIR / "categories.json").read_text())
    return tools, cats

def esc(s):
    return html.escape(str(s)) if s else ""

def pricing_label(t):
    m = t.get("pricing_model", "paid")
    if m == "free": return "Free"
    if m == "freemium": return "Freemium"
    if m == "open-source": return "Open Source"
    if m == "enterprise": return "Enterprise"
    p = t.get("price_from")
    if p == 0: return "Free tier"
    if p: return f"From ${p}/mo"
    return "Paid"

# ── SEO title / meta template (CTR-optimized, ≤60 / ≤155) ──────────
# Title:  "{Name} Review — {Pricing} | MartechSignal"        (primary)
#   Try: "{Name} Review: {Category} — {Pricing} | MartechSignal" first;
#   fallback without category if >60ch. For very long names we truncate
#   the name part (never the suffix) to keep the pipe-brand intact.
# Meta:   "{Name} — {Tagline}. {PricingPhrase} Compare AI features, integrations & top alternatives."
#   PricingPhrase varies by model: Open source / Enterprise / Starts at $X / etc.


def cat_h1(cat_name):
    """Category hub H1: append 'Tools' unless the name already ends with it."""
    name = (cat_name or "").strip()
    if name.lower().endswith("tools"):
        return name
    return f"{name} Tools"

def _seo_title_for(t, cats):
    cat_map = {c["slug"]: c["name"] for c in cats}
    name = t["name"]
    cat_name = cat_map.get(t.get("category"), "")
    price = pricing_label(t)
    suffix = " | MartechSignal"
    if cat_name:
        cand = f"{name} Review: {cat_name} \u2014 {price}{suffix}"
        if len(cand) <= 60:
            return cand
    cand2 = f"{name} Review \u2014 {price}{suffix}"
    if len(cand2) <= 60:
        return cand2
    overhead = len(f" Review \u2014 {price}{suffix}")
    budget = 60 - overhead
    if budget < 10:
        return cand2[:60]
    truncated_name = name[:budget].rsplit(" ", 1)[0] if " " in name[:budget] else name[:budget]
    return f"{truncated_name} Review \u2014 {price}{suffix}"[:60]

def _seo_description_for(t, cats):
    cat_map = {c["slug"]: c["name"] for c in cats}
    name = t["name"]
    tagline = (t.get("tagline") or "").strip()
    if not tagline or len(tagline) < 10:
        desc = (t.get("description") or "").strip()
        if desc and len(desc) >= 30:
            # use first sentence of description as tagline fallback
            import re as _re
            first = _re.split(r'[.!…]\s', desc, 1)[0].strip()
            if len(first) >= 20:
                tagline = first
            else:
                tagline = desc[:90].rsplit(" ", 1)[0] if " " in desc[:90] else desc[:90]
        else:
            tagline = f"{cat_map.get(t.get('category'), 'Marketing')} tool"
    tagline_sent = tagline if tagline.endswith(".") else tagline + "."
    if t.get("open_source"):
        price_phrase = "Open source & free to self-host."
    elif t.get("pricing_model") == "enterprise":
        price_phrase = "Enterprise pricing; demo required."
    elif t.get("price_from") is not None:
        if t.get("price_from"):
            price_phrase = f"Starts at ${t['price_from']}/mo."
        elif t.get("pricing_model") in ("freemium", "free", "open-core"):
            price_phrase = "Free tier available."
        else:
            price_phrase = "Free to use."
    else:
        price_phrase = f"{pricing_label(t)}."
    tail = " Compare AI features, integrations & top alternatives."
    base = f"{name} \u2014 {tagline_sent} {price_phrase}{tail}"
    if len(base) <= 155:
        return base
    overhead = len(f"{name} \u2014  {price_phrase}{tail}") + 3
    budget = 155 - overhead
    if len(tagline_sent) > budget:
        if budget > 20 and " " in tagline_sent[:budget]:
            trunc = tagline_sent[:budget].rsplit(" ", 1)[0]
        else:
            trunc = tagline_sent[:max(0, budget - 1)]
        tagline_sent = trunc.rstrip(" ,;:") + "\u2026"
    base2 = f"{name} \u2014 {tagline_sent} {price_phrase}{tail}"
    if len(base2) > 155:
        base2 = f"{name} \u2014 {price_phrase}{tail}".replace("  ", " ")
    return base2[:155]

# ── Shared HTML shell ──────────────────────────────────────────────

def page_shell(title, description, canonical, body, schema_json=None, og_image=None):
    og_url = og_image or "og.png"
    schema_block = ""
    if schema_json:
        schema_block = f'<script type="application/ld+json">{json.dumps(schema_json, indent=2)}</script>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23080E1A'/%3E%3Crect x='9' y='7' width='14' height='18' rx='2' fill='%23FFB224'/%3E%3C/svg%3E">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Martech Signal">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="https://martechsignal.com{canonical}">
<meta property="og:image" content="https://martechsignal.com/{og_url}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="https://martechsignal.com/{og_url}">
<link rel="canonical" href="https://martechsignal.com{canonical}">
<meta name="msvalidate.01" content="B3427474AF36B6861E22592403BA8B27">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet"></noscript>
{schema_block}
<link rel="stylesheet" href="/style.css?v=69b0f800">
<script defer src="https://analytics.martechsignal.com/script.js" data-website-id="11b28e66-3570-4781-b369-2134c7c372ab"></script>
</head>
<body class="page-tools">
<div class="bg" aria-hidden="true"></div>
<header class="masthead">
  <div class="wrap mast-in">
    <a class="wordmark" href="/">MARTECH<b>SIGNAL</b><span class="cursor">▮</span></a>
    <nav class="mast-nav"><a href="/tools/">TOOLS</a><a href="/blog/">BLOG</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</header>
<main class="wrap">
{body}
</main>
<footer>
  <div class="wrap">
    <div class="foot-links">
      <a href="/">HOME</a>
      <a href="/tools/">TOOLS</a>
      <a href="/glossary/">GLOSSARY</a>
      <a href="/blog/">BLOG</a>
      <a href="/about/">ABOUT</a>
      <a href="/contact/">CONTACT</a>
      <a href="/privacy/">PRIVACY</a>
      <a href="/terms/">TERMS</a>
      <a href="/#subscribe">SUBSCRIBE</a>
    </div>
    <p class="fine">© {datetime.now().year} MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION</p>
  </div>
</footer>
</body>
</html>"""

# ── Directory hub ──────────────────────────────────────────────────

def build_hub(tools, cats):
    cat_map = {c["slug"]: c for c in cats}
    # category pills
    pills = '<a class="cat-pill active" href="/tools/">ALL</a>\n'
    for c in cats:
        if c["slug"] == "open-source":
            n = sum(1 for t in tools if t.get("open_source") and t.get("status") == "active")
        else:
            n = sum(1 for t in tools if t["category"] == c["slug"] and t.get("status") == "active")
        if n:
            pills += f'<a class="cat-pill" href="/categories/{c["slug"]}/">{esc(c["name"])} ({n})</a>\n'

    # tool cards
    cards = ""
    for t in sorted(tools, key=lambda x: x["name"].lower()):
        if t.get("status") != "active": continue
        c = cat_map.get(t["category"], {})
        tags = f'<span class="tag pricing">{esc(pricing_label(t))}</span>'
        tags += f'<span class="tag cat">{esc(c.get("name", t["category"]))}</span>'
        if t.get("open_source"):
            tags += '<span class="tag oss">OSS</span>'
        cards += f"""<a class="tool-card" href="/tools/{t['slug']}/">
  <div class="name">{esc(t['name'])}</div>
  <div class="tagline">{esc(t.get('tagline',''))}</div>
  <div class="meta">{tags}</div>
</a>\n"""

    body = f"""<nav class="crumb"><a href="/">Home</a> / <span>Tools</span></nav>
<section class="page-head">
  <h1>AI Marketing Tool Directory</h1>
  <p class="sub">Curated tools for AI-powered marketing automation — from email and CRM to content generation and workflow automation.</p>
  <p class="count">{len([t for t in tools if t.get('status')=='active'])} TOOLS · {len(cats)} CATEGORIES · UPDATED WEEKLY</p>
</section>
<img src="/og/charts/oss-by-category.png" alt="Open-source share by category: how many of the listed tools per category are open source versus commercial" width="1200" height="630" loading="lazy" style="max-width:100%;height:auto;border-radius:10px;margin:1.5rem 0;border:1px solid var(--border)">
<nav class="cat-nav">{pills}</nav>
<div class="tool-grid">{cards}</div>"""

    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "AI Marketing Tool Directory",
        "description": "Curated directory of AI-powered marketing automation tools",
        "numberOfItems": len([t for t in tools if t.get("status") == "active"]),
        "itemListElement": []
    }
    active = [t for t in sorted(tools, key=lambda x: x["name"].lower()) if t.get("status") == "active"]
    schema["itemListElement"] = [
        {"@type": "ListItem", "position": i+1, "name": t["name"], "url": f"https://martechsignal.com/tools/{t['slug']}/"}
        for i, t in enumerate(active)
    ]

    out = TOOLS_DIR / "index.html"
    out.write_text(page_shell(
        "AI Marketing Tool Directory — MartechSignal",
        f"Browse {len(active)} curated AI marketing automation tools. Compare pricing, features, and integrations.",
        "/tools/", body, schema))
    print(f"  ✓ {out.relative_to(ROOT)}")

# ── Tool profile pages ─────────────────────────────────────────────

def build_tool_page(t, cats, all_tools):
    cat_map = {c["slug"]: c for c in cats}
    c = cat_map.get(t["category"], {})
    slug = t["slug"]

    # related tools (same category)
    related = [x for x in all_tools if x["category"] == t["category"] and x["slug"] != slug and x.get("status") == "active"][:4]
    related_html = ""
    if related:
        items = "".join(f'<a class="tool-card" href="/tools/{r["slug"]}/"><div class="name">{esc(r["name"])}</div><div class="tagline">{esc(r.get("tagline",""))}</div></a>' for r in related)
        related_html = f'<h2>Similar Tools</h2><div class="tool-grid" style="grid-template-columns:repeat(auto-fill,minmax(240px,1fr))">{items}</div>'

    source_text = ' '.join(str(t.get(key, '')) for key in ('name', 'tagline', 'description', 'ai_features', 'integrations'))
    related_posts = suggest_links.suggest_for_text(source_text, max_suggestions=3)
    if related_posts:
        links = ''.join('<li><a href="' + html.escape(item['url'], quote=True) + '">' + html.escape(item['title'], quote=False) + '</a></li>' for item in related_posts)
        related_html += '<section class="related-reading"><h2>Related reading</h2><ul>' + links + '</ul></section>'

    # AI features
    ai_html = ""
    if t.get("ai_features"):
        items = "".join(f"<li>{esc(f)}</li>" for f in t["ai_features"])
        ai_html = f'<h2>AI Capabilities</h2><ul class="feat-list">{items}</ul>'

    # integrations
    integ_html = ""
    if t.get("integrations"):
        items = "".join(f"<span>{esc(i)}</span>" for i in t["integrations"])
        integ_html = f'<h2>Key Integrations</h2><div class="integ-list">{items}</div>'

    # optional deep-dive sections (per-tool, only for tools with a deep_dive dict)
    dd = t.get("deep_dive") or {}
    dd_html = ""
    if dd:
        parts = []
        if dd.get("install"):
            steps = "".join(f"<li>{esc(s)}</li>" for s in dd["install"])
            parts.append(f'<h2>How to install</h2><ol class="feat-list">{steps}</ol>')
        if dd.get("requirements"):
            parts.append(f'<h2>Requirements</h2><p>{esc(dd["requirements"])}</p>')
        if dd.get("stats"):
            rows = "".join(f"<div class='side-row'><dt>{esc(str(k).replace('_',' ').title())}</dt><dd>{esc(str(v))}</dd></div>" for k, v in dd["stats"].items())
            parts.append(f'<div class="side-card"><h3>Project stats</h3><dl>{rows}</dl></div>')
        if dd.get("best_for"):
            parts.append(f'<h2>Best for</h2><p>{esc(dd["best_for"])}</p>')
        if dd.get("not_for"):
            parts.append(f'<h2>Not for</h2><p>{esc(dd["not_for"])}</p>')
        if dd.get("comparison_note"):
            parts.append(f'<h2>Hosted vs. original</h2><p>{esc(dd["comparison_note"])}</p>')
        if dd.get("hands_on"):
            paras = "".join(f"<p>{esc(p)}</p>" for p in dd["hands_on"])
            parts.append(f'<h2>Hands-on notes</h2>{paras}')
        if dd.get("verdict"):
            parts.append(f'<h2>Verdict</h2><p>{esc(dd["verdict"])}</p>')
        # stats card goes in the sidebar; other sections inline before related links
        inline = "".join(x for x in parts if x.startswith("<h2"))
        sidebar_extra = "".join(x for x in parts if x.startswith("<div"))
        dd_html = inline
        t["_dd_sidebar"] = sidebar_extra
    else:
        inline = ""
        sidebar_extra = ""
        dd_html = ""

    # Vendor screenshot on every tool page that has a capture (M9 media plan)
    _shot_path = f"og/screenshots/{slug}-{datetime.now().strftime('%Y-%m')}.png"
    _shot = ROOT / _shot_path
    if _shot.exists():
        shot_html = (f'<figure style="margin:1.5rem 0"><img src="/{_shot_path}" width="1200" height="750" '
                     f'alt="Screenshot of {esc(t["name"])} homepage, {datetime.now().strftime("%B %Y")}" loading="lazy" '
                     f'style="max-width:100%;height:auto;border-radius:10px;border:1px solid var(--border)"></figure>')
        dd_html = shot_html + dd_html

    # Overview paragraph
    if t.get('description'):
        overview_html = f'<p>{esc(t["description"])}</p>'
    else:
        price_str = ('$'+str(t['price_from'])+'/mo') if t.get('price_from') is not None else 'custom pricing'
        overview_html = f'<p>{esc(t.get("tagline",""))} {esc(t["name"])} is a {esc(c.get("name","").lower())} tool with {"free" if t.get("price_from",1)==0 else "paid"} pricing starting at {price_str}.</p>'

    # FAQPage Q&A: generated from tool data (AI Overview / PAA eligibility).
    # Rendered BOTH as visible accordions in the page body AND as FAQPage
    # JSON-LD — schema-only Q&A without matching on-page content risks
    # Google structured-data guideline non-compliance.
    def _faq_for(t, c):
        name = t["name"]
        cat = c.get("name", "marketing")
        price = pricing_label(t)
        q1 = f"What is {name}?"
        a1 = (t.get("tagline") or "").strip().rstrip(".") or f"{name} is a {cat.lower()} tool."
        a1 = f"{a1}. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        q2 = f"How much does {name} cost?"
        if t.get("open_source"):
            a2 = f"{name} is open source and free to self-host. Hosted plans may add support and managed features."
        elif t.get("price_from") is not None:
            if t.get("price_from"):
                a2 = f"{name} starts at ${t['price_from']}/mo."
            elif t.get("pricing_model") in ("freemium", "free", "open-core"):
                a2 = f"{name} has a free tier. Paid plans unlock higher limits."
            else:
                a2 = f"{name} is free to use."
        else:
            a2 = f"{name} uses {price.lower()} pricing. See the vendor's pricing page for current plans."
        q3 = f"Is {name} a good {cat.lower()} tool in 2026?"
        pros = []
        if t.get("g2_rating"): pros.append(f"a {t['g2_rating']}/5 G2 rating")
        if t.get("github_stars"): pros.append(f"{t['github_stars']:,} GitHub stars")
        if t.get("api_available"): pros.append("an API for custom integrations")
        a3 = (f"Our audit found {', '.join(pros)}" if pros else f"Our audit covers {name}'s core {cat.lower()} workflow")
        a3 += f". The full review breaks down where it fits in a modern martech stack."
        faqs = [
            {"@type": "Question", "name": q1, "acceptedAnswer": {"@type": "Answer", "text": a1}},
            {"@type": "Question", "name": q2, "acceptedAnswer": {"@type": "Answer", "text": a2}},
            {"@type": "Question", "name": q3, "acceptedAnswer": {"@type": "Answer", "text": a3}},
        ]
        # per-tool FAQ extensions (targets long-tail query variants)
        if dd.get("faq_extra"):
            for q, a in dd["faq_extra"]:
                faqs.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
        return faqs

    faqs = _faq_for(t, c)

    # Visible FAQ accordions (same Q&A as the FAQPage JSON-LD)
    _faq_items = [
        f'<details class="faq-item"><summary>{esc(q["name"])}</summary>'
        f'<p>{esc(q["acceptedAnswer"]["text"])}</p></details>'
        for q in faqs
    ]
    faq_html = (
        '<section class="faq-block"><h2>Frequently asked questions</h2>'
        + "".join(_faq_items) + "</section>"
    ) if _faq_items else ""

    deep_dive_html = dd_html
    deep_dive_sidebar = (t.get("_dd_sidebar") or "") if dd else ""
    body = f"""<nav class="crumb"><a href="/">Home</a> / <a href="/tools/">Tools</a> / <a href="/categories/{t['category']}/">{esc(c.get('name',''))}</a> / <span>{esc(t['name'])}</span></nav>
<section class="page-head">
  <h1>{esc(t['name'])}</h1>
  <p class="sub">{esc(t.get('tagline',''))}</p>
  <p class="count">{esc(c.get('name',''))} · {esc(pricing_label(t))}{' · OPEN SOURCE' if t.get('open_source') else ''}</p>
</section>
<div class="detail">
  <div class="detail-main">
    <h2>Overview</h2>
    {overview_html}
    {ai_html}
    {integ_html}
    {deep_dive_html}
    {faq_html}
    {related_html}
  </div>
  <aside class="sidebar">
    <div class="side-card">
      <h3>Quick Facts</h3>
      <dl>
        <div class="side-row"><dt>Pricing</dt><dd>{esc(pricing_label(t))}</dd></div>
        <div class="side-row"><dt>Category</dt><dd><a href="/categories/{t['category']}/">{esc(c.get('name',''))}</a></dd></div>
        {deep_dive_sidebar}
        {'<div class="side-row"><dt>G2 Rating</dt><dd>★ ' + str(t['g2_rating']) + ' (' + str(t.get('g2_reviews','')) + ')</dd></div>' if t.get('g2_rating') else ''}
        {'<div class="side-row"><dt>GitHub</dt><dd>★ ' + str(t['github_stars']) + '</dd></div>' if t.get('github_stars') else ''}
        {'<div class="side-row"><dt>Founded</dt><dd>' + str(t['founded']) + '</dd></div>' if t.get('founded') else ''}
        {'<div class="side-row"><dt>HQ</dt><dd>' + esc(t['hq']) + '</dd></div>' if t.get('hq') else ''}
        <div class="side-row"><dt>API</dt><dd>{'Yes' if t.get('api_available') else 'No'}</dd></div>
        {'<div class="side-row"><dt>Last verified</dt><dd><time datetime="' + esc(t['date_updated']) + '">' + esc(t['date_updated']) + '</time></dd></div>' if t.get('date_updated') else ''}
      </dl>
    </div>
    <div class="side-card">
      <a class="btn-sm" href="{esc(t.get('website','#'))}" target="_blank" rel="noopener" data-umami-event="Tool CTA click" data-umami-event-tool="{esc(t['name'])}">Visit {esc(t['name'])} →</a>
    </div>
    {'<div class="side-card"><h3>Pricing</h3><p style="color:var(--muted);font-size:.9rem">' + esc(t.get('price_notes','')) + '</p><div style="margin-top:.8rem"><a style="font:600 .74rem var(--mono);color:var(--amber);text-decoration:none" href="' + esc(t.get('pricing_url','#')) + '" target="_blank" rel="noopener" data-umami-event="Pricing click" data-umami-event-tool="' + esc(t['name']) + '">VIEW PRICING →</a></div></div>' if t.get('price_notes') else ''}
  </aside>
</div>"""

    # Schema
    schema = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": t["name"],
        "description": t.get("tagline", ""),
        "url": t.get("website", ""),
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web",
    }
    if t.get("date_updated"):
        schema["dateModified"] = t["date_updated"]
    if t.get("date_added"):
        schema["datePublished"] = t["date_added"]
    if t.get("g2_rating"):
        schema["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": t["g2_rating"],
            "reviewCount": t.get("g2_reviews", 0),
            "bestRating": 5
        }
    # Only emit offers.price when it is a real number. Custom/enterprise pricing
    # (price_from=None) must not emit price:0 - Google lifts that as a factual claim.
    _pf = t.get("price_from")
    if _pf is not None and (_pf > 0 or t.get("pricing_model") in ("free", "freemium", "open-source", "open-core")):
        schema["offers"] = {
            "@type": "Offer",
            "price": _pf,
            "priceCurrency": "USD"
        }

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://martechsignal.com/"},
            {"@type": "ListItem", "position": 2, "name": "Tools", "item": "https://martechsignal.com/tools/"},
            {"@type": "ListItem", "position": 3, "name": c.get("name", ""), "item": f"https://martechsignal.com/categories/{t['category']}/"},
            {"@type": "ListItem", "position": 4, "name": t["name"], "item": f"https://martechsignal.com/tools/{slug}/"}
        ]
    }

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": _faq_for(t, c)
    }

    out_dir = TOOLS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    # SEO title/meta: prefer persisted seo_* fields; otherwise generate via helpers (≤60/≤155, Review+Category+Pricing)
    seo_title = t.get("seo_title") or _seo_title_for(t, cats)
    seo_desc = t.get("seo_description") or _seo_description_for(t, cats)
    out.write_text(page_shell(
        seo_title,
        seo_desc,
        f"/tools/{slug}/", body, [schema, breadcrumb, faq_schema], og_image=f"og/tools/{slug}.png"))
    return out

# ── Category pages ─────────────────────────────────────────────────

def tool_card_html(t):
    tags = f'<span class="tag pricing">{esc(pricing_label(t))}</span>'
    if t.get("open_source"):
        tags += '<span class="tag oss">OSS</span>'
    return f"""<a class="tool-card" href="/tools/{t['slug']}/">
  <div class="name">{esc(t['name'])}</div>
  <div class="tagline">{esc(t.get('tagline',''))}</div>
  <div class="meta">{tags}</div>
</a>\n"""


def build_category_page(cat, tools):
    if cat["slug"] == "open-source":
        # Show ALL open-source tools regardless of primary category
        cat_tools = [t for t in sorted(tools, key=lambda x: x["name"].lower()) if t.get("open_source") and t.get("status") == "active"]
    else:
        cat_tools = [t for t in sorted(tools, key=lambda x: x["name"].lower()) if t["category"] == cat["slug"] and t.get("status") == "active"]
    if not cat_tools:
        return None

    by_slug = {t["slug"]: t for t in cat_tools}
    hub = cat.get("hub")

    if not hub:
        # Simple listing for categories without editorial hub content
        cards = "".join(tool_card_html(t) for t in cat_tools)
        intro_html = ""
        if cat.get("intro"):
            intro_html = f'<p class="cat-intro" style="max-width:680px;color:var(--muted);margin:.5rem 0 0">{esc(cat["intro"])}</p>'
        body = f"""<nav class="crumb"><a href="/">Home</a> / <a href="/tools/">Tools</a> / <span>{esc(cat['name'])}</span></nav>
<section class="page-head">
  <h1>{cat_h1(cat['name'])}</h1>
  <p class="sub">{esc(cat.get('description',''))}</p>
  {intro_html}
  <p class="count">{len(cat_tools)} TOOLS IN THIS CATEGORY</p>
</section>
<div class="tool-grid">{cards}</div>"""
    else:
        # ── Hub page: editorial intro + pipeline visual + chooser + grouped grid ──
        flow = ""
        steps = hub.get("flow", [])
        for i, s in enumerate(steps):
            style = f' {s["style"]}' if s.get("style") else ""
            flow += f'<div class="flow-step{style}"><span class="flow-label">{esc(s["label"])}</span><span class="flow-sub">{esc(s.get("sub",""))}</span></div>'
            if i < len(steps) - 1:
                flow += '<div class="flow-wire"><i class="flow-pulse"></i></div>'

        lead = "".join(f"<p>{esc(p)}</p>" for p in hub.get("lead", []))

        chooser = ""
        for row in hub.get("chooser", []):
            picks = " ".join(
                f'<a class="pick" href="/tools/{p["slug"]}/">{esc(p["name"])}</a>' for p in row["then"]
            )
            chooser += f"""<div class="chooser-row">
  <div class="chooser-if"><span class="chooser-k">IF</span> {esc(row["if"])}</div>
  <div class="chooser-then">{picks}</div>
  <div class="chooser-why">{esc(row["why"])}</div>
</div>\n"""

        groups_html = ""
        grouped_slugs = set()
        for g in hub.get("groups", []):
            g_tools = [by_slug[s] for s in g["slugs"] if s in by_slug]
            if not g_tools:
                continue
            grouped_slugs.update(g["slugs"])
            cards = "".join(tool_card_html(t) for t in g_tools)
            groups_html += f"""<div class="hub-group reveal">
  <div class="hub-group-label"><span>{esc(g["label"])}</span><i></i><em>{len(g_tools)}</em></div>
  <div class="tool-grid">{cards}</div>
</div>\n"""
        leftovers = [t for t in cat_tools if t["slug"] not in grouped_slugs]
        if leftovers:
            cards = "".join(tool_card_html(t) for t in leftovers)
            groups_html += f'<div class="hub-group reveal"><div class="tool-grid">{cards}</div></div>'

        reading = ""
        for r in hub.get("reading", []):
            reading += f"""<a class="read-row" href="/blog/{r['slug']}/">
  <div class="read-title">{esc(r["title"])}</div>
  <div class="read-note">{esc(r.get("note",""))}</div>
  <span class="read-arrow">→</span>
</a>\n"""

        body = f"""<nav class="crumb"><a href="/">Home</a> / <a href="/tools/">Tools</a> / <span>{esc(cat['name'])}</span></nav>
<section class="page-head hub-head">
  <h1>{cat_h1(cat['name'])}</h1>
  <p class="sub">{esc(hub.get('meta', cat.get('description','')))}</p>
  <p class="count">{len(cat_tools)} TOOLS IN THIS CATEGORY</p>
</section>

<div class="flow-strip reveal" aria-hidden="true">{flow}</div>

<section class="hub-lead reveal">{lead}</section>

<section class="hub-chooser reveal">
  <h2>Which one fits</h2>
  {chooser}
</section>

{groups_html}

<section class="hub-reading reveal">
  <h2>Reading before you buy</h2>
  {reading}
</section>

<script>
(function() {{
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {{ els.forEach(function(e) {{ e.classList.add('in'); }}); return; }}
  var io = new IntersectionObserver(function(entries) {{
    entries.forEach(function(en) {{ if (en.isIntersecting) {{ en.target.classList.add('in'); io.unobserve(en.target); }} }});
  }}, {{ threshold: 0.12 }});
  els.forEach(function(e) {{ io.observe(e); }});
}})();
</script>"""

    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": f"{cat['name']} Tools",
        "description": hub.get("meta", cat.get("description", "")) if hub else cat.get("description", ""),
        "numberOfItems": len(cat_tools),
        "itemListElement": [
            {"@type": "ListItem", "position": i+1, "name": t["name"], "url": f"https://martechsignal.com/tools/{t['slug']}/"}
            for i, t in enumerate(cat_tools)
        ]
    }

    out_dir = CATS_DIR / cat["slug"]
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    out.write_text(page_shell(
        f"{cat_h1(cat['name'])} — MartechSignal",
        (hub.get("meta") if hub else f"Browse {len(cat_tools)} {cat['name'].lower()} tools for AI-powered marketing automation.") or "",
        f"/categories/{cat['slug']}/", body, schema, og_image=f"og/categories/{cat['slug']}.png"))
    return out

# ── Main ───────────────────────────────────────────────────────────

# ── Sitemap ────────────────────────────────────────────────────────

_LASTMOD_STORE_PATH = ROOT / "tools" / ".lastmod.json"
_lastmod_store = None

def _load_lastmod_store():
    global _lastmod_store
    if _lastmod_store is None:
        try:
            _lastmod_store = json.loads(_LASTMOD_STORE_PATH.read_text())
        except Exception:
            _lastmod_store = {}
    return _lastmod_store

def _save_lastmod_store():
    if _lastmod_store is not None:
        _LASTMOD_STORE_PATH.write_text(json.dumps(_lastmod_store, indent=1))

def _lastmod(path):
    """Content-hash lastmod — audit 3 M2: rebuild re-stamps evergreen pages,
    teaching Google to distrust lastmod. Fingerprint the rendered HTML; if
    unchanged since the previous build, keep the stored date instead of today."""
    import datetime as _dt, hashlib as _hl, re as _re
    p = Path(path)
    if not p.exists():
        return _dt.datetime.now().strftime("%Y-%m-%d")
    fp = _hl.sha256(_re.sub(r"<lastmod>[^<]*</lastmod>", "", p.read_text()).encode()).hexdigest()[:16]
    store = _load_lastmod_store()
    key = str(p)
    prev = store.get(key)
    if prev and prev.get("fp") == fp:
        return prev["date"]
    date = _dt.datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")
    store[key] = {"fp": fp, "date": date}
    return date

def build_sitemap(tools, cats):
    today = datetime.now().strftime("%Y-%m-%d")
    urls = []

    # Homepage
    home_html = ROOT / "index.html"
    urls.append((f"https://martechsignal.com/", _lastmod(home_html) if home_html.exists() else today, "1.0"))

    # Checklist page (audit M1: live but missing from discovery)
    checklist_html = ROOT / "checklist" / "index.html"
    if checklist_html.exists():
        urls.append(("https://martechsignal.com/checklist/", _lastmod(checklist_html), "0.6"))

    # Blog posts (scan blog/ for subdirectories containing index.html)
    blog_dir = ROOT / "blog"
    if blog_dir.is_dir():
        for child in blog_dir.iterdir():
            if child.is_dir() and (child / "index.html").exists():
                urls.append((f"https://martechsignal.com/blog/{child.name}/", _lastmod(child / "index.html"), "0.9"))

    # Tools hub
    tools_hub = ROOT / "tools" / "index.html"
    urls.append((f"https://martechsignal.com/tools/", _lastmod(tools_hub) if tools_hub.exists() else today, "0.8"))

    # Contact page
    contact_html = ROOT / "contact" / "index.html"
    if contact_html.exists():
        urls.append(("https://martechsignal.com/contact/", _lastmod(contact_html), "0.5"))

    # About page
    about_html = ROOT / "about" / "index.html"
    urls.append((f"https://martechsignal.com/about/", _lastmod(about_html) if about_html.exists() else today, "0.5"))

    # Author page
    author_html = ROOT / "authors" / "tim-christensen" / "index.html"
    if author_html.exists():
        urls.append(("https://martechsignal.com/authors/tim-christensen/", _lastmod(author_html), "0.5"))

    # Individual tool pages
    for t in tools:
        if t.get("status") == "active":
            tool_html = TOOLS_DIR / t["slug"] / "index.html"
            lm = _lastmod(tool_html) if tool_html.exists() else today
            urls.append((f"https://martechsignal.com/tools/{t['slug']}/", lm, "0.7"))

    # Category pages
    for c in cats:
        cat_html = ROOT / "categories" / c["slug"] / "index.html"
        lm = _lastmod(cat_html) if cat_html.exists() else today
        urls.append((f"https://martechsignal.com/categories/{c['slug']}/", lm, "0.8"))

    # Glossary hub + term pages
    glossary_json = TOOLS_DIR / "glossary.json"
    if glossary_json.exists():
        glossary_terms = json.loads(glossary_json.read_text())
        gl_hub = ROOT / "glossary" / "index.html"
        urls.append((f"https://martechsignal.com/glossary/", _lastmod(gl_hub) if gl_hub.exists() else today, "0.8"))
        for gt in glossary_terms:
            gl_html = ROOT / "glossary" / gt["slug"] / "index.html"
            lm = _lastmod(gl_html) if gl_html.exists() else today
            urls.append((f"https://martechsignal.com/glossary/{gt['slug']}/", lm, "0.6"))

    # Blog index
    if (blog_dir / "index.html").exists():
        urls.append((f"https://martechsignal.com/blog/", _lastmod(blog_dir / "index.html"), "0.8"))

    # Generate XML
    entries = []
    for loc, lastmod, priority in urls:
        entries.append(f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><priority>{priority}</priority></url>")

    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += '\n'.join(entries)
    sitemap += '\n</urlset>\n'

    (ROOT / "sitemap.xml").write_text(sitemap)
    _save_lastmod_store()
    print(f"\nSitemap: {len(urls)} URLs written to sitemap.xml")

    # Ensure robots.txt exists
    robots_path = ROOT / "robots.txt"
    if not robots_path.exists():
        robots_path.write_text(
            "User-agent: *\nAllow: /\n\n"
            "Sitemap: https://martechsignal.com/sitemap.xml\n"
        )
        print("Robots.txt: created")


def main():
    tools, cats = load()
    active = [t for t in tools if t.get("status") == "active"]
    print(f"Building tool directory: {len(active)} active tools, {len(cats)} categories\n")

    # Hub
    print("Hub:")
    build_hub(tools, cats)

    # Tool pages
    print(f"\nTool pages ({len(active)}):")
    for t in active:
        out = build_tool_page(t, cats, tools)
        print(f"  ✓ {out.relative_to(ROOT)}")

    # Category pages
    print(f"\nCategory pages:")
    for c in cats:
        out = build_category_page(c, tools)
        if out:
            print(f"  ✓ {out.relative_to(ROOT)}")
        else:
            print(f"  · {c['slug']} (empty, skipped)")

    n_hubs = sum(1 for c in cats if c.get("hub"))
    print(f"\nDone! {len(active)} tool pages + {len(cats)} categories + {n_hubs} hub")

    # Sitemap
    build_sitemap(tools, cats)

    # llms.txt for AI-search readiness
    build_llms_txt(tools, cats)

    # Factual-consistency gate (fails the build loudly on contradictions)
    assert_factual_consistency(tools)



def assert_factual_consistency(tools):
    """Post-build gate (audit follow-up): loud failure if any tool page contradicts itself."""
    problems = []
    for t in tools:
        if t.get("status") != "active":
            continue
        slug, model = t["slug"], t.get("pricing_model")
        paid_custom = t.get("price_from") is None or t.get("pricing_model") == "enterprise"
        page = TOOLS_DIR / slug / "index.html"
        if not page.exists():
            continue
        html = page.read_text()
        if re.search(r'"price"\s*:\s*0\b', html) and model in ("enterprise", "paid"):
            problems.append(f"{slug}: offers.price=0 on {model} pricing")
        if paid_custom and "has a free tier" in html:
            problems.append(f"{slug}: FAQ claims free tier on {model} pricing")
        if t.get("name") and f">{esc(t['name'])}</h1>" not in html and len(t.get("name","")) > 3:
            problems.append(f"{slug}: H1 does not match name '{t['name']}'")
    if problems:
        print("FACTUAL CONSISTENCY FAILURES:")
        for p in problems:
            print("  !!", p)
        raise SystemExit(1)
    print("Factual consistency: OK")

def build_llms_txt(tools, cats):
    """Generate llms.txt (site summary + structured inventory for AI crawlers)."""
    import re as _re
    cat_names = {c["slug"]: c["name"] for c in cats}
    lines = [
        "# MartechSignal",
        "",
        "> Independent reviews of AI marketing automation tools. Structured audits of",
        "> 100+ martech platforms — pricing, self-hosting, APIs, and which AI features",
        "> actually ship. No sponsored rankings, no affiliate links.",
        "",
        "## Directory",
        "",
    ]
    active = [t for t in tools if t.get("status") == "active"]
    by_cat = {}
    for t in active:
        by_cat.setdefault(t.get("category", "other"), []).append(t)
    for cslug, ts in sorted(by_cat.items()):
        lines.append(f"### {cat_names.get(cslug, cslug)}")
        lines.append("")
        for t in sorted(ts, key=lambda x: x["name"].lower()):
            tag_full = (t.get("tagline") or "").strip().rstrip(".")
            if len(tag_full) > 110:
                # cut at the last clause boundary (comma/semicolon) before the limit,
                # falling back to a word boundary - never mid-word (audit M8)
                cut = max(tag_full.rfind(",", 0, 110), tag_full.rfind(";", 0, 110))
                if cut >= 40:
                    tag = tag_full[:cut].rstrip(",;:")
                else:
                    sp = tag_full.rfind(" ", 0, 110)
                    tag = tag_full[:sp] + "\u2026" if sp > 30 else tag_full[:110].rsplit(" ", 1)[0] + "\u2026"
            else:
                tag = tag_full
            oss = " (open source)" if t.get("open_source") else ""
            lines.append(f"- [{t['name']}](https://martechsignal.com/tools/{t['slug']}/): {tag}{oss}")
        lines.append("")

    blog_dir = ROOT / "blog"
    posts = []
    if blog_dir.is_dir():
        for child in sorted(blog_dir.iterdir()):
            f = child / "index.html"
            if child.is_dir() and f.exists():
                html_content = f.read_text()
                m = _re.search(r"<title>(.*?)</title>", html_content)
                d = _re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', html_content)
                if m:
                    posts.append((d.group(1) if d else "0000-00-00", child.name,
                                  m.group(1).replace("&amp;", "&").replace("&#x27;", "'")))
    posts.sort(reverse=True)
    lines += ["## Analysis", ""]
    for date, slug, title in posts:
        lines.append(f"- [{title}](https://martechsignal.com/blog/{slug}/) ({date})")
    glossary_json = TOOLS_DIR / "glossary.json"
    if glossary_json.exists():
        glossary_terms = json.loads(glossary_json.read_text())
        lines += ["", "## Glossary", ""]
        for gt in sorted(glossary_terms, key=lambda x: x["term"].lower()):
            lines.append(f"- [{gt['term']}](https://martechsignal.com/glossary/{gt['slug']}/)")
    lines += ["", "## Categories", ""]
    for c in sorted(cats, key=lambda x: x["name"].lower()):
        lines.append(f"- [{c['name']}](https://martechsignal.com/categories/{c['slug']}/)")
    lines += ["", "## Links", "", "- [Blog](https://martechsignal.com/blog/)",
              "- [Tool directory](https://martechsignal.com/tools/)",
              "- [Glossary](https://martechsignal.com/glossary/)",
              "- [Checklist](https://martechsignal.com/checklist/)",
              "- [About / editorial policy](https://martechsignal.com/about/)",
              "- [Author](https://martechsignal.com/authors/tim-christensen/)",
              "- [RSS feed](https://martechsignal.com/rss.xml)", ""]
    out = ROOT / "llms.txt"
    out.write_text("\n".join(lines))
    print(f"llms.txt: {out} ({len(lines)} lines)")

    # llms-full.txt: same inventory with full descriptions per tool (audit M8:
    # AI crawlers that want depth get it without crawling every page)
    full_lines = list(lines)
    for cslug, ts in sorted(by_cat.items()):
        full_lines.append(f"### {cat_names.get(cslug, cslug)}")
        full_lines.append("")
        for t in sorted(ts, key=lambda x: x["name"].lower()):
            desc = (t.get("description") or t.get("tagline") or "").strip()
            if not desc:
                continue
            oss = " Open source." if t.get("open_source") else ""
            price = pricing_label(t)
            full_lines.append(f"[{t['name']}](https://martechsignal.com/tools/{t['slug']}/) \u2014 {price}.{oss}")
            for para in desc.split("\n"):
                para = para.strip()
                if para:
                    full_lines.append(para)
            full_lines.append("")
    full_out = ROOT / "llms-full.txt"
    full_out.write_text("\n".join(full_lines))
    print(f"llms-full.txt: {full_out} ({len(full_lines)} lines)")

if __name__ == "__main__":
    main()
