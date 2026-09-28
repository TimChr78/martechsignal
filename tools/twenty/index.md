# Twenty review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | the pricing block publishes Cloud Pro at $9 per user per month billed yearly, Organization at $19, Enterprise from $50,000 a year, and free self-hosting, and the Twenty tool page documents no limits on objects or fields on any plan. |
| Feature depth | 8/10 | The Twenty tool page documents standard CRM objects plus first-class custom objects with their own API endpoints, views, permissions, and workflow triggers and an apps SDK, which is category baseline plus real differentiators. |
| Integrations | 6/10 | tools.json lists Gmail, Google and Microsoft calendars, IMAP, SMTP, and CalDAV, signed webhooks, REST and GraphQL APIs, and a five-app marketplace including Slack and People Data Labs, which is an open API with a small native catalog and no iPaaS coverage documented. |
| AI capability | 7/10 | The Twenty tool page documents an AI chatbot over workspace data, AI agents inside workflows, and AI-built dashboards as shipped features, while its native MCP server is a site claim that the docs do not yet document. |
| Openness | 10/10 | tools.json records an AGPL-3.0 license with free Docker Compose self-hosting that includes Pro features, which meets the OSI open source plus self-hostable anchor. |
| Operational maturity | 8/10 | tools.json reports about 56,500 GitHub stars and the Twenty tool page reports several tagged releases a week from a Paris-based company selling enterprise plans, which is beyond steady cadence though published SLA terms are not in our sources. |


| Pros | Cons |
| --- | --- |
| &#10003; AGPL-3.0 licence with free self-hosting | &#10007; Paid plans start at $9/mo once past the free tier |
| &#10003; AI capabilities: AI Chatbot with access to your workspace data |  |
| &#10003; Established community (56,507 GitHub stars) |  |
| &#10003; Native integrations include Gmail &amp; Google Calendar, Outlook &amp; Microsoft Calendar, IMAP / SMTP / CalDAV (7 listed) |  |

**What is Twenty?**
The open-source alternative to Salesforce, designed for AI with modern CRM workflows. It ships with AI Chatbot with access to your workspace data, 56,507 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Twenty cost?**
Twenty has a free tier; paid plans start at $9/mo. Self-hosted free (AGPLv3 core; all Pro features included, premium features need a paid Enterprise key). Cloud Pro $9/user/mo billed yearly, Organization $19/user/mo, Enterprise from $50k/yr. 30-day trial with card, 7 days without. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Twenty a good self-hosted CRM tool in 2026?**
The fastest-moving open-source CRM in this directory, honest about its limits and genuinely free to self-host at the Pro tier; adopt it as a platform you build on, not a finished product you switch on.

**Is Twenty really free to self-host?**
The self-hosted free plan includes all Pro features at no cost, confirmed both by the docs plan table and the LICENSE&#x27;s AGPLv3 core. What is not free: SSO, row-level permissions, audit logs, unlimited workspaces, and access to the private source code are Enterprise Edition features that require a paid key, bought through Stripe and pasted under Settings, Admin Panel, Enterprise, whether you run cloud or self-host. Enterprise files in the repo carry a commercial license and are cleared for production use only with that subscription.

**Can I migrate from Salesforce or HubSpot to Twenty?**
Through CSV import or the API (the pricing FAQ suggests the API for 50,000-plus records), but the docs are clear it is a mapping exercise rather than a connector: Accounts map to Companies, Contacts to People, Deals to Opportunities, and Activities to Tasks or Notes. Users must be invited before the import, custom fields must exist before rows arrive, and views, workflows, and permissions must be recreated manually afterward.

**Does Twenty train AI models on my CRM data?**
Twenty has no model of its own; the legal FAQ states that CRM content can be used to train AI models depending on the terms of its AI sub-processors, which is as much as it can control. You can turn AI off completely by disabling all models under Settings, AI, Models. Cloud data sits on AWS in Frankfurt, Germany, sub-processors are listed at trust.twenty.com, and EU standard contractual clauses apply.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 56507
- **Founded:** 2023
- **HQ:** Paris, France
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Twenty is a tool in CRM with free and open source. The catalog documents 4 AI features, 7 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Cordys CRM

Open-source AI CRM with built-in agents, conversational analytics, and private deployment

Warpdrive

Self-hosted open-source Pipedrive alternative for BD teams: pipelines and Gmail on your own box

n8n

Open-source workflow automation platform with AI agent capabilities and 400+ nodes

Budibase

Open-source operations platform for building AI agents, apps and automations on your own data

Attio

AI-native CRM with real-time data enrichment and agentic revenue workflows

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- Twenty
## Twenty review (2026): pricing, AI features, verdict

The open-source alternative to Salesforce, designed for AI with modern CRM workflows

CRM · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[How we review](/methodology/) · No affiliate links

[Visit Twenty &#8594;](https://twenty.com)

## MartechSignal Score: 48/60

Twenty pairs genuine open source code with published cloud pricing, so a team can price a rollout before talking to anyone. Its AI story is narrower than the marketing suggests and the native integration list is short, but for a technical team that wants a self-hosted CRM with real APIs it is the strongest all-round pick in this batch.

Scored 2026-09-26 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Twenty is an open-source CRM that bills itself as the open alternative to Salesforce, designed for AI: TypeScript and NestJS on PostgreSQL and Redis, a React frontend, GraphQL and REST APIs generated from your workspace schema, and an apps SDK for building custom objects, logic functions, and React components that render inside the product. Standard objects cover companies, people, opportunities, tasks, and notes, and custom objects get the same first-class treatment: API endpoints, views, permissions, and workflow triggers, with 20-plus field types, many-to-many relations, and no limits on objects or fields on any plan. The project is unusually honest about fit: its docs name startups with technical founders, agencies fluent in TypeScript, and privacy-conscious organizations that want to self-host, while pointing teams that want a CRM they never think about to Pipedrive or HubSpot. Documented AI is narrower than the tagline suggests: an AI chatbot with access to workspace data, AI agents inside workflows (enrichment from public sources, auto-drafting email replies), AI-built dashboards, and a native MCP server on cloud workspaces, which the site claims but the docs do not yet document. Integrations center on Gmail, Google Calendar, Outlook, and Microsoft Calendar, with IMAP, SMTP, and CalDAV for anything else, signed outbound webhooks on every object including custom ones, and a five-app marketplace (Slack, Exa, People Data Labs, and others). There is no mobile app and no static API reference, because each workspace has its own schema. Self-hosting is free and carries all Pro features on Docker Compose (2 GB RAM minimum, PostgreSQL 15 or newer, and losing ENCRYPTION_KEY loses every stored secret); premium features such as SSO and audit logs need a paid Enterprise key even self-hosted. Cloud Pro is $9 per user per month billed yearly, Organization is $19, and Enterprise starts at $50,000 a year. At 56,000-plus stars with several tagged releases a week, it is the fastest-moving CRM here, and it reads like it.

Twenty homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI Chatbot with access to your workspace data
- AI Agents in Workflows
- AI-built dashboards
- Native MCP server on cloud workspaces (site claim)
## Key Integrations

- Gmail &amp; Google Calendar
- Outlook &amp; Microsoft Calendar
- IMAP / SMTP / CalDAV
- Signed outbound webhooks
- REST + GraphQL API
- SAML 2.0 SSO (Organization plan)
- Marketplace: Slack, Exa, People Data Labs
## Pricing

Twenty is free to self-host under the AGPL-3.0 licence, paid plans start at $9/mo as of 2026-09.

Self-hosted free (AGPLv3 core; all Pro features included, premium features need a paid Enterprise key). Cloud Pro $9/user/mo billed yearly, Organization $19/user/mo, Enterprise from $50k/yr. 30-day trial with card, 7 days without.

Current plans and limits live on the [Twenty pricing page](https://twenty.com/pricing).

## How to install

- One-line installer: bash &lt;(curl -sL https://raw.githubusercontent.com/twentyhq/twenty/main/packages/twenty-docker/scripts/install.sh), optionally prefixed with VERSION=vx.y.z to pin a release.
- Manual Docker Compose: download .env.example and docker-compose.yml from packages/twenty-docker, generate ENCRYPTION_KEY with openssl rand -base64 32, then docker compose up -d. The stack is server, worker, db (postgres:16), and redis, and the app answers on http://localhost:3000.
- Storage defaults to local (STORAGE_TYPE=local) with S3 variables commented out in .env; Postgres settings are assembled into PG_DATABASE_URL by the compose file, so there is no DATABASE_URL variable to set.
- Upgrade: back up first with docker exec {db_container} pg_dumpall -U {user} &gt; databases_backup.sql, then docker compose down, change TAG in .env, and docker compose up -d. Migrations run automatically, and instances on v1.23 or later can jump straight to the latest version.
- Cloud alternative: signup starts a 30-day trial with a card or 7 days without; Twenty Cloud runs on AWS in Frankfurt, Germany, and region selection is promised from 2027.
## Requirements

Docker Compose with at least 2 GB RAM (the docs warn that low memory causes crashes), PostgreSQL 15 or newer, and a domain if you expose it beyond localhost. ENCRYPTION_KEY is critical: the docs state that losing it means losing access to every secret stored in the database, with FALLBACK_ENCRYPTION_KEY for rotations. Outbound-call protection blocks private IPs, so self-hosters with LAN mail or calendar servers set OUTBOUND_HTTP_SAFE_MODE_ENABLED=false. Config lives in an admin panel by default; PG_DATABASE_URL, SERVER_URL, and the encryption keys are env-only.

## Best for

Technical teams that want to build their CRM rather than configure one: GTM teams writing their own lead scoring, enrichment, and outbound workflows, agencies fluent in TypeScript and React, and organizations that must self-host and own their data end to end. The docs&#x27; own list adds enterprises replacing Salesforce and Salesforce partners tired of license increases.

## Not for

Teams that want a CRM they never think about, which the docs redirect to Pipedrive or HubSpot, and companies that need hundreds of pre-built integrations today. There is no mobile app, native email campaigns are not shipped, webhook event filtering is still future work, attachments sync is promised for H1 2026, and bringing your own AI model self-hosted requires an Organization license.

## Review notes

Assessed from twenty.com, docs.twenty.com (a 971KB docs corpus fetched through its published llms.txt), the GitHub repo, and the release feed in September 2026; we have not deployed an instance. Activity is the strongest signal: v2.39.0 shipped September 7, 2026, five releases landed in the prior week, and the repo was pushed the day before we checked. The vendor changelog page lags GitHub, which matters if you track versions.

The correction that matters: our earlier record listed AI-powered data enrichment, an AI email assistant, and smart relationship insights. None are documented features. The docs&#x27; own AI FAQ names exactly two capabilities, an AI Chatbot with access to workspace data and AI Agents in Workflows, and smart relationship insights appears nowhere in the 971KB corpus. We have replaced the list with documented capabilities and flagged the MCP server as a site claim that has not reached the docs.

Second correction: the license is not plain AGPLv3. The LICENSE file applies AGPLv3 to most of the code, carves out Enterprise-licensed files that require a paid subscription for production use, licenses the SDK and UI packages under MIT, and adds an AGPLv3 section 7 exception. Self-hosting genuinely includes all Pro features at no cost, but SSO, row-level permissions, audit logs, unlimited workspaces, and private source code need a paid Enterprise key even on your own servers.

What the docs do well: an explicit who-Twenty-is-not-for list, metered logic-function pricing published at Lambda-style rates ($0.0001 per invocation plus $0.0001 per second of runtime), and legal FAQs that state where cloud data lives (AWS Frankfurt), that soft-deleted records purge after 14 days and backups after 30, and that CRM content can train sub-processor models depending on their terms, with a settings path to disable AI entirely.

## Verdict

The fastest-moving open-source CRM in this directory, honest about its limits and genuinely free to self-host at the Pro tier; adopt it as a platform you build on, not a finished product you switch on.

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

The open-source alternative to Salesforce, designed for AI with modern CRM workflows. It ships with AI Chatbot with access to your workspace data, 56,507 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Twenty has a free tier; paid plans start at $9/mo. Self-hosted free (AGPLv3 core; all Pro features included, premium features need a paid Enterprise key). Cloud Pro $9/user/mo billed yearly, Organization $19/user/mo, Enterprise from $50k/yr. 30-day trial with card, 7 days without. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

The fastest-moving open-source CRM in this directory, honest about its limits and genuinely free to self-host at the Pro tier; adopt it as a platform you build on, not a finished product you switch on.

The self-hosted free plan includes all Pro features at no cost, confirmed both by the docs plan table and the LICENSE&#x27;s AGPLv3 core. What is not free: SSO, row-level permissions, audit logs, unlimited workspaces, and access to the private source code are Enterprise Edition features that require a paid key, bought through Stripe and pasted under Settings, Admin Panel, Enterprise, whether you run cloud or self-host. Enterprise files in the repo carry a commercial license and are cleared for production use only with that subscription.

Through CSV import or the API (the pricing FAQ suggests the API for 50,000-plus records), but the docs are clear it is a mapping exercise rather than a connector: Accounts map to Companies, Contacts to People, Deals to Opportunities, and Activities to Tasks or Notes. Users must be invited before the import, custom fields must exist before rows arrive, and views, workflows, and permissions must be recreated manually afterward.

Twenty has no model of its own; the legal FAQ states that CRM content can be used to train AI models depending on the terms of its AI sub-processors, which is as much as it can control. You can turn AI off completely by disabling all models under Settings, AI, Models. Cloud data sits on AWS in Frankfurt, Germany, sub-processors are listed at trust.twenty.com, and EU standard contractual clauses apply.

## Similar Tools

## Related reading

- [Your Agents Are Only as Smart as Your Identity Debt](/blog/agents-identity-debt/)
- [Your agent protocol matters less than your data plumbing](/blog/agent-protocol-vs-data-plumbing/)
- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
### Quick Facts

Related guides: [Twenty in Hubspot Crm alternatives](/alternatives/hubspot-crm) · [Open Source Crm](/best/open-source-crm) · [Ai Crm Tools](/best/ai-crm-tools) · [Open Source Marketing Tools](/best/open-source-marketing-tools)

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/twenty/#app",
    "name": "Twenty",
    "description": "The open-source alternative to Salesforce, designed for AI with modern CRM workflows",
    "image": "https://martechsignal.com/og/tools/twenty.png",
    "url": "https://martechsignal.com/tools/twenty/",
    "sameAs": [
      "https://twenty.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/twenty/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-07",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 9,
      "priceCurrency": "USD",
      "url": "https://twenty.com/pricing",
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
        "name": "Twenty",
        "item": "https://martechsignal.com/tools/twenty/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Twenty?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The open-source alternative to Salesforce, designed for AI with modern CRM workflows. It ships with AI Chatbot with access to your workspace data, 56,507 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Twenty cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Twenty has a free tier; paid plans start at $9/mo. Self-hosted free (AGPLv3 core; all Pro features included, premium features need a paid Enterprise key). Cloud Pro $9/user/mo billed yearly, Organization $19/user/mo, Enterprise from $50k/yr. 30-day trial with card, 7 days without. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Twenty a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The fastest-moving open-source CRM in this directory, honest about its limits and genuinely free to self-host at the Pro tier; adopt it as a platform you build on, not a finished product you switch on."
        }
      },
      {
        "@type": "Question",
        "name": "Is Twenty really free to self-host?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The self-hosted free plan includes all Pro features at no cost, confirmed both by the docs plan table and the LICENSE's AGPLv3 core. What is not free: SSO, row-level permissions, audit logs, unlimited workspaces, and access to the private source code are Enterprise Edition features that require a paid key, bought through Stripe and pasted under Settings, Admin Panel, Enterprise, whether you run cloud or self-host. Enterprise files in the repo carry a commercial license and are cleared for production use only with that subscription."
        }
      },
      {
        "@type": "Question",
        "name": "Can I migrate from Salesforce or HubSpot to Twenty?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Through CSV import or the API (the pricing FAQ suggests the API for 50,000-plus records), but the docs are clear it is a mapping exercise rather than a connector: Accounts map to Companies, Contacts to People, Deals to Opportunities, and Activities to Tasks or Notes. Users must be invited before the import, custom fields must exist before rows arrive, and views, workflows, and permissions must be recreated manually afterward."
        }
      },
      {
        "@type": "Question",
        "name": "Does Twenty train AI models on my CRM data?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Twenty has no model of its own; the legal FAQ states that CRM content can be used to train AI models depending on the terms of its AI sub-processors, which is as much as it can control. You can turn AI off completely by disabling all models under Settings, AI, Models. Cloud data sits on AWS in Frankfurt, Germany, sub-processors are listed at trust.twenty.com, and EU standard contractual clauses apply."
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
    "reviewBody": "Twenty pairs genuine open source code with published cloud pricing, so a team can price a rollout before talking to anyone. Its AI story is narrower than the marketing suggests and the native integration list is short, but for a technical team that wants a self-hosted CRM with real APIs it is the strongest all-round pick in this batch.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/twenty/#app",
      "name": "Twenty",
      "url": "https://martechsignal.com/tools/twenty/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 48,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
