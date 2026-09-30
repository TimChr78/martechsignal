# Growth Lab review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free under Apache 2.0 with Claude Code or Codex costs as the stated run expense (the vendor pricing page: [vendor site](https://growthlab.tsingyuai.com), verified 2026-08-28). |
| Feature depth | 5/10 | SEO page growth and Xiaohongshu loops cover two growth motions end to end (vendor documentation: [vendor site](https://growthlab.tsingyuai.com), verified 2026-09-28). |
| Integrations | 4/10 | Claude Code, Codex, IndexNow and Bing Webmaster Tools documented (vendor documentation: [vendor site](https://growthlab.tsingyuai.com), verified 2026-09-28). |
| AI capability | 5/10 | Scenario research and SERP analysis feeding page creation run as agent loops (vendor documentation: [vendor site](https://growthlab.tsingyuai.com), verified 2026-09-28). |
| Openness | 9/10 | Apache-2.0 with a self-hosted workspace (the source repository: [repository](https://github.com/tsingyuai/growth-lab), verified 2026-09-28). |
| Operational maturity | 3/10 | Founded 2026 with no API of its own (vendor documentation: [vendor site](https://growthlab.tsingyuai.com), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ Apache-2.0 licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: SEO page growth loop: scenario research, SERP analysis, page creation, IndexNow publishing |  |
| ✓ Active public repository (1,993 GitHub stars counted at last check) |  |

**What is Growth Lab?**
Growth Lab: Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex. Growth Lab ships with SEO page growth loop: scenario research, SERP analysis, page creation, IndexNow publishing. The public repository carries 1,993 stars.

**How much does Growth Lab cost?**
Growth Lab is open source - Apache-2.0 licensed and free to self-host; the public repository carries 1,993 stars; native integrations cover Claude Code, OpenAI Codex, IndexNow. You pay in server time and maintenance, not licences.

**Is Growth Lab a good self-hosted Agent Skills tool in 2026?**
Promising for teams ready to run self-hosted SEO loops with agent review. Everyone else should wait for maturity.

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 1993
- **Founded:** 2026
- **API:** No
- **Repository checked:** 2026-09-29
- **Page updated:** 2026-08-28

**Verdict:** Growth Lab is a tool in Agent Skills with free and open source. The catalog documents 5 AI features, 4 integrations and a self-hosting path. We reviewed it from vendor documentation on 2026-08-28. This is a desk review, not a hands-on test. Desk-reviewed

Codex SEO

Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations

SEO Skill Bench

Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects

Claude SEO

Open-source SEO skill for Claude Code with 25 sub-skills and 20 specialist agents

AI Business Skills

63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents

Aaron Marketing Skills

120 marketing skills across 7 disciplines for Claude Code with auditor gates

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Growth Lab
Re-check pending: pricing last verified 2026-08-28 (33 days ago).

## Growth Lab review (2026): pricing, AI features, verdict

Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex

Agent Skills · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-29

[Visit Growth Lab →](https://growthlab.tsingyuai.com)

[How we review](/methodology/) · No affiliate links

[Visit Growth Lab →](https://growthlab.tsingyuai.com)

## MartechSignal Score: 34/60

Growth Lab runs two growth loops as skills: SEO pages with IndexNow publishing and a Xiaohongshu content loop. Apache-2.0 and 2.0k stars; the harness cost is on you.

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

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Growth Lab: Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex. Growth Lab ships with SEO page growth loop: scenario research, SERP analysis, page creation, IndexNow publishing. The public repository carries 1,993 stars.

Growth Lab is open source - Apache-2.0 licensed and free to self-host; the public repository carries 1,993 stars; native integrations cover Claude Code, OpenAI Codex, IndexNow. You pay in server time and maintenance, not licences.

Promising for teams ready to run self-hosted SEO loops with agent review. Everyone else should wait for maturity.

## Similar Tools

## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Where open-source martech momentum actually lives](/blog/oss-momentum-tracker-september-2026/)
- [Claude Cowork is eating the edges of your martech stack](/blog/claude-cowork-is-eating-the-edges-of-your-martech-stack/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/growth-lab/#app",
    "name": "Growth Lab",
    "description": "Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex",
    "image": "https://martechsignal.com/og/tools/growth-lab.png",
    "url": "https://martechsignal.com/tools/growth-lab/",
    "sameAs": [
      "https://growthlab.tsingyuai.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/growth-lab/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-30",
    "datePublished": "2026-08-03",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://growthlab.tsingyuai.com",
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
        "name": "Growth Lab",
        "item": "https://martechsignal.com/tools/growth-lab/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Growth Lab?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Growth Lab: Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex. Growth Lab ships with SEO page growth loop: scenario research, SERP analysis, page creation, IndexNow publishing. The public repository carries 1,993 stars."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Growth Lab cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Growth Lab is open source - Apache-2.0 licensed and free to self-host; the public repository carries 1,993 stars; native integrations cover Claude Code, OpenAI Codex, IndexNow. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Growth Lab a good self-hosted Agent Skills tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Promising for teams ready to run self-hosted SEO loops with agent review. Everyone else should wait for maturity."
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
    "reviewBody": "Growth Lab runs two growth loops as skills: SEO pages with IndexNow publishing and a Xiaohongshu content loop. Apache-2.0 and 2.0k stars; the harness cost is on you.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/growth-lab/#app",
      "name": "Growth Lab",
      "url": "https://martechsignal.com/tools/growth-lab/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 34,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/tools/growth-lab/", "breadcrumb": {"@id": "https://martechsignal.com/tools/growth-lab/#breadcrumb"}, "dateModified": "2026-09-30"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
