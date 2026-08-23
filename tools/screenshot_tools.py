#!/usr/bin/env python3
"""Capture dated homepage screenshots of top tools for martechsignal.com (media plan #3).

Usage:
  /home/hermes/.hermes/home/.claude/skills/seo/.venv/bin/python tools/screenshot_tools.py [--limit 5] [--slugs zapier klaviyo]

Outputs: og/screenshots/<slug>-<YYYY-MM>.png  (1280x800 viewport, full page crop 1200x630)
Skips vendor bot-blocks gracefully and logs them; NEVER fabricates a capture.
"""
import argparse, json, sys, time
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og" / "screenshots"
OUT.mkdir(parents=True, exist_ok=True)

SLUGS = ["zapier", "klaviyo", "mailchimp", "braze", "intercom", "drift",
         "hubspot-marketing-hub", "salesforce-marketing-cloud", "surfer-seo",
         "tealium", "n8n", "make", "activecampaign", "hubspot-crm", "segment",
         "mautic", "cordys-crm", "attio", "clearscope", "frase"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--slugs", nargs="*", default=None)
    args = ap.parse_args()

    tools = json.loads((ROOT / "tools" / "tools.json").read_text())
    by_slug = {t["slug"]: t for t in tools if t.get("status") == "active"}
    slugs = args.slugs or SLUGS[: args.limit]

    from playwright.sync_api import sync_playwright
    stamp = datetime.now().strftime("%Y-%m")
    ok, skipped, failed = [], [], []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        ctx = browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36 MartechSignalBot/1.0",
        )
        page = ctx.new_page()
        for slug in slugs:
            t = by_slug.get(slug)
            if not t:
                skipped.append((slug, "not in tools.json"))
                continue
            site = t.get("website") or ""
            if not site.startswith("http"):
                skipped.append((slug, "no website"))
                continue
            out = OUT / f"{slug}-{stamp}.png"
            if out.exists():
                ok.append((slug, "cached"))
                continue
            try:
                page.goto(site, timeout=25000, wait_until="domcontentloaded")
                page.wait_for_timeout(2500)
                page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1280, "height": 800})
                ok.append((slug, str(out)))
                print(f"  ✓ {slug}: {site} -> {out.name}")
            except Exception as e:
                msg = str(e)[:80]
                print(f"  ✗ {slug}: {msg}")
                failed.append((slug, msg))
            time.sleep(0.8)
        browser.close()

    print(f"\nresult: {len(ok)} ok, {len(skipped)} skipped, {len(failed)} failed")
    if failed:
        print("failed (bot-blocked or error):")
        for s, m in failed:
            print(f"  - {s}: {m}")


if __name__ == "__main__":
    main()