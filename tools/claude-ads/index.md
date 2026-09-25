# Claude Ads | MartechSignal review

Paid-media operations skill for Claude Code covering 12 ad platforms

- Page: https://martechsignal.com/tools/claude-ads/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-08-28

Claude Ads is a paid-media operations skill that runs inside Claude Code. Point it at your ad account exports or connect a read-only API feed, and it audits, plans, creates, monitors, and reports across 12 platforms: Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Reddit, Snapchat, X, Apple, Amazon, and Pinterest. Each platform gets its own focused skill, audit worker, and capability declaration. The audit alone runs 250+ checks and scores your account health with dated evidence and explicit confidence levels, so you know whether a finding is a confirmed problem or a likely one.

The workflow covers the full paid-media lifecycle. /ads audit gives you an evidence-backed account review. /ads plan builds channel strategy, campaign structure, budget allocation, and measurement design. /ads create produces copy, image briefs, video scripts, and product-photo directions. /ads monitor tracks pacing, delivery, fatigue, policy compliance, and performance drift. /ads experiment designs controlled tests. Everything outputs as versioned JSON that renders to Markdown, HTML, or PDF. The critical design choice: it's read-only by default. Live account changes stay disabled until the specific platform and operation pass approval, idempotency, verification, audit, and rollback gates. You draft changes with /ads launch --draft and /ads optimize --draft, review them, then decide whether to apply.

It's free and MIT-licensed, same as Claude SEO. You need Claude Code and API tokens. The context intake system asks about your industry and spend level upfront so benchmarks are relevant to your situation rather than generic. There's a community mirror on Skool for early access, but the public repo is complete.

The closest comparison is a human PPC consultant or an agency retainer. Claude Ads doesn't replace judgment, but it replaces the 4-hour manual audit spreadsheet and the "I'll get to that creative brief next week" backlog. For agencies managing multiple ad accounts, running /ads audit on each client monthly costs API tokens instead of billable hours. For in-house teams spending $5K-50K/month on ads, it's a force multiplier that catches wasted spend and policy violations before they compound. If you only run Meta ads and want a simpler tool, Revealbot handles rule-based automation. Claude Ads is for teams that want the full operational layer.
