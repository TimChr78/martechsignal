"""Shared page chrome for the 2026-10 redesign.

One source of truth for the head font/theme tags, the top bar + masthead and
the footer. Builders import these helpers so generated pages and hand-authored
pages cannot drift; tools/sync_chrome.py normalizes the files already on disk.
Markup contract: design/DESIGN.md.
"""
from datetime import datetime

HEAD_TAGS = (
    '<link rel="preload" href="/fonts/newsreader-var.woff2" as="font" type="font/woff2" crossorigin>\n'
    '<link rel="preload" href="/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>\n'
    '<script src="/theme.js"></script>'
)

# path prefix -> nav label that gets aria-current="page"
_SECTIONS = (
    ("/tools/", "Tools"),
    ("/best/", "Best"),
    ("/vs/", "Comparisons"),
    ("/alternatives/", "Alternatives"),
    ("/categories/", "Categories"),
    ("/glossary/", "Glossary"),
    ("/blog/", "Blog"),
)


def _current(path):
    p = (path or "").split("?", 1)[0].split("#", 1)[0]
    for prefix, label in _SECTIONS:
        if p == prefix or p.startswith(prefix):
            return label
    return None


def chrome_top(path: str) -> str:
    current = _current(path)

    def link(href, label, cls=""):
        cls_attr = f' class="{cls}"' if cls else ""
        current_attr = ' aria-current="page"' if label == current else ""
        return f'<a{cls_attr} href="{href}"{current_attr}>{label}</a>'

    nav = (
        link("/tools/", "Tools")
        + link("/best/", "Best")
        + link("/vs/", "Comparisons")
        + link("/alternatives/", "Alternatives")
        + link("/categories/", "Categories")
        + link("/glossary/", "Glossary")
        + link("/blog/", "Blog")
        + link("/#subscribe", "Subscribe", "nav-sub")
    )
    return f"""<div class="topbar"><div class="wrap topbar-in">
  <p class="topbar-tag">Independent research on AI marketing automation</p>
  <button class="theme-toggle" type="button" hidden aria-label="Switch to dark theme"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 2a6 6 0 0 0 0 12z" fill="currentColor"/></svg><span class="tt-label">Dark</span></button>
</div></div>
<header class="masthead"><div class="wrap mast-in">
  <a class="wordmark" href="/">MartechSignal<span class="mark" aria-hidden="true"><i></i><i></i><i></i></span></a>
  <nav class="mast-nav" aria-label="Primary">{nav}</nav>
</div></header>"""


def chrome_footer() -> str:
    year = datetime.now().year
    return f"""<footer class="site-foot"><div class="wrap foot-cols">
  <div class="foot-brand">
    <p class="foot-wm">MartechSignal</p>
    <p>Independent research on AI marketing automation, written by <a href="/authors/tim-christensen/">Tim Christensen</a>. No affiliate links. No sponsored rankings.</p>
    <p class="fine">© {year} MartechSignal</p>
  </div>
  <nav class="foot-col" aria-label="Research"><p class="foot-h">Research</p><a href="/tools/">Tools</a><a href="/best/">Best</a><a href="/vs/">Comparisons</a><a href="/alternatives/">Alternatives</a><a href="/categories/">Categories</a><a href="/trending/">Trending</a><a href="/checklist/">Checklist</a></nav>
  <nav class="foot-col" aria-label="Read"><p class="foot-h">Read</p><a href="/blog/">Blog</a><a href="/guides/">Guides</a><a href="/glossary/">Glossary</a><a href="/rss.xml">RSS</a><a href="/#subscribe">Subscribe</a></nav>
  <nav class="foot-col" aria-label="About"><p class="foot-h">About</p><a href="/about/">About</a><a href="/authors/tim-christensen/">Author</a><a href="/methodology/">Methodology</a><a href="/corrections/">Corrections</a><a href="/ai-policy/">AI policy</a><a href="/llms.txt">AI catalog</a><a href="/contact/">Contact</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></nav>
</div></footer>"""
