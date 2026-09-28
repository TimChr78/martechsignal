# Paperclip review (2026): pricing, AI features, verdict


| Pros | Cons |
| --- | --- |
| &#10003; MIT licence with free self-hosting | &#10007; No hands-on test - this assessment is based on vendor documentation and the public repository |
| &#10003; AI capabilities: org-chart orchestration of agent teams (Claude Code, Codex, Cursor, Gemini CLI, and more) |  |
| &#10003; Established community (80,357 GitHub stars) |  |
| &#10003; Native integrations include Claude Code, Codex, Cursor (local and cloud) (12 listed) |  |

**What is Paperclip?**
Open-source control plane to manage AI agents like a company, hire, schedule, budget, and audit. It ships with org-chart orchestration of agent teams (Claude Code, Codex, Cursor, Gemini CLI, and more), 80,357 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Paperclip cost?**
Paperclip is open source - MIT licensed and free to self-host; the public repository carries 80,357 stars; native integrations cover Claude Code, Codex, Cursor (local and cloud). You pay in server time and maintenance, not licences.

**Is Paperclip worth it past the free tier?**
The most credible attempt yet at governing agent fleets like headcount rather than scripts: real budgets, approvals, and audit, with honest defaults (dormant agents, no webhooks) and a deep public docs surface.

**What happens when a Paperclip agent hits its budget cap?**
At 80% of the cap (the default warnPercent) Paperclip records a soft incident and the agent keeps working. At 100% a hard incident fires: the scope is paused immediately, no more heartbeats are scheduled, in-progress runs are cancelled, and the docs state no work is lost. You resume through the budget-incident API with raise_budget_and_resume (the new amount must exceed current spend, or the call fails) or keep_paused. Budget-paused scopes auto-resume at 00:00 UTC on the first of the month.

**Do Paperclip agents run 24/7 by default?**
No. A new agent ships with timer heartbeats turned off, and the docs recommend leaving them off and enabling wake-on-demand instead: the agent shows as active on the dashboard but consumes nothing until work lands. There are four wake sources (timer, task assignment or comment, manual wake-now, and routines), and only the timer is not event-driven. For scheduled recurring work on the hosted cloud, routines run around the clock; self-hosted routines use cron in your timezone plus signed webhooks.

**How do I connect Claude Code to Paperclip?**
Create an agent whose adapter is claude_local. Claude Code must be installed and on PATH, and authentication uses ANTHROPIC_API_KEY, AWS Bedrock environment variables, or a Claude subscription login. The adapter stores the session id and resumes it on the next heartbeat when the working directory still matches, injects Paperclip skills by building a directory of symlinks passed with --add-dir, and exposes a Test Environment button that probes the CLI in headless print mode. maxTurnsPerRun defaults to 300.

- **Pricing:** Freemium
- **Category:** [Workflow Automation](/categories/workflow-automation/)
- **GitHub:** ★ 80357
- **HQ:** EU
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Paperclip is a tool in Workflow Automation with free and open source. The catalog documents 5 AI features, 12 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Codex SEO

Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations

Zapier GTM Cheat Codes

Zapier&#x27;s installable coding-agent skills for GTM: campaign planning, CRM context, customer proof

Workato

Enterprise AI governance plus integration and automation on one platform

Pipedream

Workflow automation with 2,500+ integrations, built around data-driven triggers and HTTP steps

Budibase

Open-source operations platform for building AI agents, apps and automations on your own data

[More Workflow Automation Tools →](/categories/workflow-automation/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Workflow Automation](/categories/workflow-automation/)
- Paperclip
## Paperclip review (2026): pricing, AI features, verdict

Open-source control plane to manage AI agents like a company, hire, schedule, budget, and audit

Workflow Automation · Freemium · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[Visit Paperclip &#8594;](https://paperclip.ing)

[How we review](/methodology/) · No affiliate links

[Visit Paperclip &#8594;](https://paperclip.ing)

Not yet scored against the rubric; scored pages show six pillars.

## Overview

Paperclip is an open-source control plane for running a team of AI agents like a company: a Node.js server with a React UI that models org charts, goals, budgets, and governance instead of workflows. Its README is explicit: not an agent framework, not a workflow builder, not a chatbot, not a single-agent tool. Agents run wherever they already run (Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Hermes, Grok, Kimi Code, or an OpenClaw gateway) and connect through adapters; if it can receive a heartbeat, the docs say, it&#x27;s hired. The structure is a strict tree: every agent except the CEO has exactly one manager, and the CEO reports to you. Governance is the product. Agents cannot hire without filing a hire request into your approval queue, the CEO cannot move tasks to in progress until you approve its strategy, and budgets warn at 80% and hard-stop at 100%, pausing the scope until you raise the cap or the month resets. Every mutation produces a permanent activity record, config changes are revisioned, and one deployment can run unlimited companies with data isolation. Two details matter for anyone expecting an always-on swarm. Interval heartbeats are off by default: agents stay dormant until a task, a comment, a manual wake, or a routine arrives. And Paperclip pushes no outbound webhooks, so Slack alerting means a routine that polls. Model spend is yours: you bring provider keys, Paperclip tracks the cache-adjusted cost each agent accrues, and the docs estimate $3-15 a month for a moderately active worker. Self-hosting is free under MIT (Node.js 24.11+, pnpm 9.15+, embedded PostgreSQL, any 1 vCPU 2 GB VPS), the hosted cloud is one flat € 10/month plan with unlimited companies and EU hosting, and prebuilt company templates range from a five-agent engineering team to a 167-agent agency. At 80,187 stars with calendar-versioned releases every week or two, it is among the most active agent-management projects available.

Paperclip homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Org-chart orchestration of agent teams (Claude Code, Codex, Cursor, Gemini CLI, and more)
- Per-agent budgets: warn at 80%, hard stop at 100%, auto-pause at cap
- Approval workflows for hires, CEO strategy, and budget overrides
- Event-driven wakeups; interval heartbeats are opt-in, off by default
- Permanent activity log with revisioned config rollback
## Key Integrations

- Claude Code
- Codex
- Cursor (local and cloud)
- Gemini CLI
- OpenCode
- Hermes
- Grok Local
- Kimi Code
- Pi
- OpenClaw Gateway (coming soon)
- GitHub via pull requests
- e2b, Cloudflare, and Modal sandboxes
## Pricing

Paperclip is freemium, with a free tier to start.

Self-hosted free (MIT). Hosted cloud: one plan at € 10/month or € 100/year, 7-day trial, no credit card, unlimited companies and teammates. Model spend bills from your own provider accounts.

Current plans and limits live on the [Paperclip pricing page](https://paperclip.inc/pricing).

## How to install

- Managed install (README quickstart): curl -fsSLO https://paperclip.ing/install.sh plus its .sha256, verify with sha256sum -c, then bash install.sh. The installer ensures Node.js 24.11+, installs a CLI under ~/.paperclip/cli, and starts interactive onboarding; the README notes the checksum is served from the same origin as the script.
- Non-interactive: curl -fsSL https://paperclip.ing/install.sh | bash -s -- --no-prompt --no-onboard, then paperclipai onboard --yes. To try without installing: npx paperclipai onboard --yes, or ANTHROPIC_API_KEY=... npx paperclipai test-drive for an isolated test company pre-initialized with a CEO agent.
- The docs warn against running onboard with sudo or as root: the default setup starts embedded PostgreSQL, which refuses to run as an administrative user. Success looks like a config at ~/.paperclip/instances/default/config.json and a server on http://localhost:3100; keep it running with paperclipai service install.
- From source: git clone https://github.com/paperclipai/paperclip.git &amp;&amp; cd paperclip &amp;&amp; pnpm install &amp;&amp; pnpm dev (Node.js 24.11+, pnpm 9.15+). Docker paths exist for a quickstart compose file and a full stack with PostgreSQL 17; the image ships git, gh, ripgrep, python3, and the Claude, Codex, and OpenCode CLIs.
- Connect an agent by adapter: a Claude Code agent takes adapterType claude_local with model and working-directory config, authenticated by ANTHROPIC_API_KEY, Bedrock env vars, or Claude subscription login. Network binding presets are --bind lan and --bind tailnet; the default local_trusted mode has no login and must not be reachable from a network.
## Requirements

Node.js 24.11+ is a hard floor as of v2026.831.0 (August 2026) and pnpm 9.15+ for source installs; embedded PostgreSQL is created automatically, and any 1 vCPU, 2 GB Linux VPS is enough to start, with port 3100 kept off the internet. Telemetry is on by default and disabled with PAPERCLIP_TELEMETRY_DISABLED=1 or DO_NOT_TRACK=1. The openclaw_gateway, process, and http adapters are marked coming soon in the UI dropdown but work through the API or an imported company export, and there are no outbound webhooks, so alerting requires a polling routine.

## Best for

Teams already running several coding agents in parallel (the README&#x27;s example is twenty Claude Code terminals) that want one place to delegate through an org chart, cap spend per agent, require human approval for hires and strategy, and audit every change; also EU-constrained buyers, since cloud hosting is EU end to end and GDPR native.

## Not for

Anyone with a single agent (the README says you probably don&#x27;t need Paperclip), teams wanting drag-and-drop workflow automation (explicitly not a workflow builder), or buyers who need push notifications: no outbound webhooks exist today. Cloud Sync was removed in v2026.817.0, so company import and export is the only supported transfer path between deployments.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from github.com/paperclipai/paperclip, docs.paperclip.ing, paperclip.ing, and paperclip.inc (September 2026). Not a hands-on review. The public surface is deep: about 29 documented REST resource pages, an OpenAPI spec at /api/openapi.json, a paperclipai CLI with roughly 32 command groups, and a changelog tracking the calendar-versioned releases. Latest stable is v2026.831.1 (September 2, 2026), with canary builds shipping several times a day.

The correction that matters: our earlier hands-on notes described a lightweight trigger-action automation tool for connecting everyday SaaS apps. That is a different product. The README states plainly that Paperclip is not a workflow builder, has no drag-and-drop pipelines, and models companies with org charts, goals, budgets, and governance. We have replaced those notes in full.

Second correction: two domains, two things. paperclip.ing is the open-source project (Paperclip Labs); paperclip.inc is the hosted cloud run by Paperclip.inc OÜ, an Estonian company whose footer reads built on paperclipai/paperclip, 80.2k. Our record pointed the homepage at the commercial site; we now link the project site and keep the cloud&#x27;s pricing page. DeepSeek and Qwen are not adapters, they are model providers reachable through other adapters, and GitHub Actions is this project&#x27;s own CI, not a product integration.

Where the docs are refreshingly honest: interval heartbeats ship off by default, with the docs advising that a frequently paused agent has the wrong heartbeat rather than the wrong workflow; budget behavior is spelled out to the API call (warn at 80%, hard stop at 100%, auto-resume 00:00 UTC on the 1st); and the activity log is described as kept permanently rather than dressed up as immutable.

## Verdict

The most credible attempt yet at governing agent fleets like headcount rather than scripts: real budgets, approvals, and audit, with honest defaults (dormant agents, no webhooks) and a deep public docs surface.

## Pros and cons

## Related concepts

- [Workflow automation](/glossary/workflow-automation/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [MCP](/glossary/mcp/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source control plane to manage AI agents like a company, hire, schedule, budget, and audit. It ships with org-chart orchestration of agent teams (Claude Code, Codex, Cursor, Gemini CLI, and more), 80,357 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Paperclip is open source - MIT licensed and free to self-host; the public repository carries 80,357 stars; native integrations cover Claude Code, Codex, Cursor (local and cloud). You pay in server time and maintenance, not licences.

The most credible attempt yet at governing agent fleets like headcount rather than scripts: real budgets, approvals, and audit, with honest defaults (dormant agents, no webhooks) and a deep public docs surface.

At 80% of the cap (the default warnPercent) Paperclip records a soft incident and the agent keeps working. At 100% a hard incident fires: the scope is paused immediately, no more heartbeats are scheduled, in-progress runs are cancelled, and the docs state no work is lost. You resume through the budget-incident API with raise_budget_and_resume (the new amount must exceed current spend, or the call fails) or keep_paused. Budget-paused scopes auto-resume at 00:00 UTC on the first of the month.

No. A new agent ships with timer heartbeats turned off, and the docs recommend leaving them off and enabling wake-on-demand instead: the agent shows as active on the dashboard but consumes nothing until work lands. There are four wake sources (timer, task assignment or comment, manual wake-now, and routines), and only the timer is not event-driven. For scheduled recurring work on the hosted cloud, routines run around the clock; self-hosted routines use cron in your timezone plus signed webhooks.

Create an agent whose adapter is claude_local. Claude Code must be installed and on PATH, and authentication uses ANTHROPIC_API_KEY, AWS Bedrock environment variables, or a Claude subscription login. The adapter stores the session id and resumes it on the next heartbeat when the working directory still matches, injects Paperclip skills by building a directory of symlinks passed with --add-dir, and exposes a Test Environment button that probes the CLI in headless print mode. maxTurnsPerRun defaults to 300.

## Similar Tools

## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Your AI Marketing Agent Doesn't Need Better Prompts](/blog/ai-agents-need-campaign-state/)
- [Salesforce Made Agentforce Free. What Marketing Ops Can Build With It.](/blog/salesforce-agentforce-free-marketing-ops/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/paperclip/#app",
    "name": "Paperclip",
    "description": "Open-source control plane to manage AI agents like a company, hire, schedule, budget, and audit",
    "image": "https://martechsignal.com/og/tools/paperclip.png",
    "url": "https://martechsignal.com/tools/paperclip/",
    "sameAs": [
      "https://paperclip.ing"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/paperclip/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-07",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "EUR",
      "url": "https://paperclip.inc/pricing",
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
        "name": "Workflow Automation",
        "item": "https://martechsignal.com/categories/workflow-automation/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Paperclip",
        "item": "https://martechsignal.com/tools/paperclip/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Paperclip?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source control plane to manage AI agents like a company, hire, schedule, budget, and audit. It ships with org-chart orchestration of agent teams (Claude Code, Codex, Cursor, Gemini CLI, and more), 80,357 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Paperclip cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Paperclip is open source - MIT licensed and free to self-host; the public repository carries 80,357 stars; native integrations cover Claude Code, Codex, Cursor (local and cloud). You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Paperclip worth it past the free tier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The most credible attempt yet at governing agent fleets like headcount rather than scripts: real budgets, approvals, and audit, with honest defaults (dormant agents, no webhooks) and a deep public docs surface."
        }
      },
      {
        "@type": "Question",
        "name": "What happens when a Paperclip agent hits its budget cap?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "At 80% of the cap (the default warnPercent) Paperclip records a soft incident and the agent keeps working. At 100% a hard incident fires: the scope is paused immediately, no more heartbeats are scheduled, in-progress runs are cancelled, and the docs state no work is lost. You resume through the budget-incident API with raise_budget_and_resume (the new amount must exceed current spend, or the call fails) or keep_paused. Budget-paused scopes auto-resume at 00:00 UTC on the first of the month."
        }
      },
      {
        "@type": "Question",
        "name": "Do Paperclip agents run 24/7 by default?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. A new agent ships with timer heartbeats turned off, and the docs recommend leaving them off and enabling wake-on-demand instead: the agent shows as active on the dashboard but consumes nothing until work lands. There are four wake sources (timer, task assignment or comment, manual wake-now, and routines), and only the timer is not event-driven. For scheduled recurring work on the hosted cloud, routines run around the clock; self-hosted routines use cron in your timezone plus signed webhooks."
        }
      },
      {
        "@type": "Question",
        "name": "How do I connect Claude Code to Paperclip?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Create an agent whose adapter is claude_local. Claude Code must be installed and on PATH, and authentication uses ANTHROPIC_API_KEY, AWS Bedrock environment variables, or a Claude subscription login. The adapter stores the session id and resumes it on the next heartbeat when the working directory still matches, injects Paperclip skills by building a directory of symlinks passed with --add-dir, and exposes a Test Environment button that probes the CLI in headless print mode. maxTurnsPerRun defaults to 300."
        }
      }
    ]
  }
]
```
