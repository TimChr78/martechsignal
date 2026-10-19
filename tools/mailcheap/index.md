# MailCheap review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- MailCheap
## MailCheap review (2026): pricing, AI features, verdict

Newsletter platform billed per email sent, with full MCP control for AI agents

Email Marketing · From $19/mo · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit MailCheap →](https://mailcheap.ai)

[How we review](/methodology/) · No affiliate links

**Verdict:** MailCheap is a tool in Email Marketing with paid plans starting at $19/mo. The catalog documents 6 AI features, 12 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-10-19. This is a desk review, not a hands-on test. Desk-reviewed

[Visit MailCheap →](https://mailcheap.ai)

## Catalog facts: MailCheap

Not yet scored against the rubric, so no verdict here. This is everything the catalog holds on the tool, verified against vendor sources.

- **Founded:** 2026
- **Headquarters:** Singapore
- **Public API:** yes
- **Catalogued integrations:** 12
- **GitHub stars:** 1,237

The full rubric is on the [methodology page](/methodology/).

## Overview

MailCheap is a newsletter platform from Marc Lou, the indie maker behind ShipFast, launched in October 2026. The pitch is simple: pay for emails you actually send, not for subscribers who stopped reading. Cloud plans start at $19 a month for 20,000 emails, which Lou claims is 83% cheaper than beehiiv at the 4,000-subscriber level. The whole app is also open source (AGPL-3.0) and self-hostable: a Next.js app on MongoDB that sends through Amazon SES at roughly $0.10 to $0.16 per 1,000 emails. Lou runs his own 50,000-subscriber newsletter on it, which is the best proof of scale you will get from a product this young. The AI angle is not a writing assistant baked into the editor. Nothing generates copy inside the app. Instead, MailCheap ships an MCP server and a REST API that mirror everything the dashboard does: create_campaign, schedule_campaign, send_campaign, get_campaign_report, import_contacts. ChatGPT, Claude and Grok connect via OAuth; Claude Code, Cursor and Codex use an API key. Sending is marked as an irreversible action, so agents have to ask before a campaign goes out. A parity test in the repo fails the build if any dashboard action is missing from the API or MCP layer, which is a nicer guarantee than most vendors offer. The rest of the intelligence is mechanical list hygiene: dormant readers get one "still want this?" email and then stop receiving issues, and imports drop typos (gmial.com), spam traps, role addresses and duplicates. Agents do the writing; MailCheap executes. Pricing is refreshingly flat. Every plan has every feature, and tiers only change monthly email volume: $19 for 20K, $39 for 75K, $79 for 200K, $149 for 500K, $349 for 2M, roughly $0.95 per thousand. There is no free tier and no trial on the cloud. Go over your limit and new sends pause until you upgrade or the month resets, though signup confirmations keep flowing. Self-hosting is free but budget about an hour for MongoDB Atlas, SES production access, Upstash QStash and Vercel, plus SES costs. Support for self-hosters is explicitly none: GitHub issues are turned off. The closest alternative in this directory is listmonk, the veteran self-hosted newsletter manager with its single Go binary and ~24,000 stars. listmonk is the safer operational choice: older, bigger community, simpler stack. MailCheap answers with a hosted cloud option, per-email pricing, and the deepest agent support in the category. BillionMail and Notifuse also bolt LLM features onto self-hosted email stacks, but neither gives ChatGPT or Claude full campaign control the way MailCheap's MCP server does. Who should skip it: anyone who needs marketing automation. There are welcome emails and scheduled campaigns, but no drip sequences, no behavioral triggers, and no A/B testing in the feature list. It is a newsletter tool, not a Klaviyo or Customer.io replacement. The single-maintainer risk is real too; the repo is weeks old with a few dozen commits, and the AGPL will not suit everyone. If you want an agent-run newsletter on a budget and can live with those gaps, it is the most direct product for that job right now.

## AI Capabilities

- MCP server exposing full dashboard parity (create, schedule, send, report, import)
- OAuth connections for ChatGPT, Claude and Grok; API-key setup for Claude Code, Cursor, Codex
- Irreversible-send gating so agents confirm before dispatching campaigns
- Automated list cleanup that pauses dormant readers after a re-permission email
- Import filtering for typos, spam traps, role and disposable addresses
- Warm-up sending and bounce/complaint thresholds that pause or block sends automatically
## Key Integrations

- Amazon SES
- PostShiba
- Upstash QStash
- MongoDB
- Stripe
- Google Postmaster Tools
- Resend
- ChatGPT (MCP)
- Claude (MCP)
- Cursor (MCP)
- Codex (MCP)
- beehiiv/Substack/Mailchimp CSV import
## Pricing

MailCheap is sold on paid plans, from $19/mo as of 2026-10.

Cloud from $19/mo for 20K emails (flat feature set across tiers, ~$0.95 per 1,000). Self-host free under AGPL-3.0 plus Amazon SES costs (~$0.10-0.16 per 1,000). No free tier or trial on cloud.

Current plans and limits live on the [MailCheap pricing page](https://mailcheap.ai/pricing).

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ Open-source licensing with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: MCP server exposing full dashboard parity (create, schedule, send, report, import) |  |
| ✓ Active public repository (1,237 GitHub stars counted at last check) |  |
| ✓ Native integrations include Amazon SES, PostShiba, Upstash QStash (12 listed) |  |

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is MailCheap?**
MailCheap: Newsletter platform billed per email sent, with full MCP control for AI agents. MailCheap ships with MCP server exposing full dashboard parity (create, schedule, send, report, import). The public repository carries 1,237 stars.

**How much does MailCheap cost?**
MailCheap is open source - Free to self-host; the public repository carries 1,237 stars; native integrations cover Amazon SES, PostShiba, Upstash QStash. You pay in server time and maintenance, not licences.

**Is MailCheap worth paying for in 2026?**
Strengths include 1,237 GitHub stars, open-source licensing with free self-hosting, an API for custom integrations. MailCheap documents 12 integrations

## Similar Tools

- [Customer.io](/tools/customer-io/): Data-driven messaging platform for automated email, push, SMS, and in-app messages
- [Resend](/tools/resend/): Developer-first email API built around React Email, batch sending, and agent tooling
- [Listmonk](/tools/listmonk/): Open-source self-hosted newsletter and mailing list manager with a fast Go backend
- [Google Ads + Meta Ads + GA4 MCP](/tools/google-meta-ads-ga4-mcp/): MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4
- [Postmark](/tools/postmark/): Transactional email API with separated message streams, an MCP server, and published delivery numbers
## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Agencies don't want to own your AI tools or your data: the retainer model just broke](/blog/agency-retainer-agentic-tools/)
- [Two ways to buy the same workflow debt: task-metered and operations-metered](/blog/zapier-vs-make-two-ways-to-buy-the-same-workflow-debt/)
### Quick Facts

- **Pricing:** From $19/mo
- **Category:** [Email Marketing](/categories/email-marketing/)
- **GitHub:** ★ 1237
- **Founded:** 2026
- **HQ:** Singapore
- **API:** Yes
- **Last verified:** 2026-10-19

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Email Marketing Tools →](/categories/email-marketing/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
