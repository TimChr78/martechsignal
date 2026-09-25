# AI Marketing Suite | MartechSignal review

15-skill marketing suite for Claude Code with parallel agents and PDF reports

- Page: https://martechsignal.com/tools/ai-marketing-claude/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-08-28

AI Marketing Suite is a 15-skill pack for Claude Code aimed at solopreneurs and agency builders who want to sell marketing services. You type /market audit https://example.com and five parallel agents analyze content and messaging, conversion optimization, SEO and discoverability, competitive positioning, and brand trust. Each gets a 0-100 score. The whole thing takes a couple of minutes and outputs a structured Markdown report. Add pip install reportlab and you get a client-ready PDF.

The 15 commands cover the freelance marketing toolkit: /market copy generates optimized copy with before/after examples, /market emails builds complete email sequences, /market social produces a 30-day content calendar, /market ads writes ad creative for all platforms, /market funnel analyzes conversion paths, /market competitors runs competitive intelligence, /market landing does CRO analysis, /market launch builds a product launch playbook, and /market proposal generates client proposals. It's built for the person who just landed a marketing client and needs to deliver an audit by Friday.

Setup is a one-line curl install or a git clone. The architecture is straightforward: one orchestrator SKILL.md routes commands to 14 sub-skills, and 5 parallel subagents handle the audit dimensions. No external dependencies beyond Claude Code itself, unless you want PDF output.

The limitation is depth. Fifteen skills is a survey, not a specialization. The SEO audit won't match Claude SEO's 25 sub-skills and 18 agents. The ad copy won't match Claude Ads' 250+ platform-specific checks. But for a generalist who needs to audit a website, write some copy, build an email sequence, and hand over a PDF report, this does the job in one install. The repo was last pushed in March 2026, so it's not as actively maintained as some alternatives. The author also ships companion packs for ads (ai-ads-claude) and sales (ai-sales-team-claude) if you want to go deeper on those verticals.
