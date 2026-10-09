# Twenty review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- Twenty
Re-check pending: pricing last verified 2026-09-07 (32 days ago).

## Twenty review (2026): pricing, AI features, verdict

The open-source alternative to Salesforce, designed for AI with modern CRM workflows

CRM · Open Source from $9/user/mo Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Twenty →](https://twenty.com)

[How we review](/methodology/) · No affiliate links

**Verdict:** Twenty is a tool in CRM with free and open source. The catalog documents 4 AI features, 7 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

[Visit Twenty →](https://twenty.com)

## MartechSignal Score: 42/60

Twenty is the strongest open-source bet for teams that want Salesforce-shaped CRM data on their own server and are willing to run a young codebase. The AI workspace features are real, but the project is three years old and the premium-feature split is still settling.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Self-hosted core is free under AGPLv3 with Pro features included; Cloud Pro is $9/user/mo billed yearly and Organization $19/user/mo, with premium features gated behind an Enterprise key (the vendor pricing page: [pricing page](https://twenty.com/pricing), verified 2026-09-07). |
| Feature depth | 7/10 | Objects, workflows, email sync and dashboards cover the CRM baseline; workflow AI agents and AI-built dashboards push past it, though marketing campaign tooling is absent (vendor documentation: [vendor site](https://twenty.com), verified 2026-09-28). |
| Integrations | 6/10 | Gmail, Outlook and CalDAV sync plus signed webhooks and REST/GraphQL APIs ship in core; there is no connector marketplace to extend beyond that (vendor documentation: [vendor site](https://twenty.com), verified 2026-09-28). |
| AI capability | 7/10 | An AI chatbot over workspace data, agents inside workflows and a native MCP server on cloud workplaces put it ahead of most CRM peers (vendor documentation: [vendor site](https://twenty.com), verified 2026-09-28). |
| Openness | 9/10 | AGPLv3 with all Pro features in the free self-hosted tier; only premium add-ons need a paid key (the source repository: [repository](https://github.com/twentyhq/twenty), verified 2026-09-28). |
| Operational maturity | 5/10 | Founded 2023 with fast shipping, but no decade of operational history and the enterprise support tier is still forming (vendor documentation: [vendor site](https://twenty.com), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Twenty is an open-source CRM that bills itself as the open alternative to Salesforce, designed for AI: TypeScript and NestJS on PostgreSQL and Redis, a React frontend, GraphQL and REST APIs generated from your workspace schema, and an apps SDK for building custom objects, logic functions, and React components that render inside the product. Standard objects cover companies, people, opportunities, tasks, and notes, and custom objects get the same first-class treatment: API endpoints, views, permissions, and workflow triggers, with 20-plus field types, many-to-many relations, and no limits on objects or fields on any plan. The project is unusually honest about fit: its docs name startups with technical founders, agencies fluent in TypeScript, and privacy-conscious organizations that want to self-host, while pointing teams that want a CRM they never think about to Pipedrive or HubSpot. Documented AI is narrower than the tagline suggests: an AI chatbot with access to workspace data, AI agents inside workflows (enrichment from public sources, auto-drafting email replies), AI-built dashboards, and a native MCP server on cloud workspaces, which the site claims but the docs do not yet document. Integrations center on Gmail, Google Calendar, Outlook, and Microsoft Calendar, with IMAP, SMTP, and CalDAV for anything else, signed outbound webhooks on every object including custom ones, and a five-app marketplace (Slack, Exa, People Data Labs, and others). There is no mobile app and no static API reference, because each workspace has its own schema. Self-hosting is free and carries all Pro features on Docker Compose (2 GB RAM minimum, PostgreSQL 15 or newer, and losing ENCRYPTION_KEY loses every stored secret); premium features such as SSO and audit logs need a paid Enterprise key even self-hosted. Cloud Pro is $9 per user per month billed yearly, Organization is $19, and Enterprise starts at $50,000 a year. At 56,000-plus stars with several tagged releases a week, it is the fastest-moving CRM here, and it reads like it.

Twenty homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI Chatbot with access to your workspace data
- AI Agents in Workflows
- AI-built dashboards
- Native MCP server on cloud workspaces (site claim)
## Key Integrations

- Gmail & Google Calendar
- Outlook & Microsoft Calendar
- IMAP / SMTP / CalDAV
- Signed outbound webhooks
- REST + GraphQL API
- SAML 2.0 SSO (Organization plan)
- Marketplace: Slack, Exa, People Data Labs
## Pricing

Twenty is free to self-host under the AGPL-3.0 licence, paid plans start at $9/user/mo as of 2026-09.

Self-hosted free (AGPLv3 core; all Pro features included, premium features need a paid Enterprise key). Cloud Pro $9/user/mo billed yearly, Organization $19/user/mo, Enterprise from $50k/yr. 30-day trial with card, 7 days without.

Current plans and limits live on the [Twenty pricing page](https://twenty.com/pricing).

## How to install

- One-line installer: bash <(curl -sL https://raw.githubusercontent.com/twentyhq/twenty/main/packages/twenty-docker/scripts/install.sh), optionally prefixed with VERSION=vx.y.z to pin a release.
- Manual Docker Compose: download .env.example and docker-compose.yml from packages/twenty-docker, generate ENCRYPTION_KEY with openssl rand -base64 32, then docker compose up -d. The stack is server, worker, db (postgres:16), and redis, and the app answers on http://localhost:3000.
- Storage defaults to local (STORAGE_TYPE=local) with S3 variables commented out in .env; Postgres settings are assembled into PG_DATABASE_URL by the compose file, so there is no DATABASE_URL variable to set.
- Upgrade: back up first with docker exec {db_container} pg_dumpall -U {user} > databases_backup.sql, then docker compose down, change TAG in .env, and docker compose up -d. Migrations run automatically, and instances on v1.23 or later can jump straight to the latest version.
- Cloud alternative: signup starts a 30-day trial with a card or 7 days without; Twenty Cloud runs on AWS in Frankfurt, Germany, and region selection is promised from 2027.
## Requirements

Docker Compose with at least 2 GB RAM (the docs warn that low memory causes crashes), PostgreSQL 15 or newer, and a domain if you expose it beyond localhost. ENCRYPTION_KEY is critical: the docs state that losing it means losing access to every secret stored in the database, with FALLBACK_ENCRYPTION_KEY for rotations. Outbound-call protection blocks private IPs, so self-hosters with LAN mail or calendar servers set OUTBOUND_HTTP_SAFE_MODE_ENABLED=false. Config lives in an admin panel by default; PG_DATABASE_URL, SERVER_URL, and the encryption keys are env-only.

## Best for

Technical teams that want to build their CRM rather than configure one: GTM teams writing their own lead scoring, enrichment, and outbound workflows, agencies fluent in TypeScript and React, and organizations that must self-host and own their data end to end. The docs' own list adds enterprises replacing Salesforce and Salesforce partners tired of license increases.

## Not for

Teams that want a CRM they never think about, which the docs redirect to Pipedrive or HubSpot, and companies that need hundreds of pre-built integrations today. There is no mobile app, native email campaigns are not shipped, webhook event filtering is still future work, attachments sync is promised for H1 2026, and bringing your own AI model self-hosted requires an Organization license.

## Review notes

Assessed from twenty.com, docs.twenty.com (a 971KB docs corpus fetched through its published llms.txt), the GitHub repo, and the release feed in September 2026; we have not deployed an instance. Activity is the strongest signal: v2.39.0 shipped September 7, 2026, five releases landed in the prior week, and the repo was pushed the day before we checked. The vendor changelog page lags GitHub, which matters if you track versions.

The correction that matters: our earlier record listed AI-powered data enrichment, an AI email assistant, and smart relationship insights. None are documented features. The docs' own AI FAQ names exactly two capabilities, an AI Chatbot with access to workspace data and AI Agents in Workflows, and smart relationship insights appears nowhere in the 971KB corpus. We have replaced the list with documented capabilities and flagged the MCP server as a site claim that has not reached the docs.

Second correction: the license is not plain AGPLv3. The LICENSE file applies AGPLv3 to most of the code, carves out Enterprise-licensed files that require a paid subscription for production use, licenses the SDK and UI packages under MIT, and adds an AGPLv3 section 7 exception. Self-hosting genuinely includes all Pro features at no cost, but SSO, row-level permissions, audit logs, unlimited workspaces, and private source code need a paid Enterprise key even on your own servers.

What the docs do well: an explicit who-Twenty-is-not-for list, metered logic-function pricing published at Lambda-style rates ($0.0001 per invocation plus $0.0001 per second of runtime), and legal FAQs that state where cloud data lives (AWS Frankfurt), that soft-deleted records purge after 14 days and backups after 30, and that CRM content can train sub-processor models depending on their terms, with a settings path to disable AI entirely.

## Verdict

The fastest-moving open-source CRM in this directory, honest about its limits and genuinely free to self-host at the Pro tier; adopt it as a platform you build on, not a finished product you switch on.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ AGPL-3.0 licence with free self-hosting | ✗ Paid plans start at $9/user/mo |
| ✓ AI capabilities: AI Chatbot with access to your workspace data |  |
| ✓ Active public repository (58,108 GitHub stars counted at last check) |  |
| ✓ Native integrations include Gmail & Google Calendar, Outlook & Microsoft Calendar, IMAP / SMTP / CalDAV (7 listed) |  |

## Related concepts

- [CRM](/glossary/crm/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
- [Customer journey](/glossary/customer-journey/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Twenty?**
Twenty: The open-source alternative to Salesforce, designed for AI with modern CRM workflows. Twenty ships with AI Chatbot with access to your workspace data. The public repository carries 58,108 stars.

**How much does Twenty cost?**
Twenty has a free tier; paid plans start at $9/user/mo. Self-hosted free (AGPLv3 core; all Pro features included, premium features need a paid Enterprise key). Cloud Pro $9/user/mo billed yearly, Organization $19/user/mo, Enterprise from $50k/yr. 30-day trial with card, 7 days without. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Twenty a good self-hosted CRM tool in 2026?**
The fastest-moving open-source CRM in this directory, honest about its limits and genuinely free to self-host at the Pro tier; adopt it as a platform you build on, not a finished product you switch on.

**Is Twenty really free to self-host?**
The self-hosted free plan includes all Pro features at no cost, confirmed both by the docs plan table and the LICENSE's AGPLv3 core. What is not free: SSO, row-level permissions, audit logs, unlimited workspaces, and access to the private source code are Enterprise Edition features that require a paid key, bought through Stripe and pasted under Settings, Admin Panel, Enterprise, whether you run cloud or self-host. Enterprise files in the repo carry a commercial license and are cleared for production use only with that subscription.

**Can I migrate from Salesforce or HubSpot to Twenty?**
Through CSV import or the API (the pricing FAQ suggests the API for 50,000-plus records), but the docs are clear it is a mapping exercise rather than a connector: Accounts map to Companies, Contacts to People, Deals to Opportunities, and Activities to Tasks or Notes. Users must be invited before the import, custom fields must exist before rows arrive, and views, workflows, and permissions must be recreated manually afterward.

**Does Twenty train AI models on my CRM data?**
Twenty has no model of its own; the legal FAQ states that CRM content can be used to train AI models depending on the terms of its AI sub-processors, which is as much as it can control. You can turn AI off completely by disabling all models under Settings, AI, Models. Cloud data sits on AWS in Frankfurt, Germany, sub-processors are listed at trust.twenty.com, and EU standard contractual clauses apply.

## Similar Tools

- [Cordys CRM](/tools/cordys-crm/): Open-source AI CRM with built-in agents, conversational analytics, and private deployment
- [Warpdrive](/tools/warpdrive/): Self-hosted open-source Pipedrive alternative for BD teams: pipelines and Gmail on your own box
- [n8n](/tools/n8n/): Open-source workflow automation platform with AI agent capabilities and 400+ nodes
- [Budibase](/tools/budibase/): Open-source operations platform for building AI agents, apps and automations on your own data
- [Attio](/tools/attio/): AI-native CRM with real-time data enrichment and agentic revenue workflows
## Related reading

- [Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough](/blog/salesforce-claude-commerce-cloud-agentforce/)
- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
- [The fully open-source agentic marketing stack you can run today: 19 MCP servers, one agent](/blog/open-source-agentic-martech-stack-mcp/)
## Also featured in

- [Best open-source CRM tools (2026)](/best/open-source-crm/) — Best for technically fluent teams wanting a modern extensible CRM.
- [Best Open-Source Marketing Tools (2026): 8 compared](/best/open-source-marketing-tools/) — CRM teams that want open source without accepting feature poverty
### Quick Facts

- **Pricing:** Open Source from $9/user/mo
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 58108
- **Founded:** 2023
- **HQ:** Paris, France
- **API:** Yes
- **Repository checked:** 2026-10-09
- **Page updated:** 2026-09-07

Related guides: [Twenty in Hubspot Crm alternatives](/alternatives/hubspot-crm/) · [Open Source Crm](/best/open-source-crm/) · [Open Source Marketing Tools](/best/open-source-marketing-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
