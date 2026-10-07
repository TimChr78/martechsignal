# Digital Marketing Pro pricing

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Digital Marketing Pro
KIND: Agent Skill (not an end-to-end platform)

## Digital Marketing Pro review (2026): pricing, AI features, verdict

163-skill AI marketing plugin for agencies with EU AI Act compliance

Agent Skills · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Digital Marketing Pro →](https://github.com/indranilbanerjee/digital-marketing-pro)

[How we review](/methodology/) · No affiliate links

**Verdict:** Digital Marketing Pro is a tool in Agent Skills with free and open source. The catalog documents 5 AI features, 8 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-28. This is a desk review, not a hands-on test. Desk-reviewed

[Visit Digital Marketing Pro →](https://github.com/indranilbanerjee/digital-marketing-pro)

## Catalog facts: Digital Marketing Pro

Not yet scored against the rubric, so no verdict here. This is everything the catalog holds on the tool, verified against vendor sources.

- **Founded:** 2025
- **Licence:** MIT
- **Public API:** yes
- **Catalogued integrations:** 8
- **GitHub stars:** 854

The full rubric is on the [methodology page](/methodology/).

## Overview

Digital Marketing Pro is the heaviest skill pack in this category: 163 skills, 24 specialist agents, 18 commands, and 86 scripts. It's built for agencies and in-house teams managing 50-200 brands. The core workflow is a 12-Part Strategy Flow that produces Four Core Documents per brand, following a 61-step structure. Run /digital-marketing-pro:engagement against a brand and you get a full strategy engagement in roughly 60 minutes on an Opus-class model. The pitch is consistency: same depth, same structure, same audit trail across your entire portfolio, whether you have 3 brands or 200. The compliance angle is what makes this interesting for agencies operating in regulated markets. Version 3.31.1 (August 2026) ships EU AI Act Article 50 readiness, including C2PA content provenance and an --ai-disclosure flag for generated content. The v3.15.0 release before it purged fictional npm packages, added uniform typed-approval gates across all 18 execution skills, and consolidated agents from 25 to 24. The changelog reads like someone who takes reliability seriously. over 400 stdlib tests pass. A 16-reader audit fleet re-verified all 530 files against July 2026 ground truth and shipped roughly 250 fixes. It installs on eight native platforms (Claude Code, Cowork, Codex, Cursor, Copilot CLI, Antigravity, Hermes Agent, OpenClaw) plus 35 more via the Agent Skills open standard. The Cowork integration means team-persistent state: your brand documents and strategy context survive across sessions and team members. That's a real workflow feature, not a checkbox. The trade-off is complexity. 163 skills is a lot to learn. The README opens with a scenario about a 50-brand client and a bleeding budget, which tells you the intended user: someone who already knows marketing strategy and wants to scale its execution. If you're a solo freelancer auditing one website, AI Marketing Suite's 15 commands will get you there faster. If you're an agency that needs auditable, compliant, consistent strategy work across a portfolio, this is the only skill pack built for that.

Digital Marketing Pro homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- 163 skills with 24 specialist agents
- 12-Part Strategy Flow with Four Core Documents
- EU AI Act Article 50 compliance (C2PA, AI disclosure)
- Cowork team-persistent state
- 61-step engagement structure per brand
## Key Integrations

- Claude Code
- Anthropic Cowork
- OpenAI Codex
- Cursor
- GitHub Copilot CLI
- Google Antigravity
- Hermes Agent
- OpenClaw
## Pricing

Digital Marketing Pro is free to self-host under the MIT licence.

Free, MIT-licensed. Runs on Claude Code, Codex, Cursor, Copilot CLI, and 35+ agent platforms.

## Requirements

An agent CLI from the supported platform list and a Claude-class model with enough context for long planning sessions. The pack itself is free and MIT-licensed; model and platform costs remain yours.

## Best for

Agencies that want one planning methodology shared across every seat and every agent platform, especially shops with EU clients who need disclosure documents as a starting point.

## Not for

Teams that need live data inside their planning. Nothing in the pack connects to an ad account or an analytics property, so the frameworks run on whatever context you paste in.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Digital Marketing Pro is a skill pack for Claude-class agents covering campaign planning and channel strategy prompts. Loading it gives an agent structured planning frameworks rather than integrations - nothing connects to ad accounts directly. Value depends entirely on how much rigour your bare prompting lacks.

Useful if your agent sessions drift without structure; experienced strategists may find it constraining. Check whether the frameworks match how your team already plans.

The 12-Part Strategy Flow is the spine of the pack. It walks an agent from market context through channel planning to a four-document output set, so a planning session ends with artifacts instead of a chat transcript. Teams that already run a documented planning process will recognize the stages. The pack simply encodes them as prompts an agent can execute in order.

The EU AI Act compliance piece is documentation tooling: checklists and disclosure templates rather than legal advice. Treat it as a drafting head start that counsel still reviews before anything ships. For agencies with EU clients that paperwork is real recurring work, and starting from a first draft instead of a blank page is the part clients actually feel.

Platform breadth is the other half of the pitch. The same pack loads into Claude Code, Codex, Cursor, and GitHub Copilot CLI, so a mixed-tooling shop does not have to standardize before adopting it. Prompts do behave differently across models, though. Budget an afternoon per platform to see which of the 163 skills hold up on your stack before promising the coverage internally.

Maintenance is the quiet cost nobody prices. A 163-skill library is a library: skills drift as models change, and someone has to own the review loop. In practice one person spending an hour a month reading what the agents produced is enough to catch a skill that has gone stale against your methodology.

One honest limit worth stating before anyone buys into the breadth. A skill pack improves the shape of what an agent produces; it does not add data the agent cannot see. The strongest results in any planning session will still come from feeding the pack real inputs: your funnel numbers, your actual creative, the competitor set you really face. The frameworks organize that material. They do not replace it.

Where the pack clearly earns its keep is consistency across people. When a junior and a twenty-year strategist run the same 12-part flow, the outputs are comparable, and comparability is what makes review possible at agency speed. That is a quality-of-work argument more than a speed argument, and it is the one to make internally if adoption needs a champion.

The four core documents that anchor the strategy flow are the part worth previewing before you commit. Roughly: a market read, a positioning statement, a channel plan, and a measurement frame. Each document feeds the next, so skipping one to save time tends to surface later as a channel plan with nothing to prove against. The chain is the product. The individual prompts are replaceable.

On cost, the framing is simple: the pack is free and MIT-licensed, and every token it consumes is billed by whoever provides your model. Compare that to per-seat planning software and the math favors heavy users first. Light users should run a single project through the flow before deciding, because the value shows up in artifacts, not in the session log.

A sensible week-one rollout is narrower than the library suggests. Pick the strategy flow plus the two or three channel skills that match live work, run one real project end to end, and only then widen. Teams that install 163 skills at once tend to spend the first month learning the library instead of finishing the campaign that justified it.

Organizationally, the pack wants a named owner. The skills run anywhere, but somebody has to decide which four documents are canonical this quarter and who signs the positioning statement before it reaches a client. Shops that treat the library as shared infrastructure with one maintainer keep the value. Shops that treat it as a download drift back to bare prompting within a month, and unstructured drift is exactly the problem the pack was bought to solve.

The clearest adoption signal to watch in month one is document reuse. When the second project starts from last quarter's four documents instead of a blank prompt, the library is doing its job. If nothing is ever reused, the framework tax is not paying for itself.

## Verdict

Reasonable scaffolding for agent-run campaign planning; brings process, not magic.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: 163 skills with 24 specialist agents |  |
| ✓ Native integrations include Claude Code, Anthropic Cowork, OpenAI Codex (8 listed) |  |

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Digital Marketing Pro?**
Digital Marketing Pro: 163-skill AI marketing plugin for agencies with EU AI Act compliance. Digital Marketing Pro ships with 163 skills with 24 specialist agents. The public repository carries 854 stars.

**How much does Digital Marketing Pro cost?**
Digital Marketing Pro is open source - MIT licensed and free to self-host; the public repository carries 854 stars; native integrations cover Claude Code, Anthropic Cowork, OpenAI Codex. You pay in server time and maintenance, not licences.

**Is Digital Marketing Pro a good self-hosted Agent Skills tool in 2026?**
Reasonable scaffolding for agent-run campaign planning; brings process, not magic.

**Does Digital Marketing Pro have an API?**
Yes. The catalog records a public API for Digital Marketing Pro, so custom integrations are possible. The Key Integrations section shows what ships natively.

## Similar Tools

- [Codex SEO](/tools/codex-seo/): Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations
- [Aaron Marketing Skills](/tools/aaron-marketing-skills/): 120 marketing skills across 7 disciplines for Claude Code with auditor gates
- [AI Business Skills](/tools/ai-business-skills/): 63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents
- [SEO Skill Bench](/tools/seo-skill-bench/): Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects
- [Diffmode Growth Tactics](/tools/diffmode-growth-tactics/): Free Claude Code/Codex pipeline that mines case studies and rejects obvious growth plays
## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [MCP Rewrites the Integration Economics of Your Marketing Stack](/blog/mcp-rewrites-the-integration-economics-of-your-marketing-stack/)
- [The fully open-source agentic marketing stack you can run today: 19 MCP servers, one agent](/blog/open-source-agentic-martech-stack-mcp/)
## Also featured in

- [Best Agent Skills tools (2026): 8 compared](/best/agent-skills-tools/) — Best for agent skills teams that want cowork team-persistent state and can host it themselves, with a free starting tier.
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 854
- **Founded:** 2025
- **API:** Yes
- **Repository checked:** 2026-10-07
- **Page updated:** 2026-09-28

Related guides: [Agent Skills Tools](/best/agent-skills-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
