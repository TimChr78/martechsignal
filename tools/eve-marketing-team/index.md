# Eve Marketing Team Template | MartechSignal review

Open-source team of marketing agents on eve: lead, content, social, SEO, email

- Page: https://martechsignal.com/tools/eve-marketing-team/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-08-31

Eve Marketing Team Template is Vercel's starter for running a five-person marketing team as software. You bring the lead a job, a launch to plan, posts to write, or a page that isn't converting, and the lead briefs the right specialist. The product marketer owns positioning and the shared brand context file. The content marketer writes long-form and drops a Notion page link. The social coordinator drafts X, LinkedIn, and Bluesky posts into a Typefully queue. The SEO agent audits pages and internal linking. The email specialist builds campaigns in Resend. Anything irreversible, sending a campaign or scheduling posts, pauses for an approve or deny button in Slack or the terminal.

The template is a thin layer of prompt and routing files on top of eve, Vercel's open-source agent framework. Agents are defined as directories of instructions, so you can edit what each specialist knows without touching code. All five read one brand context document at the start of a task, which is what keeps a launch thread, a blog draft, and an email campaign saying the same thing. One-click deploy wires up the Slack, Notion, and Resend connectors and Vercel Blob for state.

Cost is the honest catch. The template itself is free and MIT licensed, but it is a template, not a product. You supply the LLM API keys, the Notion workspace, the Resend account with a verified sending domain, and a Typefully key. Small teams can run a pilot on a few dollars of model spend. A serious content operation pays normal SaaS rates for those connectors on top.

The closest existing directory entry is Zapier's GTM Cheat Codes, which is a skill library for coding agents. Eve Marketing Team is the opposite shape: a deployable multi-agent service with real delivery endpoints, closer to a miniature agency than a prompt pack. It fits teams that already use eve or Vercel and want an agentic content pipeline with guardrails. If you just need better SEO in Claude Code, the simpler skill packs in this directory cover that with less moving infrastructure.
