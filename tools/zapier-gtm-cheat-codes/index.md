# Zapier GTM Cheat Codes | MartechSignal review

Zapier's installable coding-agent skills for GTM: campaign planning, CRM context, customer proof

- Page: https://martechsignal.com/tools/zapier-gtm-cheat-codes/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-08-31

GTM Cheat Codes is the skill library Zapier's own go-to-market teams use with coding agents. It turns scattered context, CRM records, meeting notes, campaign docs, and customer stories, into reviewable work products. The repo ships installable skills for campaign planning, postmortems, media inbox triage, lead follow-up QA, account prioritization, customer decks, and content repurposing. Each skill maps a business problem to a workflow that runs in Codex, Claude Code, Cursor, or ChatGPT with Zapier MCP handling the authenticated actions.

The design philosophy is source-backed execution. Skills read from the systems of record, build a draft artifact, and stop at an approval gate before anything writes back to a CRM, sends a message, or publishes. Every skill folder has a README, a SKILL.md with the instructions, a SETUP.md, and a schema map. A registry CSV lets you find the skill closest to your workflow without reading all of them.

Setup is heavier than a prompt pack. You need a coding agent installed, Zapier MCP or SDK credentials with least-privilege scopes, and your CRM and docs connected through Zapier. The docs assume you can map a workflow to your own approved systems. A GTM operations person can manage it; a pure marketer without any tooling comfort will struggle.

The directory already covers Zapier's flagship automation platform, but that entry is about the SaaS workflow tool. This is a different artifact: a free skill pack for agent harnesses, with real approval-gate discipline that most prompt libraries skip. It is the strongest general GTM skill library in this category, broader than the SEO- or social-specific packs. If your team already runs coding agents and lives in Zapier-connected tools, this is the first skill pack to install.
