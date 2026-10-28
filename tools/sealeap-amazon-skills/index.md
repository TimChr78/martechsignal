# SeaLeap Amazon Skills pricing

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- SeaLeap Amazon Skills
Review · Agent Skills

## SeaLeap Amazon Skills review (2026): pricing, AI features, verdict

602 free Amazon seller skills for Claude Code: research, listings, ads, inventory

By [Tim Christensen](/authors/tim-christensen/) · updated 2026-10-26 · Open Source Desk-reviewed

Not yet scored

- **Price:** Open Source
- **Licence:** MIT
- **GitHub stars:** 332

[How we review](/methodology/) · No affiliate links

**Verdict:** SeaLeap Amazon Skills is a tool in Agent Skills with free and open source. The catalog documents 6 AI features, 6 integrations and a self-hosting path. We reviewed it from vendor documentation on 2026-10-26. This is a desk review, not a hands-on test. Desk-reviewed

## Catalog facts: SeaLeap Amazon Skills

Not yet scored against the rubric, so no verdict here. This is everything the catalog holds on the tool, verified against vendor sources.

- **Founded:** 2026
- **Headquarters:** China
- **Licence:** MIT
- **Public API:** no
- **Catalogued integrations:** 6
- **GitHub stars:** 332

The full rubric is on the [methodology page](/methodology/).

## Overview

SeaLeap Amazon Skills is 602 free agent skills for people who sell on Amazon and want Claude Code or Codex to reason with Amazon's vocabulary instead of generic ecommerce advice. It targets a gap every Amazon operator hits: the model knows roughly how Sponsored Products works, but not your break-even ACOS, your placement waste, or which fee rule changed this quarter. Each skill is a SKILL.md with an input checklist, a decision tree, an output contract, and a small script where a calculation is involved. It is MIT licensed, and you do not need a signup or an API key. The 602 split by where the knowledge came from: 38 skills from Amazon's authorized training material, 211 from Douyin, 108 from WeChat, 74 from Bilibili, 49 from YouTube, 9 from Xiaohongshu, plus 12 public-research topics and 101 app capabilities grouped as Athena, Hermes and Apollo. Provenance survives the distillation. The ACOS diagnostics skill names its source deck, indexes all 42 pages, cites the benchmark whitepaper behind its numbers, and grades every claim by evidence level, from account actuals through official baseline down to estimate. That paper trail is unusual, and it is the main reason I trust this pack more than the average prompt dump. Day to day it behaves like an analyst with rules. Feed the ACOS skill a marketplace, a date range and a goal, and it asks for impressions, clicks, spend, orders and ad sales, recomputes CTR, CPC, CVR, AOV, ACOS, ROAS and TACOS with scripts/acos_diagnose.py instead of trusting the console's derived columns, walks a diagnostic tree for the driver that broke, and returns a diagnosis, the gaps in your data, and one single-variable experiment. It opens in read-only mode. Bids, budgets, placements, targets and negations each need per-object human approval, and the fourth mode exists only to run one approved change and read it back. Listing, keyword, product research, inventory and FBA skills follow the same shape. Setup is a git clone and a copy of the skill folder into your agent's skills directory, and you keep references/, agents/ and scripts/ or the skill loses its evidence files. Claude Code, Codex and Cursor all work, each skill ships an agents/openai.yaml card for OpenAI-compatible clients, and you do not need credentials. A few skills expect SellerSprite or SIF exports if you want the numbers they ask for. Two limits decide whether this is for you. Everything is written in Chinese, including trigger phrases and prompt examples, so an English-only operator is running the pack through their model's translation, and output quality varies with how well it handles that. The repo is also very young: created August 21, 2026, 15 commits, no tags, no releases, so pin a commit instead of tracking main. And 602 overstates the breadth. The same Amazon task often appears once per source platform, so expect near-duplicates between the Douyin and WeChat sets and cherry-pick rather than install everything. Anything about fees, policy or new ad features deserves a check in Seller Central, because the underlying source is social content and public training material, not an official changelog. The closest thing in this directory is Aaron Marketing Skills, also free, also a large multi-discipline pack. Aaron goes for marketing breadth in English with auditor gates and assumes you market a product wherever you sell it. Sealeap goes the other way: one platform, far deeper operational detail, and a Chinese-speaking seller as the assumed reader. If your revenue runs through Amazon FBA and someone on the team reads Chinese, this is the most specific free kit I have found. For Shopify, Meta ads or B2B content it adds nothing; look at Aaron or Claude Ads instead.

## AI Capabilities

- 602 skills: Amazon official material (38), Douyin (211), WeChat (108), Bilibili (74), YouTube (49), Xiaohongshu (9), public research (12), app capability sets (101)
- ACOS diagnostics with four modes (DIAGNOSE, DRAFT, RELEASE_PREP, APPROVED_WRITE) and read-only defaults
- Bundled Python scripts recompute CTR, CPC, CVR, AOV, ACOS, ROAS and TACOS from raw figures
- Evidence grading per skill, from account actuals to estimates, with source file and page provenance
- Listing, keyword, product research, inventory, FBA, brand registry and Amazon Ads workflows
- Per-skill agents/openai.yaml interface cards for OpenAI-compatible clients
## Key Integrations

- Claude Code
- Codex
- Cursor
- OpenAI-compatible agents
- SellerSprite (optional data)
- SIF (optional data)
## Pricing

SeaLeap Amazon Skills is free to self-host under the MIT licence.

All 602 skills are free under MIT; no signup needed. Sealeap's optional community membership is 69 CNY/year during the current promo (199 CNY regular) and adds member resources and community access, not the public repo.

Current plans and limits live on the [SeaLeap Amazon Skills pricing page](https://sealeap.cn/pricing).

## Best for

Amazon FBA sellers and agencies whose team reads Chinese and already runs Claude Code, Codex or Cursor for operator work.

## Not for

English-only teams, sellers who need vendor support or versioned releases, and anyone expecting turnkey campaign execution: the skills diagnose and draft, and they will not touch a live campaign without explicit approval.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Cloned the repo and read the ACOS diagnostics skill end to end. It is a real workflow, not a prompt: a mode declaration, a data contract, a diagnostic tree, a Python script that recomputes the metrics, and an output contract that requires naming evidence gaps. The source-and-guardrails file indexes the 42-page course deck it was distilled from and grades claims by evidence level.

The rest of the repo is breadth by source platform, which is both the draw and the trap. The Douyin and WeChat collections carry near-duplicate versions of the same Amazon task, so a 602-skill install is worse than a curated 20. Treat it as a library to search, not a stack to install.

## Verdict

The most specific free Amazon skill pack available, provided you or your ops lead reads Chinese and you pin a commit. Everyone else should look at an English-language pack.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Young project (332 GitHub stars) - smaller community and plugin ecosystem |
| ✓ AI capabilities: 602 skills: Amazon official material (38), Douyin (211), WeChat (108), Bilibili (74), YouTube (49), Xiaohongshu (9), public research (12), app capability sets (101) |  |
| ✓ Native integrations include Claude Code, Codex, Cursor (6 listed) |  |

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is SeaLeap Amazon Skills?**
SeaLeap Amazon Skills: 602 free Amazon seller skills for Claude Code: research, listings, ads, inventory. SeaLeap Amazon Skills ships with 602 skills: Amazon official material (38), Douyin (211), WeChat (108), Bilibili (74), YouTube (49), Xiaohongshu (9), public research (12), app capability sets (101). The public repository carries 332 stars.

**How much does SeaLeap Amazon Skills cost?**
SeaLeap Amazon Skills is open source - MIT licensed and free to self-host; the public repository carries 332 stars; native integrations cover Claude Code, Codex, Cursor. You pay in server time and maintenance, not licences.

**Is SeaLeap Amazon Skills a good self-hosted Agent Skills tool in 2026?**
The most specific free Amazon skill pack available, provided you or your ops lead reads Chinese and you pin a commit. Everyone else should look at an English-language pack.

## Similar tools

- [Marketing Skills (coreyhaines31)](/tools/marketingskills/): ~50 marketing skills for Claude Code, Codex, and Cursor by Corey Haines
- [Codex SEO](/tools/codex-seo/): Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations
- [Growth Lab](/tools/growth-lab/): Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex
- [AI Business Skills](/tools/ai-business-skills/): 63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents
## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Where open-source martech momentum actually lives](/blog/oss-momentum-tracker-september-2026/)
- [Salesforce's third no-code promise, audited](/blog/salesforce-third-no-code-promise/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 332
- **Founded:** 2026
- **HQ:** China
- **API:** No
- **Repository checked:** 2026-10-28
- **Page updated:** 2026-10-26

## Get the next teardown

One email when a new tool review lands, nothing else.

Send me the weekly newsletter. Unsubscribe any time.

[More Agent Skills Tools →](/categories/agent-skills/)
