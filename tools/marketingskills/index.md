# Marketing Skills (coreyhaines31) pricing

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Marketing Skills (coreyhaines31)
## Marketing Skills (coreyhaines31) review (2026): pricing, AI features, verdict

~50 marketing skills for Claude Code, Codex, and Cursor by Corey Haines

Agent Skills · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Marketing Skills (coreyhaines31) →](https://marketing-skills.com)

[How we review](/methodology/) · No affiliate links

**Verdict:** Marketing Skills (coreyhaines31) is a tool in Agent Skills with free and open source. The catalog documents 5 AI features, 5 integrations and a self-hosting path. We reviewed it from vendor documentation on 2026-10-08. This is a desk review, not a hands-on test. Desk-reviewed

[Visit Marketing Skills (coreyhaines31) →](https://marketing-skills.com)

## Catalog facts: Marketing Skills (coreyhaines31)

Not yet scored against the rubric, so no verdict here. This is everything the catalog holds on the tool, verified against vendor sources.

- **Licence:** MIT
- **Public API:** no
- **Catalogued integrations:** 5
- **GitHub stars:** 53,797

The full rubric is on the [methodology page](/methodology/).

## Overview

marketingskills is the biggest marketing skill library for coding agents in this directory: around 50 skills covering CRO, copywriting, SEO, analytics, paid ads, growth loops, and sales ops. It's built by Corey Haines, who runs the Swipe Files newsletter and the Conversion Factory agency, and it shows. These read like playbooks from someone who has actually run marketing programs, not summaries of other people's blog posts. Skills are plain Markdown files that work with Claude Code, OpenAI Codex, Cursor, Windsurf, and anything else following the Agent Skills spec. The repo has 53,000+ GitHub stars, 8,000 forks, was pushed the morning I checked, and carries an MIT license. The structural idea is shared context. A product-marketing skill holds your product, audience, and positioning, and every other skill reads it first before writing anything, so your copy output doesn't come out generic. Skills cross-reference each other: copywriting pulls in cro and ab-testing, revops pulls in sales-enablement and cold-email, customer-research feeds the rest. Day to day you install the pack, describe a task ("audit this landing page", "write my cold email follow-ups", "plan a programmatic SEO template"), and the agent loads the matching framework. Output lands as working documents: audits, copy drafts, test plans, launch checklists. Not chat replies that evaporate. Installation is one command: npx skills add coreyhaines31/marketingskills. The CLI detects which agents you have and drops skills into .claude/skills/ or the shared .agents/skills/ directory. You can install individual skills with --skill cro copywriting. Claude Code and Codex users can also add the repo as a plugin marketplace and install from inside a session. One gotcha the README calls out honestly: if you ask your agent to run the install for you, it may land skills only in .agents/skills/, which Claude Code doesn't read. Pass -a claude-code explicitly. Two things to know before you commit. First, there are disclosed paid partners (Converly for conversion tracking and Ploy for site building at the moment) listed in the tool registry alongside neutral options. The repo states partners don't influence what core skills recommend, and the disclosure rules are public, but you should know the funding exists. Second, these are frameworks and checklists, not software. Nothing sends your email or bids on your ads; the skills shape how your agent thinks about the task. Against Aaron Marketing Skills, with its 120 skills, auditor gates, and lifecycle phases, this pack is looser and more readable: Aaron is process, Corey is judgment. Most founder-led and SaaS marketing teams should start here. At 53,000 stars, if a skill misbehaves, someone has probably already filed the issue.

## AI Capabilities

- ~50 Agent Skills spec Markdown skills: CRO, copywriting, SEO/GEO, analytics, ads, growth, RevOps
- Shared product-marketing context read by all skills so output stays on-positioning
- Cross-referenced skill graph (copywriting/cro/ab-testing, revops/sales-enablement/cold-email)
- marketing-council skill simulates a board of expert advisors
- marketing-loops for recurring agent-run workflows
## Key Integrations

- Claude Code
- OpenAI Codex
- Cursor
- Windsurf
- Agent Skills spec agents
## Pricing

Marketing Skills (coreyhaines31) is free to self-host under the MIT licence.

Free, MIT licensed. Install with npx skills add coreyhaines31/marketingskills or as a Claude Code/Codex plugin.

Current plans and limits live on the [Marketing Skills (coreyhaines31) pricing section](https://github.com/coreyhaines31/marketingskills).

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: ~50 Agent Skills spec Markdown skills: CRO, copywriting, SEO/GEO, analytics, ads, growth, RevOps |  |
| ✓ Active public repository (53,797 GitHub stars counted at last check) |  |
| ✓ Native integrations include Claude Code, OpenAI Codex, Cursor (5 listed) |  |

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Marketing Skills (coreyhaines31)?**
Marketing Skills (coreyhaines31): ~50 marketing skills for Claude Code, Codex, and Cursor by Corey Haines. Marketing Skills (coreyhaines31) ships with ~50 Agent Skills spec Markdown skills: CRO, copywriting, SEO/GEO, analytics, ads, growth, RevOps. The public repository carries 53,797 stars.

**How much does Marketing Skills (coreyhaines31) cost?**
Marketing Skills (coreyhaines31) is open source - MIT licensed and free to self-host; the public repository carries 53,797 stars; native integrations cover Claude Code, OpenAI Codex, Cursor. You pay in server time and maintenance, not licences.

**Is Marketing Skills (coreyhaines31) a good self-hosted Agent Skills tool in 2026?**
Strengths include 53,797 GitHub stars, MIT licensing with free self-hosting. Marketing Skills (coreyhaines31) documents 5 integrations

## Similar Tools

- [Codex SEO](/tools/codex-seo/): Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations
- [Growth Lab](/tools/growth-lab/): Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex
- [Zapier GTM Cheat Codes](/tools/zapier-gtm-cheat-codes/): Zapier's installable coding-agent skills for GTM: campaign planning, CRM context, customer proof
- [AI Business Skills](/tools/ai-business-skills/): 63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents
- [Email Marketing Bible](/tools/email-marketing-bible/): 55K-word email marketing skill with 908 sources, 19 playbooks, and ESP control via MCP
## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [NocoBase vs NocoDB vs Budibase: pick by team shape, not by spec sheet](/blog/nocobase-vs-nocodb-vs-budibase/)
- [Claude SEO benchmark: every score we have earned, and what each one measured](/blog/claude-seo-benchmark/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 53797
- **API:** No
- **Repository checked:** 2026-10-09
- **Page updated:** 2026-10-08

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
