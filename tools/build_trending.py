#!/usr/bin/env python3
"""Build trending/index.html for martechsignal.com.

Reads tools/github-history.json (daily snapshots written by github_snapshot.py)
and tools/tools.json (names, categories, tool-page links) and generates a
static momentum page: weekly movers table, per-repo sparklines, and per-category
leaderboards. No external JS; sparklines are inline SVG.

Editorial guardrails (Tim's standing rules):
  - The measurement window is stated on the page, every table row carries it.
  - A repo needs >= MIN_DAYS snapshots to appear anywhere on the page.
  - No extrapolation, no projections, plain numbers only.
"""
import html
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_tools import page_shell  # shared site shell (masthead + footer)

ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = ROOT / "tools"
HIST = TOOLS_DIR / "github-history.json"
MIN_DAYS = 5          # guardrail: repos with fewer snapshots stay off the page
MOVERS_N = 10
SPARK_W, SPARK_H, SPARK_PAD = 96, 28, 3


def esc(s):
    return html.escape(str(s))


def star(n):
    """1,234-style grouping."""
    return f"{n:,}"


def spark_svg(values):
    """Inline SVG polyline of daily star counts. No external JS."""
    if len(values) < 2:
        return ""
    lo, hi = min(values), max(values)
    span = (hi - lo) or 1
    inner_w = SPARK_W - 2 * SPARK_PAD
    inner_h = SPARK_H - 2 * SPARK_PAD
    n = len(values)
    pts = []
    for i, v in enumerate(values):
        x = SPARK_PAD + (i / (n - 1)) * inner_w
        y = SPARK_PAD + inner_h - ((v - lo) / span) * inner_h
        pts.append(f"{x:.1f},{y:.1f}")
    polylines = (
        f'<polyline points="{" ".join(pts)}" fill="none" stroke="#8FA1C0" stroke-opacity="0.5" stroke-width="1.5"/>'
        f'<polyline points="{pts[0]} {pts[-1]}" fill="none" stroke="#FFB224" stroke-width="2"/>'
    )
    label = f"{star(values[0])}&rarr;{star(values[-1])}"
    return (
        f'<svg class="spark" width="{SPARK_W}" height="{SPARK_H}" viewBox="0 0 {SPARK_W} {SPARK_H}" '
        f'role="img" aria-label="Stars per day, first to latest snapshot: {esc(values[0])} to {esc(values[-1])}">'
        f'{polylines}</svg><span class="spark-range">{label}</span>'
    )


def load_data():
    hist = json.loads(HIST.read_text())
    if not hist:
        raise SystemExit("github-history.json is empty; run github_snapshot.py first")
    tools = json.loads((TOOLS_DIR / "tools.json").read_text())
    cats = json.loads((TOOLS_DIR / "categories.json").read_text())
    tmap = {t["slug"]: t for t in tools}
    cat_name = {c["slug"]: c["name"] for c in cats}
    rows = []
    start, end = hist[0], hist[-1]
    for slug, d in end["repos"].items():
        t = tmap.get(slug)
        if not t or t.get("status") != "active":
            continue  # only tools with a live directory page get linked
        series = []
        for snap in hist:
            r = snap["repos"].get(slug)
            if r:
                series.append(r["stars"])
        if len(series) < min(MIN_DAYS, len(hist)):
            continue  # guardrail: not enough snapshots, leave it out entirely
        s0, s1 = series[0], series[-1]
        delta = s1 - s0
        pct = (delta / s0 * 100.0) if s0 else 0.0
        rows.append({
            "slug": slug,
            "name": t["name"],
            "category": t.get("category", ""),
            "cat_name": cat_name.get(t.get("category", ""), t.get("category", "")),
            "stars": s1,
            "start_stars": s0,
            "delta": delta,
            "pct": pct,
            "series": series,
            "days": len(series),
        })
    return hist, rows, start["date"], end["date"]


def fmt_day(iso):
    d = datetime.strptime(iso, "%Y-%m-%d")
    return d.strftime("%b %d").replace(" 0", " ")


def build_page():
    hist, rows, d0, d1 = load_data()
    window = f"{fmt_day(d0)} to {fmt_day(d1)}, 2026"
    n_repos = len(rows)

    movers = sorted(rows, key=lambda r: r["pct"], reverse=True)[:MOVERS_N]

    movers_rows = ""
    for r in movers:
        cls = "up" if r["delta"] > 0 else ("flat" if r["delta"] == 0 else "down")
        movers_rows += (
            f'<tr><td><a href="/tools/{r["slug"]}/">{esc(r["name"])}</a></td>'
            f'<td class="num">{star(r["stars"])}</td>'
            f'<td class="num {cls}">{r["delta"]:+d}</td>'
            f'<td class="num {cls}">{r["pct"]:.2f}%</td>'
            f'<td>{esc(window)}</td></tr>\n'
        )

    # one sparkline grid per category, sorted by its best percentage growth
    by_cat = {}
    for r in rows:
        by_cat.setdefault(r["cat_name"], []).append(r)
    cat_blocks = ""
    for cname in sorted(by_cat, key=lambda c: max(x["pct"] for x in by_cat[c]), reverse=True):
        rs = sorted(by_cat[cname], key=lambda r: r["pct"], reverse=True)
        cells = ""
        for r in rs:
            sign = "" if r["delta"] < 0 else "+"
            cls = "up" if r["delta"] > 0 else ("flat" if r["delta"] == 0 else "down")
            cells += (
                f'<div class="spark-card"><div class="spark-name">'
                f'<a href="/tools/{r["slug"]}/">{esc(r["name"])}</a></div>'
                f'<div class="spark-row">{spark_svg(r["series"])}'
                f'<span class="spark-delta {cls}">{sign}{r["delta"]:+d}</span></div></div>\n'
            )
        cat_blocks += (
            f'<div class="hub-group"><div class="hub-group-label"><span>{esc(cname)}</span>'
            f'<i></i><em>{len(rs)}</em></div><div class="spark-grid">{cells}</div></div>\n'
        )

    body = f"""<nav class="crumb"><a href="/">Home</a> / <a href="/tools/">Tools</a> / <span>Trending</span></nav>
<section class="page-head">
  <h1>Open-source martech momentum</h1>
  <p class="sub">Every morning we snapshot the GitHub stars of the {n_repos} open-source tools in the directory. This page shows what moved in the window {window}, tracked since Aug 25, 2026.</p>
  <p class="count">{n_repos} REPOS &middot; {len(hist)} DAILY SNAPSHOTS &middot; WINDOW {esc(d0)} TO {esc(d1)}</p>
</section>
<section class="trend-note">
  <p>Stars are a weak signal on their own. A repo can sit near the top of GitHub trending for a week on one HN post, and a 500-star project gaining 50 stars is a different story than a 40,000-star project gaining the same 50. The percentages below favor small bases for exactly that reason, so read the absolute deltas next to them. No projections here: just what the snapshots recorded, over the stated window, and nothing else.</p>
</section>
<h2>This week's movers</h2>
<div class="table-wrap"><table>
<thead><tr><th>Tool</th><th>Stars now</th><th>Delta</th><th>Growth</th><th>Window</th></tr></thead>
<tbody>
{movers_rows}</tbody>
</table></div>
<p class="fine">Percentage growth over the full window ({esc(d0)} to {esc(d1)}). Every repo on this page has {len(hist)} daily snapshots, so no number here comes from a partial window.</p>
<h2>Category leaderboards</h2>
<p class="trend-catintro">The same {len(hist)} snapshots, grouped by directory category and ordered by percentage growth inside each group. Tool names link to their directory pages.</p>
{cat_blocks}
<section class="trend-note method">
  <h2>Method</h2>
  <p>A scheduled script calls the GitHub API once per day for every open-source tool in the directory and stores stars, forks, open issues, and last-push date. This page is generated from those snapshots. The window is {esc(d0)} through {esc(d1)} ({len(hist)} snapshots); tracking started Aug 25, 2026, so the page gets more accurate as the history grows. Nothing is annualized, extrapolated, or normalized. Stars measure attention, not usage or quality.</p>
</section>"""

    schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Open-Source MarTech Momentum",
        "description": f"GitHub star momentum for {n_repos} open-source marketing tools, window {d0} to {d1}.",
        "url": "https://martechsignal.com/trending/",
        "isPartOf": {"@type": "WebSite", "name": "MartechSignal", "url": "https://martechsignal.com/"},
        "dateModified": d1,
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://martechsignal.com/"},
            {"@type": "ListItem", "position": 2, "name": "Tools", "item": "https://martechsignal.com/tools/"},
            {"@type": "ListItem", "position": 3, "name": "Trending", "item": "https://martechsignal.com/trending/"},
        ],
    }

    out = ROOT / "trending" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page_shell(
        "Open-Source MarTech Momentum \u2014 GitHub Star Trends | MartechSignal",
        f"Daily GitHub star tracking for {n_repos} open-source marketing tools. Weekly movers, sparklines, and category leaderboards over the stated snapshot window.",
        "/trending/", body, [schema, breadcrumb]))
    print(f"  \u2713 {out.relative_to(ROOT)}  ({len(hist)} snapshots, {n_repos} repos, window {d0}..{d1})")
    return out


if __name__ == "__main__":
    build_page()
