#!/usr/bin/env python3
"""IndexNow submission for martechsignal.com — staged, NOT auto-fired.

Usage:  python3 tools/indexnow_submit.py            # submit changed URLs from .lastmod.json
        python3 tools/indexnow_submit.py URL [URL]  # submit specific URLs

Requires: the IndexNow key file deployed at /.well-known/indexnow-<key>.txt
(placeholder below — replace with the real key on first run; Bing/IndexNow
verify domain ownership by fetching that file).

Also submits to Bing's IndexNow endpoint (same protocol). Google does NOT
participate in IndexNow — for Google, use GSC URL Inspection + sitemap pings
(already handled by deploy.sh / gsc_inspect.py --changed).
"""
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY_FILE = ROOT / "tools" / ".indexnow-key"
LASTMOD = ROOT / "tools" / ".lastmod.json"
ENDPOINT = "https://api.indexnow.org/indexnow"  # routes to participating engines (Bing, Yandex, Seznam, Naver)

HOST = "martechsignal.com"
KEYFILE_URL = f"https://{HOST}/indexnow-{{key}}.txt"  # root variant; engines verify this reliably


def load_key() -> str:
    if KEY_FILE.exists():
        return KEY_FILE.read_text().strip()
    print(f"NOTE: {KEY_FILE} missing. Generate a key (e.g. python3 -c \"import secrets;print(secrets.token_hex(16))\")"
          f", save it there, deploy {KEYFILE_URL} with the key as file content, then re-run.")
    sys.exit(1)


def changed_urls(limit: int = 100) -> list[str]:
    """URLs whose content-hash changed most recently (newest store dates first)."""
    store = json.loads(LASTMOD.read_text())
    dated = sorted(store.items(), key=lambda kv: kv[1].get("date", ""), reverse=True)
    out = []
    for path, rec in dated[:limit]:
        rel = path.replace(str(ROOT), "").lstrip("/")
        if not rel:
            out.append(f"https://{HOST}/")
            continue
        if rel.endswith("index.html"):
            rel = rel[: -len("index.html")]  # /blog/foo/index.html -> /blog/foo/
        if rel and not rel.endswith("/"):
            rel += "/"
        out.append(f"https://{HOST}/{rel}")
    return out


def submit(urls: list[str]) -> None:
    key = load_key()
    body = {
        "host": HOST,
        "key": key,
        "keyLocation": KEYFILE_URL.format(key=key),
        "urlList": urls,
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow: HTTP {r.status} for {len(urls)} URLs")
    except urllib.error.HTTPError as e:
        print(f"IndexNow error: HTTP {e.code} — {e.read().decode()[:200]}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urls = [u for u in sys.argv[1:] if u.startswith("http")]
    else:
        urls = changed_urls()
    if not urls:
        print("nothing to submit")
        sys.exit(0)
    print(f"submitting {len(urls)} URLs (first 3: {urls[:3]})")
    submit(urls)
