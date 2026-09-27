#!/usr/bin/env python3
"""Real markdown mirrors for every page family without a genuine one (A3 M-6/M-7).

The tool and category mirrors are generated from catalog data in build_tools and
are left alone. Everything else (homepage, blog index and posts, hubs, listings,
author, hand pages) previously got 6-line stubs that self-described as mirrors,
and /index.md was a byte-copy of llms.txt. This derives each mirror from the
page's own rendered HTML: title, lead paragraphs, headings and list items.
Run after the page builders in deploy.sh.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_PREFIXES = ()  # H10: every page family gets a real mirror

def html_to_md(html: str) -> str:
    """H10 (2026-09-27): >=95% parity extractor. Tables become pipe tables,
    details/summary become Q/A pairs, dl rows become bullets, inline emphasis kept."""
    title = re.search(r"<title>([^<]+)</title>", html)
    title = title.group(1).split("|")[0].split("\u00b7")[0].strip() if title else "MartechSignal"
    src = re.sub(r"<(script|style|head)[^>]*>.*?</\1>", " ", html, flags=re.S)

    def inline(x):
        x = re.sub(r"<(strong|b)[^>]*>(.*?)</\1>", r"**\2**", x, flags=re.S)
        x = re.sub(r"<(em|i)[^>]*>(.*?)</\1>", r"*\2*", x, flags=re.S)
        x = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r"[\2](\1)", x, flags=re.S)
        x = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", x, flags=re.S)
        x = re.sub(r"<[^>]+>", "", x)
        return re.sub(r"\s+", " ", x).strip()

    out = [f"# {title}", ""]
    for tm in re.finditer(r"<table[^>]*>(.*?)</table>", src, flags=re.S):
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", tm.group(1), flags=re.S)
        grid = [[inline(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, flags=re.S)] for r in rows]
        grid = [g for g in grid if g]
        if len(grid) >= 2:
            w = max(len(g) for g in grid)
            grid = [g + [""] * (w - len(g)) for g in grid]
            tbl = ["| " + " | ".join(grid[0]) + " |",
                   "| " + " | ".join("---" for _ in range(w)) + " |"]
            tbl += ["| " + " | ".join(g) + " |" for g in grid[1:]]
            out += ["", *tbl, ""]
    for dm in re.finditer(r"<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>", src, flags=re.S):
        out += [f"**{inline(dm.group(1))}**", inline(dm.group(2)), ""]
    for dlm in re.finditer(r"<dl[^>]*>(.*?)</dl>", src, flags=re.S):
        for dt in re.finditer(r"<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>", dlm.group(1), flags=re.S):
            out += [f"- **{inline(dt.group(1))}:** {inline(dt.group(2))}"]
        out += [""]
    for lv in re.finditer(r"<(div|section|header|footer|aside)[^>]*>((?:(?!<)[^<]|<(?:/?(?:strong|b|em|i|code|span|br|a|sup|sub|svg|path)\b[^>]*>))*?)</\1>", src, flags=re.S):
        t2 = inline(lv.group(2))
        if t2:
            out += [t2, ""]

    for m2 in re.finditer(r"<(h1|h2|h3|h4|p|li|blockquote|figcaption)[^>]*>(.*?)</\1>", src, flags=re.S):
        tag, inner = m2.group(1), m2.group(2)
        text = inline(inner)
        if not text:
            continue
        if tag == "h2":
            out += ["## " + text, ""]
        elif tag == "h1":
            out += ["## " + text, ""]
        elif tag in ("h3", "h4"):
            out += ["### " + text, ""]
        elif tag == "li":
            out += ["- " + text]
        elif tag == "blockquote":
            out += ["> " + text, ""]
        else:
            out += [text, ""]
    for jl in re.finditer(r'<script type="application/ld[+]json">(.*?)</script>', html, flags=re.S):
        out += ["", "```json", jl.group(1).strip(), "```"]
    return "\n".join(out).strip() + "\n"

def main():
    n = 0
    for idx in sorted(ROOT.glob("*/index.html")) + sorted(ROOT.glob("*/*/index.html")):
        rel = str(idx.parent.relative_to(ROOT))
        if rel == "." or rel.split("/")[0] + "/" in SKIP_PREFIXES:
            continue
        md_path = idx.parent / "index.md"
        md_path.write_text(html_to_md(idx.read_text()))
        n += 1
    home = ROOT / "index.html"
    (ROOT / "index.md").write_text(html_to_md(home.read_text()))
    print(f"markdown mirrors: {n} pages + homepage derived from HTML")

if __name__ == "__main__":
    main()
