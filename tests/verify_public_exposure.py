#!/usr/bin/env python3
"""Assert that nothing private is publicly reachable on martechsignal.com.

The boundary is tools/stage_deploy.py: it stages the public subset into
deploy-out/ and deploy.sh uploads that. This test takes the files it EXCLUDED and
proves none of them can be fetched, then proves the files it REQUIRED still can.

Two subtleties, both learned the hard way on 2026-09-13:
  * .gitignore and .assetsignore are NOT honoured by `wrangler pages deploy`,
    so the upload directory is the only boundary that works.
  * a path that was cached before a deploy keeps being served from the edge
    cache, so every private check is done with a cache-busting query string and
    against the deployment hostname. A plain request can lie to you.

Usage:
    python3 tests/verify_public_exposure.py                  # production alias
    python3 tests/verify_public_exposure.py --deployment https://<hash>.martechsignal.pages.dev
Exit code 0 = all clear, 1 = something private is reachable or a page is broken.
"""
from __future__ import annotations

import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://martechsignal.com"
PUBLIC_PAGES = [
    "/", "/404.html", "/style.css", "/sitemap.xml", "/robots.txt", "/rss.xml",
    "/llms.txt", "/tools/", "/tools/nocobase/", "/blog/", "/blog/index.html",
    "/glossary/", "/glossary/aeo/", "/categories/", "/authors/tim-christensen/",
    "/checklist/", "/trending/", "/about/", "/contact/", "/privacy/", "/terms/",
    "/fonts/archivo-400.woff2", "/og.png",
    "/.well-known/indexnow-da88cd820092dc919206516858cd73d9.txt",
]


def fetch(path: str, bust: bool = False) -> int | str:
    url = BASE + path
    if bust:
        url += ("&" if "?" in path else "?") + "cachebust=1"
    req = urllib.request.Request(url, headers={"User-Agent": "exposure-check/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"ERR {e}"


def excluded_paths() -> list[str]:
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "stage_deploy.py"), "--check"],
                         capture_output=True, text=True, cwd=ROOT)
    if out.returncode != 0:
        print("stage_deploy.py --check failed:\n" + out.stdout + out.stderr)
        sys.exit(2)
    return [line.split("- ", 1)[1].strip() for line in out.stdout.splitlines()
            if line.strip().startswith("- ")]


def main() -> int:
    global BASE
    if "--deployment" in sys.argv:
        BASE = sys.argv[sys.argv.index("--deployment") + 1]

    bad = []
    private = excluded_paths()
    print(f"{len(private)} private files to check (must all be unreachable)")
    for rel in private:
        code = fetch("/" + rel.lstrip("/"), bust=True)
        if code != 404:
            bad.append((rel, code))
    print(f"  -> {len(private) - len(bad)} unreachable, {len(bad)} still public"
          + ("" if not bad else "  <-- LEAK"))

    print(f"{len(PUBLIC_PAGES)} public pages/assets to check (must all be 200)")
    for p in PUBLIC_PAGES:
        code = fetch(p)
        if code != 200:
            bad.append((p, code))
            print(f"  BROKEN {code} {p}")

    print()
    if bad:
        print("FAILURES:")
        for path, code in bad:
            print(f"   {code}  {path}")
        print("\nA cache-busted 404 vs a bare 200 means the edge cache still holds a "
              "pre-deploy copy: purge the cache rather than re-deploying.")
        return 1
    print("OK: no private file is reachable and every public page still resolves.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
