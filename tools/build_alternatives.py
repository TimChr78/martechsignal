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

from build_tools import page_shell, esc, ROOT, pricing_label, out_links, _tool_fact_img
from build_tools import _pilot_shot

CONTENT = ROOT / "tools" / "alternatives-content.json"
OUT_DIR = ROOT / "alternatives"


def alt_card(item, tools_by_slug, target_name=""):
    t = tools_by_slug[item["slug"]]
    oss = ' <span class="tag oss">OSS</span>' if t.get("open_source") else ""
    # r20 M-5 (2026-10-02): bare tool-name H2s carry no query language -
    # head each card as an alternative to the page's target.
    _h2 = f"{esc(t['name'])} as a {esc(target_name)} alternative" if target_name else esc(t["name"])
    return f"""<section class="alt-item" id="{esc(t['slug'])}">
  <h2><a href="/tools/{t['slug']}/">{_h2}</a></h2>
  <p class="meta"><span class="tag pricing">{esc(pricing_label(t))}</span>{oss}</p>
  {_tool_fact_img(t)}
  {_pilot_shot(t['slug'], t['name'])}
  {out_links(t)}
  <p><strong>Best for:</strong> {esc(item['best_for'])}</p>
  <p><strong>Not for:</strong> {esc(item['not_for'])}</p>
  <p>{esc(item['why'])}</p>
</section>
"""





def _billing_label(t):
    """r22 H-1 (2026-10-02): derive the billing model from the record's OWN
    pricing_model first; only fall back to price_notes wording when the model
    is known. The r20 heuristic keyword-matched notes into "Contract" for
    self-serve tools (Make "Contract" beside "Core $9/mo") - wrong-by-inference
    on 166 records with billing: null."""
    model = str(t.get("pricing_model") or "").lower()
    if model in ("free",):
        return "Free"
    if model == "freemium":
        return "Freemium, self-serve tiers"
    if model == "open-source":
        return "Free self-host" + (", paid cloud" if "cloud" in (t.get("price_notes") or "").lower() else "")
    if model == "enterprise":
        return "Contract"
    n = (t.get("price_notes") or "").lower()
    if "no published prices" in n or "custom" in n:
        return "Contract, usage-based" if "usage" in n else "Contract"
    # genuinely unknown: say so instead of guessing
    return "See vendor"


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
        '<div class="table-wrap"><table class="alt-matrix"><caption>Compared on the axes that decide the '
        'purchase. Prices as catalogued on each vendor pricing page.</caption><thead><tr>'
        '<th>Tool</th><th>Price</th><th>Billing model</th><th>Self-host</th><th>Best for</th>'
        '</tr></thead><tbody>' + "".join(rows) + "</tbody></table></div>")

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
        # r21 M-7 (2026-10-02): answer-first slot matching the /best/ and /vs/
        # direct-answer pattern - the verdict opens the page.
        if page.get("direct_answer"):
            body.append(f'<p class="direct-answer">{esc(page["direct_answer"])}</p>')
        for para in page["intro"]:
            body.append(f"<p>{esc(para)}</p>")
        # r11 H-4 (2026-09-29): visible freshness stamp (was JSON-LD only).
        _adu = page.get("date_updated", "")
        if _adu:
            body.append(
                f'<p class="meta">Last verified <time datetime="{esc(_adu)}">{esc(_adu)}</time>.</p>')
        body.append(matrix_table(page, tools_by_slug))
        for item in page["items"]:
            assert item["slug"] in tools_by_slug, f"unknown item slug {item['slug']}"
            assert item["slug"] != page["slug"], "target listed as its own alternative"
            body.append(alt_card(item, tools_by_slug, target["name"]))
        # r11 H-4 (2026-09-29): same 3-question FAQ rollout as best/vs pages.
        for _qa in (page.get("pilot_faq") or []):
            body.append(f'<h2>{esc(_qa["q"])}</h2><p>{esc(_qa["a"])}</p>')
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
            # r15 M-2 (2026-09-29): money-template graphs join publisher + site.
            "publisher": {"@id": "https://martechsignal.com/#organization"},
            "isPartOf": {"@id": "https://martechsignal.com/#website"},
            "numberOfItems": len(items),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1,
                 "name": tools_by_slug[it["slug"]]["name"],
                 # r7 M8 (2026-09-27): item -> #app reference, matching /categories/
                 # r11 M-13 (2026-09-29): typed SoftwareApplication node, not a
                 # bare stub — hub families now model items identically.
                 "item": {"@type": "SoftwareApplication",
                          "@id": f"https://martechsignal.com/tools/{it['slug']}/#app",
                          "url": f"https://martechsignal.com/tools/{it['slug']}/",
                          "name": tools_by_slug[it["slug"]]["name"]}}
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
