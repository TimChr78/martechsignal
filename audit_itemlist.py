#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["google-api-python-client>=2.100", "google-auth>=2.23"]
# ///
"""One-shot audit: URL-inspect every sitemap URL and record ALL rich-result
issues mentioning itemListElement (plus any FAIL verdicts).

Usage: uv run audit_itemlist.py <property> <out.json> [urls.txt|- < urls]
Set GSC_SERVICE_ACCOUNT_KEY if key is not at ~/.hermes/gsc-service-account.json
"""
import json, os, sys, time

KEY_PATH = os.environ.get("GSC_SERVICE_ACCOUNT_KEY",
                          "/home/hermes/.hermes/gsc-service-account.json")

def get_service():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    creds = service_account.Credentials.from_service_account_file(
        KEY_PATH, scopes=["https://www.googleapis.com/auth/webmasters"])
    return build("searchconsole", "v1", credentials=creds)

def main():
    prop, out_path = sys.argv[1], sys.argv[2]
    urls = [u.strip() for u in sys.stdin if u.strip()]
    print(f"property={prop} urls={len(urls)}", flush=True)
    service = get_service()
    out, flagged = [], []
    for n, url in enumerate(urls, 1):
        try:
            resp = service.urlInspection().index().inspect(body={
                "inspectionUrl": url, "siteUrl": prop}).execute()
            ir = resp.get("inspectionResult", {})
            rich = ir.get("richResultsResult") or {}
            entry = {
                "url": url,
                "index": ir.get("indexStatusResult", {}).get("verdict"),
                "rich_verdict": rich.get("verdict"),
                "issues": [],
            }
            for item in rich.get("detectedItems", []):
                for sub in item.get("items", []):
                    for iss in sub.get("issues", []):
                        msg = iss.get("message", "")
                        issue = {"type": item.get("richResultType"),
                                 "item": sub.get("name"),
                                 "issue": iss.get("issueType"),
                                 "severity": iss.get("severity"),
                                 "message": msg}
                        entry["issues"].append(issue)
                        if "itemListElement" in msg or "itemListElement" in str(iss):
                            flagged.append(entry)
            out.append(entry)
            mark = " <<<ITEMLIST" if any("itemListElement" in str(i) for i in entry["issues"]) else ""
            bad = " [richFAIL]" if entry["rich_verdict"] == "FAIL" else ""
            print(f"{n}/{len(urls)} {url} idx={entry['index']} rich={entry['rich_verdict']}{bad}{mark}", flush=True)
        except Exception as e:
            out.append({"url": url, "error": str(e)[:200]})
            print(f"{n}/{len(urls)} {url} ERROR {str(e)[:120]}", flush=True)
            if "429" in str(e):
                time.sleep(30)
        time.sleep(1.2)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"\n=== {len(flagged)} URLs flagged with itemListElement issues ===", flush=True)
    for e in flagged:
        types = {i["type"] for i in e["issues"] if "itemListElement" in str(i)}
        print(f"  {e['url']}  types={sorted(types)}", flush=True)

if __name__ == "__main__":
    main()
