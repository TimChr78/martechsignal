# Aaron Marketing Skills | MartechSignal review

120 marketing skills across 7 disciplines for Claude Code with auditor gates

- Page: https://martechsignal.com/tools/aaron-marketing-skills/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (Apache-2.0)
- Last verified: 2026-08-28

Aaron Marketing Skills is a 120-skill library that turns Claude Code into a marketing operator across seven disciplines: brand narrative, SEO/GEO, social, email, paid ads, influencer, and product launch. Each discipline follows a lifecycle with phase directories. SEO goes survey, implement, tune, evaluate. Email goes setup, engage, nurture, deliver. Paid ads goes research, orchestrate, activate, scale. The /aaron-marketing:auto command routes any natural-language goal to the right skill, so you don't memorize 120 slash commands.

What makes this different from a prompt pack is the protocol layer. Eight shared commands and seven truth registries (entity, creator, offer/claims, consent, launch, channel, narrative) enforce consistency across skills. Six auditor gates score output quality: CORE-EEAT for content, CITE for domain authority, C3 for creative, ROAS for ad accounts, SEND for email, and RAMP for launches. Skills and commands are plain Markdown. Small Bash and Python-stdlib runtimes handle hooks, validation, scoring, and CI checks. No pip, no build step. Every skill runs self-contained.

Installation is a git clone into your skills directory. It works on Claude Code, Codex, Gemini CLI, and Cursor. The README is available in 10 languages, which hints at the author's ambition. Version 19.0.0 is current as of late July 2026, and the repo was pushed to today, so maintenance is active.

The trade-off with 120 skills is depth versus breadth. Each discipline gets 16 skills, which is enough for structured workflows but not the 158-skill depth of Digital Marketing Pro or the platform-specific granularity of Claude Ads. If you want one skill pack that covers everything marketing at a competent level, this is it. If you need deep paid-media operations specifically, Claude Ads goes further on that vertical. If you're an agency that needs brand narrative and launch planning alongside the performance channels, Aaron's lifecycle structure and auditor gates give you a framework that the narrower tools don't.
