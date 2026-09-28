# Postmark review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free 100 emails/mo without overages; Basic $15/mo, Pro $16.50/mo, Platform $18/mo each starting at 10K emails, published (the vendor pricing page: [pricing page](https://postmarkapp.com/pricing), verified 2026-09-28). |
| Feature depth | 5/10 | Transactional email with separated message streams and delivery diagnostics cover the sending job (vendor documentation: [vendor site](https://postmarkapp.com), verified 2026-09-28). |
| Integrations | 6/10 | Slack, Zapier, WordPress, Customer.io, Supabase, Stripe, Netlify and Datadog documented plus an API (vendor documentation: [vendor site](https://postmarkapp.com), verified 2026-09-28). |
| AI capability | 5/10 | An MCP server with 24 tools, agent skills and a documented AI prompt library (vendor documentation: [vendor site](https://postmarkapp.com), verified 2026-09-28). |
| Openness | 3/10 | Closed SaaS with strong API and MCP access (the source repository: [repository](https://postmarkapp.com), verified 2026-09-28). |
| Operational maturity | 7/10 | Long-running transactional email service with published delivery numbers (vendor documentation: [vendor site](https://postmarkapp.com), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| &#10003; AI capabilities: MCP server with 24 tools and delivery diagnostics | &#10007; Paid plans start at $15/mo once past the free tier |
| &#10003; Native integrations include Slack, Zapier, WordPress (8 listed) | &#10007; Closed source - no self-hosting option |
| &#10003; Free tier to evaluate before committing (Free plan 100 emails/mo (no overages); Basic $15/mo, Pro $16) |  |

**What is Postmark?**
Transactional email API with separated message streams, an MCP server, and published delivery numbers. It ships with MCP server with 24 tools and delivery diagnostics, 8 integrations documented on this page. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Postmark cost?**
Postmark has a free tier; paid plans start at $15/mo. Free plan 100 emails/mo (no overages); Basic $15/mo, Pro $16.50/mo, Platform $18/mo, each starting at 10,000 emails; no annual billing; dedicated IPs from $50/mo for 300k+/mo senders. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Postmark worth it past the free tier?**
The transactional specialist, now with agent tooling and a published engineering track record; pay the per-email premium for mail where speed and reputation are revenue.

**Does Postmark support marketing email?**
Yes, with boundaries. Every server gets three default streams: outbound (transactional), broadcasts, and inbound, and a server can hold up to ten streams. Postmark states that transactional and broadcast traffic never intersect, including IP ranges, so broadcasts run on their own infrastructure. What it does not offer is the rest of the marketing job: no list management, no campaign builder, no automation. Inbound processing is limited to Pro and Platform plans.

**What does Postmark cost after the free plan?**
The free plan covers 100 emails a month with no overages. Paid plans all start at 10,000 emails a month: Basic at $15, Pro at $16.50, and Platform at $18, with overage rates of $1.80, $1.30, and $1.20 per thousand respectively. Volume pricing is published up to 1.5 million emails a month ($775, $852.50, and $930), beyond which you contact sales. Dedicated IPs start at $50 a month for senders above 300,000 a month on Pro or higher, retention upgrades start at $5 a month, and DMARC monitoring starts at $14 per domain. There is no annual billing option.

**What do Postmark&#x27;s MCP server and agent skills do?**
Postmark ships tooling for AI agents rather than AI features. The official MCP server reached version 2.0 in July 2026 with 24 tools, including delivery diagnostics, and five open-source Postmark Skills teach coding agents to send email. The developer docs also publish ten copy-paste prompts for Cursor, Copilot, Claude, and ChatGPT, plus an llms.txt file for assistant context. Everything still sends through the same REST API and your server token, so the agent path adds no new deliverability behavior.

- **Pricing:** Freemium
- **Category:** [Email Marketing](/categories/email-marketing/)
- **HQ:** Chicago, IL, USA
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Postmark is a tool in Email Marketing with a free tier. The catalog documents 3 AI features, 8 integrations and a public API. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Resend

Developer-first email API built around React Email, batch sending, and agent tooling

Customer.io

Data-driven messaging platform for automated email, push, SMS, and in-app messages

Notifuse

Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations

Twilio SendGrid

Scalable email delivery API with AI-powered deliverability and engagement tools

Warmbly

Open-source cold email platform with warmup, campaigns, unified inbox, and CRM

[More Email Marketing Tools →](/categories/email-marketing/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- Postmark
## Postmark review (2026): pricing, AI features, verdict

Transactional email API with separated message streams, an MCP server, and published delivery numbers

Email Marketing · Freemium Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[Visit Postmark &#8594;](https://postmarkapp.com)

[How we review](/methodology/) · No affiliate links

[Visit Postmark &#8594;](https://postmarkapp.com)

## MartechSignal Score: 34/60

Postmark separates message streams so transactional mail survives marketing blasts, and publishes delivery numbers to back it. The MCP server with 24 diagnostic tools is the newest reason developers look.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Postmark is a transactional email service owned by ActiveCampaign, which acquired it from Wildbit in May 2022 and kept it as a standalone product: the site footer still reads Made with heart at ActiveCampaign, and the company&#x27;s own FAQ says there is no plan to roll Postmark into ActiveCampaign&#x27;s marketing platform. Focus is the product. Postmark runs parallel but separate sending infrastructure for transactional and broadcast traffic and states that the two never intersect, including IP ranges, so a marketing blast cannot degrade password-reset deliverability. Servers expose message streams, three by default (outbound transactional, broadcasts, inbound) and up to ten per server, with inbound processing reserved for Pro and Platform plans. Speed claims are specific rather than vague: up to 4x faster than the competition, and a March 2026 post details the completed migration from PowerMTA to the open-source KumoMTA, with average queue times of about 1.2 seconds to Gmail and 6.3 seconds to Apple. Full message content and history is stored for 45 days by default, adjustable from 7 to 365 days with the retention add-on, while aggregate statistics are kept indefinitely. Pricing was restructured in August 2025: Free (100 emails a month, no overages), then Basic $15, Pro $16.50, and Platform $18 a month, all starting at 10,000 emails, with published volume tiers up to 1.5 million messages and no annual billing. The REST API is the same well-documented surface as ever, with official libraries for seven supported languages plus WordPress, Craft, and Zapier options. 2026 shipped a bulk email API (500 messages per request, 50MB payloads), webhooks that verify themselves, IP allowlisting, an MCP server with 24 tools, and agent skills. What Postmark does not do matters as much: no list management, no campaign builder, no automation. It pairs with a marketing ESP rather than replacing one.

Postmark homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- MCP server with 24 tools and delivery diagnostics
- Agent Skills for coding agents
- Documented AI prompt library for dev tools
## Key Integrations

- Slack
- Zapier
- WordPress
- Customer.io
- Supabase
- Stripe
- Netlify
- Datadog
## Pricing

Postmark is freemium, with a free tier to start, paid plans start at $15/mo as of 2026-09.

Free plan 100 emails/mo (no overages); Basic $15/mo, Pro $16.50/mo, Platform $18/mo, each starting at 10,000 emails; no annual billing; dedicated IPs from $50/mo for 300k+/mo senders

Current plans and limits live on the [Postmark pricing page](https://postmarkapp.com/pricing).

## How to install

- No install: hosted SaaS. Signup is at account.postmarkapp.com/sign_up, and the documented onboarding order is: create your first Server, verify a Sender Signature or Domain, understand message streams, then send a first test email.
- Grab a token: select your server, click API Tokens, and copy the Server API token (header X-Postmark-Server-Token); account-level calls use X-Postmark-Account-Token against https://api.postmarkapp.com. The POSTMARK_API_TEST token exercises the API without sending mail.
- Approval gate: until the account is approved, sends are delivered only to the account owner&#x27;s own verified address, and the API returns error 412 when a recipient does not share the From address&#x27;s domain.
- Official libraries cover the seven supported languages: npm install postmark, pip install postmark-python, gem install postmark, composer require wildbit/postmark-php, dotnet add package Postmark, plus Rails, Java, CLI, WordPress, and Craft packages.
- For agents, add the official MCP server (24 tools as of July 2026, including delivery diagnostics) or the five documented Postmark Skills; the developer docs also publish ten copy-paste AI prompts for Cursor, Copilot, Claude, and ChatGPT.
## Requirements

A verified sending identity (a single sender signature or a domain with DKIM), a server API token, and an approved account before you can mail anyone but yourself. The Email API accepts requests up to 10MB and batch requests up to 50MB, with a maximum of 500 messages per batch and 50 recipients across To, Cc, and Bcc. No numeric API rate limit is published; over-limit requests return HTTP 429. Bulk sending requires approval.

## Best for

Application teams that need password resets, receipts, and notifications to arrive fast and never want marketing traffic anywhere near that reputation: separate streams with separate IP ranges, a 45-day full message history, and delivery numbers Postmark publishes. The 2026 bulk API and MCP server also make it workable for agent-driven sending.

## Not for

Newsletters and marketing campaigns: there is no list management, campaign builder, or automation, and broadcast streams exist precisely so that traffic lives elsewhere. Also not for the price-per-email sensitive at high volume, since $15 buys 10,000 emails where bulk providers charge far less, and annual billing is not offered.

## Review notes

Assessed from postmarkapp.com, the developer docs, and the updates page in September 2026; we have no Postmark account and have not sent through it. The documentation is unusually complete: API error codes are documented inline with their exact strings, and webhook retry behavior is spelled out (1, 5, 10, 10, 10, then 15 minutes before Postmark gives up on an event).

Corrections against our earlier record. The note claiming Postmark was Twilio was wrong: ActiveCampaign announced the acquisition on May 3, 2022, remains the owner in 2026, and its GitHub organization owns every official Postmark repository. Our three listed AI features (spam filtering, delivery optimization, bounce analysis) appear nowhere on postmarkapp.com and are removed; the real AI story is tooling for agents, not AI features. And the &#x27;about one second&#x27; delivery claim is gone from the site, replaced by &#x27;up to 4x faster than the competition&#x27; with post-migration queue times per mailbox provider.

Two structural facts our record missed. Message streams are three, not two: outbound, broadcasts, and inbound, up to ten per server, with inbound processing gated to Pro and Platform. And the August 2025 pricing restructure created Basic, Pro, and Platform at $15, $16.50, and $18 for 10,000 emails a month, where dedicated IPs start at $50 a month and require senders above 300,000 a month on Pro or higher.

The KumoMTA migration (completed March 2026) is the most interesting public engineering note: Postmark moved off PowerMTA to the open-source MTA and published before-and-after queue times for Gmail, Yahoo, Microsoft, and Apple. Publishing those numbers is not something most ESPs do, and it is the kind of evidence that makes the status page worth trusting.

Provenance has to stay honest here: postmarkapp.com publishes no founding date and no headquarters address. The 2022 acquisition post describes founders Natalie and Chris Nagele having run Wildbit for 21 years, and a March 2026 post cites 16 years of sending reputation, so we dropped our earlier &#x27;founded 2009&#x27; claim rather than restate it.

## Verdict

The transactional specialist, now with agent tooling and a published engineering track record; pay the per-email premium for mail where speed and reputation are revenue.

## Pros and cons

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Transactional email API with separated message streams, an MCP server, and published delivery numbers. It ships with MCP server with 24 tools and delivery diagnostics, 8 integrations documented on this page. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Postmark has a free tier; paid plans start at $15/mo. Free plan 100 emails/mo (no overages); Basic $15/mo, Pro $16.50/mo, Platform $18/mo, each starting at 10,000 emails; no annual billing; dedicated IPs from $50/mo for 300k+/mo senders. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

The transactional specialist, now with agent tooling and a published engineering track record; pay the per-email premium for mail where speed and reputation are revenue.

Yes, with boundaries. Every server gets three default streams: outbound (transactional), broadcasts, and inbound, and a server can hold up to ten streams. Postmark states that transactional and broadcast traffic never intersect, including IP ranges, so broadcasts run on their own infrastructure. What it does not offer is the rest of the marketing job: no list management, no campaign builder, no automation. Inbound processing is limited to Pro and Platform plans.

The free plan covers 100 emails a month with no overages. Paid plans all start at 10,000 emails a month: Basic at $15, Pro at $16.50, and Platform at $18, with overage rates of $1.80, $1.30, and $1.20 per thousand respectively. Volume pricing is published up to 1.5 million emails a month ($775, $852.50, and $930), beyond which you contact sales. Dedicated IPs start at $50 a month for senders above 300,000 a month on Pro or higher, retention upgrades start at $5 a month, and DMARC monitoring starts at $14 per domain. There is no annual billing option.

Postmark ships tooling for AI agents rather than AI features. The official MCP server reached version 2.0 in July 2026 with 24 tools, including delivery diagnostics, and five open-source Postmark Skills teach coding agents to send email. The developer docs also publish ten copy-paste prompts for Cursor, Copilot, Claude, and ChatGPT, plus an llms.txt file for assistant context. Everything still sends through the same REST API and your server token, so the agent path adds no new deliverability behavior.

## Similar Tools

## Related reading

- [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/)
- [Salesforce's third no-code promise, audited](/blog/salesforce-third-no-code-promise/)
- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/postmark/#app",
    "name": "Postmark",
    "description": "Transactional email API with separated message streams, an MCP server, and published delivery numbers",
    "image": "https://martechsignal.com/og/tools/postmark.png",
    "url": "https://martechsignal.com/tools/postmark/",
    "sameAs": [
      "https://postmarkapp.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/postmark/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-07",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 15,
      "priceCurrency": "USD",
      "url": "https://postmarkapp.com/pricing",
      "priceValidUntil": "2026-12-31"
    }
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://martechsignal.com/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Tools",
        "item": "https://martechsignal.com/tools/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Email Marketing",
        "item": "https://martechsignal.com/categories/email-marketing/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Postmark",
        "item": "https://martechsignal.com/tools/postmark/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Postmark?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Transactional email API with separated message streams, an MCP server, and published delivery numbers. It ships with MCP server with 24 tools and delivery diagnostics, 8 integrations documented on this page. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Postmark cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Postmark has a free tier; paid plans start at $15/mo. Free plan 100 emails/mo (no overages); Basic $15/mo, Pro $16.50/mo, Platform $18/mo, each starting at 10,000 emails; no annual billing; dedicated IPs from $50/mo for 300k+/mo senders. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Postmark worth it past the free tier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The transactional specialist, now with agent tooling and a published engineering track record; pay the per-email premium for mail where speed and reputation are revenue."
        }
      },
      {
        "@type": "Question",
        "name": "Does Postmark support marketing email?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, with boundaries. Every server gets three default streams: outbound (transactional), broadcasts, and inbound, and a server can hold up to ten streams. Postmark states that transactional and broadcast traffic never intersect, including IP ranges, so broadcasts run on their own infrastructure. What it does not offer is the rest of the marketing job: no list management, no campaign builder, no automation. Inbound processing is limited to Pro and Platform plans."
        }
      },
      {
        "@type": "Question",
        "name": "What does Postmark cost after the free plan?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The free plan covers 100 emails a month with no overages. Paid plans all start at 10,000 emails a month: Basic at $15, Pro at $16.50, and Platform at $18, with overage rates of $1.80, $1.30, and $1.20 per thousand respectively. Volume pricing is published up to 1.5 million emails a month ($775, $852.50, and $930), beyond which you contact sales. Dedicated IPs start at $50 a month for senders above 300,000 a month on Pro or higher, retention upgrades start at $5 a month, and DMARC monitoring starts at $14 per domain. There is no annual billing option."
        }
      },
      {
        "@type": "Question",
        "name": "What do Postmark's MCP server and agent skills do?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Postmark ships tooling for AI agents rather than AI features. The official MCP server reached version 2.0 in July 2026 with 24 tools, including delivery diagnostics, and five open-source Postmark Skills teach coding agents to send email. The developer docs also publish ten copy-paste prompts for Cursor, Copilot, Claude, and ChatGPT, plus an llms.txt file for assistant context. Everything still sends through the same REST API and your server token, so the agent path adds no new deliverability behavior."
        }
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "Review",
    "author": {
      "@type": "Person",
      "name": "Tim Christensen",
      "url": "https://martechsignal.com/authors/tim-christensen/",
      "@id": "https://martechsignal.com/authors/tim-christensen/#person"
    },
    "publisher": {
      "@type": "Organization",
      "@id": "https://martechsignal.com/#organization",
      "name": "MartechSignal"
    },
    "datePublished": "2026-09-26",
    "reviewBody": "Postmark separates message streams so transactional mail survives marketing blasts, and publishes delivery numbers to back it. The MCP server with 24 diagnostic tools is the newest reason developers look.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/postmark/#app",
      "name": "Postmark",
      "url": "https://martechsignal.com/tools/postmark/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 34,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
