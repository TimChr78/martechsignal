#!/usr/bin/env python3
"""Generate per-post OG cards (1200x630) matching MartechSignal's dark/amber brand.

Reads blog posts' title/date from the built HTML, renders PNG cards into
og/<slug>.png. Run after build_blog.py, before deploy.
"""
import html
import re
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og"
W, H = 1200, 630
BG = (8, 14, 26)          # #080E1A
AMBER = (255, 178, 36)    # #FFB224
TEXT = (232, 236, 244)
MUTED = (140, 150, 168)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def draw_logo(draw):
    """Rounded square + amber bar, echoing the favicon."""
    x, y = 80, 72
    draw.rounded_rectangle([x, y, x + 64, y + 64], radius=12, fill=(13, 20, 36), outline=(40, 52, 74), width=2)
    draw.rounded_rectangle([x + 18, y + 14, x + 46, y + 50], radius=4, fill=AMBER)


def wrap(draw, text, max_width, f):
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
    return lines


def render(slug: str, title: str, date: str) -> Path:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # subtle top amber rule
    d.rectangle([0, 0, W, 6], fill=AMBER)

    draw_logo(d)
    d.text((170, 88), "MARTECH", font=font(34), fill=TEXT)
    w = d.textlength("MARTECH", font=font(34))
    d.text((172 + w, 88), "SIGNAL", font=font(34), fill=AMBER)

    # date chip
    d.text((80, 190), date.upper(), font=font(24), fill=MUTED)

    # headline (auto-size: shrink for long titles)
    size = 76 if len(title) <= 60 else (64 if len(title) <= 90 else 54)
    f = font(size)
    lines = wrap(d, title, W - 160, f)
    while len(lines) > 4 and size > 44:
        size -= 6
        f = font(size)
        lines = wrap(d, title, W - 160, f)
    y = 250
    for line in lines[:5]:
        d.text((80, y), line, font=f, fill=TEXT)
        y += int(size * 1.18)

    # footer
    d.text((80, H - 90), "AI marketing automation, audited", font=font(26), fill=MUTED)
    d.text((W - 340, H - 90), "martechsignal.com", font=font(26), fill=AMBER)

    OUT.mkdir(exist_ok=True)
    out = OUT / f"{slug}.png"
    img.save(out, "PNG", optimize=True)
    return out


def main():
    posts_dir = ROOT / "blog"
    count = 0
    for child in sorted(posts_dir.iterdir()):
        f = child / "index.html"
        if not (child.is_dir() and f.exists()):
            continue
        h = f.read_text()
        m = re.search(r"<title>(.*?)</title>", h)
        d = re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', h)
        if not m:
            continue
        title = html.unescape(m.group(1))
        slug = child.name
        out = render(slug, title, d.group(1) if d else "")
        print(f"  ✓ og/{slug}.png ({out.stat().st_size // 1024} KB)")
        count += 1
    print(f"Generated {count} OG cards")


if __name__ == "__main__":
    main()
