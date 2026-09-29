# WaCRM review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free open-source and self-hosted with BYO OpenAI or Anthropic keys as the stated run cost (the vendor pricing page: [vendor site](https://wacrm.tech), verified 2026-09-07). |
| Feature depth | 6/10 | Shared inbox, sales pipelines, broadcasts and automations cover the WhatsApp CRM loop (vendor documentation: [vendor site](https://wacrm.tech), verified 2026-09-28). |
| Integrations | 6/10 | Meta WhatsApp Cloud API, Supabase, OpenAI, Anthropic, pgvector and MCP clients documented (vendor documentation: [vendor site](https://wacrm.tech), verified 2026-09-28). |
| AI capability | 6/10 | Grounded auto-reply with human handoff over pgvector or Postgres full-text retrieval (vendor documentation: [vendor site](https://wacrm.tech), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with 2.3k GitHub stars and full self-hosting (the source repository: [repository](https://github.com/ArnasDon/wacrm), verified 2026-09-28). |
| Operational maturity | 3/10 | Founded 2026 at 2.3k stars as an early self-hosted project (vendor documentation: [vendor site](https://wacrm.tech), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: AI reply assistant (bring your own OpenAI or Anthropic key) |  |
| ✓ Active public repository (2,285 GitHub stars counted at last check) |  |
| ✓ Native integrations include Meta WhatsApp Cloud API, Supabase, OpenAI (8 listed) |  |

**What is WaCRM?**
WaCRM: Self-hostable CRM for WhatsApp with shared inbox, sales pipelines, broadcasts, and automations. WaCRM ships with AI reply assistant (bring your own OpenAI or Anthropic key). The public repository carries 2,285 stars.

**How much does WaCRM cost?**
WaCRM is open source - MIT licensed and free to self-host; the public repository carries 2,285 stars; native integrations cover Meta WhatsApp Cloud API, Supabase, OpenAI. You pay in server time and maintenance, not licences.

**Is WaCRM a good self-hosted CRM tool in 2026?**
A legitimate starting point for WhatsApp-first sales teams that can run Node and Supabase; the official API brings template approvals and Meta vetting along with the delivery tracking.

**Is WaCRM free?**
The code is MIT-licensed and free to fork, modify, and ship, with no user or record limits. The costs around it are yours: a Supabase project, hosting, and WhatsApp Business API usage billed by Meta. The docs recommend Hostinger's managed Node.js hosting, where plans start at a few dollars a month, though the README notes it runs anywhere Node.js does, including Vercel, Railway, or your own VPS. The AI reply assistant has no per-seat fee because you bring your own OpenAI or Anthropic key.

**Does WaCRM use the official WhatsApp API or WhatsApp Web?**
The official one. Both the README and the docs site state that WaCRM talks to the Meta WhatsApp Business Cloud API using a phone number ID and access token you supply, and that any Meta-approved BSP exposing the same endpoints works. The practical consequences are delivery and read tracking on broadcasts, plus template management inside the app with live Meta approval status, balanced by a requirement that your number be approved by Meta and that broadcasts use Meta-approved templates.

**Does WaCRM have AI features?**
Yes. The AI reply assistant uses your own OpenAI or Anthropic key, stored encrypted, to draft one-click replies in the inbox or run an auto-reply bot with a per-conversation cap and human handoff, optionally grounded in a knowledge base retrieved with Postgres full-text search or pgvector when an embeddings key is set. There is also an MCP server so Claude, Cursor, and similar assistants can read the CRM, read-only by default with writes as an opt-in.

**Can WaCRM run multiple WhatsApp numbers?**
One phone number per user account: the schema enforces a unique phone_number_id and the API returns a 409 if you try to attach a number that is already claimed. Shared inbox access is handled by adding multiple humans to one account with owner, admin, agent, or viewer roles rather than by attaching several numbers to a team. If you need several numbers, run several instances, which the Docker setup supports but does not orchestrate for you.

**What breaks if I skip the cron setup in WaCRM?**
Automations and flows never run. The container schedules nothing internally, so the docs have you point an external cron at /api/automations/cron and /api/flows/cron with an x-cron-secret header; without it those endpoints return 503 and your auto replies and flows silently do not fire. From the inbox it looks like a broken WhatsApp connection, so check the cron before you debug the Cloud API.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 2285
- **Founded:** 2026
- **HQ:** Open source
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** WaCRM is a tool in CRM with free and open source. The catalog documents 4 AI features, 8 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

DeskcommCRM

Self-hosted open-source CRM with AI agents that sell through WhatsApp

Google Ads + Meta Ads + GA4 MCP

MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4

React Email Editor

Drag-n-Drop Email Editor Component for React.js

BillionMail

Open-source mail server, newsletter, and email marketing platform, fully self-hosted and free

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- WaCRM
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## WaCRM review (2026): pricing, AI features, verdict

Self-hostable CRM for WhatsApp with shared inbox, sales pipelines, broadcasts, and automations

CRM · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-26

[Visit WaCRM →](https://wacrm.tech)

[How we review](/methodology/) · No affiliate links

[Visit WaCRM →](https://wacrm.tech)

## MartechSignal Score: 38/60

WaCRM is self-hosted WhatsApp CRM with grounded auto-replies and human handoff, MIT at 2.3k stars. BYO model keys keep the AI costs yours and the data local.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

WaCRM is a self-hostable CRM template built on the official Meta WhatsApp Business Cloud API, and it is explicit about what that means: the README calls it 'a template, not a product, ' licensed MIT under the instruction 'fork it, brand it, host it.' You get the code, your own Supabase project, your own domain, and your own data. The feature set covers WhatsApp-first sales: a shared inbox with per-conversation assignment, round-robin distribution, and internal notes; a contact hub with tags, custom fields, CSV import, and deduplication; unlimited Kanban pipelines with deals linked to conversations; broadcast campaigns using Meta-approved templates with delivery, read, and reply tracking; and a no-code automation builder whose triggers include inbound messages, new contacts, tag changes, keywords, and schedules. Two additions move it past the narrower project it was a year ago. An AI reply assistant takes your own OpenAI or Anthropic key, stored encrypted, drafts one-click replies in the inbox, and can run an auto-reply bot with a per-conversation cap and human handoff, grounded in an optional knowledge base that uses Postgres full-text or pgvector semantic retrieval. A public REST API with scoped, revocable keys and an MCP server let external tools and assistants read the CRM, read-only by default with writes as an opt-in. The stack is Next.js 16, React 19, TypeScript, and Tailwind v4 on Supabase. Getting there takes real setup: fork the repo, run npm install, set Supabase credentials plus an encryption key, run migrations, then paste a Meta phone number ID and access token and expose an HTTPS webhook. Because it uses the official API, broadcasts are limited to Meta-approved templates and your number must be approved by Meta first. For a small team in a WhatsApp-heavy market that is a fair trade; for anyone needing email, a dialer, or forecasting, it is the wrong tool.

WaCRM homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI reply assistant (bring your own OpenAI or Anthropic key)
- Auto-reply bot with human handoff
- Knowledge base grounding (pgvector or Postgres full-text)
- MCP server for Claude and Cursor
## Key Integrations

- Meta WhatsApp Cloud API
- Supabase
- OpenAI
- Anthropic
- pgvector
- MCP (Claude, Cursor)
- Docker
- Hostinger
## How to install

- Fork github.com/ArnasDon/wacrm, then clone your fork and run npm install. The getting-started guide assumes Node.js 20+ and npm are already installed.
- Copy .env.local.example to .env.local. The docs state that npm run dev will not start until at least NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY are set.
- Generate the encryption key for WhatsApp token storage with node -e "console.log(require('crypto').randomBytes(32).toString('hex'))" and paste it into ENCRYPTION_KEY. The docs warn not to change it later, because stored tokens become unreadable.
- Create a Supabase project and run the migrations per docs/supabase-setup, then connect a WhatsApp number in Settings using your Meta phone number ID and access token, with an HTTPS webhook configured (docs/whatsapp-setup).
- Run npm run dev, open http://localhost:3000, and create an account at /signup. Docker Compose is documented in docs/docker.md, and Hostinger managed Node.js hosting is the recommended one-click path, though the README notes it runs anywhere Node.js does.
## Requirements

Node.js 20+, your own Supabase project, a Meta-approved WhatsApp Business number with a Cloud API access token and phone number ID, and an HTTPS webhook. You pay your own hosting and WhatsApp Business API usage.

## Best for

Small teams in WhatsApp-heavy markets that want a shared inbox, pipelines, and broadcasts they can fork, brand, and host, with AI replies running on their own OpenAI or Anthropic key.

## Not for

Teams that need email, a dialer, forecasting, or multi-channel outreach, and anyone who cannot get a WhatsApp Business number approved by Meta or does not want to maintain a fork.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

WaCRM is a fork-and-own template rather than a product you install, and the README is blunt about the consequences: 'your code, your Supabase project, your domain, your data.' The contributing policy follows the same logic, saying feature PRs often belong in your fork rather than upstream, so plan to carry your customizations yourself. Researched from the repository and the docs site. Not a hands-on review.

The channel decision defines the tool. It talks to the official Meta Cloud API, which brings template approvals, delivery and read tracking, and an HTTPS webhook requirement, and rules out the casual WhatsApp Web wrapper experience. The docs' own framing is honest about the gate: most teams are live in under 30 minutes once their WhatsApp Business number has been approved by Meta. Approval is the long pole, not the deploy.

Setup is documented to a level most template projects never reach. The getting-started guide states the minimum environment, gives a one-line command to generate the 64-character encryption key used for token storage, and warns that rotating it makes stored WhatsApp tokens unreadable. Docker and Hostinger deployment paths both exist.

Security posture is specified rather than hand-waved: WhatsApp access tokens encrypted at rest, row-level security throughout, HMAC-verified webhooks, CSP, and rate limiting. For a tool that holds WhatsApp credentials for a whole sales team, that list is the part worth reading before you fork.

## Verdict

A legitimate starting point for WhatsApp-first sales teams that can run Node and Supabase; the official API brings template approvals and Meta vetting along with the delivery tracking.

## Pros and cons

## Related concepts

- [CRM](/glossary/crm/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
- [Customer journey](/glossary/customer-journey/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

WaCRM: Self-hostable CRM for WhatsApp with shared inbox, sales pipelines, broadcasts, and automations. WaCRM ships with AI reply assistant (bring your own OpenAI or Anthropic key). The public repository carries 2,285 stars.

WaCRM is open source - MIT licensed and free to self-host; the public repository carries 2,285 stars; native integrations cover Meta WhatsApp Cloud API, Supabase, OpenAI. You pay in server time and maintenance, not licences.

A legitimate starting point for WhatsApp-first sales teams that can run Node and Supabase; the official API brings template approvals and Meta vetting along with the delivery tracking.

The code is MIT-licensed and free to fork, modify, and ship, with no user or record limits. The costs around it are yours: a Supabase project, hosting, and WhatsApp Business API usage billed by Meta. The docs recommend Hostinger's managed Node.js hosting, where plans start at a few dollars a month, though the README notes it runs anywhere Node.js does, including Vercel, Railway, or your own VPS. The AI reply assistant has no per-seat fee because you bring your own OpenAI or Anthropic key.

The official one. Both the README and the docs site state that WaCRM talks to the Meta WhatsApp Business Cloud API using a phone number ID and access token you supply, and that any Meta-approved BSP exposing the same endpoints works. The practical consequences are delivery and read tracking on broadcasts, plus template management inside the app with live Meta approval status, balanced by a requirement that your number be approved by Meta and that broadcasts use Meta-approved templates.

Yes. The AI reply assistant uses your own OpenAI or Anthropic key, stored encrypted, to draft one-click replies in the inbox or run an auto-reply bot with a per-conversation cap and human handoff, optionally grounded in a knowledge base retrieved with Postgres full-text search or pgvector when an embeddings key is set. There is also an MCP server so Claude, Cursor, and similar assistants can read the CRM, read-only by default with writes as an opt-in.

One phone number per user account: the schema enforces a unique phone_number_id and the API returns a 409 if you try to attach a number that is already claimed. Shared inbox access is handled by adding multiple humans to one account with owner, admin, agent, or viewer roles rather than by attaching several numbers to a team. If you need several numbers, run several instances, which the Docker setup supports but does not orchestrate for you.

Automations and flows never run. The container schedules nothing internally, so the docs have you point an external cron at /api/automations/cron and /api/flows/cron with an x-cron-secret header; without it those endpoints return 503 and your auto replies and flows silently do not fire. From the inbox it looks like a broken WhatsApp connection, so check the cron before you debug the Cloud API.

## Similar Tools

## Related reading

- [Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough](/blog/salesforce-claude-commerce-cloud-agentforce/)
- [Deliverability in the AI-spam Era Is a Content Problem, Not an IT Problem](/blog/deliverability-ai-spam-content-problem/)
- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
### Quick Facts

### Pricing

Free open-source; self-hosted

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/wacrm/#app",
    "name": "WaCRM",
    "description": "Self-hostable CRM for WhatsApp with shared inbox, sales pipelines, broadcasts, and automations",
    "image": "https://martechsignal.com/og/tools/wacrm.png",
    "url": "https://martechsignal.com/tools/wacrm/",
    "sameAs": [
      "https://wacrm.tech"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/wacrm/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-26",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://wacrm.tech",
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
        "name": "CRM",
        "item": "https://martechsignal.com/categories/crm/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "WaCRM",
        "item": "https://martechsignal.com/tools/wacrm/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is WaCRM?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "WaCRM: Self-hostable CRM for WhatsApp with shared inbox, sales pipelines, broadcasts, and automations. WaCRM ships with AI reply assistant (bring your own OpenAI or Anthropic key). The public repository carries 2,285 stars."
        }
      },
      {
        "@type": "Question",
        "name": "How much does WaCRM cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "WaCRM is open source - MIT licensed and free to self-host; the public repository carries 2,285 stars; native integrations cover Meta WhatsApp Cloud API, Supabase, OpenAI. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is WaCRM a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A legitimate starting point for WhatsApp-first sales teams that can run Node and Supabase; the official API brings template approvals and Meta vetting along with the delivery tracking."
        }
      },
      {
        "@type": "Question",
        "name": "Is WaCRM free?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The code is MIT-licensed and free to fork, modify, and ship, with no user or record limits. The costs around it are yours: a Supabase project, hosting, and WhatsApp Business API usage billed by Meta. The docs recommend Hostinger's managed Node.js hosting, where plans start at a few dollars a month, though the README notes it runs anywhere Node.js does, including Vercel, Railway, or your own VPS. The AI reply assistant has no per-seat fee because you bring your own OpenAI or Anthropic key."
        }
      },
      {
        "@type": "Question",
        "name": "Does WaCRM use the official WhatsApp API or WhatsApp Web?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The official one. Both the README and the docs site state that WaCRM talks to the Meta WhatsApp Business Cloud API using a phone number ID and access token you supply, and that any Meta-approved BSP exposing the same endpoints works. The practical consequences are delivery and read tracking on broadcasts, plus template management inside the app with live Meta approval status, balanced by a requirement that your number be approved by Meta and that broadcasts use Meta-approved templates."
        }
      },
      {
        "@type": "Question",
        "name": "Does WaCRM have AI features?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. The AI reply assistant uses your own OpenAI or Anthropic key, stored encrypted, to draft one-click replies in the inbox or run an auto-reply bot with a per-conversation cap and human handoff, optionally grounded in a knowledge base retrieved with Postgres full-text search or pgvector when an embeddings key is set. There is also an MCP server so Claude, Cursor, and similar assistants can read the CRM, read-only by default with writes as an opt-in."
        }
      },
      {
        "@type": "Question",
        "name": "Can WaCRM run multiple WhatsApp numbers?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "One phone number per user account: the schema enforces a unique phone_number_id and the API returns a 409 if you try to attach a number that is already claimed. Shared inbox access is handled by adding multiple humans to one account with owner, admin, agent, or viewer roles rather than by attaching several numbers to a team. If you need several numbers, run several instances, which the Docker setup supports but does not orchestrate for you."
        }
      },
      {
        "@type": "Question",
        "name": "What breaks if I skip the cron setup in WaCRM?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Automations and flows never run. The container schedules nothing internally, so the docs have you point an external cron at /api/automations/cron and /api/flows/cron with an x-cron-secret header; without it those endpoints return 503 and your auto replies and flows silently do not fire. From the inbox it looks like a broken WhatsApp connection, so check the cron before you debug the Cloud API."
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
    "reviewBody": "WaCRM is self-hosted WhatsApp CRM with grounded auto-replies and human handoff, MIT at 2.3k stars. BYO model keys keep the AI costs yours and the data local.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/wacrm/#app",
      "name": "WaCRM",
      "url": "https://martechsignal.com/tools/wacrm/"
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
