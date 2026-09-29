# Relaticle review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Self-hosted free (AGPL-3.0, unlimited users and records); Cloud Pro $19/workspace/mo yearly with 2,000 AI credits published (the vendor pricing page: [pricing page](https://relaticle.com/pricing), verified 2026-09-28). |
| Feature depth | 5/10 | CRM records with native agent support and built-in AI chat cover the small-team CRM loop (vendor documentation: [vendor site](https://relaticle.com), verified 2026-09-28). |
| Integrations | 5/10 | Five named MCP clients plus REST API v1 (OpenAPI 3.1) and CSV import/export (vendor documentation: [vendor site](https://relaticle.com), verified 2026-09-28). |
| AI capability | 6/10 | A 37-tool MCP server and built-in AI chat with agent support are native, not bolted on (vendor documentation: [vendor site](https://relaticle.com), verified 2026-09-28). |
| Openness | 8/10 | AGPL-3.0 with 1.6k GitHub stars and full self-hosting (the source repository: [repository](https://github.com/relaticle/relaticle), verified 2026-09-28). |
| Operational maturity | 4/10 | Founded 2024 at 1.6k stars with priced cloud tiers (vendor documentation: [vendor site](https://relaticle.com), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ AGPL-3.0 licence with free self-hosting | ✗ Paid plans start at $19/mo once past the free tier |
| ✓ AI capabilities: native AI agent support |  |
| ✓ Active public repository (1,635 GitHub stars counted at last check) |  |

**What is Relaticle?**
Relaticle: Open-source CRM with native AI agent support, 37 MCP tools, REST API, Laravel & Filament. Relaticle ships with native AI agent support. The public repository carries 1,635 stars.

**How much does Relaticle cost?**
Relaticle has a free tier; paid plans start at $19/mo. Self-hosted free (AGPL-3.0, unlimited users and records); hosted Cloud Pro $19/workspace/mo yearly ($24 monthly) with 2,000 AI credits; Enterprise from $20,000/yr. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Relaticle a good self-hosted CRM tool in 2026?**
A fast-moving, agent-friendly Laravel CRM whose AI layer outgrew our old notes: free and capable self-hosted, AGPL-3.0, PostgreSQL-only, and no longer without paid tiers.

**How do I install Relaticle on my own server?**
The documented Docker path is one downloaded file and one command: fetch compose.yml from the repository, create a .env containing a generated APP_KEY (echo 'APP_KEY=base64:$(openssl rand -base64 32)') and a DB_PASSWORD, then docker compose up -d. That starts five containers (app, horizon, scheduler, postgres:17-alpine, redis:7-alpine). Create your first admin with docker compose exec app php artisan make:filament-user. Upgrades are docker compose pull followed by docker compose up -d, and migrations run automatically on startup.

**What can an AI agent do through Relaticle's MCP server?**
The hosted MCP endpoint at mcp.relaticle.com exposes 37 tools: cross-entity search and fetch, a whoami call, workspace introspection (CRM schema, CRM summary, opportunity aggregation, activity and custom field listings), list/get/create/update/delete sets for companies, people, and opportunities, and create, update, delete, attach, and detach for tasks and notes. Authentication is OAuth 2.1 with PKCE and dynamic client registration, or a personal access token from Settings, Access Tokens, passed as a bearer header. Destructive operations in the built-in chat require approval, and MCP requests are capped at 120 per minute per user.

**Is Relaticle free, and what does Cloud Pro add?**
Self-hosting is free under AGPL-3.0 with unlimited users and records on your own server. The paid tiers are hosted: Cloud Pro is $19 per workspace per month ($228 billed yearly, or $24 month to month) with a 14-day trial and no card required, adding 2,000 AI credits a month on top of unlimited users, records, the REST API, and the MCP server. Enterprise starts at $20,000 a year, billed yearly, and the site stresses it is never per seat. Self-hosted instances default to the Free plan's 300 AI credits a month unless you bring your own key for more.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 1635
- **Founded:** 2024
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Relaticle is a tool in CRM with free and open source. The catalog documents 3 AI features, 3 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Django CRM

Multi-tenant open-source CRM on Django with leads, campaigns, and self-hosting

IDURAR ERP & CRM

Free Open Source ERP CRM Software Accounting Invoicing | Node.Js React

Customer.io

Data-driven messaging platform for automated email, push, SMS, and in-app messages

Paperclip

Open-source control plane to manage AI agents like a company, hire, schedule, budget, and audit

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- Relaticle
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## Relaticle review (2026): pricing, AI features, verdict

Open-source CRM with native AI agent support, 37 MCP tools, REST API, Laravel & Filament

CRM · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-28

[Visit Relaticle →](https://relaticle.com)

[How we review](/methodology/) · No affiliate links

[Visit Relaticle →](https://relaticle.com)

## MartechSignal Score: 36/60

Relaticle is a Laravel CRM with a 37-tool MCP server and native agent support, free self-hosted with unlimited records. Cloud Pro adds 2,000 AI credits for $19 per workspace.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Relaticle is an open-source CRM you run on your own server under the AGPL-3.0 license, built on Laravel 13, Filament 5, Livewire 4, and PHP 8.5. The repository was created in September 2024, the first stable release shipped in April 2025, and development moves fast: 86 releases so far, 74 of them in the twelve months to September 2026, with v3.5.7 landing on September 6, 2026 alongside 1,635 GitHub stars GitHub stars and a claimed 2,000+ automated tests. The feature set covers companies, people, opportunities with custom pipeline stages and win/loss analysis, tasks, notes, and an activity log, on a customizable data model with 22 field types, conditional visibility, per-field encryption, and no schema migrations. AI is the pitch rather than an afterthought: a 37-tool MCP server at mcp.relaticle.com authenticates with OAuth 2.1 and PKCE or a personal access token, exposing search, fetch, and full create-read-update-delete across companies, people, opportunities, tasks, and notes to Claude, ChatGPT, Cursor, and other MCP clients, with destructive actions gated behind approval cards and requests capped at 120 per minute. There is also Rela, a built-in chat interface that answers questions about your records with model choices and one-click undo on approved destructive actions. Developers get a REST API v1 with twelve paths and a published OpenAPI 3.1 spec at api.relaticle.com, plus CSV import up to 10,000 rows and 10MB per file with column mapping and record-ID matching for updates. The business model outgrew the original no-premium-tiers promise: self-hosting is still free with unlimited users, but the site now sells Cloud Pro at $19 per workspace per month with 2,000 AI credits and an Enterprise tier from $20,000 a year. Per-seat pricing never arrived. Requirements are PostgreSQL 17 and Redis 7, with no MySQL path documented.

Relaticle homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Native AI agent support
- 37-tool MCP server
- Built-in AI chat (Rela)
## Key Integrations

- MCP clients (Claude Code, Claude Desktop, ChatGPT, Cursor, VS Code)
- REST API v1 (OpenAPI 3.1)
- CSV import/export
## Pricing

Relaticle is free to self-host under the AGPL-3.0 licence, paid plans start at $19/mo as of 2026-09.

Self-hosted free (AGPL-3.0, unlimited users and records); hosted Cloud Pro $19/workspace/mo yearly ($24 monthly) with 2,000 AI credits; Enterprise from $20,000/yr

Current plans and limits live on the [Relaticle pricing page](https://relaticle.com/pricing).

## How to install

- Docker path: curl -o compose.yml https://raw.githubusercontent.com/Relaticle/relaticle/main/compose.yml, then create a .env with a generated APP_KEY (echo 'APP_KEY=base64:$(openssl rand -base64 32)') and a DB_PASSWORD, then docker compose up -d. That pulls ghcr.io/relaticle/relaticle:latest plus postgres:17-alpine and redis:7-alpine, for five containers: app, horizon, scheduler, postgres, redis.
- Create your first admin with docker compose exec app php artisan make:filament-user; the admin panel lives at {APP_URL}/app, and instance-level sysadmin access comes from php artisan sysadmin:create, served at /sysadmin.
- From source: git clone https://github.com/Relaticle/relaticle.git, cd relaticle, then composer app-install, a composer script that runs composer install followed by php artisan relaticle:install.
- Manual sequence from the self-hosting docs: composer install --no-dev --optimize-autoloader, pnpm install --frozen-lockfile && pnpm run build, cp .env.example .env, php artisan key:generate, php artisan migrate --force, php artisan storage:link, fix storage and bootstrap/cache permissions, then php artisan make:filament-user.
- Upgrades on Docker are docker compose pull followed by docker compose up -d; the docs say migrations run automatically on startup.
## Requirements

PHP 8.5 with the pdo_pgsql, gd, bcmath, mbstring, xml, and redis extensions, PostgreSQL 17 or newer, Redis 7 or newer, Node.js 22+, Composer 2+, and a web server with Supervisor for queues. MySQL is not a documented option; PostgreSQL is the only database in the docs. The Docker path needs only APP_KEY and DB_PASSWORD. MCP requests are capped at 120 per minute per authenticated user, and self-hosted AI credits default to the Free plan's 300 a month.

## Best for

Laravel and Filament shops that want a CRM their developers can read, extend, and drive from agents: the 37-tool MCP server, REST API v1, and CSV import cover the programmatic paths, AGPL-3.0 keeps the code open, and self-hosting stays free with unlimited users and records.

## Not for

Teams that need native connectors to email, Slack, or marketing tools: none are documented, only MCP, the REST API, and CSV. Also not for buyers who read AGPL-3.0 as a permissive license (offering Relaticle as a service triggers the source obligation), or who want MySQL instead of PostgreSQL 17 and Redis 7. Vendor support means the Enterprise tier, from $20,000 a year.

## Review notes

Assessed from github.com/relaticle/relaticle, relaticle.com, and relaticle.com/docs in September 2026; we have not deployed an instance. The commit log is live (commits dated the day before we checked) and the release cadence is unusually high for a CRM in this bracket: 74 releases in the twelve months to September 2026, currently at v3.5.7.

Corrections against our earlier record. The stack is Laravel 13 with Filament 5, Livewire 4, and PHP 8.5, not Laravel 12 and Filament 3. Our description said the product had no AI features while our own tagline listed MCP tools; the tagline was closer, and understated, because the MCP server exposes 37 tools rather than 30 and there is a built-in chat assistant with approval cards. Stars moved from 1,470 to 1,610.

Two more corrections. The license is AGPL-3.0, so the free claim needs its condition attached: modifying and offering Relaticle as a service triggers the source obligation. And the no-premium-tiers promise is gone; the pricing page now sells Cloud Pro at $19 per workspace per month (14-day trial, no card) and Enterprise from $20,000 a year, though per-seat pricing never arrived and self-hosting remains free.

The self-hosting docs are the strongest part of the public surface: a five-container compose stack, a fully spelled-out manual install sequence, automatic migrations on startup, and a separate sysadmin panel at /sysadmin. The API surface is documented with an OpenAPI 3.1 spec covering twelve paths across companies, people, opportunities, tasks, notes, and custom fields, and the CSV importer documents match-on-ID updates rather than insert-only behavior.

No hosted demo exists, which tells you where the project is: the sitemap lists no demo page, and the closest public entry points are the hosted app at app.relaticle.com and the repository. Evaluation means cloning and installing.

## Verdict

A fast-moving, agent-friendly Laravel CRM whose AI layer outgrew our old notes: free and capable self-hosted, AGPL-3.0, PostgreSQL-only, and no longer without paid tiers.

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

Relaticle: Open-source CRM with native AI agent support, 37 MCP tools, REST API, Laravel & Filament. Relaticle ships with native AI agent support. The public repository carries 1,635 stars.

Relaticle has a free tier; paid plans start at $19/mo. Self-hosted free (AGPL-3.0, unlimited users and records); hosted Cloud Pro $19/workspace/mo yearly ($24 monthly) with 2,000 AI credits; Enterprise from $20,000/yr. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

A fast-moving, agent-friendly Laravel CRM whose AI layer outgrew our old notes: free and capable self-hosted, AGPL-3.0, PostgreSQL-only, and no longer without paid tiers.

The documented Docker path is one downloaded file and one command: fetch compose.yml from the repository, create a .env containing a generated APP_KEY (echo 'APP_KEY=base64:$(openssl rand -base64 32)') and a DB_PASSWORD, then docker compose up -d. That starts five containers (app, horizon, scheduler, postgres:17-alpine, redis:7-alpine). Create your first admin with docker compose exec app php artisan make:filament-user. Upgrades are docker compose pull followed by docker compose up -d, and migrations run automatically on startup.

The hosted MCP endpoint at mcp.relaticle.com exposes 37 tools: cross-entity search and fetch, a whoami call, workspace introspection (CRM schema, CRM summary, opportunity aggregation, activity and custom field listings), list/get/create/update/delete sets for companies, people, and opportunities, and create, update, delete, attach, and detach for tasks and notes. Authentication is OAuth 2.1 with PKCE and dynamic client registration, or a personal access token from Settings, Access Tokens, passed as a bearer header. Destructive operations in the built-in chat require approval, and MCP requests are capped at 120 per minute per user.

Self-hosting is free under AGPL-3.0 with unlimited users and records on your own server. The paid tiers are hosted: Cloud Pro is $19 per workspace per month ($228 billed yearly, or $24 month to month) with a 14-day trial and no card required, adding 2,000 AI credits a month on top of unlimited users, records, the REST API, and the MCP server. Enterprise starts at $20,000 a year, billed yearly, and the site stresses it is never per seat. Self-hosted instances default to the Free plan's 300 AI credits a month unless you bring your own key for more.

## Similar Tools

## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Fifty days of open-source MarTech, audited](/blog/oss-martech-50-day-checkin/)
- [ChatGPT Isn't Search Anymore, It's Checkout](/blog/chatgpt-isnt-search-anymore-its-checkout/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/relaticle/#app",
    "name": "Relaticle",
    "description": "Open-source CRM with native AI agent support, 37 MCP tools, REST API, Laravel & Filament",
    "image": "https://martechsignal.com/og/tools/relaticle.png",
    "url": "https://martechsignal.com/tools/relaticle/",
    "sameAs": [
      "https://relaticle.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/relaticle/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-28",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 19,
      "priceCurrency": "USD",
      "url": "https://relaticle.com/pricing",
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
        "name": "Relaticle",
        "item": "https://martechsignal.com/tools/relaticle/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Relaticle?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Relaticle: Open-source CRM with native AI agent support, 37 MCP tools, REST API, Laravel & Filament. Relaticle ships with native AI agent support. The public repository carries 1,635 stars."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Relaticle cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Relaticle has a free tier; paid plans start at $19/mo. Self-hosted free (AGPL-3.0, unlimited users and records); hosted Cloud Pro $19/workspace/mo yearly ($24 monthly) with 2,000 AI credits; Enterprise from $20,000/yr. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Relaticle a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A fast-moving, agent-friendly Laravel CRM whose AI layer outgrew our old notes: free and capable self-hosted, AGPL-3.0, PostgreSQL-only, and no longer without paid tiers."
        }
      },
      {
        "@type": "Question",
        "name": "How do I install Relaticle on my own server?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The documented Docker path is one downloaded file and one command: fetch compose.yml from the repository, create a .env containing a generated APP_KEY (echo 'APP_KEY=base64:$(openssl rand -base64 32)') and a DB_PASSWORD, then docker compose up -d. That starts five containers (app, horizon, scheduler, postgres:17-alpine, redis:7-alpine). Create your first admin with docker compose exec app php artisan make:filament-user. Upgrades are docker compose pull followed by docker compose up -d, and migrations run automatically on startup."
        }
      },
      {
        "@type": "Question",
        "name": "What can an AI agent do through Relaticle's MCP server?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The hosted MCP endpoint at mcp.relaticle.com exposes 37 tools: cross-entity search and fetch, a whoami call, workspace introspection (CRM schema, CRM summary, opportunity aggregation, activity and custom field listings), list/get/create/update/delete sets for companies, people, and opportunities, and create, update, delete, attach, and detach for tasks and notes. Authentication is OAuth 2.1 with PKCE and dynamic client registration, or a personal access token from Settings, Access Tokens, passed as a bearer header. Destructive operations in the built-in chat require approval, and MCP requests are capped at 120 per minute per user."
        }
      },
      {
        "@type": "Question",
        "name": "Is Relaticle free, and what does Cloud Pro add?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Self-hosting is free under AGPL-3.0 with unlimited users and records on your own server. The paid tiers are hosted: Cloud Pro is $19 per workspace per month ($228 billed yearly, or $24 month to month) with a 14-day trial and no card required, adding 2,000 AI credits a month on top of unlimited users, records, the REST API, and the MCP server. Enterprise starts at $20,000 a year, billed yearly, and the site stresses it is never per seat. Self-hosted instances default to the Free plan's 300 AI credits a month unless you bring your own key for more."
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
    "reviewBody": "Relaticle is a Laravel CRM with a 37-tool MCP server and native agent support, free self-hosted with unlimited records. Cloud Pro adds 2,000 AI credits for $19 per workspace.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/relaticle/#app",
      "name": "Relaticle",
      "url": "https://martechsignal.com/tools/relaticle/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 36,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
