#!/usr/bin/env python3
"""SX-6 pilot (2026-09-26, decided by Tim): "<tool> alternatives" pages.

Neutral-publisher pages for the "X alternatives" query class, where today only
conflicted vendors rank themselves. Content lives in tools/alternatives-content.json
(writer-produced, grounded in tools.json); this script only renders it.

Runs BEFORE build_tools.py in deploy.sh so the sitemap scan and the tool-page
interlink see the generated pages.
"""
import json
import re
from pathlib import Path

from build_tools import page_shell, esc, ROOT, pricing_label, out_links

CONTENT = ROOT / "tools" / "alternatives-content.json"
OUT_DIR = ROOT / "alternatives"


def alt_card(item, tools_by_slug):
    t = tools_by_slug[item["slug"]]
    oss = ' <span class="tag oss">OSS</span>' if t.get("open_source") else ""
    return f"""<section class="alt-item" id="{esc(t['slug'])}">
  <h2><a href="/tools/{t['slug']}/">{esc(t['name'])}</a></h2>
  <p class="meta"><span class="tag pricing">{esc(pricing_label(t))}</span>{oss}</p>
  {out_links(t)}
  <p><strong>Best for:</strong> {esc(item['best_for'])}</p>
  <p><strong>Not for:</strong> {esc(item['not_for'])}</p>
  <p>{esc(item['why'])}</p>
</section>
"""





def _billing_label(t):
    """Categorical billing model derived from the catalog's verified price notes.
    Deliberately labels, not numbers (the number rule: only the cost display)."""
    n = (t.get("price_notes") or "").lower()
    if "no published prices" in n or "custom" in n:
        return "Contract, usage-based" if "usage" in n else "Contract"
    unit = ("Task tiers" if "task" in n else
            "Credits" if "credit" in n else
            "Per bot" if "bot/month" in n or "per bot" in n else
            "Per user" if "user/month" in n or "per user" in n else
            "Flat fee" if "flat" in n else "Monthly plans")
    if "lifetime" in n:
        return unit + ", yearly or one-time"
    if "billed yearly" in n or "annual" in n or "paid yearly" in n:
        return unit + ", billed yearly"
    return unit + ", monthly"


def matrix_table(page, tools_by_slug):
    """H-6 (2026-09-27): the scannable comparison the finding asked for."""
    rows = []
    for item in page["items"]:
        t = tools_by_slug[item["slug"]]
        self_host = "Yes" if t.get("open_source") else "No"
        rows.append(
            f'<tr><td><a href="/tools/{t["slug"]}/">{esc(t["name"])}</a></td>'
            f'<td>{esc(pricing_label(t))}</td>'
            f'<td>{esc(_billing_label(t))}</td>'
            f'<td>{self_host}</td>'
            f'<td>{esc(item["best_for"])}</td></tr>')
    return (
        '<table class="alt-matrix"><caption>Compared on the axes that decide the '
        'purchase. Prices as catalogued on each vendor pricing page.</caption><thead><tr>'
        '<th>Tool</th><th>Price</th><th>Billing model</th><th>Self-host</th><th>Best for</th>'
        '</tr></thead><tbody>' + "".join(rows) + "</tbody></table>")

def build():
    data = json.loads(CONTENT.read_text())
    tools = json.loads((ROOT / "tools" / "tools.json").read_text())
    tools_by_slug = {t["slug"]: t for t in tools}
    built = []
    for page in data["pages"]:
        # self-healing title counts (2026-09-27): a stale "5 Tools Compared" survived
        # a 10-item expansion once. Counts derive from the items list now.
        page["seo_title"] = re.sub(r"\d+(?= Tools Compared)", str(len(page["items"])),
                                   page.get("seo_title") or "")
        target = tools_by_slug[page["slug"]]
        body = ['<nav class="crumb"><a href="/">Home</a><span class="crumb-sep" aria-hidden="true">/</span><a href="/alternatives/">Alternatives guides</a> / '
                f'<span>{esc(target["name"])} alternatives</span></nav>',
                f'<h1>{esc(page["title"])}</h1>']
        for para in page["intro"]:
            body.append(f"<p>{esc(para)}</p>")
        body.append(matrix_table(page, tools_by_slug))
        for item in page["items"]:
            assert item["slug"] in tools_by_slug, f"unknown item slug {item['slug']}"
            assert item["slug"] != page["slug"], "target listed as its own alternative"
            body.append(alt_card(item, tools_by_slug))
        body.append(
            f'<p class="alt-back">Read the full assessment of '
            f'<a href="/tools/{target["slug"]}/">{esc(target["name"])}</a>, or browse all '
            f'<a href="/categories/{target["category"]}/">'
            f'{esc(target["category"].replace("-", " "))} tools</a>.</p>')

        items = page["items"]
        schema = {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": page["title"],
            "datePublished": page.get("date_published", ""), "dateModified": page.get("date_updated", ""),
            "author": {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/"},
            "numberOfItems": len(items),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1,
                 "name": tools_by_slug[it["slug"]]["name"],
                 # r7 M8 (2026-09-27): item -> #app reference, matching /categories/
                 "item": {"@id": f"https://martechsignal.com/tools/{it['slug']}/#app",
                          "url": f"https://martechsignal.com/tools/{it['slug']}/"}}
                for i, it in enumerate(items)],
        }
        breadcrumb = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home",
                 "item": "https://martechsignal.com/"},
                {"@type": "ListItem", "position": 2, "name": "Alternatives guides",
                 "item": "https://martechsignal.com/alternatives/"},
                # A3 M-2c (2026-09-27): the schema label must match the visible
                # trail ("HubSpot CRM alternatives"), not the page title with the
                # "Best ... (2026)" wrapper Google would show as the SERP crumb.
                {"@type": "ListItem", "position": 3, "name": (page["title"][5:] if page["title"].startswith("Best ") else page["title"]).removesuffix(" (2026)").strip(),
                 "item": f"https://martechsignal.com/alternatives/{page['slug']}/"},
            ],
        }
        out_dir = OUT_DIR / page["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / "index.html"
        out.write_text(page_shell(
            page["seo_title"], page["meta"], f"/alternatives/{page['slug']}/",
            "\n".join(body), [schema, breadcrumb]))
        built.append(page["slug"])
    print(f"alternatives pages built: {len(built)} ({', '.join(built)})")
    return built


if __name__ == "__main__":
    build()
