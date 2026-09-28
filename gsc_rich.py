#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["google-api-python-client>=2.100", "google-auth>=2.23"]
# ///
"""Dump rich-results detection (richResultsResult) for URLs via the GSC URL
Inspection API: which rich-result type Google saw (e.g. Product snippets),
the verdict, and every detected item/issue. Read-only; consumes inspection quota.

Usage:
    uv run gsc_rich.py <url> [url2 ...]
    uv run gsc_rich.py --file urls.txt
"""
import json, os, sys

SITE = "https://martechsignal.com/"
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


def main():
    args = sys.argv[1:]
    if args and args[0] == "--file":
        urls = [u.strip() for u in open(args[1]) if u.strip()]
    else:
        urls = args
    service = get_service()
    out = []
    for url in urls:
        try:
            resp = service.urlInspection().index().inspect(body={
                "inspectionUrl": url,
                "siteUrl": PROPERTY,
            }).execute()
            ir = resp.get("inspectionResult", {})
            rich = ir.get("richResultsResult")
            entry = {"url": url, "index": ir.get("indexStatusResult", {}).get("verdict"),
                     "rich_verdict": None, "detected": []}
            if rich:
                entry["rich_verdict"] = rich.get("verdict")
                # API shape: detectedItems[] = {richResultType, items: [{name, issues}]}
                for item in rich.get("detectedItems", []):
                    kids = []
                    for sub in item.get("items", []):
                        kids.append({"name": sub.get("name"),
                                     "issues": [{"name": i.get("name"), "severity": i.get("severity"),
                                                 "message": i.get("message")}
                                                for i in sub.get("issues", [])]})
                    entry["detected"].append({"type": item.get("richResultType"), "items": kids})
            out.append(entry)
            print(json.dumps(entry))
        except Exception as e:
            print(json.dumps({"url": url, "error": str(e)}))
    with open("/opt/data/gsc-rich-results.json", "w") as f:
        json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
