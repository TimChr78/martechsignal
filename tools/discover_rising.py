#!/usr/bin/env python3
"""Rising-stars discovery: young GitHub repos (created <120 days) gaining traction
in martech-relevant topics. Complements discover_tools.py (which finds established
projects via topic+stars queries but misses newcomers before they accumulate stars
and topic tags).

Outputs to tools/candidates.json (merged with existing queue), same schema as
discover_tools.py so the existing triage flow works unchanged.

Run: python3 tools/discover_rising.py
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANDIDATES = ROOT / "tools" / "candidates.json"
REJECTED = ROOT / "tools" / "rejected.json"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Young repos: push velocity matters more than total stars. A repo created 3 weeks
# ago with 60 stars is a stronger signal than a 3-year-old repo with 600.
MIN_STARS = 15
MAX_AGE_DAYS = 120

# Topic pairs that map to the directory's categories (kept deliberately broad here;
# triage filters relevance).
SEARCH_QUERIES = [
    "topic:marketing-automation",
    "topic:marketing topic:ai",
    "topic:email-marketing",
    "topic:crm",
    "topic:seo topic:ai",
    "topic:ai-agents topic:marketing",
    "topic:agentic topic:marketing",
    "topic:marketing topic:automation",
    "topic:marketing topic:mcp",
    "topic:chatbot topic:marketing",
    "topic:marketing-analytics",
]


def gh_get(path: str) -> dict:
    url = f"https://api.github.com{path}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        "User-Agent": "martechsignal-discovery",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def load_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text())
    return default


def main():
    since = (datetime.now(timezone.utc) - timedelta(days=MAX_AGE_DAYS)).strftime("%Y-%m-%d")
    existing = load_json(CANDIDATES, [])
    queue = existing if isinstance(existing, list) else existing.get("candidates", [])
    seen_repos = {c.get("full_name") for c in queue if isinstance(c, dict)}
    # also skip anything already in the directory or previously rejected
    tools = load_json(ROOT / "tools" / "tools.json", [])
    dir_repos = {str(t.get("github_repo") or "").rstrip("/").split("github.com/")[-1].lower()
                 for t in tools if isinstance(t, dict)}
    # directory slug names too (catches slug-vs-reponame drift, e.g. maizzle/framework vs slug 'maizzle')
    dir_slugs = {str(t.get("slug") or "").lower() for t in tools if isinstance(t, dict)}
    rejected = load_json(REJECTED, [])
    rej_repos = {x.get("full_name", "").lower() for x in rejected if isinstance(x, dict)}
    rej_names = {x.get("name", "").lower() for x in rejected if isinstance(x, dict)}

    # spam heuristics: mass-uploaded guide/cheatsheet repos that pollute the queue
    # (2026-08-31 wave: ~10 German "Leitfaden" guide repos at 50-66 stars from single-author accounts)
    SPAM_MARKERS = (
        "leitfaden", "cheatsheet", "cheat-sheet", "cheat sheet", "awesome-", "playbook",
        "guide", "anleitung", "tutorial", "wörterbuch", "handbuch", "資源", "教程",
        "download", "booste", "reichweite", "kaltakquise", "vertriebsautomatisierung",
    )
    def looks_like_spam(repo):
        desc = (repo.get("description") or "").lower()
        name = (repo.get("name") or "").lower()
        if any(m in desc for m in SPAM_MARKERS) or any(m in name for m in SPAM_MARKERS):
            return True
        # README-sized red flag: description calling it a framework/list rather than a tool
        if desc.startswith(("a curated", "the ultimate", "free guerrilla", "battle-tested ai prompts")):
            return True
        return False

    new_items = []
    for query in SEARCH_QUERIES:
        q = urllib.parse.quote(f"{query} stars:>={MIN_STARS} created:>={since}")
        try:
            data = gh_get(f"/search/repositories?q={q}&sort=stars&order=desc&per_page=20")
        except Exception as e:
            print(f"  ! search failed for {query}: {e}")
            continue
        for repo in data.get("items", []):
            full = repo.get("full_name", "")
            if not full or full.lower() in seen_repos:
                continue
            if full.lower() in rej_repos or repo.get("name", "").lower() in rej_names:
                continue
            if full.lower() in dir_repos:
                continue
            # dedupe by directory slug too: 'maizzle/framework' matches existing slug 'maizzle'
            if repo.get("name", "").lower() in dir_slugs:
                continue
            if looks_like_spam(repo):
                continue
            seen_repos.add(full)
            age_days = (datetime.now(timezone.utc) - datetime.fromisoformat(
                repo["created_at"].replace("Z", "+00:00"))).days
            stars_per_week = round(repo["stargazers_count"] / max(age_days / 7, 0.5), 1)
            new_items.append({
                "full_name": full,
                "name": repo.get("name", ""),
                "url": repo.get("html_url", ""),
                "description": (repo.get("description") or "")[:200],
                "stars": repo.get("stargazers_count", 0),
                "age_days": age_days,
                "stars_per_week": stars_per_week,
                "topics": repo.get("topics", []),
                "language": repo.get("language"),
                "source": f"rising:{query.split()[0].replace('topic:', '')}",
                "found_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            })
        # search API: 30 req/min authenticated max; be polite
        import time
        time.sleep(2)

    if not new_items:
        print("no new rising repos found")
        return

    # rank by stars/week (the rising metric)
    new_items.sort(key=lambda x: -x["stars_per_week"])
    queue.extend(new_items)
    CANDIDATES.write_text(json.dumps(queue, indent=1, ensure_ascii=False))
    print(f"queued {len(new_items)} rising repos (top: " +
          ", ".join(f"{i['name']} {i['stars']}★/{i['age_days']}d" for i in new_items[:5]) + ")")


if __name__ == "__main__":
    main()
