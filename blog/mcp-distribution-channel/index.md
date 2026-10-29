# 31% of martech tools now ship an MCP server

AI Agents · Marketing Automation · 6 min read

## 31% of the tools in our directory now ship an MCP server

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · 31% of the tools in our directory now ship an MCP server

28 Oct 2026

Filed under [Marketing Automation](/categories/marketing-automation/) · [Agent Skills](/categories/agent-skills/)

Three marketing technology announcements in the past seven days, and not one of them pitched an API.

Last Thursday, [Qlik put its MCP server into Anthropic's Claude Directory](https://martechseries.com/analytics/qlik-brings-governed-business-context-and-analytics-workflows-to-claude). On Friday, Limelit, a generative engine optimization platform, [announced](https://martechseries.com/content/ai-visibility-tool-with-an-mcp-server-and-autonomous-content-agents-limelit-gives-ai-agents-211-tools-to-automate-geo-workflows-free-to-start) that every account now ships an MCP server exposing 211 tools. On Monday, TapClicks [publicly released](https://martechseries.com/predictive-ai/ai-platforms-machine-learning/tapclicks-delivers-governed-ai-data-access-with-the-public-release-of-tapclicks-mcp) its MCP server for agencies and media companies. Three vendors from three different corners of the stack, and the pitch is identical: here is a server your agent can call, and the access is governed.

A week like that is not a coincidence. It is a channel opening.

Because we maintain a structured catalog of marketing tools, we can do something most commentary cannot: count the shift instead of gesturing at it. So we ran the numbers on our own shelf.

## How we counted

We searched every active record in the catalog for "MCP" or "Model Context Protocol" in the places a buyer actually reads: tagline, description, AI features, integrations, and the deep dive notes. The count came out at 53 of 171 active tools, or 31%. Eighteen of those list MCP explicitly as an integration, the same way they list Salesforce or Slack.

The age split is the real finding. Of the 48 tools added to the directory since September 1, 22 mention MCP. That is 46%. Of the 123 older tools, 31 mention it, or 25%. Nearly half of everything that has crossed our desk in the past two months ships an MCP server or documents one, against a quarter of the tools that were already established when we started counting.

Two months is all it took for MCP to go from line item to default expectation.

## A feature does not ship on the free tier

The tell is where vendors put the server. [Zapier](/tools/zapier/) lists Zapier MCP on every plan with basic access. [Amplitude](/tools/amplitude/) states its MCP server works on every plan including Free. [Activepieces](/tools/activepieces/) ships MCP and API access on its free tier. [Make](/tools/make/) ships a Make MCP Server for connecting external agents. [Pipedream](/tools/pipedream/) goes furthest in a different direction: you can turn any workflow into an MCP endpoint that a coding agent calls directly, which makes the whole automation library agent-addressable.

You do not give away a feature on the free plan. You give away distribution. The person clicking through your UI is no longer the only user. The assistant is a user too, and it lives in Claude, ChatGPT, Cursor, and whatever your team standardizes on next year. An MCP server is how a tool gets a listing in that world. Qlik putting its server in the Claude Directory is the most literal version of this: it is app store placement, for agents.

Limelit is the sharpest example of the land grab. Its server ships on every account, exposes 211 tools according to its own documentation, and reading data through it costs nothing. When a new vendor gives agents 211 tools for free, it is not monetizing a feature. It is buying a habit.


| Vendor | What shipped | The part that matters |
| --- | --- | --- |
| Qlik | MCP server listed in Anthropic's Claude Directory | Directory placement where agents already browse |
| Limelit | MCP server on every account, 211 tools, reads free | A new tool leading with agent access, not a UI |
| TapClicks | Public release of TapClicks MCP | Per-person permissions, checked and logged on every request |

## The demo question changed

For a decade, the integration question in every martech evaluation was some version of "does it have an API." That question is close to dead. Everyone has an API and most of them are fine. The question now is what your MCP server exposes, and what stops an agent from doing something stupid with it.

The answers vary more than the press releases admit. TapClicks built its server around agency reality: each person connects with their own login, and the connection inherits exactly what that person is allowed to see, verified and logged on every request. [NocoDB](/tools/nocodb/)'s server connects Claude, ChatGPT, Cursor, and Windsurf, and its documentation states the limit plainly: record-level operations only, no table, field, or metadata changes. [Customer.io](/tools/customer-io/) publishes setup guides for four clients, a CLI, and an agent skill. Three vendors, three different answers, and only one of them is a permission model.

So ask for the tool list, not the logo. A server exposing two read-only endpoints and a server exposing 211 tools are different products wearing the same marketing. The analytics side shows the same spread: [PostHog](/tools/posthog/)'s assistant answers questions across web, Slack, desktop, and MCP, [Ahrefs](/tools/ahrefs/) lists an Ahrefs SEO MCP among its integrations, and [Superlines](/tools/superlines/) exposes its tracking across 10+ engines through a UI, an API, and an MCP server. How much of that surface an agent can actually write to is the part worth auditing.

## Lock-in moves to context

The old lock-in question was "can I get my data out," and the industry spent twenty years making the answer boring. Export buttons, CSVs, APIs, migration tools. Everyone has them. Data leaves in an afternoon.

Context does not. When Qlik describes what its server brings into Claude, the words are governed data, analytical logic, lineage, business metrics, trusted context instead of raw data alone. That is the stickiness talking. Your metric definitions, your permission scopes, the workflows your agents have been drilled on, the tool names your prompts reference: none of that exports. The renewal question stops being about data portability and becomes "how much of our agents' working knowledge lives inside your server." Vendors understand this. It is a large part of why they are racing.

## We will keep counting

The 31% figure will look small within a year, and the 46% cohort number says where the floor is heading. We plan to re-run this count monthly and publish the movement, because a census beats any single announcement. Next month's number tells us whether the older tools are retrofitting servers or whether the market splits into agent-addressable and human-only.

Every tool named here has a record in the [directory](/tools/), with MCP noted where it ships and what it exposes. If you are shortlisting tools this quarter, weigh agent access the way you once weighed API limits.

**Available is not the same as safe.** A third of the catalog mentions MCP support, and the cohort trend says that share climbs fast from here. But servers differ enormously in what they expose and how they gate it. Audit the tool list and the permission model before you point an agent at any of them.

## Related reading

- [The CDP is being rebuilt as an agent's context layer, and no vendor will call it that](/blog/cdp-agents-context-layer/)
- [Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough](/blog/salesforce-claude-commerce-cloud-agentforce/)
- [Your Agents Are Only as Smart as Your Identity Debt](/blog/agents-identity-debt/)
## Related tools

- [SeaLeap Amazon Skills](/tools/sealeap-amazon-skills/) - 602 free Amazon seller skills for Claude Code: research, listings, ads, inventory
- [Cordys CRM](/tools/cordys-crm/) - Open-source AI CRM with built-in agents, conversational analytics, and private deployment
- [Google Ads + Meta Ads + GA4 MCP](/tools/google-meta-ads-ga4-mcp/) - MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4
## Comparison guides

- [Best Agent Skills tools (2026): 8 compared](/best/agent-skills-tools/)
- [Matomo vs Plausible (2026): analytics depth or simplicity](/vs/matomo-vs-plausible/)
## Glossary terms

- [MCP](/glossary/mcp/)
- [AI Agent](/glossary/ai-agent/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.
