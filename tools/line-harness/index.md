# Line Harness review (2026): pricing, AI features, verdict


| Pros | Cons |
| --- | --- |
| &#10003; MIT licence with free self-hosting | &#10007; No hands-on test - this assessment is based on vendor documentation and the public repository |
| &#10003; AI capabilities: MCP server for Claude Code (create scenarios, monitor inbox, send broadcasts via natural language) |  |
| &#10003; Native integrations include LINE Messaging API, LINE LIFF, Google Calendar (6 listed) |  |

**What is Line Harness?**
Open-source CRM for LINE Official Accounts with step delivery, scoring, and an MCP server for AI control. It ships with MCP server for Claude Code (create scenarios, monitor inbox, send broadcasts via natural language), 589 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Line Harness cost?**
Line Harness is open source - MIT licensed and free to self-host; the public repository carries 589 stars; native integrations cover LINE Messaging API, LINE LIFF, Google Calendar. You pay in server time and maintenance, not licences.

**Is Line Harness a good self-hosted Marketing Automation tool in 2026?**
The first credible free alternative to L-Step for LINE marketing in Japan. Outside Japan there is no use case.

**What does L Harness cost to run?**
The software is MIT licensed and free to self host on Cloudflare Workers, D1, and Pages, which the project states fits inside Cloudflare&#x27;s free tier. You still pay for the LINE Official Account itself under LINE Yahoo&#x27;s free message allotment and paid plans, a custom domain, any external AI provider, and an outsourced build if you commission one. Two operational caveats from the docs: D1 queries error out once daily read or write limits are hit rather than billing overage, and L Harness Cloud is a separate managed product with no published price.

**What can an AI agent control through the MCP server?**
The bundled @line-harness/mcp-server is documented as full operation from Claude Code in natural language. Named tools cover reading conversations (list_conversations, get_conversation) so an agent can monitor unanswered chats, building messages (create_scenario, update_step), and sending (broadcast, send_message), where sending requires user confirmation. The practical loop is an agent drafting and staging step sequences and broadcasts while you approve the sends.

**What is step delivery on LINE?**
Step delivery sends a pre built sequence of LINE messages where each step waits a set delay before the next, which is how Japanese LINE marketers run onboarding and nurture. In L Harness each step carries its own delay in minutes and steps can branch, and broadcasts go to all followers, tags, or segments on a schedule with automatic queueing past 500 recipients. Rich menus can auto switch per user or tag alongside the sequence.

**What happens when a LINE account gets banned?**
The docs describe BAN detection with automatic friend migration to the next account in a pool, and a traffic pool that spreads sending across multiple LINE Official Accounts, all managed from one dashboard with per account scoping for scenarios, tags, and delivery. Worth knowing that running several accounts to spread volume sits outside what LINE&#x27;s terms are written for, so treat the pool as resilience rather than a growth lever.

- **Pricing:** Open Source
- **Category:** [Marketing Automation](/categories/marketing-automation/)
- **GitHub:** ★ 589
- **Founded:** 2026
- **HQ:** Tokyo, Japan
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Line Harness is a tool in Marketing Automation with free and open source. The catalog documents 5 AI features, 6 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Salesforce Marketing Cloud

Enterprise marketing automation on Salesforce with Agentforce AI across email, SMS, and web

Mautic

Open-source marketing automation platform with email, campaigns, and lead management

Ortto

Customer data and marketing automation platform with journeys, CDP, and AI features

Opteo

Continuous Google Ads monitoring with one-click improvements

Braze

Customer engagement platform with AI-powered real-time messaging across channels

[More Marketing Automation Tools →](/categories/marketing-automation/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Marketing Automation](/categories/marketing-automation/)
- Line Harness
## Line Harness review (2026): pricing, AI features, verdict

Open-source CRM for LINE Official Accounts with step delivery, scoring, and an MCP server for AI control

Marketing Automation · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[How we review](/methodology/) · No affiliate links

[Visit Line Harness &#8594;](https://the-harness.com/line-harness/)

Not yet scored against the rubric; scored pages show six pillars.

## Overview

L Harness (line-harness-oss) is an open-source CRM and marketing automation suite for LINE Official Accounts, built by Japanese developer Shuichi Noda and run under AI Agent Inc. It targets companies, shops, and marketing agencies in Japan that run LINE as a customer channel and want the step-delivery and segmentation features of paid tools like L-Step (from ¥20,000/mo) and L Message without the monthly license fee. The software itself costs ¥0; you deploy it to your own Cloudflare account using Workers, D1, and Pages, and the setup CLI (npx create-line-harness) handles database creation, worker deployment, LIFF app registration, and admin user creation in about five minutes. The feature list covers the standard LINE marketing playbook: step delivery with minute-level delay control and conditional branching, tag-based segment broadcasts with automatic queueing past 500 recipients, LIFF forms, rich menu switching per user or tag, behavior-based lead scoring, Google Calendar booking with webinar auto-scheduling, and an affiliate measurement system with click-to-conversion tracking and last-touch attribution. What separates it from the commercial incumbents is the AI layer. The repo ships an MCP server (@line-harness/mcp-server) so you can drive the entire system from Claude Code in natural language: create scenarios, monitor unanswered conversations, and send broadcasts. There is also a typed TypeScript SDK and webhook input/output for Stripe and Slack. BAN detection with automatic account switching is included for multi-account operators, a feature the paid tools do not touch. Pricing is genuinely simple but not free in the absolute sense. The MIT-licensed software costs nothing, and Cloudflare&#x27;s free tier covers most small deployments, but you still pay LINE&#x27;s own per-message delivery fees and any Cloudflare usage beyond the free tier. The project&#x27;s own pricing page is honest about this, and also about the fact that someone on your side owns updates and incident response. A managed version, L Harness Cloud, exists from the same developer if you want the infrastructure handled. Against the paid incumbents, L Harness wins on cost, API access (full API where L-Step and L Message expose none), and the MCP integration. It loses on support guarantees: no SLA, no phone support, and the admin UI documentation is Japanese-first, with English, Chinese, Korean, and Spanish READMEs. The repo has 568 stars and 246 commits as of August 2026, pushed within days of this writing, so it is actively maintained but still pre-1.0 (v0.21.x). Who should skip it: teams with no Cloudflare or LINE Developers setup capability, anyone who needs a vendor SLA, and marketers outside Japan where LINE is not a primary channel. For everyone else running LINE marketing, this is the first credible zero-license-cost alternative to the L-Step category.

Line Harness homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- MCP server for Claude Code (create scenarios, monitor inbox, send broadcasts via natural language)
- Typed TypeScript SDK for programmatic control
- BAN detection with automatic account switching
- Behavior-based lead scoring
- IF-THEN automation rules (7 triggers x 6 actions)
## Key Integrations

- LINE Messaging API
- LINE LIFF
- Google Calendar
- Stripe (webhook)
- Slack (webhook)
- Cloudflare Workers/D1/Pages
## Pricing

Line Harness is free to self-host under the MIT licence.

Free open-source (MIT); self-hosted on Cloudflare Workers/D1/Pages. You pay LINE delivery fees and any Cloudflare usage beyond the free tier. Managed version (L Harness Cloud) available separately.

Current plans and limits live on the [Line Harness pricing page](https://the-harness.com/line-harness/pricing/).

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

L Harness is the zero-license alternative to the paid LINE marketing tools: step delivery with minute-level delays and conditional branching, tag-based segment broadcasts, LIFF forms, rich menus, behavior-based lead scoring, Google Calendar booking, and affiliate tracking with last-touch attribution, all deployed to your own Cloudflare account in about five minutes via the setup CLI. The software itself costs nothing, so the barrier to entry is Cloudflare comfort rather than budget.

You still pay LINE&#x27;s per-message fees and any Cloudflare usage past the free tier, and operations, updates, and incident response are yours, with no SLA to lean on. Documentation is Japanese-first, the project sits pre-1.0 at v0.21.x with 568 stars, and it has existed for only months. The MCP server for Claude Code control is genuinely unusual, but the use case is strictly Japan-focused LINE marketing.

## Verdict

The first credible free alternative to L-Step for LINE marketing in Japan. Outside Japan there is no use case.

## Pros and cons

## Related concepts

- [Marketing automation](/glossary/marketing-automation/)
- [Customer journey](/glossary/customer-journey/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source CRM for LINE Official Accounts with step delivery, scoring, and an MCP server for AI control. It ships with MCP server for Claude Code (create scenarios, monitor inbox, send broadcasts via natural language), 589 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Line Harness is open source - MIT licensed and free to self-host; the public repository carries 589 stars; native integrations cover LINE Messaging API, LINE LIFF, Google Calendar. You pay in server time and maintenance, not licences.

The first credible free alternative to L-Step for LINE marketing in Japan. Outside Japan there is no use case.

The software is MIT licensed and free to self host on Cloudflare Workers, D1, and Pages, which the project states fits inside Cloudflare&#x27;s free tier. You still pay for the LINE Official Account itself under LINE Yahoo&#x27;s free message allotment and paid plans, a custom domain, any external AI provider, and an outsourced build if you commission one. Two operational caveats from the docs: D1 queries error out once daily read or write limits are hit rather than billing overage, and L Harness Cloud is a separate managed product with no published price.

The bundled @line-harness/mcp-server is documented as full operation from Claude Code in natural language. Named tools cover reading conversations (list_conversations, get_conversation) so an agent can monitor unanswered chats, building messages (create_scenario, update_step), and sending (broadcast, send_message), where sending requires user confirmation. The practical loop is an agent drafting and staging step sequences and broadcasts while you approve the sends.

Step delivery sends a pre built sequence of LINE messages where each step waits a set delay before the next, which is how Japanese LINE marketers run onboarding and nurture. In L Harness each step carries its own delay in minutes and steps can branch, and broadcasts go to all followers, tags, or segments on a schedule with automatic queueing past 500 recipients. Rich menus can auto switch per user or tag alongside the sequence.

The docs describe BAN detection with automatic friend migration to the next account in a pool, and a traffic pool that spreads sending across multiple LINE Official Accounts, all managed from one dashboard with per account scoping for scenarios, tags, and delivery. Worth knowing that running several accounts to spread volume sits outside what LINE&#x27;s terms are written for, so treat the pool as resilience rather than a growth lever.

## Similar Tools

## Related reading

- [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/)
- [Check outputs, not logs: the silent-failure audit](/blog/silent-failure-audit/)
- [NocoBase vs NocoDB vs Budibase: pick by team shape, not by spec sheet](/blog/nocobase-vs-nocodb-vs-budibase/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/line-harness/#app",
    "name": "Line Harness",
    "description": "Open-source CRM for LINE Official Accounts with step delivery, scoring, and an MCP server for AI control",
    "image": "https://martechsignal.com/og/tools/line-harness.png",
    "url": "https://martechsignal.com/tools/line-harness/",
    "sameAs": [
      "https://the-harness.com/line-harness/"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/line-harness/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-07",
    "datePublished": "2026-08-20",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://the-harness.com/line-harness/pricing/",
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
        "name": "Marketing Automation",
        "item": "https://martechsignal.com/categories/marketing-automation/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Line Harness",
        "item": "https://martechsignal.com/tools/line-harness/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Line Harness?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source CRM for LINE Official Accounts with step delivery, scoring, and an MCP server for AI control. It ships with MCP server for Claude Code (create scenarios, monitor inbox, send broadcasts via natural language), 589 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Line Harness cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Line Harness is open source - MIT licensed and free to self-host; the public repository carries 589 stars; native integrations cover LINE Messaging API, LINE LIFF, Google Calendar. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Line Harness a good self-hosted Marketing Automation tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The first credible free alternative to L-Step for LINE marketing in Japan. Outside Japan there is no use case."
        }
      },
      {
        "@type": "Question",
        "name": "What does L Harness cost to run?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The software is MIT licensed and free to self host on Cloudflare Workers, D1, and Pages, which the project states fits inside Cloudflare's free tier. You still pay for the LINE Official Account itself under LINE Yahoo's free message allotment and paid plans, a custom domain, any external AI provider, and an outsourced build if you commission one. Two operational caveats from the docs: D1 queries error out once daily read or write limits are hit rather than billing overage, and L Harness Cloud is a separate managed product with no published price."
        }
      },
      {
        "@type": "Question",
        "name": "What can an AI agent control through the MCP server?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The bundled @line-harness/mcp-server is documented as full operation from Claude Code in natural language. Named tools cover reading conversations (list_conversations, get_conversation) so an agent can monitor unanswered chats, building messages (create_scenario, update_step), and sending (broadcast, send_message), where sending requires user confirmation. The practical loop is an agent drafting and staging step sequences and broadcasts while you approve the sends."
        }
      },
      {
        "@type": "Question",
        "name": "What is step delivery on LINE?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Step delivery sends a pre built sequence of LINE messages where each step waits a set delay before the next, which is how Japanese LINE marketers run onboarding and nurture. In L Harness each step carries its own delay in minutes and steps can branch, and broadcasts go to all followers, tags, or segments on a schedule with automatic queueing past 500 recipients. Rich menus can auto switch per user or tag alongside the sequence."
        }
      },
      {
        "@type": "Question",
        "name": "What happens when a LINE account gets banned?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The docs describe BAN detection with automatic friend migration to the next account in a pool, and a traffic pool that spreads sending across multiple LINE Official Accounts, all managed from one dashboard with per account scoping for scenarios, tags, and delivery. Worth knowing that running several accounts to spread volume sits outside what LINE's terms are written for, so treat the pool as resilience rather than a growth lever."
        }
      }
    ]
  }
]
```
