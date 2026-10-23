#!/usr/bin/env python3
"""Build the newsletter subscribe result pages + the internal platform test page.

These are utility pages, not editorial content: every one is ``noindex`` and
intentionally absent from sitemap.xml, llms.txt and the markdown mirrors
(build_md_mirrors.py skips the ``subscribe/`` prefix). Run before
build_tools.py in deploy.sh so the sitemap step sees the whole tree; the
sitemap is built from explicit content lists, so these four stay out.

Kit remains the live provider. Only /subscribe/test/ renders the self-hosted
form, via ``form_html(..., provider="am")``, so the pilot can be exercised
without moving any public page off Kit.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_tools import page_shell
from subscribe_form import form_html

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "subscribe"

VIEWPORT = '<meta name="viewport" content="width=device-width, initial-scale=1">'
NOINDEX = '<meta name="robots" content="noindex">'


def _build(slug, title, description, body):
    path = f"/subscribe/{slug}/"
    schema = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": f"https://martechsignal.com{path}",
        "url": f"https://martechsignal.com{path}",
        "name": title,
        "isPartOf": {"@id": "https://martechsignal.com/#website"},
    }
    html = page_shell(title, description, path, body, schema)
    # page_shell has no noindex switch (it serves indexable pages); add the tag
    # directly after the viewport meta so every utility page is excluded alike.
    assert VIEWPORT in html, f"page_shell head changed; cannot add noindex to {path}"
    html = html.replace(VIEWPORT, VIEWPORT + "\n" + NOINDEX, 1)
    out_dir = OUT / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html)
    print(f"  ✓ {out_dir.relative_to(ROOT)}/index.html")


def build_check_your_inbox():
    _build(
        "check-your-inbox",
        "Check your inbox | MartechSignal",
        "Confirm your MartechSignal newsletter subscription from the link in your inbox.",
        """<article class="page-head">
<h1>Check your inbox</h1>
<p class="lede">We sent you a confirmation link. Click it to start getting the newsletter. The link is valid for 7 days.</p>
<p class="fine">Nothing arrived? Check the spam folder, or try again with another address.</p>
<p><a class="textlink" href="/">Back to the homepage</a></p>
</article>""",
    )


def build_welcome():
    _build(
        "welcome",
        "You’re in | MartechSignal",
        "Your MartechSignal newsletter subscription is confirmed.",
        """<article class="page-head">
<h1>You’re in</h1>
<p class="lede">The next issue arrives on Friday.</p>
<div class="list">
<a href="/tools/">Tool directory</a>
<a href="/blog/">Latest writing</a>
<a href="/methodology/">How we review</a>
</div>
</article>""",
    )


def build_oops():
    _build(
        "oops",
        "That didn’t work | MartechSignal",
        "Something went wrong with the newsletter signup. Please try again or contact us.",
        """<article class="page-head">
<h1>That didn’t work</h1>
<p class="lede">Something went wrong with the signup. Please try again, or write to us via the contact page.</p>
<p><a class="textlink" href="/#subscribe">Try again</a> · <a class="textlink" href="/contact/">Contact</a></p>
</article>""",
    )


def build_test():
    _build(
        "test",
        "Newsletter signup test | MartechSignal",
        "Internal test page for the new newsletter platform.",
        """<article class="page-head">
<h1>Newsletter signup test</h1>
<p class="fine">Internal test page for the new newsletter platform. Not linked from the site.</p>
</article>
<section class="subscribe sub-inline" id="subscribe"><h2>Subscribe</h2>"""
        + form_html("/subscribe/test/", "Newsletter subscribe (test)", provider="am")
        + "</section>",
    )


def main():
    print("Subscribe pages:")
    build_check_your_inbox()
    build_welcome()
    build_oops()
    build_test()


if __name__ == "__main__":
    main()
