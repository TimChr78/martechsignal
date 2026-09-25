# Resend | MartechSignal review

Developer-first email API built around React Email, batch sending, and agent tooling

- Page: https://martechsignal.com/tools/resend/
- Category: Email Marketing
- Pricing: Freemium
- Open source: no
- Last verified: 2026-09-07

Resend is a developer-first email platform built by people who make developer tools: founders Zeno Rocha, Bu Kinoshita, and Jonni Lundy started the open-source React Email project in 2022, launched the sending platform in 2023 through Y Combinator's W23 batch, and raised an $18M Series A led by Andreessen Horowitz in December 2024. By June 2026 the company reported 3 million users, 6.8 million weekly npm downloads, and profitability. The product split is unusual and worth understanding before you buy: transactional and marketing email are separate subscriptions. Transactional starts free at 3,000 emails a month (100 a day), Pro is $20 a month for 50,000, and Scale publishes tiers from $90 for 100,000 to $1,150 for 2.5 million a month; marketing is priced by contacts, from $40 a month for 5,000. There are no annual discounts, and the pricing FAQ says so in one word: no. The developer surface is the draw. Official SDKs cover Node.js, Python, Go, Rust, PHP, Laravel, Ruby, Java, and .NET, plus a chat adapter, batch sending takes up to 100 messages per call, and webhooks document eight event types with retries and replays, alongside inbound receiving, broadcasts, audiences, templates, and automations. Agent tooling is first-class: a hosted MCP server at mcp.resend.com with OAuth, a CLI, and documented skills for Claude Code, Cursor, and Codex. AI is real but modest: an AI Email Editor with brand-voice drafting and pre-send checks, an assistant in the template editor, and AI column mapping on contact imports, metered through monthly AI credits. Deliverability tooling is rule-based, not AI. Sending runs on AWS across four regions, with account data held in the United States regardless of region. Resend fits product teams shipping email from code, not marketers who want a campaign studio.
