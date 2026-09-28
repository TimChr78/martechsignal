# Resend review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free 3,000 emails/mo (100/day, 3 domains), Transactional Pro $20/mo (50K), Scale $90 to $1,150/mo published tiers (the vendor pricing page). |
| Feature depth | 6/10 | Transactional and marketing email with batch sending and contact imports cover the developer email stack (vendor documentation). |
| Integrations | 6/10 | Next.js, Vercel, React Email, Zapier, an official Cursor plugin and Vercel Marketplace documented (vendor documentation). |
| AI capability | 6/10 | AI Email Editor with brand-voice drafting, template assistant and column mapping plus a hosted MCP server (vendor documentation). |
| Openness | 6/10 | MIT SDKs at 19.7k GitHub stars behind a closed sending service (the source repository). |
| Operational maturity | 6/10 | Founded 2023 with fast developer adoption and published tier ceilings (vendor documentation). |


| Pros | Cons |
| --- | --- |
| &#10003; AI capabilities: AI Email Editor with brand-voice drafting | &#10007; Paid plans start at $20/mo once past the free tier |
| &#10003; Established community (19,722 GitHub stars) | &#10007; Closed source - no self-hosting option |
| &#10003; Native integrations include Next.js, Vercel, React Email (6 listed) |  |
| &#10003; Free tier to evaluate before committing (Free 3,000 emails/mo (100/day cap, 3 domains); Transactional) |  |

**What is Resend?**
Developer-first email API built around React Email, batch sending, and agent tooling. It ships with AI Email Editor with brand-voice drafting, 19,722 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Resend cost?**
Resend has a free tier; paid plans start at $20/mo. Free 3,000 emails/mo (100/day cap, 3 domains); Transactional Pro $20/mo for 50,000; Scale $90-$1,150/mo published tiers; Enterprise custom; Marketing priced by contacts from $40/mo for 5,000; no annual discounts. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Resend worth it past the free tier?**
The most developer-native platform in email, with an honest free tier, real agent tooling, and a published limit sheet; check the transactional versus marketing split before committing either budget.

**What are Resend&#x27;s rate limits and batch limits?**
The API allows 10 requests per second per team with no burst allowance; exceeding it returns 429, and Resend says it can raise the limit for trusted senders on request. Batch sending accepts up to 100 emails in a single call, and each batch counts as one request against the rate limit, but attachments are not supported on the batch endpoint. Per-email attachments cap at 40MB after base64 encoding, and a hard limit of 5x your monthly quota applies to sending.

**Is Resend free, and what does the free tier include?**
The transactional free plan includes 3,000 emails a month with a 100-per-day cap, 3 verified domains, 5 AI credits, and 10,000 automation runs a month. Pro is $20 a month for 50,000 emails, Scale publishes tiers from $90 for 100,000 to $1,150 for 2.5 million, and Enterprise is custom, with a 99.99% uptime SLA. Marketing email is a separate, contact-based subscription starting at $40 a month for 5,000 contacts. There are no annual discounts; the pricing FAQ answers that question with a plain no.

**Does Resend work with AI agents and coding tools?**
Yes, and it is one of the better-documented cases in email. Resend hosts an MCP server at mcp.resend.com/mcp with OAuth, ships an official Claude plugin (claude plugin install resend@claude-plugins-official), and documents a Resend skill and a React Email skill alongside a CLI. Clients listed in the docs include Claude Code, Claude, Cursor, Codex, Copilot, Windsurf, and Warp. The changelog shows steady investment: an official MCP server in April 2026, a remote MCP server in July, and an official Cursor plugin in August.

- **Pricing:** Freemium
- **Category:** [Email Marketing](/categories/email-marketing/)
- **GitHub:** ★ 19722
- **Founded:** 2023
- **HQ:** San Francisco, CA, USA
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Resend is a tool in Email Marketing with a free tier. The catalog documents 4 AI features, 6 integrations and a public API. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

React Email Editor

Drag-n-Drop Email Editor Component for React.js

Customer.io

Data-driven messaging platform for automated email, push, SMS, and in-app messages

Postmark

Transactional email API with separated message streams, an MCP server, and published delivery numbers

Loops

Email marketing for SaaS: marketing, product, and transactional email in one tool

[More Email Marketing Tools →](/categories/email-marketing/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- Resend
## Resend review (2026): pricing, AI features, verdict

Developer-first email API built around React Email, batch sending, and agent tooling

Email Marketing · Freemium Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[Visit Resend &#8594;](https://resend.com)

[How we review](/methodology/) · No affiliate links

[Visit Resend &#8594;](https://resend.com)

## MartechSignal Score: 38/60

Resend is developer email built around React Email, with a hosted MCP server and an official Cursor plugin. 19.7k stars on the MIT SDKs, and marketing prices published alongside transactional.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Resend is a developer-first email platform built by people who make developer tools: founders Zeno Rocha, Bu Kinoshita, and Jonni Lundy started the open-source React Email project in 2022, launched the sending platform in 2023 through Y Combinator&#x27;s W23 batch, and raised an $18M Series A led by Andreessen Horowitz in December 2024. By June 2026 the company reported 3 million users, 6.8 million weekly npm downloads, and profitability. The product split is unusual and worth understanding before you buy: transactional and marketing email are separate subscriptions. Transactional starts free at 3,000 emails a month (100 a day), Pro is $20 a month for 50,000, and Scale publishes tiers from $90 for 100,000 to $1,150 for 2.5 million a month; marketing is priced by contacts, from $40 a month for 5,000. There are no annual discounts, and the pricing FAQ says so in one word: no. The developer surface is the draw. Official SDKs cover Node.js, Python, Go, Rust, PHP, Laravel, Ruby, Java, and .NET, plus a chat adapter, batch sending takes up to 100 messages per call, and webhooks document eight event types with retries and replays, alongside inbound receiving, broadcasts, audiences, templates, and automations. Agent tooling is first-class: a hosted MCP server at mcp.resend.com with OAuth, a CLI, and documented skills for Claude Code, Cursor, and Codex. AI is real but modest: an AI Email Editor with brand-voice drafting and pre-send checks, an assistant in the template editor, and AI column mapping on contact imports, metered through monthly AI credits. Deliverability tooling is rule-based, not AI. Sending runs on AWS across four regions, with account data held in the United States regardless of region. Resend fits product teams shipping email from code, not marketers who want a campaign studio.

Resend homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI Email Editor with brand-voice drafting
- AI assistant in the template editor
- AI column mapping on contact imports
- Hosted MCP server and agent skills
## Key Integrations

- Next.js
- Vercel
- React Email
- Zapier
- Cursor (official plugin)
- Vercel Marketplace
## Pricing

Resend is freemium, with a free tier to start, paid plans start at $20/mo as of 2026-09.

Free 3,000 emails/mo (100/day cap, 3 domains); Transactional Pro $20/mo for 50,000; Scale $90-$1,150/mo published tiers; Enterprise custom; Marketing priced by contacts from $40/mo for 5,000; no annual discounts

Current plans and limits live on the [Resend pricing page](https://resend.com/pricing).

## How to install

- npm install resend, then send with an API key: import { Resend } from &#x27;resend&#x27;; const resend = new Resend(&#x27;re_xxxxxxxxx&#x27;). Official SDKs cover Node.js, Python, Go, Rust, PHP, Laravel, Ruby, Java, and .NET.
- Or use the CLI: curl -fsSL https://resend.com/install.sh | bash (also npm install -g resend-cli and brew install resend/cli/resend; on Windows, irm https://resend.com/install.ps1 | iex).
- Verify a domain before production: add the generated DKIM and SPF records (TXT plus MX or CNAME) exactly as Resend generates them. The docs strongly recommend a subdomain such as notifications.example.com rather than your root domain.
- Pick a sending region at setup: North Virginia (us-east-1), Ireland (eu-west-1), Sao Paulo (sa-east-1), or Tokyo (ap-northeast-1). The docs state that all account data stays in the United States regardless of region.
- For agents, point an MCP client at https://mcp.resend.com/mcp (OAuth) or run claude plugin install resend@claude-plugins-official; the docs also publish a Resend skill and a React Email skill for coding agents.
## Requirements

A domain you control with DNS access for DKIM and SPF records, and an API key. The API rate limit is 10 requests per second per team with no burst allowance (429 beyond it, raiseable for trusted senders on request), batch sends take up to 100 messages per call and do not support attachments, and per-email attachments cap at 40MB after base64 encoding. Domains allowed: 3 on Free, 10 on Pro, 1,000 on Scale. Sent and inbound emails both count against quota, with a hard ceiling of 5x your monthly quota.

## Best for

Product and platform teams that send application email from code and want the workflow to live next to their IDE: React Email components, typed SDKs, batch API, webhooks with replays, and an MCP server for coding agents. The free tier and three-domain allowance make it a comfortable start for side projects and SaaS products alike.

## Not for

Marketing teams that want a campaign studio first: marketing plans exist but are priced by contacts, and broadcasts can only go to existing contacts, so segmentation and journey building are thinner than Customer.io or Klaviyo. Also not for buyers needing annual billing discounts, HIPAA compliance (listed as in progress), or dedicated IP pools below the Scale tier.

## Review notes

Assessed from resend.com, resend.com/docs, and the changelog RSS in September 2026; we have no Resend account and have not sent through it. The documentation corpus is large and current: the changelog&#x27;s newest entries are Link Checker (September 3, 2026), Single Sign-On (September 1), and an Email Metrics API (August 27).

The correction that matters: the three AI features in our earlier record (AI deliverability optimization, AI spam detection, smart retry logic) appear nowhere in Resend&#x27;s documentation. The documented AI surface is an AI Email Editor with brand-voice drafting and pre-send checks, an assistant in the template editor, AI column mapping on imports, and monthly AI credits; Deliverability Insights is explicitly a set of best-practice checks, not AI. Slack and Segment are not documented integrations, and Scale is not custom-priced.

Open source is the exit surface, and our record undersold it: react-email alone holds about 19,700 GitHub stars under MIT, an order of magnitude larger than any Resend SDK repo, and the organization publishes roughly 100 repositories including the MCP server, CLI, skills, and OpenAPI spec. Templates you build in React Email keep working against another sender.

The transactional and marketing split is the pricing trap. A team that starts on Pro for product email and later wants newsletters takes a second, contact-based subscription, and the docs recommend separate subdomains per stream anyway. IP pools are a $30 a month Scale add-on with an eligibility bar of 3,000 emails a day, so shared IPs are the default reality for most accounts.

## Verdict

The most developer-native platform in email, with an honest free tier, real agent tooling, and a published limit sheet; check the transactional versus marketing split before committing either budget.

## Pros and cons

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Developer-first email API built around React Email, batch sending, and agent tooling. It ships with AI Email Editor with brand-voice drafting, 19,722 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Resend has a free tier; paid plans start at $20/mo. Free 3,000 emails/mo (100/day cap, 3 domains); Transactional Pro $20/mo for 50,000; Scale $90-$1,150/mo published tiers; Enterprise custom; Marketing priced by contacts from $40/mo for 5,000; no annual discounts. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

The most developer-native platform in email, with an honest free tier, real agent tooling, and a published limit sheet; check the transactional versus marketing split before committing either budget.

The API allows 10 requests per second per team with no burst allowance; exceeding it returns 429, and Resend says it can raise the limit for trusted senders on request. Batch sending accepts up to 100 emails in a single call, and each batch counts as one request against the rate limit, but attachments are not supported on the batch endpoint. Per-email attachments cap at 40MB after base64 encoding, and a hard limit of 5x your monthly quota applies to sending.

The transactional free plan includes 3,000 emails a month with a 100-per-day cap, 3 verified domains, 5 AI credits, and 10,000 automation runs a month. Pro is $20 a month for 50,000 emails, Scale publishes tiers from $90 for 100,000 to $1,150 for 2.5 million, and Enterprise is custom, with a 99.99% uptime SLA. Marketing email is a separate, contact-based subscription starting at $40 a month for 5,000 contacts. There are no annual discounts; the pricing FAQ answers that question with a plain no.

Yes, and it is one of the better-documented cases in email. Resend hosts an MCP server at mcp.resend.com/mcp with OAuth, ships an official Claude plugin (claude plugin install resend@claude-plugins-official), and documents a Resend skill and a React Email skill alongside a CLI. Clients listed in the docs include Claude Code, Claude, Cursor, Codex, Copilot, Windsurf, and Warp. The changelog shows steady investment: an official MCP server in April 2026, a remote MCP server in July, and an official Cursor plugin in August.

## Similar Tools

## Related reading

- [Salesforce Made Agentforce Free. What Marketing Ops Can Build With It.](/blog/salesforce-agentforce-free-marketing-ops/)
- [Claude SEO vs Seonaut: which free SEO checker should you run](/blog/claude-seo-vs-seonaut/)
- [Salesforce's third no-code promise, audited](/blog/salesforce-third-no-code-promise/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/resend/#app",
    "name": "Resend",
    "description": "Developer-first email API built around React Email, batch sending, and agent tooling",
    "image": "https://martechsignal.com/og/tools/resend.png",
    "url": "https://martechsignal.com/tools/resend/",
    "sameAs": [
      "https://resend.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/resend/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-07",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 20,
      "priceCurrency": "USD",
      "url": "https://resend.com/pricing",
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
        "name": "Resend",
        "item": "https://martechsignal.com/tools/resend/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Resend?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Developer-first email API built around React Email, batch sending, and agent tooling. It ships with AI Email Editor with brand-voice drafting, 19,722 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Resend cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Resend has a free tier; paid plans start at $20/mo. Free 3,000 emails/mo (100/day cap, 3 domains); Transactional Pro $20/mo for 50,000; Scale $90-$1,150/mo published tiers; Enterprise custom; Marketing priced by contacts from $40/mo for 5,000; no annual discounts. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Resend worth it past the free tier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The most developer-native platform in email, with an honest free tier, real agent tooling, and a published limit sheet; check the transactional versus marketing split before committing either budget."
        }
      },
      {
        "@type": "Question",
        "name": "What are Resend's rate limits and batch limits?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The API allows 10 requests per second per team with no burst allowance; exceeding it returns 429, and Resend says it can raise the limit for trusted senders on request. Batch sending accepts up to 100 emails in a single call, and each batch counts as one request against the rate limit, but attachments are not supported on the batch endpoint. Per-email attachments cap at 40MB after base64 encoding, and a hard limit of 5x your monthly quota applies to sending."
        }
      },
      {
        "@type": "Question",
        "name": "Is Resend free, and what does the free tier include?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The transactional free plan includes 3,000 emails a month with a 100-per-day cap, 3 verified domains, 5 AI credits, and 10,000 automation runs a month. Pro is $20 a month for 50,000 emails, Scale publishes tiers from $90 for 100,000 to $1,150 for 2.5 million, and Enterprise is custom, with a 99.99% uptime SLA. Marketing email is a separate, contact-based subscription starting at $40 a month for 5,000 contacts. There are no annual discounts; the pricing FAQ answers that question with a plain no."
        }
      },
      {
        "@type": "Question",
        "name": "Does Resend work with AI agents and coding tools?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, and it is one of the better-documented cases in email. Resend hosts an MCP server at mcp.resend.com/mcp with OAuth, ships an official Claude plugin (claude plugin install resend@claude-plugins-official), and documents a Resend skill and a React Email skill alongside a CLI. Clients listed in the docs include Claude Code, Claude, Cursor, Codex, Copilot, Windsurf, and Warp. The changelog shows steady investment: an official MCP server in April 2026, a remote MCP server in July, and an official Cursor plugin in August."
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
    "reviewBody": "Resend is developer email built around React Email, with a hosted MCP server and an official Cursor plugin. 19.7k stars on the MIT SDKs, and marketing prices published alongside transactional.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/resend/#app",
      "name": "Resend",
      "url": "https://martechsignal.com/tools/resend/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 38,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
