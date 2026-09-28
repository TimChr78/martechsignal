# IDURAR ERP &amp; CRM pricing


| Pros | Cons |
| --- | --- |
| &#10003; AGPL-3.0 licence with free self-hosting | &#10007; No hands-on test - this assessment is based on vendor documentation and the public repository |
| &#10003; API access for custom integrations |  |
| &#10003; Established community (8,776 GitHub stars) |  |

**What is IDURAR ERP &amp; CRM?**
Free Open Source ERP CRM Software Accounting Invoicing | Node.Js React. It ships with 8,776 GitHub stars, an API for custom integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does IDURAR ERP &amp; CRM cost?**
IDURAR ERP &amp; CRM is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 8,776 stars. You pay in server time and maintenance, not licences.

**Is IDURAR ERP &amp; CRM a good self-hosted CRM tool in 2026?**
A compact AGPL starting point for custom MERN invoicing and payments work, not a deployable CRM suite: read the three model files before you believe any feature list.

**Is IDURAR open source or fair-code?**
The license file is standard AGPL-3.0 with no added clauses, and the README says IDURAR is free for personal or commercial use. The fair-code label comes from the project&#x27;s own copy: the README uses both phrases in different lines and the backend package.json still declares a Fair-code License, which does not match the license file. Functionally the repo is AGPL software, so the network-copyleft obligation applies if you modify it and serve users without publishing source. The vendor sells paid lifetime licenses on its site, which buy support and features rather than permission.

**What does IDURAR cost, and what do the paid licenses include?**
Self-hosting the Community Edition is free. The vendor site publishes two one-time licenses: Professional at $5,000 with three months of support, and Enterprise at $10,000 with six months, adding multi-company and branch support, multi-currency, multiple languages, a headless API and public forms. The site&#x27;s own comparison table says Community is limited to one admin user, but the AGPL-3.0 license in the repository carries no user limit, so treat the cap as a commercial position, not a code enforcement.

**Can IDURAR replace SuiteCRM or Dolibarr for a sales team?**
No, not in the open-source edition. SuiteCRM and Dolibarr ship leads, pipelines, cases, campaigns and role-based teams; IDURAR&#x27;s repository has three application models (clients, invoices, payments) and a single owner role. It competes as a developer base for custom billing and customer invoicing tools, where its small MERN codebase and generated REST routes are the advantage. If the requirement is a CRM your team configures in the admin UI, the config-first open-source CRMs are the better fit.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 8776
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** IDURAR ERP &amp; CRM is a tool in CRM with free and open source. The catalog documents a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Frappe CRM

Fully featured, open source CRM

Ever Gauzy

Open business management platform: ERP, CRM, HRM, ATS, and time tracking

Macro

Open source workspace with a self-updating, agent-driven CRM and shared AI team memory

Relaticle

Open-source CRM with native AI agent support, 37 MCP tools, REST API, Laravel &amp; Filament

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- IDURAR ERP &amp; CRM
## IDURAR ERP &amp; CRM review (2026): pricing, AI features, verdict

Free Open Source ERP CRM Software Accounting Invoicing | Node.Js React

CRM · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[How we review](/methodology/) · No affiliate links

[Visit IDURAR ERP & CRM &#8594;](https://cloud.idurarapp.com)

Not yet scored against the rubric; scored pages show six pillars.

## Overview

IDURAR is an open-source ERP and CRM on the MERN stack - Node.js and Express with MongoDB behind an Ant Design React frontend - and it is smaller than its 8,700-plus GitHub stars suggest. The license file is verbatim AGPL-3.0 with no custom clauses, and the README answers the commercial question directly: free for personal or commercial use. The same README also calls the project fair-code in one line and open source in another, and the backend package.json still says Fair-code License, so the licensing story is untidy even though the license itself is standard AGPL. The feature set needs the most correction before you commit: the README claims exactly four modules - invoice, payment, quote, and customer management - and the code backs that up. Quotes are not a separate entity but an invoice with a quote type, converted through a dedicated endpoint, and recurring invoices are a field on the invoice model rather than a billing engine. There are no expense, lead, product, or inventory models in the open-source code, and the role model ships with a single owner role, so this is a one-admin invoicing core rather than a departmental suite. The paid tiers on the vendor site make the same point by omission: a Professional lifetime license at $5,000 and an Enterprise license at $10,000, which add multi-company, multi-currency, multiple languages, a headless API, and support windows. Every entity gets auto-generated REST routes (create, read, update, delete, search, filter, summary) but there is no Swagger spec and the docs subdomain does not resolve, so plan to read the source. Installation is two npm terminals rather than a container; there is no Dockerfile in the repository. This assessment is from the repository, the license file, and the vendor site.

IDURAR ERP &amp; CRM homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## Pricing

IDURAR ERP &amp; CRM is free to self-host under the AGPL-3.0 licence.

Self-host free under AGPL-3.0. The vendor sells one-time license tiers on its site: Professional lifetime license $5,000, Enterprise $10,000, adding multi-company, multi-currency, a headless API and support.

Current plans and limits live on the [IDURAR ERP &amp; CRM pricing page](https://www.idurarapp.com).

## How to install

- From INSTALLATION-INSTRUCTIONS.md, backend first: git clone https://github.com/idurar/idurar-erp-crm.git, cd idurar-erp-crm, cd backend, then npm install, npm run setup and npm run dev. npm run setup runs src/setup/setup.js.
- Frontend in a second terminal: cd frontend, npm install, npm run dev. The doc says open http://localhost:3000; the Vite dev server proxies /api to the backend on port 8888.
- Backend configuration lives in /backend/.env. The required value is DATABASE (your MongoDB connection string); the checked-in template also carries JWT_SECRET, NODE_ENV and PUBLIC_SERVER_FILE, with RESEND_API and OPENAI_API_KEY commented out.
- There is no Dockerfile or docker-compose file in the repository, so containerizing is on you. The install doc includes a legacy OpenSSL workaround (export NODE_OPTIONS=--openssl-legacy-provider) for older Node, or recommends Node.js v20.
- npm run upgrade and npm run reset exist alongside setup for schema and data resets; read them before running against data you care about.
## Requirements

Node.js 20.9 and npm 10.2 are the pinned engines, with MongoDB as the only database (Mongoose 8 on the backend, Express 4, React 18, Ant Design 5, Redux Toolkit and Vite on the frontend). PDF output uses html-pdf with pug templates, which needs the pdf engine available on the host. There is no official container image, so a bare host or your own image is the deployment path.

## Best for

Developers on the MERN stack who want a working starting point for a custom invoicing, quoting and payments product: the CRUD API, PDF generation and Ant Design UI are real, and the codebase is small enough to read end to end in an afternoon.

## Not for

Sales teams looking for a CRM to configure: there is no lead or pipeline model in the open-source code, one user role, and no documented API reference. Teams needing multi-company, multi-currency or headless API access are pointed at paid licenses rather than code.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from the repository, the license file, the installation doc and the vendor site. Not a hands-on review. The most useful evaluation step is reading backend/src/models/appModels: exactly three application models exist (Client, Invoice, Payment), which settles in one glance what the open-source edition is. Quotes are an invoice with a quote type and a /quote/convert/:id endpoint, and the recurring field on the invoice model is a schedule enum, not a billing engine.

The vendor site and the repository disagree, and the difference matters commercially. The site&#x27;s comparison table caps the Community Edition at one admin user and marks core features as excluded, while the AGPL-3.0 license in the repo places no such limit, and the README invites free commercial use. The site sells a Professional lifetime license at $5,000 and Enterprise at $10,000 covering multi-company, multi-currency, languages, a headless API and support. Read the license, not the marketing table, before deciding what your install may do.

Some feature pages on the vendor site describe capabilities that do not exist in the open-source code at all: purchase orders, supplier management, barcodes, a general ledger and webhooks appear in the localized marketing pages but have no models or routes in the repository. Treat the site&#x27;s feature copy as aspirational and the repository as the product.

The REST API is real but undocumented: routes are generated per entity for create, read, update, delete, search, list, filter and summary, plus mail endpoints and quote conversion. There is no OpenAPI spec in the repo and docs.idurarapp.com does not resolve, so integration work means reading backend/src/routes. AI features: none. The openai dependency in backend/package.json is unused, and the only other AI reference in the repo is a maintainer CV written for AI agents.

## Verdict

A compact AGPL starting point for custom MERN invoicing and payments work, not a deployable CRM suite: read the three model files before you believe any feature list.

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

Free Open Source ERP CRM Software Accounting Invoicing | Node.Js React. It ships with 8,776 GitHub stars, an API for custom integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

IDURAR ERP &amp; CRM is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 8,776 stars. You pay in server time and maintenance, not licences.

A compact AGPL starting point for custom MERN invoicing and payments work, not a deployable CRM suite: read the three model files before you believe any feature list.

The license file is standard AGPL-3.0 with no added clauses, and the README says IDURAR is free for personal or commercial use. The fair-code label comes from the project&#x27;s own copy: the README uses both phrases in different lines and the backend package.json still declares a Fair-code License, which does not match the license file. Functionally the repo is AGPL software, so the network-copyleft obligation applies if you modify it and serve users without publishing source. The vendor sells paid lifetime licenses on its site, which buy support and features rather than permission.

Self-hosting the Community Edition is free. The vendor site publishes two one-time licenses: Professional at $5,000 with three months of support, and Enterprise at $10,000 with six months, adding multi-company and branch support, multi-currency, multiple languages, a headless API and public forms. The site&#x27;s own comparison table says Community is limited to one admin user, but the AGPL-3.0 license in the repository carries no user limit, so treat the cap as a commercial position, not a code enforcement.

No, not in the open-source edition. SuiteCRM and Dolibarr ship leads, pipelines, cases, campaigns and role-based teams; IDURAR&#x27;s repository has three application models (clients, invoices, payments) and a single owner role. It competes as a developer base for custom billing and customer invoicing tools, where its small MERN codebase and generated REST routes are the advantage. If the requirement is a CRM your team configures in the admin UI, the config-first open-source CRMs are the better fit.

## Similar Tools

## Related reading

- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [AI watermarks are now part of your agent's risk surface](/blog/watermark-provenance-tax-agents/)
- [Your agent protocol matters less than your data plumbing](/blog/agent-protocol-vs-data-plumbing/)
### Quick Facts

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/idurar-erp-crm/#app",
    "name": "IDURAR ERP & CRM",
    "description": "Free Open Source ERP CRM Software Accounting Invoicing | Node.Js React",
    "image": "https://martechsignal.com/og/tools/idurar-erp-crm.png",
    "url": "https://martechsignal.com/tools/idurar-erp-crm/",
    "sameAs": [
      "https://cloud.idurarapp.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/idurar-erp-crm/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-07",
    "datePublished": "2026-08-25",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://www.idurarapp.com",
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
        "name": "IDURAR ERP & CRM",
        "item": "https://martechsignal.com/tools/idurar-erp-crm/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is IDURAR ERP & CRM?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Free Open Source ERP CRM Software Accounting Invoicing | Node.Js React. It ships with 8,776 GitHub stars, an API for custom integrations. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does IDURAR ERP & CRM cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "IDURAR ERP & CRM is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 8,776 stars. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is IDURAR ERP & CRM a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A compact AGPL starting point for custom MERN invoicing and payments work, not a deployable CRM suite: read the three model files before you believe any feature list."
        }
      },
      {
        "@type": "Question",
        "name": "Is IDURAR open source or fair-code?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The license file is standard AGPL-3.0 with no added clauses, and the README says IDURAR is free for personal or commercial use. The fair-code label comes from the project's own copy: the README uses both phrases in different lines and the backend package.json still declares a Fair-code License, which does not match the license file. Functionally the repo is AGPL software, so the network-copyleft obligation applies if you modify it and serve users without publishing source. The vendor sells paid lifetime licenses on its site, which buy support and features rather than permission."
        }
      },
      {
        "@type": "Question",
        "name": "What does IDURAR cost, and what do the paid licenses include?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Self-hosting the Community Edition is free. The vendor site publishes two one-time licenses: Professional at $5,000 with three months of support, and Enterprise at $10,000 with six months, adding multi-company and branch support, multi-currency, multiple languages, a headless API and public forms. The site's own comparison table says Community is limited to one admin user, but the AGPL-3.0 license in the repository carries no user limit, so treat the cap as a commercial position, not a code enforcement."
        }
      },
      {
        "@type": "Question",
        "name": "Can IDURAR replace SuiteCRM or Dolibarr for a sales team?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No, not in the open-source edition. SuiteCRM and Dolibarr ship leads, pipelines, cases, campaigns and role-based teams; IDURAR's repository has three application models (clients, invoices, payments) and a single owner role. It competes as a developer base for custom billing and customer invoicing tools, where its small MERN codebase and generated REST routes are the advantage. If the requirement is a CRM your team configures in the admin UI, the config-first open-source CRMs are the better fit."
        }
      }
    ]
  }
]
```
