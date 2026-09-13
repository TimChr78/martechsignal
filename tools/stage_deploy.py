#!/usr/bin/env python3
"""Stage the public site into deploy-out/ so the working tree is NOT the publish root.

Why this exists
---------------
deploy.sh used to run `wrangler pages deploy .`, which uploads the whole repo
directory to martechsignal.com. That put 31 content drafts, 19 pipeline scripts,
pipeline JSON state, docs/, .github/workflows/, __pycache__ and 15 editor
backups on the public web. Two things were verified on 2026-09-13:

  * .gitignore is NOT honoured by `wrangler pages deploy` (a __pycache__/*.pyc was
    served byte-identical to the local file).
  * .assetsignore is NOT honoured by `wrangler pages deploy` either (adding it and
    redeploying left every path public - that mechanism is for Workers Assets).

So the only reliable boundary is the upload directory itself: copy the public
subset to deploy-out/ and deploy that.

Exclusions come from .assetsignore (one source of truth, reviewable in the repo).
The script refuses to stage if any known-public file would be left out, so a bad
pattern edit fails the deploy instead of taking the site down.

Usage:  python3 tools/stage_deploy.py            # stage only
        python3 tools/stage_deploy.py --check     # stage + print what was excluded
"""
from __future__ import annotations

import fnmatch
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT / "deploy-out"
IGNORE_FILE = ROOT / ".assetsignore"

# Never copied, regardless of .assetsignore.
ALWAYS_SKIP = {".git", ".wrangler", "deploy-out", "node_modules", ".pytest_cache"}

# If any of these is missing from the stage, the site is broken -> abort.
REQUIRED = [
    "index.html", "404.html", "style.css", "sitemap.xml", "robots.txt", "rss.xml",
    "llms.txt", "llms-full.txt", "og.png", "_redirects", "_headers",
    "blog/index.html", "tools/index.html", "glossary/index.html",
    "categories/index.html", "authors/index.html", "trending/index.html",
    "fonts/archivo-400.woff2", "og/agents-identity-debt.png",
    "ca0ff0788c47a161e772b2e9b073b2a4.txt",
    ".well-known/indexnow-da88cd820092dc919206516858cd73d9.txt",
]


def load_patterns() -> list[str]:
    pats = []
    for line in IGNORE_FILE.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            pats.append(line)
    return pats


def is_excluded(rel: str, name: str, patterns: list[str]) -> str | None:
    """Return the matching pattern if rel should not be published."""
    for p in patterns:
        anchored = p.startswith("/")
        pat = p[1:] if anchored else p
        dir_only = pat.endswith("/")
        pat = pat.rstrip("/")
        if dir_only:
            # directory pattern: excludes the subtree; match the directory itself
            if anchored:
                if rel == pat or rel.startswith(pat + "/"):
                    return p
            else:
                parts = rel.split("/")
                if any(fnmatch.fnmatch(part, pat) for part in parts[:-1]):
                    return p
            continue
        if anchored:
            if fnmatch.fnmatch(rel, pat) or rel.startswith(pat + "/"):
                return p
        else:
            if fnmatch.fnmatch(name, pat) or fnmatch.fnmatch(rel, pat) or any(
                fnmatch.fnmatch(part, pat) for part in rel.split("/")
            ):
                return p
    return None


def main() -> int:
    patterns = load_patterns()
    check = "--check" in sys.argv

    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)

    copied = excluded = 0
    excluded_paths: list[str] = []

    for entry in sorted(ROOT.rglob("*")):
        rel = entry.relative_to(ROOT).as_posix()
        top = rel.split("/")[0]
        if top in ALWAYS_SKIP:
            continue
        if any(part in ALWAYS_SKIP for part in rel.split("/")):
            continue
        if is_excluded(rel, entry.name, patterns):
            if entry.is_file():
                excluded += 1
                excluded_paths.append(rel)
            continue
        dest = STAGE / rel
        if entry.is_dir():
            dest.mkdir(parents=True, exist_ok=True)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(entry, dest)
            copied += 1

    missing = [r for r in REQUIRED if not (STAGE / r).exists()]
    if missing:
        print("STAGE FAILED - these public files would not be published:", file=sys.stderr)
        for m in missing:
            print("   ", m, file=sys.stderr)
        return 2

    total = sum(1 for p in STAGE.rglob("*") if p.is_file())
    size = sum(p.stat().st_size for p in STAGE.rglob("*") if p.is_file())
    print(f"staged {total} public files ({size / 1048576:.1f} MB) in deploy-out/")
    print(f"excluded {excluded} files that must not be public")
    if check:
        try:
            for path in sorted(excluded_paths):
                print("   -", path)
        except BrokenPipeError:  # piping into head/less is fine
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
