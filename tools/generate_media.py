#!/usr/bin/env python3
"""Generate branded media cards for every martechsignal.com entity.

Outputs (1200x630 PNG, editorial style from design/DESIGN.md: paper #F6F4EF,
ink type, one vermilion accent):
  og/tools/<slug>.png     - tool card: name, category, pricing, badges
  og/categories/<slug>.png - category card
  og/glossary/<slug>.png   - glossary card
  og/charts/*.png          - data charts from tools.json
  og/authors/tim-christensen.png - author card

Run from repo root: uv run --with pillow python tools/generate_media.py
Wired into deploy.sh after build.

STYLE_VERSION is part of the card identity: bump it whenever the visual system
changes so any content-hash based cache invalidates.
"""
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og"
W, H = 1200, 630

STYLE_VERSION = "2026-10-editorial-1"

# Palette (design/DESIGN.md, light theme)
PAPER = (246, 244, 239)   # #F6F4EF
SURFACE = (255, 255, 255)  # #FFFFFF
SUNK = (239, 236, 229)    # #EFECE5
INK = (24, 24, 27)        # #18181B
INK2 = (63, 61, 57)       # #3F3D39
MUTED = (103, 99, 91)     # #67635B
LINE = (221, 216, 205)    # #DDD8CD
ACCENT = (185, 58, 26)    # #B93A1A
POS = (30, 111, 71)       # #1E6F47

MARGIN = 80
RIGHT = W - MARGIN
CONTENT_W = RIGHT - MARGIN

FONT_DIR = ROOT / "design" / "og-fonts"
SERIF = str(FONT_DIR / "Newsreader-Display-Medium.ttf")
SERIF_ITALIC = str(FONT_DIR / "Newsreader-Display-Italic.ttf")
SANS = str(FONT_DIR / "Archivo-Medium.ttf")
SANS_SEMI = str(FONT_DIR / "Archivo-SemiBold.ttf")

KEEP_UPPER = {"ai": "AI", "seo": "SEO", "geo": "GEO", "llm": "LLM",
              "cdp": "CDP", "crm": "CRM", "api": "API", "ga4": "GA4",
              "mcp": "MCP", "abm": "ABM"}


def serif(size):
    return ImageFont.truetype(SERIF, size)


def serif_italic(size):
    return ImageFont.truetype(SERIF_ITALIC, size)


def sans(size, semibold=False):
    return ImageFont.truetype(SANS_SEMI if semibold else SANS, size)


def sentence_case(text: str) -> str:
    """'Workflow Automation' -> 'Workflow automation' (acronyms preserved)."""
    words = text.replace("-", " ").split()
    out = []
    for i, word in enumerate(words):
        low = word.lower()
        if low in KEEP_UPPER:
            out.append(KEEP_UPPER[low])
        elif word == "&":
            out.append(word)
        elif i == 0:
            out.append(word[:1].upper() + word[1:].lower())
        else:
            out.append(word.lower())
    return " ".join(out)


def base_canvas():
    img = Image.new("RGB", (W, H), PAPER)
    return img, ImageDraw.Draw(img)


def wrap(d, text, font_obj, max_w, max_lines=None):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split():
            trial = (cur + " " + word).strip()
            if d.textlength(trial, font=font_obj) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1].rstrip()
        if not last.endswith(("…", ".", "!", "?", ":", ";", ",")):
            lines[-1] = last + "…"
    return lines


def draw_chrome(d, label: str):
    """Wordmark + mark, 2px rule, and the accent label line."""
    f = serif(40)
    x, y = MARGIN, 64
    d.text((x, y), "MartechSignal", font=f, fill=INK, anchor="la")
    tw = d.textlength("MartechSignal", font=f)
    ascent, _ = f.getmetrics()
    baseline = y + ascent

    bx = x + tw + 10
    mark_h = 28
    for i, frac in enumerate((0.4, 0.7, 1.0)):
        bar_h = int(round(mark_h * frac))
        left = bx + i * 10
        d.rectangle([left, baseline - bar_h, left + 7, baseline], fill=ACCENT)

    d.rectangle([MARGIN, 128, RIGHT - 1, 129], fill=INK)
    d.text((MARGIN, 156), label, font=sans(24, semibold=True), fill=ACCENT,
           anchor="la")


def draw_title(d, title: str, max_lines: int = 4, top: int = 210):
    """Auto-size 72 -> 46 so the headline fits max_lines of 1040px."""
    size = 72
    while True:
        f = serif(size)
        lines = wrap(d, title, f, CONTENT_W)
        if len(lines) <= max_lines or size <= 46:
            break
        size -= 2
    lines = lines[:max_lines]
    line_h = int(round(size * 1.12))
    for i, line in enumerate(lines):
        d.text((MARGIN, top + i * line_h), line, font=f, fill=INK, anchor="la")
    return top + len(lines) * line_h


def draw_footer(d, right_text="martechsignal.com"):
    d.line([MARGIN, 540, RIGHT, 540], fill=LINE, width=1)
    d.text((MARGIN, 560), "Independent research on AI marketing automation",
           font=sans(22), fill=MUTED, anchor="la")
    rf = sans(22, semibold=True)
    tw = d.textlength(right_text, font=rf)
    d.text((RIGHT - tw, 560), right_text, font=rf, fill=INK, anchor="la")


def draw_chips(d, badges, x, y):
    """Sentence-case chips: sunk pill, or green outline for 'Open source'."""
    f = sans(20)
    pad, height = 16, 38
    for badge in badges:
        bw = int(d.textlength(badge, font=f)) + 2 * pad
        if badge.strip().lower() == "open source":
            d.rounded_rectangle([x, y, x + bw, y + height], radius=4,
                                outline=POS, width=2)
            d.text((x + pad, y + height / 2), badge, font=f, fill=POS,
                   anchor="lm")
        else:
            d.rounded_rectangle([x, y, x + bw, y + height], radius=4, fill=SUNK)
            d.text((x + pad, y + height / 2), badge, font=f, fill=INK2,
                   anchor="lm")
        x += bw + 10


def price_label(t):
    pf = t.get("price_from")
    pm = t.get("pricing_model") or ""
    if t.get("open_source"): return "Open source"
    # r34 M-13 (2026-10-06): "Free tier" keys on pricing_model, never on
    # price_from — sendgrid carries price_from 19.95 as a paid record and a
    # stale "Free tier" badge survived in raster. Unit-qualified figures
    # (trakkr "From $100/brand/mo") so badges match the text-layer fence.
    if pm in ("free", "freemium") or (pf in (None, 0, "0") and not pm):
        return "Free tier"
    if pf in (None, 0, "0"): return pm or "See pricing"
    try:
        v = float(pf)
        unit = (t.get("price_unit") or "").strip()
        fig = f"${int(v)}" if v == int(v) else f"${v}"
        return f"From {fig}/{unit}/mo" if unit else f"From {fig}/mo"
    except (TypeError, ValueError):
        return pm or "See pricing"


def sha(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


def _media_tools():
    """r6 M-2: tool cards for the catalog AND the /guides/ entries."""
    out = []
    for name in ("tools.json", "guides.json"):
        p = Path(__file__).resolve().parent / name
        if p.exists():
            out.extend(json.load(open(p)))
    return out


def gen_tool_card(t, d_out):
    name = t["name"]
    cat = sentence_case((t.get("category") or "").replace("-", " "))
    tagline = (t.get("tagline") or t.get("description") or "").strip().rstrip(".")[:180]
    img, d = base_canvas()
    draw_chrome(d, f"Tool review · {cat}" if cat else "Tool review")

    # Name (serif, auto-sized; at most two lines so the tagline still fits)
    bottom = draw_title(d, name, max_lines=2)

    # Tagline wrapped in the sans body face
    ty = max(bottom + 18, 310)
    for line in wrap(d, tagline, sans(24), CONTENT_W, max_lines=2):
        d.text((MARGIN, ty), line, font=sans(24), fill=INK2, anchor="la")
        ty += 32

    badges = [price_label(t)]
    if t.get("api_available"): badges.append("API")
    if t.get("github_stars"):
        try:
            stars = int(t["github_stars"])
            badges.append(f"{stars//1000}k GitHub stars" if stars >= 1000 else f"{stars} GitHub stars")
        except (TypeError, ValueError): pass
    draw_chips(d, badges[:3], MARGIN, 470)
    draw_footer(d)
    img.save(d_out, "PNG", optimize=True)


def gen_category_card(c, count, d_out):
    name = sentence_case(c["name"])
    desc = (c.get("intro") or c.get("description") or "").strip().split(". ")[0][:200]
    img, d = base_canvas()
    draw_chrome(d, "Category")

    bottom = draw_title(d, name, max_lines=2)
    ty = max(bottom + 18, 310)
    for line in wrap(d, desc, sans(24), CONTENT_W, max_lines=2):
        d.text((MARGIN, ty), line, font=sans(24), fill=INK2, anchor="la")
        ty += 32
    d.text((MARGIN, 478), f"{count} tools reviewed & compared", font=sans(22),
           fill=MUTED, anchor="la")
    draw_footer(d)
    img.save(d_out, "PNG", optimize=True)


def gen_glossary_card(g, defn, d_out):
    term = g.get("term") or g.get("short")
    img, d = base_canvas()
    draw_chrome(d, "Glossary")

    bottom = draw_title(d, term, max_lines=2)
    ty = max(bottom + 16, 330)
    raw = defn.strip()
    if len(raw) > 250:
        raw = raw[:250].rsplit(" ", 1)[0].rstrip(",;:.") + "…"
    for line in wrap(d, raw, sans(24), CONTENT_W, max_lines=3):
        d.text((MARGIN, ty), line, font=sans(24), fill=INK2, anchor="la")
        ty += 30
    draw_footer(d)
    img.save(d_out, "PNG", optimize=True)


def gen_author_card():
    img, d = base_canvas()
    draw_chrome(d, "Author")
    d.text((MARGIN, 210), "Tim Christensen", font=serif(72), fill=INK,
           anchor="la")
    d.text((MARGIN, 318), "Martech product owner · Malmö",
           font=serif_italic(34), fill=INK2, anchor="la")
    for i, line in enumerate(["Writes the MartechSignal teardowns:",
                              "hands-on reviews of AI marketing",
                              "automation tools, no sponsorships."]):
        d.text((MARGIN, 380 + i * 32), line, font=sans(24), fill=MUTED,
               anchor="la")
    draw_footer(d, "martechsignal.com/authors/tim-christensen")
    img.save(ROOT / "og" / "authors" / "tim-christensen.png", "PNG",
             optimize=True)


def gen_charts(tools, cats, out_dir):
    """Simple bar charts via PIL from tools.json aggregates (data unchanged)."""
    from collections import Counter
    active = [t for t in tools if t.get("status") == "active"]
    oss = Counter(); total = Counter()
    for t in active:
        c = t.get("category") or "other"
        total[c] += 1
        if t.get("open_source"): oss[c] += 1
    # R6 (2026-09-25): the open-source "category" is a meta-category that
    # aggregates OSS tools from every other category. As a bar it double-counts
    # tools already plotted elsewhere and is trivially 100% open source, so it
    # is excluded here (it stays a real hub page). Also: the old [:12] cap
    # silently dropped the two smallest categories while the subtitle claimed
    # all tools. Show every real category and make the subtitle match the bars.
    cats_sorted = sorted((k for k in total if k != "open-source"), key=lambda k: -total[k])
    shown = sum(total[k] for k in cats_sorted)
    oss_all = sum(1 for t in active if t.get("open_source"))
    img, d = base_canvas()
    d.text((MARGIN, 70), "Open-source share by category", font=serif(40),
           fill=INK, anchor="la")
    d.text((MARGIN, 122),
           f"{shown} tools in {len(cats_sorted)} categories · martechsignal.com directory",
           font=sans(19), fill=MUTED, anchor="la")
    d.text((MARGIN, 150),
           f"open-source is a meta-category ({oss_all} OSS tools) and is excluded here",
           font=sans(17), fill=MUTED, anchor="la")
    n = len(cats_sorted)
    # Two-line wrapped labels under each bar (readable at OG size; no truncation mid-word)
    label_fs = 14
    gap = 22
    bar_w = max(24, (CONTENT_W - (n - 1) * gap) // max(n, 1))
    x0 = MARGIN
    LABELS = {
        "marketing-automation": ["marketing", "automation"],
        "workflow-automation": ["workflow", "automation"],
        "email-marketing": ["email", "marketing"],
        "agent-skills": ["agent", "skills"],
        "open-source": ["open", "source"],
        "social-media": ["social", "media"],
        "content-ai": ["content", "ai"],
        "advertising": ["advertising"],
        "adtech": ["adtech"],
        "crm": ["crm"], "seo": ["seo"], "analytics": ["analytics"], "chatbots": ["chatbots"],
    }
    def _wrap(cat, max_chars=9):
        if cat in LABELS:
            return LABELS[cat]
        words = cat.split("-") if "-" in cat else [cat]
        if len(cat) <= max_chars:
            return [cat]
        lines, cur = [], ""
        for w in words:
            cand = w if not cur else cur
            if len(w) <= max_chars:
                if cur:
                    lines.append(cur)
                cur = w
            else:
                if cur:
                    lines.append(cur)
                    cur = ""
                cur = w
        if cur:
            lines.append(cur)
        return lines[:3]

    baseline = 560
    top_bar = 280
    max_total = max(total.values())
    # Hairline gridlines at quarter steps of the tallest bar.
    for k in range(1, 5):
        gy = baseline - int(top_bar * k / 4)
        d.line([MARGIN, gy, RIGHT, gy], fill=LINE, width=1)

    for i, c in enumerate(cats_sorted):
        tot, o = total[c], oss[c]
        h_full = top_bar * tot / max_total
        h_oss = top_bar * o / max_total
        x = x0 + i * (bar_w + gap)
        d.rectangle([x, baseline - int(h_full), x + bar_w, baseline], fill=SUNK,
                    outline=LINE)
        if o:
            d.rectangle([x, baseline - int(h_oss), x + bar_w, baseline],
                        fill=ACCENT)
        cnt = f"{tot}"
        cw = d.textlength(cnt, font=sans(18))
        d.text((x + bar_w / 2 - cw / 2, baseline - h_full - 26), cnt,
               font=sans(18), fill=INK, anchor="la")
        # centered wrapped category label
        lines = _wrap(c)
        y = baseline + 14
        for ln in lines:
            lf = sans(label_fs)
            lw = d.textlength(ln, font=lf)
            maxw = bar_w + gap - 6
            if lw > maxw:  # shrink-to-fit so long single words don't collide
                fs2 = max(10, int(label_fs * maxw / lw))
                lf = sans(fs2)
                lw = d.textlength(ln, font=lf)
            d.text((x + bar_w / 2 - lw / 2, y), ln, font=lf, fill=INK2,
                   anchor="la")
            y += 19
    # legend (top-right, clear of the short bars at the right end)
    d.rectangle([900, 190, 914, 204], fill=ACCENT)
    d.text((924, 190), "Open source", font=sans(20), fill=MUTED, anchor="la")
    d.rectangle([900, 222, 914, 236], fill=SUNK, outline=LINE)
    d.text((924, 222), "Commercial", font=sans(20), fill=MUTED, anchor="la")
    out = out_dir / "oss-by-category.png"
    img.save(out, "PNG", optimize=True)


def gen_vs_card(a_name, b_name, d_out):
    """r10 H-4 (2026-09-29): per-comparison social/schema image (A vs B)."""
    img, d = base_canvas()
    draw_chrome(d, "Comparison")
    title = f"{a_name} vs {b_name}"
    bottom = draw_title(d, title, max_lines=3)
    d.text((MARGIN, max(bottom + 20, 470)),
           "Pricing, features and verdict compared", font=sans(22), fill=MUTED,
           anchor="la")
    draw_footer(d)
    img.save(d_out, "PNG", optimize=True)


def main():
    import os
    os.chdir(ROOT)
    tools = json.loads((ROOT / "tools" / "tools.json").read_text())
    cats = json.loads((ROOT / "tools" / "categories.json").read_text())
    gloss = json.loads((ROOT / "tools" / "glossary.json").read_text())
    active = [t for t in tools if t.get("status") == "active"]

    tdir = OUT / "tools"; tdir.mkdir(parents=True, exist_ok=True)
    cdir = OUT / "categories"; cdir.mkdir(parents=True, exist_ok=True)
    gdir = OUT / "glossary"; gdir.mkdir(parents=True, exist_ok=True)
    chdir = OUT / "charts"; chdir.mkdir(parents=True, exist_ok=True)
    (OUT / "authors").mkdir(parents=True, exist_ok=True)

    n_t = n_c = n_g = 0
    for t in _media_tools():
        gen_tool_card(t, tdir / f"{t['slug']}.png"); n_t += 1
    counts = {}
    for t in active:
        counts[t.get("category")] = counts.get(t.get("category"), 0) + 1
    for c in cats:
        slug = c.get("slug")
        gen_category_card(c, counts.get(slug, 0), cdir / f"{slug}.png"); n_c += 1
    for g in gloss:
        gen_glossary_card(g, g.get("definition", ""), gdir / f"{g['slug']}.png"); n_g += 1
    gen_author_card()
    gen_charts(active, cats, chdir)
    # r10 H-4: one card per /vs/ page (social + Article image).
    _vsx = json.loads((ROOT / "tools" / "vsx-content.json").read_text())
    _vs_pages = _vsx if isinstance(_vsx, list) else _vsx.get("pages", [])
    _by_slug = {t["slug"]: t["name"] for t in tools}
    _vdir = OUT / "vs"; _vdir.mkdir(parents=True, exist_ok=True)
    n_v = 0
    for _p in _vs_pages:
        _a = _by_slug.get(_p.get("a_slug", ""), _p.get("a_slug", "?"))
        _b = _by_slug.get(_p.get("b_slug", ""), _p.get("b_slug", "?"))
        gen_vs_card(_a, _b, _vdir / f"{_p['slug']}.png"); n_v += 1
    print(f"media: {n_t} tool cards, {n_c} category cards, {n_g} glossary cards, author card, charts, {n_v} vs cards")

if __name__ == "__main__":
    main()
