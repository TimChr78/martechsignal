# SEO Skill Bench review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | Free under MIT with leaderboard runs costing $1.70 to $4.46 in LLM tokens each, published as exact figures (the vendor pricing page: [pricing page](https://seoagent.com/seo-skill-benchmark), verified 2026-09-28). |
| Feature depth | 4/10 | Headless skill execution, answer-key scoring and hallucination trap detection cover benchmarking narrowly (vendor documentation: [vendor site](https://seoagent.com/seo-skill-benchmark), verified 2026-09-28). |
| Integrations | 2/10 | Claude Code is the only documented harness (vendor documentation: [vendor site](https://seoagent.com/seo-skill-benchmark), verified 2026-09-28). |
| AI capability | 5/10 | Deterministic planted-defect scoring and trap avoidance measurement are meta-evaluation of AI output (vendor documentation: [vendor site](https://seoagent.com/seo-skill-benchmark), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with 51 GitHub stars and fully local execution (the source repository: [repository](aleclindz/seo-skill-bench), verified 2026-09-28). |
| Operational maturity | 2/10 | 51 stars as a young benchmark project with no API (vendor documentation: [vendor site](https://seoagent.com/seo-skill-benchmark), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Young project (51 GitHub stars) - smaller community and plugin ecosystem |
| ✓ AI capabilities: headless execution of Claude Code SEO skills | ✗ Short native integration list - plan for API work |
| ✓ Native integrations include Claude Code (1 listed) |  |

**What is SEO Skill Bench?**
SEO Skill Bench: Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects. SEO Skill Bench ships with headless execution of Claude Code SEO skills. The public repository carries 51 stars. MartechSignal's review covers features, pricing, and how it compares to alternatives.

**How much does SEO Skill Bench cost?**
SEO Skill Bench is open source - MIT licensed and free to self-host; the public repository carries 51 stars. You pay in server time and maintenance, not licences.

**Is SEO Skill Bench a good self-hosted Agent Skills tool in 2026?**
Strengths include 51 GitHub stars, MIT licensing with free self-hosting. The full review breaks down where it fits in a modern martech stack.

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 51
- **API:** No
- **Last verified:** 2026-09-03

**Verdict:** SEO Skill Bench is a tool in Agent Skills with free and open source. The catalog documents 5 AI features, 1 integrations and a self-hosting path. We reviewed it from vendor documentation on 2026-09-03. This is a desk review, not a hands-on test. Desk-reviewed

Zapier GTM Cheat Codes

Zapier's installable coding-agent skills for GTM: campaign planning, CRM context, customer proof

Aaron Marketing Skills

120 marketing skills across 7 disciplines for Claude Code with auditor gates

AI Business Skills

63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents

Codex SEO

Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations

Claude Ads

Paid-media operations skill for Claude Code covering 12 ad platforms

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- SEO Skill Bench
Re-check pending: pricing last verified 2026-09-03 (26 days ago).

## SEO Skill Bench review (2026): pricing, AI features, verdict

Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects

Agent Skills · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-03

[Visit SEO Skill Bench →](https://seoagent.com/seo-skill-benchmark)

[How we review](/methodology/) · No affiliate links

[Visit SEO Skill Bench →](https://seoagent.com/seo-skill-benchmark)

## MartechSignal Score: 31/60

SEO Skill Bench scores Claude Code SEO skills against fixture sites with planted defects and hallucination traps. MIT, and each leaderboard run costs $1.70 to $4.46 in tokens, stated to the cent.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

SEO Skill Bench answers the question every Claude Code SEO skill README can't: does the thing actually work once installed? It is an open benchmark that runs SEO skills for Claude Code and other coding agents against fixture websites with deliberately planted defects, then scores what they find. If you are choosing an SEO skill for your agent workflow, this is the closest thing to a published answer key. The harness installs each entrant in a real headless Claude Code session (claude -p), not a simulation reconstructed from its README, and points it at the pivot-saas fixture site. Scoring follows a pre-registered 100-point rubric: 40 points for detecting planted defects, 25 for avoiding traps, meaning the skill never recommends fixing something that is already fine, 25 for blind-judged judgment calls, and 10 for execution. Scores are medians across runs. On the August 2026 board, SEOAgent led at 84.9 while the vanilla baseline with no skill scored 73.0. That spread tells you two things: skills can add real value, and some entrants score below doing nothing at all. Setup needs Node and a Claude Code install. You run node harness/run.mjs with a skill id and fixture, then the score and judge scripts, and entrants register with a one-line entry in skills.json. The leaderboard also publishes what each skill costs, kept outside the composite on purpose: resident tokens the skill occupies in every system prompt, per-run cost, and median time. Runs on the board cost between $1.70 and $4.46 and took 405 to 779 seconds. Heavy skills like Corey Haines' Marketing Skills carry 8,770 resident tokens, which dilutes every other skill you have installed. The big caveat is the maintainer's conflict of interest. SEOAgent, the company behind the benchmark, also ships the top-ranked entrant. The structural mitigations are real: published fixtures, deterministic answer keys, a frozen rubric, blind judging, and a harness anyone can re-run. Still, treat the leaderboard as a strong signal rather than gospel. The benchmark only measures technical on-site audit work against one fixture. It says nothing about content strategy, links, or your actual site. At about 50 stars the community is small, and the repo's value is its method more than its momentum. Compared to picking a skill by GitHub stars or vibes, this is the most concrete public way to see detection rates and hallucination traps side by side. If you are building an agent-driven SEO workflow, run your candidate skill through this harness before you point it at a production site.

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

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

SEO Skill Bench: Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects. SEO Skill Bench ships with headless execution of Claude Code SEO skills. The public repository carries 51 stars. MartechSignal's review covers features, pricing, and how it compares to alternatives.

SEO Skill Bench is open source - MIT licensed and free to self-host; the public repository carries 51 stars. You pay in server time and maintenance, not licences.

Strengths include 51 GitHub stars, MIT licensing with free self-hosting. The full review breaks down where it fits in a modern martech stack.

## Similar Tools

## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [AI watermarks are now part of your agent's risk surface](/blog/watermark-provenance-tax-agents/)
- [Why Your Marketing Stack Doesn't Need Another AI Tool](/blog/why-your-marketing-automation-stack-doesnt-need-another-ai-tool/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/seo-skill-bench/#app",
    "name": "SEO Skill Bench",
    "description": "Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects",
    "image": "https://martechsignal.com/og/tools/seo-skill-bench.png",
    "url": "https://martechsignal.com/tools/seo-skill-bench/",
    "sameAs": [
      "https://seoagent.com/seo-skill-benchmark"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/seo-skill-bench/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-14",
    "datePublished": "2026-09-03"
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
        "name": "SEO Skill Bench",
        "item": "https://martechsignal.com/tools/seo-skill-bench/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is SEO Skill Bench?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "SEO Skill Bench: Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects. SEO Skill Bench ships with headless execution of Claude Code SEO skills. The public repository carries 51 stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does SEO Skill Bench cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "SEO Skill Bench is open source - MIT licensed and free to self-host; the public repository carries 51 stars. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is SEO Skill Bench a good self-hosted Agent Skills tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Strengths include 51 GitHub stars, MIT licensing with free self-hosting. The full review breaks down where it fits in a modern martech stack."
        }
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "Review",
    "author": {
      "@type": "Person",
      "name": "Tim Christensen",
      "url": "https://martechsignal.com/authors/tim-christensen/",
      "@id": "https://martechsignal.com/authors/tim-christensen/#person"
    },
    "publisher": {
      "@type": "Organization",
      "@id": "https://martechsignal.com/#organization",
      "name": "MartechSignal"
    },
    "datePublished": "2026-09-26",
    "reviewBody": "SEO Skill Bench scores Claude Code SEO skills against fixture sites with planted defects and hallucination traps. MIT, and each leaderboard run costs $1.70 to $4.46 in tokens, stated to the cent.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/seo-skill-bench/#app",
      "name": "SEO Skill Bench",
      "url": "https://martechsignal.com/tools/seo-skill-bench/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 31,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
