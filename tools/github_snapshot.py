#!/usr/bin/env python3
"""Daily GitHub stars/forks snapshot for martechsignal /trending/ momentum tracker.
Appends one snapshot per day to tools/github-history.json. Silent unless error."""
import json, os, sys, urllib.request
from datetime import date

REPO = "/mnt/user/dev/martechsignal"
HIST = os.path.join(REPO, "tools", "github-history.json")
TODAY = date.today().isoformat()

# token from hermes .env (5000/hr vs 60 unauth)
tok = None
for line in open("/home/hermes/.hermes/.env"):
    if line.strip().startswith("GITHUB_TOKEN="):
        tok = line.split("=", 1)[1].strip()

tools = json.load(open(os.path.join(REPO, "tools", "tools.json")))
if not isinstance(tools, list):
    tools = tools.get("tools", [])
repos = [(t["slug"], t["github_repo"]) for t in tools if t.get("github_repo")]

try:
    hist = json.load(open(HIST))
except Exception:
    hist = []

# skip if today's snapshot already exists (idempotent)
if hist and hist[-1].get("date") == TODAY:
    print(f"[SILENT] snapshot for {TODAY} already exists")
    sys.exit(0)

headers = {"User-Agent": "martechsignal"}
if tok:
    headers["Authorization"] = f"Bearer {tok}"

snapshot = {"date": TODAY, "repos": {}}
errors = []
for slug, repo in repos:
    try:
        # tolerate full-URL github_repo values (older pipeline entries)
        api_repo = repo.rstrip("/").split("github.com/")[-1]
        req = urllib.request.Request(f"https://api.github.com/repos/{api_repo}", headers=headers)
        d = json.load(urllib.request.urlopen(req, timeout=15))
        snapshot["repos"][slug] = {
            "full_name": repo,
            "stars": d["stargazers_count"],
            "forks": d["forks_count"],
            "open_issues": d["open_issues_count"],
            "pushed": d["pushed_at"][:10],
        }
    except Exception as e:
        errors.append(f"{slug}: {str(e)[:60]}")

hist.append(snapshot)
json.dump(hist, open(HIST, "w"), indent=1)

# r14 H-2 (2026-09-29): one pipeline, one number. The money-page momentum
# blocks read the fresh snapshot while tool pages read the catalog record,
# so every fast-growing repo diverged upward (40/40 claims). Sync the
# snapshot figures back into the catalog record (stars + forks + check
# date) so every page quoting a number quotes the same one, stamped with
# the same date. Per-record human verification (date_updated on other
# fields) is untouched — only the machine-counted GitHub figures sync.
_tools_path = os.path.join(REPO, "tools", "tools.json")
_catalog = json.load(open(_tools_path))
_records = _catalog if isinstance(_catalog, list) else _catalog.get("tools", [])
_synced = 0
for _t in _records:
    _snap = snapshot["repos"].get(_t.get("slug", ""))
    if not _snap:
        continue
    if _t.get("github_stars") != _snap["stars"] or _t.get("github_forks") != _snap["forks"]:
        _t["github_stars"] = _snap["stars"]
        _t["github_forks"] = _snap["forks"]
        _t["github_checked"] = TODAY
        _synced += 1
if _synced:
    json.dump(_catalog, open(_tools_path, "w"), indent=2, ensure_ascii=False)
    print(f"[SYNC] {TODAY}: {_synced} catalog records synced to snapshot figures")

if errors:
    print(f"[WARN] {TODAY}: {len(snapshot['repos'])}/{len(repos)} collected; errors: {errors}")
elif len(snapshot['repos']) == 0:
    print(f"[ERROR] no repos tracked")
# else silent success
