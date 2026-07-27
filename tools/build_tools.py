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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet">
{schema_block}
<style>
:root{{
  --bg:#080E1A; --card:#0F1B31; --line:#1D2B47; --line2:#2A3D63;
  --text:#E9EEF8; --muted:#8FA1C0; --amber:#FFB224; --green:#3DDC97; --red:#FF5C5C;
  --mono:'Spline Sans Mono',ui-monospace,monospace; --disp:'Archivo Black',sans-serif; --body:'Archivo',sans-serif;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{background:var(--bg);color:var(--text);font-family:var(--body);line-height:1.65;-webkit-font-smoothing:antialiased}}
::selection{{background:var(--amber);color:#141005}}
a{{color:inherit}}
.bg{{position:fixed;inset:0;z-index:-1;
  background:
    radial-gradient(900px 520px at 88% -8%, rgba(255,178,36,.11), transparent 62%),
    radial-gradient(760px 560px at -12% 34%, rgba(61,220,151,.07), transparent 60%),
    radial-gradient(700px 400px at 60% 110%, rgba(255,92,92,.05), transparent 60%),
    var(--bg);}}
.mono{{font-family:var(--mono)}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 1.25rem}}
.masthead{{border-bottom:1px solid var(--line)}}
.mast-in{{display:flex;align-items:center;justify-content:space-between;padding:1.1rem 0}}
.wordmark{{font-family:var(--disp);font-size:1.15rem;letter-spacing:.03em;text-decoration:none}}
.wordmark b{{color:var(--amber);font-weight:inherit}}
.cursor{{color:var(--amber);animation:blink 1.1s steps(2) infinite;margin-left:2px}}
@keyframes blink{{50%{{opacity:0}}}}

/* breadcrumb */
.crumb{{padding:1.2rem 0 .4rem;font:500 .72rem var(--mono);letter-spacing:.1em;color:var(--muted)}}
.crumb a{{color:var(--muted);text-decoration:none;transition:color .2s}}
.crumb a:hover{{color:var(--amber)}}
.crumb span{{color:var(--amber)}}

/* page header */
.page-head{{padding:2.2rem 0 1.6rem;border-bottom:1px solid var(--line)}}
.page-head h1{{font-family:var(--disp);font-weight:400;font-size:clamp(1.8rem,4vw,2.8rem);letter-spacing:-.01em}}
.page-head .sub{{color:var(--muted);font-size:1.05rem;margin-top:.6rem;max-width:42rem}}
.page-head .count{{font:600 .72rem var(--mono);letter-spacing:.14em;color:var(--amber);margin-top:.8rem}}

/* tool grid */
.tool-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:1.2rem;padding:1.8rem 0}}
.tool-card{{background:var(--card);border:1px solid var(--line2);border-radius:10px;padding:1.4rem 1.5rem;text-decoration:none;transition:border-color .25s,transform .25s,box-shadow .25s;display:flex;flex-direction:column;gap:.6rem}}
.tool-card:hover{{border-color:var(--amber);transform:translateY(-3px);box-shadow:0 12px 36px rgba(2,6,16,.5)}}
.tool-card .name{{font:700 1.1rem var(--body);letter-spacing:-.01em}}
.tool-card .tagline{{color:var(--muted);font-size:.9rem;line-height:1.5;flex:1}}
.tool-card .meta{{display:flex;gap:.6rem;flex-wrap:wrap;align-items:center}}
.tag{{font:600 .64rem var(--mono);letter-spacing:.1em;padding:.25rem .6rem;border-radius:4px;border:1px solid var(--line2);color:var(--muted)}}
.tag.pricing{{border-color:rgba(61,220,151,.35);color:var(--green);background:rgba(61,220,151,.07)}}
.tag.cat{{border-color:rgba(255,178,36,.3);color:var(--amber);background:rgba(255,178,36,.06)}}
.tag.oss{{border-color:rgba(61,220,151,.35);color:var(--green)}}

/* category nav */
.cat-nav{{display:flex;gap:.6rem;flex-wrap:wrap;padding:1.2rem 0}}
.cat-pill{{font:600 .72rem var(--mono);letter-spacing:.08em;padding:.45rem .9rem;border-radius:99px;border:1px solid var(--line2);color:var(--muted);text-decoration:none;transition:all .2s}}
.cat-pill:hover,.cat-pill.active{{border-color:var(--amber);color:var(--amber);background:rgba(255,178,36,.06)}}

/* tool detail */
.detail{{display:grid;grid-template-columns:1fr 340px;gap:2.4rem;padding:2rem 0}}
@media(max-width:880px){{.detail{{grid-template-columns:1fr}}}}
.detail-main h2{{font-family:var(--disp);font-weight:400;font-size:1.3rem;margin:1.8rem 0 .8rem}}
.detail-main h2:first-child{{margin-top:0}}
.detail-main p{{color:#C8D2E4;font-size:.97rem;line-height:1.7;margin-bottom:.8rem}}
.feat-list{{list-style:none;display:grid;gap:.4rem}}
.feat-list li{{display:flex;align-items:center;gap:.6rem;font-size:.92rem;color:#C8D2E4}}
.feat-list li::before{{content:"▸";color:var(--amber);font-size:.7rem}}
.integ-list{{display:flex;gap:.5rem;flex-wrap:wrap}}
.integ-list span{{font:500 .78rem var(--mono);padding:.3rem .7rem;border-radius:4px;background:rgba(15,27,49,.8);border:1px solid var(--line2);color:var(--muted)}}

/* sidebar */
.sidebar{{position:sticky;top:1.5rem;align-self:start}}
.side-card{{background:var(--card);border:1px solid var(--line2);border-radius:10px;padding:1.4rem 1.5rem;margin-bottom:1rem}}
.side-card h3{{font:600 .7rem var(--mono);letter-spacing:.14em;color:var(--amber);margin-bottom:.9rem;text-transform:uppercase}}
.side-row{{display:flex;justify-content:space-between;align-items:baseline;padding:.5rem 0;border-top:1px dashed var(--line2)}}
.side-row:first-of-type{{border-top:none}}
.side-row dt{{font:500 .72rem var(--mono);letter-spacing:.1em;color:var(--muted)}}
.side-row dd{{font:600 .86rem var(--body)}}
.side-row dd a{{color:var(--amber);text-decoration:none}}
.side-row dd a:hover{{text-decoration:underline}}
.btn-sm{{display:inline-block;background:var(--amber);color:#141005;font:700 .85rem var(--body);text-decoration:none;padding:.65rem 1.3rem;border-radius:6px;text-align:center;transition:transform .2s,box-shadow .2s;width:100%}}
.btn-sm:hover{{transform:translateY(-2px);box-shadow:0 8px 24px rgba(255,178,36,.3)}}

/* footer */
footer{{border-top:1px solid var(--line);padding:2.2rem 0;margin-top:2rem}}
.foot-links{{display:flex;gap:1.6rem;flex-wrap:wrap;align-items:center;margin-bottom:1rem}}
.foot-links a{{font:600 .74rem var(--mono);letter-spacing:.12em;color:var(--muted);text-decoration:none;transition:color .2s}}
.foot-links a:hover{{color:var(--amber)}}
.fine{{font:500 .64rem var(--mono);letter-spacing:.14em;color:#5A6C8F}}
</style>
</head>
<body>
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

    body = f"""<nav class="crumb"><a href="/">Home</a> / <a href="/tools/">Tools</a> / <a href="/categories/{t['category']}/">{esc(c.get('name',''))}</a> / <span>{esc(t['name'])}</span></nav>
<section class="page-head">
  <h1>{esc(t['name'])}</h1>
  <p class="sub">{esc(t.get('tagline',''))}</p>
  <p class="count">{esc(c.get('name',''))} · {esc(pricing_label(t))}{' · OPEN SOURCE' if t.get('open_source') else ''}</p>
</section>
<div class="detail">
  <div class="detail-main">
    <h2>Overview</h2>
    <p>{esc(t.get('tagline',''))} {esc(t['name'])} is a {esc(c.get('name','').lower())} tool with {'free' if t.get('price_from',1)==0 else 'paid'} pricing starting at {('$'+str(t['price_from'])+'/mo') if t.get('price_from') else 'custom pricing'}.</p>
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

if __name__ == "__main__":
    main()
