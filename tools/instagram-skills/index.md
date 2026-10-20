# Instagram Skills pricing

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Instagram Skills
## Instagram Skills review (2026): pricing, AI features, verdict

9 Instagram marketing skills for Claude Code and Codex: captions, carousels, hooks, hashtags

Agent Skills · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Instagram Skills →](https://github.com/sergebulaev/instagram-skills)

[How we review](/methodology/) · No affiliate links

**Verdict:** Instagram Skills is a tool in Agent Skills with free and open source. The catalog documents 9 AI features, 9 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-10-12. This is a desk review, not a hands-on test. Desk-reviewed

[Visit Instagram Skills →](https://github.com/sergebulaev/instagram-skills)

## Catalog facts: Instagram Skills

Not yet scored against the rubric, so no verdict here. This is everything the catalog holds on the tool, verified against vendor sources.

- **Licence:** MIT
- **Public API:** yes
- **Catalogued integrations:** 9
- **GitHub stars:** 523

The full rubric is on the [methodology page](/methodology/).

## Overview

instagram-skills turns Claude Code or Codex into an Instagram content desk. Nine skills cover the channel end to end: a caption writer, carousel planner, hook extractor, hashtag strategist, humanizer, weekly content planner, repurposer, profile optimizer, and audience insights. You ask in plain language ("write a caption for this Reel", "plan a week of posts for my design course launch") and the right skill activates. It comes from Creative Content Crafts, an agency that open-sourced the top layer of its internal content stack under MIT. 374 GitHub stars and a push in October 2026 at the time of writing, so it is young but alive. Each skill is a SKILL.md prompt file backed by shared references: 10 hook formulas, 2026 Instagram algorithm heuristics, and a sized-hashtag model that argues for 3-5 tags you can rank in instead of a 30-tag wall. The voice rules are unusually concrete. The hook must fit the first 125 characters because the rest sits behind the "more" fold. Em dashes are capped at roughly one per 100 words. One AI-vocabulary marker in a paragraph passes; three triggers a rewrite. The bundled humanizer strips AI tells and ships an audit mode you can run on any draft before posting. Every draft waits for your approval; nothing publishes silently. Publishing itself is optional and runs through Publora, a separate product from the same company, which handles Instagram's draft, upload-to-S3, then schedule flow in one API call. Pixfaro (image generation) and Apify (reading real niche data) are optional add-ons behind their own keys. Setup takes one command in most environments: codex plugin marketplace add sergebulaev/instagram-skills for Codex CLI, /plugin install for Claude Code, paste the repo into the Skills panel on claude.ai, or run npx skills add for anything that reads SKILL.md files, including Cursor, OpenClaw, and Hermes Agent. The Python lib wants requests and python-dotenv. Auto-posting needs a Business or Creator Instagram account, a Publora API key, and a platform ID in .env. Audience insights needs an Apify token. Without any keys the skills still write everything and hand you copy-paste blocks. The honest limits. There is no read layer by default: the hook extractor asks you to paste the Reel caption yourself, because Instagram offers no cheap documented way to read posts. You always supply the media, since Instagram rejects text-only posts and these skills only write words. Auto-posting ties you to Publora, a third-party service run by the same vendor, so you are really evaluating a bundle, and the free repo is also the top of a funnel for the agency's paid content-engineering work. None of that disqualifies it, but go in aware. Against SaaS alternatives the split is clean: Buffer and Hootsuite schedule but do not write, Predis.ai writes but is closed and per-seat. Against the other skill packs in this directory, Aaron Marketing Skills spans seven disciplines with 120 skills, but nothing there goes as deep on one channel as this goes on Instagram. If Instagram is where your audience lives and you already work in an agent CLI, this is the most specialized free option we have listed. If you do not run one, a scheduler plus a general chatbot gets you most of the way with less setup.

## AI Capabilities

- Caption and Reels hook writing in your voice with a 125-char hook rule
- Carousel planning (up to 10 slides) with hook, value, and payoff structure
- Hook extractor that reverse-engineers viral Reels into fill-in templates
- Sized hashtag sets (3-5 niche/mid/broad tags instead of 30)
- Humanizer skill that strips AI tells, with a pre-publish audit mode
- Weekly content planner with Reels/carousel/story mix and posting times
- Cross-platform repurposing (LinkedIn, blog, YouTube, X to native Instagram)
- Profile optimizer with scorecard and before/after rewrites
- Audience insights from real Instagram data via Apify
## Key Integrations

- Claude Code
- Codex CLI
- claude.ai
- Cursor
- OpenClaw
- Hermes Agent
- Publora
- Apify
- Pixfaro
## Pricing

Instagram Skills is free to self-host under the MIT licence.

Free, MIT licensed. Optional paid dependencies: Publora for auto-publishing, Apify for audience data, Pixfaro for image generation.

Current plans and limits live on the [Instagram Skills pricing section](https://github.com/sergebulaev/instagram-skills).

## Best for

Creators, founders and small marketing teams that run Claude Code or Codex daily and want agent-written Instagram captions, carousels and weekly plans with an approval gate before anything publishes.

## Not for

Teams that do not use an agent CLI, accounts that need Instagram analytics or engagement management (there is no read layer without Apify), and anyone unwilling to depend on Publora for auto-posting.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Nine skills that activate on plain-language Instagram requests inside Claude Code or Codex: captions with the hook forced into the first 125 characters, carousels planned slide by slide, 3-5 sized hashtags instead of the old 30-tag wall, and a humanizer with an audit mode that checks drafts for AI tells before you post. Shared reference files carry the 10 hook formulas and 2026 algorithm heuristics every skill inherits, so output is consistent across the pack rather than per-prompt luck.

Drafts always wait for approval; publishing is opt-in through Publora (same vendor), which runs Instagram's draft, S3 upload, schedule flow in one call and needs a Business or Creator account. No read layer by default, so the hook extractor wants you to paste Reel captions, and Apify is an optional paid add-on for real niche data. You always supply the media. At 374 stars the community is small and the free repo doubles as the top of the agency's funnel, but MIT plus one-command installs across Claude Code, Codex, Cursor, OpenClaw and Hermes make the trial cost near zero.

## Verdict

The most Instagram-specific free skill pack we list. Best if you already work in an agent CLI; Publora dependency and no read layer are the trade-offs.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: caption and Reels hook writing in your voice with a 125-char hook rule |  |
| ✓ Native integrations include Claude Code, Codex CLI, claude.ai (9 listed) |  |

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Instagram Skills?**
Instagram Skills: 9 Instagram marketing skills for Claude Code and Codex: captions, carousels, hooks, hashtags. Instagram Skills ships with caption and Reels hook writing in your voice with a 125-char hook rule. The public repository carries 523 stars.

**How much does Instagram Skills cost?**
Instagram Skills is open source - MIT licensed and free to self-host; the public repository carries 523 stars; native integrations cover Claude Code, Codex CLI, claude.ai. You pay in server time and maintenance, not licences.

**Is Instagram Skills a good self-hosted Agent Skills tool in 2026?**
The most Instagram-specific free skill pack we list. Best if you already work in an agent CLI; Publora dependency and no read layer are the trade-offs.

**Does Instagram Skills have an API?**
Yes. The catalog records a public API for Instagram Skills, so custom integrations are possible. The Key Integrations section shows what ships natively.

## Similar Tools

- [Marketing Skills (coreyhaines31)](/tools/marketingskills/): ~50 marketing skills for Claude Code, Codex, and Cursor by Corey Haines
- [Codex SEO](/tools/codex-seo/): Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations
- [Digital Marketing Pro](/tools/digital-marketing-pro/): 163-skill AI marketing plugin for agencies with EU AI Act compliance
- [AI Business Skills](/tools/ai-business-skills/): 63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents
- [Marketing Studio](/tools/marketing-studio/): Agent-driven marketing studio for Claude Code: launch assets from one command
## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Braze moved AI from content to campaign operations: who approves when the campaign runs itself](/blog/braze-ai-campaign-operations/)
- [Before your next automation, run the blast radius audit](/blog/automation-blast-radius-audit/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 523
- **API:** Yes
- **Repository checked:** 2026-10-20
- **Page updated:** 2026-10-12

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
