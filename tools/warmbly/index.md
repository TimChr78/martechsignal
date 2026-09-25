# Warmbly | MartechSignal review

Open-source cold email platform with warmup, campaigns, unified inbox, and CRM

- Page: https://martechsignal.com/tools/warmbly/
- Category: Email Marketing
- Pricing: Open Source
- Open source: yes (Apache-2.0)
- Last verified: 2026-09-24

Warmbly is an open-source cold email platform that sends from mailboxes you already own and warms them gradually so they stop landing in spam. It bundles warmup pools, multi-step campaigns, a shared reply inbox, analytics, and a small CRM into one self-hostable stack (Apache 2.0, built with Go, Rust, Elixir, and React). The audience is founders, agencies, and sales teams running outbound B2B, the same crowd paying Instantly or Smartlead for this workflow today.

The AI parts are narrower than the "AI-native" branding suggests. Campaign sequences can include AI agent steps that branch on classified reply intent. The unified inbox labels incoming replies as positive, out of office, unsubscribe, or bounce the moment they land, and holds agent drafts for follow-ups. A content checker scores template deliverability before you send, advisory only, it never blocks a campaign. Reply classification is the genuinely useful piece; the rest is assistive rather than autonomous.

Pricing splits cleanly in two. Self-hosting is free with no cloud dependency: a curl install script brings up Docker Compose with Postgres and Redis, and outbound mail leaves through each mailbox's own provider rather than Warmbly's servers. The hosted cloud has a free plan with 10 mailboxes, then Starter at $29/mo (150 sends/day), Grow at $89/mo (3,000 sends/day, adds CRM, A/B variants, and the API), and Business at $329/mo (15,000 sends/day, team roles, audit log). Watch the send caps: 150/day at Starter is thin next to similarly priced plans at Instantly, though annual billing shaves 20%.

Against Smartlead or Instantly, the draw is self-hosting and the Apache 2.0 license. Your mailbox credentials and lead data never leave your own infrastructure, and you scale throughput by running more workers. The trade-off is youth: 316 GitHub stars as of September 2026, one company behind it (Mindroot Ltd, London), and no lead database included. The hosted competitors have years of deliverability tooling and B2B data you would have to source separately.

If you want managed cold email at volume and do not care where the servers live, the incumbents are more mature. If you are an agency that needs client outreach on your own hardware, or a product team that wants to embed sending behind an API with signed webhooks, Warmbly earns a Docker Compose run.
