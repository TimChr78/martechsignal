#!/usr/bin/env python3
"""Generate per-post OG cards (1200x630) in MartechSignal's editorial style.

Reads blog posts' title/date from the built HTML, renders PNG cards into
og/<slug>.png. Run after build_blog.py, before deploy.

Design: warm paper, ink serif headline, one vermilion accent (design/DESIGN.md).
The STYLE_VERSION below is part of the card identity: bump it whenever the
visual system changes so any content-hash based consumer invalidates.
"""
import html
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og"
W, H = 1200, 630

# Bumped whenever the card design changes, so cached/hashed consumers refresh.
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

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def serif(size):
    return ImageFont.truetype(SERIF, size)


def serif_italic(size):
    return ImageFont.truetype(SERIF_ITALIC, size)


def sans(size, semibold=False):
    return ImageFont.truetype(SANS_SEMI if semibold else SANS, size)


def format_date(iso: str) -> str:
    """ISO (YYYY-MM-DD) -> '23 Oct 2026' as used in visible copy."""
    try:
        y, m, d = (int(part) for part in iso.split("-"))
        return f"{d:02d} {MONTHS[m - 1]} {y}"
    except (ValueError, IndexError):
        return iso or ""


def wrap(draw, text, f, max_width, max_lines=None):
    """Greedy word wrap; keeps the existing behaviour for unbreakable words."""
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split():
            cand = f"{cur} {word}".strip()
            if draw.textlength(cand, font=f) <= max_width:
                cur = cand
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        if max_lines is not None and len(lines) >= max_lines:
            break
    return lines if max_lines is None else lines[:max_lines]


def draw_chrome(d, label: str):
    """Wordmark + mark, 2px rule, and the accent label line."""
    f = serif(40)
    x, y = MARGIN, 64
    d.text((x, y), "MartechSignal", font=f, fill=INK, anchor="la")
    tw = d.textlength("MartechSignal", font=f)
    ascent, _ = f.getmetrics()
    baseline = y + ascent

    # Three accent bars, bottom-aligned to the wordmark baseline.
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
    if len(lines) == max_lines and len(wrap(d, title, f, CONTENT_W)) > max_lines:
        last = lines[-1].rstrip()
        if not last.endswith(("…", ".", "!", "?", ":", ";", ",")):
            lines[-1] = last + "…"
    line_h = int(round(size * 1.12))
    for i, line in enumerate(lines):
        d.text((MARGIN, top + i * line_h), line, font=f, fill=INK, anchor="la")
    return top + len(lines) * line_h


def draw_footer(d, right_text: str = "martechsignal.com"):
    d.line([MARGIN, 540, RIGHT, 540], fill=LINE, width=1)
    d.text((MARGIN, 560), "Independent research on AI marketing automation",
           font=sans(22), fill=MUTED, anchor="la")
    rf = sans(22, semibold=True)
    tw = d.textlength(right_text, font=rf)
    d.text((RIGHT - tw, 560), right_text, font=rf, fill=INK, anchor="la")


def render(slug: str, title: str, date: str) -> Path:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    draw_chrome(d, format_date(date))
    draw_title(d, title)
    draw_footer(d)

    OUT.mkdir(exist_ok=True)
    out = OUT / f"{slug}.png"
    img.save(out, "PNG", optimize=True)
    return out


def save_renditions(card_path: Path, slug: str):
    """Emit the hero .webp srcset trio every <img class="post-hero"> uses."""
    card = Image.open(card_path).convert("RGB")
    for width in (1200, 800, 480):
        suffix = "" if width == 1200 else f"-{width}"
        img = (card if width == 1200 else card.resize(
            (width, round(card.height * width / card.width)), Image.LANCZOS))
        img.save(ROOT / "og" / f"hero-{slug}{suffix}.webp", "WEBP", quality=82)


def render_post(child: Path, label: str = "") -> bool:
    f = child / "index.html"
    if not (child.is_dir() and f.exists()):
        return False
    h = f.read_text()
    m = re.search(r"<title>(.*?)</title>", h)
    d = re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', h)
    if not m:
        return False
    title = html.unescape(m.group(1))
    slug = child.name
    out = render(slug, title, d.group(1) if d else "")
    save_renditions(out, slug)
    note = f", {label}" if label else ""
    print(f"  ✓ og/{slug}.png ({out.stat().st_size // 1024} KB{note})")
    return True


def main():
    count = 0
    for child in sorted((ROOT / "blog").iterdir()):
        if render_post(child):
            count += 1
    for child in sorted((ROOT / "guides").iterdir()):
        if render_post(child, "guide"):
            count += 1
    print(f"Generated {count} OG cards")


if __name__ == "__main__":
    main()
