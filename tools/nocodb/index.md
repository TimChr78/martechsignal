# NocoDB review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Marketing Automation](/categories/marketing-automation/)
- NocoDB
Re-check pending: pricing last verified 2026-09-07 (29 days ago).

## NocoDB review (2026): pricing, AI features, verdict

Free, self-hostable Airtable alternative that turns any database into a smart spreadsheet

Marketing Automation · Open-core from $12/seat/mo · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit NocoDB →](https://nocodb.com)

[How we review](/methodology/) · No affiliate links

**Verdict:** NocoDB is a tool in Marketing Automation with free and open source. The catalog documents 3 AI features, 8 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

[Visit NocoDB →](https://nocodb.com)

## MartechSignal Score: 45/60

The shortest self-hosted route from spreadsheet sprawl to permissioned, API-covered bases over a database you own, with pricing that is fully visible. The license is fair-code rather than open source, and the features teams often want most, AI fields and advanced views, are paid.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 10/10 | nocodb.com/pricing documents the whole ladder with limits: self-hosted free with unlimited records and seats, Cloud Free (3 users, 1,000 records), Plus at 12 USD, Business at 24 USD and Scale at 45 USD per seat billed annually, with Enterprise the only quote-only item (the vendor pricing page: [pricing page](https://nocodb.com/pricing), verified 2026-09-26). |
| Feature depth | 7/10 | Six core views, forms, per-role permissions, conditional webhooks and workflows over your own Postgres or MySQL cover the baseline with the bring-your-own-database design as differentiator, while timeline, gantt and AI features sit behind paid tiers (vendor documentation: [vendor site](https://nocodb.com), verified 2026-09-26). |
| Integrations | 6/10 | REST API v3 with Swagger and conditional webhooks cover programmatic access over Postgres, MySQL and SQLite, but Slack, Discord, SES and S3 arrive through a paid App Store and no broad native catalog exists (vendor documentation: [vendor site](https://nocodb.com), verified 2026-09-26). |
| AI capability | 7/10 | NocoAI generates schemas, tables, views and formulas from prompts, AI button and AI prompt field types ship on paid tiers, and an MCP server gives agents record-level access to a base (vendor documentation: [vendor site](https://nocodb.com), verified 2026-09-26). |
| Openness | 7/10 | The Sustainable Use License is fair-code and source-available with free self-hosting and unlimited seats, but it is not OSI-approved and forbids offering NocoDB to others as a hosted service (the source repository: [repository](https://github.com/nocodb/nocodb), verified 2026-09-26). |
| Operational maturity | 8/10 | Calendar-versioned releases (2026.08.2 shipped September 3, 2026), full documentation and paid plans that carry support (vendor documentation: [vendor site](https://nocodb.com), verified 2026-09-26). |

Scored 2026-09-26 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

NocoDB turns a database you already run into an Airtable-style spreadsheet: point it at Postgres or MySQL and you get grids, forms, kanban, calendar and map views, per-role permissions, webhooks and REST APIs over tables your team owns. It is the largest project in this class at 65,195 GitHub stars, with calendar-versioned releases (2026.08.2 shipped September 3, 2026). The license comes first: NocoDB is published under the Sustainable Use License, a fair-code, source-available license rather than an OSI-approved one. Internal business use is fine and self-hosting is free with unlimited records and seats, but offering it to others as a hosted service requires a commercial license, so the open source label on the marketing site overstates it. Self-hosting is a one-command job: the docs quickstart brings up a compose stack (NocoDB, a background worker, Postgres, Redis) on port 8080, or you can run the Docker image against an existing Postgres by setting NC_DB. Docs list 2 vCPU and 2 GB RAM as the minimum. For marketing teams the fit is the spreadsheet sprawl that runs campaign ops: content calendars, launch checklists, partner and influencer trackers, budget tables and lead lists, with forms feeding them and webhooks pushing changes into the rest of the stack. Community edition includes the six core views, conditional webhooks with custom payloads, and two workflows per base; timeline, gantt and list views, the AI field types, most integrations (Slack, SES, S3) and sources beyond Postgres and MySQL (SQL Server, Oracle) are paid. Cloud plans run from a free three-user tier through Plus at $12 per seat monthly billed annually to Business at $24 with external database connections and SAML SSO. Compared with NocoBase or Budibase it is much faster to value, and compared with Airtable you trade polish and the integration catalog for ownership and SQL access. This assessment is based on the documented architecture and public materials.

NocoDB homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- NocoAI prompt-based schema, table, view and formula generation (paid)
- AI button and AI prompt field types (paid)
- MCP server for record-level agent access
## Key Integrations

- PostgreSQL
- MySQL
- SQLite
- REST APIs (v3) with Swagger
- Conditional webhooks with custom payloads
- MCP server
- Slack / Discord / Mattermost (paid App Store)
- AWS SES / SMTP / MailerSend (paid App Store)
## Pricing

NocoDB is open core: the self-hosted version is free, paid plans start at $12/seat/mo as of 2026-09.

Self-host free, unlimited records and seats (Sustainable Use License, fair-code). Cloud: Free (3 users, 1,000 records), Plus $12/seat/mo billed annually, Business $24 (external DB connections, SAML SSO), Scale $45, Enterprise custom.

Current plans and limits live on the [NocoDB pricing page](https://nocodb.com/pricing).

## How to install

- Quickstart: curl -fsSL https://install.nocodb.com/noco.sh | bash -s -- --quick generates a Compose stack (nocodb, a worker for background jobs, Postgres, Redis) and serves the app at http://localhost:8080. The first user to sign up becomes super admin.
- Production single-server: curl -fsSL https://install.nocodb.com/noco.sh | bash prompts for your domain, Postgres (bundled or existing), Redis and a Let's Encrypt email, then runs Traefik with automatic SSL in front.
- The README's auto-upstall variant, bash <(curl -sSL http://install.nocodb.com/noco.sh) <(mktemp), generates a docker-compose setup for a production server. Note the README publishes that URL with http while the docs use https.
- Docker against an existing Postgres: docker run -d --name noco -v "$(pwd)"/nocodb:/usr/app/data/ -p 8080:8080 -e NC_DB="pg://host.docker.internal:5432?u=root&p=password&d=d1" -e NC_AUTH_JWT_SECRET="569a1821-0a93-45e8-87ab-eb857f20a010" nocodb/nocodb:latest
- Sizing per the docs: minimum 2 vCPU, 2 GB RAM, 10 GB disk; recommended for production 4 vCPU, 8 GB RAM, 50 GB or more.
- Skip the binaries for anything serious: the README says the single-file downloads (curl http://get.nocodb.com/linux-x64 -o nocodb) are only for quick local testing, and building from source needs Node 22 or newer.
## Best for

Marketing ops teams that want Airtable-style shared bases over a Postgres or MySQL instance they own, without per-seat costs: content calendars, launch trackers, partner lists and form-fed lead lists, with webhooks and REST APIs into the rest of the stack.

## Not for

Teams that need an OSI-approved open-source license, want AI features or timeline and gantt views without paying, need SQL Server or Oracle sources outside enterprise plans, or are shopping for a full app platform with custom logic rather than a smart spreadsheet.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

NocoDB is a smart-spreadsheet layer over a database, and the bring-your-own-database part is the identity: you connect an external Postgres or MySQL instance as a data source, and bases, tables, views, forms and webhooks sit on top of your own tables. Two defaults matter for anyone pointing it at a production database: data editing is on and schema editing is off, and the docs advise leaving schema editing off unless you truly need it, so the default posture writes rows but does not alter your tables.

The marketing builds are the unglamorous ones that spreadsheets handle badly: content calendars with per-role edit rights, launch checklists, partner and influencer trackers, budget tables, and lead lists that a form feeds directly. Because views, forms and API tokens all sit over the same tables, the same base can serve an editor, a reviewer reading a shared view, and a script hitting the REST API. Community edition covers grid, gallery, form, kanban, calendar and map views, conditional webhooks with custom payloads, and two workflows per base with core nodes only.

The free-versus-paid line is worth reading before you commit, because several headline features sit above it. Timeline, gantt and list views are paid; every AI feature (NocoAI generation of schemas, tables, views and formulas, plus AI button and AI prompt field types) is paid; Slack, Discord, SES and S3 integrations come through the App Store on paid tiers; and SQL Server or Oracle as external sources are enterprise add-ons you request by email. Self-hosted community still gives you unlimited records, storage and seats, which is the part most teams want.

AI access is real but gated and bounded. NocoAI generates schemas, tables, views and formulas from prompts on cloud Plus and above, or on self-hosted Business and above with your own provider configured. The MCP server connects Claude Desktop, Claude Web, ChatGPT, Cursor and Windsurf to a base, and the docs state its limit plainly: it supports record-level operations only and does not handle table, field or metadata changes. Treat it as a data-entry and query surface for agents, not an admin surface.

This assessment is based on the repository, the docs at nocodb.com/docs and the release notes. Calibration notes from that reading: the README lags the docs (it omits the map view and interfaces), docs.nocodb.com now redirects into nocodb.com/docs, and versioning is calendar-based, so check the releases page rather than the package version when you evaluate freshness.

## Verdict

The shortest self-hosted path from spreadsheet chaos to a permissioned, API-covered base over your own database. Go in knowing the license is fair-code rather than open source, and that AI and the advanced views sit behind paid tiers.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ Open-source licensing with free self-hosting | ✗ Paid plans start at $12/seat/mo once past the free tier |
| ✓ AI capabilities: nocoAI prompt-based schema, table, view and formula generation (paid) |  |
| ✓ Active public repository (65,195 GitHub stars counted at last check) |  |
| ✓ Native integrations include PostgreSQL, MySQL, SQLite (8 listed) |  |

## Related concepts

- [Marketing automation](/glossary/marketing-automation/)
- [Customer journey](/glossary/customer-journey/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is NocoDB?**
NocoDB: Free, self-hostable Airtable alternative that turns any database into a smart spreadsheet. NocoDB ships with nocoAI prompt-based schema, table, view and formula generation (paid). The public repository carries 65,195 stars.

**How much does NocoDB cost?**
NocoDB has a free tier; paid plans start at $12/seat/mo. Self-host free, unlimited records and seats (Sustainable Use License, fair-code). Cloud: Free (3 users, 1,000 records), Plus $12/seat/mo billed annually, Business $24 (external DB connections, SAML SSO), Scale $45, Enterprise custom. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is NocoDB a good self-hosted Marketing Automation tool in 2026?**
The shortest self-hosted path from spreadsheet chaos to a permissioned, API-covered base over your own database. Go in knowing the license is fair-code rather than open source, and that AI and the advanced views sit behind paid tiers.

**Is NocoDB open source?**
Not in the OSI sense. The code is published under the Sustainable Use License, a fair-code, source-available license: you can use and modify it for internal business purposes and self-host free with unlimited records and seats, but you cannot offer it to third parties as a hosted service, and redistribution is limited to free, non-commercial use. It is the same class of license as n8n's. If your procurement or policy requirements name OSI-approved licenses, NocoDB does not qualify.

**NocoDB vs Airtable: what do you gain?**
Ownership and cost structure. Your data lives in your own Postgres or MySQL, self-hosting is free with unlimited seats, and every field is reachable through REST APIs and conditional webhooks. You give up Airtable's polish, interface depth and native integration catalog. On NocoDB Cloud the free tier holds three editors and 1,000 records and paid plans start at $12 per seat monthly billed annually. One gating detail surprises people: external database connections need the Business plan on cloud, so bring-your-own-Postgres is effectively a self-hosting feature.

**Can NocoDB use my existing Postgres or MySQL database?**
Yes, that is the core design: connect an external data source and NocoDB builds spreadsheet views, forms, permissions and webhooks over your existing tables. Community edition covers PostgreSQL (14 or later recommended) and MySQL (5.7 or later); SQL Server and Oracle are enterprise add-ons. Schema editing is disabled by default and the docs advise keeping it that way, so the default setup writes data without altering your tables. On NocoDB Cloud, external connections are not available on the Plus plan and require Business.

## Similar Tools

- [Ever Gauzy](/tools/ever-gauzy/): Open business management platform: ERP, CRM, HRM, ATS, and time tracking
- [Twenty](/tools/twenty/): The open-source alternative to Salesforce, designed for AI with modern CRM workflows
- [Line Harness](/tools/line-harness/): Open-source CRM for LINE Official Accounts with step delivery, scoring, and an MCP server for AI control
- [Appsmith](/tools/appsmith/): Open-source platform for building admin panels and internal dashboards on your existing databases and APIs
- [Mautic](/tools/mautic/): Open-source marketing automation platform with email, campaigns, and lead management
## Related reading

- [Where NocoDB sits against NocoBase and Budibase](/blog/nocobase-vs-nocodb-vs-budibase/)
- [The fully open-source agentic marketing stack you can run today: 19 MCP servers, one agent](/blog/open-source-agentic-martech-stack-mcp/)
- [Your Martech Budget Is Bleeding and Nobody's Measuring It](/blog/martech-budget-bleeding-nobody-measuring/)
## Also featured in

- [Best AI Marketing Automation tools (2026): 8 compared](/best/ai-marketing-automation-tools/) — Best for marketing automation teams that want the job covered in one platform and can host it themselves, with a free starting tier.
- [NocoDB vs NocoBase (2026): spreadsheet layer or system builder](/vs/nocodb-vs-nocobase/) — Pick NocoDB if your tables already exist and you want a spreadsheet-style surface over data you own.
### Quick Facts

- **Pricing:** Open-core from $12/seat/mo
- **Category:** [Marketing Automation](/categories/marketing-automation/)
- **GitHub:** ★ 65195
- **API:** Yes
- **Repository checked:** 2026-10-06
- **Page updated:** 2026-09-07

Related guides: [NocoDB vs Nocobase](/vs/nocodb-vs-nocobase/) · [Ai Marketing Automation Tools](/best/ai-marketing-automation-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Marketing Automation Tools →](/categories/marketing-automation/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
