# Codex SEO review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Codex SEO
Re-check pending: pricing last verified 2026-08-28 (39 days ago).

## Codex SEO review (2026): pricing, AI features, verdict

Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations

Agent Skills · Free Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Codex SEO →](https://github.com/AgriciDaniel/codex-seo)

[How we review](/methodology/) · No affiliate links

**Verdict:** Codex SEO is a tool in Agent Skills with a free tier. The catalog documents 5 AI features, 5 integrations and a public API. We reviewed it from vendor documentation on 2026-08-28. This is a desk review, not a hands-on test. Desk-reviewed

[Visit Codex SEO →](https://github.com/AgriciDaniel/codex-seo)

## MartechSignal Score: 34/60

Codex SEO is a serious free skill suite: 26 workflows, 24 agent profiles and real API integrations. The proprietary courtesy licence means free today and unknowable later.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 7/10 | Free to use with API costs for DataForSEO, Gemini, Google and Firecrawl stated as the run cost (the vendor pricing page: [vendor site](https://github.com/AgriciDaniel/codex-seo), verified 2026-08-28). |
| Feature depth | 6/10 | 26 SEO workflows with 24 TOML agent profiles and GEO/AEO optimization cover the agent-SEO surface (vendor documentation: [vendor site](https://github.com/AgriciDaniel/codex-seo), verified 2026-09-28). |
| Integrations | 7/10 | DataForSEO, Google Search Console, Firecrawl and Gemini documented plus Codex as the harness (vendor documentation: [vendor site](https://github.com/AgriciDaniel/codex-seo), verified 2026-09-28). |
| AI capability | 6/10 | GEO/AEO optimization workflows with agent profiles make it agent-native SEO tooling (vendor documentation: [vendor site](https://github.com/AgriciDaniel/codex-seo), verified 2026-09-28). |
| Openness | 4/10 | Free and source-visible but under a proprietary courtesy licence, not OSS (the source repository: [repository](https://github.com/AgriciDaniel/codex-seo), verified 2026-09-28). |
| Operational maturity | 4/10 | Founded 2025 under a solo author's licence (vendor documentation: [vendor site](https://github.com/AgriciDaniel/codex-seo), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Codex SEO is the OpenAI Codex port of Claude SEO, built by the same author (AgriciDaniel). It covers the same SEO surface: technical audits, on-page analysis, E-E-A-T content quality, schema markup, Core Web Vitals, GEO/AEO for AI search, backlinks, local SEO, ecommerce SEO, hreflang, and semantic clustering. The difference is the runtime. Instead of Claude Code's subagent model, Codex SEO uses 24 TOML agent profiles, deterministic headless runners, and a Python virtualenv at ~/.codex/skills/seo/.venv/. If your team runs Codex instead of Claude Code, this is the same workflow adapted to your platform. The integration surface is wider than Claude SEO's. Codex SEO connects to DataForSEO for keyword and SERP data, Google Search Console for performance metrics, Firecrawl for page crawling, and Gemini for image analysis workflows. The headless runners mean you can script audits in CI or run them on a schedule without an interactive terminal. 52 tests pass, and the installer handles dependency setup, capability groups, and runtime verification. Installation is a one-line curl (or PowerShell on Windows). The installer copies skills into ~/.codex/skills/, agents into ~/.codex/agents/, creates the virtualenv, and installs dependencies. Current release is v1.9.6-codex.5, synchronized to Claude SEO upstream at commit a9cf338. If you're choosing between this and Claude SEO, the decision is simple: use whichever matches your agent platform. The SEO methodology is the same. Codex SEO adds the DataForSEO and Firecrawl integrations that Claude SEO handles through its own extension system. For teams already paying for OpenAI's Codex, this avoids the cost of switching to Claude Code just for SEO audits. The star count (534) is lower than Claude SEO's 12,873, which reflects the smaller Codex user base, not a quality gap.

Codex SEO homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- 26 SEO workflows with 24 TOML agent profiles
- DataForSEO, Gemini, Google API, and Firecrawl integrations
- GEO/AEO optimization for AI search
- Core Web Vitals and technical SEO audits
- Deterministic headless runners for repeatable execution
## Key Integrations

- OpenAI Codex
- DataForSEO
- Google Search Console
- Firecrawl
- Gemini
## Pricing

Codex SEO is free to use.

Free to use. The bundled licence is proprietary (courtesy of the author) - not an OSS licence.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Codex SEO is the OpenAI Codex port of Claude SEO from the same author, covering the full surface: technical audits, on-page analysis, E-E-A-T content checks, schema, Core Web Vitals, GEO and AEO for AI search, backlinks, local and ecommerce SEO, hreflang, and semantic clustering. The difference is the runtime: 24 TOML agent profiles, deterministic headless runners, and a Python virtualenv under ~/.codex instead of Claude's subagent model.

Everything depends on your team's stack. If you run Codex, you get the same workflows Claude shops enjoy, 26 of them across the suite and hundreds of stars and climbing. If you run Claude Code, stay with the original. Setup is developer work: venv management, agent config, and no UI or support when things break. The output ceiling is whatever model you point at it.

## Verdict

The right SEO skill pack for Codex-based teams. Claude Code users should stick with the original Claude SEO.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ AI capabilities: 26 SEO workflows with 24 TOML agent profiles | ✗ Closed source - no self-hosting option |
| ✓ Native integrations include OpenAI Codex, DataForSEO, Google Search Console (5 listed) |  |
| ✓ Free tier to evaluate before committing (Free to use. The bundled licence is proprietary (courtesy of the author) - not an OSS licence) |  |

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Codex SEO?**
Codex SEO: Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations. Codex SEO ships with 26 SEO workflows with 24 TOML agent profiles. The public repository carries 777 stars.

**How much does Codex SEO cost?**
Codex SEO has a free tier, so you can run a real evaluation before paying. Free to use. The bundled licence is proprietary (courtesy of the author) - not an OSS licence. We last checked the plan structure on 2026-08-28; paid tiers mainly raise limits rather than unlocking core features.

**What does running Codex SEO actually cost?**
The right SEO skill pack for Codex-based teams. Claude Code users should stick with the original Claude SEO.

## Similar Tools

- [Claude SEO](/tools/claude-seo/): Open-source SEO skill for Claude Code with 25 sub-skills and 20 specialist agents
- [AI Business Skills](/tools/ai-business-skills/): 63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents
- [Digital Marketing Pro](/tools/digital-marketing-pro/): 163-skill AI marketing plugin for agencies with EU AI Act compliance
- [Growth Lab](/tools/growth-lab/): Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex
- [Open Mercato](/tools/open-mercato/): Open-source TypeScript foundation for AI-built commerce, CRM, and ERP
## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Microsoft Just Removed the Steering Wheel From Search Ads](/blog/microsoft-search-ads-steering-wheel/)
- [Your agent protocol matters less than your data plumbing](/blog/agent-protocol-vs-data-plumbing/)
## Also featured in

- [Best AI SEO tools (2026): 8 compared](/best/ai-seo-tools/) — Best for Codex CLI users who want scripted SEO workflows.
### Quick Facts

- **Pricing:** Free
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 777
- **Founded:** 2025
- **API:** Yes
- **Repository checked:** 2026-10-05
- **Page updated:** 2026-08-28

Related guides: [Ai Seo Tools](/best/ai-seo-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
