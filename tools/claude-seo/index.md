# Claude SEO review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 7/10 | The skill is free and MIT-licensed with no paid tier, and the tool page documents the real usage cost of roughly 6 USD in API tokens per full audit, while the optional paid Skool mirror has no published price in our sources (the vendor pricing page). |
| Feature depth | 8/10 | 25 sub-skills, 18 specialist agents, 30 commands and 439 passing tests at v2.2.5 go past the skill-pack baseline with citability scoring, dependency tracking and explicit failure checks as differentiators (vendor documentation). |
| Integrations | 3/10 | Five named integrations cover the surface: Claude Code, Google Search Console, DataForSEO, Firecrawl and Lighthouse, with no marketplace behind them (vendor documentation). |
| AI capability | 9/10 | The product is itself an agent harness: /seo audit coordinates its specialist agents across 25 sub-skills inside Claude Code (vendor documentation). |
| Openness | 10/10 | MIT-licensed with the whole audit stack inspectable and no paid tier hiding functionality (the source repository). |
| Operational maturity | 6/10 | Founded in February 2026 with 17,737 GitHub stars, 2,599 forks (verified 2026-09-26) and active v2.2.x releases in August 2026, but it remains a young project with no company or SLAs behind it (vendor documentation). |


| Grader | Date | Score | Context |
| --- | --- | --- | --- |
| v2.2.4 | 2026-08-23 | **83**/100 | First audit, 169 pages |
| v2.2.4 | 2026-08-24 | **92**/100 | After fixing round-1 findings |
| v2.2.4 | 2026-08-25 | **96**/100 | Zero critical and high findings |
| v2.2.5 | 2026-08-26 | **61**/100 | Same site, stricter grader |
| v2.2.5 | 2026-08-27 | **66**/100 | First remediation wave |
| v2.2.5 | 2026-08-27 | **72**/100 | Remediation waves 2 and 3 |
| v2.2.5 | 2026-08-27 | **74.6**/100 | All 115 tool pages differentiated |


| Pros | Cons |
| --- | --- |
| &#10003; MIT licence with free self-hosting | &#10007; Runs inside Claude Code, so a paid Anthropic subscription is part of the real cost |
| &#10003; AI capabilities: 25 parallel sub-skills for technical SEO, E-E-A-T, schema, GEO/AEO | &#10007; Grader strictness shifts between versions, so scores are not comparable across releases |
| &#10003; Active public repository (16,675 GitHub stars counted at last check) | &#10007; Multi-site config needs manual .env work and API keys for DataForSEO and Firecrawl |
| &#10003; Native integrations include Claude Code, Google Search Console, DataForSEO (5 listed) |  |
| &#10003; MIT licensed with no paid tier, so the whole audit stack is inspectable |  |

**What is Claude SEO?**
Open-source SEO skill for Claude Code with 25 sub-skills and 20 specialist agents. It ships with 25 parallel sub-skills for technical SEO, E-E-A-T, schema, GEO/AEO, 16,675 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Claude SEO cost?**
Claude SEO is open source - MIT licensed and free to self-host; the public repository carries 16,675 stars; native integrations cover Claude Code, Google Search Console, DataForSEO. You pay in server time and maintenance, not licences.

**Is Claude SEO a good self-hosted Agent Skills tool in 2026?**
The most thorough free SEO audit you can run without leaving your terminal. Scores only mean something within one grader version, so pin the version and track deltas, not absolutes. It caught real bugs in our own production deploy pipeline on day one.

**Is Claude SEO the same as SEO tools for Claude?**
Yes. &#x27;Claude SEO&#x27; usually refers to this open-source skill that runs inside Claude Code. MartechSignal&#x27;s review covers what it audits and how it compares to hosted alternatives.

**How does a Claude SEO audit work?**
You run /seo audit with a URL. The skill coordinates its specialist agents that check technical SEO, content quality, schema, performance, and AI-search readiness, then returns a prioritized list of fixes.

**Is there a free Claude SEO checker?**
Yes, and it is the same project. Claude SEO is free and MIT-licensed; the checker is the /seo audit command inside Claude Code. We ran seven audits on two production sites in one week and scored up to 96/100 on the v2.2.4 grader.

**What is the Claude SEO tool?**
An open-source SEO analysis toolkit for Claude Code: 25 sub-skills and 20 agents that crawl your site and grade technical SEO, content, schema, and AI-search readiness. On our own sites it surfaced 96 findings in about five minutes.

**Can Claude Code do SEO audits?**
Yes. With the Claude SEO skill installed, you type /seo audit plus a URL. Claude Code coordinates specialist agents checking crawlability, structured data, content quality, and AI-answer citability, then returns a prioritized fix list.

**How much does a Claude SEO audit cost?**
The skill itself is free. Your only cost is Claude Code API tokens: our full-site audits on 90-to-170-page sites ran about five minutes and roughly six dollars each, far less than a consultant day rate or a month of SaaS audit tools.

**Is Claude SEO better than Screaming Frog?**
They overlap on technical checks but differ in output. Screaming Frog crawls fast and cheap for raw data; Claude SEO spends more tokens per run but returns prioritized findings with dependencies, verification checks, and AI-search citability scoring that crawlers don&#x27;t attempt.

**Are Claude SEO scores reliable?**
Within one version, yes: our score moved 61 to 66 to 72 to 74.6 as we fixed flagged issues, and every point tracked a real repair. Across versions, no: v2.2.4 scored the same site 96 that v2.2.5 scored 61. Pin the version before comparing runs.

**Does Claude SEO work as SEO analysis software?**
It runs as analysis software inside your terminal rather than a dashboard. Each audit crawls every URL, grades seven categories, and writes a full report with prioritized fixes. We published three complete reports from real runs on this site&#x27;s own domain.

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **Github Stars:** 17,737
- **Forks:** 2,443
- **Sub Skills:** 25
- **Agents:** 18
- **Commands:** 30

**Verdict:** Claude SEO is a tool in Agent Skills with free and open source. The catalog documents 5 AI features, 5 integrations, a public API and a self-hosting path. We ran this ourselves before reviewing it; the run notes and dates sit in Review notes below. Hands-on

Codex SEO

Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations

Claude Ads

Paid-media operations skill for Claude Code covering 12 ad platforms

Growth Lab

Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex

SEO Skill Bench

Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Claude SEO
## Claude SEO review (2026): pricing, AI features, verdict

Open-source SEO skill for Claude Code with 25 sub-skills and 20 specialist agents

Agent Skills · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-27

[Visit Claude SEO &#8594;](https://claude-seo.md/)

[How we review](/methodology/) · No affiliate links

[Visit Claude SEO &#8594;](https://claude-seo.md/)

## Benchmark log: 43/60

A deep, free SEO audit layer for Claude Code whose findings carry evidence, dependencies and verification checks. It needs the paid Claude Code runtime to run and grader scores shift between releases, so track deltas within one version rather than absolutes.

Scored 2026-09-26 against our published rubric: six pillars, 0-10 each. This is our own tool, scored from running it in our benchmark suite and four production audit cycles. Per our review policy we do not publish first-party self-ratings as Review markup, so this is a benchmark log, not a review rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Claude SEO turns Claude Code into an SEO audit machine. You type /seo audit and it spawns its specialist agents in parallel, each covering a different discipline: technical SEO, content quality, E-E-A-T signals, Schema.org markup, Core Web Vitals, local SEO, ecommerce SEO, international SEO, and AI search optimization (what Google calls GEO). A full-site audit that would take a consultant a full day finishes in minutes. The output is a prioritized action plan where every recommendation carries the observation it rests on, its dependencies, and an explicit &quot;how would we know this failed?&quot; check. That last part matters. Most SEO tools tell you what&#x27;s wrong. Claude SEO tells you what&#x27;s wrong, why it matters, and how you&#x27;d verify the fix worked. The AI-search angle is what separates this from a Screaming Frog crawl. Claude SEO scores your content for citability by AI answer engines: whether your pages have self-contained 134-167 word answer blocks, question-based heading hierarchy, and the structured data that makes LLMs cite you instead of your competitor. It checks for IPTC TrainedAlgorithmicMedia metadata on AI-generated images, llms.txt files, and agent-friendly page structure per web.dev guidance. If you&#x27;re optimizing for a world where Google&#x27;s AI Overviews and ChatGPT answers replace traditional blue links, this is the audit tool built for that reality. It&#x27;s free and MIT-licensed. The catch is you need Claude Code (Anthropic&#x27;s paid CLI/IDE product) to run it, so you&#x27;re paying for API tokens. A full audit on a 200-page site burns through a meaningful chunk of tokens. There&#x27;s also a private community mirror on Skool (AI Marketing Hub Pro) that gets early features, but the public repo is fully functional. Version 2.2.5 ships 439 passing tests, which is unusual rigor for a skill pack. Compared to doing this manually with Screaming Frog, Ahrefs, and a spreadsheet, Claude SEO collapses the workflow into one command. Compared to SaaS audit tools like Sitebulb or Lumar, it&#x27;s more flexible and cheaper, but you lose the polished dashboards and historical tracking. It&#x27;s best for SEO agencies running 5+ client sites who want weekly automated audits instead of quarterly manual ones, and for in-house SEO leads who want a second pair of eyes before executive reviews. If you don&#x27;t use Claude Code, look at Codex SEO, the same author&#x27;s port for OpenAI&#x27;s Codex.

Claude SEO homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- 25 parallel sub-skills for technical SEO, E-E-A-T, schema, GEO/AEO
- 20 specialist agents, concurrent by design
- AI search optimization (GEO) aligned with Google&#x27;s AI Optimization Guide
- Citability scoring for AI-answer engines
- Falsifiable recommendations with dependency tracking
## Key Integrations

- Claude Code
- Google Search Console
- DataForSEO
- Firecrawl
- Lighthouse
## Pricing

Claude SEO is free to self-host under the MIT licence.

Free, MIT-licensed. Self-hosted inside Claude Code. Optional paid community mirror on Skool.

## How to install

- Clone the repo: git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
- Run the installer: bash claude-seo/install.sh
- Open Claude Code and type /seo setup once, then /seo doctor to confirm
- Start an audit with /seo audit https://your-site.com
## Requirements

Python 3.10+ and Claude Code CLI. macOS, Linux, Windows (PowerShell installer available). Audits run locally; only Google API calls and optional providers leave your machine.

## Best for

Developers and SEO practitioners who want audit depth without a SaaS subscription, and teams already living in Claude Code who want SEO checks next to their code workflow.

## Not for

Marketers who want a dashboard, rank tracking history, or scheduled reports. Claude SEO produces point-in-time audits in your terminal; there is no UI and no storage beyond what you keep.

## Hosted vs. original

SE Ranking sells hosted Claude SEO skills as an add-on to its platform. The original project is free and runs entirely in your terminal; SE Ranking&#x27;s version trades independence for integration with its existing suite.

## Audit scores on our own sites

Second site check: **oresund.live** **68** (2026-08-23) → **87** (2026-08-25)

How we read scores: v2.2.4 and v2.2.5 are different graders. The 96 to 61 move in late August was a version change, not a site regression. Within v2.2.5, 61 to 74.6 in one day reflects real fixes to real findings.

## Review notes

Ownership disclosure: Claude SEO is a third-party MIT project by AgriciDaniel (github.com/AgriciDaniel/claude-seo). MartechSignal has no affiliation with its author. The results below come from running the tool on our own production sites, and our audit pipeline depends on it. For that reason this page is excluded from our Review structured data (the MartechSignal Score panel is the standard catalog panel, shown unedited).

We ran Claude SEO on our own production sites before writing this. On a 170-page marketing site it surfaced 96 findings in about five minutes; on a smaller transit-info site it flagged 87 findings across technical SEO, schema gaps, and citability issues like missing llms.txt. Both audits cost roughly six dollars of API tokens each.

Findings are graded High/Medium/Low with dependency tracking, which matters when several fixes interact: schema work depends on markup cleanup, citability fixes depend on heading hierarchy. Re-running after fixing confirmed the score moved from 68 to 87 on one site. That verify-the-fix loop is the part most audit tools skip.

The v2.2.5 release (August 2026) is a reliability and Google-currency pass: refreshed guidance through the August spam update, Preferred Sources, Search Console platform properties, and PageSpeed Insights Agentic Browsing, plus safer JSON-LD traversal and bounded Chromium accessibility-tree capture. Test count is up to 439. Nothing changed in the workflow, but the audit rules track Google&#x27;s current guidance.

## Verdict

The most thorough free SEO audit you can run without leaving your terminal. Scores only mean something within one grader version, so pin the version and track deltas, not absolutes. It caught real bugs in our own production deploy pipeline on day one.

## Pros and cons

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source SEO skill for Claude Code with 25 sub-skills and 20 specialist agents. It ships with 25 parallel sub-skills for technical SEO, E-E-A-T, schema, GEO/AEO, 16,675 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Claude SEO is open source - MIT licensed and free to self-host; the public repository carries 16,675 stars; native integrations cover Claude Code, Google Search Console, DataForSEO. You pay in server time and maintenance, not licences.

The most thorough free SEO audit you can run without leaving your terminal. Scores only mean something within one grader version, so pin the version and track deltas, not absolutes. It caught real bugs in our own production deploy pipeline on day one.

Yes. &#x27;Claude SEO&#x27; usually refers to this open-source skill that runs inside Claude Code. MartechSignal&#x27;s review covers what it audits and how it compares to hosted alternatives.

You run /seo audit with a URL. The skill coordinates its specialist agents that check technical SEO, content quality, schema, performance, and AI-search readiness, then returns a prioritized list of fixes.

Yes, and it is the same project. Claude SEO is free and MIT-licensed; the checker is the /seo audit command inside Claude Code. We ran seven audits on two production sites in one week and scored up to 96/100 on the v2.2.4 grader.

An open-source SEO analysis toolkit for Claude Code: 25 sub-skills and 20 agents that crawl your site and grade technical SEO, content, schema, and AI-search readiness. On our own sites it surfaced 96 findings in about five minutes.

Yes. With the Claude SEO skill installed, you type /seo audit plus a URL. Claude Code coordinates specialist agents checking crawlability, structured data, content quality, and AI-answer citability, then returns a prioritized fix list.

The skill itself is free. Your only cost is Claude Code API tokens: our full-site audits on 90-to-170-page sites ran about five minutes and roughly six dollars each, far less than a consultant day rate or a month of SaaS audit tools.

They overlap on technical checks but differ in output. Screaming Frog crawls fast and cheap for raw data; Claude SEO spends more tokens per run but returns prioritized findings with dependencies, verification checks, and AI-search citability scoring that crawlers don&#x27;t attempt.

Within one version, yes: our score moved 61 to 66 to 72 to 74.6 as we fixed flagged issues, and every point tracked a real repair. Across versions, no: v2.2.4 scored the same site 96 that v2.2.5 scored 61. Pin the version before comparing runs.

It runs as analysis software inside your terminal rather than a dashboard. Each audit crawls every URL, grades seven categories, and writes a full report with prioritized fixes. We published three complete reports from real runs on this site&#x27;s own domain.

## Similar Tools

## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Competitive-Intel Tools Were the First Martech Category AI Killed](/blog/ci-tools-were-the-first-martech-category-ai-killed/)
- [Fifty days of open-source MarTech, audited](/blog/oss-martech-50-day-checkin/)
### Quick Facts

### Project stats

### Our rating

★★★★☆

**4.5 / 5**The audits found real, verifiable issues on every run, which earns the high score. Scoring shifts between grader versions and is sometimes erratic, so not a 5. No paid placement, no affiliate link: the tool is free and open source.

Related guides: [Ai Seo Tools](/best/ai-seo-tools/) · [Open Source Marketing Tools](/best/open-source-marketing-tools/) · [Agent Skills Tools](/best/agent-skills-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/claude-seo/#app",
    "name": "Claude SEO",
    "description": "Open-source SEO skill for Claude Code with 25 sub-skills and 20 specialist agents",
    "image": "https://martechsignal.com/og/tools/claude-seo.png",
    "url": "https://martechsignal.com/tools/claude-seo/",
    "sameAs": [
      "https://claude-seo.md/"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/claude-seo/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-27",
    "datePublished": "2026-07-31",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://claude-seo.md/",
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
        "name": "Claude SEO",
        "item": "https://martechsignal.com/tools/claude-seo/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Claude SEO?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source SEO skill for Claude Code with 25 sub-skills and 20 specialist agents. It ships with 25 parallel sub-skills for technical SEO, E-E-A-T, schema, GEO/AEO, 16,675 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Claude SEO cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Claude SEO is open source - MIT licensed and free to self-host; the public repository carries 16,675 stars; native integrations cover Claude Code, Google Search Console, DataForSEO. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Claude SEO a good self-hosted Agent Skills tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The most thorough free SEO audit you can run without leaving your terminal. Scores only mean something within one grader version, so pin the version and track deltas, not absolutes. It caught real bugs in our own production deploy pipeline on day one."
        }
      },
      {
        "@type": "Question",
        "name": "Is Claude SEO the same as SEO tools for Claude?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. 'Claude SEO' usually refers to this open-source skill that runs inside Claude Code. MartechSignal's review covers what it audits and how it compares to hosted alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How does a Claude SEO audit work?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "You run /seo audit with a URL. The skill coordinates its specialist agents that check technical SEO, content quality, schema, performance, and AI-search readiness, then returns a prioritized list of fixes."
        }
      },
      {
        "@type": "Question",
        "name": "Is there a free Claude SEO checker?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, and it is the same project. Claude SEO is free and MIT-licensed; the checker is the /seo audit command inside Claude Code. We ran seven audits on two production sites in one week and scored up to 96/100 on the v2.2.4 grader."
        }
      },
      {
        "@type": "Question",
        "name": "What is the Claude SEO tool?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "An open-source SEO analysis toolkit for Claude Code: 25 sub-skills and 20 agents that crawl your site and grade technical SEO, content, schema, and AI-search readiness. On our own sites it surfaced 96 findings in about five minutes."
        }
      },
      {
        "@type": "Question",
        "name": "Can Claude Code do SEO audits?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. With the Claude SEO skill installed, you type /seo audit plus a URL. Claude Code coordinates specialist agents checking crawlability, structured data, content quality, and AI-answer citability, then returns a prioritized fix list."
        }
      },
      {
        "@type": "Question",
        "name": "How much does a Claude SEO audit cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The skill itself is free. Your only cost is Claude Code API tokens: our full-site audits on 90-to-170-page sites ran about five minutes and roughly six dollars each, far less than a consultant day rate or a month of SaaS audit tools."
        }
      },
      {
        "@type": "Question",
        "name": "Is Claude SEO better than Screaming Frog?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "They overlap on technical checks but differ in output. Screaming Frog crawls fast and cheap for raw data; Claude SEO spends more tokens per run but returns prioritized findings with dependencies, verification checks, and AI-search citability scoring that crawlers don't attempt."
        }
      },
      {
        "@type": "Question",
        "name": "Are Claude SEO scores reliable?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Within one version, yes: our score moved 61 to 66 to 72 to 74.6 as we fixed flagged issues, and every point tracked a real repair. Across versions, no: v2.2.4 scored the same site 96 that v2.2.5 scored 61. Pin the version before comparing runs."
        }
      },
      {
        "@type": "Question",
        "name": "Does Claude SEO work as SEO analysis software?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "It runs as analysis software inside your terminal rather than a dashboard. Each audit crawls every URL, grades seven categories, and writes a full report with prioritized fixes. We published three complete reports from real runs on this site's own domain."
        }
      }
    ]
  }
]
```
