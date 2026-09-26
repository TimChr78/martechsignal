#!/usr/bin/env python3
"""Tool discovery pipeline for martechsignal.com directory.

Scans GitHub + RSS feeds for new AI marketing tools not yet in the directory.
Outputs candidate list to tools/candidates.json for human review.

Run: python3 /opt/data/martechsignal/tools/discover_tools.py
Env: GITHUB_TOKEN (optional, raises rate limit from 60→5000/hr)
"""
import json, os, re, sys, urllib.request, urllib.parse, ssl
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS_FILE = ROOT / "tools" / "tools.json"
CANDIDATES_FILE = ROOT / "tools" / "candidates.json"
CATEGORIES_FILE = ROOT / "tools" / "categories.json"
REJECTED_FILE = ROOT / "tools" / "rejected.json"

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
USER_AGENT = "MartechSignal-ToolDiscovery/1.0"

# SSL context for environments without full cert bundles
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_json(url, headers=None):
    """Fetch JSON from URL with error handling."""
    hdrs = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"  ⚠ Failed: {url[:80]}... → {e}", file=sys.stderr)
        return None

def github_headers():
    h = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        h["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return h

# ── Load existing tools ────────────────────────────────────────────

def load_existing():
    tools = json.loads(TOOLS_FILE.read_text())
    slugs = {t["slug"] for t in tools}
    names = {t["name"].lower() for t in tools}
    websites = set()
    for t in tools:
        w = t.get("website", "").rstrip("/").lower()
        w = re.sub(r'^https?://(www\.)?', '', w)
        websites.add(w)
    repos = {t["github_repo"] for t in tools if t.get("github_repo")}
    return tools, slugs, names, websites, repos

# ── GitHub discovery ───────────────────────────────────────────────

GITHUB_QUERIES = [
    "topic:marketing-automation stars:>100",
    "topic:marketing+topic:ai stars:>50",
    "topic:email-marketing stars:>100",
    "topic:crm stars:>200",
    "topic:marketing+topic:automation stars:>80",
    "topic:seo+topic:ai stars:>50",
    "topic:chatbot+topic:marketing stars:>50",
    "topic:content-generation+topic:ai stars:>100",
    "topic:marketing-analytics stars:>80",
    "topic:marketing+topic:llm stars:>30",
    "topic:ai-agents+topic:marketing stars:>30",
    "topic:agentic+topic:marketing stars:>20",
    "topic:ai-agents+topic:crm stars:>20",
    "topic:seo+topic:agent stars:>20",
    "topic:marketing+topic:mcp stars:>10",
]

def search_github():
    """Search GitHub for marketing/AI repos not in directory."""
    _, slugs, names, websites, repos = load_existing()
    candidates = []
    seen_repos = set()

    for query in GITHUB_QUERIES:
        url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(query)}&sort=stars&order=desc&per_page=30"
        data = fetch_json(url, github_headers())
        if not data or "items" not in data:
            continue

        for item in data["items"]:
            full_name = item["full_name"]
            if full_name in repos or full_name in seen_repos:
                continue
            seen_repos.add(full_name)

            # Skip if name matches existing tool
            repo_name = item.get("name", "").lower()
            if repo_name in names:
                continue

            # Skip non-tool repos (libraries, awesome-lists, tutorials)
            desc = (item.get("description") or "").lower()
            skip_words = ["awesome", "list", "tutorial", "course", "book", "guide",
                         "collection", "resources", "cheatsheet", "interview"]
            if any(w in repo_name or w in desc[:50] for w in skip_words):
                continue

            # Must have some activity
            pushed = item.get("pushed_at", "")
            if pushed:
                try:
                    last_push = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
                    if last_push < datetime.now(last_push.tzinfo) - timedelta(days=180):
                        continue  # stale repo
                except:
                    pass

            candidates.append({
                "source": "github",
                "name": item.get("name", ""),
                "full_name": full_name,
                "description": item.get("description", ""),
                "stars": item.get("stargazers_count", 0),
                "url": item.get("html_url", ""),
                "homepage": item.get("homepage", ""),
                "topics": item.get("topics", []),
                "language": item.get("language", ""),
                "last_push": pushed,
                "discovered": datetime.now().isoformat(),
            })

        # Rate limit courtesy
        import time
        time.sleep(1)

    return candidates

# ── RSS discovery ──────────────────────────────────────────────────

RSS_FEEDS = [
    ("HubSpot", "https://blog.hubspot.com/marketing/rss.xml"),
    ("Salesforce", "https://www.salesforce.com/blog/feed/"),
    ("Zapier", "https://zapier.com/blog/feeds/latest/"),
    ("Hootsuite", "https://blog.hootsuite.com/feed/"),
    ("Intercom", "https://www.intercom.com/blog/feed/"),
]

def fetch_rss_titles(url, max_items=10):
    """Fetch recent titles from RSS feed (simple XML parse, no deps)."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            content = resp.read().decode("utf-8", errors="replace")[:50000]
        # Extract titles from <title> tags (skip first = feed title)
        titles = re.findall(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', content, re.DOTALL)
        return [t.strip() for t in titles[1:max_items+1] if t.strip()]
    except Exception as e:
        print(f"  ⚠ RSS failed: {url} → {e}", file=sys.stderr)
        return []

def scan_rss():
    """Scan RSS feeds for mentions of new tools."""
    _, slugs, names, websites, repos = load_existing()
    mentions = []

    # Keywords that suggest a new tool announcement
    tool_keywords = ["launch", "new tool", "introducing", "announce", "release",
                    "ai tool", "ai-powered", "platform", "startup"]

    for source, url in RSS_FEEDS:
        titles = fetch_rss_titles(url)
        for title in titles:
            tl = title.lower()
            if any(kw in tl for kw in tool_keywords):
                mentions.append({
                    "source": f"rss:{source}",
                    "title": title,
                    "feed_url": url,
                    "discovered": datetime.now().isoformat(),
                })

    return mentions

# ── Main ───────────────────────────────────────────────────────────

def log(msg):
    """Progress output to stderr (invisible to cron delivery)."""
    print(msg, file=sys.stderr)

def main():
    log(f"🔍 Tool Discovery Pipeline - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    log(f"   GitHub token: {'✓ set' if GITHUB_TOKEN else '✗ not set (60 req/hr limit)'}")
    log("")

    # Load existing
    tools, slugs, names, websites, repos = load_existing()
    log(f"   Existing directory: {len(tools)} tools, {len(repos)} GitHub repos tracked")
    log("")

    # GitHub search
    log("📡 Searching GitHub...")
    gh_candidates = search_github()
    log(f"   Found {len(gh_candidates)} new repo candidates")

    # RSS scan
    log("📡 Scanning RSS feeds...")
    rss_mentions = scan_rss()
    log(f"   Found {len(rss_mentions)} tool-related mentions")

    # Load previous candidates to avoid duplicates
    prev = []
    if CANDIDATES_FILE.exists():
        try:
            prev = json.loads(CANDIDATES_FILE.read_text())
        except:
            prev = []
    prev_repos = {c.get("full_name") for c in prev if c.get("source") == "github"}
    prev_titles = {c.get("title") for c in prev if c.get("source", "").startswith("rss")}

    # Deduplicate
    # (2026-09-16 fix: the rejected-filter used to run only on the merged queue,
    # while the Telegram announcement printed the PRE-filter new_gh/new_rss -
    # so every run advertised items its own filter discarded seconds later.)
    new_gh = [c for c in gh_candidates if c["full_name"] not in prev_repos]
    new_rss = [c for c in rss_mentions if c["title"] not in prev_titles]

    # Skip previously rejected tools (2026-09-10: queue was re-filling with
    # ~25 settled rejections every run because rejected.json was never checked)
    rejected = []
    if REJECTED_FILE.exists():
        try:
            rejected = json.loads(REJECTED_FILE.read_text())
        except Exception as e:
            log(f"  ⚠ Could not parse rejected.json ({e}) - proceeding without it")
    rej_urls = set()
    for x in rejected:
        if not isinstance(x, dict):
            continue
        u = (x.get("url") or "").rstrip("/").lower()
        u = re.sub(r'^https?://(www\.)?', '', u)
        if u:
            rej_urls.add(u)
        n = (x.get("name") or "").lower()
        if n:
            rej_urls.add(n)

    # Tools already in the live directory must not be re-announced: their queue
    # entry is consumed at review time, so without this check an approved tool
    # reappears in the next run's announcement (2026-09-16)
    live_names, live_repos, live_hosts = set(), set(), set()
    try:
        live_tools = json.loads(TOOLS_FILE.read_text())
        for t in live_tools:
            if t.get("status") != "active":
                continue
            if t.get("name"):
                live_names.add(str(t["name"]).lower())
            repo = str(t.get("github_repo") or "").rstrip("/").lower()
            repo = re.sub(r"^https?://(www\.)?github\.com/", "", repo)
            site = str(t.get("website") or "").rstrip("/").lower()
            # ~17 live tools use a github.com URL as their website; match those
            # by repo path, never by host (github.com in live_hosts would
            # suppress every future GitHub candidate)
            if "github.com/" in site and not repo:
                repo = site.split("github.com/")[-1]
            if repo:
                live_repos.add(repo)
            host = re.sub(r"^https?://(www\.)?", "", site).split("/")[0]
            if host and "github.com" not in host:
                live_hosts.add(host)
    except Exception as e:
        log(f"  ⚠ Could not load tools.json for live-check ({e})")

    def is_rejected(c):
        u = (c.get("url") or c.get("homepage") or "").rstrip("/").lower()
        u = re.sub(r'^https?://(www\.)?', '', u)
        if u and u in rej_urls:
            return True
        gh = (c.get("url") or "").rstrip("/").split("github.com/")[-1].lower()
        if c.get("source") == "github" and gh and gh in rej_urls:
            return True
        # already live in the directory -> not a "new" candidate
        if (c.get("name") or "").lower() in live_names:
            return True
        c_repo = (c.get("url") or "").rstrip("/").split("github.com/")[-1].lower()
        if c_repo and c_repo in live_repos:
            return True
        c_host = re.sub(r"^https?://(www\.)?", "", (c.get("homepage") or c.get("url") or "")
                        .rstrip("/").lower()).split("/")[0]
        if c_host and c_host in live_hosts:
            return True
        # RSS mentions carry the post title in `title`; rejected entries store
        # that same title as `name` (and the feed URL as `url`)
        if (c.get("title") or "").lower() in rej_urls:
            return True
        return (c.get("name") or "").lower() in rej_urls

    # Filter rejections from the NEW items (2026-09-16: filter new_gh/new_rss
    # BEFORE both the announcement and the merge - previously the filter ran
    # only on the merged queue while the announcement printed the pre-filter
    # lists, so settled rejections were advertised every run and then dropped)
    pre_filter = len(new_gh) + len(new_rss)
    new_gh = [c for c in new_gh if not is_rejected(c)]
    new_rss = [c for c in new_rss if not is_rejected(c)]
    filtered = pre_filter - len(new_gh) - len(new_rss)
    if filtered:
        log(f"   Skipped {filtered} previously-rejected candidate(s)")

    # Merge with previous (keep last 100). Everything merged here has already
    # passed the rejection filter, so the queue can't refill with settled items
    # (2026-09-10 queue-refill fix, tightened 2026-09-16)
    all_candidates = prev + new_gh + new_rss
    all_candidates = all_candidates[-100:]  # cap at 100

    # Save
    CANDIDATES_FILE.write_text(json.dumps(all_candidates, indent=2))

    # Also write to n8n shared data dir
    n8n_dir = Path("/mnt/cache/appdata/n8n/data")
    try:
        n8n_dir.mkdir(parents=True, exist_ok=True)
        (n8n_dir / "tool-candidates.json").write_text(json.dumps(all_candidates, indent=2))
    except OSError:
        pass

    # Log summary to stderr
    log("")
    log(f"{'='*50}")
    log(f"📋 RESULTS: {len(new_gh)} new GitHub + {len(new_rss)} new RSS | queue: {len(all_candidates)}")

    # stdout ONLY when there's something new (silent watchdog pattern)
    if new_gh or new_rss:
        print(f"🔍 Tool Discovery - {len(new_gh)} new candidates + {len(new_rss)} mentions\n")
        if new_gh:
            print("🆕 Top GitHub discoveries:")
            for c in sorted(new_gh, key=lambda x: -x.get("stars", 0))[:10]:
                print(f"  ★{c['stars']:>6} | {c['full_name']:<40} | {c['description'][:60]}")
        if new_rss:
            print("\n📰 RSS mentions:")
            for c in new_rss[:5]:
                print(f"  [{c['source']}] {c['title'][:70]}")
        print(f"\nReview: tools/candidates.json")
    # else: empty stdout = no Telegram message

    return 0

if __name__ == "__main__":
    sys.exit(main())
