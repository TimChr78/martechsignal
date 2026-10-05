# ToolJet review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Workflow Automation](/categories/workflow-automation/)
- ToolJet
Re-check pending: pricing last verified 2026-09-07 (28 days ago).

## ToolJet review (2026): pricing, AI features, verdict

Open-source low-code platform for internal tools: prompt or build admin panels, dashboards and operational apps

Workflow Automation · Open-core from $79/mo · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit ToolJet →](https://tooljet.com)

[How we review](/methodology/) · No affiliate links

[Visit ToolJet →](https://tooljet.com)

## MartechSignal Score: 42/60

ToolJet generates internal apps from a prompt over 41,040 stars of AGPL code, with an MCP server for the agent harnesses. Pricing is published down to builder seats and the Enterprise floor.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Self-host CE free (AGPL-3.0), Cloud Free (2 builders), Pro $79/builder/mo annual, Team $199, Enterprise from $3,000/mo published (the vendor pricing page: [pricing page](https://tooljet.com/pricing), verified 2026-09-28). |
| Feature depth | 7/10 | Prompt-built apps, dashboards and operational tools over your databases cover internal tooling (vendor documentation: [vendor site](https://tooljet.com), verified 2026-09-28). |
| Integrations | 7/10 | Twelve named datasources from PostgreSQL and Snowflake to Stripe, Slack and three API protocols (vendor documentation: [vendor site](https://tooljet.com), verified 2026-09-28). |
| AI capability | 6/10 | Prompt-to-app generation, query generation and a beta MCP server for three agent harnesses (vendor documentation: [vendor site](https://tooljet.com), verified 2026-09-28). |
| Openness | 8/10 | AGPL-3.0 with community-edition self-hosting (the source repository: [repository](https://github.com/ToolJet/ToolJet), verified 2026-09-28). |
| Operational maturity | 6/10 | With priced cloud tiers and an Enterprise floor published (vendor documentation: [vendor site](https://tooljet.com), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

ToolJet is an open-source platform for building internal tools: admin panels, dashboards and operational apps that run against your databases, APIs and SaaS systems, built with a visual builder, a prompt-driven AI builder, or an MCP server that lets coding agents such as Claude Code and Cursor build and edit apps directly. The repo is AGPL-3.0 and now describes itself as the open-source foundation of ToolJet AI: AI app generation, AI query building, the agent builder, workflows, modules, git sync and audit logs belong to the paid editions, metered in AI credits on cloud and licensed on self-host. At 41,040 GitHub stars with roughly 400 contributors, and with several releases a week on an LTS track (v3.20.x) plus a beta track, it sits alongside Appsmith at the top of this class. For marketing operations the builds are the same set as its peers: campaign dashboards over ad-platform APIs, lead-quality consoles beside the CRM, and approval panels, self-hosted so lead and consent data stays in-house. Around 50 data sources are documented, including PostgreSQL, MySQL, MongoDB, Snowflake, BigQuery, Elasticsearch, S3, Stripe, Slack, SendGrid, Airtable and NocoDB, plus generic REST, GraphQL and gRPC. Self-hosting has real requirements: x86 64-bit only (no arm64 images), PostgreSQL 16 recommended, Redis 7, and two separate Postgres databases, with MySQL explicitly unsupported; a single docker run command still gets you a working instance. Two honesty notes from the docs: self-hosted AI calls ToolJet's hosted api-gateway and python-server endpoints, so it is not air-gapped without ToolJet AI Enterprise, and the published images are tagged ee even though the repo license is AGPL, so the community and enterprise boundary is not spelled out in a license file. Cloud pricing runs from free (2 builders, 2 apps) to $79 per builder monthly billed annually, with Team at $199 and Enterprise from $3,000 per month. This assessment is based on the documented architecture and public materials.

ToolJet homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- ToolJet AI generates apps from a prompt
- AI query generation and JS/Python code assistant
- MCP server (beta) for Claude Code, Codex and Cursor builds
## Key Integrations

- PostgreSQL
- MySQL
- MongoDB
- Snowflake
- BigQuery
- Elasticsearch
- S3
- Stripe
- Slack
- SendGrid
- Airtable
- REST / GraphQL / gRPC
## Pricing

ToolJet is open core: the self-hosted version is free, paid plans start at $79/mo as of 2026-09.

Self-host CE free (AGPL-3.0). Cloud Free (2 builders, 2 apps), Pro $79/builder/mo billed annually, Team $199, Enterprise from $3,000/mo. Self-host Team $199/builder/mo. AI credits $1 per 100.

Current plans and limits live on the [ToolJet pricing page](https://tooljet.com/pricing).

## How to install

- README one-liner: docker run --name tooljet --restart unless-stopped -p 80:80 --platform linux/amd64 -v tooljet_data:/var/lib/postgresql/13/main tooljet/try:ee-lts-latest. The docs version of the same command mounts /var/lib/postgresql/16/main instead, reflecting the Postgres 16 migration; for a non-standard port add -p 8080:8080 -e PORT=8080. The README recommends the LTS tag over latest when upgrading.
- Docker Compose: curl -LO https://tooljet-deployments.s3.us-west-1.amazonaws.com/docker/docker-compose-db.yaml && mv docker-compose-db.yaml docker-compose.yaml && mkdir postgres_data, then fetch .env.internal.example and internal.sh from the same bucket, run ./internal.sh to seed secrets, and docker-compose up -d. An external-Postgres variant swaps in docker-compose.yaml, .env.external.example and external.sh; a backup-restore.sh script is published alongside.
- Helm: helm repo add tooljet https://github.com/ToolJet/helm-charts.git && helm install tooljet tooljet/tooljet. The chart ships PostgreSQL enabled and Redis present but disabled, which must be enabled when replicas exceed one.
- Raw Kubernetes: kubectl apply -f https://tooljet-deployments.s3.us-west-1.amazonaws.com/kubernetes/deployment.yaml, then kubectl get pods. PostgREST variables (PGRST_HOST, PGRST_DB_URI, PGRST_JWT_SECRET and others) are mandatory in this path.
- System requirements per the docs: Ubuntu 22.04 or later, x86 64-bit only (arm64 is not supported), 4 GB RAM and 1 vCPU for the app VM, PostgreSQL 16.x recommended, Redis 7.x, and two distinct Postgres databases for TOOLJET_DB and PG_DB.
- For AI features and workflows: whitelist https://api-gateway.tooljet.ai and https://python-server.tooljet.ai, set WORKER=true for scheduled workflows, and provide external Redis for multi-worker deployments.
## Best for

Teams that want to generate internal dashboards by prompt, or hand the build to Claude Code over MCP, self-hosted, with a wide connector library and a developer nearby to review the queries and permissions the AI produced.

## Not for

ARM or Apple-silicon-only infrastructure (no arm64 images), shops standardized on MySQL as the backing store, teams that need air-gapped AI without an enterprise agreement, and anyone who wants the simplest possible two-container install.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

ToolJet gives you three ways into the same app model. The visual builder is the classic loop: drop components, write queries in SQL, JavaScript or Python, bind results. The ToolJet Database is a no-code table editor sitting on PostgreSQL when there is no source system yet. And the AI builder takes a prompt on the home page and produces a working app with UI, queries and data bindings, no confirmation step. Docs also document AI query generation and an AI code generator for JavaScript and Python snippets, and note that only query names leave your instance for that feature.

The MCP server is the distinctive piece and the reason agent-first teams shortlist ToolJet. It is marked beta, and it exposes your instance to a coding agent: the agent can generate and modify apps in place, inspect datasources, create and seed ToolJet DB tables, write queries against ToolJet DB, Postgres, REST or any plugin, and manage page and query permissions and users. ToolJet ships a packaged plugin for Claude Code (tooljet-app-builder) and Codex, and any other MCP client can register the server from the ToolJet/tooljet-mcp repo. You need a personal access token (tj_pat_) and Node 20 or newer.

Editions and metering need reading before you budget. Cloud plans meter AI work in credits, and monthly credits do not carry forward; add-on credits cost $1 per 100. Enterprise adds bring-your-own-key AI at no credit cost and ToolJet AI Enterprise, which runs the AI server on your own infrastructure for a fully air-gapped deployment. Without that tier, self-hosted AI features call ToolJet's hosted api-gateway.tooljet.ai and python-server.tooljet.ai endpoints, which the setup docs tell you to whitelist. Related honesty note: the published Docker images are tagged ee even though the repo LICENSE is AGPL-3.0, and no separate license file spells out where community code ends.

Self-hosting requirements are stricter than peers and worth planning around: x86 64-bit only, with arm64 explicitly unsupported; PostgreSQL 16.x recommended, with 13.x at end of life since November 2025 and upgrade guides published; Redis 7.x required; and two separate Postgres databases (TOOLJET_DB and PG_DB must differ, and the docs warn that sharing one causes deployment failure). MySQL is explicitly not on the roadmap. Workflows need WORKER=true and an external Redis once you run more than one replica, and the workflow engine itself moved from Temporal to BullMQ, with a migration guide.

This assessment is based on the repository, docs.tooljet.com and release notes. Calibration: development is genuinely active, with multiple releases per week and two on September 7, 2026, split across an LTS track (v3.20.x) and a beta track (v3.21.x); and ToolJet's own marketing numbers lag its repo, with the pricing page citing 41,040 GitHub stars and the homepage 40,777 against an API count of 40,857. The 3.0 upgrade has documented breaking changes around dynamic component references and variable access, so test before upgrading.

## Verdict

The most AI-forward option in the open-source internal-tools class, with the sharpest self-hosting requirements to match. Strong if an agent-driven build path appeals; read the ee-tagged image boundary against the AGPL license before you standardize on it.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ AGPL-3.0 licence with free self-hosting | ✗ Paid plans start at $79/mo once past the free tier |
| ✓ AI capabilities: toolJet AI generates apps from a prompt |  |
| ✓ Active public repository (41,040 GitHub stars counted at last check) |  |
| ✓ Native integrations include PostgreSQL, MySQL, MongoDB (12 listed) |  |

## Related concepts

- [Workflow automation](/glossary/workflow-automation/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [MCP](/glossary/mcp/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is ToolJet?**
ToolJet: Open-source low-code platform for internal tools: prompt or build admin panels, dashboards and operational apps. ToolJet ships with toolJet AI generates apps from a prompt. The public repository carries 41,040 stars.

**How much does ToolJet cost?**
ToolJet has a free tier; paid plans start at $79/mo. Self-host CE free (AGPL-3.0). Cloud Free (2 builders, 2 apps), Pro $79/builder/mo billed annually, Team $199, Enterprise from $3,000/mo. Self-host Team $199/builder/mo. AI credits $1 per 100. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is ToolJet a good self-hosted Workflow Automation tool in 2026?**
The most AI-forward option in the open-source internal-tools class, with the sharpest self-hosting requirements to match. Strong if an agent-driven build path appeals; read the ee-tagged image boundary against the AGPL license before you standardize on it.

**Is ToolJet free to self-host?**
The community edition is AGPL-3.0 and free to self-host, with no app or user ceiling written into the license. What costs money is the ToolJet AI layer and enterprise features: AI app generation and AI query building are metered in credits on cloud plans, and SSO, audit logs, modules, git sync, multi-environment and bring-your-own-key or air-gapped AI are licensed, with self-hosted paid plans starting at $199 per builder monthly. Two caveats the docs make explicit: self-hosted AI calls ToolJet's hosted gateway endpoints unless you buy ToolJet AI Enterprise, and the published Docker images are tagged ee even though the repo license is AGPL.

**ToolJet vs Retool: how do they compare?**
Retool is the commercial incumbent: hosted, closed source, priced per user at a premium. ToolJet is AGPL-3.0 with a free self-hosted edition, and its own comparison page pitches AI-first app generation, full app generation from a prompt and multi-LLM support as the differences, alongside SOC 2 Type II, GDPR and ISO 27001 claims for its cloud. Choose Retool for a managed platform with mature connectors and support; choose ToolJet when self-hosting, source access or the MCP build path matter more than managed convenience, and budget for stricter requirements (x86 only, PostgreSQL 16, Redis, two separate databases).

**Can Claude Code or Cursor build ToolJet apps?**
Yes, through the ToolJet MCP server, which the README marks as beta. You create a ToolJet personal access token and run Node 20 or newer, then in Claude Code install the packaged plugin with /plugin marketplace add ToolJet/tooljet-mcp followed by /plugin install tooljet-app-builder@tooljet. Codex has equivalent commands, and Cursor or Cline connect by registering the stdio server from the ToolJet/tooljet-mcp repository. Once connected, the agent can generate and modify apps, inspect datasources, create and seed ToolJet DB tables, write queries and manage permissions, drawing on its own model subscription rather than your ToolJet AI credits.

## Similar Tools

- [Budibase](/tools/budibase/): Open-source operations platform for building AI agents, apps and automations on your own data
- [Appsmith](/tools/appsmith/): Open-source platform for building admin panels and internal dashboards on your existing databases and APIs
- [GrowthBook](/tools/growthbook/): Open-source feature flags and A/B testing with a visual editor and attribute-based targeting
- [n8n](/tools/n8n/): Open-source workflow automation platform with AI agent capabilities and 400+ nodes
## Related reading

- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
- [OpenAI Isn't Building Ads. It's Building Agents That Spend Money Without You.](/blog/openai-agent-ads-spending-without-you/)
- [Why Your Marketing Stack Doesn't Need Another AI Tool](/blog/why-your-marketing-automation-stack-doesnt-need-another-ai-tool/)
### Quick Facts

- **Pricing:** Open-core from $79/mo
- **Category:** [Workflow Automation](/categories/workflow-automation/)
- **GitHub:** ★ 41040
- **API:** Yes
- **Repository checked:** 2026-10-05
- **Page updated:** 2026-09-07

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Workflow Automation Tools →](/categories/workflow-automation/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
