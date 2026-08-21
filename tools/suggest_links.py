#!/usr/bin/env python3
"""Suggest internal links for a blog post draft.

Scans all published blog posts, scores keyword overlap with the draft,
and outputs suggested links with anchor text. Designed to be called by
the blog pipeline cron after drafting, before publishing.

Usage:
  python3 tools/suggest_links.py <draft_path> [--apply]

Without --apply: prints suggestions to stdout.
With --apply: inserts links into the draft markdown (before the footer).
"""
import json
import re
import sys
import html
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
BLOG_DIR = ROOT / "blog"
CONTENT_DIR = ROOT / "content"
TOOLS_JSON = ROOT / "tools" / "tools.json"

# Words too common to be useful for matching
STOPWORDS = set("""
a an and are as at be by for from has have in is it its of on or that the
this to was were will with your you we they their our can could would should
may might must not no nor so if then than too very just about above after
again all also am any because before being below between both but did do
does doing down during each few further here how into more most other out
over own same some such through under until up what when where which while
who whom why with marketing tool tools ai use using used new one two three
get got make made like know think time way even still back well much many
""".split())


def extract_text(html_or_md: str) -> str:
    """Strip HTML tags and markdown formatting to get plain text."""
    text = re.sub(r'<[^>]+>', ' ', html_or_md)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # markdown links
    text = re.sub(r'[#*_`>]', ' ', text)
    return text.lower()


def keywords(text: str, top_n: int = 40) -> Counter:
    """Extract meaningful keywords from text."""
    words = re.findall(r'[a-z][a-z-]{2,}', text)
    filtered = [w for w in words if w not in STOPWORDS and len(w) > 3]
    return Counter(dict(Counter(filtered).most_common(top_n)))


def score_overlap(draft_kw: Counter, post_kw: Counter) -> float:
    """Score keyword overlap between draft and a published post."""
    draft_set = set(draft_kw.keys())
    post_set = set(post_kw.keys())
    overlap = draft_set & post_set
    if not overlap:
        return 0.0
    # Weight by combined frequency
    score = sum(draft_kw[w] + post_kw[w] for w in overlap)
    return score / (len(draft_set) + len(post_set))


def get_published_posts():
    """Find all published blog posts (HTML in blog/ dir)."""
    posts = []
    if not BLOG_DIR.is_dir():
        return posts
    for child in BLOG_DIR.iterdir():
        index = child / "index.html"
        if child.is_dir() and index.exists():
            content = index.read_text()
            # Extract title from <h1> or <title>
            title_m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
            if not title_m:
                title_m = re.search(r'<title>([^<]+)</title>', content)
            title = html.unescape(title_m.group(1)) if title_m else child.name
            posts.append({
                "slug": child.name,
                "title": title,
                "url": f"/blog/{child.name}/",
                "text": extract_text(content),
            })
    return posts


def get_draft_text(draft_path: Path) -> str:
    """Read draft content (markdown or HTML)."""
    content = draft_path.read_text()
    # Strip frontmatter
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            content = content[end + 3:]
    return content


def suggest_for_text(text: str, max_suggestions: int = 3, exclude_slug: str = ""):
    """Return related published posts for arbitrary source text."""
    source_kw = keywords(extract_text(text))
    scored = []
    for post in get_published_posts():
        if exclude_slug and post["slug"] == exclude_slug:
            continue
        score = score_overlap(source_kw, keywords(post["text"]))
        if score > 0:
            scored.append((score, post))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [
        {"title": post["title"], "url": post["url"], "score": round(score, 3), "slug": post["slug"]}
        for score, post in scored[:max_suggestions]
    ]


def _blog_linked_tool_slugs() -> set:
    """Slugs of tools linked from at least one published blog post's body."""
    linked = set()
    pat = re.compile(r"/tools/([^/\"'\\?#]+)/")
    for f in BLOG_DIR.glob("*/index.html"):
        try:
            html_src = f.read_text()
        except Exception:
            continue
        # body only: cut the head to avoid counting nav/schema links
        body = html_src.split("</head>", 1)[-1]
        linked.update(pat.findall(body))
    return linked


def suggest_tools_for_text(text: str, max_suggestions: int = 3, exclude_slugs: set | None = None, prefer_orphans: bool = False) -> list[dict]:
    """Return related tools for arbitrary source text (blog <-> tools linking).

    Scores keyword overlap between source text and each tool's metadata
    (name + tagline + description + ai_features + integrations).
    Filters out inactive tools and optionally excluded slugs.

    prefer_orphans: boost tools that currently receive zero links from any
    published blog post, so the internal-linking graph stays healthy and no
    tool page becomes an orphan. The boost only breaks ties between
    comparable matches — relevance still dominates.
    """
    if not TOOLS_JSON.exists():
        return []
    try:
        tools = json.loads(TOOLS_JSON.read_text())
    except Exception:
        return []
    source_kw = keywords(extract_text(text))
    exclude_slugs = set(exclude_slugs or [])
    linked = _blog_linked_tool_slugs() if prefer_orphans else set()
    scored: list[tuple[float, dict]] = []
    for t in tools:
        if t.get("status") != "active":
            continue
        if t.get("slug") in exclude_slugs:
            continue
        blob = " ".join(str(t.get(k, "")) for k in ("name", "tagline", "description", "ai_features", "integrations"))
        if not blob.strip():
            continue
        score = score_overlap(source_kw, keywords(extract_text(blob)))
        if score > 0:
            if prefer_orphans and t.get("slug") not in linked:
                score *= 1.5  # orphan boost: relevance still gates entry, this reorders near-ties
            scored.append((score, t))
    scored.sort(key=lambda item: item[0], reverse=True)
    out = []
    for score, t in scored[:max_suggestions]:
        out.append({"name": t["name"], "slug": t["slug"], "url": f"/tools/{t['slug']}/", "score": round(score, 3), "tagline": t.get("tagline", "")})
    return out


def suggest(draft_path: Path, max_suggestions: int = 3):
    """Return list of suggested links for a draft."""
    draft_text = get_draft_text(draft_path)
    draft_kw = keywords(extract_text(draft_text))

    # Derive a slug fragment from the draft filename to exclude self-matches
    draft_stem = draft_path.stem.lower()  # e.g. "ai-agents-need-campaign-state-2026-08-03"
    # Strip trailing date pattern (YYYY-MM-DD) for matching
    draft_key = re.sub(r'-\d{4}-\d{2}-\d{2}$', '', draft_stem)

    # Also extract the draft's title for title-based self-matching
    raw_content = draft_path.read_text()
    draft_title_m = re.search(r'^#\s+(.+)$', raw_content, re.MULTILINE)
    if not draft_title_m:
        fm_title = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', raw_content, re.MULTILINE)
        draft_title_m = fm_title
    draft_title_words = set(re.findall(r'[a-z]{3,}', (draft_title_m.group(1) if draft_title_m else "").lower()))

    posts = get_published_posts()
    scored = []
    for post in posts:
        # Skip self via slug overlap
        post_words = set(post["slug"].split("-"))
        draft_words = set(draft_key.split("-"))
        overlap = post_words & draft_words
        if len(overlap) >= 3 and len(overlap) / max(len(draft_words), 1) >= 0.5:
            continue
        # Skip self via title overlap
        post_title_words = set(re.findall(r'[a-z]{3,}', post["title"].lower()))
        title_overlap = draft_title_words & post_title_words
        if len(title_overlap) >= 3 and len(title_overlap) / max(len(draft_title_words), 1) >= 0.5:
            continue
        post_kw = keywords(post["text"])
        s = score_overlap(draft_kw, post_kw)
        if s > 0:
            scored.append((s, post))

    scored.sort(key=lambda x: x[0], reverse=True)
    suggestions = []
    for score, post in scored[:max_suggestions]:
        # Find a good anchor phrase from the draft that relates to this post
        suggestions.append({
            "title": post["title"],
            "url": post["url"],
            "score": round(score, 3),
            "slug": post["slug"],
        })
    return suggestions


def apply_links(draft_path: Path, suggestions: list) -> str:
    """Insert a 'Related reading' section before the footer/tools-linked line."""
    content = draft_path.read_text()

    # Build the section
    lines = ["\n## Related reading\n"]
    for s in suggestions:
        lines.append(f"- [{s['title']}]({s['url']})")
    section = "\n".join(lines) + "\n"

    # Insert before "Tools linked in this post" if it exists, else at end
    marker = "Tools linked in this post:"
    if marker in content:
        content = content.replace(marker, section + "\n" + marker)
    else:
        content = content.rstrip() + "\n" + section

    draft_path.write_text(content)
    return section


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tools/suggest_links.py <draft_path> [--apply]")
        sys.exit(1)

    draft_path = Path(sys.argv[1])
    if not draft_path.exists():
        print(f"Error: {draft_path} not found")
        sys.exit(1)

    apply = "--apply" in sys.argv
    suggestions = suggest(draft_path)

    if not suggestions:
        print("No related posts found.")
        return

    print(f"Suggested links for: {draft_path.name}\n")
    for s in suggestions:
        print(f"  [{s['score']:.3f}] {s['title']}")
        print(f"         {s['url']}")
    print()

    if apply:
        section = apply_links(draft_path, suggestions)
        print(f"Applied {len(suggestions)} links to {draft_path.name}")
        print(section)
    else:
        print("Run with --apply to insert into draft.")


if __name__ == "__main__":
    main()


_CATEGORY_FILL_PLAN: dict[str, list[str]] = {}

def set_category_fill_plan(plan: dict[str, list[str]]) -> None:
    """Build-level plan: post slug -> ordered tool slugs to link as directory fill."""
    global _CATEGORY_FILL_PLAN
    _CATEGORY_FILL_PLAN = plan or {}

def build_category_fill_plan(max_per_post: int = 4) -> dict[str, list[str]]:
    """Deterministic whole-build plan assigning still-unlinked tools to posts.

    Round-robin over posts (alphabetical) so the fill spreads evenly; tools are
    taken alphabetically per category first, then globally. Computed once per
    build so every rebuild converges instead of rotating targets.
    """
    pat = re.compile(r'/tools/([^/"\'?#]+)/')
    linked = set()
    for f in BLOG_DIR.glob("*/index.html"):
        try:
            body = f.read_text().split("</head>", 1)[-1]
        except Exception:
            continue
        linked.update(pat.findall(body))
    tools = json.loads(TOOLS_JSON.read_text())
    active = [t for t in tools if t.get("status") == "active"]
    orphans = sorted((t for t in active if t["slug"] not in linked), key=lambda t: t["name"].lower())
    if not orphans:
        return {}
    posts = sorted(f.parent.name for f in BLOG_DIR.glob("*/index.html"))
    plan: dict[str, list[str]] = {}
    i = 0
    for o in orphans:
        # give each orphan to the next post in rotation, skipping the post it
        # would naturally duplicate on (a post links a slug only once)
        for _ in range(len(posts)):
            post = posts[i % len(posts)]
            i += 1
            bucket = plan.setdefault(post, [])
            if o["slug"] not in bucket and len(bucket) < max_per_post:
                bucket.append(o["slug"])
                break
    return plan

def suggest_category_fill(text: str, max_suggestions: int = 2, exclude_slugs: set | None = None, post_slug: str = "") -> list[dict]:
    """Return this post's precomputed directory-fill links (see build_category_fill_plan)."""
    if not TOOLS_JSON.exists():
        return []
    try:
        tools = json.loads(TOOLS_JSON.read_text())
    except Exception:
        return []
    exclude_slugs = set(exclude_slugs or [])
    by_slug = {t["slug"]: t for t in tools}
    out = []
    for slug in _CATEGORY_FILL_PLAN.get(post_slug, []):
        t = by_slug.get(slug)
        if not t or t.get("status") != "active" or slug in exclude_slugs:
            continue
        out.append({"name": t["name"], "url": f"/tools/{t['slug']}/", "slug": slug})
        if len(out) >= max_suggestions:
            break
    return out
