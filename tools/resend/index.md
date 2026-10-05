# Resend review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- Resend
Re-check pending: pricing last verified 2026-09-07 (28 days ago).

## Resend review (2026): pricing, AI features, verdict

Developer-first email API built around React Email, batch sending, and agent tooling

Email Marketing · Freemium from $20/mo Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Resend →](https://resend.com)

[How we review](/methodology/) · No affiliate links

[Visit Resend →](https://resend.com)

## MartechSignal Score: 38/60

Resend is developer email built around React Email, with a hosted MCP server and an official Cursor plugin. 19,808 stars on the MIT SDKs, and marketing prices published alongside transactional.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free 3,000 emails/mo (100/day, 3 domains), Transactional Pro $20/mo (50K), Scale $90 to $1,150/mo published tiers (the vendor pricing page: [pricing page](https://resend.com/pricing), verified 2026-09-28). |
| Feature depth | 6/10 | Transactional and marketing email with batch sending and contact imports cover the developer email stack (vendor documentation: [vendor site](https://resend.com), verified 2026-09-28). |
| Integrations | 6/10 | Next.js, Vercel, React Email, Zapier, an official Cursor plugin and Vercel Marketplace documented (vendor documentation: [vendor site](https://resend.com), verified 2026-09-28). |
| AI capability | 6/10 | AI Email Editor with brand-voice drafting, template assistant and column mapping plus a hosted MCP server (vendor documentation: [vendor site](https://resend.com), verified 2026-09-28). |
| Openness | 6/10 | MIT SDKs behind a closed sending service (the source repository: [repository](https://github.com/resend/react-email), verified 2026-09-28). |
| Operational maturity | 6/10 | Founded 2023 with fast developer adoption and published tier ceilings (vendor documentation: [vendor site](https://resend.com), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Resend is a developer-first email platform built by people who make developer tools: founders Zeno Rocha, Bu Kinoshita, and Jonni Lundy started the open-source React Email project in 2022, launched the sending platform in 2023 through Y Combinator's W23 batch, and raised an $18M Series A led by Andreessen Horowitz in December 2024. By June 2026 the company reported 3 million users, 6.8 million weekly npm downloads, and profitability. The product split is unusual and worth understanding before you buy: transactional and marketing email are separate subscriptions. Transactional starts free at 3,000 emails a month (100 a day), Pro is $20 a month for 50,000, and Scale publishes tiers from $90 for 100,000 to $1,150 for 2.5 million a month; marketing is priced by contacts, from $40 a month for 5,000. There are no annual discounts, and the pricing FAQ says so in one word: no. The developer surface is the draw. Official SDKs cover Node.js, Python, Go, Rust, PHP, Laravel, Ruby, Java, and .NET, plus a chat adapter, batch sending takes up to 100 messages per call, and webhooks document eight event types with retries and replays, alongside inbound receiving, broadcasts, audiences, templates, and automations. Agent tooling is first-class: a hosted MCP server at mcp.resend.com with OAuth, a CLI, and documented skills for Claude Code, Cursor, and Codex. AI is real but modest: an AI Email Editor with brand-voice drafting and pre-send checks, an assistant in the template editor, and AI column mapping on contact imports, metered through monthly AI credits. Deliverability tooling is rule-based, not AI. Sending runs on AWS across four regions, with account data held in the United States regardless of region. Resend fits product teams shipping email from code, not marketers who want a campaign studio.

Resend homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI Email Editor with brand-voice drafting
- AI assistant in the template editor
- AI column mapping on contact imports
- Hosted MCP server and agent skills
## Key Integrations

- Next.js
- Vercel
- React Email
- Zapier
- Cursor (official plugin)
- Vercel Marketplace
## Pricing

Resend is freemium, with a free tier to start, paid plans start at $20/mo as of 2026-09.

Free 3,000 emails/mo (100/day cap, 3 domains); Transactional Pro $20/mo for 50,000; Scale $90-$1,150/mo published tiers; Enterprise custom; Marketing priced by contacts from $40/mo for 5,000; no annual discounts

Current plans and limits live on the [Resend pricing page](https://resend.com/pricing).

## How to install

- npm install resend, then send with an API key: import { Resend } from 'resend'; const resend = new Resend('re_xxxxxxxxx'). Official SDKs cover Node.js, Python, Go, Rust, PHP, Laravel, Ruby, Java, and .NET.
- Or use the CLI: curl -fsSL https://resend.com/install.sh | bash (also npm install -g resend-cli and brew install resend/cli/resend; on Windows, irm https://resend.com/install.ps1 | iex).
- Verify a domain before production: add the generated DKIM and SPF records (TXT plus MX or CNAME) exactly as Resend generates them. The docs strongly recommend a subdomain such as notifications.example.com rather than your root domain.
- Pick a sending region at setup: North Virginia (us-east-1), Ireland (eu-west-1), Sao Paulo (sa-east-1), or Tokyo (ap-northeast-1). The docs state that all account data stays in the United States regardless of region.
- For agents, point an MCP client at https://mcp.resend.com/mcp (OAuth) or run claude plugin install resend@claude-plugins-official; the docs also publish a Resend skill and a React Email skill for coding agents.
## Requirements

A domain you control with DNS access for DKIM and SPF records, and an API key. The API rate limit is 10 requests per second per team with no burst allowance (429 beyond it, raiseable for trusted senders on request), batch sends take up to 100 messages per call and do not support attachments, and per-email attachments cap at 40MB after base64 encoding. Domains allowed: 3 on Free, 10 on Pro, 1,000 on Scale. Sent and inbound emails both count against quota, with a hard ceiling of 5x your monthly quota.

## Best for

Product and platform teams that send application email from code and want the workflow to live next to their IDE: React Email components, typed SDKs, batch API, webhooks with replays, and an MCP server for coding agents. The free tier and three-domain allowance make it a comfortable start for side projects and SaaS products alike.

## Not for

Marketing teams that want a campaign studio first: marketing plans exist but are priced by contacts, and broadcasts can only go to existing contacts, so segmentation and journey building are thinner than Customer.io or Klaviyo. Also not for buyers needing annual billing discounts, HIPAA compliance (listed as in progress), or dedicated IP pools below the Scale tier.

## Review notes

Assessed from resend.com, resend.com/docs, and the changelog RSS in September 2026; we have no Resend account and have not sent through it. The documentation corpus is large and current: the changelog's newest entries are Link Checker (September 3, 2026), Single Sign-On (September 1), and an Email Metrics API (August 27).

The correction that matters: the three AI features in our earlier record (AI deliverability optimization, AI spam detection, smart retry logic) appear nowhere in Resend's documentation. The documented AI surface is an AI Email Editor with brand-voice drafting and pre-send checks, an assistant in the template editor, AI column mapping on imports, and monthly AI credits; Deliverability Insights is explicitly a set of best-practice checks, not AI. Slack and Segment are not documented integrations, and Scale is not custom-priced.

Open source is the exit surface, and our record undersold it: react-email alone holds about 19,808 GitHub stars under MIT, an order of magnitude larger than any Resend SDK repo, and the organization publishes roughly 100 repositories including the MCP server, CLI, skills, and OpenAPI spec. Templates you build in React Email keep working against another sender.

The transactional and marketing split is the pricing trap. A team that starts on Pro for product email and later wants newsletters takes a second, contact-based subscription, and the docs recommend separate subdomains per stream anyway. IP pools are a $30 a month Scale add-on with an eligibility bar of 3,000 emails a day, so shared IPs are the default reality for most accounts.

## Verdict

The most developer-native platform in email, with an honest free tier, real agent tooling, and a published limit sheet; check the transactional versus marketing split before committing either budget.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ AI capabilities: AI Email Editor with brand-voice drafting | ✗ Paid plans start at $20/mo once past the free tier |
| ✓ Active public repository (19,808 GitHub stars counted at last check) | ✗ Closed source - no self-hosting option |
| ✓ Native integrations include Next.js, Vercel, React Email (6 listed) |  |
| ✓ Free tier to evaluate before committing (Free 3,000 emails/mo (100/day cap, 3 domains); Transactional Pro $20/mo for 50,000) |  |

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Resend?**
Resend: Developer-first email API built around React Email, batch sending, and agent tooling. Resend ships with AI Email Editor with brand-voice drafting. The public repository carries 19,808 stars.

**How much does Resend cost?**
Resend has a free tier; paid plans start at $20/mo. Free 3,000 emails/mo (100/day cap, 3 domains); Transactional Pro $20/mo for 50,000; Scale $90-$1,150/mo published tiers; Enterprise custom; Marketing priced by contacts from $40/mo for 5,000; no annual discounts. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Resend worth it past the free tier?**
The most developer-native platform in email, with an honest free tier, real agent tooling, and a published limit sheet; check the transactional versus marketing split before committing either budget.

**What are Resend's rate limits and batch limits?**
The API allows 10 requests per second per team with no burst allowance; exceeding it returns 429, and Resend says it can raise the limit for trusted senders on request. Batch sending accepts up to 100 emails in a single call, and each batch counts as one request against the rate limit, but attachments are not supported on the batch endpoint. Per-email attachments cap at 40MB after base64 encoding, and a hard limit of 5x your monthly quota applies to sending.

**Is Resend free, and what does the free tier include?**
The transactional free plan includes 3,000 emails a month with a 100-per-day cap, 3 verified domains, 5 AI credits, and 10,000 automation runs a month. Pro is $20 a month for 50,000 emails, Scale publishes tiers from $90 for 100,000 to $1,150 for 2.5 million, and Enterprise is custom, with a 99.99% uptime SLA. Marketing email is a separate, contact-based subscription starting at $40 a month for 5,000 contacts. There are no annual discounts; the pricing FAQ answers that question with a plain no.

**Does Resend work with AI agents and coding tools?**
Yes, and it is one of the better-documented cases in email. Resend hosts an MCP server at mcp.resend.com/mcp with OAuth, ships an official Claude plugin (claude plugin install resend@claude-plugins-official), and documents a Resend skill and a React Email skill alongside a CLI. Clients listed in the docs include Claude Code, Claude, Cursor, Codex, Copilot, Windsurf, and Warp. The changelog shows steady investment: an official MCP server in April 2026, a remote MCP server in July, and an official Cursor plugin in August.

## Similar Tools

- [React Email Editor](/tools/react-email-editor/): Drag-n-Drop Email Editor Component for React.js
- [Customer.io](/tools/customer-io/): Data-driven messaging platform for automated email, push, SMS, and in-app messages
- [Postmark](/tools/postmark/): Transactional email API with separated message streams, an MCP server, and published delivery numbers
- [Loops](/tools/loops/): Email marketing for SaaS: marketing, product, and transactional email in one tool
## Related reading

- [The fully open-source agentic marketing stack you can run today: 19 MCP servers, one agent](/blog/open-source-agentic-martech-stack-mcp/)
- [MCP Rewrites the Integration Economics of Your Marketing Stack](/blog/mcp-rewrites-the-integration-economics-of-your-marketing-stack/)
- [AI watermarks are now part of your agent's risk surface](/blog/watermark-provenance-tax-agents/)
### Quick Facts

- **Pricing:** Freemium from $20/mo
- **Category:** [Email Marketing](/categories/email-marketing/)
- **GitHub:** ★ 19808
- **Founded:** 2023
- **HQ:** San Francisco, CA, USA
- **API:** Yes
- **Repository checked:** 2026-10-05
- **Page updated:** 2026-09-07

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Email Marketing Tools →](/categories/email-marketing/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
