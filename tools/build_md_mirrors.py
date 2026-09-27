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

SKIP_PREFIXES = ("tools/", "categories/")

def html_to_md(html: str) -> str:
    title = re.search(r"<title>([^<]+)</title>", html)
    title = title.group(1).split("|")[0].split("\u00b7")[0].strip() if title else "MartechSignal"
    body = re.search(r"<(article|main)[^>]*>(.*?)</\1>", html, flags=re.S)
    src = body.group(2) if body else html
    src = re.sub(r"<(script|style|nav|footer)[^>]*>.*?</\1>", " ", src, flags=re.S)
    out = [f"# {title}", ""]
    for chunk in re.split(r"<(h2|h3|p|li)[^>]*>", src):
        pass
    for m in re.finditer(r"<(h2|h3|p|li)[^>]*>(.*?)</\1>", src, flags=re.S):
        tag, inner = m.group(1), m.group(2)
        text = re.sub(r"<[^>]+>", "", inner)
        text = re.sub(r"\s+", " ", text).strip()
        if not text or len(text) < 12:
            continue
        if tag == "h2":
            out += [f"## {text}", ""]
        elif tag == "h3":
            out += [f"### {text}", ""]
        elif tag == "li":
            out.append(f"- {text}")
        else:
            out += [text, ""]
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
