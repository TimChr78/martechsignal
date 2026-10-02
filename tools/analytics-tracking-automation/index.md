# Analytics Tracking Automation pricing

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Analytics Tracking Automation
Re-check pending: pricing last verified 2026-08-28 (35 days ago).

## Analytics Tracking Automation review (2026): pricing, AI features, verdict

AI skill for GA4 + GTM event tracking: site analysis, schema design, and go-live

Agent Skills · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Analytics Tracking Automation →](https://www.jtracking.ai/skills)

[How we review](/methodology/) · No affiliate links

[Visit Analytics Tracking Automation →](https://www.jtracking.ai/skills)

## MartechSignal Score: 34/60

This npm skill does the unglamorous work: GA4 event schemas and GTM-ready output with verification. Small, free, and useful exactly once per site.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 10/10 | Free under Apache 2.0, npm-based, nothing to price (the vendor pricing page: [vendor site](https://www.jtracking.ai/skills), verified 2026-08-28). |
| Feature depth | 4/10 | Site analysis, page grouping, GA4 schema design and GTM output with verification cover one job (vendor documentation: [vendor site](https://www.jtracking.ai/skills), verified 2026-09-28). |
| Integrations | 4/10 | GA4, Google Tag Manager, Cursor, Codex and Shopify documented (vendor documentation: [vendor site](https://www.jtracking.ai/skills), verified 2026-09-28). |
| AI capability | 4/10 | Agent-run tracking design is the whole scope by design (vendor documentation: [vendor site](https://www.jtracking.ai/skills), verified 2026-09-28). |
| Openness | 9/10 | Apache-2.0 with readable source (the source repository: [repository](https://github.com/jtrackingai/analytics-tracking-automation), verified 2026-09-28). |
| Operational maturity | 3/10 | Founded 2025; a focused small project (vendor documentation: [vendor site](https://www.jtracking.ai/skills), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Analytics Tracking Automation solves a specific, annoying problem: setting up GA4 and GTM event tracking correctly. Most marketing teams either skip proper tracking setup or pay a consultant $2,000 to do it. This skill automates the workflow from site analysis to go-live. You give it a URL, and it analyzes the site, groups pages by business purpose, designs a GA4 event schema, produces GTM-ready outputs, and walks you through verification before publishing. It handles both generic websites and Shopify storefronts. The workflow is artifact-backed, meaning each step produces a reviewable file you can inspect before moving on. The site analysis groups pages into business categories (product, checkout, blog, support) so the event schema maps to actual user journeys rather than generic pageview tracking. The GTM output includes the container configuration, trigger definitions, and variable setup. Verification guidance tells you what to check in GTM preview mode before you publish. If you stop halfway through, the artifacts let you resume where you left off. Installation is npm-based: clone the repo and run npm run install:skills, or use npx skills add jtrackingai/analytics-tracking-automation for a no-clone install. It works on Cursor, Codex, and any agent that reads the skill format. The ClawHub publish path strips executable runtime files for marketplace safety. This is the narrowest tool in this batch, and that's its strength. It doesn't try to be a full marketing suite. It does one thing that every marketing team needs and few do well. With barely a hundred stars, it's the smallest repo here, and the last push was April 2026, so it's not getting weekly updates. But the problem it solves doesn't change often. GA4's event model is stable, GTM's container format is stable, and the workflow from "we need tracking" to "tracking is live and verified" is well-defined. If you're setting up analytics for a new site or auditing an existing GTM mess, this saves you a day of spreadsheet work and a week of "is this firing correctly?" anxiety.

Analytics Tracking Automation homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Automated site analysis and page grouping by business purpose
- GA4 event schema design and review
- GTM-ready output generation with verification guidance
- Shopify storefront support
- Artifact-backed progress that can be resumed
## Key Integrations

- GA4
- Google Tag Manager
- Cursor
- Codex
- Shopify
## Pricing

Analytics Tracking Automation is free to self-host under the Apache-2.0 licence.

Free. Runs on Cursor, Codex, and any AI agent. npm-based install.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Give this skill a URL and it walks the full GA4 and GTM setup: it analyzes the site, groups pages by business purpose, designs a GA4 event schema, produces GTM-ready outputs, and runs you through verification before anything goes live. Shopify storefronts get their own handling. A workflow that normally costs a $2,000 consultant becomes a session that leaves reviewable artifacts at every step, so nothing happens invisibly.

The honest caveats: the schema it proposes is a starting point, not the final word, and your team should sign off before publishing, since a bad event model is worse than none. The project is young with a small community, and the skill is only as current as the GA4 interface it documents. For teams stuck with no tracking at all, it is a fast rescue that beats another quarter of guessing.

## Verdict

Free and fast if tracking keeps slipping through the cracks. Review every schema it proposes before publishing anything.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ Apache-2.0 licence with free self-hosting | ✗ Young project (141 GitHub stars) - smaller community and plugin ecosystem |
| ✓ AI capabilities: automated site analysis and page grouping by business purpose |  |
| ✓ Native integrations include GA4, Google Tag Manager, Cursor (5 listed) |  |

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Analytics Tracking Automation?**
Analytics Tracking Automation: AI skill for GA4 + GTM event tracking: site analysis, schema design, and go-live. Analytics Tracking Automation ships with automated site analysis and page grouping by business purpose. The public repository carries 141 stars.

**How much does Analytics Tracking Automation cost?**
Analytics Tracking Automation is open source - Apache-2.0 licensed and free to self-host; the public repository carries 141 stars; native integrations cover GA4, Google Tag Manager, Cursor. You pay in server time and maintenance, not licences.

**Is Analytics Tracking Automation a good self-hosted Agent Skills tool in 2026?**
Free and fast if tracking keeps slipping through the cracks. Review every schema it proposes before publishing anything.

## Similar Tools

- [AI Business Skills](/tools/ai-business-skills/): 63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents
- [SEO Skill Bench](/tools/seo-skill-bench/): Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects
- [Zapier GTM Cheat Codes](/tools/zapier-gtm-cheat-codes/): Zapier's installable coding-agent skills for GTM: campaign planning, CRM context, customer proof
- [Codex SEO](/tools/codex-seo/): Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations
## Related reading

- [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/)
- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Two ways to buy the same workflow debt: task-metered and operations-metered](/blog/zapier-vs-make-two-ways-to-buy-the-same-workflow-debt/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 141
- **Founded:** 2025
- **API:** Yes
- **Repository checked:** 2026-10-02
- **Page updated:** 2026-08-28

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
