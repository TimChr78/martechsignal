#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["google-api-python-client>=2.100", "google-auth>=2.23"]
# ///
"""Request Google indexing for URLs via Search Console URL Inspection API.

Usage:
    uv run gsc_inspect.py <url> [url2 ...]
    uv run gsc_inspect.py --all          # inspect all site URLs
    uv run gsc_inspect.py --changed      # inspect URLs changed in last git commit

Requires: GSC_SERVICE_ACCOUNT_KEY env var or ~/.hermes/gsc-service-account.json
The service account must be added as an owner/user in Google Search Console.
"""
import json, os, sys, subprocess, time

SITE = "https://martechsignal.com/"
# Domain properties must be addressed by their sc-domain: identifier, not URL.
PROPERTY = os.environ.get("GSC_PROPERTY", "sc-domain:martechsignal.com")
KEY_PATH = os.environ.get("GSC_SERVICE_ACCOUNT_KEY",
                          "/home/hermes/.hermes/gsc-service-account.json")

def get_service():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    creds = service_account.Credentials.from_service_account_file(
        KEY_PATH, scopes=["https://www.googleapis.com/auth/webmasters"]
    )
    return build("searchconsole", "v1", credentials=creds)

def inspect_url(service, url):
    """Request indexing inspection for a single URL. Returns (url, status, detail)."""
    try:
        resp = service.urlInspection().index().inspect(body={
            "inspectionUrl": url,
            "siteUrl": PROPERTY
        }).execute()
        result = resp.get("inspectionResult", {}).get("indexStatusResult", {})
        verdict = result.get("verdict", "UNKNOWN")
        coverage = result.get("coverageState", "")
        last_crawl = result.get("lastCrawlTime", "never")
        return (url, verdict, f"{coverage} | last crawl: {last_crawl}")
    except Exception as e:
        return (url, "ERROR", str(e))

def get_all_urls():
    """Get all site URLs from the built output."""
    urls = [SITE]
    base = os.path.dirname(os.path.abspath(__file__))
    blog_dir = os.path.join(base, "blog")
    if os.path.isdir(blog_dir):
        for entry in sorted(os.listdir(blog_dir)):
            if os.path.isfile(os.path.join(blog_dir, entry, "index.html")):
                urls.append(f"{SITE}blog/{entry}/")
    tools_dir = os.path.join(base, "tools")
    if os.path.isdir(tools_dir):
        for entry in sorted(os.listdir(tools_dir)):
            if os.path.isfile(os.path.join(tools_dir, entry, "index.html")):
                urls.append(f"{SITE}tools/{entry}/")
    return urls

def get_changed_urls():
    """Get URLs changed in the last git commit."""
    base = os.path.dirname(os.path.abspath(__file__))
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True, text=True, cwd=base, timeout=10
        )
        urls = []
        for line in result.stdout.strip().splitlines():
            line = line.strip()
            if line.startswith("blog/") and line.endswith("/index.html"):
                slug = line.split("/")[1]
                urls.append(f"{SITE}blog/{slug}/")
            elif line.startswith("tools/") and line.endswith("/index.html"):
                slug = line.split("/")[1]
                urls.append(f"{SITE}tools/{slug}/")
            elif line == "index.html":
                urls.append(SITE)
        return urls
    except Exception:
        return []

def main():
    if not os.path.exists(KEY_PATH):
        print(f"SKIP: Service account key not found at {KEY_PATH}")
        print("Create one in Google Cloud Console and add the SA email to GSC.")
        sys.exit(0)

    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        urls = get_all_urls()
    elif len(sys.argv) > 1 and sys.argv[1] == "--changed":
        urls = get_changed_urls()
        if not urls:
            print("No changed URLs detected.")
            sys.exit(0)
    elif len(sys.argv) > 1:
        urls = sys.argv[1:]
    else:
        print("Usage: gsc_inspect.py <url>... | --all | --changed")
        sys.exit(1)

    print(f"Inspecting {len(urls)} URLs on {SITE}...")
    service = get_service()
    counts = {"PASS": 0, "FAIL": 0, "NEUTRAL": 0, "ERROR": 0}

    for url in urls:
        u, verdict, detail = inspect_url(service, url)
        counts[verdict] = counts.get(verdict, 0) + 1
        short = u.replace(SITE, "/")
        print(f"  {verdict:8s} {short}  ({detail})")
        time.sleep(0.3)

    p = counts.get("PASS", 0)
    n = counts.get("NEUTRAL", 0)
    f = counts.get("FAIL", 0)
    e = counts.get("ERROR", 0)
    print(f"\nDone: {p} indexed, {n} pending, {f} failed, {e} errors")

if __name__ == "__main__":
    main()
