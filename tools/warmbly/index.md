# Warmbly review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free to self-host under Apache 2.0; cloud free plan with 10 mailboxes, Starter $29/mo (150 sends/day), Grow $89/mo (3,000 sends/day) published (the vendor pricing page: [pricing page](https://warmbly.com/pricing/), verified 2026-09-24). |
| Feature depth | 6/10 | Warmup, campaigns, a unified inbox and CRM make a complete cold-email loop for its size (vendor documentation: [vendor site](https://warmbly.com), verified 2026-09-28). |
| Integrations | 5/10 | HubSpot, Slack, Zapier, Gmail, Microsoft 365 and SMTP plus REST API and HMAC webhooks documented (vendor documentation: [vendor site](https://warmbly.com), verified 2026-09-28). |
| AI capability | 7/10 | Agent steps that branch on classified reply intent with automatic reply classification (positive, OOO, unsubscribe, bounce) are genuinely agentic (vendor documentation: [vendor site](https://warmbly.com), verified 2026-09-28). |
| Openness | 9/10 | Apache-2.0 self-hosted with no cloud dependency and 316 GitHub stars (the source repository: [repository](warmbly/warmbly), verified 2026-09-28). |
| Operational maturity | 3/10 | Founded 2026 with 316 stars; the operating history is measured in months (vendor documentation: [vendor site](https://warmbly.com), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| &#10003; Apache-2.0 licence with free self-hosting | &#10007; Paid plans start at $23/mo once past the free tier |
| &#10003; AI capabilities: AI agent steps in campaign sequences that branch on classified reply intent | &#10007; Young project (316 GitHub stars) - smaller community and plugin ecosystem |
| &#10003; Native integrations include HubSpot, Slack, Zapier (8 listed) |  |

**What is Warmbly?**
Open-source cold email platform with warmup, campaigns, unified inbox, and CRM. It ships with AI agent steps in campaign sequences that branch on classified reply intent, 316 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Warmbly cost?**
Warmbly has a free tier; paid plans start at $23/mo. Free to self-host under Apache 2.0 with no cloud dependency. Hosted cloud: free plan with 10 mailboxes; Starter $29/mo (150 sends/day), Grow $89/mo (3,000 sends/day, CRM + API), Business $329/mo (15,000 sends/day). Annual billing saves 20%. We last checked both ends of that split on 2026-09-24. The pricing section above shows what the free tier actually covers.

**Is Warmbly a good self-hosted Email Marketing tool in 2026?**
The most complete open-source cold email stack we have listed, but young (316 stars, launched 2026) and self-hosting puts deliverability operations on you.

- **Pricing:** Open Source
- **Category:** [Email Marketing](/categories/email-marketing/)
- **GitHub:** ★ 316
- **Founded:** 2026
- **HQ:** London, UK
- **API:** Yes
- **Last verified:** 2026-09-24

**Verdict:** Warmbly is a tool in Email Marketing with free and open source. The catalog documents 4 AI features, 8 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-24. This is a desk review, not a hands-on test. Desk-reviewed

Notifuse

Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations

Loops

Email marketing for SaaS: marketing, product, and transactional email in one tool

Customer.io

Data-driven messaging platform for automated email, push, SMS, and in-app messages

Listmonk

Open-source self-hosted newsletter and mailing list manager with a fast Go backend

[More Email Marketing Tools →](/categories/email-marketing/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- Warmbly
## Warmbly review (2026): pricing, AI features, verdict

Open-source cold email platform with warmup, campaigns, unified inbox, and CRM

Email Marketing · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-24

[Visit Warmbly &#8594;](https://warmbly.com)

[How we review](/methodology/) · No affiliate links

[Visit Warmbly &#8594;](https://warmbly.com)

## MartechSignal Score: 38/60

Warmbly packages cold email honestly as open source: Apache 2.0, self-hosted, with warmup and reply classification built in. At 316 stars and a 2026 founding date, you are the early adopter and the operator.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Warmbly is an open-source cold email platform that sends from mailboxes you already own and warms them gradually so they stop landing in spam. It bundles warmup pools, multi-step campaigns, a shared reply inbox, analytics, and a small CRM into one self-hostable stack (Apache 2.0, built with Go, Rust, Elixir, and React). The audience is founders, agencies, and sales teams running outbound B2B, the same crowd paying Instantly or Smartlead for this workflow today. The AI parts are narrower than the &quot;AI-native&quot; branding suggests. Campaign sequences can include AI agent steps that branch on classified reply intent. The unified inbox labels incoming replies as positive, out of office, unsubscribe, or bounce the moment they land, and holds agent drafts for follow-ups. A content checker scores template deliverability before you send, advisory only, it never blocks a campaign. Reply classification is the genuinely useful piece; the rest is assistive rather than autonomous. Pricing splits cleanly in two. Self-hosting is free with no cloud dependency: a curl install script brings up Docker Compose with Postgres and Redis, and outbound mail leaves through each mailbox&#x27;s own provider rather than Warmbly&#x27;s servers. The hosted cloud has a free plan with 10 mailboxes, then Starter at $29/mo (150 sends/day), Grow at $89/mo (3,000 sends/day, adds CRM, A/B variants, and the API), and Business at $329/mo (15,000 sends/day, team roles, audit log). Watch the send caps: 150/day at Starter is thin next to similarly priced plans at Instantly, though annual billing shaves 20%. Against Smartlead or Instantly, the draw is self-hosting and the Apache 2.0 license. Your mailbox credentials and lead data never leave your own infrastructure, and you scale throughput by running more workers. The trade-off is youth: 316 GitHub stars as of September 2026, one company behind it (Mindroot Ltd, London), and no lead database included. The hosted competitors have years of deliverability tooling and B2B data you would have to source separately. If you want managed cold email at volume and do not care where the servers live, the incumbents are more mature. If you are an agency that needs client outreach on your own hardware, or a product team that wants to embed sending behind an API with signed webhooks, Warmbly earns a Docker Compose run.

## AI Capabilities

- AI agent steps in campaign sequences that branch on classified reply intent
- Automatic reply classification (positive, out of office, unsubscribe, bounce) in the unified inbox
- Agent-drafted follow-up replies
- Advisory AI content check with deliverability score before sending
## Key Integrations

- HubSpot
- Slack
- Zapier
- REST API
- Webhooks (HMAC-signed)
- Gmail
- Microsoft 365
- SMTP
## Pricing

Warmbly is free to self-host under the Apache-2.0 licence, paid plans start at $23/mo as of 2026-09.

Free to self-host under Apache 2.0 with no cloud dependency. Hosted cloud: free plan with 10 mailboxes; Starter $29/mo (150 sends/day), Grow $89/mo (3,000 sends/day, CRM + API), Business $329/mo (15,000 sends/day). Annual billing saves 20%.

Current plans and limits live on the [Warmbly pricing page](https://warmbly.com/pricing/).

## Best for

Agencies and dev-heavy teams that want cold outreach data on their own infrastructure, or product teams embedding sending via API and signed webhooks.

## Not for

Teams that need a built-in B2B lead database, or anyone who wants a battle-tested managed sender and does not want to operate Postgres and Redis.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Warmbly is the self-hostable answer to Instantly and Smartlead: warmup pools, rotating mailbox sends, a shared reply inbox, and a light CRM, all Apache 2.0. The architecture separates a control plane (Postgres, Redis, event bus) from Go workers that send through each mailbox&#x27;s own provider, so throughput scales by adding workers and mail never routes through Warmbly&#x27;s IPs.

The AI layer is reply classification plus agent steps in sequences, not autonomous campaign building. Self-hosting is genuinely free (one curl install, Docker Compose); the paid side is the hosted cloud, priced by daily send volume. This assessment comes from the repo, docs, and vendor pricing pages.

## Verdict

The most complete open-source cold email stack we have listed, but young (316 stars, launched 2026) and self-hosting puts deliverability operations on you.

## Pros and cons

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source cold email platform with warmup, campaigns, unified inbox, and CRM. It ships with AI agent steps in campaign sequences that branch on classified reply intent, 316 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Warmbly has a free tier; paid plans start at $23/mo. Free to self-host under Apache 2.0 with no cloud dependency. Hosted cloud: free plan with 10 mailboxes; Starter $29/mo (150 sends/day), Grow $89/mo (3,000 sends/day, CRM + API), Business $329/mo (15,000 sends/day). Annual billing saves 20%. We last checked both ends of that split on 2026-09-24. The pricing section above shows what the free tier actually covers.

The most complete open-source cold email stack we have listed, but young (316 stars, launched 2026) and self-hosting puts deliverability operations on you.

## Similar Tools

## Related reading

- [Salesforce Made Agentforce Free. What Marketing Ops Can Build With It.](/blog/salesforce-agentforce-free-marketing-ops/)
- [Microsoft Just Removed the Steering Wheel From Search Ads](/blog/microsoft-search-ads-steering-wheel/)
- [Where open-source martech momentum actually lives](/blog/oss-momentum-tracker-september-2026/)
### Quick Facts

Related guides: [Ai Email Marketing Tools](/best/ai-email-marketing-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/warmbly/#app",
    "name": "Warmbly",
    "description": "Open-source cold email platform with warmup, campaigns, unified inbox, and CRM",
    "image": "https://martechsignal.com/og/tools/warmbly.png",
    "url": "https://martechsignal.com/tools/warmbly/",
    "sameAs": [
      "https://warmbly.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/warmbly/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-26",
    "datePublished": "2026-09-24",
    "offers": {
      "@type": "Offer",
      "price": 23,
      "priceCurrency": "USD",
      "url": "https://warmbly.com/pricing/",
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
        "name": "Warmbly",
        "item": "https://martechsignal.com/tools/warmbly/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Warmbly?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source cold email platform with warmup, campaigns, unified inbox, and CRM. It ships with AI agent steps in campaign sequences that branch on classified reply intent, 316 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Warmbly cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Warmbly has a free tier; paid plans start at $23/mo. Free to self-host under Apache 2.0 with no cloud dependency. Hosted cloud: free plan with 10 mailboxes; Starter $29/mo (150 sends/day), Grow $89/mo (3,000 sends/day, CRM + API), Business $329/mo (15,000 sends/day). Annual billing saves 20%. We last checked both ends of that split on 2026-09-24. The pricing section above shows what the free tier actually covers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Warmbly a good self-hosted Email Marketing tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The most complete open-source cold email stack we have listed, but young (316 stars, launched 2026) and self-hosting puts deliverability operations on you."
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
    "reviewBody": "Warmbly packages cold email honestly as open source: Apache 2.0, self-hosted, with warmup and reply classification built in. At 316 stars and a 2026 founding date, you are the early adopter and the operator.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/warmbly/#app",
      "name": "Warmbly",
      "url": "https://martechsignal.com/tools/warmbly/"
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

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
