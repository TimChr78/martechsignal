# SEO Skill Bench review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- SEO Skill Bench
Re-check pending: pricing last verified 2026-09-03 (32 days ago).

## SEO Skill Bench review (2026): pricing, AI features, verdict

Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects

Agent Skills · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit SEO Skill Bench →](https://seoagent.com/seo-skill-benchmark)

[How we review](/methodology/) · No affiliate links

**Verdict:** SEO Skill Bench is a tool in Agent Skills with free and open source. The catalog documents 5 AI features, 1 integration and a self-hosting path. We reviewed it from vendor documentation on 2026-09-03. This is a desk review, not a hands-on test. Desk-reviewed

[Visit SEO Skill Bench →](https://seoagent.com/seo-skill-benchmark)

## MartechSignal Score: 31/60

SEO Skill Bench scores Claude Code SEO skills against fixture sites with planted defects and hallucination traps. MIT, and each leaderboard run costs $1.70 to $4.46 in tokens, stated to the cent.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | Free under MIT with leaderboard runs costing $1.70 to $4.46 in LLM tokens each, published as exact figures (the vendor pricing page: [vendor site](https://seoagent.com/seo-skill-benchmark), verified 2026-09-28). |
| Feature depth | 4/10 | Headless skill execution, answer-key scoring and hallucination trap detection cover benchmarking narrowly (vendor documentation: [vendor site](https://seoagent.com/seo-skill-benchmark), verified 2026-09-28). |
| Integrations | 2/10 | Claude Code is the only documented harness (vendor documentation: [vendor site](https://seoagent.com/seo-skill-benchmark), verified 2026-09-28). |
| AI capability | 5/10 | Deterministic planted-defect scoring and trap avoidance measurement are meta-evaluation of AI output (vendor documentation: [vendor site](https://seoagent.com/seo-skill-benchmark), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with fully local execution (the source repository: [repository](https://github.com/aleclindz/seo-skill-bench), verified 2026-09-28). |
| Operational maturity | 2/10 | A young benchmark project with no API (vendor documentation: [vendor site](https://seoagent.com/seo-skill-benchmark), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

SEO Skill Bench answers the question every Claude Code SEO skill README can't: does the thing actually work once installed? It is an open benchmark that runs SEO skills for Claude Code and other coding agents against fixture websites with deliberately planted defects, then scores what they find. If you are choosing an SEO skill for your agent workflow, this is the closest thing to a published answer key. The harness installs each entrant in a real headless Claude Code session (claude -p), not a simulation reconstructed from its README, and points it at the pivot-saas fixture site. Scoring follows a pre-registered 100-point rubric: 40 points for detecting planted defects, 25 for avoiding traps, meaning the skill never recommends fixing something that is already fine, 25 for blind-judged judgment calls, and 10 for execution. Scores are medians across runs. On the August 2026 board, SEOAgent led at 84.9 while the vanilla baseline with no skill scored 73.0. That spread tells you two things: skills can add real value, and some entrants score below doing nothing at all. Setup needs Node and a Claude Code install. You run node harness/run.mjs with a skill id and fixture, then the score and judge scripts, and entrants register with a one-line entry in skills.json. The leaderboard also publishes what each skill costs, kept outside the composite on purpose: resident tokens the skill occupies in every system prompt, per-run cost, and median time. Runs on the board cost between $1.70 and $4.46 and took 405 to 779 seconds. Heavy skills like Corey Haines' Marketing Skills carry 8,770 resident tokens, which dilutes every other skill you have installed. The big caveat is the maintainer's conflict of interest. SEOAgent, the company behind the benchmark, also ships the top-ranked entrant. The structural mitigations are real: published fixtures, deterministic answer keys, a frozen rubric, blind judging, and a harness anyone can re-run. Still, treat the leaderboard as a strong signal rather than gospel. The benchmark only measures technical on-site audit work against one fixture. It says nothing about content strategy, links, or your actual site. At about 51 stars the community is small, and the repo's value is its method more than its momentum. Compared to picking a skill by GitHub stars or vibes, this is the most concrete public way to see detection rates and hallucination traps side by side. If you are building an agent-driven SEO workflow, run your candidate skill through this harness before you point it at a production site.

SEO Skill Bench homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Headless execution of Claude Code SEO skills
- Deterministic planted-defect answer-key scoring
- Hallucination trap detection (trap avoidance)
- Blind judging panel for subjective calls
- Token footprint and per-run cost measurement
## Key Integrations

- Claude Code
## Pricing

SEO Skill Bench is free to self-host under the MIT licence.

Free, MIT licensed. Runs cost LLM API tokens only: leaderboard runs cost $1.70 to $4.46 each.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Young project (51 GitHub stars) - smaller community and plugin ecosystem |
| ✓ AI capabilities: headless execution of Claude Code SEO skills | ✗ Short native integration list - plan for API work |
| ✓ Native integrations include Claude Code (1 listed) |  |

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is SEO Skill Bench?**
SEO Skill Bench: Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects. SEO Skill Bench ships with headless execution of Claude Code SEO skills. The public repository carries 51 stars.

**How much does SEO Skill Bench cost?**
SEO Skill Bench is open source - MIT licensed and free to self-host; the public repository carries 51 stars. You pay in server time and maintenance, not licences.

**Is SEO Skill Bench a good self-hosted Agent Skills tool in 2026?**
Strengths include 51 GitHub stars, MIT licensing with free self-hosting. SEO Skill Bench documents 1 integration

## Similar Tools

- [Zapier GTM Cheat Codes](/tools/zapier-gtm-cheat-codes/): Zapier's installable coding-agent skills for GTM: campaign planning, CRM context, customer proof
- [Digital Marketing Pro](/tools/digital-marketing-pro/): 163-skill AI marketing plugin for agencies with EU AI Act compliance
- [Aaron Marketing Skills](/tools/aaron-marketing-skills/): 120 marketing skills across 7 disciplines for Claude Code with auditor gates
- [AI Business Skills](/tools/ai-business-skills/): 63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents
- [Claude Ads](/tools/claude-ads/): Paid-media operations skill for Claude Code covering 12 ad platforms
## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Two ways to buy the same workflow debt: task-metered and operations-metered](/blog/zapier-vs-make-two-ways-to-buy-the-same-workflow-debt/)
- [Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough](/blog/salesforce-claude-commerce-cloud-agentforce/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 51
- **API:** No
- **Repository checked:** 2026-09-29
- **Page updated:** 2026-09-03

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
