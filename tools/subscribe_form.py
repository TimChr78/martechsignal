"""Shared newsletter subscribe form partial.

Kit stays the live provider for every page that renders a subscribe form. The
self-hosted platform (am.martechsignal.com) is prepared here behind
``NEWSLETTER_PROVIDER`` and exercised only by the internal /subscribe/test/
page; switching the constant is the whole cutover.

Markup contract: design/DESIGN.md (sentence case, existing classes, no inline
colour styles).
"""
from __future__ import annotations

import html

# "kit" (live today) | "am" (self-hosted platform, not switched on yet)
NEWSLETTER_PROVIDER = "am"

AM_FORM_URL = "https://am.martechsignal.com/f/frm_01a16cd267367aa4b58e42c1400965fc"
CONSENT_TEXT = "Send me the weekly newsletter. Unsubscribe any time."

# Kit form 9136291 - unchanged action/fields from the pre-partial markup.
_KIT_ACTION = "https://app.kit.com/forms/9136291/subscriptions"
_KIT_FORM = (
    f'<form class="sub-form" action="{_KIT_ACTION}" method="post" '
    'data-sv-form="9136291" data-uid="f315181f90" target="_blank">'
    '<input type="hidden" name="newsletter[subscriber][first_name]" value="">'
    '<input type="email" name="email_address" autocomplete="email" '
    'placeholder="you@company.com" aria-label="Email address" required>'
    '<button type="submit">Subscribe</button>'
    '</form>'
)


def form_html(page_path: str, button_event: str = "Newsletter subscribe",
              provider: str | None = None) -> str:
    """Return the subscribe ``<form>`` element only (no surrounding section).

    ``provider`` defaults to ``NEWSLETTER_PROVIDER`` so builders keep posting to
    Kit until the constant is deliberately changed. ``page_path`` is only
    consumed by the self-hosted provider, which stores the originating page.
    """
    provider = provider or NEWSLETTER_PROVIDER
    if provider == "kit":
        # Byte-identical to the form every builder emitted before the partial.
        return _KIT_FORM
    if provider == "am":
        page_esc = html.escape(page_path, quote=True)
        event_esc = html.escape(button_event, quote=True)
        return (
            f'<form class="sub-form" action="{AM_FORM_URL}" method="post">'
            '<input type="email" name="email" autocomplete="email" '
            'placeholder="you@company.com" aria-label="Email address" required>'
            '<div class="hp" aria-hidden="true">'
            '<input type="text" name="am_hp" tabindex="-1" autocomplete="off">'
            '</div>'
            f'<input type="hidden" name="page" value="{page_esc}">'
            f'<button type="submit" data-umami-event="{event_esc}">Subscribe</button>'
            f'<p class="fine consent">{CONSENT_TEXT}</p>'
            '</form>'
        )
    raise ValueError(f"Unknown newsletter provider: {provider!r}")
