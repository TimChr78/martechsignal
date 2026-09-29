# Django CRM review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free self-hosted under MIT with no user caps or feature paywall; managed hosting exists from Bottle CRM with published vertical packs (the vendor pricing page: [vendor site](https://bottlecrm.io), verified 2026-09-06). |
| Feature depth | 5/10 | Leads, campaigns and multi-tenant basics cover the CRM core; marketing automation depth is minimal (vendor documentation: [vendor site](https://bottlecrm.io), verified 2026-09-28). |
| Integrations | 4/10 | REST API with an OpenAPI 3 schema, Google OAuth, optional SES and Sentry documented (vendor documentation: [vendor site](https://bottlecrm.io), verified 2026-09-28). |
| AI capability | 2/10 | No AI features are documented in the catalog as of 2026-09-28 (vendor documentation: [vendor site](https://bottlecrm.io), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with no paywalled features (the source repository: [repository](https://github.com/Django-CRM/Django-CRM), verified 2026-09-28). |
| Operational maturity | 4/10 | Community-run with one managed-hosting vendor behind it (vendor documentation: [vendor site](https://bottlecrm.io), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ Active public repository (2,432 GitHub stars counted at last check) |  |
| ✓ Native integrations include REST API (OpenAPI 3 schema), Swagger UI, Google OAuth (5 listed) |  |

**What is Django CRM?**
Django CRM: Multi-tenant open-source CRM on Django with leads, campaigns, and self-hosting. The public repository carries 2,432 stars. Django CRM offers a public API for custom integrations.

**How much does Django CRM cost?**
Django CRM is open source - MIT licensed and free to self-host; the public repository carries 2,432 stars; native integrations cover REST API (OpenAPI 3 schema), Swagger UI, Google OAuth. You pay in server time and maintenance, not licences.

**Is Django CRM a good self-hosted CRM tool in 2026?**
A disciplined, well-documented multi-tenant CRM for Django teams that want to own the code. Everyone else gets faster value from a hosted product with a larger community.

**Does Django CRM support MCP?**
Not any more. The project shipped an MCP server at /mcp and then removed it, documenting the reasoning: it proxied eight entities to the same REST API and added no capability. The current guidance is to point an agent at the OpenAPI schema at GET /schema/ with a personal access token.

**Can Django CRM run on SQLite or MySQL?**
No. Multi-tenancy depends on PostgreSQL Row-Level Security, which has no SQLite equivalent, and the only non-test settings module configures PostgreSQL. SQLite appears only in test settings, and PostgreSQL 16 is the version the project's CI exercises.

**How does multi-tenancy work in Django CRM?**
Each request sets a PostgreSQL session variable (app.current_org) and Row-Level Security policies filter every table against it at the database layer. The app connects as a restricted crm_user role, never a superuser, because a superuser connection bypasses RLS entirely. That is what lets one deployment host many organizations.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 2432
- **API:** Yes
- **Repository checked:** 2026-09-29
- **Page updated:** 2026-09-06

**Verdict:** Django CRM is a tool in CRM with free and open source. The catalog documents 5 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-06. This is a desk review, not a hands-on test. Desk-reviewed

SuiteCRM

Enterprise-grade open-source CRM with sales, marketing, and support automation

Relaticle

Open-source CRM with native AI agent support, 37 MCP tools, REST API, Laravel & Filament

Twenty

The open-source alternative to Salesforce, designed for AI with modern CRM workflows

EspoCRM

Lightweight open-source CRM with sales automation, marketing tools, and customer management

Freshsales

AI-powered CRM with built-in phone, email, and chat for sales teams

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- Django CRM
Re-check pending: pricing last verified 2026-09-06 (24 days ago).

## Django CRM review (2026): pricing, AI features, verdict

Multi-tenant open-source CRM on Django with leads, campaigns, and self-hosting

CRM · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-29

[Visit Django CRM →](https://bottlecrm.io)

[How we review](/methodology/) · No affiliate links

[Visit Django CRM →](https://bottlecrm.io)

## MartechSignal Score: 32/60

Django CRM is a CRM for teams that read Python: MIT, multi-tenant, no feature paywall at all. The trade is that everything around it, including AI, is your own build.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Django CRM, sold hosted as Bottle CRM, is an open-source, multi-tenant CRM built on Django REST Framework with a Svelte 5 and SvelteKit frontend and a Flutter app for iOS and Android, all sharing one backend and one documented REST API. It covers leads, accounts, contacts, opportunities, support cases, tasks, and invoices, and the helpdesk is a real one: SLA timers, approvals, escalations, macros, and a knowledge base rather than a ticket list. The engineering decision that defines it is PostgreSQL Row-Level Security. Tenant isolation is enforced in the database through an app.current_org session variable, so one deployment can serve a startup or hundreds of organizations, and the docs are blunt that SQLite cannot run the application because RLS has no SQLite equivalent. The agent story is unusual for an open-source CRM and worth reading before you plan anything: the project shipped an MCP server at /mcp and then removed it, on the stated grounds that it covered eight entities and added nothing the REST API did not already do. Instead you mint a personal access token, stored only as a SHA-256 hash and shown once, point Claude, Cursor, or Codex at the OpenAPI 3 schema generated by drf-spectacular, and the agent works as a normal API client that inherits your role, org, and RLS scope. Two caveats the docs state plainly: the scopes field on tokens exists but nothing enforces it yet, so a token equals that user's full access, and invoice PDF generation runs synchronously through WeasyPrint. Licensing is MIT with no per-seat pricing, user caps, or feature paywalls. Requirements are Python 3.12 or later, Django 6.1 or later, PostgreSQL 16, Redis 7, and Node 24. The community is small at around 2,400 stars, with MicroPyramid as the commercial backer. Pick it for a Django codebase you can extend; the marketing surface is campaign basics, not automation.

Django CRM homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## Key Integrations

- REST API (OpenAPI 3 schema)
- Swagger UI
- Google OAuth
- Amazon SES (optional email)
- Sentry (optional)
## Pricing

Django CRM is free to self-host under the MIT licence.

Free open-source self-hosting under MIT with no user caps or feature paywall; Bottle CRM sells managed hosting, with vertical packs and demo data layered on the open core.

## How to install

- Fastest path is Docker Compose from the repo root: git clone https://github.com/django-crm/Django-CRM.git, cd Django-CRM, then docker compose up --build. That starts six services: PostgreSQL 16, Redis 7, the Django API on port 8000, a Celery worker, a Celery beat scheduler, and the SvelteKit frontend on port 5173.
- Nothing needs configuring to get a working stack. The checked-in .env.docker ships development defaults and is loaded by every service; overrides go in a gitignored .env.docker.local whose values win.
- Migrations run automatically on container start. Load demo data with docker compose exec backend python manage.py seed_data --email YOUR-EMAIL, which creates an organization named MicroPyramid plus demo leads, accounts, contacts, opportunities, cases, tasks, and invoices.
- Sign in with docker compose exec backend python manage.py devlogin YOUR-EMAIL --org MicroPyramid, which prints an access token, a refresh token, and the org UUID. The frontend is at http://localhost:5173 and the API with Swagger UI at http://localhost:8000/swagger-ui/.
- If Docker does not fit, the docs' Manual setup page covers running the backend, database, Redis, Celery, and frontend directly on one machine.
- For an agent, mint a personal access token at Settings, then API tokens, and point the agent at GET /schema/ so it can discover endpoints itself.
## Requirements

Python 3.12 or later, Django 6.1.1 or later, PostgreSQL 16 (the only supported backend and the only version CI exercises, because RLS makes SQLite unusable), Redis 7, and Node 24 with pnpm 10 for the frontend. The backend also installs Cairo, Pango, and gdk-pixbuf for WeasyPrint's PDF rendering.

## Best for

Django-fluent teams that want a self-hosted CRM they can extend on day one, agencies running several brands or client books from one multi-tenant instance, and shops that want AI agents driving the CRM through a documented REST API.

## Not for

Teams that want SQLite or MySQL (PostgreSQL 16 only), anyone expecting enforced token scopes or an MCP endpoint, and marketing teams wanting automation - campaign and email features are basics, and integrations are whatever you build.

## Review notes

Assessed from the repository and its MkDocs documentation, which publishes to Read the Docs, rather than a running instance. The docs are unusually candid for a commercially backed project: they name the removed MCP server, the unenforced token scopes, and the fact that no benchmarked sizing guide exists rather than inventing one.

Multi-tenancy is the architecture story, and it is checkable. RLS policies key on app.current_org, the Django containers connect as a non-superuser crm_user role created by init-rls-user.sql, and the docs warn that connecting as the postgres superuser would make every policy silently inert. Coverage is published as a badge in the README rather than only claimed.

The AI-agent angle is documented rather than implied: no special protocol, just a bearer token and an OpenAPI schema, with RLS, RBAC, and field validation applying to the agent exactly as to the web app. Vertical packs layer industry-specific pipelines and sample records on top of seed data, which tells you the product direction is industry templates.

## Verdict

A disciplined, well-documented multi-tenant CRM for Django teams that want to own the code. Everyone else gets faster value from a hosted product with a larger community.

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

Django CRM: Multi-tenant open-source CRM on Django with leads, campaigns, and self-hosting. The public repository carries 2,432 stars. Django CRM offers a public API for custom integrations.

Django CRM is open source - MIT licensed and free to self-host; the public repository carries 2,432 stars; native integrations cover REST API (OpenAPI 3 schema), Swagger UI, Google OAuth. You pay in server time and maintenance, not licences.

A disciplined, well-documented multi-tenant CRM for Django teams that want to own the code. Everyone else gets faster value from a hosted product with a larger community.

Not any more. The project shipped an MCP server at /mcp and then removed it, documenting the reasoning: it proxied eight entities to the same REST API and added no capability. The current guidance is to point an agent at the OpenAPI schema at GET /schema/ with a personal access token.

No. Multi-tenancy depends on PostgreSQL Row-Level Security, which has no SQLite equivalent, and the only non-test settings module configures PostgreSQL. SQLite appears only in test settings, and PostgreSQL 16 is the version the project's CI exercises.

Each request sets a PostgreSQL session variable (app.current_org) and Row-Level Security policies filter every table against it at the database layer. The app connects as a restricted crm_user role, never a superuser, because a superuser connection bypasses RLS entirely. That is what lets one deployment host many organizations.

## Similar Tools

## Related reading

- [Your AI Marketing Agent Doesn't Need Better Prompts](/blog/ai-agents-need-campaign-state/)
- [Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough](/blog/salesforce-claude-commerce-cloud-agentforce/)
- [Most of your marketing AI agents should be if/then](/blog/determinism-audit/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/django-crm/#app",
    "name": "Django CRM",
    "description": "Multi-tenant open-source CRM on Django with leads, campaigns, and self-hosting",
    "image": "https://martechsignal.com/og/tools/django-crm.png",
    "url": "https://martechsignal.com/tools/django-crm/",
    "sameAs": [
      "https://bottlecrm.io"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/django-crm/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-29",
    "datePublished": "2026-08-21",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://bottlecrm.io",
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
        "name": "Django CRM",
        "item": "https://martechsignal.com/tools/django-crm/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Django CRM?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Django CRM: Multi-tenant open-source CRM on Django with leads, campaigns, and self-hosting. The public repository carries 2,432 stars. Django CRM offers a public API for custom integrations."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Django CRM cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Django CRM is open source - MIT licensed and free to self-host; the public repository carries 2,432 stars; native integrations cover REST API (OpenAPI 3 schema), Swagger UI, Google OAuth. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Django CRM a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A disciplined, well-documented multi-tenant CRM for Django teams that want to own the code. Everyone else gets faster value from a hosted product with a larger community."
        }
      },
      {
        "@type": "Question",
        "name": "Does Django CRM support MCP?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Not any more. The project shipped an MCP server at /mcp and then removed it, documenting the reasoning: it proxied eight entities to the same REST API and added no capability. The current guidance is to point an agent at the OpenAPI schema at GET /schema/ with a personal access token."
        }
      },
      {
        "@type": "Question",
        "name": "Can Django CRM run on SQLite or MySQL?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. Multi-tenancy depends on PostgreSQL Row-Level Security, which has no SQLite equivalent, and the only non-test settings module configures PostgreSQL. SQLite appears only in test settings, and PostgreSQL 16 is the version the project's CI exercises."
        }
      },
      {
        "@type": "Question",
        "name": "How does multi-tenancy work in Django CRM?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Each request sets a PostgreSQL session variable (app.current_org) and Row-Level Security policies filter every table against it at the database layer. The app connects as a restricted crm_user role, never a superuser, because a superuser connection bypasses RLS entirely. That is what lets one deployment host many organizations."
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
    "reviewBody": "Django CRM is a CRM for teams that read Python: MIT, multi-tenant, no feature paywall at all. The trade is that everything around it, including AI, is your own build.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/django-crm/#app",
      "name": "Django CRM",
      "url": "https://martechsignal.com/tools/django-crm/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 32,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/tools/django-crm/", "breadcrumb": {"@id": "https://martechsignal.com/tools/django-crm/#breadcrumb"}, "dateModified": "2026-09-29"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
