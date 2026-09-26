#!/usr/bin/env python3
"""SX-6 pilot (2026-09-26, decided by Tim): "<tool> alternatives" pages.

Neutral-publisher pages for the "X alternatives" query class, where today only
conflicted vendors rank themselves. Content lives in tools/alternatives-content.json
(writer-produced, grounded in tools.json); this script only renders it.

Runs BEFORE build_tools.py in deploy.sh so the sitemap scan and the tool-page
interlink see the generated pages.
"""
import json
from pathlib import Path

from build_tools import page_shell, esc, ROOT, pricing_label

CONTENT = ROOT / "tools" / "alternatives-content.json"
OUT_DIR = ROOT / "alternatives"


def alt_card(item, tools_by_slug):
    t = tools_by_slug[item["slug"]]
    oss = ' <span class="tag oss">OSS</span>' if t.get("open_source") else ""
    return f"""<section class="alt-item" id="{esc(t['slug'])}">
  <h2><a href="/tools/{t['slug']}/">{esc(t['name'])}</a></h2>
  <p class="meta"><span class="tag pricing">{esc(pricing_label(t))}</span>{oss}</p>
  <p><strong>Best for:</strong> {esc(item['best_for'])}</p>
  <p><strong>Not for:</strong> {esc(item['not_for'])}</p>
  <p>{esc(item['why'])}</p>
</section>
"""


def build():
    data = json.loads(CONTENT.read_text())
    tools = json.loads((ROOT / "tools" / "tools.json").read_text())
    tools_by_slug = {t["slug"]: t for t in tools}
    built = []
    for page in data["pages"]:
        target = tools_by_slug[page["slug"]]
        body = ['<nav class="crumb"><a href="/">Home</a> / <a href="/tools/">Tools</a> / '
                f'<span>{esc(target["name"])} alternatives</span></nav>',
                f'<h1>{esc(page["title"])}</h1>']
        for para in page["intro"]:
            body.append(f"<p>{esc(para)}</p>")
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
            "numberOfItems": len(items),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1,
                 "name": tools_by_slug[it["slug"]]["name"],
                 "url": f"https://martechsignal.com/tools/{it['slug']}/"}
                for i, it in enumerate(items)],
        }
        breadcrumb = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home",
                 "item": "https://martechsignal.com/"},
                {"@type": "ListItem", "position": 2, "name": "Tools",
                 "item": "https://martechsignal.com/tools/"},
                {"@type": "ListItem", "position": 3, "name": page["title"],
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
