#!/usr/bin/env python3
"""M3 (2026-09-27): /methodology/ renders on the main template like every other
page. Content lives in tools/methodology-content.html; this wraps it in the
shared shell (masthead, footer, stylesheet) and ships the 2-level breadcrumb."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from build_tools import page_shell  # noqa: E402

content = (ROOT / "tools" / "methodology-content.html").read_text()
breadcrumb = {
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://martechsignal.com/"},
        {"@type": "ListItem", "position": 2, "name": "Methodology", "item": "https://martechsignal.com/methodology/"},
    ],
}
out = page_shell(
    "Methodology | MartechSignal",
    "How MartechSignal researches tools, verifies prices and dates, and scores the six pillars. "
    "Desk research with dated verification; no sponsored rankings; corrections are logged.",
    "https://martechsignal.com/methodology/",
    content,
    schema_json=[breadcrumb],
)
out = out.replace(
    "</head>",
    '<link rel="alternate" type="text/markdown" href="/methodology/index.md" title="Markdown mirror">\n</head>',
    1,
)
(ROOT / "methodology" / "index.html").write_text(out)
print("ok: /methodology/ built on the main template")
