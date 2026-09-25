# Line Harness | MartechSignal review

Open-source CRM for LINE Official Accounts with step delivery, scoring, and an MCP server for AI control

- Page: https://martechsignal.com/tools/line-harness/
- Category: Marketing Automation
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-09-07

L Harness (line-harness-oss) is an open-source CRM and marketing automation suite for LINE Official Accounts, built by Japanese developer Shuichi Noda and run under AI Agent Inc. It targets companies, shops, and marketing agencies in Japan that run LINE as a customer channel and want the step-delivery and segmentation features of paid tools like L-Step (from ¥20,000/mo) and L Message without the monthly license fee. The software itself costs ¥0; you deploy it to your own Cloudflare account using Workers, D1, and Pages, and the setup CLI (npx create-line-harness) handles database creation, worker deployment, LIFF app registration, and admin user creation in about five minutes.

The feature list covers the standard LINE marketing playbook: step delivery with minute-level delay control and conditional branching, tag-based segment broadcasts with automatic queueing past 500 recipients, LIFF forms, rich menu switching per user or tag, behavior-based lead scoring, Google Calendar booking with webinar auto-scheduling, and an affiliate measurement system with click-to-conversion tracking and last-touch attribution. What separates it from the commercial incumbents is the AI layer. The repo ships an MCP server (@line-harness/mcp-server) so you can drive the entire system from Claude Code in natural language: create scenarios, monitor unanswered conversations, and send broadcasts. There is also a typed TypeScript SDK and webhook input/output for Stripe and Slack. BAN detection with automatic account switching is included for multi-account operators, a feature the paid tools do not touch.

Pricing is genuinely simple but not free in the absolute sense. The MIT-licensed software costs nothing, and Cloudflare's free tier covers most small deployments, but you still pay LINE's own per-message delivery fees and any Cloudflare usage beyond the free tier. The project's own pricing page is honest about this, and also about the fact that someone on your side owns updates and incident response. A managed version, L Harness Cloud, exists from the same developer if you want the infrastructure handled.

Against the paid incumbents, L Harness wins on cost, API access (full API where L-Step and L Message expose none), and the MCP integration. It loses on support guarantees: no SLA, no phone support, and the admin UI documentation is Japanese-first, with English, Chinese, Korean, and Spanish READMEs. The repo has 568 stars and 246 commits as of August 2026, pushed within days of this writing, so it is actively maintained but still pre-1.0 (v0.21.x).

Who should skip it: teams with no Cloudflare or LINE Developers setup capability, anyone who needs a vendor SLA, and marketers outside Japan where LINE is not a primary channel. For everyone else running LINE marketing, this is the first credible zero-license-cost alternative to the L-Step category.
