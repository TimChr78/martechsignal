# Open Mercato review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 6/10 | MIT core free self-hosted; the Enterprise Edition (SSO, MFA, record locks) exists with no published pricing (the vendor pricing page: [vendor site](https://www.openmercato.com/), verified 2026-09-07). |
| Feature depth | 6/10 | Commerce, CRM and ERP building blocks with an AI development harness cover the platform scope (vendor documentation: [vendor site](https://www.openmercato.com/), verified 2026-09-28). |
| Integrations | 2/10 | No named integrations in the catalog, though an API is documented (vendor documentation: [vendor site](https://www.openmercato.com/), verified 2026-09-28). |
| AI capability | 7/10 | A 192-case evaluation harness, ~70-tool MCP server and LLM email triage with human approval gate (vendor documentation: [vendor site](https://www.openmercato.com/), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with 1.7k GitHub stars and full self-hosting (the source repository: [repository](https://github.com/open-mercato/open-mercato), verified 2026-09-28). |
| Operational maturity | 4/10 | Founded 2025 at 1.7k stars with a commercial Enterprise layer forming (vendor documentation: [vendor site](https://www.openmercato.com/), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ API access for custom integrations |  |
| ✓ AI capabilities: AI development harness with 192 evaluation cases |  |
| ✓ Active public repository (1,715 GitHub stars counted at last check) |  |

**What is Open Mercato?**
Open Mercato: Open-source TypeScript foundation for AI-built commerce, CRM, and ERP. Open Mercato ships with AI development harness with 192 evaluation cases. The public repository carries 1,715 stars.

**How much does Open Mercato cost?**
Open Mercato is open source - MIT licensed and free to self-host; the public repository carries 1,715 stars. You pay in server time and maintenance, not licences.

**Is Open Mercato a good self-hosted Agent Skills tool in 2026?**
A credible AI-first foundation for engineering-led commerce and CRM builds; early, fast-moving, and not a turnkey product.

**Is Open Mercato a ready-to-use CRM or ERP?**
No, and the project says so itself: it is a foundation framework, with the pitch that business modules and conventions are pre-decided so you start at 80% and build the differentiating 20%. The core CRM module does ship with people, companies, deals, and activities, plus a customer self-service portal, and a demo with sample CRM data loads during yarn initialize, so you can see working software at demo.openmercato.com. But the intended comparison is against starting a Next.js commerce project from scratch, not against Shopify or a configured CRM, and evaluation should assume engineering work.

**How does Open Mercato work with Claude Code, Codex, or Cursor?**
The framework is built around agent tooling. The repo's AGENTS.md defines a spec-first workflow (designs live in .ai/specs/ as dated markdown files) with Always, Ask-First, and Never rules, and CLAUDE.md simply points at it. The standalone project generator emits an AI development harness with guides, skills, and tool-specific configuration for Codex, Claude Code, and Cursor, backed by 192 evaluation cases and a sandboxed release gate. At runtime, a documented MCP server exposes about 70 tools for agent access, and shared skills install with npx skills add open-mercato/skills. In-product, an AI framework provides typed module agents with a mutation-approval gate before AI-driven changes land.

**What does Open Mercato cost to run?**
The core is MIT-licensed and free to self-host, including all documented core modules, so costs are your infrastructure (PostgreSQL 17 with pgvector, Redis 7, Meilisearch) and engineering time. A separate Enterprise Edition package adds SSO with OIDC and SCIM 2.0, MFA, sudo re-authentication, and record locks, and ships outside the MIT core; no price is published anywhere on the site or docs. The site mentions community and commercial support tiers without amounts, so enterprise pricing and support are quote-based by absence of a published list.

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 1715
- **Founded:** 2025
- **HQ:** Open source
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Open Mercato is a tool in Agent Skills with free and open source. The catalog documents 3 AI features, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

DeskcommCRM

Self-hosted open-source CRM with AI agents that sell through WhatsApp

Budibase

Open-source operations platform for building AI agents, apps and automations on your own data

Scrunch

The AI Customer Experience Platform: monitor, optimize and serve your site to AI agents

Intercom

AI-first customer service platform with Fin AI agent and omnichannel messaging

AI Business Skills

63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Open Mercato
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## Open Mercato review (2026): pricing, AI features, verdict

Open-source TypeScript foundation for AI-built commerce, CRM, and ERP

Agent Skills · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-26

[Visit Open Mercato →](https://www.openmercato.com/)

[How we review](/methodology/) · No affiliate links

[Visit Open Mercato →](https://www.openmercato.com/)

## MartechSignal Score: 34/60

Open Mercato is a TypeScript foundation for AI-built commerce and CRM, with a 192-case evaluation harness as its trust argument. The MIT core is free; the Enterprise package prices behind a conversation.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Open Mercato is an MIT-licensed TypeScript framework that positions itself as an AI-engineering foundation for commerce, CRM, and ERP builds: business modules and platform conventions ship pre-decided, so human developers and AI coding agents build features instead of re-arguing architecture on every prompt. The pitch is starting at 80% done. The stack is a Yarn-workspaces monorepo on Next.js App Router with MikroORM, zod, Redis, and Meilisearch, and the core package ships catalog, sales (quoting, ordering, fulfillment, billing, payment gateways, shipping carriers), a CRM module with people, companies, deals, and activities, a customer self-service portal, checkout, workflows, business rules, custom entities, translations, dashboards, audit logs, and API keys. Multi-tenancy is the default posture: a directory module provisions tenants and organization trees, tenant and organization context propagates so queries filter themselves, and per-tenant field-level encryption uses AES-GCM. RBAC is two-layer, roles bundling module.action feature strings with per-user, per-tenant overrides. The AI story is documented rather than implied: the repo carries an AGENTS.md spec-first workflow, a standalone AI development harness with 192 evaluation cases and tool configuration for Claude Code, Codex, and Cursor, an in-product AI framework with typed module agents and a mutation-approval gate, and an MCP server exposing about 70 tools. An Enterprise Edition package adds SSO with OIDC and SCIM, MFA, and record locks outside the MIT core, with no published pricing. A public demo runs at demo.openmercato.com, sandboxes at sandboxes.openmercato.com, and community chat on Discord. Version 0.7.0 shipped on August 26, 2026, and the requirements are honest about weight: Node 24, PostgreSQL 17 with pgvector, Redis 7, and Meilisearch via Docker Compose. This is a foundation framework, not a product: compare it against starting a Next.js commerce project from scratch, not against Shopify or a configured CRM.

Open Mercato homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI development harness with 192 evaluation cases
- MCP server exposing about 70 tools
- LLM email triage with human approval gate
## Pricing

Open Mercato is free to self-host under the MIT licence.

MIT-licensed core, free self-hosted; a separate Enterprise Edition package (SSO, MFA, record locks) exists with no published pricing

## How to install

- Monorepo quick start from the docs: git clone https://github.com/open-mercato/open-mercato.git, cd open-mercato && git checkout develop, docker compose up -d, then cp apps/mercato/.env.example apps/mercato/.env and set DATABASE_URL, JWT_SECRET, and REDIS_URL.
- Continue with yarn install, yarn build:packages, yarn generate, then yarn build:packages a second time (the docs require it), then yarn initialize, which runs migrations, seeds roles, provisions an admin, and loads demo CRM data (pass --no-examples to skip demo data).
- Start development with yarn dev; the backend app runs at http://localhost:3000/backend with credentials printed by yarn initialize, and the splash page on port 4000.
- For a standalone project rather than the monorepo: npx create-mercato-app my-app. The CLI binary is yarn mercato, used for commands such as auth setup, db:migrate, entities install, and api_keys add.
- Upgrades follow git pull && yarn install && yarn db:migrate && yarn generate && yarn dev. Development variants include yarn dev:greenfield, dev:ephemeral, dev:classic, and dev:verbose.
## Requirements

Node.js 24 with Yarn 4 via corepack. Docker Compose brings PostgreSQL 17 with the pgvector extension, Redis 7, and Meilisearch (ports 5432, 6379, and 7700). The MCP server runs separately (yarn mcp:dev on port 3001, yarn mcp:serve in production).

## Best for

TypeScript teams standing up custom commerce, marketplace, or CRM backends with an AI-assisted development workflow, who want multi-tenancy, RBAC, and business modules already decided so agents and developers spend their time on the differentiating features.

## Not for

Teams that want a CRM or storefront they configure rather than code, and anyone needing a turnkey admin experience on day one. Enterprise features (OIDC/SCIM SSO, MFA, record locks) live in a separate package with no published pricing, so regulated buyers need to talk to the vendor first.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from the repository, docs.openmercato.com, and openmercato.com. Not a hands-on review. The project is young (repo created September 2025) and moving fast: v0.7.0 on August 26, 2026 added the standalone AI development harness, an EUDR module, a warranty and RMA desk, and mobile push, following v0.6.7 with a phase-one WMS. Expect breaking change cadence typical of 0.x software.

The AI tooling is the substance behind the marketing framing, and it is unusually concrete for an open-source project: an AGENTS.md with a 32,768-byte budget and Always/Ask-First/Never rules, spec-first design in .ai/specs/, per-agent configuration for Codex, Claude Code, and Cursor, 192 evaluation cases, and a documented MCP server with about 70 tools plus a full Claude Code setup guide. CLAUDE.md in the repo is a one-line pointer to AGENTS.md.

Two documentation gaps are worth knowing before you commit: the website still claims version 0.4.6 against an actual v0.7.0, and the docs' pinned Yarn version (4.12.0) disagrees with package.json (4.17.1). Neither is serious, but both mean you should trust package.json and GitHub releases over the marketing site.

Scale expectations matter: 1,700-plus stars, a public Discord, a demo at demo.openmercato.com, and sandboxes at sandboxes.openmercato.com signal an active early project, not an established platform. The roadmap (visual module scaffolder, GraphQL gateway, multi-region tenancy, plugin marketplace) is documented but unbuilt.

## Verdict

A credible AI-first foundation for engineering-led commerce and CRM builds; early, fast-moving, and not a turnkey product.

## Pros and cons

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open Mercato: Open-source TypeScript foundation for AI-built commerce, CRM, and ERP. Open Mercato ships with AI development harness with 192 evaluation cases. The public repository carries 1,715 stars.

Open Mercato is open source - MIT licensed and free to self-host; the public repository carries 1,715 stars. You pay in server time and maintenance, not licences.

A credible AI-first foundation for engineering-led commerce and CRM builds; early, fast-moving, and not a turnkey product.

No, and the project says so itself: it is a foundation framework, with the pitch that business modules and conventions are pre-decided so you start at 80% and build the differentiating 20%. The core CRM module does ship with people, companies, deals, and activities, plus a customer self-service portal, and a demo with sample CRM data loads during yarn initialize, so you can see working software at demo.openmercato.com. But the intended comparison is against starting a Next.js commerce project from scratch, not against Shopify or a configured CRM, and evaluation should assume engineering work.

The framework is built around agent tooling. The repo's AGENTS.md defines a spec-first workflow (designs live in .ai/specs/ as dated markdown files) with Always, Ask-First, and Never rules, and CLAUDE.md simply points at it. The standalone project generator emits an AI development harness with guides, skills, and tool-specific configuration for Codex, Claude Code, and Cursor, backed by 192 evaluation cases and a sandboxed release gate. At runtime, a documented MCP server exposes about 70 tools for agent access, and shared skills install with npx skills add open-mercato/skills. In-product, an AI framework provides typed module agents with a mutation-approval gate before AI-driven changes land.

The core is MIT-licensed and free to self-host, including all documented core modules, so costs are your infrastructure (PostgreSQL 17 with pgvector, Redis 7, Meilisearch) and engineering time. A separate Enterprise Edition package adds SSO with OIDC and SCIM 2.0, MFA, sudo re-authentication, and record locks, and ships outside the MIT core; no price is published anywhere on the site or docs. The site mentions community and commercial support tiers without amounts, so enterprise pricing and support are quote-based by absence of a published list.

## Similar Tools

## Related reading

- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
- [Most of your marketing AI agents should be if/then](/blog/determinism-audit/)
- [Where open-source martech momentum actually lives](/blog/oss-momentum-tracker-september-2026/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/open-mercato/#app",
    "name": "Open Mercato",
    "description": "Open-source TypeScript foundation for AI-built commerce, CRM, and ERP",
    "image": "https://martechsignal.com/og/tools/open-mercato.png",
    "url": "https://martechsignal.com/tools/open-mercato/",
    "sameAs": [
      "https://www.openmercato.com/"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/open-mercato/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-26",
    "datePublished": "2026-08-25",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://www.openmercato.com/",
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
        "name": "Agent Skills",
        "item": "https://martechsignal.com/categories/agent-skills/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Open Mercato",
        "item": "https://martechsignal.com/tools/open-mercato/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Open Mercato?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open Mercato: Open-source TypeScript foundation for AI-built commerce, CRM, and ERP. Open Mercato ships with AI development harness with 192 evaluation cases. The public repository carries 1,715 stars."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Open Mercato cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open Mercato is open source - MIT licensed and free to self-host; the public repository carries 1,715 stars. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Open Mercato a good self-hosted Agent Skills tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A credible AI-first foundation for engineering-led commerce and CRM builds; early, fast-moving, and not a turnkey product."
        }
      },
      {
        "@type": "Question",
        "name": "Is Open Mercato a ready-to-use CRM or ERP?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No, and the project says so itself: it is a foundation framework, with the pitch that business modules and conventions are pre-decided so you start at 80% and build the differentiating 20%. The core CRM module does ship with people, companies, deals, and activities, plus a customer self-service portal, and a demo with sample CRM data loads during yarn initialize, so you can see working software at demo.openmercato.com. But the intended comparison is against starting a Next.js commerce project from scratch, not against Shopify or a configured CRM, and evaluation should assume engineering work."
        }
      },
      {
        "@type": "Question",
        "name": "How does Open Mercato work with Claude Code, Codex, or Cursor?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The framework is built around agent tooling. The repo's AGENTS.md defines a spec-first workflow (designs live in .ai/specs/ as dated markdown files) with Always, Ask-First, and Never rules, and CLAUDE.md simply points at it. The standalone project generator emits an AI development harness with guides, skills, and tool-specific configuration for Codex, Claude Code, and Cursor, backed by 192 evaluation cases and a sandboxed release gate. At runtime, a documented MCP server exposes about 70 tools for agent access, and shared skills install with npx skills add open-mercato/skills. In-product, an AI framework provides typed module agents with a mutation-approval gate before AI-driven changes land."
        }
      },
      {
        "@type": "Question",
        "name": "What does Open Mercato cost to run?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The core is MIT-licensed and free to self-host, including all documented core modules, so costs are your infrastructure (PostgreSQL 17 with pgvector, Redis 7, Meilisearch) and engineering time. A separate Enterprise Edition package adds SSO with OIDC and SCIM 2.0, MFA, sudo re-authentication, and record locks, and ships outside the MIT core; no price is published anywhere on the site or docs. The site mentions community and commercial support tiers without amounts, so enterprise pricing and support are quote-based by absence of a published list."
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
    "reviewBody": "Open Mercato is a TypeScript foundation for AI-built commerce and CRM, with a 192-case evaluation harness as its trust argument. The MIT core is free; the Enterprise package prices behind a conversation.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/open-mercato/#app",
      "name": "Open Mercato",
      "url": "https://martechsignal.com/tools/open-mercato/"
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

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
