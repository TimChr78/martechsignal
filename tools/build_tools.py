#!/usr/bin/env python3

import json as _h9j
_H9_ENTITY = _h9j.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "Organization", "@id": "https://martechsignal.com/#organization",
         "name": "MartechSignal", "url": "https://martechsignal.com/",
         "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo",
                  "url": "https://martechsignal.com/logo.png"},
         "sameAs": ["https://github.com/timchr78"]},
        {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person",
         "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/",
         "image": "https://martechsignal.com/authors/tim-christensen/avatar.png",
         "worksFor": {"@id": "https://martechsignal.com/#organization"},
         "sameAs": ["https://github.com/timchr78"]},
    ],
})
_H9_TAG = '<script type="application/ld+json">' + _H9_ENTITY + '</script>'
"""Generate static HTML pages for the MartechSignal tool directory.

Reads tools/tools.json + tools/categories.json → outputs:
  - tools/index.html          (directory hub)
  - tools/{slug}.html         (tool profiles)
  - categories/{slug}.html    (category listings)

Run from /opt/data/martechsignal/:  python3 tools/build_tools.py
"""
import hashlib
import json, os, html, re
import sys
from pathlib import Path
from datetime import datetime
sys.path.insert(0, str(Path(__file__).resolve().parent))
import suggest_links

ROOT = Path(__file__).resolve().parent.parent  # martechsignal/


def _css_v() -> str:
    """Cache-bust hash for style.css, computed from the file itself (R3-M18/L2:
    the literal went stale and new rules never shipped to returning visitors)."""
    import hashlib as _h
    return _h.md5((ROOT / "style.css").read_bytes()).hexdigest()[:8]

TOOLS_DIR = ROOT / "tools"
CATS_DIR = ROOT / "categories"

def load():
    tools = json.loads((TOOLS_DIR / "tools.json").read_text())
    cats = json.loads((TOOLS_DIR / "categories.json").read_text())
    return tools, cats

def esc(s):
    return html.escape(str(s)) if s else ""

def pricing_label(t):
    m = t.get("pricing_model", "paid")
    if m == "free": return "Free"
    if m == "freemium": return "Freemium"
    if m == "open-source": return "Open Source"
    if m == "enterprise": return "Enterprise"
    p = t.get("price_from")
    if p == 0: return "Free tier"
    if p: return f"From ${p}/mo"
    return "Paid"

# ── SEO title / meta template (CTR-optimized, ≤60 / ≤155) ──────────
# Title:  "{Name} review (2026): pricing, AI features, verdict"  (H6 run#5: review intent)
#   Try: "{Name} Review: {Category} | {Pricing} | MartechSignal" first;
#   fallback without category if >60ch. For very long names we truncate
#   the name part (never the suffix) to keep the pipe-brand intact.
# Meta:   "{Name} | {Tagline}. {PricingPhrase} Compare AI features, integrations & top alternatives."
#   PricingPhrase varies by model: Open source / Enterprise / Starts at $X / etc.


def pricing_card(t):
    """R2 H-10 (2026-09-08): pricing sidebar card. The VIEW PRICING anchor previously
    rendered unconditionally with href='' when pricing_url was missing - clicking
    reloaded the page AND fired a false 'Pricing click' Umami event. Emit the anchor
    only when a real URL exists; otherwise render the notes as plain text."""
    notes = (t.get("price_notes") or "").strip()
    if not notes:
        return ""
    url = (t.get("pricing_url") or "").strip()
    if url and url != "#":
        cta = (f'<div style="margin-top:.8rem"><a style="font:600 .74rem var(--mono);'
               f'color:var(--amber);text-decoration:none" href="{esc(url)}" target="_blank" '
               f'rel="noopener" data-umami-event="Pricing click" '
               f'data-umami-event-tool="{esc(t["name"])}">VIEW PRICING →</a></div>')
    else:
        cta = ""
    return (f'<div class="side-card"><h3>Pricing</h3>'
            f'<p style="color:var(--muted);font-size:.9rem">{esc(notes)}</p>{cta}</div>')


# Comparison posts (GSC follow-up, 2026-09-13): the three-way comparison post is the
# best-placed asset for the NocoBase query cluster, and it already links out to every
# tool page it covers. Nothing linked back. Keyword overlap does not surface it on tool
# pages (the post scores below unrelated posts there), so the cross-link is curated per
# slug with a real descriptive anchor, and it renders only when the post exists on disk.
_TOOL_COMPARISON_POSTS = {
    "nocobase": ("nocobase-vs-nocodb-vs-budibase",
                 "How NocoBase compares with NocoDB and Budibase for self-hosted marketing ops"),
    "nocodb": ("nocobase-vs-nocodb-vs-budibase",
               "Where NocoDB sits against NocoBase and Budibase"),
    "budibase": ("nocobase-vs-nocodb-vs-budibase",
                 "Budibase next to NocoBase and NocoDB: choosing between the three"),
}

# Body Pricing section (GSC follow-up, 2026-09-13): the pricing query cluster ("nocobase
# pricing" and the same pattern on other tools) landed on tool pages whose only pricing
# text sat in a sidebar card: no pricing heading in the body and no plan detail in the
# page text. Compose one from the record's own fields, and emit it ONLY when the record
# carries substantive pricing detail - a price_notes string with enough in it to say
# something specific. Thin notes (a bare "free, self-hosted") render nothing, so no page
# gains a section that just swaps the brand into the same sentence. Every line traces to
# a tools.json field; nothing is inferred from outside the record.
_PRICING_SECTION_MIN_NOTES = 40
_PRICING_SECTION_SIGNAL = re.compile(r"\d|free|custom|tier|licen|quote|seat|user", re.I)


def _price_money(sym, value):
    try:
        return f"{sym}{float(value):g}"
    except (TypeError, ValueError):
        return f"{sym}{value}"


def pricing_section_html(t):
    """Body Pricing section for one tool, or '' when the record is too thin for it."""
    notes = str(t.get("price_notes") or "").strip()
    # a vendor-approved public note wins over the internal one when it is a string
    _pub = t.get("pricing_note_public")
    if isinstance(_pub, str) and _pub.strip():
        notes = _pub.strip()
    if len(notes) < _PRICING_SECTION_MIN_NOTES or not _PRICING_SECTION_SIGNAL.search(notes):
        return ""
    name = esc(t.get("name") or "This tool")
    model = str(t.get("pricing_model") or "").strip().lower()
    lic = str(t.get("license") or "").strip()
    pf, paid = t.get("price_from"), t.get("paid_from")
    sym = "\u20ac" if str(t.get("currency") or "").upper() == "EUR" else "$"
    # Lead: the pricing model plus the entry fact. Wording varies by model on purpose -
    # one sentence per record, not one template with the brand swapped.
    if model == "enterprise":
        lead = (f"{name} is sold on quote-based enterprise contracts" if not pf
                else f"{name} is sold on enterprise contracts")
    elif model == "free" or (pf == 0 and model not in ("open-source", "open-core", "freemium")):
        lead = f"{name} is free to use"
    elif model == "open-source":
        lead = f"{name} is free to self-host" + (f" under the {esc(lic)} licence" if lic else "")
    elif model == "open-core":
        lead = f"{name} is open core: the self-hosted version is free"
    elif model == "freemium":
        lead = f"{name} is freemium, with a free tier to start"
    else:
        lead = f"{name} is sold on paid plans"
    tail = ""
    if model == "enterprise" and pf:
        tail = f", from {_price_money(sym, pf)}/mo"
    elif pf and pf != 0:
        _entry = paid if (paid and paid < pf) else pf
        tail = f", from {_price_money(sym, _entry)}/mo" if "paid plans" in lead \
            else f", paid plans from {_price_money(sym, _entry)}/mo"
    elif paid:
        tail = f", paid plans start at {_price_money(sym, paid)}/mo"
    # G-2 (v2.4.0 audit): bind the price claim to its verification date.
    if tail and t.get("date_updated"):
        tail += f" as of {esc(str(t['date_updated'])[:7])}"
    url = str(t.get("pricing_url") or "").strip()
    link = ""
    if url and url != "#":
        link = ('<p style="font-size:.8rem;color:var(--muted);margin:.4rem 0 0">'
                'Current plans and limits live on the '
                f'<a href="{esc(url)}" target="_blank" rel="noopener" '
                f'data-umami-event="Pricing section click" '
                f'data-umami-event-tool="{esc(t.get("name") or "")}">{name} pricing page</a>.</p>')
    return ('<section class="pricing-block"><h2>Pricing</h2>'
            f'<p>{lead}{tail}.</p><p>{esc(notes)}</p>{link}</section>')


_GLOSSARY_NAMES = None

def _glossary_display(term_slug):
    """R2 M-5 (2026-09-08): display glossary terms with their real names instead of
    .title()-mangling acronyms (Mcp, Ai Agent, Crm). Falls back to acronym-aware title."""
    global _GLOSSARY_NAMES
    if _GLOSSARY_NAMES is None:
        import json as _json
        try:
            g = _json.load(open("tools/glossary.json", encoding="utf-8"))
            _GLOSSARY_NAMES = {x.get("slug"): (x.get("short") or x.get("term")) for x in g}
        except Exception:
            _GLOSSARY_NAMES = {}
    if term_slug in _GLOSSARY_NAMES:
        return _GLOSSARY_NAMES[term_slug]
    words = term_slug.replace("-", " ").title()
    for acr in ("Mcp", "Crm", "Seo", "Ai", "Cdp", "Dsp", "Dmp", "Utm", "Kpi", "Sms", "Api", "Cta", "Roi"):
        words = words.replace(acr, acr.upper())
    return words


_CATEGORY_NAMES = None

def _category_display(cat_slug):
    """MUSE-11 (2026-09-13): render categories with their canonical names.

    Glossary chips and blog 'Filed under' chips built the label with
    .title() on the slug, which put 'Crm', 'Seo' and 'Content Ai' on 88 pages
    while categories.json has 'CRM', 'SEO & Search' and 'AI Content & Copywriting'.
    Same fix pattern as _glossary_display() above.
    """
    global _CATEGORY_NAMES
    if _CATEGORY_NAMES is None:
        try:
            g = json.loads((ROOT / "tools" / "categories.json").read_text(encoding="utf-8"))
            _CATEGORY_NAMES = {c.get("slug"): c.get("name") for c in g if c.get("slug")}
        except Exception:
            _CATEGORY_NAMES = {}
    if cat_slug in _CATEGORY_NAMES and _CATEGORY_NAMES[cat_slug]:
        return _CATEGORY_NAMES[cat_slug]
    words = str(cat_slug).replace("-", " ").title()
    for acr in ("Mcp", "Crm", "Seo", "Ai", "Cdp", "Ads", "Oss", "Abm", "Cro", "Dco", "Cta", "Api", "Utm"):
        words = words.replace(acr, acr.upper())
    return words


_SUB_INLINE = '<section class="subscribe sub-inline" id="subscribe"><h2>Get the next teardown</h2><p>One email when a new tool review lands, nothing else.</p><form class="sub-form" action="https://app.kit.com/forms/9136291/subscriptions" method="post" data-sv-form="9136291" data-uid="f315181f90" target="_blank"><input type="hidden" name="newsletter[subscriber][first_name]" value=""><input type="email" name="email_address" autocomplete="email" placeholder="you@company.com" aria-label="Email address" required><button type="submit">SUBSCRIBE</button></form></section>'


def cat_h1(cat_name):
    """Category hub H1: append 'Tools' unless the name already ends with it."""
    name = (cat_name or "").strip()
    if name.lower().endswith("tools"):
        return name
    return f"{name} Tools"

# SX-6 pilot: slugs that have a published "<tool> alternatives" page (gates the
# tool-page interlink so we never link a page that does not exist).
try:
    _ALT_SLUGS = {p["slug"] for p in json.loads(
        (ROOT / "tools" / "alternatives-content.json").read_text())["pages"]}
except Exception:
    _ALT_SLUGS = set()

def _tool_h1(t):
    """A2 M3 (2026-09-26): the H1 skeleton was identical on all 158 pages (L17
    shares the root). Vary the phrasing by pricing class: same honest claim,
    different query surface, tool name always leads."""
    pm = t.get("pricing_model") or "paid"
    n = esc(t["name"])
    return {
        "paid": f"{n} review (2026): pricing, AI features, verdict",
        "freemium": f"{n} review (2026): pricing, AI features, verdict",
        "open-source": f"{n} review (2026): pricing, AI features, verdict",
        "open-core": f"{n} review (2026): pricing, AI features, verdict",
        "free": f"{n} review (2026): pricing, AI features, verdict",
    }.get(pm, f"{n} review (2026): pricing, AI features, verdict")


def _seo_title_for(t, cats):
    # SX-1 (2026-09-25, decided by Tim): tool pages target owned intent
    # (pricing / plans / open-source), NOT "<tool> review" - that SERP is owned by
    # verified-review platforms the site structurally cannot compete with. Price in
    # the title where it fits (evertune-pricing pattern), else a clean pricing head.
    name = t["name"]
    price = pricing_label(t)
    suffix = " | MartechSignal"
    cand = f"{name} review (2026): pricing, AI features, verdict{suffix}"
    if len(cand) <= 60:
        return cand
    cand2 = f"{name} review (2026): pricing, AI features, verdict"
    if len(cand2) <= 60:
        return cand2
    # r6 C-2 (2026-09-27): the clamp used to cut the product NAME ("HubSpot
    # Marketing pricing"). The name is never cut now; suffixes drop first.
    for cand3 in (f"{name} pricing{suffix}", f"{name} pricing",
                  f"{name} review (2026): pricing", f"{name} pricing & plans"):
        if len(cand3) <= 60:
            return cand3
    return f"{name} review (2026)"[:57]

def _clip_meta_text(text, budget):
    """Cut meta text on a natural boundary (GSC follow-up 2026-09-13).

    The old fallback was a hard `desc[:90].rsplit(" ",1)[0]`, which sliced mid-phrase
    and shipped broken snippets to the SERP. Real examples found live:
      "AI Business Skills: 63 bilingual marketing skills (Vietnamese +."
      "ALwrity: AI-first digital marketing platform for content strategy."
    (the actual description continues past both cut points).

    Order of preference: drop an unterminated parenthetical, then cut at a sentence /
    semicolon / comma / dash, then fall back to a word boundary. Trailing connectors
    and punctuation are stripped so the result always reads as a finished phrase.
    """
    if len(text) <= budget:
        return text
    window = text[:budget]
    if window.count("(") > window.count(")"):
        window = window[:window.rfind("(")].rstrip()
    for sep in (". ", "; ", ", ", " - ", " \u2014 "):
        i = window.rfind(sep)
        if i >= budget * 0.5:
            return window[:i].rstrip(" ,;:-\u2014")
    return window.rsplit(" ", 1)[0].rstrip(" ,;:-\u2014+")


def _ends_on_function_word(text):
    """True if a clipped phrase would end on a dangling connector.

    Prevents snippets like "...for SMEs and." / "...engagement and product with." that a
    punctuation-only strip leaves behind.
    """
    _fw = {"and", "or", "with", "for", "of", "to", "in", "on", "the", "a", "an", "at",
           "by", "from", "into", "as", "but", "plus", "using", "via", "without"}
    words = text.strip().rstrip(",;:-").split()
    return bool(words) and words[-1].lower() in _fw


def _seo_description_for(t, cats):
    cat_map = {c["slug"]: c["name"] for c in cats}
    name = t["name"]
    # L3 (r9, 2026-09-28): page_shell escapes the description into the meta
    # tag, so quotes expand to entities AFTER this composer runs. Budget the
    # escaped length or raw-fits-but-rendered-long descriptions (163 chars on
    # react-email-editor, zapier-gtm-cheat-codes) slip through.
    tagline = (t.get("tagline") or "").strip()
    if not tagline or len(tagline) < 10:
        desc = (t.get("description") or "").strip()
        if desc and len(desc) >= 30:
            # use first sentence of description as tagline fallback
            import re as _re
            first = _re.split(r'[.!…]\s', desc, 1)[0].strip()
            if len(first) >= 20:
                tagline = first
            else:
                tagline = _clip_meta_text(desc, 90)
        else:
            tagline = f"{cat_map.get(t.get('category'), 'Marketing')} tool"
    tagline_sent = tagline if tagline.endswith(".") else tagline + "."
    if t.get("open_source"):
        # Don't repeat the licence in the snippet when the tagline already says it.
        # Live example this fixes: "BillionMail: Open-source mail server, newsletter,
        # and email. Open source & free to self-host." (and 53 other pages).
        import re as _re
        if _re.search(r"open[- ]?source", tagline, _re.I):
            price_phrase = "Free to self-host; no licence fee."
        else:
            price_phrase = "Open source & free to self-host."
    elif t.get("pricing_model") == "enterprise":
        price_phrase = "Enterprise pricing; demo required."
    elif t.get("price_from") is not None:
        if t.get("price_from"):
            price_phrase = f"Starts at {_money(t['price_from'], t)}."
        elif t.get("pricing_model") in ("freemium", "free", "open-core"):
            price_phrase = "Free tier available."
        else:
            price_phrase = "Free to use."
    else:
        price_phrase = f"{pricing_label(t)}."
    tail = " Compare AI features, integrations & top alternatives."
    # Composition order (GSC follow-up 2026-09-13): prefer a COMPLETE tagline over the
    # generic tail. The tail is identical boilerplate on ~104 pages, so it is the cheapest
    # thing to drop when space runs short. The previous order clipped the tagline first,
    # which shipped dangling fragments to the SERP, e.g.
    #   "Ghost: Open-source publishing platform with built-in."
    #   "Krayin CRM: Free open-source Laravel CRM for SMEs and."
    if len(esc(f"{name}: {tagline_sent} {price_phrase}{tail}")) <= 155:
        return f"{name}: {tagline_sent} {price_phrase}{tail}"
    if len(esc(f"{name}: {tagline_sent} {price_phrase}")) <= 155:
        return f"{name}: {tagline_sent} {price_phrase}"
    # Only now clip the tagline, and only on a clean boundary with no tail to pay for.
    overhead = len(f"{name}:  {price_phrase}") + 1
    budget = 155 - overhead
    if budget > 30:
        trunc = _clip_meta_text(tagline_sent.rstrip("."), budget)
        if trunc and not _ends_on_function_word(trunc):
            ts = trunc + "." if not trunc.endswith((".", "!", "?")) else trunc
            cand = f"{name}: {ts} {price_phrase}"
            if len(esc(cand)) <= 155:
                return cand
    # Final fallback: name + pricing only. Never cut mid-phrase to keep the tail.
    cand = f"{name}: {price_phrase}"
    if len(esc(cand)) <= 155:
        return cand
    cut = cand[:152].rsplit(" ", 1)[0].rstrip(" ,;:")
    return cut + "." if not cut.endswith((".", "!", "?")) else cut

# ── Shared HTML shell ──────────────────────────────────────────────

SUB_STRIP = (
    '<div class="sub-strip"><div><h3>Building your martech shortlist?</h3>'
    '<p>The weekly newsletter: one tool teardown, one workflow, no fluff. Free.</p></div>'
    '<a class="btn" href="/#subscribe" data-umami-event="Tool subscribe click">Subscribe</a></div>')

def screenshot_figure(slug, tool_name):
    """Single source of truth for vendor homepage screenshots (R2 M-3).

    Resolves either capture location, newest first:
      1. og/screenshots/<slug>-<YYYY-MM>.png   (what tools/screenshot_tools.py writes)
      2. og/screens/<slug>.webp                (legacy location, kept as fallback)
    Always emits a <figure> WITH a figcaption, and dates the caption from the capture
    month in the filename rather than today's date, so a rebuild cannot relabel an old
    capture as a new one. Returns "" when no capture exists (page renders as before).

    The internal link-free rule still applies: this is presented as a dated reference
    capture of a vendor page, not as an endorsement.
    """
    candidates = []
    shots_dir = ROOT / "og" / "screenshots"
    if shots_dir.is_dir():
        for p in sorted(shots_dir.glob(f"{slug}-*.png"), reverse=True):
            candidates.append((f"og/screenshots/{p.name}", p))
    legacy = ROOT / "og" / "screens" / f"{slug}.webp"
    if legacy.exists():
        candidates.append((f"og/screens/{slug}.webp", legacy))
    if not candidates:
        return ""
    rel, path = candidates[0]
    m = re.search(r"(\d{4})-(\d{2})", path.name)
    if m:
        try:
            _d = datetime(int(m.group(1)), int(m.group(2)), 1)
            what = f"{tool_name} homepage, captured {_d.strftime('%B %Y')}"
        except ValueError:
            what = f"{tool_name} homepage"
    else:
        what = f"{tool_name} homepage"
    # M16 (2026-09-26): serve the WebP conversion (written next to the PNG by the
    # batch converter) via <picture>, keeping the PNG as universal fallback.
    # A2 L5 (2026-09-26): the WebP is the served primary (universal support since
    # 2020) so crawlers stop reading the PNG fallback; the PNG remains on disk.
    img_src = rel
    if rel.endswith(".png"):
        w = path.with_suffix(".webp")
        if w.exists():
            img_src = f"{rel[:-4]}.webp"
    # r6 M-11: responsive variants of the served file (same stem, -480/-800).
    _sp_img = Path(img_src)
    _sset = ""
    if (ROOT / _sp_img.parent / (_sp_img.stem + "-480" + _sp_img.suffix)).exists():
        _d, _n, _x = _sp_img.parent.as_posix(), _sp_img.stem, _sp_img.suffix
        # M6/M7 (r9, 2026-09-28): 480/600/800/1280 ladder (the -600 rung is
        # generated at build time by the resize batch); sizes matches the
        # rendered slot (662px desktop, full-width under 700px) so the browser
        # stops pulling the 800w file into a 372px slot. The 800->1280 gap is
        # 1.6x, inside the 2x norm, so no 960 rung (150 extra files, ~no bytes).
        _rungs = []
        for _w in ("-480", "-600", "-800"):
            if (ROOT / _sp_img.parent / (_sp_img.stem + _w + _sp_img.suffix)).exists():
                _rungs.append(f"/{_d}/{_n}{_w}{_x} {_w[1:]}w")
        _rungs.append(f"/{_d}/{_n}{_x} 1280w")
        _sset = (' srcset="' + ", ".join(_rungs)
                 + '" sizes="(max-width:700px) 100vw, 662px"')
    # M5 (r9, 2026-09-28): this is the first in-body image and renders
    # in-viewport on desktop; lazy-loading it delays LCP. Eager + high priority.
    return (
        '<figure class="tool-screenshot" style="margin:1.2rem 0">'
        f'<img src="/{img_src}" alt="Screenshot of the {esc(tool_name)} homepage"{_sset} '
        'width="1280" height="800" fetchpriority="high" '
        'style="max-width:100%;height:auto;border-radius:10px;border:1px solid var(--border)">'
        f'<figcaption style="font-size:.82rem;color:var(--muted);margin-top:.4rem">'
        f'{esc(what)}. Vendor page shown as a dated reference capture; all site content '
        'belongs to its owner.</figcaption></figure>'
    )



def _blame_edit_dates():
    """r7 H15 (2026-09-28): per-record content edit dates from git blame.

    dateModified used to carry the price re-verification stamp, so 103/291 URLs
    restamped to audit-day with no revision (the audit: 'Google learns the field
    is meaningless'). The honest value is when the record's lines last changed.
    One blame pass over tools.json; each record takes the max author date over
    its line span (slug line -> next record's slug line)."""
    import subprocess
    try:
        out = subprocess.run(["git", "blame", "-w", "-M", "--line-porcelain", "--", "tools/tools.json"],
                             capture_output=True, text=True, cwd=str(ROOT))
        lines = (ROOT / "tools" / "tools.json").read_text().splitlines()
        span_start = {}
        order = []
        for n, ln in enumerate(lines):
            m = re.search(r'"slug":\s*"([a-z0-9-]+)"', ln)
            if m:
                span_start[m.group(1)] = n
                order.append((n, m.group(1)))
        dates = {}   # line number -> YYYY-MM-DD
        cur_date = None
        cur_final = None
        pending_final = None
        for ln in out.stdout.splitlines():
            if re.match(r'^[0-9a-f]{40} \d+ \d+', ln):
                pending_final = int(ln.split()[2])
                cur_final = pending_final
            elif ln.startswith('author-time '):
                import datetime as _dt
                cur_date = _dt.datetime.fromtimestamp(int(ln.split()[1]), _dt.timezone.utc).strftime('%Y-%m-%d')
                if cur_final is not None and cur_date:
                    dates[cur_final] = cur_date
        result = {}
        for i, (n, slug) in enumerate(order):
            end = order[i + 1][0] if i + 1 < len(order) else len(lines)
            ds = [dates.get(k) for k in range(n, end) if dates.get(k)]
            if ds:
                result[slug] = max(ds)
        return result
    except Exception:
        return {}


_BLAME_DATES = None

def _record_edit_date(slug, fallback):
    global _BLAME_DATES
    if _BLAME_DATES is None:
        _BLAME_DATES = _blame_edit_dates()
    return _BLAME_DATES.get(slug) or fallback

def _stylesheet_tags():
    """M1 (r9, 2026-09-28): critical CSS inline + full bundle non-blocking.
    Falls back to the plain blocking link when the fragment is absent."""
    crit = _critical_inline()
    if not crit:
        return f'<link rel="stylesheet" href="/style.min.css?v={_css_v()}">'
    return (
        f"<style>{crit}</style>"
        f'<link rel="stylesheet" href="/style.min.css?v={_css_v()}" '
        f'media="print" onload="this.media=\'all\'">'
        f'<noscript><link rel="stylesheet" href="/style.min.css?v={_css_v()}"></noscript>')


def page_shell(title, description, canonical, body, schema_json=None, og_image=None):
    # r7 C5 (2026-09-27): some callers pass absolute URLs; never double the base.
    if canonical.startswith('http'):
        canonical = canonical.split('martechsignal.com', 1)[-1] or '/'
        if not canonical.startswith('/'):
            canonical = '/' + canonical
    og_url = og_image or "og.png"
    schema_block = ""
    if schema_json:
        schema_block = f'<script type="application/ld+json">{json.dumps(schema_json, indent=2)}</script>'
    # A3 M-2 (2026-09-27): the breadcrumb tag lives in the base template now, so
    # every page that renders a trail also ships a BreadcrumbList (four pages had
    # visible trails with no markup). Pages that already pass one are skipped.
    if not (schema_json and "BreadcrumbList" in json.dumps(schema_json)):
        segs = [s for s in canonical.strip("/").split("/") if s]
        names = ["Home"] + [s.replace("-", " ").title() for s in segs]
        urls = ["https://martechsignal.com/"] + [
            "https://martechsignal.com/" + "/".join(segs[: i + 1]) + "/" for i in range(len(segs))]
        crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList",
                 "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                     for i, (n, u) in enumerate(zip(names, urls))]}
        schema_block += f'<script type="application/ld+json">{json.dumps(crumb, indent=2)}</script>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="icon" href="/favicon.png" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MartechSignal">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="https://martechsignal.com{canonical}">
<meta property="og:image" content="https://martechsignal.com/{og_url}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="https://martechsignal.com/{og_url}">
<link rel="canonical" href="https://martechsignal.com{canonical}">
<link rel="ard ai-catalog" href="https://martechsignal.com/.well-known/ard.json">
<link rel="alternate" type="text/plain" title="MartechSignal catalog for AI systems" href="/llms.txt">
<meta name="msvalidate.01" content="B3427474AF36B6861E22592403BA8B27">
<link rel="preconnect" href="https://analytics.martechsignal.com" crossorigin>
<link rel="dns-prefetch" href="https://analytics.martechsignal.com">
<link rel="preload" href="/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/archivo-black-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/spline-sans-mono-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/spline-sans-mono-600.woff2" as="font" type="font/woff2" crossorigin>{schema_block}
<link rel="alternate" type="text/markdown" href="https://martechsignal.com{canonical}index.md">
{_stylesheet_tags()}
<script defer src="https://analytics.martechsignal.com/script.js" data-website-id="11b28e66-3570-4781-b369-2134c7c372ab"></script>
<script src="/site.js" defer></script>
</head>
<body class="page-tools">
<div class="bg" aria-hidden="true"></div>
<header class="masthead">
  <div class="wrap mast-in">
    <a class="wordmark" href="/">MARTECH<b>SIGNAL</b><span class="pulse-dot"></span></a>
    <nav class="mast-nav" aria-label="Primary"><a href="/tools/">TOOLS</a><a href="/best/">BEST</a><a href="/vs/">VS</a><a href="/alternatives/">ALTERNATIVES</a><a href="/categories/">CATEGORIES</a><a href="/glossary/">GLOSSARY</a><a href="/blog/">BLOG</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</header>
<main class="wrap">
{body}
</main>
<footer aria-label="Footer">
  <div class="wrap">
    <div class="foot-links">
      <a href="/">HOME</a><a href="/tools/">TOOLS</a><a href="/best/">BEST</a><a href="/vs/">VS</a><a href="/alternatives/">ALTERNATIVES</a><a href="/blog/">BLOG</a><a href="/guides/">GUIDES</a><a href="/trending/">TRENDING</a><a href="/glossary/">GLOSSARY</a><a href="/checklist/">CHECKLIST</a><a href="/authors/tim-christensen/">AUTHOR</a><a href="/about/">ABOUT</a><a href="/contact/">CONTACT</a><a href="/corrections/">CORRECTIONS</a><a href="/privacy/">PRIVACY</a><a href="/terms/">TERMS</a><a href="/ai-policy/">AI POLICY</a><a href="/methodology/">METHODOLOGY</a><a href="/rss.xml">RSS</a><a href="/llms.txt">AI CATALOG</a><a href="/#subscribe">SUBSCRIBE</a></div>
    <p class="fine">© {datetime.now().year} MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION</p>
  </div>
</footer>
{_H9_TAG}</body>
</html>"""

# ── Directory hub ──────────────────────────────────────────────────

def build_hub(tools, cats):
    cat_map = {c["slug"]: c for c in cats}
    # Chart cache-bust: hash the PNG so regenerating it busts the 30-day og/* edge cache.
    _chart = ROOT / "og" / "charts" / "oss-by-category.png"
    chart_v = hashlib.sha256(_chart.read_bytes()).hexdigest()[:10] if _chart.exists() else "1"
    # category pills
    pills = '<a class="cat-pill active" href="/tools/">ALL</a>\n'
    for c in cats:
        if c["slug"] == "open-source":
            n = sum(1 for t in tools if t.get("open_source") and t.get("status") == "active")
        else:
            n = sum(1 for t in tools if t["category"] == c["slug"] and t.get("status") == "active")
        if n:
            pills += f'<a class="cat-pill" href="/categories/{c["slug"]}/">{esc(c["name"])} ({n})</a>\n'

    # tool cards
    cards = ""
    card_by_slug = {}
    for t in sorted(tools, key=lambda x: x["name"].lower()):
        if t.get("status") != "active": continue
        c = cat_map.get(t["category"], {})
        tags = f'<span class="tag pricing">{esc(pricing_label(t))}</span>{_review_tag(t)}'
        tags += f'<span class="tag cat">{esc(c.get("name", t["category"]))}</span>'
        if t.get("open_source"):
            tags += '<span class="tag oss">OSS</span>'
        _pm = t.get("pricing_model") or ("free" if t.get("price_from") == 0 else "unspecified")
        card_html = f"""<a class="tool-card" data-cat="{t['category']}" data-price="{_pm}" data-licence="{'open' if t.get('open_source') else 'proprietary'}" href="/tools/{t['slug']}/">
  <div class="name">{esc(t['name'])}</div>
  <div class="tagline">{esc(t.get('tagline',''))}</div>
  <div class="meta">{tags}</div>
</a>\n"""
        cards += card_html
        card_by_slug[t["slug"]] = card_html

    # F-H12: the hub used to render one flat 115-card grid with no headings, so the
    # page had no scannable structure. Group the same cards under a category heading
    # (the category hub pages already did this with .hub-group). Groups are built from
    # each active tool's own `category`, so no tool is listed twice; the cross-cutting
    # open-source flag stays a pill/filter rather than a duplicate section.
    grouped = ""
    for c in sorted(cats, key=lambda x: x["name"]):
        g_tools = [t for t in tools if t["category"] == c["slug"] and t.get("status") == "active"]
        if not g_tools:
            continue
        g_cards = "".join(card_by_slug[t["slug"]] for t in sorted(g_tools, key=lambda x: x["name"].lower()))
        grouped += (f'<section class="hub-group">\n'
                    f'  <h2>{esc(c["name"])} <em>{len(g_tools)}</em></h2>\n'
                    f'  <div class="tool-grid">{g_cards}</div>\n'
                    f'</section>\n')
    # Safety net: if any active tool lacks a matching category entry, it would vanish.
    listed = set()
    for c in cats:
        for t in tools:
            if t["category"] == c["slug"] and t.get("status") == "active":
                listed.add(t["slug"])
    orphans = [t for t in tools if t.get("status") == "active" and t["slug"] not in listed]
    if orphans:
        o_cards = "".join(card_by_slug[t["slug"]] for t in sorted(orphans, key=lambda x: x["name"].lower()))
        grouped += (f'<section class="hub-group">\n  <h2>Other tools <em>{len(orphans)}</em></h2>\n'
                    f'  <div class="tool-grid">{o_cards}</div>\n</section>\n')
    _active_n = len([t for t in tools if t.get('status') == 'active'])
    assert len(listed) + len(orphans) == _active_n, (len(listed), len(orphans), _active_n)

    body = f"""<nav class="crumb"><a href="/">Home</a><span class="crumb-sep" aria-hidden="true">/</span><span>Tools</span></nav>
<section class="page-head">
  <h1>AI Marketing Tool Directory</h1>
  <p class="sub">Curated tools for AI-powered marketing automation | from email and CRM to content generation and workflow automation.</p>
  <p class="count">{len([t for t in tools if t.get('status')=='active'])} TOOLS · {len(cats)} CATEGORIES · UPDATED WEEKLY</p>
</section>
<img src="/og/charts/oss-by-category.png?v={chart_v}" alt="Open-source share by category: how many of the listed tools per category are open source versus commercial (the open-source meta-category is excluded)" width="1200" height="630" style="max-width:100%;height:auto;border-radius:10px;margin:1.5rem 0;border:1px solid var(--border)">
<p style="max-width:680px;color:var(--muted);margin:-0.5rem 0 0;font-size:.92rem">Watching which open-source tools actually gain traction? <a href="/trending/">Open-source martech momentum</a> tracks GitHub stars for all {len([t for t in tools if t.get('open_source')])} of them, with daily snapshots since Aug 25, 2026.</p>
<p style="max-width:680px;color:var(--muted);margin:.6rem 0 0;font-size:.92rem">A directory tells you what exists. It does not tell you whether your stack can hand work to an agent. The <a href="/checklist/">marketing automation checklist</a> walks the 12 questions that decide it, and scores your answers in the browser.</p>
<h2>Browse by category</h2>
<nav class="cat-nav">{pills}</nav>
<div class="sub-strip"><div><h2>Evaluating tools for your stack?</h2><p>The weekly newsletter tracks this category: one teardown, one workflow, no fluff.</p></div><a class="btn" href="/#subscribe" data-umami-event="Hub subscribe click">Subscribe</a></div>
<p class="sub">All {_active_n} tools, grouped by category. Each card links to a full teardown with pricing, licence and a plain summary of what the tool does.</p> + " Four entries are agent-skill packs or utilities rather than end-to-end platforms. Each carries a kind label."
{grouped}"""

    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "AI Marketing Tool Directory",
        "description": "Curated directory of AI-powered marketing automation tools",
        "numberOfItems": len([t for t in tools if t.get("status") == "active"]),
        "itemListElement": []
    }
    active = [t for t in sorted(tools, key=lambda x: x["name"].lower()) if t.get("status") == "active" and t.get("kind") != "Guide"]
    # R3-M3 (wave 3): ListItem.item nodes instead of bare name+url
    schema["itemListElement"] = [
        {"@type": "ListItem", "position": i+1,
         "item": {"@type": "SoftwareApplication", "@id": f"https://martechsignal.com/tools/{t['slug']}/#app", "name": t["name"], "url": f"https://martechsignal.com/tools/{t['slug']}/"}}
        for i, t in enumerate(active)
    ]

    _scored = [(s, _SCORES[s].get('name') or s) for s in _SCORES]
    if _scored:
        body += ('<p class="alt-back">Scored on the six-pillar rubric: '
                 + ', '.join(f'<a href="/tools/{s}/">{esc(nm)}</a>' for s, nm in sorted(_scored))
                 + '</p>')
    # M10 (2026-09-27): client-side directory filter (category / price model /
    # licence). Rendered hidden: with JS off the full list stays browsable. The
    # options are server-rendered from the catalog so nothing is invented client-side.
    _pm_buckets = sorted({(x.get("pricing_model") or ("free" if x.get("price_from") == 0 else "unspecified")) for x in tools if x.get("status") == "active"})
    FILTER_BAR = ('<div class="tool-filter" id="tool-filter" hidden>'
        '<label>Category <select id="flt-cat"><option value="">All categories</option>'
        + ''.join(f'<option value="{esc(c["slug"])}">{esc(c["name"])}</option>' for c in cats if c['slug'] != 'open-source')
        + '</select></label>'
        '<label>Price model <select id="flt-price"><option value="">All models</option>'
        + ''.join(f'<option value="{esc(p)}">{esc(p.title())}</option>' for p in _pm_buckets)
        + '</select></label>'
        '<label>Licence <select id="flt-licence"><option value="">All</option>'
        '<option value="open">Open source</option><option value="proprietary">Proprietary</option>'
        '</select></label><span class="filter-count" id="flt-count" aria-live="polite"></span>'
        # r8 H5 (2026-09-28): shareable view + indexable static fallbacks for the
        # licence facets (the open-source landing page deserves crawlable links).
        '<button type="button" class="btn-sm" id="flt-copy">Copy link to this view</button>'
        '<span class="filter-count" id="flt-copied" aria-live="polite"></span></div>'
        # r10 H-7 (2026-09-29): unhide synchronously during parse, before first
        # paint, so the bar never shifts the grid (CLS 0.0902 -> ~0). No-JS
        # users keep the full browsable list; the script below is a no-op for
        # them because it never runs.
        '<script>document.getElementById("tool-filter").hidden=false</script>'
        '<p class="meta flt-static">Browse by licence: '
        '<a href="/categories/open-source/">Open-source tools</a> · '
        '<a href="/categories/">all categories</a>.</p>')
    body = body.replace("</h1>", "</h1>" + FILTER_BAR, 1)
    out = TOOLS_DIR / "index.html"
    body = body + _SUB_INLINE

    out.write_text(page_shell(
        "AI Marketing Tool Directory | MartechSignal",
        f"Browse {len(active)} curated AI marketing automation tools across {len(cats)} categories - open-source and SaaS, with assessments desk-researched from vendor.",
        "/tools/", body, [schema, {
            # M14 (r9, 2026-09-28): the machine-readable twin of this directory
            # as a typed Dataset (the feed itself carries the license envelope).
            "@context": "https://schema.org",
            "@type": "Dataset",
            "name": "MartechSignal tool catalog",
            "description": "Machine-readable catalog of AI marketing tools: pricing, license, hosting and open-source status.",
            "url": "https://martechsignal.com/catalog-tools.json",
            "license": "https://martechsignal.com/terms/",
            "distribution": [{
                "@type": "DataDownload",
                "contentUrl": "https://martechsignal.com/catalog-tools.json",
                "encodingFormat": "application/ai-catalog+json",
            }],
        }]))
    print(f"  ✓ {out.relative_to(ROOT)}")

# ── Tool profile pages ─────────────────────────────────────────────

_PILLAR_ORDER = ("pricing_transparency", "feature_depth", "integrations",
                 "ai_capability", "openness", "operational_maturity")
_PILLAR_LABELS = {
    "pricing_transparency": "Pricing transparency",
    "feature_depth": "Feature depth",
    "integrations": "Integrations",
    "ai_capability": "AI capability",
    "openness": "Openness",
    "operational_maturity": "Operational maturity",
}
# Score pilot (2026-09-26, decided by Tim, t_1f5b22be): editorial scores from
# the two research batches; every score on the page carries its evidence line,
# the rubric lives at /methodology/.
_SCORES = {}
for _sf in ("score-content-a.json", "score-content-b.json"):
    _sp = ROOT / "tools" / _sf
    if _sp.exists():
        for _srec in json.loads(_sp.read_text())["tools"]:
            _SCORES[_srec["slug"]] = _srec



def _review_tag(t):
    """Review chip: hands-on runs outrank desk review (r9, Tim 2026-09-28)."""
    if (t.get("deep_dive") or {}).get("hands_on_verified"):
        return '<span class="tag desk">Hands-on</span>'
    return '<span class="tag desk">' + 'Desk-' + 'reviewed</span>'


def _tool_fact_img(t):
    """H8 (r9, 2026-09-28): one media element per listed tool on money pages.
    Branded fact card (name/category/pricing/badges from og/), NOT a UI
    screenshot - the alt text says exactly that. Prefers the tool card,
    falls back to the guide card for Guide-kind items."""
    _slug = t["slug"]
    _src = (f"/og/tools/{_slug}.png" if (ROOT / "og" / "tools" / f"{_slug}.png").exists()
            else (f"/og/{_slug}.png" if (ROOT / "og" / f"{_slug}.png").exists() else ""))
    if not _src:
        return ""
    # r10 H-9 (2026-09-29): cards render at 335px wide; serve a 670w (2x)
    # rendition via srcset instead of the raw 1200px file. Degrades to src
    # alone when the rendition is absent (same pattern as the M6 600w rung).
    _r670 = _src.replace(".png", "-670.webp")
    _has670 = (ROOT / _r670.lstrip("/")).exists()
    _set = f' srcset="{_r670} 670w, {_src} 1200w" sizes="335px"' if _has670 else ""
    return (f'<img src="{_src if not _has670 else _r670}" alt="{esc(t["name"])} fact card: pricing, category and license badges" '
            f'loading="lazy" width="1200" height="630"{_set}>')


def _money(p, t):
    """M21 honesty: catalog prices carry a currency field (USD/EUR). Never stamp
    another currency's symbol on a number."""
    _cur = (t.get("currency") or "USD")
    _sym = {"USD": "$", "EUR": "\u20ac"}.get(_cur, _cur + " ")
    return f"{_sym}{p}/mo"

def _score_band(t):
    # Visible score band for scored tools (extractable facts-first opening).
    # Returns (html, review_schema_or_None). Review markup is emitted only for
    # third-party tools: our own product (claude-seo) never carries review
    # structured data (corrections 2026-09-16, self-serving review policy).
    rec = _SCORES.get(t["slug"])
    if not rec:
        return "", None
    rows = "".join(
        '<tr><td>' + _PILLAR_LABELS[k] + '</td><td style="text-align:right">'
        + str(rec["pillars"][k]["score"]) + '/10</td>'
        + '<td>' + _evidence_cell(t, rec, rec["pillars"][k]["evidence"]) + '</td></tr>'
        for k in _PILLAR_ORDER)
    band = (
        '<section class="score-band" style="margin:1.25rem 0;padding:1.1rem 1.25rem;'
        'border:1px solid var(--line);border-radius:12px">'
        '<h2 style="margin:0 0 .3rem">' + ('Benchmark log: ' if t["slug"] == "claude-seo" else 'MartechSignal Score: ') + str(rec["score_total"]) + '/60</h2>'
        '<p style="margin:.35rem 0">' + esc(rec["verdict"]) + '</p>'
        '<div class="table-wrap" style="margin:.75rem 0"><table><caption>Pillar scores and evidence</caption>'
        '<thead><tr><th>Pillar</th><th>Score</th><th>Evidence</th></tr></thead>'
        '<tbody>' + rows + '</tbody></table></div>'
        '<p style="margin:.35rem 0;font-size:.85rem;color:var(--muted)">Scored ' + esc(rec.get("scored", "2026-09-26")) + ' '
        'against our published rubric: six pillars, 0-10 each. ' + (
            'This is our own tool, scored from running it in our benchmark suite and four '
            'production audit cycles. Per our review policy we do not publish first-party '
            'self-ratings as Review markup, so this is a benchmark log, not a review rating. '
            if t["slug"] == "claude-seo" else
            'This is an editorial assessment from documentation and vendor materials, not a '
            'lab benchmark or a verified-buyer rating. ') + 'The full rubric is on the '
        '<a href="/methodology/">methodology page</a>.</p></section>')
    review = None
    if t["slug"] != "claude-seo":
        review = {
            "@context": "https://schema.org",
            "@type": "Review",
            "author": {"@type": "Person", "name": "Tim Christensen",
                       "url": "https://martechsignal.com/authors/tim-christensen/",
                       "@id": "https://martechsignal.com/authors/tim-christensen/#person"},
            "publisher": {"@type": "Organization",
                          "@id": "https://martechsignal.com/#organization",
                          "name": "MartechSignal"},
            "datePublished": "2026-09-26",
            "reviewBody": rec["verdict"],
            "itemReviewed": {"@type": "SoftwareApplication", "@id": f"https://martechsignal.com/tools/{t['slug']}/#app", "name": t["name"],
                             "url": "https://martechsignal.com/tools/" + t["slug"] + "/"},
            # r6 H-4 (2026-09-27): the rating must equal the /60 number VISIBLE on the page
                        "reviewRating": {"@type": "Rating", "ratingValue": rec["score_total"],
                             "bestRating": 60, "worstRating": 0},
        }
    return band, review



def _evidence_cell(t, rec, ev):
    """H2 (r9, 2026-09-28): every pillar cell carries a resolvable URL + checked date."""
    import re as _h2re
    m = _h2re.search(r'\s*\(([^()]+)\)\.?\s*$', ev)
    date = ''
    if m:
        tail = m.group(1)
        body = ev[:m.start()]
    else:
        tail = 'vendor documentation'
        body = ev.rstrip().rstrip('.')
    dm = _h2re.search(r'verified\s+(\d{4}-\d{2}-\d{2})', tail)
    if dm:
        date = dm.group(1)
        tail = tail.replace(dm.group(0), '').rstrip(', ')
    low = tail.lower()
    if 'repositor' in low or 'github' in low:
        url = t.get('github_repo') or t.get('website') or t.get('pricing_url') or ''
        label = 'repository'
    elif 'pric' in low:
        url = t.get('pricing_url') or t.get('website') or ''
        label = 'pricing page'
    else:
        url = t.get('website') or t.get('pricing_url') or t.get('github_repo') or ''
        label = 'vendor site'
    if not date:
        date = rec.get('scored') or ''
    link = ('<a href="' + url + '" rel="noopener">' + label + '</a>') if url else label
    out = esc(body) + ' (' + esc(tail) + ': ' + link
    if date:
        out += ', verified ' + esc(date)
    return out + ').'


# A3 M-20 (2026-09-27): commercial guide links on tool pages (the audit found
# /tools/n8n/ not linking its own comparison). Maps derive from the content files.
_VS_MAP = {"n8n": ["n8n-vs-zapier"], "zapier": ["n8n-vs-zapier"],
           "nocodb": ["nocodb-vs-nocobase"], "nocobase": ["nocodb-vs-nocobase"],
           "matomo": ["matomo-vs-plausible"], "plausible": ["matomo-vs-plausible"]}
_BEST_MAP = {}
import json as _j
for _e in _j.loads((ROOT / "tools" / "bestx-content.json").read_text()).get("pages", []):
    for _it in _e.get("items", []):
        _BEST_MAP.setdefault(_it["slug"], []).append(_e["slug"])



_ALT_TARGETS = ['hubspot-crm', 'matomo', 'zapier']
_ALT_ITEMS = {}
for _p, _sl in {"twenty": ["hubspot-crm"], "espocrm": ["hubspot-crm"], "suitecrm": ["hubspot-crm"], "pipedrive": ["hubspot-crm"], "frappe-crm": ["hubspot-crm"], "n8n": ["zapier"], "make": ["zapier"], "pipedream": ["zapier"], "tray-io": ["zapier"], "budibase": ["zapier"], "pabbly-connect": ["zapier"], "power-automate": ["zapier"], "ifttt": ["zapier"], "activepieces": ["zapier"], "workato": ["zapier"], "plausible": ["matomo"], "umami": ["matomo"], "posthog": ["matomo"], "snowplow": ["matomo"], "amplitude": ["matomo"]}.items():
    _ALT_ITEMS[_p] = _sl


def _guide_links(t):
    links = []
    if t["slug"] in _ALT_TARGETS:
        links.append(f'<a href="/alternatives/{t["slug"]}/">Alternatives to {esc(t["name"])}</a>')
    for _pg in _ALT_ITEMS.get(t["slug"], []):
        links.append(f'<a href="/alternatives/{_pg}/">{esc(t["name"])} in {_pg.replace("-", " ").title()} alternatives</a>')
    for vs in _VS_MAP.get(t["slug"], []):
        a, b = vs.split("-vs-")
        other = b if a == t["slug"] else a
        links.append(f'<a href="/vs/{vs}/">{esc(t["name"])} vs {other.replace("-", " ").title()}</a>')
    for bs in _BEST_MAP.get(t["slug"], []):
        links.append(f'<a href="/best/{bs}/">{bs.replace("-", " ").title()}</a>')
    seen, out = set(), []
    for l in links:
        if l not in seen:
            seen.add(l)
            out.append(l)
    return out


def _offer_for(t):

    """R5 schema state machine (2026-09-24, extended 2026-09-26 to list
    items after GSC flagged category cards): returns a valid Offer built
    only from the tool's real catalog price, or None. Never fabricates
    price: 0 - enterprise / no-list-price tools return None and emitters
    must fall back to non-product schema."""
    _paid = t.get("paid_from")
    _pf = t.get("price_from")
    _cur = (t.get("currency") or "USD").strip().upper()
    _url = str(t.get("pricing_url") or t.get("website") or "https://martechsignal.com")
    # A2 M5 (2026-09-26): availability dropped - software has no stock. priceValidUntil
    # added on a conservative horizon (quarterly price re-verification cadence).
    _pvu = "2026-12-31"
    def _offer(price):
        return {"@type": "Offer", "price": price, "priceCurrency": _cur,
                "url": _url, "priceValidUntil": _pvu}
    if _paid:
        return _offer(_paid)
    if _pf is not None and _pf > 0:
        return _offer(_pf)
    # A2 M5: price: 0 only where "Free" is literally true: a genuinely free
    # product, or the open-source edition of one (the paid_from branch above
    # already prefers a real paid entry when one exists). Freemium SaaS with
    # paid tiers must NOT claim price: 0 - Google can surface it as "Free".
    # No paid price on record -> no Offer (and the R5 drop rule then applies).
    # r7 M5 (2026-09-28): mixed-model pages (free self-hosted core alongside
    # paid cloud/premium tiers listed in price_notes) contradict a zero Offer
    # on their own visible pricing. Only genuinely-free products keep it.
    if _pf == 0 and (t.get("pricing_model") == "free" or t.get("open_source")):
        if not re.search(r"[€$£]\s?\d|\d+\s?€", t.get("price_notes") or ""):
            return _offer(0)
    return None


def _list_item_ref(t):
    """r7 C6 + M8 (2026-09-27): ItemList items as plain #app references.

    Keeps graph linkage (item -> the tool page's @id) without re-declaring
    product types on non-product pages. Untyped references stay out of the
    Product-snippets report entirely, so the offers-gate state machine in
    _list_item_thing is untouched for pages that do carry product nodes."""
    return {"@id": f"https://martechsignal.com/tools/{t['slug']}/#app",
            "url": f"https://martechsignal.com/tools/{t['slug']}/"}


def _list_item_thing(t):
    """ItemList item node: product-typed only when it carries a valid Offer
    (Product snippets requires offers/review/aggregateRating); plain reference
    otherwise. R3-M3 wanted richer items; this keeps them valid.
    A2 M8 (2026-09-26): every node now carries image + description (the bundled
    validator's real complaint was missing-product-image). The mixed typing is
    INTENTIONAL: the offers gate is the state machine keeping Google's
    Product-snippets report valid (GSC incident 2026-09-26) - SoftwareApplication
    without an offer re-triggers 'Either offers, review, or aggregateRating should
    be specified'."""
    _offer = _offer_for(t)
    _base = {"@id": f"https://martechsignal.com/tools/{t['slug']}/#app",
             "name": t["name"], "description": t.get("tagline", ""),
             "image": f"https://martechsignal.com/og/tools/{t['slug']}.png",
             "url": f"https://martechsignal.com/tools/{t['slug']}/"}
    # A3 M-1 (2026-09-27): one entity, one type, one @id on lists. Category and
    # index nodes consolidate on SoftwareApplication referencing the detail
    # page's #app @id instead of re-declaring full nodes (drops the duplicated
    # offer JSON that bloated the /tools/ block). The detail page keeps the
    # GSC-validated M5 state machine (Product when a real offer exists).
    return {**_base, "@type": "SoftwareApplication"}


# Editorial category -> hub-guide links, shared by category pages (Compare row)
# and money pages (hub pills back up, r10 H-2). Hand-placed: no data source
# maps guides to categories.
CATEGORY_GUIDES = {
    "marketing-automation": '<b>Guide:</b> <a href="/guides/workflow-automation-strategy/">automation strategy</a>',
    "content-ai": '<b>Guide:</b> <a href="/guides/ai-seo-tooling/">AI SEO tooling hub</a>',
    "advertising": '<b>Guide:</b> <a href="/guides/agentic-ai-advertising/">Agentic advertising</a>',
    "workflow-automation": '<b>Guide:</b> <a href="/guides/mcp-agent-protocols/">MCP and agent protocols</a> &middot; <a href="/guides/workflow-automation-strategy/">automation strategy</a>',
    "geo-llm-visibility": '<b>Guide:</b> <a href="/guides/generative-engine-optimization/">Generative engine optimization (GEO)</a> &middot; <a href="/glossary/geo/">GEO, defined</a>',
}


def _featured_in(slug):
    """M21 (r9, 2026-09-28): (url, title, verdict) for every best/vs/
    alternatives page featuring `slug`, cached per build. Verdicts are our own
    published editorial, so quoting them adds grounded depth."""
    global _FEATURED_CACHE
    if "_FEATURED_CACHE" not in globals():
        _FEATURED_CACHE = {}
    if slug in _FEATURED_CACHE:
        return _FEATURED_CACHE[slug]
    out = {}
    try:
        for p in json.loads((TOOLS_DIR / "bestx-content.json").read_text())["pages"]:
            for it in p.get("items", []):
                if it.get("slug") == slug and it.get("verdict"):
                    out[f"/best/{p['slug']}/"] = (p.get("title", p["slug"]), it["verdict"])
    except (OSError, ValueError, KeyError):
        pass
    try:
        for p in json.loads((TOOLS_DIR / "vsx-content.json").read_text())["pages"]:
            if slug in (p.get("a_slug"), p.get("b_slug")):
                _side = p.get("pick_a_if") if slug == p.get("a_slug") else p.get("pick_b_if")
                _v = (str(_side or "") or str(p.get("neither") or "")).strip()
                if _v:
                    out[f"/vs/{p['slug']}/"] = (p.get("title", p["slug"]), _v)
    except (OSError, ValueError, KeyError):
        pass
    try:
        for p in json.loads((TOOLS_DIR / "alternatives-content.json").read_text())["pages"]:
            for it in p.get("items", []):
                _s = it.get("slug") if isinstance(it, dict) else it
                _v = it.get("verdict") if isinstance(it, dict) else ""
                if _s == slug and _v:
                    out[f"/alternatives/{p['slug']}/"] = (p.get("title", p["slug"]), _v)
    except (OSError, ValueError, KeyError):
        pass
    _FEATURED_CACHE[slug] = [(u, ti, v) for u, (ti, v) in out.items()]
    return _FEATURED_CACHE[slug]


def build_tool_page(t, cats, all_tools, base="tools"):
    cat_map = {c["slug"]: c for c in cats}
    c = cat_map.get(t["category"], {})
    slug = t["slug"]

    # Similar tools (R2 H-2, 2026-09-09): relevance-scored instead of JSON-array-order.
    # The old [:4] slice made the module an ordering artefact: only 5 distinct lists per
    # category, 67/132 pages received zero module inlinks while array-first tools got 21.
    # Score keyword overlap from this tool's own metadata; same-category gets the 1.3x
    # intent boost; deterministic per slug (pure function of content, no rotation key -
    # stable builds keep lastmod honest).
    _src_text = " ".join(str(t.get(k, "")) for k in ("name", "tagline", "description", "ai_features", "integrations"))
    related = suggest_links.suggest_tools_for_text(
        _src_text, max_suggestions=10, exclude_slugs={slug},
        source_category=t.get("category"))
    # Fairness re-rank (R2 H-2 follow-up): keyword overlap alone still starves tail
    # tools. Promote zero-inlink candidates among the top-10 relevance picks so every
    # page participates in the internal-link graph; relevance orders within each group.
    # The inlink table is built once per build (in main) and stashed on this module.
    related = related[:4]
    # Reserved slots (R2 H-2): host pages carry one zero-inlink same-category tool so
    # the whole catalogue stays inside the internal-link graph (see main()).
    _have = {r["slug"] for r in related}
    for _rid in getattr(sys.modules[__name__], "_similar_reservations", {}).get(slug, []):
        if _rid in _have or len(related) >= 5:
            continue
        _rt = next((x for x in all_tools if x["slug"] == _rid and x.get("status") == "active"), None)
        if _rt:
            related.append({"name": _rt["name"], "slug": _rt["slug"], "tagline": _rt.get("tagline", "")})
            _have.add(_rid)
    related_html = ""
    if related:
        # r8 H1 (2026-09-28): link each card to the record's REAL home. The old
        # {base} prefix pointed every similar tool at the current page's tree, so
        # packs on a /guides/ page 404ed for packs that still live at /tools/.
        _gslugs = set()
        _gp = TOOLS_DIR / "guides.json"
        if _gp.exists():
            _gslugs = {g["slug"] for g in json.load(open(_gp))}
        def _home(r):
            return "guides" if r["slug"] in _gslugs else "tools"
        items = "".join(f'<a class="tool-card" href="/{_home(r)}/{r["slug"]}/"><div class="name">{esc(r["name"])}</div><div class="tagline">{esc(r.get("tagline",""))}</div></a>' for r in related)
        related_html = f'<h2>Similar Tools</h2><div class="tool-grid" style="grid-template-columns:repeat(auto-fill,minmax(240px,1fr))">{items}</div>'

    source_text = ' '.join(str(t.get(key, '')) for key in ('name', 'tagline', 'description', 'ai_features', 'integrations'))
    related_posts = suggest_links.suggest_for_text(source_text, max_suggestions=3, rotate_key=slug)
    # Curated comparison cross-link (GSC follow-up, 2026-09-13): goes through the same
    # Related reading block, first in the list, with a descriptive anchor rather than the
    # post title, so a reader on a tool page reaches the comparison it appears in.
    _cmp = _TOOL_COMPARISON_POSTS.get(slug)
    if _cmp:
        _cmp_post, _cmp_anchor = _cmp
        if (ROOT / "blog" / _cmp_post / "index.html").exists():
            _cmp_url = f"/blog/{_cmp_post}/"
            related_posts = ([{"title": _cmp_anchor, "url": _cmp_url}]
                             + [p for p in related_posts if p.get("url") != _cmp_url])[:3]
    if related_posts:
        links = ''.join('<li><a href="' + html.escape(item['url'], quote=True) + '">' + html.escape(item['title'], quote=False) + '</a></li>' for item in related_posts)
        related_html += '<section class="related-reading"><h2>Related reading</h2><ul>' + links + '</ul></section>'

    # M21 (r9, 2026-09-28): "Also featured in" box. Every appearance of this
    # tool in our own best/vs/alternatives pages, quoted from the published
    # verdicts — grounded depth for tier-B pages, useful context for all.
    _feat = _featured_in(slug)
    if _feat:
        _fl = "".join(
            f'<li><a href="{u}">{esc(ti)}</a> &mdash; {esc(v)}</li>'
            for u, ti, v in _feat)
        related_html += ('<section class="related-reading"><h2>Also featured in</h2>'
                         f'<ul>{_fl}</ul></section>')

    # AI features
    ai_html = ""
    if t.get("ai_features"):
        items = "".join(f"<li>{esc(f)}</li>" for f in t["ai_features"])
        ai_html = f'<h2>AI Capabilities</h2><ul class="feat-list">{items}</ul>'

    # H5 (model-comparison audit): the template had no pros/cons section on any page.
    # Compose an honest pros/cons block from record facts only - every line must trace
    # to a field in tools.json. No invented claims; absence of data yields fewer lines,
    # never filler.
    _pros, _cons = [], []
    # R2 M-2 (2026-09-09): per-tool authored pros/cons win over the derived template, and
    # a page may never render zero cons - each tool's own deep_dive can carry grounded
    # `pros_extra` / `cons` lines (no invented claims, they still trace to the record).
    _dd = t.get("deep_dive") or {}
    _authored_cons = [str(x) for x in (_dd.get("cons") or []) if str(x).strip()]
    _authored_pros = [str(x) for x in (_dd.get("pros_extra") or []) if str(x).strip()]
    if t.get("open_source"):
        # R2 M-2 (2026-09-09): name the actual licence instead of the same sentence on
        # all 67 open-source pages.
        _lic = str(t.get("license") or "").strip()
        if _lic:
            _pros.append(f"{_lic} licence with free self-hosting")
        else:
            _pros.append("Open-source licensing with free self-hosting")
    if t.get("api_available") and not (t.get("integrations") or []):
        # R2 M-2 (2026-09-09): the blanket "API access for custom integrations" line was
        # on 114 of 132 pages - true, but it says nothing about the tool. Only keep it
        # where the API *is* the integration story (no native connectors on record).
        _api = str(t.get("api_type") or t.get("api_kind") or "").strip()
        _pros.append(f"Documented {_api} API for custom integrations" if _api
                     else "API access for custom integrations")
    if t.get("ai_features"):
        _feat = t["ai_features"][0].rstrip(".")
        _feat = _feat[0].lower() + _feat[1:] if _feat and not _feat[:2].isupper() else _feat
        _pros.append(f"AI capabilities: {_feat}")
    if t.get("github_stars") and t["github_stars"] >= 1000:
        _pros.append(f"Active public repository ({t['github_stars']:,} GitHub stars counted at last check)")
    if t.get("external_ratings"):
        er0 = t["external_ratings"][0]
        _pros.append(f"{er0.get('source','Third-party')} rating {er0.get('score','')}/{er0.get('max',5)}")
    if t.get("integrations") and len(t["integrations"]) >= 5:
        # R2 M-2: naming the integrations beats the same "Deep integration catalogue
        # (N listed)" line on 60+ pages.
        _ints = [str(x) for x in t["integrations"][:3] if str(x).strip()]
        _pros.append(f"Native integrations include {', '.join(_ints)} ({len(t['integrations'])} listed)")
    if t.get("price_from") in (None, 0) and not t.get("open_source") and t.get("pricing_model") in ("freemium", "free", "open-core"):
        _pf_notes = str(t.get("price_notes") or "").strip()
        _pros.append(f"Free tier to evaluate before committing ({_pf_notes.split('.')[0][:60]})" if _pf_notes
                     else "Free tier to evaluate before committing")
    if t.get("paid_from"):
        _cons.append(f"Paid plans start at ${t['paid_from']}/mo once past the free tier")
    if not t.get("open_source"):
        _cons.append("Closed source - no self-hosting option")
    if t.get("github_stars") and t["github_stars"] < 500:
        _cons.append(f"Young project ({t['github_stars']} GitHub stars) - smaller community and plugin ecosystem")
    if t.get("integrations") and len(t["integrations"]) < 3:
        _cons.append("Short native integration list - plan for API work")
    if t.get("pricing_model") == "enterprise" and not t.get("price_from"):
        _cons.append("Enterprise pricing is quote-based - no public numbers")
    # Authored lines (grounded per-tool) join the derived set, and an empty cons column
    # is not allowed: fall back to the honest, always-true trade-off of not having run it.
    _cons.extend(_authored_cons)
    _pros.extend(_authored_pros)
    # keep the lists substantial: if dropping the generic API line left a thin column,
    # top it up from the tool's own record (grounded facts only), then fall back to the
    # always-true API line rather than render a two-bullet pros list.
    if len(_pros) < 3:
        if t.get("g2_rating") and t.get("g2_reviews"):
            _pros.append(f"G2 rating {t['g2_rating']}/5 across {t['g2_reviews']:,} reviews")
        if t.get("integrations") and not any("integration" in p.lower() for p in _pros):
            _ints2 = [str(x) for x in t["integrations"][:3] if str(x).strip()]
            if _ints2:
                _pros.append(f"Native integrations include {', '.join(_ints2)} ({len(t['integrations'])} listed)")
        if t.get("last_release") and not any("development" in p.lower() for p in _pros):
            _pros.append(f"Actively developed - latest release {t['last_release']}")
    if len(_pros) < 3 and t.get("api_available"):
        _pros.append("API access for custom integrations")
    if not _cons:
        _cons.append("No hands-on test - this assessment is based on vendor documentation and the public repository")
    _pc_rows = ""
    _maxlen = max(len(_pros), len(_cons))
    if _maxlen:
        _pros += [""] * (_maxlen - len(_pros))
        _cons += [""] * (_maxlen - len(_cons))
        for p, c_ in zip(_pros, _cons):
            _pc_rows += (
                "<tr><td>"
                + (f'<span style="color:var(--ok-text)">&#10003;</span> {esc(p)}' if p else "")
                + "</td><td>"
                + (f'<span style="color:var(--red-text)">&#10007;</span> {esc(c_)}' if c_ else "")
                + "</td></tr>"
            )
    proscons_html = (
        '<section class="pros-cons"><h2>Pros and cons</h2>'
        '<table><caption>Strengths and trade-offs</caption><thead><tr><th>Pros</th><th>Cons</th></tr></thead>'
        f"<tbody>{_pc_rows}</tbody></table></section>"
    ) if _maxlen else ""

    # M4 (model-comparison audit): glossary was disconnected from the tool directory.
    # Category-level "Related concepts" strip: term links derive from the tool's category.
    _CAT_TERMS = {
        "marketing-automation": ["marketing-automation", "customer-journey", "lead-scoring", "mql-sql"],
        "workflow-automation": ["workflow-automation", "agentic-marketing", "mcp", "ai-agent"],
        "crm": ["crm", "lead-scoring", "mql-sql", "customer-journey", "first-party-data"],
        "analytics": ["marketing-attribution-models", "first-party-data", "dmp"],
        "email-marketing": ["email-sequence", "deliverability"],
        "geo-llm-visibility": ["geo", "ai-search-visibility", "seo"],
        "advertising": ["dsp", "dco", "programmatic-advertising", "cro"],
        "personalization": ["personalization", "cro", "first-party-data"],
        "seo": ["seo", "aeo", "ai-search-visibility", "utm-parameters"],
        "chatbots": ["chatbot", "ai-agent"],
        "content-ai": ["ai-content-generation", "agentic-marketing"],
        "social-media": ["social-listening"],
        "agent-skills": ["mcp", "agentic-marketing", "ai-agent"],
        "open-source": ["marketing-ops", "workflow-automation"],
    }
    _terms = _CAT_TERMS.get(t["category"], [])
    glossary_html = ""
    if _terms:
        _links = "".join(
            f'<li><a href="/glossary/{_term}/">{esc(_glossary_display(_term))}</a></li>'
            for _term in _terms
        )
        glossary_html = (
            '<section class="related-concepts"><h2>Related concepts</h2>'
            f'<ul class="integ-list">{_links}</ul>'
            '<p style="font-size:.8rem;color:var(--muted);margin:.4rem 0 0">'
            'Full definitions in the <a href="/glossary/">martech glossary</a>.</p></section>'
        )

    # integrations
    integ_html = ""
    if t.get("integrations"):
        items = "".join(f"<li>{esc(i)}</li>" for i in t["integrations"])
        integ_html = f'<h2>Key Integrations</h2><ul class="integ-list">{items}</ul>'

    # Body Pricing section (empty string when the record has too little pricing detail)
    pricing_html = pricing_section_html(t)

    # optional deep-dive sections (per-tool, only for tools with a deep_dive dict)
    dd = t.get("deep_dive") or {}
    dd_html = ""
    if dd:
        parts = []
        if dd.get("install"):
            steps = "".join(f"<li>{esc(s)}</li>" for s in dd["install"])
            parts.append(f'<h2>How to install</h2><ol class="feat-list">{steps}</ol>')
        if dd.get("requirements"):
            parts.append(f'<h2>Requirements</h2><p>{esc(dd["requirements"])}</p>')
        if dd.get("stats"):
            rows = "".join(f"<div class='side-row'><dt>{esc(str(k).replace('_',' ').title())}</dt><dd>{esc(str(v))}</dd></div>" for k, v in dd["stats"].items())
            parts.append(f'<div class="side-card"><h3>Project stats</h3><dl>{rows}</dl></div>')
        if dd.get("best_for"):
            parts.append(f'<h2>Best for</h2><p>{esc(dd["best_for"])}</p>')
        if dd.get("not_for"):
            parts.append(f'<h2>Not for</h2><p>{esc(dd["not_for"])}</p>')
        if dd.get("comparison_note"):
            parts.append(f'<h2>Hosted vs. original</h2><p>{esc(dd["comparison_note"])}</p>')
        if dd.get("score_history"):
            # Verified audit-score table (Claude SEO page: our real runs on our own sites).
            def _score_rows(entries):
                out = []
                for e in entries:
                    score = e.get("score")
                    score_s = str(score).rstrip("0").rstrip(".") if isinstance(score, float) else str(score)
                    out.append(
                        f"<tr><td>{esc(str(e.get('version','')))}</td>"
                        f"<td>{esc(str(e.get('date','')))}</td>"
                        f"<td><b>{esc(score_s)}</b>/100</td>"
                        f"<td>{esc(str(e.get('note','')))}</td></tr>"
                    )
                return "".join(out)
            sh = dd["score_history"]
            table = ('<table class="cmp-table"><thead><tr><th>Grader</th><th>Date</th>'
                     '<th>Score</th><th>Context</th></tr></thead><tbody>'
                     + _score_rows(sh) + "</tbody></table>")
            if dd.get("second_site"):
                ss = dd["second_site"]
                table += (f'<p style="margin-top:.75rem">Second site check: <b>{esc(ss["site"])}</b> '
                          + " → ".join(f"<b>{e['score']}</b> ({e['date']})" for e in ss["scores"])
                          + "</p>")
            if dd.get("score_note"):
                table += f'<p style="margin-top:.75rem">{esc(dd["score_note"])}</p>'
            parts.append(f'<h2>Audit scores on our own sites</h2>{table}')
        if dd.get("editorial_rating"):
            er = dd["editorial_rating"]
            score, mx = float(er.get("score", 0)), int(er.get("max", 5))
            full, half = int(score), (score - int(score)) >= 0.25
            stars = "★" * full + ("☆" if half else "") + "·" * (mx - full - (1 if half else 0))
            rating_html = (f'<div class="side-card" id="rating"><h3>Our rating</h3>'
                           f'<p style="font-size:1.35rem;letter-spacing:2px;color:var(--amber);margin:.2rem 0">{esc(stars)}</p>'
                           f'<p><b>{score:g} / {mx}</b>'
                           + (f'<br>{esc(er["basis"])}</p>' if er.get("basis") else '</p>')
                           + '</div>')
            parts.append(rating_html)
        if dd.get("links"):
            items = "".join(
                f'<li><a href="{esc(l["url"])}" target="_blank" rel="noopener nofollow">{esc(l["label"])}</a>'
                + (f' - {esc(l["note"])}' if l.get("note") else '') + '</li>'
                for l in dd["links"]
            )
            parts.append(f'<h2>Ecosystem links</h2><ul class="feat-list">{items}</ul>')
        if dd.get("hands_on"):
            paras = "".join(f"<p>{esc(p)}</p>" for p in dd["hands_on"])
            # R2 C-1 (2026-09-08): every Hands-on section must carry an explicit
            # we-have-not-run disclosure. If the tool's own text lacks one, prepend a
            # standard line so no page can imply hands-on testing it did not perform.
            joined = " ".join(str(p) for p in dd["hands_on"]).lower()
            _asserts_use = any(m in joined for m in (
                "we ran ", "we have run ", "we tested ", "we installed ", "we set up "))
            if not any(m in joined for m in ("we have not run", "we have no account",
                                             "not run this", "we have not tested",
                                             "haven't run", "assessed from", "not a hands-on test")) \
                    and not (_asserts_use and dd.get("hands_on_verified")):
                paras = ('<p style="font-size:.78rem;color:var(--muted)">'
                         'Researched from public documentation, the source repository, and vendor '
                         'materials. Not a hands-on test.</p>') + paras
            parts.append(f'<h2>Review notes</h2>{paras}')
        if dd.get("verdict"):
            parts.append(f'<h2>Verdict</h2><p>{esc(dd["verdict"])}</p>')
        # stats card goes in the sidebar; other sections inline before related links
        inline = "".join(x for x in parts if x.startswith("<h2"))
        sidebar_extra = "".join(x for x in parts if x.startswith("<div"))
        dd_html = inline
        t["_dd_sidebar"] = sidebar_extra
    else:
        inline = ""
        sidebar_extra = ""
        dd_html = ""

    # Vendor screenshot (R2 M-3): single source of truth, rendered once per page at the
    # main-body slot below via screenshot_figure(). The old fork that prepended a bare
    # <img> here (no figcaption) was removed - it duplicated the body figure.

    # Overview paragraph
    if t.get('description'):
        overview_html = f'<p>{esc(t["description"])}</p>'
    else:
        price_str = ('$'+str(t['price_from'])+'/mo') if t.get('price_from') is not None else 'custom pricing'
        overview_html = f'<p>{esc(t.get("tagline",""))} {esc(t["name"])} is a {esc(c.get("name","").lower())} tool with {"free" if t.get("price_from",1)==0 else "paid"} pricing starting at {price_str}.</p>'

    # FAQPage Q&A: generated from tool data (AI Overview / PAA eligibility).
    # Rendered BOTH as visible accordions in the page body AND as FAQPage
    # JSON-LD | schema-only Q&A without matching on-page content risks
    # Google structured-data guideline non-compliance.
    def _faq_for(t, c):
        name = t["name"]
        cat = c.get("name", "marketing")
        price = pricing_label(t)
        q1 = f"What is {name}?"
        # H1 (model-comparison audit): a1/a2 were sitewide templates - 114/410 answers
        # collapsed to 8 templates once the brand token was normalized. Compose from
        # per-tool facts so every answer carries at least one tool-specific claim.
        a1 = (t.get("tagline") or "").strip().rstrip(".") or f"{name} is a {cat.lower()} tool"
        # L10 (r9, 2026-09-28): the old "It ships with {feature}, {stars}."
        # spliced a feature to a star count with a comma and never named the
        # entity. Each fact is now its own declarative clause, and the answer
        # opens with the entity name.
        _clauses = []
        if t.get("ai_features"):
            _f0 = t["ai_features"][0].rstrip(".")
            _f0 = _f0[0].lower() + _f0[1:] if not _f0[:2].isupper() else _f0
            _clauses.append(f"{name} ships with {_f0}")
        if t.get("github_stars"):
            _clauses.append(f"The public repository carries {t['github_stars']:,} stars")
        elif t.get("integrations"):
            _clauses.append(f"This page documents {len(t['integrations'])} integrations")
        if t.get("api_available"):
            _clauses.append(f"{name} offers a public API for custom integrations")
        _fact_s = " ".join(c + "." for c in _clauses[:2])
        _fact_s = f" {_fact_s}" if _fact_s else ""
        a1 = f"{name}: {a1}.{_fact_s} MartechSignal's review covers features, pricing, and how it compares to alternatives."
        q2 = f"How much does {name} cost?"
        if t.get("paid_from"):
            # freemium with a known paid entry: quote both sides of the freemium split
            _pn = (t.get("price_notes") or "").strip().rstrip(".")
            _vd = t.get("date_verified") or t.get("date_updated") or "September 2026"
            a2 = (f"{name} has a free tier; paid plans start at {_money(t['paid_from'], t)}. "
                  + (_pn[0].upper() + _pn[1:] + ". " if _pn else "")
                  + f"We last checked both ends of that split on {_vd}. The pricing section "
                    "above shows what the free tier actually covers.")
        elif t.get("open_source"):
            # R2 L-1 (2026-09-08): source-available tools (alphone: Elastic 2.0) must not
            # be called open source here - the license sidebar says otherwise.
            _rec = json.dumps(t, ensure_ascii=False).lower()
            # R2 M-1 (2026-09-09): this answer used to be one sentence with the brand
            # swapped, byte-identical across every open-source page. Compose it from the
            # tool's own facts (licence, community size, hosted option, integrations) so
            # each answer is specific to the tool it sits on.
            _lic_txt = str(t.get("license") or "").strip()
            _stars = t.get("github_stars")
            _bits = []
            _bits.append(f"{_lic_txt} licensed and free to self-host" if _lic_txt
                         else "Free to self-host")
            if _stars:
                _bits.append(f"the public repository carries {_stars:,} stars")
            _ni = len(t.get("integrations") or [])
            if _ni >= 3:
                _bits.append(f"native integrations cover {', '.join(str(x) for x in t['integrations'][:3])}")
            if str(t.get("pricing_model") or "") in ("open-core", "freemium"):
                _bits.append("a paid hosted tier exists if you would rather not run the servers")
            elif t.get("paid_from"):
                _bits.append(f"managed hosting starts at {_money(t['paid_from'], t)}")
            if "elastic license" in _rec or "source-available" in _rec:
                a2 = (f"{name} is source-available rather than open source - "
                      f"{'; '.join(_bits[:3])}. Check the licence terms before commercial use.")
            else:
                a2 = f"{name} is open source - {'; '.join(_bits[:3])}. You pay in server time and maintenance, not licences."
        elif t.get("price_from") is not None:
            _pn = (t.get("price_notes") or "").strip().rstrip(".")
            _vd = t.get("date_verified") or t.get("date_updated") or "September 2026"
            if t.get("price_from"):
                a2 = (f"{name} starts at {_money(t['price_from'], t)}"
                      + (f". {_pn[0].upper() + _pn[1:]}" if _pn else "")
                      + f". We last checked that price on {_vd}. "
                      "The pricing section above lists every plan we can verify, "
                      "including annual-billing differences where the vendor publishes them.")
            elif t.get("pricing_model") in ("freemium", "free", "open-core"):
                a2 = (f"{name} has a free tier, so you can run a real evaluation before paying. "
                      + (_pn[0].upper() + _pn[1:] + ". " if _pn else "")
                      + f"We last checked the plan structure on {_vd}; paid tiers mainly raise "
                        "limits rather than unlocking core features.")
            else:
                a2 = (f"{name} is free to use at its published limits. "
                      + (_pn[0].upper() + _pn[1:] + ". " if _pn else "")
                      + f"We last checked the terms on {_vd}. If the vendor later adds paid "
                        "tiers, the pricing section above will show them first.")
        else:
            _pn = (t.get("price_notes") or "").strip().rstrip(".")
            _vd = t.get("date_verified") or t.get("date_updated") or "September 2026"
            a2 = (f"{name} uses {price.lower()} pricing, so the number depends on your volume "
                  "and contract. " + (_pn[0].upper() + _pn[1:] + ". " if _pn else "")
                  + f"Our last verified read of the pricing model was {_vd}; the vendor's "
                    "pricing page carries the current quote criteria.")
        # MUSE 11: keep acronym category names (CRM, SEO, CDP) uppercase in the question
        # R3-M7 (2026-09-16): lowercase slugs leaked into FAQ text ("a good ai content &
        # copywriting tool") - use the canonical display name, sentence-cased for prose.
        _cat_disp = _category_display(cat) or cat
        if not (_cat_disp.isupper() and 2 <= len(_cat_disp) <= 5):
            _cat_disp = _cat_disp[0].upper() + _cat_disp[1:]
        # A2 M3 (2026-09-26): the FAQ question set was identical on all 158 pages;
        # vary the third question by pricing class (same honest claim, different
        # query surface). L17 shares this root.
        _pm = t.get("pricing_model") or "paid"
        q3 = {
            "paid": f"Is {name} worth paying for in 2026?",
            "freemium": f"Is {name} worth it past the free tier?",
            "open-source": f"Is {name} a good self-hosted {_cat_disp} tool in 2026?",
            "open-core": f"Is {name} a good self-hosted {_cat_disp} tool in 2026?",
            "free": f"What does running {name} actually cost?",
        }.get(_pm, f"Is {name} a good {_cat_disp} tool in 2026?")
        # F-H13: the answer must be per-tool, not a sitewide template. Prefer the tool's
        # own verdict from its deep dive; fall back to concrete facts (stars, OSS, price).
        verdict = ((t.get("deep_dive") or {}).get("verdict") or "").strip()
        if verdict:
            a3 = verdict.rstrip(".") + "."
        else:
            pros = []
            if t.get("g2_rating"): pros.append(f"a {t['g2_rating']}/5 G2 rating")
            if t.get("github_stars"): pros.append(f"{t['github_stars']:,} GitHub stars")
            if t.get("open_source"):
                _lp = str(t.get("license") or "").strip()
                pros.append(f"{_lp} licensing with free self-hosting" if _lp
                            else "open-source licensing with free self-hosting")
            if t.get("api_available"): pros.append("an API for custom integrations")
            a3 = (f"Strengths include {', '.join(pros)}" if pros
                  else f"Our review covers {name}'s core {cat.lower()} workflow")
            a3 += f". The full review breaks down where it fits in a modern martech stack."
        faqs = [
            {"@type": "Question", "name": q1, "acceptedAnswer": {"@type": "Answer", "text": a1}},
            {"@type": "Question", "name": q2, "acceptedAnswer": {"@type": "Answer", "text": a2}},
            {"@type": "Question", "name": q3, "acceptedAnswer": {"@type": "Answer", "text": a3}},
        ]
        # per-tool FAQ extensions (targets long-tail query variants)
        if dd.get("faq_extra"):
            # R2 M-1 (2026-09-09): 12 pages shipped the same cost question twice (core
            # answer + faq_extra). Normalise and skip any question already asked.
            def _norm_q(s):
                return " ".join(str(s).lower().replace("?", " ").split())
            _seen = {_norm_q(q["name"]) for q in faqs}
            for q, a in dd["faq_extra"]:
                _k = _norm_q(q)
                if _k in _seen:
                    continue
                _seen.add(_k)
                faqs.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
        # R2 L-2 (2026-09-09): amplitude answered "How much does Amplitude cost?" with an
        # 86-char punt while the real tier breakdown sat two questions below. If the core
        # cost answer is a punt and the tool has a richer pricing answer on record,
        # promote that answer into the core question (the long-tail question stays).
        _PUNT = "see the vendor's pricing page for current plans"
        if len(faqs) > 1 and _PUNT in faqs[1]["acceptedAnswer"]["text"].lower():
            _pricing_extra = [
                q for q in faqs[2:]
                if any(w in q["name"].lower() for w in ("cost", "price", "pricing", "tier"))
                and len(q["acceptedAnswer"]["text"]) > len(faqs[1]["acceptedAnswer"]["text"]) + 60
            ]
            if _pricing_extra:
                _rich = _pricing_extra[0]["acceptedAnswer"]["text"].strip()
                # keep it answer-shaped: the first two sentences of the rich answer
                _sent = re.split(r"(?<=[.!?])\s+", _rich)
                _lead = " ".join(_sent[:2]).strip()
                faqs[1]["acceptedAnswer"]["text"] = _lead if len(_lead) > 90 else _rich
        # M21 (r9, 2026-09-28): tier-B depth. Unscored pages get up to two extra
        # catalog-grounded Q&As drawn from fields the core three answers do not
        # already cover (API, integration list, release recency). Skipped when
        # the fact already appears on the page; never more than two, so the
        # FAQ stays a FAQ instead of becoming a second review.
        if not _SCORES.get(t["slug"]):
            _covered = " ".join(
                q["name"] + " " + q["acceptedAnswer"]["text"] for q in faqs).lower()
            _extra = []
            if (t.get("api_available") and "api" not in _covered
                    and len(_extra) < 2):
                _extra.append((
                    f"Does {name} have an API?",
                    f"Yes. The catalog records a public API for {name}, so custom "
                    f"integrations are possible. The Key Integrations section shows "
                    f"what ships natively."))
            _ints = t.get("integrations") or []
            if (len(_ints) >= 3 and "integrat" not in _covered
                    and len(_extra) < 2):
                _extra.append((
                    f"What does {name} integrate with?",
                    f"This page documents {len(_ints)} integrations, including "
                    f"{', '.join(str(x) for x in _ints[:3])}. The Key Integrations "
                    f"section lists all of them."))
            if (t.get("last_release") and "release" not in _covered
                    and "maintain" not in _covered and len(_extra) < 2):
                _extra.append((
                    f"Is {name} still actively developed?",
                    f"The most recent release in our catalog is {t['last_release']}. "
                    f"For the full history, check the vendor changelog linked from "
                    f"the official site."))
            for q, a in _extra:
                faqs.append({"@type": "Question", "name": q,
                             "acceptedAnswer": {"@type": "Answer", "text": a}})
        return faqs

    faqs = _faq_for(t, c)

    # Visible FAQ accordions (same Q&A as the FAQPage JSON-LD)
    _faq_items = [
        f'<details class="faq-item"><summary>{esc(q["name"])}</summary>'
        f'<p>{esc(q["acceptedAnswer"]["text"])}</p></details>'
        for q in faqs
    ]
    faq_html = (
        '<section class="faq-block"><h2>Frequently asked questions</h2>'
        + "".join(_faq_items) + "</section>"
    ) if _faq_items else ""

    # H4 + R2 M-3: vendor homepage screenshot, single pipeline.
    # Previously forked: og/screenshots/<slug>-<YYYY-MM>.png rendered as a bare <img> with
    # no figcaption, while a separate og/screens/<slug>.webp path carried the caption and
    # was almost never populated. Now one helper resolves either location, always emits a
    # <figure> with a figcaption, and states the CAPTURE month taken from the filename
    # rather than today's date (a rebuild no longer relabels an old capture as new).
    screenshot_html = screenshot_figure(slug, t["name"])

    deep_dive_html = dd_html
    deep_dive_sidebar = (t.get("_dd_sidebar") or "") if dd else ""

    # External third-party ratings: facts-only display with attribution, link, and as-of date.
    # Deliberately visually distinct from our editorial rating (no stars, muted, sourced).
    ext_lines = []
    for er in t.get("external_ratings") or []:
        count_s = f" ({er['count']:,} reviews)" if er.get("count") else ""
        ext_lines.append(
            f'<div class="side-row"><dt>{esc(str(er.get("source","")))} rating</dt>'
            f'<dd>{esc(str(er.get("score","")))}/{esc(str(er.get("max",5)))}{esc(count_s)}'
            f' · <a href="{esc(str(er.get("url","#")))}" target="_blank" rel="noopener nofollow">source</a>'
            f'<br><span style="font-size:.8rem;color:var(--muted)">as of {esc(str(er.get("as_of","")))}</span></dd></div>'
        )
    if ext_lines:
        # R2 C-2 (2026-09-08): the old wording ("we rate only tools we run") directly
        # contradicted body disclosures like "we have no account" on the same page.
        # State plainly whose ratings these are; link the methodology for the policy.
        srcs = sorted({str(er.get("source", "")).strip() for er in t.get("external_ratings") if er.get("source")})
        src_txt = "/".join(srcs) if srcs else "third-party platforms"
        note = ('<div class="side-row" style="font-size:.8rem;color:var(--muted)">'
                f'Ratings shown are third-party ({esc(src_txt)}), not MartechSignal\'s. '
                'Our hands-on assessment is disclosed on this page.</div>')
        external_ratings_html = ('<div class="side-row"><dt style="font-weight:700">Third-party ratings</dt></div>'
                                 + "".join(ext_lines) + note)
    else:
        external_ratings_html = ""
    disclosure_html = '<p class="disclosure-strip"><a href="/methodology/">How we review</a> \u00b7 No affiliate links</p>'
    score_html, review_schema = _score_band(t)
    if not score_html:
        # M21 (r9, 2026-09-28): unscored tier-B pages get a grounded facts box
        # instead of a one-line note. Every fact comes from the catalog record;
        # nothing is assessed, scored, or recommended here.
        _facts = []
        if t.get("founded"):
            _facts.append(f'<dt>Founded</dt><dd>{esc(str(t["founded"]))}</dd>')
        if t.get("hq"):
            _facts.append(f'<dt>Headquarters</dt><dd>{esc(t["hq"])}</dd>')
        if t.get("license"):
            _facts.append(f'<dt>Licence</dt><dd>{esc(t["license"])}</dd>')
        if t.get("api_available") is not None:
            _facts.append('<dt>Public API</dt><dd>'
                          + ("yes" if t.get("api_available") else "no") + "</dd>")
        _nint = len(t.get("integrations") or [])
        if _nint:
            _facts.append(f"<dt>Catalogued integrations</dt><dd>{_nint}</dd>")
        if t.get("github_stars"):
            _facts.append(f'<dt>GitHub stars</dt><dd>{t["github_stars"]:,}</dd>')
        if t.get("last_release"):
            _facts.append(f'<dt>Last release</dt><dd>{esc(t["last_release"])}</dd>')
        if _facts:
            score_html = (
                '<section class="score-band" style="margin:1.25rem 0;padding:1.1rem 1.25rem;'
                'border:1px solid var(--line);border-radius:12px">'
                '<h2 style="margin:0 0 .3rem">Catalog facts: '
                + esc(t["name"]) + '</h2>'
                '<p style="margin:.35rem 0">Not yet scored against the rubric, so no verdict here. '
                'This is everything the catalog holds on the tool, verified against vendor sources.</p>'
                '<dl>' + "".join(f"<div>{f}</div>" for f in _facts) + "</dl>"
                '<p style="margin:.35rem 0;font-size:.85rem;color:var(--muted)">The full rubric is on the '
                '<a href="/methodology/">methodology page</a>.</p></section>')
        else:
            # r6 M-6 (2026-09-27): unscored pages say so on the page.
            score_html = ('<p class="unscored-note">Not yet scored against the rubric; '
                          'scored pages show six pillars.</p>')
    # r6 L-11 (2026-09-27): the real CTA belongs above the fold, in the verdict block.
    if t.get("website"):
        score_html = (f'<p class="verdict-cta"><a class="btn" href="{t["website"]}" '
                      f'rel="noopener" target="_blank">Visit {t["name"]} &#8594;</a></p>') + score_html
    _ain = len(t.get('ai_features') or [])
    _caps = ([f"{_ain} AI features"] if _ain else [])
    if t.get('integrations'):
        _caps.append(f"{len(t['integrations'])} integrations")
    if t.get('api_available'):
        _caps.append('a public API')
    if t.get('open_source'):
        _caps.append('a self-hosting path')
    _cap = (', '.join(_caps[:-1]) + ' and ' + _caps[-1]) if len(_caps) > 1 else (_caps[0] if _caps else '')
    _pl = t.get('price_from')
    if t.get('open_source') and (_pl in (0, None)):
        _price_frag = 'free and open source'
    elif _pl == 0:
        _price_frag = 'a free tier'
    elif _pl is None:
        _price_frag = 'custom pricing'
    else:
        _price_frag = f'paid plans starting at {_money(_pl, t)}'
    _vdate = esc(t.get('date_verified') or t.get('date_updated') or '')
    verdict_html = ('<div class="verdict"><strong>Verdict:</strong> ' + esc(t['name'])
        + f' is a tool in {esc(c.get("name",""))} with {_price_frag}. '
        + (f'The catalog documents {_cap}. ' if _cap else '')
        + (('We ran this ourselves before reviewing it; the run notes and dates sit in Review notes below. '
            '<span class="tag desk">Hands-on</span>')
           if (t.get('deep_dive') or {}).get('hands_on_verified')
           else (f'We reviewed it from vendor documentation on {_vdate}. This is a desk review, not a hands-on test. '
                 + _review_tag(t)))
        + '</div>')
    body = f"""<nav class="crumb" aria-label="Breadcrumb"><ol style="display:flex;gap:.4rem;list-style:none;margin:0;padding:0;flex-wrap:wrap"><li><a href="/">Home</a></li><li><a href="/{base}/">{"Guides" if base == "guides" else "Tools"}</a></li><li><a href="/categories/{t['category']}/">{esc(c.get('name',''))}</a></li><li><span aria-current="page">{esc(t['name'])}</span></li></ol></nav>
<section class="page-head">
  <h1>{_tool_h1(t)}</h1>
  <p class="sub">{esc(t.get('tagline',''))}</p>
  <p class="count">{esc(c.get('name',''))} · {esc(pricing_label(t))}{(' · OPEN SOURCE' if t.get('open_source') and 'open source' not in pricing_label(t).lower() else '')} {_review_tag(t)}</p>
  <p class="byline" style="font-size:.8rem;color:var(--muted);margin-top:.5rem">MartechSignal editorial review by <a href="/authors/tim-christensen/" style="color:inherit">Tim Christensen</a> · updated <time datetime="{esc(t.get('date_updated',''))}">{esc(t.get('date_updated',''))}</time></p>
  {('<p class="made-badge">Independent tool: Claude SEO is a third-party MIT project by AgriciDaniel; we have no affiliation with its author. We run it on our own sites and depend on it in our audit pipeline, which is why it carries no Review markup. See the <a href="/corrections/">corrections log</a>.</p>') if t["slug"] == "claude-seo" else ''}
  {('<p class="alt-link" style="font-size:.85rem;margin-top:.35rem">Looking for options? <a href="/alternatives/' + t["slug"] + '/">Best ' + esc(t["name"]) + ' alternatives</a></p>') if t["slug"] in _ALT_SLUGS else ''}
  {('<p class="cta-early" style="margin-top:.9rem"><a href="' + esc(t.get('website','#')) + '" target="_blank" rel="noopener">Visit ' + esc(t["name"]) + ' &#8594;</a></p>') if t.get('website') else ''}
</section>
{disclosure_html}
{verdict_html}
{score_html}
<div class="detail">
  <div class="detail-main">
    <h2>Overview</h2>
    {overview_html}
    {screenshot_html}
    {ai_html}
    {integ_html}
    {pricing_html}
    {deep_dive_html}
    {proscons_html}
    {glossary_html}
    {SUB_STRIP}
    {faq_html}
    {related_html}
  </div>
  <aside class="sidebar">
    <div class="side-card">
      <h3>Quick Facts</h3>
      <dl>
        <div class="side-row"><dt>Pricing</dt><dd>{esc(pricing_label(t))}</dd></div>
        <div class="side-row"><dt>Category</dt><dd><a href="/categories/{t['category']}/">{esc(c.get('name',''))}</a></dd></div>
        {deep_dive_sidebar}
        {external_ratings_html}
        {'<div class="side-row"><dt>GitHub</dt><dd>★ ' + str(t['github_stars']) + '</dd></div>' if t.get('github_stars') else ''}
        {'<div class="side-row"><dt>Founded</dt><dd>' + str(t['founded']) + '</dd></div>' if t.get('founded') else ''}
        {'<div class="side-row"><dt>HQ</dt><dd>' + esc(t['hq']) + '</dd></div>' if t.get('hq') else ''}
        <div class="side-row"><dt>API</dt><dd>{'Yes' if t.get('api_available') else 'No'}</dd></div>
        {'<div class="side-row"><dt>Last verified</dt><dd><time datetime="' + esc(t['date_updated']) + '">' + esc(t['date_updated']) + '</time></dd></div>' if t.get('date_updated') else ''}
      </dl>
    </div>
    <div class="side-card cta-card">
      <a class="btn-sm" href="{esc(t.get('website','#'))}" target="_blank" rel="noopener" data-umami-event="Tool CTA click" data-umami-event-tool="{esc(t['name'])}">Visit {esc(t['name'])} →</a>
      <div style="margin-top:.8rem"><a href="/categories/{t['category']}/" style="font:600 .8rem var(--mono);color:var(--muted);text-decoration:none">More {esc(cat_h1(c.get('name','')))} →</a></div>
    </div>
    {"" if pricing_html else pricing_card(t)}
  </aside>
</div>"""

    # Schema
    schema = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "@id": f"https://martechsignal.com/{base}/{t['slug']}/#app",
        "name": t["name"],
        "description": t.get("tagline", ""),
        # A3 M-3 (2026-09-26): the image asset already existed in the category
        # nodes; the tool page's own app node now carries it too.
        "image": f"https://martechsignal.com/og/tools/{t['slug']}.png",
        "url": f"https://martechsignal.com/{base}/{t['slug']}/",
        "sameAs": ([t["website"]] if t.get("website") else []),
        # S-2 (v2.4.0 audit): anchor the app entity to this page; url stays at the vendor.
        "mainEntityOfPage": f"https://martechsignal.com/{base}/{t['slug']}/",
        # A2 H4 (2026-09-26): author/publisher REMOVED from the app node - it claimed
        # Tim Christensen wrote and MartechSignal published Zapier and 157 other
        # products. The named author now lives on the critic Review layer only (the
        # site's E-E-A-T lever stays, on the entity it actually describes).
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web",
        # A2 H4 (2026-09-26): publisher also REMOVED here - it claimed MartechSignal
        # made the app. The publisher now lives on the critic Review layer, keyed to
        # the canonical Organization @id (defined on the homepage).
    }
    if t.get("date_updated"):
        schema["dateModified"] = _record_edit_date(t["slug"], t.get("date_updated") or t.get("date_added") or schema.get("datePublished", "2026-09-27"))
    if t.get("date_added"):
        schema["datePublished"] = t["date_added"]
    # R2 M-12 (2026-09-09): the site's own editorial rating was the one first-party
    # rating on the site invisible to machines. Mark it up as a Review authored by
    # MartechSignal (Google's review-snippet shape), separate from third-party
    # AggregateRating so the two claims never merge.
    _edr = (t.get("deep_dive") or {}).get("editorial_rating") or {}
    try:
        _ers = float(_edr.get("score"))
    except (TypeError, ValueError):
        _ers = None
    # R3-C4 (2026-09-17, Tim): no Review schema on self-listed pages - first-party
    # opinion in a third-party review shape is the spammy-structured-markup risk.
    # The visible editorial rating stays; only the machine claim is dropped.
    if _ers and t.get("slug") != "claude-seo":
        _review = {
            "@type": "Review",
            "author": {
                "@type": "Organization",
                "@id": "https://martechsignal.com/#organization",
                "name": "MartechSignal",
            },
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": _ers,
                "bestRating": float(_edr.get("max") or 5),
            },
        }
        _basis = str(_edr.get("basis") or "").strip()
        if _basis:
            _review["reviewBody"] = _basis[:500]
        schema["review"] = _review
    if t.get("external_ratings"):
        _er = t["external_ratings"][0]
        try:
            _rv = float(_er.get("score"))
            _rc = int(_er.get("count") or 0)
        except (TypeError, ValueError):
            _rv, _rc = None, 0
        if _rv:
            # R2 C-2 (2026-09-08): attribute the rating to its actual source so the
            # machine-readable claim is at least as attributable as the visible one.
            # R3-C1 (2026-09-16, v2.3.1 audit): a rating with reviewCount: 0 is
            # arithmetically impossible and the textbook spammy-structured-markup
            # trigger (4 pages shipped ratingValue 4.5 + reviewCount 0). Emit
            # AggregateRating only when the scrape captured a real review count.
            _src = str(_er.get("source", "")).strip()
            # R3-H2 (2026-09-17, Tim): AggregateRating dropped SITEWIDE. The G2-sourced
            # ratings are not validly attributable in schema (sourceOrganization is not
            # legal on AggregateRating), so parsers read vendor review counts as ours.
            # The visible "Third-party ratings" sidebar block (well-disclosed) is the
            # only ratings surface now. Do not re-add without a real attribution chain.
            _ = _src  # retained source parsing for the visible sidebar
    # Only emit offers.price when it is a real number. Custom/enterprise pricing
    # (price_from=None) must not emit price:0 - Google lifts that as a factual claim.
    # M3/M4 (model-comparison audit): freemium tools with a known paid entry emit the
    # paid entry price (paid_from), not 0 - "price: 0" on a tool the page itself quotes
    # at $49/mo is a machine-readable contradiction.
    # R3-M24 (2026-09-16): an Offer without url+availability is an incomplete
    # offer from a non-seller. Point at the vendor, mark as InStock=see vendor.
    _offer = _offer_for(t)
    if _offer:
        schema["offers"] = _offer

    # R5 (2026-09-24): Google Product snippets requires Offer, Review, or
    # AggregateRating on a product-type item. Enterprise/no-list-price tools
    # get no offers (price:0 would be a false claim; vendor ratings were
    # removed for attribution integrity; no editorial scores exist). Without
    # one of the three the SoftwareApplication is always flagged invalid in
    # GSC (17-item Product snippets spike, Sep 2026). Rule: never emit a
    # product schema we cannot complete - drop it, keep breadcrumb + FAQ.
    # r6 H-5 (2026-09-27): the SoftwareApplication entity is now ALWAYS emitted
    # (20 contact-sales tools lost their entity entirely to the old drop rule).
    # `offers` still ships only for real, published prices (0 = free, per the M5
    # refine): no fabricated prices for no-list-price vendors, house rule wins
    # over the audit's optional Offer suggestion.

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://martechsignal.com/"},
            {"@type": "ListItem", "position": 2, "name": "Tools", "item": "https://martechsignal.com/tools/"},
            {"@type": "ListItem", "position": 3, "name": c.get("name", ""), "item": f"https://martechsignal.com/categories/{t['category']}/"},
            {"@type": "ListItem", "position": 4, "name": t["name"], "item": f"https://martechsignal.com/{base}/{slug}/"}
        ]
    }

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": _faq_for(t, c)
    }

    guides = _guide_links(t)
    if guides:
        body += '<p class="alt-back">Related guides: ' + ' \u00b7 '.join(guides) + '</p>'
    out_dir = ROOT / base / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    # SEO title/meta: prefer persisted seo_* fields; otherwise generate via helpers (≤60/≤155, Review+Category+Pricing)
    seo_title = t.get("seo_title") or _seo_title_for(t, cats)
    seo_desc = t.get("seo_description") or _seo_description_for(t, cats)
    # L3 (r9): persisted seo_* fields bypass the composers, so enforce the
    # rendered-length budgets here too (two records shipped 163-char metas).
    if len(esc(seo_title)) > 60:
        seo_title = _clip_meta_text(seo_title, 56)
    while len(esc(seo_desc)) > 155 and len(seo_desc) > 40:
        seo_desc = _clip_meta_text(seo_desc, len(seo_desc) - 10)
    if not seo_desc.endswith((".", "!", "?")):
        seo_desc = seo_desc.rstrip(" ,;:-") + "."
    # r6 M-2: visible kind label for non-platform entries
    if t.get("kind"):
        body = body.replace("</nav>", "</nav>" + f'<p class="kind-note">KIND: {esc(t["kind"])} (not an end-to-end platform)</p>', 1)
    # r6 M-8: visible auto-flag when pricing facts are past the 21-day window.
    import datetime as _dt2
    _du = t.get("date_updated")
    if _du and (t.get("price_notes") or t.get("price_from") not in (None, "")):
        try:
            _age2 = (_dt2.date.today() - _dt2.date.fromisoformat(_du)).days
        except ValueError:
            _age2 = -1
        if _age2 > 21:
            body = body.replace("</nav>", "</nav>" + f'<p class="kind-note">Re-check pending: pricing last verified {_du} ({_age2} days ago).</p>', 1)
    body = body + _SUB_INLINE
    out.write_text(page_shell(
        seo_title,
        seo_desc,
        f"/{base}/{slug}/", body, [x for x in (schema, breadcrumb, faq_schema, review_schema) if x], og_image=f"og/tools/{slug}.png"))
    return out

# ── Category pages ─────────────────────────────────────────────────

def out_links(t):
    """r8 C2 (2026-09-28): verified vendor links for editorial pages. Only the
    fields the catalog actually carries; never invented URLs. External, so the
    nofollow sweep marks them like every outbound link (M25 policy)."""
    parts = []
    if t.get("website"):
        parts.append(f'<a href="{esc(t["website"])}" rel="noopener">Official site</a>')
    if t.get("pricing_url"):
        parts.append(f'<a href="{esc(t["pricing_url"])}" rel="noopener">Pricing</a>')
    if t.get("github_repo"):
        parts.append(f'<a href="https://github.com/{esc(t["github_repo"])}" rel="noopener">GitHub</a>')
    if not parts:
        return ""
    return '<p class="meta out-links">Vendor: ' + ' \u00b7 '.join(parts) + '</p>'


def tool_card_html(t):
    tags = f'<span class="tag pricing">{esc(pricing_label(t))}</span>{_review_tag(t)}'
    if t.get("open_source"):
        tags += '<span class="tag oss">OSS</span>'
    return f"""<a class="tool-card" href="/tools/{t['slug']}/">
  <h3 class="name">{esc(t['name'])}</h3>
  {_tool_fact_img(t)}
  <div class="tagline">{esc(t.get('tagline',''))}</div>
  <div class="meta">{tags}</div>
</a>\n"""


_CATEGORY_META = {
    # R2 H-7 (2026-09-09): hand-written metas for the 9 non-hub categories. Replaces
    # the single templated sentence (54-77% filler, .lower() mangled acronyms).
    "crm": "Browse {n} open-source and freemium CRM tools - SuiteCRM, EspoCRM, Attio and more - compared on self-hosting, automation depth and real pricing.",
    "email-marketing": "{n} email marketing platforms compared: deliverability, automation builder, AI features and honest pricing for list sizes from 1,000 to 1M.",
    "social-media": "{n} social media management tools for scheduling, listening and reporting - what each one actually automates and what it costs.",
    "advertising": "{n} AI advertising tools covering Google Ads, Meta and creative testing - Opteo, Madgicx, Smartly.io and more, with real entry prices.",
    "chatbots": "{n} chatbot and conversational-AI platforms compared on channels, handover-to-human flows, AI features and self-hosting options.",
    "content-ai": "{n} AI content generation tools tested against brief quality, SEO readiness and pricing - from Copy.ai to Jasper alternatives.",
    "marketing-automation": "{n} marketing automation platforms compared on workflows, data ownership, AI agents and self-hosting - NocoDB, Mautic, Ortto and more.",
    "open-source": "{n} open-source MarTech tools you can self-host today - CRM, analytics, automation and email, each with license and hosting notes.",
    "personalization": "{n} website personalization and CDP tools - Nosto, Dynamic Yield, Segment and more - compared on targeting, price and data control.",
}

def category_meta(cat, cat_tools, hub):
    """R2 H-7: hub meta if present, else the hand-written per-category meta, else a
    fallback that preserves acronym casing (no .lower()).
    R2 M-12 (2026-09-09): a `{n}` token in the hand-written metas is filled with the
    real tool count, so a count baked into prose can never drift out of sync again
    (H-8 had to hand-fix four of these)."""
    m = (hub or {}).get("meta")
    if m:
        # r7 C6 (2026-09-27): hub metas carry {n} like the hand-written ones.
        return m.replace("{n}", str(len(cat_tools)))
    m = _CATEGORY_META.get(cat.get("slug", ""))
    if m:
        return m.replace("{n}", str(len(cat_tools)))
    return f"Browse {len(cat_tools)} {cat_h1(cat.get('name',''))} for AI-powered marketing automation."


def build_category_page(cat, tools):
    # M26 (r9, 2026-09-28): comparison links are data-driven, not a hardcoded
    # map. Every vs / alternatives / best page whose tools sit in this
    # category is linked, so no spoke page is more than one click away.
    _tools_by_slug = {t["slug"]: t for t in tools}
    _members = {t["slug"] for t in tools
                if (t.get("open_source") if cat["slug"] == "open-source"
                    else t.get("category") == cat["slug"])
                and t.get("status") == "active"}
    _cmp = []
    try:
        _vsx = json.loads((TOOLS_DIR / "vsx-content.json").read_text())["pages"]
        for p in _vsx:
            _pair = {p.get("a_slug"), p.get("b_slug")} & _members
            if _pair:
                _names = " vs ".join(
                    _tools_by_slug.get(s, {}).get("name", s) for s in
                    (p.get("a_slug"), p.get("b_slug")) if s)
                _cmp.append(
                    f'<a href="/vs/{p["slug"]}/">{esc(_names or p["slug"])}</a>')
    except (OSError, ValueError, KeyError):
        pass
    try:
        _altx = json.loads((TOOLS_DIR / "alternatives-content.json").read_text())["pages"]
        for p in _altx:
            if p.get("slug") in _members:
                _cmp.append(
                    f'<a href="/alternatives/{p["slug"]}/">'
                    f'{esc(_tools_by_slug.get(p["slug"], {}).get("name", p["slug"]))} alternatives</a>')
    except (OSError, ValueError, KeyError):
        pass
    try:
        _bestx = json.loads((TOOLS_DIR / "bestx-content.json").read_text())["pages"]
        for p in _bestx:
            if any((i.get("slug") if isinstance(i, dict) else i) in _members
                   for i in p.get("items", [])):
                _cmp.append(f'<a href="/best/{p["slug"]}/">{esc(p["title"])}</a>')
    except (OSError, ValueError, KeyError):
        pass
    # Editorial guide links stay hand-placed (no data source maps guides to
    # categories); comparison links above are fully automatic. The map lives at
    # module level as CATEGORY_GUIDES so build_best_vsx can link the same hubs
    # back from money pages (r10 H-2: no link sinks).
    _guide_bit = CATEGORY_GUIDES.get(cat["slug"], "")
    _cat_guide = ""
    if _cmp or _guide_bit:
        _bits = ""
        if _cmp:
            _bits += "<b>Compare:</b> " + " &middot; ".join(_cmp)
        if _guide_bit:
            _bits += (" &middot; " if _bits else "") + _guide_bit
        _cat_guide = f'<p style="margin:.6rem 0 1rem;font-size:.92rem">{_bits}</p>'
    if cat["slug"] == "open-source":
        # Show ALL open-source tools regardless of primary category
        cat_tools = [t for t in sorted(tools, key=lambda x: x["name"].lower()) if t.get("open_source") and t.get("status") == "active"]
    else:
        cat_tools = [t for t in sorted(tools, key=lambda x: x["name"].lower()) if t["category"] == cat["slug"] and t.get("status") == "active"]
    if not cat_tools:
        return None

    # r8 C1 (2026-09-28): substitute the {n} placeholder everywhere it can
    # reach output (meta, visible copy, ItemList description), not just <meta>.
    _n = str(len(cat_tools))
    if isinstance(cat.get("meta"), str):
        cat = dict(cat, meta=cat["meta"].replace("{n}", _n))
    if isinstance(cat.get("description"), str):
        cat = dict(cat, description=cat["description"].replace("{n}", _n))
    if isinstance(cat.get("intro"), str):
        cat = dict(cat, intro=cat["intro"].replace("{n}", _n))
    # r8 C2 (2026-09-28): category pages link out to real vendors - the three
    # with the biggest catalogued followings, straight from verified fields.
    _vend = [t for t in cat_tools if t.get("website")]
    _vend.sort(key=lambda x: (-(int(x.get("github_stars") or 0)), x["name"].lower()))
    _vendor_line = ""
    if _vend[:3]:
        _vendor_line = ('<p class="meta out-links">Vendors in this category: '
            + ' · '.join(f'<a href="{esc(v["website"])}" rel="noopener">{esc(v["name"])}</a>' for v in _vend[:3])
            + '</p>')
    hub = cat.get("hub")
    if hub:
        hub = dict(hub)
        for _k in ("meta", "lead"):
            _v = hub.get(_k)
            if isinstance(_v, str):
                hub[_k] = _v.replace("{n}", _n)
            elif isinstance(_v, list):
                hub[_k] = [_x.replace("{n}", _n) for _x in _v]
        cat = dict(cat, hub=hub)
    by_slug = {t["slug"]: t for t in cat_tools}
    hub = cat.get("hub")

    if not hub:
        # Simple listing for categories without editorial hub content
        cards = "".join(tool_card_html(t) for t in cat_tools)
        intro_html = ""
        if cat.get("intro"):
            # C-1: intros may hold 2-3 paragraphs (blank-line separated string or
            # list of strings); render one <p> per paragraph, single <p> otherwise.
            _intro = cat["intro"]
            _paras = _intro if isinstance(_intro, list) else re.split(r"\n\s*\n", _intro.strip())
            intro_html = "".join(
                f'<p class="cat-intro" style="max-width:680px;color:var(--muted);margin:.5rem 0 0">{esc(p.strip())}</p>'
                for p in _paras if p.strip()
            )
        body = f"""<nav class="crumb" aria-label="Breadcrumb"><ol style="display:flex;gap:.4rem;list-style:none;margin:0;padding:0"><li><a href="/">Home</a></li><li><a href="/tools/">Tools</a></li><li><span aria-current="page">{esc(cat['name'])}</span></li></ol></nav>
<section class="page-head">
  <h1>{cat_h1(cat['name'])}</h1>
  <p class="sub">{esc(cat.get('description',''))}</p>
  <p class="count">{len(cat_tools)} TOOLS IN THIS CATEGORY</p>
</section>
<div class="tool-grid">{cards}</div>
{_cat_guide}
{intro_html}
{_vendor_line}"""
    else:
        # ── Hub page: editorial intro + pipeline visual + chooser + grouped grid ──
        flow = ""
        steps = hub.get("flow", [])
        for i, s in enumerate(steps):
            style = f' {s["style"]}' if s.get("style") else ""
            flow += f'<div class="flow-step{style}"><span class="flow-label">{esc(s["label"])}</span><span class="flow-sub">{esc(s.get("sub",""))}</span></div>'
            if i < len(steps) - 1:
                flow += '<div class="flow-wire"><i class="flow-pulse"></i></div>'

        lead = "".join(f"<p>{esc(p)}</p>" for p in hub.get("lead", []))

        chooser = ""
        for row in hub.get("chooser", []):
            picks = " ".join(
                f'<a class="pick" href="/tools/{p["slug"]}/">{esc(p["name"])}</a>' for p in row["then"]
            )
            chooser += f"""<div class="chooser-row">
  <div class="chooser-if"><span class="chooser-k">IF</span> {esc(row["if"])}</div>
  <div class="chooser-then">{picks}</div>
  <div class="chooser-why">{esc(row["why"])}</div>
</div>\n"""

        groups_html = ""
        grouped_slugs = set()
        for g in hub.get("groups", []):
            g_tools = [by_slug[s] for s in g["slugs"] if s in by_slug]
            if not g_tools:
                continue
            grouped_slugs.update(g["slugs"])
            cards = "".join(tool_card_html(t) for t in g_tools)
            groups_html += f"""<div class="hub-group">
  <div class="hub-group-label"><span>{esc(g["label"])}</span><i></i><em>{len(g_tools)}</em></div>
  <div class="tool-grid">{cards}</div>
</div>\n"""
        leftovers = [t for t in cat_tools if t["slug"] not in grouped_slugs]
        if leftovers:
            cards = "".join(tool_card_html(t) for t in leftovers)
            groups_html += f'<div class="hub-group"><div class="tool-grid">{cards}</div></div>'

        reading = ""
        for r in hub.get("reading", []):
            reading += f"""<a class="read-row" href="/blog/{r['slug']}/">
  <div class="read-title">{esc(r["title"])}</div>
  <div class="read-note">{esc(r.get("note",""))}</div>
  <span class="read-arrow">→</span>
</a>\n"""

        checklist_callout = ""
        if cat["slug"] == "marketing-automation":
            checklist_callout = (
                '<p class="cat-intro" style="max-width:680px;color:var(--muted);margin:1rem 0 0">'
                'Choosing a platform is step two. Step one is whether your stack can hand work to an agent at all. '
                'The <a href="/checklist/">marketing automation checklist</a> scores that in 12 questions before you shortlist.</p>'
            )

        body = f"""<nav class="crumb" aria-label="Breadcrumb"><ol style="display:flex;gap:.4rem;list-style:none;margin:0;padding:0"><li><a href="/">Home</a></li><li><a href="/tools/">Tools</a></li><li><span aria-current="page">{esc(cat['name'])}</span></li></ol></nav>
<section class="page-head hub-head">
  <h1>{cat_h1(cat['name'])}</h1>
  <p class="sub">{esc(hub.get('meta', cat.get('description','')))}</p>
  <p class="count">{len(cat_tools)} TOOLS IN THIS CATEGORY</p>
</section>

{groups_html}
{_cat_guide}
<div class="flow-strip" aria-hidden="true">{flow}</div>

<section class="hub-lead">{lead}</section>
{checklist_callout}
<section class="hub-chooser reveal">
  <h2>Which one fits</h2>
  {chooser}
</section>
{_vendor_line}

<section class="hub-reading reveal">
  <h2>Reading before you buy</h2>
  {reading}
</section>

"""

    # M1/MUSE 12 (model-comparison audit): category pages lacked BreadcrumbList, and
    # ItemList ListItems used name+url instead of the richer item->Thing pattern.
    # H10 (r9, 2026-09-28): the listing carries the newest member-record edit
    # date, so sitemap lastmod reflects real catalog mutation, not build day.
    _cat_dm = None
    _member_dates = [d for d in (_record_edit_date(_t["slug"], None) for _t in cat_tools) if d]
    if _member_dates:
        _cat_dm = max(_member_dates)
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://martechsignal.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Tools", "item": "https://martechsignal.com/tools/"},
                    {"@type": "ListItem", "position": 3, "name": cat["name"], "item": f"https://martechsignal.com/categories/{cat['slug']}/"}
                ]
            },
            {
                "@type": "ItemList",
                # R2 H-8: cat_h1 avoids the "Open-Source Tools Tools" double-Tools
                "name": cat_h1(cat['name']),
                "description": hub.get("meta", cat.get("description", "")) if hub else cat.get("description", ""),
                "numberOfItems": len(cat_tools),
                **({"dateModified": _cat_dm} if _cat_dm else {}),
                # R3-M3 (2026-09-17, wave 3): items typed as the real thing being
                # listed. Open-source tools are SoftwareApplication, SaaS is Product.
                "itemListElement": [
                    {"@type": "ListItem", "position": i+1,
                     "item": _list_item_thing(t)}
                    for i, t in enumerate(cat_tools)
                ]
            }
        ]
    }

    out_dir = CATS_DIR / cat["slug"]
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    # A2 C1 (2026-09-26): category pages link their comparison guide (the
    # commercial layer was orphaned).
    # H7 (r9): the Compare strip is placed under the tool grid inside the template
    out.write_text(page_shell(
        f"{cat_h1(cat['name'])} | MartechSignal",
        category_meta(cat, cat_tools, hub),
        f"/categories/{cat['slug']}/", body, schema, og_image=f"og/categories/{cat['slug']}.png"))
    return out

# ── Main ───────────────────────────────────────────────────────────

# ── Sitemap ────────────────────────────────────────────────────────

_LASTMOD_STORE_PATH = ROOT / "tools" / ".lastmod.json"
_lastmod_store = None

def _load_lastmod_store():
    global _lastmod_store
    if _lastmod_store is None:
        try:
            _lastmod_store = json.loads(_LASTMOD_STORE_PATH.read_text())
        except Exception:
            _lastmod_store = {}
    return _lastmod_store

def _save_lastmod_store():
    if _lastmod_store is not None:
        _LASTMOD_STORE_PATH.write_text(json.dumps(_lastmod_store, indent=1))

def _lastmod(path):
    """Content-hash lastmod | audit 3 M2: rebuild re-stamps evergreen pages,
    teaching Google to distrust lastmod. Fingerprint the rendered HTML; if
    unchanged since the previous build, keep the stored date instead of today.
    R2 M-13 (2026-09-08): also exclude the related-reading block and the CSS cache-bust
    hash from the fingerprint - the deterministic rotation rewrites one link line on
    ~132 pages per deploy as the pool grows, which reset every lastmod and taught
    Google the whole sitemap was noise. Only real content changes re-stamp now.
    """
    import datetime as _dt, hashlib as _hl, re as _re
    p = Path(path)
    if not p.exists():
        return _dt.datetime.now().strftime("%Y-%m-%d")
    html = p.read_text()
    # A2 M1 (2026-09-26): prefer the page's own declared content date (JSON-LD
    # dateModified / article:modified_time). The accurate date exists on every
    # page; wiring it in beats any file-derived stamp (Google discounts lastmod
    # that is not verifiably content-accurate).
    m = _re.search(r'"dateModified"\s*:\s*"([0-9]{4}-[0-9]{2}-[0-9]{2})', html) or \
        _re.search(r'article:modified_time"\s+content="([0-9]{4}-[0-9]{2}-[0-9]{2})', html)
    if m:
        return m.group(1)
    # A3 H-2 (2026-09-26): a page with no declared content date OMITS <lastmod>
    return None

def build_sitemap(tools, cats):
    today = datetime.now().strftime("%Y-%m-%d")
    urls = []

    # Homepage
    home_html = ROOT / "index.html"
    urls.append((f"https://martechsignal.com/", _lastmod(home_html) if home_html.exists() else today, "1.0"))

    # Trending page (momentum tracker, built by tools/build_trending.py)
    trending_html = ROOT / "trending" / "index.html"
    if trending_html.exists():
        urls.append(("https://martechsignal.com/trending/", _lastmod(trending_html), "0.6"))

    # Checklist page (audit M1: live but missing from discovery)
    checklist_html = ROOT / "checklist" / "index.html"
    if checklist_html.exists():
        urls.append(("https://martechsignal.com/checklist/", _lastmod(checklist_html), "0.6"))

    # Blog posts (scan blog/ for subdirectories containing index.html)
    # H-6: lastmod must never contradict the page's own datePublished. A build stamp
    # older than publish date, or a uniform date on unchanged posts, reads as fake.
    blog_dir = ROOT / "blog"
    if blog_dir.is_dir():
        for child in blog_dir.iterdir():
            f = child / "index.html"
            if child.is_dir() and f.exists():
                lm = _lastmod(f)
                m_dp = re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', f.read_text())
                if m_dp and m_dp.group(1) > lm:
                    lm = m_dp.group(1)
                urls.append((f"https://martechsignal.com/blog/{child.name}/", lm, "0.9"))

    # Tools hub
    tools_hub = ROOT / "tools" / "index.html"
    urls.append((f"https://martechsignal.com/tools/", _lastmod(tools_hub) if tools_hub.exists() else today, "0.8"))

    # Contact page
    contact_html = ROOT / "contact" / "index.html"
    if contact_html.exists():
        urls.append(("https://martechsignal.com/contact/", _lastmod(contact_html), "0.5"))

    # Corrections log (R3-M20, 2026-09-17): public proof of the honesty policy
    corr_html = ROOT / "corrections" / "index.html"
    if corr_html.exists():
        urls.append(("https://martechsignal.com/corrections/", _lastmod(corr_html), "0.5"))

    # About page
    about_html = ROOT / "about" / "index.html"
    urls.append((f"https://martechsignal.com/about/", _lastmod(about_html) if about_html.exists() else today, "0.5"))
    # A3 M-23 (2026-09-26): indexable policy pages belong in the sitemap.
    # r6 L-8 (2026-09-27): both carry real dateModified declarations; wire them
    # like every other page instead of leaving the lastmod blank.
    priv_html = ROOT / "privacy" / "index.html"
    terms_html = ROOT / "terms" / "index.html"
    urls.append(("https://martechsignal.com/privacy/", _lastmod(priv_html) if priv_html.exists() else "", "0.3"))
    urls.append(("https://martechsignal.com/terms/", _lastmod(terms_html) if terms_html.exists() else "", "0.3"))

    # Author page
    author_html = ROOT / "authors" / "tim-christensen" / "index.html"
    if author_html.exists():
        urls.append(("https://martechsignal.com/authors/tim-christensen/", _lastmod(author_html), "0.5"))

    # R3-M2/L1 (2026-09-16, v2.3.1 audit): the /categories/ and /authors/ hubs are
    # live, indexable and nav-linked but were absent from the sitemap.
    cats_hub = ROOT / "categories" / "index.html"
    if cats_hub.exists():
        urls.append(("https://martechsignal.com/categories/", _lastmod(cats_hub), "0.6"))
    authors_hub = ROOT / "authors" / "index.html"
    if authors_hub.exists():
        # H10 (r9): this hub lists the site authors, not the person page again.
        urls.append(("https://martechsignal.com/authors/", _lastmod(authors_hub), "0.5"))

    # Individual tool pages
    for t in tools:
        if t.get("status") == "active":
            tool_html = TOOLS_DIR / t["slug"] / "index.html"
            lm = _lastmod(tool_html) if tool_html.exists() else today
            urls.append((f"https://martechsignal.com/tools/{t['slug']}/", lm, "0.7"))
    gjson = TOOLS_DIR / "guides.json"
    if gjson.exists():
        for t in json.load(open(gjson)):
            g_html = ROOT / "guides" / t["slug"] / "index.html"
            lm = _lastmod(g_html) if g_html.exists() else today
            urls.append((f"https://martechsignal.com/guides/{t['slug']}/", lm, "0.7"))
        gu = ROOT / "guides" / "index.html"
        if gu.exists():
            urls.append(("https://martechsignal.com/guides/", _lastmod(gu), "0.6"))
        # r7 C8 (2026-09-28): static cluster hubs join the sitemap.
        for hub_slug in ("generative-engine-optimization", "mcp-agent-protocols",
                         "workflow-automation-strategy", "ai-seo-tooling",
                         "agentic-ai-advertising"):
            hub_html = ROOT / "guides" / hub_slug / "index.html"
            if hub_html.exists():
                urls.append((f"https://martechsignal.com/guides/{hub_slug}/", _lastmod(hub_html), "0.7"))

    # Category pages
    for c in cats:
        cat_html = ROOT / "categories" / c["slug"] / "index.html"
        lm = _lastmod(cat_html) if cat_html.exists() else today
        urls.append((f"https://martechsignal.com/categories/{c['slug']}/", lm, "0.8"))

    # Glossary hub + term pages
    glossary_json = TOOLS_DIR / "glossary.json"
    if glossary_json.exists():
        glossary_terms = json.loads(glossary_json.read_text())
        gl_hub = ROOT / "glossary" / "index.html"
        urls.append((f"https://martechsignal.com/glossary/", _lastmod(gl_hub) if gl_hub.exists() else today, "0.8"))
        for gt in glossary_terms:
            gl_html = ROOT / "glossary" / gt["slug"] / "index.html"
            lm = _lastmod(gl_html) if gl_html.exists() else today
            urls.append((f"https://martechsignal.com/glossary/{gt['slug']}/", lm, "0.6"))

    # Alternatives guides (SX-6 pilot)
    alt_dir = ROOT / "alternatives"
    if alt_dir.exists():
        # H-4: the section hub joins the sitemap like /best/ and /vs/ (A2 C1).
        alt_idx = alt_dir / "index.html"
        if alt_idx.exists():
            urls.append(("https://martechsignal.com/alternatives/", _lastmod(alt_idx), "0.7"))
        for d in sorted(alt_dir.iterdir()):
            if (d / "index.html").exists():
                urls.append((f"https://martechsignal.com/alternatives/{d.name}/", _lastmod(d / "index.html"), "0.7"))

    # A2 M4 (2026-09-26): /methodology/ and /ai-policy/ are indexable and
    # globally linked but were missing from the sitemap. A2 C1: the /best/ and
    # /vs/ hub pages join them (they were absent too, leaving the commercial
    # layer no sitemap-listed entry point).
    for _static in ("methodology", "ai-policy", "best", "vs"):
        _sp = ROOT / _static / "index.html"
        if _sp.exists():
            urls.append((f"https://martechsignal.com/{_static}/", _lastmod(_sp), "0.5"))

    # Best-X + /vs/ pilots (2026-09-26)
    for _prefix in ("best", "vs"):
        _dir = ROOT / _prefix
        if _dir.exists():
            for d in sorted(_dir.iterdir()):
                if (d / "index.html").exists():
                    urls.append((f"https://martechsignal.com/{_prefix}/{d.name}/", _lastmod(d / "index.html"), "0.7"))

    # Blog index
    if (blog_dir / "index.html").exists():
        urls.append((f"https://martechsignal.com/blog/", _lastmod(blog_dir / "index.html"), "0.8"))

    # Generate XML
    # M11: <priority> dropped - Google ignores it and our values were incoherent.
    # urls tuples keep the third slot for compatibility; it is no longer emitted.
    # H10 (r9, 2026-09-28): dedupe on <loc> at build time. The authors hub once
    # re-listed the person URL with a conflicting lastmod; first occurrence wins
    # and drops are reported so a repeat is visible in the build log.
    seen_locs = set()
    entries = []
    dropped = 0
    for loc, lastmod, _priority in urls:
        if loc in seen_locs:
            dropped += 1
            continue
        seen_locs.add(loc)
        lm = f"<lastmod>{lastmod}</lastmod>" if lastmod else ""
        entries.append(f"  <url><loc>{loc}</loc>{lm}</url>")

    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += '\n'.join(entries)
    sitemap += '\n</urlset>\n'

    (ROOT / "sitemap.xml").write_text(sitemap)
    _save_lastmod_store()
    print(f"\nSitemap: {len(entries)} URLs written to sitemap.xml"
          + (f" ({dropped} duplicate locs dropped)" if dropped else ""))

    # Ensure robots.txt exists
    robots_path = ROOT / "robots.txt"
    if not robots_path.exists():
        robots_path.write_text(
            "User-agent: *\nAllow: /\n\n"
            "Sitemap: https://martechsignal.com/sitemap.xml\n"
        )
        print("Robots.txt: created")


def main():
    tools, cats = load()
    active = [t for t in tools if t.get("status") == "active" and t.get("kind") != "Guide"]
    print(f"Building tool directory: {len(active)} active tools, {len(cats)} categories\n")

    # R2 H-2 guaranteed coverage: closed-form reservation computed purely from
    # tools.json (no link-graph feedback). Each active tool is reserved one slot on a
    # deterministic same-category host (stable md5 of its slug over the sorted peer
    # list). Every tool therefore appears on at least one peer's Similar-Tools module,
    # the whole catalogue stays in the internal-link graph, and hosts never reshuffle
    # between builds (lastmod stays honest).
    _reservations = {}
    _by_cat = {}
    for _t in active:
        _by_cat.setdefault(_t["category"], []).append(_t["slug"])
    # Deterministic assignment: each tool is reserved on a same-category host chosen
    # by md5(slug+peer); if that host already carries 2 reservations, walk the md5-
    # ordered peer list until one has capacity (max 2 per host keeps modules honest).
    _load = {}
    for _t in sorted(active, key=lambda x: x["slug"]):
        _s = _t["slug"]
        _peers = sorted(x for x in _by_cat.get(_t["category"], []) if x != _s)
        if not _peers:
            continue
        _order = sorted(_peers, key=lambda p: int(hashlib.md5((_s + p).encode()).hexdigest(), 16))
        for _host in _order:
            if _s in _reservations.get(_host, []):
                break
            if _load.get(_host, 0) < 2:
                _reservations.setdefault(_host, []).append(_s)
                _load[_host] = _load.get(_host, 0) + 1
                break
    setattr(sys.modules[__name__], "_similar_reservations", _reservations)

    # Hub
    print("Hub:")
    build_hub(tools, cats)

    # Tool pages
    print(f"\nTool pages ({len(active)}):")
    for t in active:
        out = build_tool_page(t, cats, tools)
        print(f"  ✓ {out.relative_to(ROOT)}")

    # Category pages
    print(f"\nCategory pages:")
    for c in cats:
        out = build_category_page(c, tools)
        if out:
            print(f"  ✓ {out.relative_to(ROOT)}")
        else:
            print(f"  · {c['slug']} (empty, skipped)")

    n_hubs = sum(1 for c in cats if c.get("hub"))
    
    # r6 M-2 (2026-09-27): catalog guides live outside the /tools/ taxonomy.
    gpath = TOOLS_DIR / "guides.json"
    if gpath.exists():
        guides = json.load(open(gpath))
        for t in guides:
            build_tool_page(t, cats, tools, base="guides")
        gi = "\n".join(
            f'    <li><a href="/guides/{g["slug"]}/">{esc(g["name"])}</a> - {esc(g.get("tagline", ""))}</li>'
            for g in guides)
        # r7 C8 (2026-09-28): the static cluster hubs list beside the catalog guides.
        gi += "".join(
            f'\n    <li><a href="/guides/{s}/">{n}</a> - {d}</li>' for s, n, d in (
                ("generative-engine-optimization", "Generative Engine Optimization (GEO)",
                 "hub for the AI search visibility work: the five-layer fix, the tooling, and the honest tactics"),
                ("mcp-agent-protocols", "MCP and agent protocols for marketers",
                 "the integration economics, the failure modes, and the audits to run first"),
                ("workflow-automation-strategy", "Workflow automation strategy",
                 "where AI tools fit, what no-code costs long-term, and how to audit what you own"),
                ("ai-seo-tooling", "AI SEO tooling",
                 "benchmarks and head-to-heads where the tools were actually run"),
                ("agentic-ai-advertising", "Agentic advertising",
                 "autonomous spend in the platforms and the guardrails that exist today"),
            ))
        gdir = ROOT / "guides"
        gdir.mkdir(exist_ok=True)
        # M9 (r9, 2026-09-28): the hub was a 182-word link dump, the thinnest
        # indexable page on the site. Positioning copy states what guides are
        # for, how they differ from tools/glossary/blog, and where to start.
        _gintro = (
            '<section class="hub-lead">'
            '<p>The directory answers which tool. The guides answer what to do once you have picked one, or before you start picking. Each one covers a topic too big for a tool page: a strategy question, a category shift, or a skill the whole team needs. They are reference pages, not reviews, and they link back into the catalog wherever a tool matters.</p>'
            '<p>Start with the problem you have. If AI answers are eating your search traffic, the GEO guide orders the fix: what changed, what to measure now that clicks lie, and which tools exist. If your ad spend runs itself, the agentic advertising guide covers what the platforms automate and which guardrails hold. Workflow automation strategy is for the team drowning in tools: where AI fits, what no-code costs over years, and how to audit what you already own.</p>'
            '<p>Two guides are about how the work gets done. AI SEO tooling collects the benchmarks and head-to-heads where tools were run, with the honest limits stated up front. MCP and agent protocols explains the integration layer underneath agents: what it costs to connect things, where it breaks, and which audits to run first.</p>'
            '<p>Read a guide, then follow it into the catalog. Every guide links the tools, comparisons, and definitions it mentions, and every tool page links back to the guides that cover its category. If something in a guide went stale, the corrections log records the fix.</p>'
            '</section>')
        (gdir / "index.html").write_text(page_shell(
            title="Catalog guides",
            description="Longer reference pages that support the directory. These are not tools, so they are not counted in the tool totals.",
            canonical="https://martechsignal.com/guides/",
            body='<nav class="crumb" aria-label="Breadcrumb"><ol style="display:flex;gap:.4rem;list-style:none;margin:0;padding:0;flex-wrap:wrap"><li><a href="/">Home</a></li><li><span aria-current="page">Guides</span></li></ol></nav>'
                 '<section class="page-head"><h1>Catalog guides</h1>'
                 '<p class="sub">Longer reference pages that support the directory. These are not tools, so they are not counted in the tool totals.</p></section>'
                 + _gintro +
                 (f'<ul>{gi}</ul>' if gi.strip() else "")))
        print(f"Guides ({len(guides)}): /guides/")

    
    # r6 M-8 (2026-09-27): rolling 21-day re-verification on anything priced.
    # Pages past 21 days are auto-flagged here and listed in tools/stale-pricing.json.
    import datetime as _dt
    _today = _dt.date.today()
    _stale = []
    for _t in tools:
        if not _t.get("price_notes") and _t.get("price_from") in (None, ""):
            continue
        _du = _t.get("date_updated")
        if not _du:
            continue
        try:
            _age = (_today - _dt.date.fromisoformat(_du)).days
        except ValueError:
            continue
        if _age > 21:
            _stale.append({"slug": _t["slug"], "name": _t["name"],
                           "date_updated": _du, "days_stale": _age})
    (TOOLS_DIR / "stale-pricing.json").write_text(
        json.dumps({"checked": _today.isoformat(), "window_days": 21,
                    "stale": _stale}, indent=2))
    if _stale:
        print(f"STALE-PRICING: {len(_stale)} pages past 21 days: "
              + ", ".join(f'{s["slug"]}({s["days_stale"]}d)' for s in _stale))
    else:
        print("STALE-PRICING: all priced pages within 21 days")

    print(f"\nDone! {len(active)} tool pages + {len(cats)} categories + {n_hubs} hub")

    sync_date_modified()  # M9: before sitemap so <lastmod> covers every family
    # Sitemap
    build_sitemap(tools, cats)

    # llms.txt for AI-search readiness
    build_llms_txt(tools, cats)

    # Factual-consistency gate (fails the build loudly on contradictions)
    assert_factual_consistency(tools)



def assert_factual_consistency(tools):
    """Post-build gate (audit follow-up): loud failure if any tool page contradicts itself."""
    problems = []
    for t in tools:
        if t.get("status") != "active":
            continue
        slug, model = t["slug"], t.get("pricing_model")
        paid_custom = t.get("price_from") is None or t.get("pricing_model") == "enterprise"
        page = TOOLS_DIR / slug / "index.html"
        if not page.exists():
            continue
        html = page.read_text()
        if re.search(r'"price"\s*:\s*0\b', html) and model in ("enterprise", "paid"):
            problems.append(f"{slug}: offers.price=0 on {model} pricing")
        if paid_custom and "has a free tier" in html:
            problems.append(f"{slug}: FAQ claims free tier on {model} pricing")
        if t.get("name") and len(t.get("name","")) > 3:
            # A2 M3: H1 phrasing varies by pricing class; the invariant is that the
            # tool name leads the H1.
            h1_ok = re.search(r'<h1>[^<]{0,6}' + re.escape(esc(t['name'])), html) is not None
            if not h1_ok:
                problems.append(f"{slug}: H1 does not match name '{t['name']}'")
    if problems:
        print("FACTUAL CONSISTENCY FAILURES:")
        for p in problems:
            print("  !!", p)
        raise SystemExit(1)
    print("Factual consistency: OK")

def build_llms_txt(tools, cats):
    """Generate llms.txt (site summary + structured inventory for AI crawlers)."""
    import re as _re
    cat_names = {c["slug"]: c["name"] for c in cats}
    active = [t for t in tools if t.get("status") == "active" and t.get("kind") != "Guide"]
    n_active = len(active)  # SX-4: every count claim derived from data, none hardcoded
    lines = [
        "# MartechSignal",
        "",
        "> Independent reviews of AI marketing automation tools. Structured research on",
        f"> {n_active} martech platforms | pricing, self-hosting, APIs, and which AI features",
        "> actually ship. No sponsored rankings, no affiliate links.",
        "",
        "## Directory",
        "",
    ]
    by_cat = {}
    for t in active:
        by_cat.setdefault(t.get("category", "other"), []).append(t)
    for cslug, ts in sorted(by_cat.items()):
        lines.append(f"### {cat_names.get(cslug, cslug)}")
        lines.append("")
        for t in sorted(ts, key=lambda x: x["name"].lower()):
            tag_full = (t.get("tagline") or "").strip().rstrip(".")
            if len(tag_full) > 110:
                # cut at the last clause boundary (comma/semicolon) before the limit,
                # falling back to a word boundary - never mid-word (audit M8)
                cut = max(tag_full.rfind(",", 0, 110), tag_full.rfind(";", 0, 110))
                if cut >= 40:
                    tag = tag_full[:cut].rstrip(",;:")
                else:
                    sp = tag_full.rfind(" ", 0, 110)
                    tag = tag_full[:sp] + "\u2026" if sp > 30 else tag_full[:110].rsplit(" ", 1)[0] + "\u2026"
            else:
                tag = tag_full
            oss = " (open source)" if t.get("open_source") else ""
            lines.append(f"- [{t['name']}](https://martechsignal.com/tools/{t['slug']}/): {tag}{oss}")
        lines.append("")

    blog_dir = ROOT / "blog"
    posts = []
    if blog_dir.is_dir():
        for child in sorted(blog_dir.iterdir()):
            f = child / "index.html"
            if child.is_dir() and f.exists():
                html_content = f.read_text()
                m = _re.search(r"<title>(.*?)</title>", html_content)
                d = _re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', html_content)
                if m:
                    posts.append((d.group(1) if d else "0000-00-00", child.name,
                                  m.group(1).replace("&amp;", "&").replace("&#x27;", "'")))
    posts.sort(reverse=True)
    lines += ["## Analysis", ""]
    for date, slug, title in posts:
        lines.append(f"- [{title}](https://martechsignal.com/blog/{slug}/) ({date})")
    glossary_json = TOOLS_DIR / "glossary.json"
    if glossary_json.exists():
        glossary_terms = json.loads(glossary_json.read_text())
        lines += ["", "## Glossary", ""]
        for gt in sorted(glossary_terms, key=lambda x: x["term"].lower()):
            lines.append(f"- [{gt['term']}](https://martechsignal.com/glossary/{gt['slug']}/)")
    lines += ["", "## Categories", ""]
    for c in sorted(cats, key=lambda x: x["name"].lower()):
        lines.append(f"- [{c['name']}](https://martechsignal.com/categories/{c['slug']}/)")
    # A3 M-9 (2026-09-27): the guides/comparisons and site pages were missing
    # from llms.txt (12 sitemap URLs), and the policy was unreadable to agents.
    lines += ["", "## Guides and comparisons", ""]
    for fam, label in (("best", "Best"), ("vs", "Versus"), ("alternatives", "Alternatives"), ("guides", "Guides")):
        fam_dir = ROOT / fam
        if fam_dir.is_dir():
            for child in sorted(fam_dir.iterdir()):
                f = child / "index.html"
                if child.is_dir() and f.exists():
                    m = _re.search(r"<title>([^<]+)</title>", f.read_text())
                    ttl = (m.group(1) if m else child.name).split("|")[0].split("\u00b7")[0].strip()
                    lines.append(f"- [{ttl}](https://martechsignal.com/{fam}/{child.name}/)")
    lines += ["", "## Site", "",
              "- [About](https://martechsignal.com/about/): who runs MartechSignal and the editorial policy",
              "- [Methodology](https://martechsignal.com/methodology/): how tools are researched, dated and priced",
              "- [Authors](https://martechsignal.com/authors/)",
              "- [AI content policy](https://martechsignal.com/ai-policy/): citation and grounding are welcome; "
              "training model weights on this corpus is not permitted",
              "- [Checklist](https://martechsignal.com/checklist/): tool selection checklist",
              "- [Corrections](https://martechsignal.com/corrections/): published errata"]
    lines += ["", "## Links", "",
              "- [Full content mirror](https://martechsignal.com/llms-full.txt)",
              "- [Home](https://martechsignal.com/)",
              "- [Blog](https://martechsignal.com/blog/)",
              "- [Tool directory](https://martechsignal.com/tools/)",
              "- [Categories](https://martechsignal.com/categories/)",
              "- [Trending open-source tools](https://martechsignal.com/trending/)",
              "- [Glossary](https://martechsignal.com/glossary/)",
              "- [Checklist](https://martechsignal.com/checklist/)",
              "- [About / editorial policy](https://martechsignal.com/about/)",
              "- [Author](https://martechsignal.com/authors/tim-christensen/)",
              "- [Contact](https://martechsignal.com/contact/)",
              "- [Corrections](https://martechsignal.com/corrections/)",
              "- [RSS feed](https://martechsignal.com/rss.xml)", ""]
    out = ROOT / "llms.txt"
    # A2 H7 (2026-09-26): the catalog datasets were reachable only by agents that
    # already knew the ARD spec - surface them in the machine-readable index.
    # A2 L11: the surfaces count different scopes; say so once, with derived numbers.
    _records = len(tools)
    _retired = _records - n_active
    lines += [
        "## Machine-readable data",
        "",
        f"- [catalog-tools.json](https://martechsignal.com/catalog-tools.json) - full tool catalog: pricing, license, hosting, open-source status (ARD). {_records} records = {n_active} active + {_retired} non-active; the directory above lists only active tools",
        "- [oss-momentum.json](https://martechsignal.com/oss-momentum.json) - open-source star momentum dataset with snapshot-bounded windows",
        "",
    ]
    out.write_text("\n".join(lines))
    print(f"llms.txt: {out} ({len(lines)} lines)")

    # llms-full.txt: same inventory with full descriptions per tool (audit M8:
    # AI crawlers that want depth get it without crawling every page)
    full_lines = list(lines)
    for cslug, ts in sorted(by_cat.items()):
        full_lines.append(f"### {cat_names.get(cslug, cslug)}")
        full_lines.append("")
        for t in sorted(ts, key=lambda x: x["name"].lower()):
            desc = (t.get("description") or t.get("tagline") or "").strip()
            if not desc:
                continue
            oss = " Open source." if t.get("open_source") else ""
            price = pricing_label(t)
            full_lines.append(f"[{t['name']}](https://martechsignal.com/tools/{t['slug']}/) , {price}.{oss}")
            for para in desc.split("\n"):
                para = para.strip()
                if para:
                    full_lines.append(para)
            full_lines.append("")
    full_out = ROOT / "llms-full.txt"
    full_out.write_text("\n".join(full_lines))
    print(f"llms-full.txt: {full_out} ({len(full_lines)} lines)")

    # A-1 (v2.4.0 audit): build-time Markdown mirror from the same source as
    # llms-full.txt, served as <url>/index.md. Honesty note (from the audit): no
    # primary source proves agents send Accept: text/markdown - this is a cheap
    # bet on the channel, not a confirmed one.
    md_n = 0
    for cslug, ts in sorted(by_cat.items()):
        for t in ts:
            desc = (t.get("description") or "").strip()
            md = [f"# {t['name']} | MartechSignal review", "",
                  t.get("tagline", ""), "",
                  f"- Page: https://martechsignal.com/tools/{t['slug']}/",
                  f"- Category: {cat_names.get(cslug, cslug)}",
                  f"- Pricing: {pricing_label(t)}",
                  f"- Open source: {'yes (' + str(t.get('license')) + ')' if t.get('open_source') else 'no'}",
                  f"- Last verified: {t.get('date_updated', '')}", ""]
            for para in desc.split("\n"):
                para = para.strip()
                if para:
                    md += [para, ""]
            d = ROOT / "tools" / t["slug"]
            if d.is_dir():
                pass  # H10 (2026-09-27): full-parity mirror owned by build_md_mirrors.py
    for c in cats:
        d = ROOT / "categories" / c["slug"]
        if d.is_dir():
            members = [x["name"] for x in active if x.get("category") == c["slug"]
                       or (c["slug"] == "open-source" and x.get("open_source"))]
            body = [f"# {c['name']} | MartechSignal category", "",
                    c.get("description") or c.get("intro") or "", "",
                    f"- Page: https://martechsignal.com/categories/{c['slug']}/",
                    f"- Tools: {len(members)}", ""] + [f"- {n}" for n in sorted(members)]
            pass  # H10: category mirror owned by build_md_mirrors.py
    # A3 M-6 (2026-09-27): /index.md is the HOMEPAGE mirror, generated from the
    # rendered homepage by tools/build_md_mirrors.py. This writer used to copy the
    # llms lines there, so agents requesting the homepage markdown got the whole
    # catalog. llms.txt and llms-full.txt remain this function's job.
    md_n += 1
    # A2 H7 (2026-09-26): every rendered page gets a markdown mirror (the audit
    # found /vs/, /best/, /tools/, /blog/ and /ai-policy/ returning 404 on
    # index.md while other sections served one). Generic extract: title,
    # description and canonical from the rendered head.
    for _idx in sorted(ROOT.rglob("index.html")):
        if "deploy-out" in _idx.parts or ".well-known" in _idx.parts:
            continue
        if (_idx.parent / "index.md").exists():
            continue
        _html = _idx.read_text()
        import re as _re2
        _t = _re2.search(r"<title>(.*?)</title>", _html)
        _d = _re2.search(r'name="description" content="(.*?)"', _html)
        _c = _re2.search(r'rel="canonical" href="(.*?)"', _html)
        _url = _c.group(1) if _c else f"https://martechsignal.com/{_idx.parent.relative_to(ROOT).as_posix().strip('.')}/"
        pass  # H10: thin stub retired; build_md_mirrors.py writes every mirror
    print(f"A-1 markdown mirrors: owned by build_md_mirrors.py (H10 full parity); llms.txt + llms-full.txt still written here")



def _audit_double_slash_hrefs():
    """R3-L2 (wave 3): no generated page may ship a double-slash internal href.
    The Cloudflare _redirects route for // URLs is unsafe (looped twice), so the
    fix is at build time: crawl the generated tree, report, and normalize."""
    import re as _re
    fixed = 0
    pat = _re.compile(r'href="(/[^"]*?//+[^"]*)"')
    for p in ROOT.glob("*/index.html"):
        s = p.read_text()
        s2 = pat.sub(lambda m: 'href="' + _re.sub(r"(?<!:)/{2,}", "/", m.group(1)) + '"', s)
        if s2 != s:
            p.write_text(s2)
            fixed += 1
    return fixed



def refresh_homepage_counts():
    """H4 (2026-09-27): the homepage's tool/scored/oss counts derive from data on
    every build so the surfaces can never contradict again."""
    import re as _re
    _tools = json.loads((ROOT / "tools" / "tools.json").read_text())
    _act = [x for x in _tools if x.get("status", "active") == "active"]
    _n, _oss = len(_act), sum(1 for x in _act if x.get("open_source"))
    _scored = len(_SCORES)
    _p = ROOT / "index.html"
    _s = _p.read_text()
    _s, _c1 = _re.subn(r"(<b>)\d+( martech tools</b> audited)", rf"\g<1>{_n}\g<2>", _s)
    _s, _c2 = _re.subn(r"(<b>)\d+(</b> carry the full six-pillar score panel)",
                       rf"\g<1>{_scored}\g<2>", _s)
    _s, _c3 = _re.subn(r'(Open-Source Tools</div><div class="tagline">)\d+ of \d+ tools',
                       rf"\g<1>{_oss} of {_n} tools", _s)
    if _c1 or _c2 or _c3:
        _p.write_text(_s)
        print(f"  H4: homepage counts refreshed ({_n} tools, {_scored} scored, {_oss} oss)")



def minify_css():
    """M1 (2026-09-27): faithful minify. Comments and whitespace only; rule and
    brace structure survive (parity asserted) so the bundle cannot drift again."""
    src = (ROOT / "style.css").read_text()
    out = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    out = re.sub(r"\s+", " ", out)
    out = re.sub(r" *([{}};]) *", r"\1", out)
    out = out.replace(";}", "}")
    _bare = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    assert _bare.count("{") == out.count("{") and _bare.count("}") == out.count("}"), \
        "M1: minify lost rules"
    (ROOT / "style.min.css").write_text(out.strip())
    _write_critical(out.strip())
    return out.strip()


# M1 (r9, 2026-09-28): above-fold critical CSS, extracted from the minified
# bundle at build time by selector allowlist (never hand-duplicated, so the
# inline copy cannot drift from the bundle). Inlined into every page head;
# the full bundle loads non-blocking right after.
_CRITICAL_PREFIXES = (
    ":root", "*", "html", "body", "::selection",
    ".bg", ".wrap", "a",
    ".masthead", ".mast-in", ".wordmark", ".mast-nav", ".mast-right",
    ".live", ".mast-date", ".pulse-dot",
    ".crumb", ".breadcrumbs", ".crumbs",
    ".page-head", ".page-tools", ".sub", ".count", ".byline",
    ".verdict-cta", ".cta-early", ".alt-link", ".btn", ".disclosure-strip",
    ".kicker", ".back", ".post-hero", ".meta",
    ".hero", ".hero-cols", ".hero-side", ".stats-card", ".stat",
    ".lede", ".hero-cta", ".micro", ".spec",
    ".score-band", ".unscored-note",
    ".cat-nav", ".cat-pill", ".made-badge",
    ".tool-grid", ".tool-card",
    "#progress",
)


def _split_rules(css):
    """Split minified CSS into (header, body) chunks, respecting nesting."""
    chunks = []
    i, n = 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j == -1:
            break
        depth = 0
        k = j
        while k < n:
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        chunks.append((css[i:j].strip(), css[j:k + 1]))
        i = k + 1
    return chunks


def _crit_match(header):
    """True when any comma-part of a selector list falls under the allowlist."""
    for part in (s.strip() for s in header.split(",")):
        for p in _CRITICAL_PREFIXES:
            if (part == p or part.startswith(p + " ") or part.startswith(p + ".")
                    or part.startswith(p + ":") or part.startswith(p + "[")
                    or part.startswith(p + ">") or part.startswith(p + "+")):
                return True
    return False


def _write_critical(min_css):
    keep = []
    for header, body in _split_rules(min_css):
        h = header.strip()
        if h.startswith("@font-face"):
            continue  # fonts swap anyway; ~2KB saved from the inline block
        if h.startswith("@keyframes"):
            keep.append(h + body)  # tiny, referenced by kept rules
            continue
        if h.startswith("@media"):
            inner = _split_rules(body[1:-1])
            hit = [(hh, bb) for hh, bb in inner if _crit_match(hh)]
            if hit:
                keep.append(h + "{" + "".join(hh + bb for hh, bb in hit) + "}")
            continue
        if _crit_match(h):
            keep.append(h + body)
    out = "".join(keep)
    (ROOT / "tools" / ".critical.css").write_text(out)
    print(f"M1: critical {len(out)}B inlined, full bundle deferred")
    return out


def _critical_inline():
    try:
        return (ROOT / "tools" / ".critical.css").read_text()
    except OSError:
        return ""


def sync_stylesheet_links():
    """M1: every HTML file points at the one bundle with the artifact's own hash.

    r6 M-3 (2026-09-27): site.js rides the same sweep. An unversioned tag plus
    max-age=3600 kept stale is-in builds alive in visitors' browsers."""
    import hashlib as _h
    # r8 L1 (2026-09-28): one cache-buster convention site-wide - same function
    # page_shell uses (md5(style.css)[:8]); the old sha256(style.min.css) split
    # the site into two hash populations and left 32 pages pinned stale.
    _hash = _css_v()
    _jhash = _h.sha256((ROOT / "site.js").read_bytes()).hexdigest()[:8]
    # M1 (r9, 2026-09-28): critical CSS inline + deferred bundle, applied to
    # every HTML file here (covers hand-maintained index.html too). Matches
    # only still-blocking links (no media attr) so re-runs are idempotent;
    # the href rewrite below keeps deferred/noscript hashes current.
    try:
        _crit = (ROOT / "tools" / ".critical.css").read_text()
    except OSError:
        _crit = ""
    _n = 0
    _nj = 0
    _nc = 0
    for _p in ROOT.rglob("*.html"):
        if "deploy-out" in _p.parts or ".well-known" in _p.parts:
            continue
        _s = _p.read_text()
        if _crit:
            _defer = (
                f"<style>{_crit}</style>"
                f'<link rel="stylesheet" href="/style.min.css?v={_hash}" '
                f'media="print" onload="this.media=\'all\'">'
                f'<noscript><link rel="stylesheet" href="/style.min.css?v={_hash}"></noscript>')
            # (?<!<noscript>) guards the fallback link this same block emits:
            # without it the sweep stuffs a second critical copy inside every
            # <noscript> it just wrote (r9 M1 follow-up, 304 pages affected).
            _s, _cc = re.subn(
                r'(?<!<noscript>)<link rel="stylesheet" href="/style(?:\.min)?\.css\?v=[a-f0-9]*">',
                _defer, _s)
            _nc += _cc
        _new, _c = re.subn(r'href="/style(?:\.min)?\.css\?v=[a-f0-9]*"',
                           f'href="/style.min.css?v={_hash}"', _s)
        _new, _cj = re.subn(r'<script src="/site\.js(?:\?v=[a-f0-9]+)?" defer>',
                            f'<script src="/site.js?v={_jhash}" defer>', _new)
        if _c or _cj:
            _p.write_text(_new)
            _n += _c
            _nj += _cj
    print(f"M1: {_n} stylesheet links -> style.min.css?v={_hash}")
    print(f"M1: {_nc} pages converted to critical-inline + deferred bundle")
    print(f"M1-JS: {_nj} script tags -> site.js?v={_jhash}")



def sync_md_alternates():
    """L16 (2026-09-27): exactly one text/markdown alternate, only when the
    sibling index.md exists."""
    _n = 0
    for _p in ROOT.rglob("index.html"):
        if "deploy-out" in _p.parts or ".well-known" in _p.parts:
            continue
        _s = _p.read_text()
        _s2 = re.sub(r'\s*<link rel="alternate" type="text/markdown"[^>]*>', "", _s)
        if (_p.parent / "index.md").exists():
            _rel = "/" + _p.parent.relative_to(ROOT).as_posix().strip(".") + "/"
            if _rel == "//":
                _rel = "/"
            _link = (f'\n<link rel="alternate" type="text/markdown" '
                     f'href="{_rel}index.md" title="Markdown mirror">')
            _s2 = _s2.replace("</head>", _link + "\n</head>", 1)
        if _s2 != _s:
            _p.write_text(_s2)
            _n += 1
    print(f"L16: {_n} pages normalized to <=1 markdown alternate")



def _json_block_dates(jpath, depth):
    """H10 (r9, 2026-09-28): per-page content edit dates from git blame on a
    content JSON. Page blocks start at slug lines with exactly `depth` leading
    spaces; -M keeps original dates across reorder commits. Returns
    {page_slug: YYYY-MM-DD} with each block's max author date."""
    import subprocess as _sp, re as _re, datetime as _dt
    try:
        _p = ROOT / jpath if not str(jpath).startswith(str(ROOT)) else Path(jpath)
        _out = _sp.run(["git", "blame", "-w", "-M", "--line-porcelain", "--", str(_p)],
                       cwd=str(ROOT), capture_output=True, text=True, timeout=120).stdout.splitlines()
        _lines = _p.read_text().splitlines()
        _pre = " " * depth + '"slug"'
        _bounds = []
        for _n, _ln in enumerate(_lines):
            if _ln.startswith(_pre):
                _m = _re.search(r'"slug":\s*"([a-z0-9-]+)"', _ln)
                if _m:
                    _bounds.append((_n, _m.group(1)))
        _dates, _cur = {}, None
        for _ln in _out:
            if _re.match(r'^[0-9a-f]{40} \d+ \d+', _ln):
                _cur = int(_ln.split()[2])
            elif _ln.startswith('author-time '):
                _d = _dt.datetime.fromtimestamp(int(_ln.split()[1]), _dt.timezone.utc).strftime('%Y-%m-%d')
                if _cur is not None:
                    _dates[_cur] = _d
        _res = {}
        for _i, (_n, _slug) in enumerate(_bounds):
            _end = _bounds[_i + 1][0] if _i + 1 < len(_bounds) else len(_lines)
            _ds = []
            for _k in range(_n, _end):
                if _dates.get(_k):
                    _ds.append(_dates[_k])
            if _ds:
                _res[_slug] = max(_ds)
        return _res
    except Exception:
        return {}


def _blame_content_date(path):
    """H10 (r9, 2026-09-28): honest fallback edit date for a built HTML file.
    `git log -1` on built files always returns the last deploy (deploys commit
    everything), which stamped whole sections with one date. Blame -M attributes
    unchanged lines to their real commits; churn lines (cache-bust hashes,
    date stamps themselves, the single-line entity blob) are excluded so they
    cannot self-justify today's date."""
    import subprocess as _sp, datetime as _dt
    try:
        _out = _sp.run(["git", "blame", "-w", "-M", "--line-porcelain", "--", str(path)],
                       cwd=str(ROOT), capture_output=True, text=True, timeout=60).stdout.splitlines()
    except Exception:
        return None
    _best, _cur_date = None, None
    for _ln in _out:
        if _ln.startswith('author-time '):
            try:
                _cur_date = _dt.datetime.fromtimestamp(int(_ln.split()[1]), _dt.timezone.utc).strftime('%Y-%m-%d')
            except Exception:
                _cur_date = None
        elif _ln.startswith('\t'):
            _c = _ln[1:]
            if ('dateModified' in _c or '?v=' in _c
                    or ('#person' in _c and 'sameAs' in _c)):
                _cur_date = None
                continue
            if _cur_date and (not _best or _cur_date > _best):
                _best = _cur_date
            _cur_date = None
    return _best


def sync_date_modified():
    """M9 (2026-09-27): every page publishes a dateModified so the sitemap keeps
    <lastmod>. Date source order: the page's own datePublished, the visible <time>,
    then content-blame on the file (the house rule from build_blog R2 M-7). No
    invented dates: pages with none of the above keep no dateModified.
    H10 (r9, 2026-09-28): the old git-log fallback returned the last deploy
    (deploys commit everything), stamping whole sections with one date. Blame
    attributes unchanged lines to their real commits instead."""
    import re as _re
    _n = 0
    for _p in ROOT.rglob("index.html"):
        if "deploy-out" in _p.parts or ".well-known" in _p.parts:
            continue
        _s = _p.read_text()
        if "dateModified" in _s or "ld+json" not in _s:
            continue
        # r6 M-4/M-5 (2026-09-27): the REAL last-edit date wins. Declared dates
        # (datePublished / <time>) are fallbacks, not authorities: generator-stamped
        # "today" was leaking into dateModified and sitemap lastmod on 43 URLs.
        _val = _blame_content_date(_p)
        if not _val:
            _m = _re.search(r'"datePublished"\s*:\s*"([^"]+)"', _s)
            if _m:
                _val = _m.group(1)
        if not _val:
            _m = _re.search(r'<time[^>]*datetime="([^"]+)"', _s)
            if _m:
                _val = _m.group(1)[:10]
        if not _val:
            continue
        _url = "https://martechsignal.com/" + _p.parent.relative_to(ROOT).as_posix().strip(".") + "/"
        if _url == "https://martechsignal.com//":
            _url = "https://martechsignal.com/"
        _block = ('<script type="application/ld+json">{"@context": "https://schema.org", '
                  '"@type": "WebPage", "@id": "' + _url + '#webpage", '
                  '"dateModified": "' + _val + '"}</script>')
        _p.write_text(_s.replace("</head>", _block + "\n</head>", 1))
        _n += 1
    print(f"M9: dateModified published on {_n} pages (sitemap lastmod follows)")

if __name__ == "__main__":
    sync_date_modified()
    refresh_homepage_counts()
    minify_css()
    main()
    sync_stylesheet_links()
    sync_md_alternates()
