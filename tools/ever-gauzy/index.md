# Ever Gauzy review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Self-hosted free (AGPLv3), Cloud Starter free for 1 company/1 employee, Small Business $17/mo annual, Enterprise $139/mo published (the vendor pricing page: [vendor site](https://gauzy.co), verified 2026-09-28). |
| Feature depth | 6/10 | ERP, CRM, HRM, ATS and time tracking make a broad business management suite (vendor documentation: [vendor site](https://gauzy.co), verified 2026-09-28). |
| Integrations | 2/10 | No named integrations in the catalog (vendor documentation: [vendor site](https://gauzy.co), verified 2026-09-28). |
| AI capability | 2/10 | No AI features are documented in the catalog as of 2026-09-28 (vendor documentation: [vendor site](https://gauzy.co), verified 2026-09-28). |
| Openness | 9/10 | AGPL-3.0 with full self-hosting (the source repository: [repository](https://github.com/ever-co/ever-gauzy), verified 2026-09-28). |
| Operational maturity | 5/10 | With priced cloud tiers above the free plan (vendor documentation: [vendor site](https://gauzy.co), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ AGPL-3.0 licence with free self-hosting | ✗ Paid plans start at $17/mo once past the free tier |
| ✓ API access for custom integrations |  |
| ✓ Active public repository (8,125 GitHub stars counted at last check) |  |

**What is Ever Gauzy?**
Ever Gauzy: Open business management platform: ERP, CRM, HRM, ATS, and time tracking. The public repository carries 8,125 stars. Ever Gauzy offers a public API for custom integrations.

**How much does Ever Gauzy cost?**
Ever Gauzy has a free tier; paid plans start at $17/mo. Self-hosted free (AGPLv3 Community Edition); Cloud Starter free for 1 company and 1 employee, Small Business $17/mo billed annually, Enterprise $139/mo billed annually. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."

**Is Ever Gauzy a good self-hosted CRM tool in 2026?**
Unusually broad open-source business platform with published cloud pricing; best value where time and activity tracking anchors the rollout, and best run by teams with operational patience.

**How much does Ever Gauzy cost in practice?**
Self-hosting is free under the AGPLv3 Community Edition license with no seat limits in the license itself. The hosted cloud plans are published in USD: Starter is free forever for one company and one employee; Small Business is $17 per month billed annually ($204 per year) for one company with ten employees, and additional employees cost $5 per month each; Enterprise is $139 per month billed annually ($1,668 per year), either with one company and unlimited employees or unlimited companies with ten employees each, and additional employees cost $10 per month each. Both paid tiers include a 90-day free trial, and customized UX/UI design or integrations carry additional quoted fees.

**Can I use Ever Gauzy free for business, and what does AGPLv3 require?**
Yes for internal business use, with one obligation to understand. Gauzy's default license is the AGPLv3 Community Edition, and the README also names paid Small Business and Enterprise license tiers for teams that need different terms. AGPLv3 closes the hosting loophole in plain GPL: if you offer Gauzy to users over a network, you must make the corresponding source available to those users. Running it internally for your own staff does not create that obligation. If you plan to resell hosted access to clients or modify the code and want to keep changes private, that is exactly what the commercial tiers exist for, so read the license terms before building on it.

**Does Ever Gauzy include employee time tracking?**
Yes, and it is the platform's anchor module. The README lists employee time-tracking, activity, and productivity tracking as a core capability, and it ships with dedicated desktop applications: Gauzy Desktop and a Desktop Timer app for Windows, Mac, and Linux, so tracked time feeds the same platform that handles invoicing, estimates, and payroll-adjacent reporting. The related features (schedules, appointments, time off, holidays) sit in the same module set. Note that activity tracking of this kind is employee monitoring in substance, so involve the people being tracked before rollout rather than after.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 8125
- **API:** Yes
- **Repository checked:** 2026-09-29
- **Page updated:** 2026-09-07

**Verdict:** Ever Gauzy is a tool in CRM with free and open source. The catalog documents a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

NocoDB

Free, self-hostable Airtable alternative that turns any database into a smart spreadsheet

IDURAR ERP & CRM

Free Open Source ERP CRM Software Accounting Invoicing | Node.Js React

Salesforce Marketing Cloud

Enterprise marketing automation on Salesforce with Agentforce AI across email, SMS, and web

Macro

Open source workspace with a self-updating, agent-driven CRM and shared AI team memory

Django CRM

Multi-tenant open-source CRM on Django with leads, campaigns, and self-hosting

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- Ever Gauzy
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## Ever Gauzy review (2026): pricing, AI features, verdict

Open business management platform: ERP, CRM, HRM, ATS, and time tracking

CRM · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-29

[Visit Ever Gauzy →](https://gauzy.co)

[How we review](/methodology/) · No affiliate links

[Visit Ever Gauzy →](https://gauzy.co)

## MartechSignal Score: 32/60

Ever Gauzy packs ERP, CRM, HRM and time tracking under AGPL with a real free cloud tier. The breadth means depth per module is the trade-off.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Ever Gauzy is an open business management platform from Ever Co that bundles ERP, CRM, HRM, applicant tracking, project management, and employee time and activity tracking under an AGPLv3 Community Edition license, with paid Small Business and Enterprise license tiers documented alongside it. The module list is unusually wide for open source: estimates, invoicing, payments, income and expense tracking, inventory and equipment sharing, schedules and appointments, sales pipelines and proposals, goals and KPIs, time off, a help center with knowledge base, and reports, alongside multi-organization, multi-currency, and multi-language support. The stack is TypeScript on Node.js and NestJS with an Angular frontend and TypeORM or MikroORM for data, SQLite for demos and PostgreSQL or MySQL recommended for production, deployable with Docker Compose or Kubernetes. Public APIs are served from api.gauzy.co with Swagger docs at the /docs path, and desktop applications (a server, a desktop app, and a timer app) run on Windows, Mac, and Linux for time and activity tracking. Companion products connect to the same APIs: Ever Teams for work management, built on React, Next.js, and React Native, and Ever Works, an agentic runtime. Hosted cloud pricing is published: a Starter tier free for one company and one employee, Small Business at $17 per month billed annually for ten employees with additional employees at $5 each, and Enterprise at $139 per month billed annually with either unlimited employees or unlimited companies; both paid tiers carry a 90-day free trial, and the hosted SaaS at app.gauzy.co is marked alpha. No AI features are documented in the product; the AI-adjacent material in the repo is developer tooling, not capability. Treat Gauzy as a broad platform where you adopt two or three modules, not a suite you adopt whole.

Ever Gauzy homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## Pricing

Ever Gauzy is free to self-host under the AGPL-3.0 licence, paid plans start at $17/mo as of 2026-09.

Self-hosted free (AGPLv3 Community Edition); Cloud Starter free for 1 company and 1 employee, Small Business $17/mo billed annually, Enterprise $139/mo billed annually

## How to install

- Fastest look: the hosted demo at demo.gauzy.co, or the hosted SaaS at app.gauzy.co, which the README marks as an alpha version. Default demo logins documented in the README are the demo admin login (admin at ever.co) / admin and the demo employee login (employee at ever.co) / 12345678.
- Demo stack in one command: docker-compose -f docker-compose.demo.yml up (Docker Compose v2.20 or later is the stated minimum).
- Production containers: docker-compose up -d after setting JWT_SECRET, JWT_REFRESH_TOKEN_SECRET, and JWT_VERIFICATION_TOKEN_SECRET in .env.compose (the README suggests generating them with openssl rand -hex 64). A docker-compose.infra.yml brings up infrastructure only, and docker-compose.build.yml builds locally.
- From source: yarn bootstrap, optionally yarn prepare:husky, then yarn start; seed demo data with yarn seed or yarn seed:all. The UI runs at localhost:4200 and the API at localhost:3000/api.
- Desktop users install Gauzy Desktop or the Desktop Timer app for Windows, Mac, or Linux from the releases rather than running the web stack.
## Requirements

Node.js and Yarn for a source build, with PostgreSQL or MySQL recommended for production (SQLite is the default only for demos; MariaDB, MS SQL, CockroachDB, Oracle, and MongoDB are also listed as supported by the ORM layer). Docker Compose v2.20 or later for containers, Kubernetes documented for production deployments.

## Best for

Small teams and agencies that want one self-hosted system combining client billing, invoicing, pipelines, and employee time and activity tracking, and are comfortable running a multi-service NestJS platform to get it without per-seat license fees.

## Not for

Teams wanting a single-purpose, lightweight tool: this is a many-module monorepo with real operational weight. Also reconsider where employee activity monitoring is sensitive; the tracking heritage needs an explicit conversation before rollout. AI-driven CRM is absent by any documented measure.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from github.com/ever-co/ever-gauzy, gauzy.co, and its pricing page. Not a hands-on review. The repo is large and active (4,300-plus stars, 27,000-plus commits), and the README is honest about maturity markers: app.gauzy.co is labeled alpha, and the demo database defaults to SQLite unless you configure PostgreSQL or MySQL.

A correction against our earlier record: Gauzy's own frontend is Angular, not React. The README lists Angular with ngx-admin for the Gauzy UI; Next.js belongs to the companion product Ever Teams, which is a separate codebase connecting to Gauzy's APIs. We had attributed the wrong frontend stack to Gauzy itself.

The commercial model is clearer than most open-core projects: the README names three license tiers (Community Edition, Small Business, Enterprise), the cloud pricing page publishes exact numbers (Starter free for one company and one employee, Small Business $17 per month billed annually for ten employees plus $5 per additional employee, Enterprise $139 per month billed annually with unlimited employees or unlimited companies), and both paid tiers carry a 90-day free trial. The hosted SaaS is explicitly alpha, so self-hosting or the demo remain the serious evaluation paths.

No AI features are documented in the product itself. The AI-adjacent items visible in the repo (AGENTS.md, .claude and .cursor directories, CodeRabbit review) are development tooling for contributors, and Ever Works, the agentic runtime product from Ever Co, is a separate project, not a Gauzy module. Any AI capability claim about Gauzy should be treated as unsupported until it appears in the README or changelog.

## Verdict

Unusually broad open-source business platform with published cloud pricing; best value where time and activity tracking anchors the rollout, and best run by teams with operational patience.

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

Ever Gauzy: Open business management platform: ERP, CRM, HRM, ATS, and time tracking. The public repository carries 8,125 stars. Ever Gauzy offers a public API for custom integrations.

Ever Gauzy has a free tier; paid plans start at $17/mo. Self-hosted free (AGPLv3 Community Edition); Cloud Starter free for 1 company and 1 employee, Small Business $17/mo billed annually, Enterprise $139/mo billed annually. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."

Unusually broad open-source business platform with published cloud pricing; best value where time and activity tracking anchors the rollout, and best run by teams with operational patience.

Self-hosting is free under the AGPLv3 Community Edition license with no seat limits in the license itself. The hosted cloud plans are published in USD: Starter is free forever for one company and one employee; Small Business is $17 per month billed annually ($204 per year) for one company with ten employees, and additional employees cost $5 per month each; Enterprise is $139 per month billed annually ($1,668 per year), either with one company and unlimited employees or unlimited companies with ten employees each, and additional employees cost $10 per month each. Both paid tiers include a 90-day free trial, and customized UX/UI design or integrations carry additional quoted fees.

Yes for internal business use, with one obligation to understand. Gauzy's default license is the AGPLv3 Community Edition, and the README also names paid Small Business and Enterprise license tiers for teams that need different terms. AGPLv3 closes the hosting loophole in plain GPL: if you offer Gauzy to users over a network, you must make the corresponding source available to those users. Running it internally for your own staff does not create that obligation. If you plan to resell hosted access to clients or modify the code and want to keep changes private, that is exactly what the commercial tiers exist for, so read the license terms before building on it.

Yes, and it is the platform's anchor module. The README lists employee time-tracking, activity, and productivity tracking as a core capability, and it ships with dedicated desktop applications: Gauzy Desktop and a Desktop Timer app for Windows, Mac, and Linux, so tracked time feeds the same platform that handles invoicing, estimates, and payroll-adjacent reporting. The related features (schedules, appointments, time off, holidays) sit in the same module set. Note that activity tracking of this kind is employee monitoring in substance, so involve the people being tracked before rollout rather than after.

## Similar Tools

## Related reading

- [Salesforce Made Agentforce Free. What Marketing Ops Can Build With It.](/blog/salesforce-agentforce-free-marketing-ops/)
- [Deliverability in the AI-spam Era Is a Content Problem, Not an IT Problem](/blog/deliverability-ai-spam-content-problem/)
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
    "@id": "https://martechsignal.com/tools/ever-gauzy/#app",
    "name": "Ever Gauzy",
    "description": "Open business management platform: ERP, CRM, HRM, ATS, and time tracking",
    "image": "https://martechsignal.com/og/tools/ever-gauzy.png",
    "url": "https://martechsignal.com/tools/ever-gauzy/",
    "sameAs": [
      "https://gauzy.co"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/ever-gauzy/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-29",
    "datePublished": "2026-08-25",
    "offers": [
      {
        "@type": "Offer",
        "price": 0,
        "priceCurrency": "USD",
        "url": "https://gauzy.co",
        "priceValidUntil": "2026-12-31"
      },
      {
        "@type": "Offer",
        "price": 17,
        "priceCurrency": "USD",
        "url": "https://gauzy.co",
        "priceValidUntil": "2026-12-31"
      }
    ]
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
        "name": "Ever Gauzy",
        "item": "https://martechsignal.com/tools/ever-gauzy/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Ever Gauzy?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Ever Gauzy: Open business management platform: ERP, CRM, HRM, ATS, and time tracking. The public repository carries 8,125 stars. Ever Gauzy offers a public API for custom integrations."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Ever Gauzy cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Ever Gauzy has a free tier; paid plans start at $17/mo. Self-hosted free (AGPLv3 Community Edition); Cloud Starter free for 1 company and 1 employee, Small Business $17/mo billed annually, Enterprise $139/mo billed annually. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.\""
        }
      },
      {
        "@type": "Question",
        "name": "Is Ever Gauzy a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Unusually broad open-source business platform with published cloud pricing; best value where time and activity tracking anchors the rollout, and best run by teams with operational patience."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Ever Gauzy cost in practice?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Self-hosting is free under the AGPLv3 Community Edition license with no seat limits in the license itself. The hosted cloud plans are published in USD: Starter is free forever for one company and one employee; Small Business is $17 per month billed annually ($204 per year) for one company with ten employees, and additional employees cost $5 per month each; Enterprise is $139 per month billed annually ($1,668 per year), either with one company and unlimited employees or unlimited companies with ten employees each, and additional employees cost $10 per month each. Both paid tiers include a 90-day free trial, and customized UX/UI design or integrations carry additional quoted fees."
        }
      },
      {
        "@type": "Question",
        "name": "Can I use Ever Gauzy free for business, and what does AGPLv3 require?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes for internal business use, with one obligation to understand. Gauzy's default license is the AGPLv3 Community Edition, and the README also names paid Small Business and Enterprise license tiers for teams that need different terms. AGPLv3 closes the hosting loophole in plain GPL: if you offer Gauzy to users over a network, you must make the corresponding source available to those users. Running it internally for your own staff does not create that obligation. If you plan to resell hosted access to clients or modify the code and want to keep changes private, that is exactly what the commercial tiers exist for, so read the license terms before building on it."
        }
      },
      {
        "@type": "Question",
        "name": "Does Ever Gauzy include employee time tracking?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, and it is the platform's anchor module. The README lists employee time-tracking, activity, and productivity tracking as a core capability, and it ships with dedicated desktop applications: Gauzy Desktop and a Desktop Timer app for Windows, Mac, and Linux, so tracked time feeds the same platform that handles invoicing, estimates, and payroll-adjacent reporting. The related features (schedules, appointments, time off, holidays) sit in the same module set. Note that activity tracking of this kind is employee monitoring in substance, so involve the people being tracked before rollout rather than after."
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
    "reviewBody": "Ever Gauzy packs ERP, CRM, HRM and time tracking under AGPL with a real free cloud tier. The breadth means depth per module is the trade-off.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/ever-gauzy/#app",
      "name": "Ever Gauzy",
      "url": "https://martechsignal.com/tools/ever-gauzy/"
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
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/tools/ever-gauzy/", "dateModified": "2026-09-29"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
