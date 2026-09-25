# Cordys CRM | MartechSignal review

Open-source AI CRM with built-in agents, conversational analytics, and private deployment

- Page: https://martechsignal.com/tools/cordys-crm/
- Category: CRM
- Pricing: Freemium
- Open source: yes (GPL-3.0)
- Last verified: 2026-09-07

Cordys CRM is an open-source, AI-native CRM from FIT2CLOUD, the Chinese software company behind 1Panel, JumpServer, and MaxKB. It covers the full lead-to-cash cycle: lead capture and routing, customer and contact management, opportunities, contracts, orders, and payment collection. The pitch is a self-hosted Salesforce alternative for mid-size and large teams that want their sales data on their own servers. It's Java (Spring Boot) on the backend with a Vue frontend, ships as a Docker install, and hit 100,000 downloads within 25 days of its August 2025 public beta.

The AI part is real, not a bolted-on chatbot. The AI is assembled from outside rather than built in. MaxKB, FIT2CLOUD's agent platform, connects over the API to run sales agents for lead triage and follow-up drafting. DataEase handles embedded BI dashboards, and that integration requires a DataEase commercial edition. Conversational SQL analytics is not part of the product: SQLBot appears only in FIT2CLOUD's sibling product navigation, with no Cordys documentation behind it. CORDYS AI, added in v1.9.0, is the server-side agent, it is enterprise only, and it reuses the CRM's RBAC so reads run directly, writes are permission checked, and deletes need manual confirmation. There's also an MCP server, so outside agents (Claude, Cursor, and similar) can read and act on CRM data directly. Since v1.8.1 the free community edition exposes the API and MCP access too, capped at 1,000 API calls a day, which is unusual. The catch is that you're really running three systems in a trench coat, and the setup and upkeep reflect that.

Pricing skips per-seat fees entirely. The community edition is free and self-hosted under a GPLv3-based license (the FIT2CLOUD Open Source License) that bars you from swapping out the logo or copyright notices. The enterprise edition is an annual subscription in standard, professional, and flagship tiers, published at ¥30,000, ¥60,000, and ¥120,000 a year by company revenue, with flagship adding hot-standby and distributed high availability. The no-per-seat model can work out far cheaper than Salesforce or HubSpot for a 100-person sales team, but you're trading license cost for hosting and ops effort.

Against Twenty, the other big open-source CRM in this directory, Cordys goes deeper on native AI (Twenty's AI is lighter and its community is more global) but feels less polished and skews heavily toward the Chinese market. EspoCRM is easier to stand up and lighter to run, but has no comparable AI layer. If you want Salesforce-style depth with AI agents baked in and no per-seat bill, and you're comfortable self-hosting, Cordys is worth a serious look.

Who should skip it: anyone who needs a SaaS product that just works without a server, teams outside China who want English-first docs and community support (the docs and forums are Chinese-first), and small teams that don't have Java ops capacity. The stack is heavier than a typical PHP CRM, and the enterprise motion is built around Chinese enterprises. For a China-based sales team that wants private deployment and real AI features without per-seat fees, though, it's one of the few open-source options that delivers both.
