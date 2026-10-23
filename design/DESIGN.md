# MartechSignal design system (2026-10 redesign)

Reference mockup: `design/mockup.src.html` (open `design/mockup.html` for the
self-contained version with embedded fonts). This document is the contract
between templates (Python builders + hand-authored HTML) and `style.css`.

## Principles

- Editorial research publication, not a SaaS landing page.
- Serif headlines and reading text, sans for interface. **No uppercase,
  letter-spaced mono labels.** Every UI string is sentence case
  ("All posts →", not "ALL POSTS →").
- One accent colour (vermilion). Hierarchy comes from type, rules and space,
  not from glows, gradients, shadows or rounded cards.
- No decorative motion: no pulsing dots, no hover lift, no scroll reveals.
- Light and dark themes are equals. Default follows the OS; the user can
  override it with the toggle, and the choice persists (localStorage `ms-theme`).

## Tokens (defined once in `style.css`; never hard-code colours elsewhere)

| token | light | dark | use |
|---|---|---|---|
| `--bg` | `#F6F4EF` | `#131312` | page |
| `--surface` | `#FFFFFF` | `#1B1B19` | raised panels (score box, subscribe) |
| `--sunk` | `#EFECE5` | `#0E0E0D` | tags, notes, row hover, code |
| `--ink` | `#18181B` | `#ECE9E2` | primary text |
| `--ink-2` | `#3F3D39` | `#CFCBC2` | secondary text, ledes |
| `--muted` | `#67635B` | `#9C978D` | meta, captions, labels |
| `--line` | `#DDD8CD` | `#2D2C29` | hairlines |
| `--rule` | `#18181B` | `#ECE9E2` | strong section rules |
| `--accent` | `#B93A1A` | `#F0754F` | links underline, labels, primary CTA |
| `--accent-ink` | `#FFFFFF` | `#131312` | text on accent |
| `--tint` | `#F5E4DC` | `#2B1C16` | accent-tinted background |
| `--pos` / `--neg` | `#1E6F47` / `#B42318` | `#5DBE8A` / `#F08A74` | good / bad scores |

Fonts: `--serif` Newsreader (variable 400–600, `/fonts/newsreader-var.woff2`,
italic `/fonts/newsreader-italic-var.woff2`), `--sans` Archivo (variable
400–700, `/fonts/archivo-var.woff2`), `--code` system monospace stack.
Archivo Black and Spline Sans Mono are retired.

Legacy token names (`--card`, `--line2`, `--text`, `--amber`, `--green`,
`--red`, `--mono`, `--disp`, `--body`) stay as aliases in `style.css` so
old inline styles keep working, but new code must use the names above.

## Theme mechanism

1. `/theme.js` is loaded **synchronously** in `<head>` (before the stylesheet
   tags) as `<script src="/theme.js"></script>`. It reads
   `localStorage['ms-theme']` and, if it is `light` or `dark`, sets
   `data-theme` on `<html>`. Nothing else. (CSP allows `'self'` scripts; no
   inline script allowed.)
2. CSS: light tokens on `:root`; dark tokens on `:root[data-theme=dark]` and
   on `:root:not([data-theme=light])` inside
   `@media (prefers-color-scheme: dark)`.
3. `site.js` wires the toggle button: un-hides it, flips the effective theme,
   writes `localStorage['ms-theme']`, updates the label and `aria-label`, and
   follows OS changes while no explicit choice is stored.

## Shared page chrome (exact markup)

### Head, font + theme tags (replace the old three font preloads)

```html
<link rel="preload" href="/fonts/newsreader-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<script src="/theme.js"></script>
```

### Top bar + masthead (first thing inside `<body>`)

```html
<div class="topbar"><div class="wrap topbar-in">
  <p class="topbar-tag">Independent research on AI marketing automation</p>
  <button class="theme-toggle" type="button" hidden aria-label="Switch to dark theme"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 2a6 6 0 0 0 0 12z" fill="currentColor"/></svg><span class="tt-label">Dark</span></button>
</div></div>
<header class="masthead"><div class="wrap mast-in">
  <a class="wordmark" href="/">MartechSignal<span class="mark" aria-hidden="true"><i></i><i></i><i></i></span></a>
  <nav class="mast-nav" aria-label="Primary"><a href="/tools/">Tools</a><a href="/best/">Best</a><a href="/vs/">Comparisons</a><a href="/alternatives/">Alternatives</a><a href="/categories/">Categories</a><a href="/glossary/">Glossary</a><a href="/blog/">Blog</a><a class="nav-sub" href="/#subscribe">Subscribe</a></nav>
</div></header>
```

The nav link whose section contains the current page gets
`aria-current="page"` (e.g. every `/tools/...` page marks Tools; `/blog/...`
marks Blog). Home marks nothing.

Removed from every page: `<div class="bg">`, `.dot-grid`, `.glow*` divs,
`.pulse-dot` span. `#progress` (reading progress bar on posts) stays.

### Footer (last thing before scripts at end of `<body>`)

```html
<footer class="site-foot"><div class="wrap foot-cols">
  <div class="foot-brand">
    <p class="foot-wm">MartechSignal</p>
    <p>Independent research on AI marketing automation, written by <a href="/authors/tim-christensen/">Tim Christensen</a>. No affiliate links. No sponsored rankings.</p>
    <p class="fine">© {YEAR} MartechSignal</p>
  </div>
  <nav class="foot-col" aria-label="Research"><p class="foot-h">Research</p><a href="/tools/">Tools</a><a href="/best/">Best</a><a href="/vs/">Comparisons</a><a href="/alternatives/">Alternatives</a><a href="/categories/">Categories</a><a href="/trending/">Trending</a><a href="/checklist/">Checklist</a></nav>
  <nav class="foot-col" aria-label="Read"><p class="foot-h">Read</p><a href="/blog/">Blog</a><a href="/guides/">Guides</a><a href="/glossary/">Glossary</a><a href="/rss.xml">RSS</a><a href="/#subscribe">Subscribe</a></nav>
  <nav class="foot-col" aria-label="About"><p class="foot-h">About</p><a href="/about/">About</a><a href="/authors/tim-christensen/">Author</a><a href="/methodology/">Methodology</a><a href="/corrections/">Corrections</a><a href="/ai-policy/">AI policy</a><a href="/llms.txt">AI catalog</a><a href="/contact/">Contact</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></nav>
</div></footer>
```

## Components (class names styled by `style.css`)

Existing class names are kept wherever possible so builders need no markup
change; `style.css` restyles them. New classes introduced by the redesign:

- `.eyebrow`: small sans label in accent colour above a headline (replaces
  `.kicker` visually; `.kicker` is styled identically).
- `.sec-head` (`h2` + optional link): section header with a 2px top rule.
- `.lede` / `.dek`: serif standfirst under an h1.
- `.btn` (solid ink), `.btn.accent` (solid accent), `.textlink` (underlined
  link with accent underline).
- `.tag`: small sentence-case chip on `--sunk`.
- `.figures` / `.fig`: ruled "by the numbers" list.
- `.tindex`: tool index table.
- `.latest`, `.lead`, `.list`: homepage latest-posts lead + list.
- `.scorebox`: review score panel.

## Copy rules for templates

- Sentence case for every label, button, kicker and nav item.
- No `//` prefixes, no `|` separators in kickers; use ` · `.
- Dates in visible text: `23 Oct 2026` style where the builder formats them.
