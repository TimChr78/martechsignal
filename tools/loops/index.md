# Loops review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 5/10 | Free up to 1,000 contacts and 4,000 sends per rolling 30 days published; paid plans are contact-based with no listed prices (the vendor pricing page: [pricing page](https://loops.so/pricing), verified 2026-09-28). |
| Feature depth | 6/10 | Marketing, product and transactional email in one tool cover the SaaS messaging stack (vendor documentation: [vendor site](https://loops.so), verified 2026-09-28). |
| Integrations | 6/10 | Stripe, Segment, Zapier, PostHog, Supabase, Clerk, Fivetran and Make documented plus an API (vendor documentation: [vendor site](https://loops.so), verified 2026-09-28). |
| AI capability | 5/10 | LLM email translation, an AI workflow builder and an MCP server for agent access (vendor documentation: [vendor site](https://loops.so), verified 2026-09-28). |
| Openness | 3/10 | Closed SaaS with API and MCP access (vendor documentation: [vendor site](https://loops.so), verified 2026-09-28). |
| Operational maturity | 5/10 | Founded 2022 with a developer-market product shape (vendor documentation: [vendor site](https://loops.so), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ AI capabilities: LLM email translation | ✗ Closed source - no self-hosting option |
| ✓ Native integrations include Stripe, Segment, Zapier (8 listed) |  |
| ✓ Free tier to evaluate before committing (Free up to 1,000 subscribed contacts and 4,000 sends per rolling 30 days) |  |

**What is Loops?**
Loops: Email marketing for SaaS: marketing, product, and transactional email in one tool. Loops ships with LLM email translation. This page documents 8 integrations.

**How much does Loops cost?**
Loops has a free tier, so you can run a real evaluation before paying. Free up to 1,000 subscribed contacts and 4,000 sends per rolling 30 days; paid plans are contact-based with unlimited sends and no published list prices. We last checked the plan structure on 2026-09-07; paid tiers mainly raise limits rather than unlocking core features.

**Is Loops worth it past the free tier?**
A focused, developer-friendly email platform for SaaS: strong API and agent access, honest scope, email only, and paid pricing you calculate rather than read.

**Does Loops support custom HTML email?**
No. Loops does not accept custom HTML emails; content is created in its editor or in LMX, the platform's XML-based markup, and reused through a Components API so edits cascade into every email that uses the component. Imports are supported from MJML, Emailify, and Email Love. The docs include a page titled Why we don't support HTML emails explaining the reasoning, so teams with strict design-control requirements should test the editor against their needs first.

**How does Loops pricing work as your list grows?**
It is contact-based, not send-based: Loops charges on subscribed contacts and does not charge separately for sending. The free plan covers 0 to 1,000 subscribed contacts and up to 4,000 sends in any rolling 30 days, with all features included and a small Powered by Loops footer. Paid plans remove the branding, raise throughput to 1,000 emails per second, and lift the send cap entirely, with no per-seat fees. Loops publishes no dollar figures on its pricing page; you move a slider to estimate cost, and unsubscribed contacts do not count toward the limit.

**Can AI coding agents connect to Loops?**
Yes, and it is documented as a first-class surface rather than a bolt-on. Loops publishes an MCP server so any MCP client can read and write contacts, events, and content, along with agent skills for Claude Code, Codex, and Cursor, setup and migrate CLI commands, and a Claude Connector added in August 2026. The REST API underneath exposes roughly 70 endpoints with a public OpenAPI spec at app.loops.so/openapi.json. Separately, an in-app AI agent can assemble a workflow from a prompt, and LLM Translation translates an email branch in one click.

- **Pricing:** Freemium
- **Category:** [Email Marketing](/categories/email-marketing/)
- **Founded:** 2022
- **HQ:** Washington, DC, USA
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Loops is a tool in Email Marketing with a free tier. The catalog documents 3 AI features, 8 integrations and a public API. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Notifuse

Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations

Resend

Developer-first email API built around React Email, batch sending, and agent tooling

Customer.io

Data-driven messaging platform for automated email, push, SMS, and in-app messages

Postmark

Transactional email API with separated message streams, an MCP server, and published delivery numbers

[More Email Marketing Tools →](/categories/email-marketing/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- Loops
Re-check pending: pricing last verified 2026-09-07 (23 days ago).

## Loops review (2026): pricing, AI features, verdict

Email marketing for SaaS: marketing, product, and transactional email in one tool

Email Marketing · Freemium Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-29

[Visit Loops →](https://loops.so)

[How we review](/methodology/) · No affiliate links

[Visit Loops →](https://loops.so)

## MartechSignal Score: 30/60

Loops is SaaS email done in one tool: marketing, product and transactional with an MCP server for agents. Free to 1,000 contacts; paid pricing is contact-based and quoted rather than listed.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Loops is an email platform built for SaaS companies, covering marketing campaigns, product announcements, and transactional email from one dashboard, and deliberately nothing else: there is no SMS, no push, and no in-app messaging. Founded in 2022 by Chris Frantz and Adam Kaczmarek, it went through Y Combinator's W22 batch, and the site names Linear, Perplexity, Framer, Clerk, Reuters, Granola, and Sketch among its customers. Automation was rebuilt and renamed Workflows in May 2026, replacing the original loop builder: workflows trigger on contact property changes, new contacts, or external events, branch on contact properties, and pause on timers. Experiments, added in June 2025, handle split testing. Guardian, introduced in September 2025, runs pre-send checks that flag misplaced variables, missing button links, and missing fallbacks. Deliverability handling is documented rather than claimed: hard bounces and complaints are suppressed, temporary failures retried, and large sends rate-limited. One constraint surprises people: Loops does not accept custom HTML email. Content is built in the editor or in LMX, an XML-based markup, with a Components API that cascades edits into every email using the component; MJML, Emailify, and Email Love files can be imported. Developers get roughly 70 REST endpoints with an OpenAPI spec, official SDKs for JavaScript, Go, Nuxt, PHP, and Ruby, a CLI, webhooks, SMTP for transactional sending, and an MCP server so coding agents can read and write contacts, events, and content. LLM translation, added in January 2026, duplicates an email branch and translates it in one click. Pricing is contact-based: the free plan covers up to 1,000 subscribed contacts and 4,000 sends per rolling 30 days with all features included; paid plans add unlimited sends, no Loops branding, and 1,000 emails per second, with no per-seat fees and no published list prices.

Loops homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- LLM email translation
- AI workflow builder
- MCP server for agent access
## Key Integrations

- Stripe
- Segment
- Zapier
- PostHog
- Supabase
- Clerk
- Fivetran
- Make
## Pricing

Loops is freemium, with a free tier to start.

Free up to 1,000 subscribed contacts and 4,000 sends per rolling 30 days; paid plans are contact-based with unlimited sends and no published list prices

Current plans and limits live on the [Loops pricing page](https://loops.so/pricing).

## How to install

- Sign up at loops.so with no credit card; the free plan includes all features up to 1,000 subscribed contacts and 4,000 sends per rolling 30 days.
- Verify a sending domain before production sends; the docs carry around 15 deliverability guides covering DKIM, DMARC, inbox placement, sender reputation, and subdomains.
- Get contacts in via CSV upload, simple or custom forms, the REST API, or the official Segment integration.
- For API use, create a key in the dashboard; the OpenAPI spec lives at app.loops.so/openapi.json and official SDKs exist for JavaScript, Go, Nuxt, PHP, and Ruby, plus a Go CLI at github.com/loops-so/cli.
- Agents connect over MCP (the docs publish a Claude Connector guide), and transactional sending can also run over SMTP from Django, Laravel, Rails, or Supabase.
## Requirements

A verified sending domain for production and an API key for programmatic use; Loops is hosted SaaS with nothing to self-host. Unsubscribed contacts do not count toward plan limits.

## Best for

SaaS teams that want marketing, product announcement, and transactional email in one modern tool driven from the API: contact-based pricing, all features on the free tier, and agent access over MCP make it a natural fit for developer-led startups sending onboarding sequences and lifecycle email.

## Not for

Teams that need custom HTML email (not accepted; content is editor or LMX based), multi-channel programs needing SMS, push, or in-app messaging, or buyers who require published price lists before signing up, since paid figures come from the on-site calculator only.

## Review notes

Assessed from loops.so, loops.so/docs, and loops.so/changelog; we have no Loops account and have not sent through it. The changelog is the best evidence of momentum: 15 entries between February 2025 and August 2026, including Workflows (May 2026), Goals (July 2026), and a Workflows API with a Claude Connector (August 2026).

The product correction that matters against our earlier record: none of the previously listed AI features (subject line suggestions, content generation, send-time optimization) appear anywhere in the docs. What is documented is LLM Translation for one-click email translation (January 2026), an AI agent that assembles workflows from a prompt, and an MCP server plus skills for coding agents. Our earlier integration list named Slack, Shopify, and HubSpot, none of which appear in the documented integration index; the documented set is Stripe, Polar, Auth0, Clerk, Supabase, PostHog, RudderStack, Segment, Clay, Fivetran, Make, Integrately, Zapier, and others.

The email-only scope is confirmed and stated plainly: no SMS, push, or in-app. Combined with the no-custom-HTML policy and contact-based pricing, the product is narrow by design, and the docs are unusually explicit about what it will not do.

Where it sits against incumbents: Customer.io and Userlist remain the closest comparisons for SaaS lifecycle email. Loops differentiates on the free tier (all features, 1,000 contacts), the 70-endpoint API with a public OpenAPI spec, and agent tooling (MCP, CLI, skills) that most competitors in this bracket do not document.

## Verdict

A focused, developer-friendly email platform for SaaS: strong API and agent access, honest scope, email only, and paid pricing you calculate rather than read.

## Pros and cons

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Loops: Email marketing for SaaS: marketing, product, and transactional email in one tool. Loops ships with LLM email translation. This page documents 8 integrations.

Loops has a free tier, so you can run a real evaluation before paying. Free up to 1,000 subscribed contacts and 4,000 sends per rolling 30 days; paid plans are contact-based with unlimited sends and no published list prices. We last checked the plan structure on 2026-09-07; paid tiers mainly raise limits rather than unlocking core features.

A focused, developer-friendly email platform for SaaS: strong API and agent access, honest scope, email only, and paid pricing you calculate rather than read.

No. Loops does not accept custom HTML emails; content is created in its editor or in LMX, the platform's XML-based markup, and reused through a Components API so edits cascade into every email that uses the component. Imports are supported from MJML, Emailify, and Email Love. The docs include a page titled Why we don't support HTML emails explaining the reasoning, so teams with strict design-control requirements should test the editor against their needs first.

It is contact-based, not send-based: Loops charges on subscribed contacts and does not charge separately for sending. The free plan covers 0 to 1,000 subscribed contacts and up to 4,000 sends in any rolling 30 days, with all features included and a small Powered by Loops footer. Paid plans remove the branding, raise throughput to 1,000 emails per second, and lift the send cap entirely, with no per-seat fees. Loops publishes no dollar figures on its pricing page; you move a slider to estimate cost, and unsubscribed contacts do not count toward the limit.

Yes, and it is documented as a first-class surface rather than a bolt-on. Loops publishes an MCP server so any MCP client can read and write contacts, events, and content, along with agent skills for Claude Code, Codex, and Cursor, setup and migrate CLI commands, and a Claude Connector added in August 2026. The REST API underneath exposes roughly 70 endpoints with a public OpenAPI spec at app.loops.so/openapi.json. Separately, an in-app AI agent can assemble a workflow from a prompt, and LLM Translation translates an email branch in one click.

## Similar Tools

## Related reading

- [Deliverability in the AI-spam Era Is a Content Problem, Not an IT Problem](/blog/deliverability-ai-spam-content-problem/)
- [Microsoft Just Removed the Steering Wheel From Search Ads](/blog/microsoft-search-ads-steering-wheel/)
- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/loops/#app",
    "name": "Loops",
    "description": "Email marketing for SaaS: marketing, product, and transactional email in one tool",
    "image": "https://martechsignal.com/og/tools/loops.png",
    "url": "https://martechsignal.com/tools/loops/",
    "sameAs": [
      "https://loops.so"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/loops/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-29",
    "datePublished": "2026-07-27"
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
        "name": "Loops",
        "item": "https://martechsignal.com/tools/loops/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Loops?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Loops: Email marketing for SaaS: marketing, product, and transactional email in one tool. Loops ships with LLM email translation. This page documents 8 integrations."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Loops cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Loops has a free tier, so you can run a real evaluation before paying. Free up to 1,000 subscribed contacts and 4,000 sends per rolling 30 days; paid plans are contact-based with unlimited sends and no published list prices. We last checked the plan structure on 2026-09-07; paid tiers mainly raise limits rather than unlocking core features."
        }
      },
      {
        "@type": "Question",
        "name": "Is Loops worth it past the free tier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A focused, developer-friendly email platform for SaaS: strong API and agent access, honest scope, email only, and paid pricing you calculate rather than read."
        }
      },
      {
        "@type": "Question",
        "name": "Does Loops support custom HTML email?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. Loops does not accept custom HTML emails; content is created in its editor or in LMX, the platform's XML-based markup, and reused through a Components API so edits cascade into every email that uses the component. Imports are supported from MJML, Emailify, and Email Love. The docs include a page titled Why we don't support HTML emails explaining the reasoning, so teams with strict design-control requirements should test the editor against their needs first."
        }
      },
      {
        "@type": "Question",
        "name": "How does Loops pricing work as your list grows?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "It is contact-based, not send-based: Loops charges on subscribed contacts and does not charge separately for sending. The free plan covers 0 to 1,000 subscribed contacts and up to 4,000 sends in any rolling 30 days, with all features included and a small Powered by Loops footer. Paid plans remove the branding, raise throughput to 1,000 emails per second, and lift the send cap entirely, with no per-seat fees. Loops publishes no dollar figures on its pricing page; you move a slider to estimate cost, and unsubscribed contacts do not count toward the limit."
        }
      },
      {
        "@type": "Question",
        "name": "Can AI coding agents connect to Loops?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, and it is documented as a first-class surface rather than a bolt-on. Loops publishes an MCP server so any MCP client can read and write contacts, events, and content, along with agent skills for Claude Code, Codex, and Cursor, setup and migrate CLI commands, and a Claude Connector added in August 2026. The REST API underneath exposes roughly 70 endpoints with a public OpenAPI spec at app.loops.so/openapi.json. Separately, an in-app AI agent can assemble a workflow from a prompt, and LLM Translation translates an email branch in one click."
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
    "reviewBody": "Loops is SaaS email done in one tool: marketing, product and transactional with an MCP server for agents. Free to 1,000 contacts; paid pricing is contact-based and quoted rather than listed.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/loops/#app",
      "name": "Loops",
      "url": "https://martechsignal.com/tools/loops/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 30,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/tools/loops/", "breadcrumb": {"@id": "https://martechsignal.com/tools/loops/#breadcrumb"}, "dateModified": "2026-09-29"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
