#!/usr/bin/env python3
"""Generate branded media cards for every martechsignal.com entity.

Outputs (1200x630 PNG, brand style: navy #080E1A / amber #FFB224):
  og/tools/<slug>.png     — tool card: name, category, pricing, badges
  og/categories/<slug>.png — category card
  og/glossary/<slug>.png   — glossary card
  og/charts/*.png          — data charts from tools.json
  og/author-tim-christensen.png — author monogram

Run from repo root: .venv-imggen/bin/python tools/generate_media.py
Wired into deploy.sh after build. Deterministic: regenerates only when data changes.
"""
import json, hashlib, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og"
BG = (8, 14, 26); AMBER = (255, 178, 36); TEXT = (232, 236, 244); MUTED = (140, 150, 168)
CARD = (13, 20, 36); BORDER = (40, 52, 74); DIM = (24, 32, 50)
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(sz, bold=True):
    return ImageFont.truetype(FB if bold else FR, sz)

def base_canvas():
    img = Image.new("RGB", (1200, 630), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1200, 6], fill=AMBER)
    return img, d

def brand_header(img, d, label):
    d.rounded_rectangle([80, 60, 144, 124], radius=12, fill=CARD, outline=BORDER, width=2)
    d.rounded_rectangle([98, 74, 126, 110], radius=4, fill=AMBER)
    d.text((164, 78), "MARTECH", font=font(30), fill=TEXT)
    w = d.textlength("MARTECH", font=font(30))
    d.text((166 + w, 78), "SIGNAL", font=font(30), fill=AMBER)
    d.text((80, 150), label.upper(), font=font(22), fill=MUTED)

def footer(d, right_text):
    d.line([80, 540, 1120, 540], fill=BORDER, width=1)
    d.text((80, 562), "Independent reviews · No sponsorships", font=font(22), fill=MUTED)
    tw = d.textlength(right_text, font=font(22))
    d.text((1120 - tw, 562), right_text, font=font(22), fill=AMBER)

def wrap(d, text, font_obj, max_w, max_lines=2):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font_obj) <= max_w:
            cur = trial
        else:
            if cur: lines.append(cur)
            cur = w
            if len(lines) == max_lines: break
    if cur and len(lines) < max_lines: lines.append(cur)
    return lines

def price_label(t):
    pf = t.get("price_from")
    pm = t.get("pricing_model") or ""
    if t.get("open_source"): return "Open source"
    if pf in (None, 0, "0"): return "Free tier"
    try:
        v = float(pf)
        return f"From ${int(v)}/mo" if v == int(v) else f"From ${v}/mo"
    except (TypeError, ValueError):
        return pm or "See pricing"

def sha(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def gen_tool_card(t, d_out):
    name = t["name"]
    cat = (t.get("category") or "").replace("-", " ").title()
    tagline = (t.get("tagline") or t.get("description") or "").strip().rstrip(".")[:180]
    img, d = base_canvas()
    brand_header(img, d, f"{cat} review")
    # Name (big)
    nf = font(64 if len(name) <= 22 else 54 if len(name) <= 30 else 44)
    d.text((80, 210), name, font=nf, fill=TEXT)
    y = 300
    # Tagline wrapped
    for line in wrap(d, tagline, font(28), 1000):
        d.text((80, y), line, font=font(28), fill=MUTED); y += 42
    # Badges row
    by = 470
    badges = [price_label(t)]
    if t.get("api_available"): badges.append("API")
    if t.get("github_stars"):
        try:
            stars = int(t["github_stars"])
            badges.append(f"{stars//1000}k GitHub stars" if stars >= 1000 else f"{stars} GitHub stars")
        except (TypeError, ValueError): pass
    bx = 80
    for b in badges[:3]:
        bw = d.textlength(b, font=font(24)) + 36
        d.rounded_rectangle([bx, by, bx + bw, by + 48], radius=8, fill=DIM, outline=BORDER, width=1)
        d.text((bx + 18, by + 10), b, font=font(24), fill=AMBER)
        bx += bw + 16
    footer(d, "martechsignal.com")
    img.save(d_out, "PNG", optimize=True)

def gen_category_card(c, count, d_out):
    name = c["name"]
    desc = (c.get("intro") or c.get("description") or "").strip().split(". ")[0][:200]
    img, d = base_canvas()
    brand_header(img, d, "category guide")
    d.text((80, 210), name, font=font(60 if len(name) <= 26 else 48), fill=TEXT)
    y = 310
    for line in wrap(d, desc, font(28), 1000):
        d.text((80, y), line, font=font(28), fill=MUTED); y += 42
    d.text((80, 462), f"{count} tools reviewed & compared", font=font(26), fill=TEXT)
    footer(d, "martechsignal.com")
    img.save(d_out, "PNG", optimize=True)

def gen_glossary_card(g, defn, d_out):
    term = g.get("term") or g.get("short")
    short = g.get("short") or term
    img, d = base_canvas()
    brand_header(img, d, "glossary definition")
    tf = font(72 if len(term) <= 20 else 58 if len(term) <= 30 else 44)
    d.text((80, 220), term, font=tf, fill=TEXT)
    y = 330
    for line in wrap(d, defn.strip()[:250], font(28), 1000, max_lines=3):
        d.text((80, y), line, font=font(28), fill=MUTED); y += 42
    footer(d, "martechsignal.com")
    img.save(d_out, "PNG", optimize=True)

def gen_author_card():
    from PIL import ImageDraw as D
    img, d = base_canvas()
    brand_header(img, d, "author")
    # Monogram
    d.rounded_rectangle([80, 230, 260, 410], radius=24, fill=CARD, outline=AMBER, width=3)
    mf = font(96)
    tw = d.textlength("TC", font=mf)
    d.text((170 - tw/2, 275), "TC", font=mf, fill=AMBER)
    d.text((300, 250), "Tim Christensen", font=font(56), fill=TEXT)
    d.text((302, 330), "Martech Product Owner · Malmö", font=font(28), fill=MUTED)
    for i, line in enumerate(["Writes the MartechSignal teardowns:",
                               "hands-on reviews of AI marketing",
                               "automation tools, no sponsorships."]):
        d.text((302, 380 + i*38), line, font=font(24), fill=MUTED)
    footer(d, "martechsignal.com/authors/tim-christensen")
    img.save(ROOT / "og" / "authors" / "tim-christensen.png", "PNG", optimize=True)

def gen_charts(tools, cats, out_dir):
    """SVG-free simple bar charts via PIL from tools.json aggregates."""
    # Chart 1: open-source vs commercial per category (stacked bars)
    from collections import Counter
    active = [t for t in tools if t.get("status") == "active"]
    oss = Counter(); total = Counter()
    for t in active:
        c = t.get("category") or "other"
        total[c] += 1
        if t.get("open_source"): oss[c] += 1
    cats_sorted = sorted(total.keys(), key=lambda k: -total[k])[:12]
    W, H, LH = 1200, 630, 34
    top_pad, bot_pad = 130, 90
    img, d = base_canvas()
    d.text((80, 70), "Open-source share by category", font=font(40), fill=TEXT)
    d.text((80, 122), f"{len(active)} tools · martechsignal.com directory", font=font(22), fill=MUTED)
    n = len(cats_sorted)
    bar_w, gap = 56, 18
    x0 = 80
    for i, c in enumerate(cats_sorted):
        tot, o = total[c], oss[c]
        h_full = 280 * tot / max(total.values())
        h_oss = 280 * o / max(total.values())
        x = x0 + i * (bar_w + gap)
        d.rectangle([x, 560 - h_full - bot_pad + bot_pad, x + bar_w, 560], fill=DIM, outline=BORDER)
        if o:
            d.rectangle([x, 560 - h_oss, x + bar_w, 560], fill=AMBER)
        label = c[:9]
        lw = d.textlength(label, font=font(16))
        d.text((x + bar_w/2 - lw/2, 566), label, font=font(16), fill=MUTED)
        cnt = f"{tot}"
        cw = d.textlength(cnt, font=font(18))
        d.text((x + bar_w/2 - cw/2, 560 - h_full - 26), cnt, font=font(18), fill=TEXT)
    # legend
    d.rectangle([900, 480, 924, 500], fill=AMBER)
    d.text((932, 482), "open source", font=font(20), fill=MUTED)
    d.rectangle([900, 512, 924, 532], fill=DIM, outline=BORDER)
    d.text((932, 514), "commercial", font=font(20), fill=MUTED)
    out = out_dir / "oss-by-category.png"
    img.save(out, "PNG", optimize=True)

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
    for t in active:
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
    print(f"media: {n_t} tool cards, {n_c} category cards, {n_g} glossary cards, author card, charts")

if __name__ == "__main__":
    main()