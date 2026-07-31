#!/usr/bin/env python3
"""Generate static HTML pages for the MartechSignal tool directory.

Reads tools/tools.json + tools/categories.json → outputs:
  - tools/index.html          (directory hub)
  - tools/{slug}.html         (tool profiles)
  - categories/{slug}.html    (category listings)

Run from /opt/data/martechsignal/:  python3 tools/build_tools.py
"""
import json, os, html, re
from pathlib import Path
from datetime import datetime

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

# ── Shared HTML shell ──────────────────────────────────────────────

def page_shell(title, description, canonical, body, schema_json=None):
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
<link rel="canonical" href="https://martechsignal.com{canonical}">
<meta name="msvalidate.01" content="B3427474AF36B6861E22592403BA8B27">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet">
{schema_block}
<link rel="stylesheet" href="/style.css">
</head>
<body class="page-tools">
<div class="bg" aria-hidden="true"></div>
<header class="masthead">
  <div class="wrap mast-in">
    <a class="wordmark" href="/">MARTECH<b>SIGNAL</b><span class="cursor">▮</span></a>
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
      <a href="/blog/">BLOG</a>
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

    # Overview paragraph
    if t.get('description'):
        overview_html = f'<p>{esc(t["description"])}</p>'
    else:
        price_str = ('$'+str(t['price_from'])+'/mo') if t.get('price_from') is not None else 'custom pricing'
        overview_html = f'<p>{esc(t.get("tagline",""))} {esc(t["name"])} is a {esc(c.get("name","").lower())} tool with {"free" if t.get("price_from",1)==0 else "paid"} pricing starting at {price_str}.</p>'

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
    {related_html}
  </div>
  <aside class="sidebar">
    <div class="side-card">
      <h3>Quick Facts</h3>
      <dl>
        <div class="side-row"><dt>Pricing</dt><dd>{esc(pricing_label(t))}</dd></div>
        <div class="side-row"><dt>Category</dt><dd><a href="/categories/{t['category']}/">{esc(c.get('name',''))}</a></dd></div>
        {'<div class="side-row"><dt>G2 Rating</dt><dd>★ ' + str(t['g2_rating']) + ' (' + str(t.get('g2_reviews','')) + ')</dd></div>' if t.get('g2_rating') else ''}
        {'<div class="side-row"><dt>GitHub</dt><dd>★ ' + str(t['github_stars']) + '</dd></div>' if t.get('github_stars') else ''}
        {'<div class="side-row"><dt>Founded</dt><dd>' + str(t['founded']) + '</dd></div>' if t.get('founded') else ''}
        {'<div class="side-row"><dt>HQ</dt><dd>' + esc(t['hq']) + '</dd></div>' if t.get('hq') else ''}
        <div class="side-row"><dt>API</dt><dd>{'Yes' if t.get('api_available') else 'No'}</dd></div>
      </dl>
    </div>
    <div class="side-card">
      <a class="btn-sm" href="{esc(t.get('website','#'))}" target="_blank" rel="noopener">Visit {esc(t['name'])} →</a>
    </div>
    {'<div class="side-card"><h3>Pricing</h3><p style="color:var(--muted);font-size:.9rem">' + esc(t.get('price_notes','')) + '</p><div style="margin-top:.8rem"><a style="font:600 .74rem var(--mono);color:var(--amber);text-decoration:none" href="' + esc(t.get('pricing_url','#')) + '" target="_blank" rel="noopener">VIEW PRICING →</a></div></div>' if t.get('price_notes') else ''}
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
    if t.get("g2_rating"):
        schema["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": t["g2_rating"],
            "reviewCount": t.get("g2_reviews", 0),
            "bestRating": 5
        }
    if t.get("price_from") is not None:
        schema["offers"] = {
            "@type": "Offer",
            "price": t["price_from"],
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

    out_dir = TOOLS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    out.write_text(page_shell(
        f"{t['name']} — AI Marketing Tool | MartechSignal",
        f"{t.get('tagline','')} Pricing, AI features, integrations, and alternatives.",
        f"/tools/{slug}/", body, [schema, breadcrumb]))
    return out

# ── Category pages ─────────────────────────────────────────────────

def build_category_page(cat, tools):
    if cat["slug"] == "open-source":
        # Show ALL open-source tools regardless of primary category
        cat_tools = [t for t in sorted(tools, key=lambda x: x["name"].lower()) if t.get("open_source") and t.get("status") == "active"]
    else:
        cat_tools = [t for t in sorted(tools, key=lambda x: x["name"].lower()) if t["category"] == cat["slug"] and t.get("status") == "active"]
    if not cat_tools:
        return None

    cards = ""
    for t in cat_tools:
        tags = f'<span class="tag pricing">{esc(pricing_label(t))}</span>'
        if t.get("open_source"):
            tags += '<span class="tag oss">OSS</span>'
        cards += f"""<a class="tool-card" href="/tools/{t['slug']}/">
  <div class="name">{esc(t['name'])}</div>
  <div class="tagline">{esc(t.get('tagline',''))}</div>
  <div class="meta">{tags}</div>
</a>\n"""

    body = f"""<nav class="crumb"><a href="/">Home</a> / <a href="/tools/">Tools</a> / <span>{esc(cat['name'])}</span></nav>
<section class="page-head">
  <h1>{esc(cat['name'])} Tools</h1>
  <p class="sub">{esc(cat.get('description',''))}</p>
  <p class="count">{len(cat_tools)} TOOLS IN THIS CATEGORY</p>
</section>
<div class="tool-grid">{cards}</div>"""

    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": f"{cat['name']} Tools",
        "description": cat.get("description", ""),
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
        f"{cat['name']} Tools — MartechSignal",
        f"Browse {len(cat_tools)} {cat['name'].lower()} tools for AI-powered marketing automation.",
        f"/categories/{cat['slug']}/", body, schema))
    return out

# ── Main ───────────────────────────────────────────────────────────

# ── Sitemap ────────────────────────────────────────────────────────

def build_sitemap(tools, cats):
    today = datetime.now().strftime("%Y-%m-%d")
    urls = []

    # Homepage
    urls.append((f"https://martechsignal.com/", today, "1.0"))

    # Blog posts (scan blog/ for subdirectories containing index.html)
    blog_dir = ROOT / "blog"
    if blog_dir.is_dir():
        for child in blog_dir.iterdir():
            if child.is_dir() and (child / "index.html").exists():
                urls.append((f"https://martechsignal.com/blog/{child.name}/", today, "0.9"))

    # Tools hub
    urls.append((f"https://martechsignal.com/tools/", today, "0.8"))

    # Individual tool pages
    for t in tools:
        if t.get("status") == "active":
            urls.append((f"https://martechsignal.com/tools/{t['slug']}/", today, "0.7"))

    # Category pages
    for c in cats:
        urls.append((f"https://martechsignal.com/categories/{c['slug']}/", today, "0.8"))

    # Glossary hub + term pages
    glossary_json = TOOLS_DIR / "glossary.json"
    if glossary_json.exists():
        glossary_terms = json.loads(glossary_json.read_text())
        urls.append((f"https://martechsignal.com/glossary/", today, "0.8"))
        for gt in glossary_terms:
            urls.append((f"https://martechsignal.com/glossary/{gt['slug']}/", today, "0.6"))

    # Blog index
    if (blog_dir / "index.html").exists():
        urls.append((f"https://martechsignal.com/blog/", today, "0.8"))

    # Generate XML
    entries = []
    for loc, lastmod, priority in urls:
        entries.append(f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><priority>{priority}</priority></url>")

    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += '\n'.join(entries)
    sitemap += '\n</urlset>\n'

    (ROOT / "sitemap.xml").write_text(sitemap)
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

    print(f"\nDone! {len(active)} tool pages + {len(cats)} categories + 1 hub")

    # Sitemap
    build_sitemap(tools, cats)

if __name__ == "__main__":
    main()
