#!/usr/bin/env python3
"""Single canonical GitHub-star sync (A3 stardrift architecture, 2026-10-02).
tools.json is the ONLY star store. Any writer (snapshot cron, build entry)
calls sync_from_history() instead of private one-off syncs; builders immport
this before load() so every rendered number equals github-history's newest
day. Idempotent, quiet."""
import json
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HIST = os.path.join(REPO, "tools", "github-history.json")
TOOLS = os.path.join(REPO, "tools", "tools.json")


def sync_from_history():
    """Sync catalog github_stars/forks/checked from the newest history day.
    Returns count synced. Never writes when nothing drifted."""
    try:
        hist = json.load(open(HIST))
    except (OSError, ValueError):
        return 0
    if not hist:
        return 0
    latest = hist[-1]
    snap = latest.get("repos") or {}
    try:
        cat = json.load(open(TOOLS))
    except (OSError, ValueError):
        return 0
    recs = cat if isinstance(cat, list) else cat.get("tools", [])
    n = 0
    for t in recs:
        if not isinstance(t, dict):
            continue
        s = snap.get(t.get("slug", ""))
        if not s:
            continue
        if t.get("github_stars") != s.get("stars") or t.get("github_forks") != s.get("forks"):
            t["github_stars"] = s.get("stars")
            t["github_forks"] = s.get("forks")
            t["github_checked"] = latest.get("date")
            n += 1
    if n:
        json.dump(cat, open(TOOLS, "w"), indent=1, ensure_ascii=False)
    return n


if __name__ == "__main__":
    n = sync_from_history()
    print(n)
