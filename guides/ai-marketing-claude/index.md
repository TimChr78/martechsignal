# AI Marketing Suite pricing


| Pros | Cons |
| --- | --- |
| &#10003; MIT licence with free self-hosting | &#10007; Short native integration list - plan for API work |
| &#10003; AI capabilities: 15 marketing skills with 5 parallel subagents |  |
| &#10003; Active public repository (2,628 GitHub stars counted at last check) |  |

**What is AI Marketing Suite?**
AI Marketing Suite: 15-skill marketing suite for Claude Code with parallel agents and PDF reports. AI Marketing Suite ships with 15 marketing skills with 5 parallel subagents. The public repository carries 2,628 stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does AI Marketing Suite cost?**
AI Marketing Suite is open source - MIT licensed and free to self-host; the public repository carries 2,628 stars. You pay in server time and maintenance, not licences.

**Is AI Marketing Suite a good self-hosted Agent Skills tool in 2026?**
Best as a proposal-generation engine for agencies selling audits. For steady content work, the writing skills are the lasting value.

- **Founded:** 2025
- **Licence:** MIT
- **Public API:** no
- **Catalogued integrations:** 1
- **GitHub stars:** 2,628

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 2628
- **Founded:** 2025
- **API:** No
- **Last verified:** 2026-09-28

**Verdict:** AI Marketing Suite is a tool in Agent Skills with free and open source. The catalog documents 5 AI features, 1 integrations and a self-hosting path. We reviewed it from vendor documentation on 2026-09-28. This is a desk review, not a hands-on test. Desk-reviewed

Claude SEO

Open-source SEO skill for Claude Code with 25 sub-skills and 20 specialist agents

Aaron Marketing Skills

120 marketing skills across 7 disciplines for Claude Code with auditor gates

AI Business Skills

63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents

SEO Skill Bench

Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Guides](/guides/)
- [Agent Skills](/categories/agent-skills/)
- AI Marketing Suite
KIND: Guide (not an end-to-end platform)

## AI Marketing Suite review (2026): pricing, AI features, verdict

15-skill marketing suite for Claude Code with parallel agents and PDF reports

Agent Skills · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-28

[Visit AI Marketing Suite &#8594;](https://github.com/zubair-trabzada/ai-marketing-claude)

[How we review](/methodology/) · No affiliate links

[Visit AI Marketing Suite &#8594;](https://github.com/zubair-trabzada/ai-marketing-claude)

## Catalog facts: AI Marketing Suite

Not yet scored against the rubric, so no verdict here. This is everything the catalog holds on the tool, verified against vendor sources.

The full rubric is on the [methodology page](/methodology/).

## Overview

AI Marketing Suite is a 15-skill pack for Claude Code aimed at solopreneurs and agency builders who want to sell marketing services. You type /market audit https://example.com and five parallel agents analyze content and messaging, conversion optimization, SEO and discoverability, competitive positioning, and brand trust. Each gets a 0-100 score. The whole thing takes a couple of minutes and outputs a structured Markdown report. Add pip install reportlab and you get a client-ready PDF. The 15 commands cover the freelance marketing toolkit: /market copy generates optimized copy with before/after examples, /market emails builds complete email sequences, /market social produces a 30-day content calendar, /market ads writes ad creative for all platforms, /market funnel analyzes conversion paths, /market competitors runs competitive intelligence, /market landing does CRO analysis, /market launch builds a product launch playbook, and /market proposal generates client proposals. It&#x27;s built for the person who just landed a marketing client and needs to deliver an audit by Friday. Setup is a one-line curl install or a git clone. The architecture is straightforward: one orchestrator SKILL.md routes commands to 14 sub-skills, and 5 parallel subagents handle the audit dimensions. No external dependencies beyond Claude Code itself, unless you want PDF output. The limitation is depth. Fifteen skills is a survey, not a specialization. The SEO audit won&#x27;t match Claude SEO&#x27;s 25 sub-skills and 18 agents. The ad copy won&#x27;t match Claude Ads&#x27; 250+ platform-specific checks. But for a generalist who needs to audit a website, write some copy, build an email sequence, and hand over a PDF report, this does the job in one install. The repo was last pushed in March 2026, so it&#x27;s not as actively maintained as some alternatives. The author also ships companion packs for ads (ai-ads-claude) and sales (ai-sales-team-claude) if you want to go deeper on those verticals.

AI Marketing Suite homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- 15 marketing skills with 5 parallel subagents
- Full website marketing audit with 0-100 scoring
- AI copywriting with before/after examples
- Email sequence and content calendar generation
- Client-ready PDF report generation
## Key Integrations

- Claude Code
## Pricing

AI Marketing Suite is free to self-host under the MIT licence.

Free. Optional pip install reportlab for PDF output. Claude API costs apply.

## Requirements

Claude Code and a model with room for parallel subagents in one session. PDF output needs the optional reportlab install. The pack is MIT-licensed and free; API usage is billed by your provider.

## Best for

Freelancers and small agencies selling paid audits who want a repeatable first draft, and solo operators who want research and copy to share one context.

## Not for

Larger teams with existing audit tooling. Five fixed rubrics are a starting point, and an established practice will want to tune them before anything reaches a client.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Type /market audit with a URL and five parallel agents score content, conversion optimization, SEO and discoverability, competitive positioning, and brand trust, each out of 100, and return a structured report in minutes. Add reportlab and the same run produces a client-ready PDF. For freelancers and small agencies this compresses a paid audit into an afternoon, and the consistency is repeatable across prospects. The pack ships 15 commands, with /market copy earning its keep daily.

The caveat: the 0-100 scores are heuristics from the agents, not measured benchmarks, so the report needs a human read before it goes to a prospect. Output quality tracks whatever model you run, and brand-specific nuance still requires edits. It is open-source, so you can tighten the scoring prompts to your own methodology. Audit outputs win clients, but a steady feed of on-brand copy is what keeps them.

The parallel-agent design is the interesting engineering choice here. Five specialists scoring one site in a single pass keeps the audit internally consistent, because each agent reads the same snapshot instead of five separate crawls taken days apart. It also caps the ceiling: the scores are only as sharp as the five rubrics behind them, and those ship as editable prompts rather than tuned models.

The writing side is quieter than the audit but steadier. /market copy and its sibling commands generate campaign drafts from the same model context the audit established, so the research does not have to be retyped into every prompt. For a solo operator that continuity is most of the value. The 15 commands cover the recurring marketing chores rather than one hero workflow.

The PDF path deserves one line. Add reportlab and the same run emits a document a client can forward internally, which changes who the output is for: a chat log is for you, a PDF is for the buying committee. For freelancers who sell audits, that packaging step is often the difference between a tool and an offer.

Being MIT-licensed means the rubrics are editable. When the 0-100 audit scores drift from what you would actually tell a client, the fix is a prompt edit rather than a support ticket. Keep a copy of your edits when the pack updates so your methodology survives upstream changes.

One honest limit before adopting it for client work. The audit scores come from prompt rubrics, and two runs on an unchanged site can land a few points apart. Present the output as an assessment with stated criteria rather than a measurement, and the variance stops being a credibility problem. The report is strongest where it names specific pages and quotes specifics, which is exactly the part worth keeping after your own read.

The five audit pillars map cleanly onto what prospects ask for in an initial call: content, conversion optimization, SEO and discoverability, competitive positioning, and brand trust. That mapping is the pitch&#x27;s quiet strength. The report answers the questions a buyer already has, in the order they ask them, which is why the output converts better than a generic technical audit nobody requested.

On the 0-100 scale, the honest framing is calibration, not measurement. The scores rank pages against each other and track movement over time more reliably than they compare two different sites. Use them to show a before-and-after and to prioritize which section to fix first. Presenting a 71 as an objective grade invites an argument the number cannot win.

A sensible first week is small by design. Run the audit on your own site, read every line of the report once, and rewrite the two sections you disagree with. That pass teaches you the rubrics faster than any documentation, and the site you know best is the one where you will spot soft judgment immediately. Client work comes after that read.

Running costs stay low by design. The pack is MIT-licensed with no seat fees, reportlab is optional and free, and the only recurring bill is model usage at your provider&#x27;s rates. A full five-agent audit is one of the heavier runs in the suite, so price it like a research call rather than a keystroke. Against a day of manual review, most solo operators find that an easy trade.

The clearest signal after a month is whether the reports survive your own edits untouched. Forwarding output to a prospect with light changes means the suite is earning its place. When every section needs rewriting, the rubrics want the prompt-level tune-up the license allows.

## Verdict

Best as a proposal-generation engine for agencies selling audits. For steady content work, the writing skills are the lasting value.

## Pros and cons

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

AI Marketing Suite: 15-skill marketing suite for Claude Code with parallel agents and PDF reports. AI Marketing Suite ships with 15 marketing skills with 5 parallel subagents. The public repository carries 2,628 stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

AI Marketing Suite is open source - MIT licensed and free to self-host; the public repository carries 2,628 stars. You pay in server time and maintenance, not licences.

Best as a proposal-generation engine for agencies selling audits. For steady content work, the writing skills are the lasting value.

## Similar Tools

## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [OpenAI Isn't Building Ads. It's Building Agents That Spend Money Without You.](/blog/openai-agent-ads-spending-without-you/)
- [Check outputs, not logs: the silent-failure audit](/blog/silent-failure-audit/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/guides/ai-marketing-claude/#app",
    "name": "AI Marketing Suite",
    "description": "15-skill marketing suite for Claude Code with parallel agents and PDF reports",
    "image": "https://martechsignal.com/og/tools/ai-marketing-claude.png",
    "url": "https://martechsignal.com/guides/ai-marketing-claude/",
    "sameAs": [
      "https://github.com/zubair-trabzada/ai-marketing-claude"
    ],
    "mainEntityOfPage": "https://martechsignal.com/guides/ai-marketing-claude/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-28",
    "datePublished": "2026-07-31",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://github.com/zubair-trabzada/ai-marketing-claude",
      "priceValidUntil": "2026-12-31"
    }
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://martechsignal.com/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Tools",
        "item": "https://martechsignal.com/tools/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Agent Skills",
        "item": "https://martechsignal.com/categories/agent-skills/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "AI Marketing Suite",
        "item": "https://martechsignal.com/guides/ai-marketing-claude/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is AI Marketing Suite?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "AI Marketing Suite: 15-skill marketing suite for Claude Code with parallel agents and PDF reports. AI Marketing Suite ships with 15 marketing skills with 5 parallel subagents. The public repository carries 2,628 stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does AI Marketing Suite cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "AI Marketing Suite is open source - MIT licensed and free to self-host; the public repository carries 2,628 stars. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is AI Marketing Suite a good self-hosted Agent Skills tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Best as a proposal-generation engine for agencies selling audits. For steady content work, the writing skills are the lasting value."
        }
      }
    ]
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
