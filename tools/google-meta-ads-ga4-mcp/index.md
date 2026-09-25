# Google Ads + Meta Ads + GA4 MCP | MartechSignal review

MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4

- Page: https://martechsignal.com/tools/google-meta-ads-ga4-mcp/
- Category: Agent Skills
- Pricing: Freemium
- Open source: yes (MIT)
- Last verified: 2026-09-07

google-meta-ads-ga4-mcp is an MCP server that lets AI assistants manage Google Ads, Meta Ads, and GA4 from one conversation. Instead of jumping between three dashboards, you ask Claude or ChatGPT to pull campaign performance, pause ad sets, build audiences, or reconcile ad spend against GA4 conversions. It exposes 250+ tools: roughly 150 for Google Ads (campaign CRUD across Search, Display, Shopping, PMax, and Video, Keyword Planner data, bidding and budget controls, experiments, conversion tracking), 80+ for Meta Ads (campaigns, ad sets, creatives, lookalikes, lead forms, product catalogs), and 20+ for GA4 (standard and realtime reports, audiences, attribution settings, key events).

Day to day, the value is in cross-platform work that usually means exporting CSVs. You can compare Google versus Meta spend side by side, correlate ad cost with GA4 conversion events, and ask for a unified ROAS read across both networks. The repo ships with 60+ example prompts and an n8n workflow template. Write access is a deliberate choice: the official Google MCP server is read-only, while this one can create, pause, and delete campaigns. That power means you should gate it carefully. Give it a test account first, and keep a human approving anything that touches budgets.

Setup is remote rather than local. You add an endpoint URL to claude_desktop_config.json, Cursor, Windsurf, ChatGPT connectors, or n8n's MCP node. There's no local code to run and no API keys to manage in config files, but the endpoint comes from Ryze AI (Meow AI, LLC), the company behind the repo. The code is MIT licensed and free, but the hosted server is tied to Ryze's trial and paid plans, so treat this as freemium infrastructure rather than a standalone open-source deployment. The repo launched in April 2026 and picked up over 1,000 stars quickly; most of that momentum is marketing from Ryze's blog, which is worth keeping in mind.

Versus the official Google Ads MCP server, this one trades vendor independence for reach and write access. Versus the Claude Ads skill pack already in this directory, the roles differ: Claude Ads is the analyst that audits and plans, while this MCP server is the plumbing that lets any MCP-compatible agent reach live accounts. If you run an agent stack around n8n or Claude Code and manage spend on both Google and Meta, it's the fastest way to give your agents hands on the ad accounts. Just remember that hands can also delete things.
