# Digital Marketing Pro pricing


| Pros | Cons |
| --- | --- |
| ✓ Open-source licensing with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: 163 marketing skills + 24 specialist agents (strategy, SEO, AEO/GEO, paid, content, CRM, analytics) |  |
| ✓ Native integrations include Claude Code, Anthropic Cowork, OpenAI Codex (17 listed) |  |

**What is Digital Marketing Pro?**
163-skill marketing plugin running full 12-part brand strategy engagements in coding agents. It ships with 163 marketing skills + 24 specialist agents (strategy, SEO, AEO/GEO, paid, content, CRM, analytics), 837 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives.

**How much does Digital Marketing Pro cost?**
Digital Marketing Pro is open source - Free to self-host; the public repository carries 837 stars; native integrations cover Claude Code, Anthropic Cowork, OpenAI Codex. You pay in server time and maintenance, not licences.

**Is Digital Marketing Pro a good self-hosted Agent Skills tool in 2026?**
Strengths include 837 GitHub stars, open-source licensing with free self-hosting. The full review breaks down where it fits in a modern martech stack.

- **Pricing:** Open Source
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 837
- **API:** No
- **Last verified:** 2026-09-28

**Verdict:** Digital Marketing Pro is a tool in Agent Skills with free and open source. The catalog documents 6 AI features, 17 integrations and a self-hosting path. We reviewed it from vendor documentation on 2026-09-28. This is a desk review, not a hands-on test. Desk-reviewed

Codex SEO

Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations

Claude SEO

Open-source SEO skill for Claude Code with 25 sub-skills and 18 parallel agents

SEO Skill Bench

Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects

AI Business Skills

63 bilingual marketing skills (Vietnamese + Global) for Claude Code and agents

Diffmode Growth Tactics

Free Claude Code/Codex pipeline that mines case studies and rejects obvious growth plays

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Digital Marketing Pro
## Digital Marketing Pro review (2026): pricing, AI features, verdict

163-skill marketing plugin running full 12-part brand strategy engagements in coding agents

Agent Skills · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-28

[How we review](/methodology/) · No affiliate links

[Visit Digital Marketing Pro →](https://github.com/indranilbanerjee/digital-marketing-pro)

Not yet scored against the rubric; scored pages show six pillars.

## Overview

Digital Marketing Pro is a plugin with 163 marketing skills and 24 specialist agents that runs inside coding agents: Claude Code, OpenAI Codex, Cursor, GitHub Copilot CLI, Hermes, and roughly 35 other harnesses that adopted the Agent Skills open standard. What separates it from most skill packs is that it is not a loose pile of prompts. Every brand goes through the same fixed 12-part strategy flow. You run /digital-marketing-pro:engagement, and about an hour later you have 50 to 60 canonical files per brand: market research, segmentation, positioning, a 12-month growth plan, channel strategies, ad copy, and AI creative briefs. The maintainer puts API spend at $15 to $40 per full engagement on Opus-class models, which sounds about right for that file count. A good chunk of this is real tooling rather than prompt dressing. There are Python scripts behind the skills: SERP-overlap keyword clustering (now Unicode-aware after a German compound-word bug surfaced in issue #11), backlink gap analysis, and a /check gate that scans drafts for hallucinations, unsupported claims, and brand-voice drift before anything ships. Eight HTTP connectors (Slack, HubSpot, Klaviyo, SendGrid, Brevo, Customer.io, Mailchimp, Ahrefs) fire real API calls with audit logging, and a doctor command shows what is wired versus what still needs setup. C2PA content provenance signing and EU AI Act Article 50 disclosure clauses are built into the creative-brief skills, which matters if you market into the EU. The repo carries over 400 stdlib tests, unusual for a marketing skill pack. Setup is one command on the canonical path: /plugin marketplace add indranilbanerjee/neels-plugins, then install. Non-technical marketers can go through the Anthropic Cowork UI instead and never open a terminal; outputs persist to the team's Google Drive. Since the skills are plain SKILL.md files, Goose, OpenHands, Gemini CLI, and others can consume the skills/ folder directly with no platform-specific manifest. Python stdlib only, no third-party dependencies, MIT licensed, no telemetry. The honest limitation: 50 to 60 documents per brand is a lot to review, and consistent structure is not the same as quality. The flow has a Client Validation Document as its one mandatory stop, and a decision matrix maps client pushback to selective v2 re-runs, so the design anticipates this. But if you run one brand and want a quick campaign brief, this is overkill. It is aimed squarely at agencies and in-house teams juggling 50 to 200 brands, where the point is that every engagement looks the same so handoffs work and quality is auditable across the portfolio. Against claude-seo in this directory, which concentrates on SEO with 25 sub-skills and 18 agents, DMP covers the whole funnel: strategy, content, paid media, CRM, analytics, and compliance. It is also slower to first value. At 837 stars, 137 commits, 61 tagged releases, and a v3.31.1 that reproduced and fixed all five open community issues with regression tests, it is one of the most actively maintained marketing skill packs on GitHub right now.

Digital Marketing Pro homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- 163 marketing skills + 24 specialist agents (strategy, SEO, AEO/GEO, paid, content, CRM, analytics)
- 12-Part Strategy Flow producing ~50-60 canonical documents per brand engagement
- 6-platform AEO/GEO audit including Google AI Mode
- C2PA content provenance signing + EU AI Act Article 50 disclosure clauses
- /check pre-publish gate: hallucination, claims, and brand-voice scanning
- Real API execution via 8 verified HTTP connectors with audit logging
## Key Integrations

- Claude Code
- Anthropic Cowork
- OpenAI Codex
- Cursor
- GitHub Copilot CLI
- Google Antigravity
- Hermes Agent
- OpenClaw
- Grok
- Slack
- HubSpot
- Klaviyo
- SendGrid
- Brevo
- Customer.io
- Mailchimp
- Ahrefs
## Pricing

Digital Marketing Pro is free to self-host.

Free, MIT licensed. Pay your own model API costs: roughly $15-40 per full 12-part engagement on Opus-class models.

Current plans and limits live on the [Digital Marketing Pro pricing page](https://github.com/indranilbanerjee/digital-marketing-pro#quick-start).

## Pros and cons

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

163-skill marketing plugin running full 12-part brand strategy engagements in coding agents. It ships with 163 marketing skills + 24 specialist agents (strategy, SEO, AEO/GEO, paid, content, CRM, analytics), 837 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives.

Digital Marketing Pro is open source - Free to self-host; the public repository carries 837 stars; native integrations cover Claude Code, Anthropic Cowork, OpenAI Codex. You pay in server time and maintenance, not licences.

Strengths include 837 GitHub stars, open-source licensing with free self-hosting. The full review breaks down where it fits in a modern martech stack.

## Similar Tools

## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Competitive-Intel Tools Were the First Martech Category AI Killed](/blog/ci-tools-were-the-first-martech-category-ai-killed/)
- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
### Quick Facts

Related guides: [Agent Skills Tools](/best/agent-skills-tools/)

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/digital-marketing-pro/#app",
    "name": "Digital Marketing Pro",
    "description": "163-skill marketing plugin running full 12-part brand strategy engagements in coding agents",
    "image": "https://martechsignal.com/og/tools/digital-marketing-pro.png",
    "url": "https://martechsignal.com/tools/digital-marketing-pro/",
    "sameAs": [
      "https://github.com/indranilbanerjee/digital-marketing-pro"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/digital-marketing-pro/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-28",
    "datePublished": "2026-09-28",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://github.com/indranilbanerjee/digital-marketing-pro#quick-start",
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
        "name": "Digital Marketing Pro",
        "item": "https://martechsignal.com/tools/digital-marketing-pro/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Digital Marketing Pro?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "163-skill marketing plugin running full 12-part brand strategy engagements in coding agents. It ships with 163 marketing skills + 24 specialist agents (strategy, SEO, AEO/GEO, paid, content, CRM, analytics), 837 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Digital Marketing Pro cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Digital Marketing Pro is open source - Free to self-host; the public repository carries 837 stars; native integrations cover Claude Code, Anthropic Cowork, OpenAI Codex. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Digital Marketing Pro a good self-hosted Agent Skills tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Strengths include 837 GitHub stars, open-source licensing with free self-hosting. The full review breaks down where it fits in a modern martech stack."
        }
      }
    ]
  }
]
```
