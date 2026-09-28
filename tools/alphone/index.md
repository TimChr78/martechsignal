# AlphOne review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 5/10 | Self-hosting is free as stated in the README, but there is no pricing page, no published commercial or support terms, and the project is early-stage (the vendor pricing page). |
| Feature depth | 4/10 | Contacts, tasks, an importer, configurable fields and a WhatsApp Cloud API channel cover core CRM plus a little more, and the plugin catalogue is still young (vendor documentation). |
| Integrations | 4/10 | GraphQL and REST APIs plus webhooks, an MCP server, a community n8n node and a WhatsApp Cloud API plugin cover programmatic access, with no marketplace behind them (vendor documentation). |
| AI capability | 6/10 | AlphOne speaks MCP from version 0.9.0 so agent clients can query tasks, contacts and fields through a defined tool list and agent-created records are marked, but there are no built-in AI features (vendor documentation). |
| Openness | 7/10 | The backend is source-available under Elastic License 2.0 with an AGPLv3 frontend: free to self-host, not OSI open source, and forbidden as a hosted service offered to third parties (the source repository). |
| Operational maturity | 3/10 | Founded in 2026 with 176 GitHub stars and an active commit log, which places it at young-project maturity with no company or support track record behind it (vendor documentation). |


| Pros | Cons |
| --- | --- |
| &#10003; Elastic License 2.0 licence with free self-hosting | &#10007; Young project (176 GitHub stars) - smaller community and plugin ecosystem |
| &#10003; API access for custom integrations |  |
| &#10003; API access for custom integrations |  |

**What is AlphOne?**
Plugin-first CRM (source-available, Elastic 2.0) written in Go. It ships with 176 GitHub stars, an API for custom integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does AlphOne cost?**
AlphOne is source-available rather than open source - Elastic License 2.0 licensed and free to self-host; the public repository carries 176 stars. Check the licence terms before commercial use.

**Is AlphOne a good self-hosted CRM tool in 2026?**
An API-first CRM built to be driven by n8n and AI agents rather than replace them. Early-stage, split-licensed, and best judged as a foundation for an automated stack.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 176
- **Founded:** 2026
- **HQ:** Open source
- **API:** Yes
- **Last verified:** 2026-09-06

**Verdict:** AlphOne is a tool in CRM with free and open source. The catalog documents a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-06. This is a desk review, not a hands-on test. Desk-reviewed

DeskcommCRM

Self-hosted open-source CRM with AI agents that sell through WhatsApp

Django CRM

Multi-tenant open-source CRM on Django with leads, campaigns, and self-hosting

React Email Editor

Drag-n-Drop Email Editor Component for React.js

Notifuse

Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- AlphOne
Re-check pending: pricing last verified 2026-09-06 (22 days ago).

## AlphOne review (2026): pricing, AI features, verdict

Plugin-first CRM (source-available, Elastic 2.0) written in Go

CRM · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-06

[Visit AlphOne &#8594;](https://github.com/gopherium/AlphOne)

[How we review](/methodology/) · No affiliate links

[Visit AlphOne &#8594;](https://github.com/gopherium/AlphOne)

## MartechSignal Score: 29/60

An API-first CRM designed to be driven by n8n and AI agents, with MCP support that older CRMs lack. It is early: thin features, a small community and a split license that rules out resale, so judge it as a foundation rather than a finished product.

Scored 2026-09-26 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

AlphOne is a plugin-first CRM with a Go backend exposing both GraphQL and REST APIs, a React single-page frontend, and a design that treats automation as an external concern: there is no built-in rules engine, because everything the UI does is available over HTTP with a token. Features ship as plugins with their own repositories; the current in-repo set covers fields, an importer, and a WhatsApp Cloud API channel that lands customer conversations in a shared inbox attached to the right contact. For marketing ops the notable part is how deliberately the project meets agents where they already work: it speaks MCP (Model Context Protocol) natively, so any MCP client can ask about today&#x27;s tasks or waiting contacts, and there is a community n8n node (n8n-nodes-alphone) with documented end-to-end workflows, such as an inbound WhatsApp message creating a write-back task on the right contact. The same API-first logic works with Activepieces, Windmill, Node-RED, or a cron job with curl. Licensing needs a look before you commit: the Go backend and SQL migrations carry the Elastic License 2.0, which forbids offering AlphOne to third parties as a hosted service, while the frontend, tests, and docs are AGPLv3. That split is workable for a company extending a self-hosted CRM in Go, and rules out SaaS vendors reselling hosted CRM. At 176 stars the community is early-stage, but the repo ships with code coverage, sqlc, GraphQL codegen, and an active commit log. Evaluate it as an API-first foundation for an n8n- or agent-driven stack, not a finished SuiteCRM replacement.

AlphOne homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## Pricing

AlphOne is free to self-host under the Elastic License 2.0 licence.

Free to self-host. Split license: backend under Elastic License 2.0 (source-available, not OSI open source), check terms for commercial use.

Current plans and limits live on the [AlphOne pricing page](https://github.com/gopherium/AlphOne).

## Best for

Marketing ops teams that already run n8n or AI agents and want a CRM those tools can drive natively - MCP support and the n8n community node make AlphOne addressable without middleware.

## Not for

Teams wanting a finished, feature-complete CRM on day one (the plugin catalogue is young), and SaaS vendors reselling hosted CRM - the Elastic License 2.0 backend forbids exactly that.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

The README is short and the documentation lives on a separate docs site, which tells you where the project is in its lifecycle: the code and setup path are real (Go backend, React SPA, plugin repositories per feature), but the marketing surface is minimal. The plugin-first model means most evaluation effort goes into reading the plugin catalogue rather than feature pages. Claims here rest on the repository itself.

From the documentation: AI access is native rather than bolted on. AlphOne speaks MCP from version 0.9.0, so any MCP client can query tasks, contacts, and fields through a defined tool list. The catch is the license, not the tech: Elastic License 2.0 on the backend means no offering AlphOne as a hosted or managed service to third parties, while the frontend carries AGPLv3. If your use case is internal CRM on your own infrastructure, neither restriction bites. If you build client solutions, read both licenses before writing any code against the API.

The automation story is the differentiator and it is documented, not implied: AlphOne has no built-in rules engine, and the docs say so plainly. Everything the frontend does runs over the same HTTP API a token unlocks, so an external engine drives the CRM the way the UI does. The docs walk an n8n workflow end to end - an inbound WhatsApp message creating a &#x27;write back to contact&#x27; task - using the community node n8n-nodes-alphone, and mark automated records so humans can tell agent-made work from human-made work. This assessment is from the live documentation and repository.

AI access is native rather than bolted on. AlphOne speaks MCP, the same protocol Claude Code and other agent clients use, from version 0.9.0 onward: you mint a token, connect an MCP client, and the agent can query tasks, contacts, and fields through a defined tool list. For a marketing ops team already running agents, that means the CRM is addressable by the same infrastructure that runs everything else, without a vendor middleware layer in between. The GraphQL and REST APIs plus webhooks cover the cases MCP does not.

Self-hosting is a single container image with a compose file, an environment file, and a reverse proxy - the install guide runs four steps. Updates and backups have their own documented procedures, and translation flows through POEditor with a weekly sync rather than direct commits. The plugin catalogue is the honest weak spot at this stage: fields, an importer, and WhatsApp are in-repo, and evaluation effort goes into reading the plugin repositories to see what exists versus what the roadmap promises.

## Verdict

An API-first CRM built to be driven by n8n and AI agents rather than replace them. Early-stage, split-licensed, and best judged as a foundation for an automated stack.

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

Plugin-first CRM (source-available, Elastic 2.0) written in Go. It ships with 176 GitHub stars, an API for custom integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

AlphOne is source-available rather than open source - Elastic License 2.0 licensed and free to self-host; the public repository carries 176 stars. Check the licence terms before commercial use.

An API-first CRM built to be driven by n8n and AI agents rather than replace them. Early-stage, split-licensed, and best judged as a foundation for an automated stack.

## Similar Tools

## Related reading

- [Check outputs, not logs: the silent-failure audit](/blog/silent-failure-audit/)
- [Salesforce's third no-code promise, audited](/blog/salesforce-third-no-code-promise/)
- [AI watermarks are now part of your agent's risk surface](/blog/watermark-provenance-tax-agents/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/alphone/#app",
    "name": "AlphOne",
    "description": "Plugin-first CRM (source-available, Elastic 2.0) written in Go",
    "image": "https://martechsignal.com/og/tools/alphone.png",
    "url": "https://martechsignal.com/tools/alphone/",
    "sameAs": [
      "https://github.com/gopherium/AlphOne"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/alphone/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-06",
    "datePublished": "2026-08-29",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://github.com/gopherium/AlphOne",
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
        "name": "AlphOne",
        "item": "https://martechsignal.com/tools/alphone/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is AlphOne?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Plugin-first CRM (source-available, Elastic 2.0) written in Go. It ships with 176 GitHub stars, an API for custom integrations. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does AlphOne cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "AlphOne is source-available rather than open source - Elastic License 2.0 licensed and free to self-host; the public repository carries 176 stars. Check the licence terms before commercial use."
        }
      },
      {
        "@type": "Question",
        "name": "Is AlphOne a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "An API-first CRM built to be driven by n8n and AI agents rather than replace them. Early-stage, split-licensed, and best judged as a foundation for an automated stack."
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
    "reviewBody": "An API-first CRM designed to be driven by n8n and AI agents, with MCP support that older CRMs lack. It is early: thin features, a small community and a split license that rules out resale, so judge it as a foundation rather than a finished product.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/alphone/#app",
      "name": "AlphOne",
      "url": "https://martechsignal.com/tools/alphone/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 29,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
