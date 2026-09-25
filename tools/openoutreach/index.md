# OpenOutreach | MartechSignal review

Open-source AI lead finder: describe your product and it finds and qualifies the leads

- Page: https://martechsignal.com/tools/openoutreach/
- Category: Email Marketing
- Pricing: Open Source
- Open source: yes (GPL-3.0)
- Last verified: 2026-09-07

OpenOutreach is an open-source AI agent for B2B lead generation, and it inverts the usual cold-email workflow: you do not bring a list. You describe your product and your target market, and the agent finds the people who fit, writes a reason for each one, and emails them from your own mailbox. It is a self-hosted Python CLI installed with two commands, uv tool install openoutreach and then openoutreach, organized as three packages on one Django registry and database: OpenOutFind for discovery, qualification, and CRM, OpenOutSend for the outreach agent, mailbox, and send guards, and OpenOutreach as the wizard that ties them together. Lead discovery runs on BetterContact's Lead Finder, a licensed data provider, with a confidence gate that rations the paid email lookups, which cost one credit per verified work email; a free account comes with 40 credits and no card required. The AI work is split into named steps: an LLM turns your product description into search keywords, another pass qualifies candidates against your ICP and writes the plain-language reason (there is deliberately no score column), and the agent writes each opener while send guards handle the sending window, daily cap, and pacing. A Gaussian Process over profile embeddings that learns from your verdicts is documented as an active experiment that has not been shown to beat random ordering. LLM access is verified at the prompt and accepts OpenAI, Anthropic, or any OpenAI-compatible endpoint; any SMTP or IMAP mailbox with an app password works, and Google Workspace works out of the box. A Claude Code plugin is included, and the same logic ships as a skill for Codex or Cursor. CSV export is shaped for Instantly and Smartlead importers with no column mapping. GPLv3, around 2,900 GitHub stars, funded by affiliate links rather than subscriptions.
