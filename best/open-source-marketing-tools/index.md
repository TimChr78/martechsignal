# Best Open-Source Marketing Automation Tools (2026): 8 compared


| Tool | Pricing | Public API | Verdict |
| --- | --- | --- | --- |
| [Mautic](/tools/mautic/) | Open Source | yes | Marketing teams that want HubSpot-class automation they can host themselves |
| [Listmonk](/tools/listmonk/) | Open Source | yes | Newsletter and lifecycle email at one list price, with no per-contact billing |
| [Laudspeaker](/tools/laudspeaker/) | Open Source | yes | Lifecycle messaging and onboarding journeys that live outside the CRM |
| [SuiteCRM](/tools/suitecrm/) | Open Source | yes | Sales teams that want a mature, enterprise-shaped CRM they control |
| [n8n](/tools/n8n/) | Open Source | yes | Workflow teams that want automation they can audit line by line |
| [Matomo](/tools/matomo/) | Open Source | yes | Analytics teams that want traffic data on servers they control |
| [Twenty](/tools/twenty/) | Open Source | yes | CRM teams that want open source without accepting feature poverty |
| [OpenOutreach](/tools/openoutreach/) | Open Source | no | Email marketing teams that want agent-written openers and self-hosting |

[Analytics & Attribution](/categories/analytics/)[CRM](/categories/crm/)[Email Marketing](/categories/email-marketing/)[Marketing Automation](/categories/marketing-automation/)[Open-Source Tools](/categories/open-source/)[Workflow Automation](/categories/workflow-automation/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

## Best Open-Source Marketing Tools (2026): 8 compared

Mautic comes first: HubSpot-class automation you host yourself. Listmonk sends newsletters with no per-contact billing. Laudspeaker runs lifecycle messaging outside the CRM. SuiteCRM covers sales. Everything here self-hosts free, so hosting effort is the price you actually pay. The other four play the same game in narrower lanes; the table below lines them up.

**Our top pick: [Mautic](#mautic)** — Marketing teams that want HubSpot-class automation they can host themselves [Try Mautic](https://www.mautic.org)

Last verified 2026-09-28.

## How we picked

The directory's open-source badge marks tools whose code and terms are public. These eight are where a marketing team should start, ordered by how directly they answer the job: Mautic for marketing automation first, newsletter and messaging engines next, then CRM, automation glue, and analytics. Scored tools come first. Nobody pays for placement.

Considered and excluded, with reasons: Odoo Community (ERP-first; we have not reviewed it to catalog depth), Keila (newsletter-focused; not yet in our directory), EspoCRM (a fine lightweight CRM that SuiteCRM and Twenty cover here), Dolibarr (accounting and ERP first), NocoDB (an Airtable alternative, not marketing), React Email Editor (a component library, not a product), and Claude SEO (SEO tooling rather than marketing automation; we review it hands-on elsewhere).

Everything here is desk-researched from vendor documentation and our own catalog. Each tool page shows the date we last checked it. This is not a hands-on test. Prices appear exactly as the catalog records them.

## What we checked and when

Pricing checked 2026-09-28 against each vendor's own pricing page · API availability confirmed from public documentation · Integrations read from vendor listings and source repositories. Not installed and not benchmarked: this is desk research with dates on it.

What we could not verify is called out under each tool below.

## Browse the hubs behind these picks

**Guide:** [automation strategy](/guides/workflow-automation-strategy/) · **Guide:** [MCP and agent protocols](/guides/mcp-agent-protocols/) · [automation strategy](/guides/workflow-automation-strategy/)

## Open-source momentum, with receipts

Star counts we snapshot ourselves every morning — check any of them against GitHub in one click.

- Mautic — 10,575 stars, +189 in the 36-snapshot window to 2026-09-29 10,386→10,575 [verify on GitHub](https://github.com/mautic/mautic)
- Listmonk — 23,611 stars, +490 in the 36-snapshot window to 2026-09-29 23,121→23,611 [verify on GitHub](https://github.com/knadh/listmonk)
- Laudspeaker — 2,626 stars, +8 in the 36-snapshot window to 2026-09-29 2,618→2,626 [verify on GitHub](https://github.com/laudspeaker/laudspeaker)
- SuiteCRM — 5,774 stars, +84 in the 36-snapshot window to 2026-09-29 5,690→5,774 [verify on GitHub](https://github.com/SuiteCRM/SuiteCRM)
- n8n — 206,232 stars, +3,829 in the 36-snapshot window to 2026-09-29 202,403→206,232 [verify on GitHub](https://github.com/n8n-io/n8n)
- Matomo — 21,908 stars, +103 in the 36-snapshot window to 2026-09-29 21,805→21,908 [verify on GitHub](https://github.com/matomo-org/matomo)
- Twenty — 57,682 stars, +2,157 in the 36-snapshot window to 2026-09-29 55,525→57,682 [verify on GitHub](https://github.com/twentyhq/twenty)
- OpenOutreach — 3,106 stars, +288 in the 36-snapshot window to 2026-09-29 2,818→3,106 [verify on GitHub](https://github.com/eracle/OpenOutreach)
[All movers on the trending page](/trending/).

## [Mautic](/tools/mautic/)

Mautic is the longest-running open-source marketing automation platform: email, landing pages, forms, segments, campaigns, contact scoring, and multi-channel messaging across email, SMS, web notifications, and mobile push, all self-hosted under GPL-3.0. Started in 2014, it has been community-governed since Acquia acquired Mautic Inc. in May 2019; the trademark is now held by fiscal host Open Source Collective and operations run through an elected Mautic Council, with Acquia and Dropsolid the largest funders. Around 10,472 GitHub stars, eleven bundled plugin packages, and translations into 70 languages reflect that community. The current line is 7.x (7.2.0 shipped in September 2026) and its requirements are serious: PHP 8.2 or newer, minimums raised to MySQL 8.4 and MariaDB 10.11 in the 7.0 release, npm for asset builds, mandatory cron jobs for segments, campaigns, and the email queue, and command-line-only updates, since browser updating was removed in 5.0. Shared hosting is explicitly discouraged. Campaigns, segments, and points-based lead scoring are deterministic rule engines; there is no AI anywhere, and the project's AI Manifesto states plainly that it hosts or maintains no AI services and remains AI-agnostic, so any Mautic AI pitch is a third-party layer rather than a product feature. Integrations are plugin-based: Salesforce, HubSpot, Pipedrive, Zoho, and Dynamics among CRMs, plus WordPress, Twilio, Mailchimp, Gmail and Outlook connectors, Google Tag Manager, Amazon S3, and Zapier. The project's own comparison page positions Mautic for organizations whose automation grows more complex over time and that need control over data governance and infrastructure with predictable costs rather than contact-based fees, while conceding HubSpot for teams that want a polished hosted experience. The software is free; money enters through partner Dropsolid's managed hosting (from € 247.50 a month, 14-day trial, no card) and paid Extended Long Term Support for older versions. The honest costs are operational: upgrades, backups, deliverability, and cron management are yours, and campaigns cannot be moved between instances. It starts free, and Free and open source (GPL-3.0), self-hosted. Managed hosting by official partner Dropsolid from € 247.50/mo with a 14-day no-card trial; paid Extended Long Term Support (ELTS) sold by the project for old versions. (verified 2026-09-07). The catalog documents 0 AI features, 10 integrations, a self-hosting path.

**Verdict:** Marketing teams that want HubSpot-class automation they can host themselves

Vendor: [Official site](https://www.mautic.org) · [Pricing](https://www.mautic.org/pricing) · [GitHub](https://github.com/mautic/mautic)

**Skip it if the team needs vendor-run SLAs and a polished UI over control; you run and update Mautic yourself.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Listmonk](/tools/listmonk/)

Built as an open-source, self-hosted mailing list manager, Listmonk gives marketing teams a lightweight way to run newsletters, subscriber lists, and email campaigns without relying on a hosted SaaS platform. Its Go backend is designed for speed and low operational overhead, while PostgreSQL handles subscriber and campaign data. The project is free under the AGPL license, with no paid tiers, and it exposes an API for custom workflows. It also supports practical integrations such as SMTP providers, Zapier, and WordPress, making it possible to connect signup forms, automation, and existing site infrastructure. Listmonk is a good fit for technical marketers, developers, and privacy-conscious organizations that want direct control over email infrastructure and subscriber data. Founded in 2019 and based in Bangalore, India, the project has attracted strong open-source interest, with 23,343 GitHub stars GitHub stars. Its AI capabilities are practical rather than central: AI-assisted template editing can help refine email layouts and copy, while AI campaign analytics can support performance review and optimization. These features sit alongside standard campaign tools such as segmentation, templates, and reporting. Compared with commercial alternatives such as Mailchimp, Campaign Monitor, or ActiveCampaign, Listmonk trades managed convenience for ownership, lower recurring costs, and greater flexibility. Teams will need to handle hosting, deliverability configuration, and maintenance themselves, so it is less suited to users who want a fully managed service. It is best for technically capable teams, indie publishers, SaaS companies, and nonprofits that want an open-source email platform with API access, self-hosted data control, and optional AI assistance for campaign production and analysis. It starts free, and Free and open-source (AGPL); self-hosted; no paid tiers (verified 2026-08-28). The catalog documents 2 AI features, 4 integrations, a self-hosting path.

**Verdict:** Newsletter and lifecycle email at one list price, with no per-contact billing

Vendor: [Official site](https://listmonk.app) · [Pricing](https://listmonk.app) · [GitHub](https://github.com/knadh/listmonk)

**Skip it if you need a full marketing suite; this is a newsletter and mailing engine, not a CRM.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Laudspeaker](/tools/laudspeaker/)

Designed as an open-source customer engagement and product onboarding platform, Laudspeaker helps teams automate lifecycle messaging without locking their data into a proprietary stack. It supports behavioral triggers, customer journey automation, and AI-powered messaging, allowing marketers and product teams to build sequences such as welcome flows, activation campaigns, re-engagement emails, in-app messages, and lifecycle nudges based on user actions. Because the platform is self-hostable and has an active GitHub presence with more than 2,622 stars, engineering teams can inspect the codebase, extend functionality, and connect it directly to their own data infrastructure through its API. The platform is aimed at startups, technical growth teams, and companies that want more control over their marketing automation stack than a closed SaaS tool typically provides. Its open-source model is the main differentiator: while commercial alternatives such as Braze offer polished hosted infrastructure and enterprise support, Laudspeaker offers a lower-cost entry point and greater flexibility for teams willing to manage deployment and maintenance. Pricing includes a free open-source self-hosted option, with cloud plans available for organizations that prefer managed hosting. AI capabilities are practical rather than experimental, focusing on message generation, trigger-based automation, and journey orchestration. Best for technical marketing and product teams that need an open-source alternative to Braze for customer engagement, onboarding automation, and behavioral messaging. It starts free, and Free open-source self-hosted; cloud plans available (verified 2026-08-28). The catalog documents 3 AI features, 0 integrations, a self-hosting path.

**Verdict:** Lifecycle messaging and onboarding journeys that live outside the CRM

Vendor: [Official site](https://laudspeaker.com/?ref=github) · [GitHub](https://github.com/laudspeaker/laudspeaker)

**Skip it if your journeys live in one app already; Laudspeaker earns its keep as the orchestration layer.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [SuiteCRM](/tools/suitecrm/)

SuiteCRM is the AGPLv3 open-source CRM that forked SugarCRM Community Edition and outlived it, maintained by SuiteCRM Ltd from Stirling, Scotland. Two release lines are current: 8.10.2 and 7.15.2 shipped on the same day in July 2026 as a joint security release, and 7.15 is an extended support release with security fixes published into 2028. The module set is the deepest in this directory's CRM category: leads, accounts, contacts, opportunities, quotes, invoices, contracts, PDF templates, campaigns with target lists and confirmed opt-in, surveys, events, cases with a knowledge base, bugs, reports with scheduled runs, calendar, projects, and document management, plus Studio for no-code layout changes and Module Builder for new entities from six templates. Workflow automation is free in the core, with calculated fields, which is the main structural difference from EspoCRM, where workflows are a paid extension. What SuiteCRM does not have matters too: there is no native AI anywhere in the documented feature set, and no official mobile app. Elasticsearch is an optional search backend, and Redis or RabbitMQ are optional message transports for background jobs beyond a single server. Two APIs are documented, the newer V8 API with OAuth and the legacy V4. Requirements are PHP 8.2 to 8.4 with MariaDB 10.6 or later, or MySQL 8.0 or later, on Apache 2.4. Installation is a pre-built zip with a permissions pass, then a browser wizard or a CLI installer with flags for the admin user, database, and demo data. Migrating from 7.x to 8.x is a documented fresh install with three console commands, not a patch. Commercial support is GBP-priced: hosting from 50 pounds monthly with unlimited users, and SuiteASSURED from 3,350 pounds a year carrying warranties and indemnities. This assessment is from the repository, the docs, and the vendor site. It starts free, and Free open-source self-hosted; paid cloud hosting available (verified 2026-09-07). The catalog documents 0 AI features, 0 integrations, a self-hosting path.

**Verdict:** Sales teams that want a mature, enterprise-shaped CRM they control

Vendor: [Official site](https://www.suitecrm.com) · [GitHub](https://github.com/SuiteCRM/SuiteCRM)

**Skip it if you want a modern UI out of the box; SuiteCRM wins on maturity, not looks.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [n8n](/tools/n8n/)

Built as a flexible, open-source automation framework, n8n lets marketing, operations, and technical teams connect apps, move data, and orchestrate multi-step processes through a visual workflow builder. It starts free, and self-hosted free (fair-code); Cloud Starter $20/mo; Pro $50/mo; Enterprise custom (verified 2026-08-28). The catalog documents 5 AI features, 8 integrations, a public API, and a self-hosting path.

**Verdict:** Workflow teams that want automation they can audit line by line

Vendor: [Official site](https://n8n.io) · [Pricing](https://n8n.io/pricing/) · [GitHub](https://github.com/n8n-io/n8n)

**Skip it if nobody on the team wants to run a server; the self-hosting is the trade you are making.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Matomo](/tools/matomo/)

Matomo is an open-source web analytics platform you run on your own infrastructure, licensed GPL v3 or later, with 5.13.0 released in August 2026 and an active 6.x branch. It starts free, and self-hosted core free (GPL v3+). On-Premise premium bundles: Team 275 €/mo, Business 1,450 €/mo, Enterprise 3,400 €/mo, about 17% less billed annually. Cloud from 22 €/mo for 50,000 hits, scaling to 14,850 €/mo at 100 million. 21-day Cloud trial (verified 2026-09-06). The catalog documents 4 AI features, 8 integrations, a public API, and a self-hosting path.

**Verdict:** Analytics teams that want traffic data on servers they control

Vendor: [Official site](https://matomo.org) · [Pricing](https://matomo.org/pricing/) · [GitHub](https://github.com/matomo-org/matomo)

**Skip it if you just need page counts; Matomo earns the setup when privacy or data ownership is the driver.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Twenty](/tools/twenty/)

Twenty is an open-source CRM that bills itself as the open alternative to Salesforce, designed for AI: TypeScript and NestJS on PostgreSQL and Redis, a React frontend, GraphQL and REST APIs generated from your workspace schema, and an apps SDK for building custom objects, logic functions, and React components that render inside the product. It starts free, and self-hosted free (AGPLv3 core; all Pro features included, premium features need a paid Enterprise key). Cloud Pro $9/user/mo billed yearly, Organization $19/user/mo, Enterprise from $50k/yr. 30-day trial with card, 7 days without (verified 2026-09-07). The catalog documents 4 AI features, 7 integrations, a public API, and a self-hosting path.

**Verdict:** CRM teams that want open source without accepting feature poverty

Vendor: [Official site](https://twenty.com) · [Pricing](https://twenty.com/pricing) · [GitHub](https://github.com/twentyhq/twenty)

**Skip it if you need deep marketing automation inside the CRM; Twenty is sales-record first.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [OpenOutreach](/tools/openoutreach/)

OpenOutreach is an open-source AI agent for B2B lead generation, and it inverts the usual cold-email workflow: you do not bring a list. It starts free, and free, GPLv3, self-hosted. You pay your own LLM keys and mailbox, plus BetterContact credits for discovery (1 credit per verified work email; free account includes 40 credits, no card) (verified 2026-09-07). The catalog documents 5 AI features, 9 integrations, and a self-hosting path.

**Verdict:** Email marketing teams that want agent-written openers and self-hosting

Vendor: [Official site](https://openoutreach.app) · [GitHub](https://github.com/eracle/OpenOutreach)

**Skip it if you already have a clean list and a sending habit; the agent-first workflow is for teams starting from zero.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

Every price quoted here comes from the vendor's own pricing page as catalogued on the tool page. Browse [all 163 tools](/tools/) or read [how we evaluate](/methodology/), or download the [machine-readable catalog](/catalog-tools.json).

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Best Open-Source Marketing Tools (2026): 8 compared",
    "datePublished": "2026-09-27",
    "dateModified": "2026-09-28",
    "author": {
      "@type": "Person",
      "@id": "https://martechsignal.com/authors/tim-christensen/#person",
      "name": "Tim Christensen",
      "url": "https://martechsignal.com/authors/tim-christensen/"
    },
    "numberOfItems": 8,
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Mautic",
        "item": {
          "@id": "https://martechsignal.com/tools/mautic/#app",
          "url": "https://martechsignal.com/tools/mautic/"
        }
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Listmonk",
        "item": {
          "@id": "https://martechsignal.com/tools/listmonk/#app",
          "url": "https://martechsignal.com/tools/listmonk/"
        }
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Laudspeaker",
        "item": {
          "@id": "https://martechsignal.com/tools/laudspeaker/#app",
          "url": "https://martechsignal.com/tools/laudspeaker/"
        }
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "SuiteCRM",
        "item": {
          "@id": "https://martechsignal.com/tools/suitecrm/#app",
          "url": "https://martechsignal.com/tools/suitecrm/"
        }
      },
      {
        "@type": "ListItem",
        "position": 5,
        "name": "n8n",
        "item": {
          "@id": "https://martechsignal.com/tools/n8n/#app",
          "url": "https://martechsignal.com/tools/n8n/"
        }
      },
      {
        "@type": "ListItem",
        "position": 6,
        "name": "Matomo",
        "item": {
          "@id": "https://martechsignal.com/tools/matomo/#app",
          "url": "https://martechsignal.com/tools/matomo/"
        }
      },
      {
        "@type": "ListItem",
        "position": 7,
        "name": "Twenty",
        "item": {
          "@id": "https://martechsignal.com/tools/twenty/#app",
          "url": "https://martechsignal.com/tools/twenty/"
        }
      },
      {
        "@type": "ListItem",
        "position": 8,
        "name": "OpenOutreach",
        "item": {
          "@id": "https://martechsignal.com/tools/openoutreach/#app",
          "url": "https://martechsignal.com/tools/openoutreach/"
        }
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
        "name": "Best-of lists",
        "item": "https://martechsignal.com/best/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Best Open-Source Marketing Tools (2026): 8 compared",
        "item": "https://martechsignal.com/best/open-source-marketing-tools/"
      }
    ]
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
