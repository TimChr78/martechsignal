# Growth Lab review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Growth Lab
Re-check pending: pricing last verified 2026-08-28 (39 days ago).

## Growth Lab review (2026): pricing, AI features, verdict

Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex

Agent Skills · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Growth Lab →](https://growthlab.tsingyuai.com)

[How we review](/methodology/) · No affiliate links

**Verdict:** Growth Lab is a tool in Agent Skills with free and open source. The catalog documents 5 AI features, 4 integrations and a self-hosting path. We reviewed it from vendor documentation on 2026-08-28. This is a desk review, not a hands-on test. Desk-reviewed

[Visit Growth Lab →](https://growthlab.tsingyuai.com)

## MartechSignal Score: 34/60

Growth Lab runs two growth loops as skills: SEO pages with IndexNow publishing and a Xiaohongshu content loop. Apache-2.0 and 1,993 stars; the harness cost is on you.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free under Apache 2.0 with Claude Code or Codex costs as the stated run expense (the vendor pricing page: [vendor site](https://growthlab.tsingyuai.com), verified 2026-08-28). |
| Feature depth | 5/10 | SEO page growth and Xiaohongshu loops cover two growth motions end to end (vendor documentation: [vendor site](https://growthlab.tsingyuai.com), verified 2026-09-28). |
| Integrations | 4/10 | Claude Code, Codex, IndexNow and Bing Webmaster Tools documented (vendor documentation: [vendor site](https://growthlab.tsingyuai.com), verified 2026-09-28). |
| AI capability | 5/10 | Scenario research and SERP analysis feeding page creation run as agent loops (vendor documentation: [vendor site](https://growthlab.tsingyuai.com), verified 2026-09-28). |
| Openness | 9/10 | Apache-2.0 with a self-hosted workspace (the source repository: [repository](https://github.com/tsingyuai/growth-lab), verified 2026-09-28). |
| Operational maturity | 3/10 | Founded 2026 with no API of its own (vendor documentation: [vendor site](https://growthlab.tsingyuai.com), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Growth Lab is an agent skill pack that turns Claude Code or OpenAI Codex into a growth operator. You clone the repo, open the folder in your agent, and describe the growth outcome you want. The agent reads your product (a codebase, a prototype, or just a URL), researches what people actually search for, creates SEO pages aimed at those queries, publishes them, pings IndexNow, then reads the performance data and decides what to do next. The pitch is that context stops leaking between five disconnected tools. One workspace holds the product, the research, the output, and the results. Skills carry the method, and files carry the memory. Each capability is an observe-act-review loop with its own persistent memory, and the next run reads the previous results before it starts. The SEO loop maps user scenarios to live SERP research and generates pages that answer real queries. In the team's own test run, new pages got indexed within 1-2 days and page impressions and clicks both rose about 10x on a 7-day average. Average CTR dropped 50%, which they treated as input for the next iteration rather than a failure. The second loop targets Xiaohongshu: it collects high-performing posts in your niche, replicates the winning structure, writes the copy, generates images, runs a compliance check, and reviews the results. Their best test post drew 4,000+ likes and saves. Actual publishing on Xiaohongshu stays manual by design. Setup is git clone plus a conversation. An onboarding skill audits what's missing: API keys, browser sessions, third-party clients. You fix gaps in plain language instead of editing a config file. Secrets and cookies stay outside the workspace and never enter memory. The repo is Apache 2.0 licensed, was pushed within days of this writing. The honest caveats: the project is roughly a week old. Only two loops actually work, and all the performance numbers come from a single run on the authors' own site. You need paid access to Claude Code or Codex, plus comfort working in a terminal with an agent. If your channels are X, LinkedIn, or TikTok, there's no loop for those yet. Who it's for: technical founders and small teams already living in a coding agent who want the growth work done rather than another dashboard. Compared with Surfer or Semrush, it writes and publishes the page instead of handing you recommendations. Compared with doing it manually, the research-to-publish cycle becomes one conversation. Compared with most agent skill packs, which teach the agent marketing knowledge, this one runs the loop end to end, memory included.

Growth Lab homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- SEO page growth loop: scenario research, SERP analysis, page creation, IndexNow publishing
- Xiaohongshu loop: viral post collection, structure replication, copy, images, compliance check
- Persistent per-loop memory that feeds real results into the next run
- Product understanding from a repo, prototype, URL, or notes
- Natural-language configuration audit via the onboarding skill
## Key Integrations

- Claude Code
- OpenAI Codex
- IndexNow
- Bing Webmaster Tools
## Pricing

Growth Lab is free to self-host under the Apache-2.0 licence.

Free, Apache 2.0. Self-hosted workspace; runs inside Claude Code or OpenAI Codex (both paid).

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Growth Lab turns Claude Code or Codex into a growth operator: describe the outcome, and the agent reads your product from a codebase, prototype, or URL, researches real search queries, creates SEO pages around them, publishes, pings IndexNow, then reads the performance data and decides what to do next. It is a loop rather than one-shot generation, and the research and results share one workspace, so context stops leaking between tools.

Publishing from an agent means you own the pipeline: hosting, deploys, and content review on your side, which is a real commitment. The project is young, and the results ceiling is your model's judgment, so weak pages can ship at loop speed if you skip review. The Xiaohongshu growth loops are a rare China-market angle in Western tooling.

## Verdict

Promising for teams ready to run self-hosted SEO loops with agent review. Everyone else should wait for maturity.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ Apache-2.0 licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: SEO page growth loop: scenario research, SERP analysis, page creation, IndexNow publishing |  |
| ✓ Active public repository (1,993 GitHub stars counted at last check) |  |

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Growth Lab?**
Growth Lab: Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex. Growth Lab ships with SEO page growth loop: scenario research, SERP analysis, page creation, IndexNow publishing. The public repository carries 1,993 stars.

**How much does Growth Lab cost?**
Growth Lab is open source - Apache-2.0 licensed and free to self-host; the public repository carries 1,993 stars; native integrations cover Claude Code, OpenAI Codex, IndexNow. You pay in server time and maintenance, not licences.

**Is Growth Lab a good self-hosted Agent Skills tool in 2026?**
Promising for teams ready to run self-hosted SEO loops with agent review. Everyone else should wait for maturity.

## Similar Tools

- [Codex SEO](/tools/codex-seo/): Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations
- [SEO Skill Bench](/tools/seo-skill-bench/): Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects
- [Claude SEO](/tools/claude-seo/): Open-source SEO skill for Claude Code with 25 sub-skills and 20 specialist agents
- [AI Business Skills](/tools/ai-business-skills/): 63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents
- [Aaron Marketing Skills](/tools/aaron-marketing-skills/): 120 marketing skills across 7 disciplines for Claude Code with auditor gates
## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [ChatGPT Isn't Search Anymore, It's Checkout](/blog/chatgpt-isnt-search-anymore-its-checkout/)
- [The CDP Reckoning: Your Next CDP Is a Data Platform You Already Pay For](/blog/cdp-reckoning-warehouse-native/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 1993
- **Founded:** 2026
- **API:** No
- **Repository checked:** 2026-10-06
- **Page updated:** 2026-08-28

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
