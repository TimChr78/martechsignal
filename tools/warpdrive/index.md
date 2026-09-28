# Warpdrive review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | Free under MIT with no per-seat billing; your only cost is the hosting server, stated plainly (the vendor pricing page, verified 2026-09-07). |
| Feature depth | 3/10 | Pipelines and Gmail integration cover the BD workflow minimum (vendor documentation). |
| Integrations | 3/10 | Gmail and Google Workspace with SSO, MinIO storage and Postgres documented (vendor documentation). |
| AI capability | 2/10 | No AI features are documented in the catalog as of 2026-09-28 (vendor documentation). |
| Openness | 9/10 | MIT-licensed with 72 GitHub stars and full self-hosting (the source repository). |
| Operational maturity | 2/10 | 72 stars with no API and a minimal dependency stack (vendor documentation). |


| Pros | Cons |
| --- | --- |
| &#10003; MIT licence with free self-hosting | &#10007; Young project (72 GitHub stars) - smaller community and plugin ecosystem |
| &#10003; Native integrations include Gmail / Google Workspace, Google Workspace SSO, MinIO / S3-compatible storage (4 listed) |  |

**What is Warpdrive?**
Self-hosted open-source Pipedrive alternative for BD teams: pipelines and Gmail on your own box. It ships with 72 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Warpdrive cost?**
Warpdrive is open source - MIT licensed and free to self-host; the public repository carries 72 stars; native integrations cover Gmail / Google Workspace, Google Workspace SSO, MinIO / S3-compatible storage. You pay in server time and maintenance, not licences.

**Is Warpdrive a good self-hosted CRM tool in 2026?**
A scoped, honestly documented self-hosted Pipedrive alternative whose AI story is an MCP server rather than a model. One maintainer and a private upstream mean you are betting on a person, not a community.

**Does Warpdrive import my existing Gmail when I connect a mailbox?**
No. The docs are explicit that there is no backfill: the first sync records Gmail&#x27;s current history cursor and starts from there, so mail already in the mailbox is not imported and a freshly connected inbox stays empty until new mail arrives. Inboxes are also personal; colleagues do not see yours and you do not see theirs. Sharing happens by linking a Gmail thread to a deal or contact so it appears on that record&#x27;s timeline.

**Can an AI assistant delete records or send email through Warpdrive&#x27;s MCP server?**
No on both counts. The MCP server exposes 29 tools (13 read, 16 write) and has no delete tools for CRM records and no send tool: email drafts are written for review and sending stays a human action. Every call runs as the OAuth signed-in user, bounded by that user&#x27;s visibility and permission flags, and writes land in the change log attributed to that user. Access is revoked per client under Settings, Connected apps.

**How do I back up a self-hosted Warpdrive instance?**
Two volumes, both required: a Postgres dump and the miniodata volume, since attachments live in MinIO and the docs warn that a database dump alone restores records whose attachments are gone. The documented command is docker compose exec -T postgres pg_dump -U warpdrive warpdrive | gzip &gt; backup-$(date +%F).sql.gz, followed by copying the miniodata volume, and they recommend testing a restore before you need one.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 72
- **API:** No
- **Last verified:** 2026-09-07

**Verdict:** Warpdrive is a tool in CRM with free and open source. The catalog documents 4 integrations and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Twenty

The open-source alternative to Salesforce, designed for AI with modern CRM workflows

BillionMail

Open-source mail server, newsletter, and email marketing platform, fully self-hosted and free

Cordys CRM

Open-source AI CRM with built-in agents, conversational analytics, and private deployment

DeskcommCRM

Self-hosted open-source CRM with AI agents that sell through WhatsApp

Salesforce CRM

Enterprise CRM platform with Einstein AI for sales, service, and marketing teams

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- Warpdrive
## Warpdrive review (2026): pricing, AI features, verdict

Self-hosted open-source Pipedrive alternative for BD teams: pipelines and Gmail on your own box

CRM · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[Visit Warpdrive &#8594;](https://warpdrivecrm.com)

[How we review](/methodology/) · No affiliate links

[Visit Warpdrive &#8594;](https://warpdrivecrm.com)

## MartechSignal Score: 28/60

Warpdrive is the tiny Pipedrive alternative: pipelines and Gmail on your own server, MIT with no per-seat billing. At 72 stars it is a bet on a codebase, not a product decision.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Warpdrive is a self-hosted, MIT-licensed CRM that reimplements Pipedrive&#x27;s core business development loop: kanban pipelines, a deal workspace, contacts and organizations, and two-way Gmail. It is single-tenant, runs on your own box, and has no per-seat bill. The README&#x27;s comparison table against Pipedrive marks products, projects, invoicing, forecasting, multi-currency, workflow automation, and native mobile apps as intentionally out of scope, and the docs are blunt about it: if your team needs those, this is not the right tool. What it covers is deep for a project this young: pipelines with weighted stage totals and rotting-deal indicators, people and orgs with JSONB custom fields, a leads inbox with CSV import and undo, funnel stats, RBAC, and Gmail with thread linking, open and click tracking, templates, merge fields, and scheduled send. Sync is go-forward only: the docs state there is no backfill, so existing mail is never imported. AI access exists, but not as AI features. There is no lead scoring or drafting model; instead the project ships a documented MCP server at /api/mcp with 29 tools, OAuth 2.1 protected, so Claude, ChatGPT, or Cursor can search and update the CRM under each user&#x27;s own permissions. The server has no delete tools for CRM records and no send tool: drafts are written for review and sending stays human. Contact enrichment is not AI either; it wraps your own paid Apollo, RocketReach, or GetProspect keys behind a review step. Setup is docker compose up -d --build after copying .env.example, bringing up Postgres 16, MinIO, a background worker, and Caddy for TLS. Requirements are specific: a domain with a second s3. subdomain record, ports 80 and 443, and a Google Workspace OAuth client, since Google is both the SSO and the mail provider. One maintainer, 35 commits, one release, 72 stars, and a public mirror of a private upstream: treat it as a young tool worth an afternoon, not a settled platform.

Warpdrive homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## Key Integrations

- Gmail / Google Workspace
- Google Workspace SSO
- MinIO / S3-compatible storage
- Postgres
## Pricing

Warpdrive is free to self-host under the MIT licence.

Free, MIT licensed, no per-seat billing. You pay only for the server you host it on.

## How to install

- Prerequisites (docs.warpdrivecrm.com/setup): a Linux box with Docker and the Compose plugin, a domain with A/AAAA records for both the app host and an s3. subdomain (browser uploads POST presigned requests there; skipping it breaks every upload), ports 80 and 443 open, and a Google OAuth client from the project that owns your Workspace.
- Install is two commands from the repo: cp .env.example .env, fill in domain, Google OAuth, storage, and secrets, then docker compose up -d --build. That starts caddy, postgres (postgres:16-alpine), minio, app, ws, and worker, plus one-shot migrate and createbuckets services.
- Secrets come from openssl: openssl rand -base64 32 for TOKEN_ENCRYPTION_KEY, openssl rand -hex 32 for WS_TICKET_SECRET, openssl rand -hex 16 for the MinIO keys, and openssl rand -base64 32 for OAUTH_SIGNING_KEY. DATABASE_URL and the other secrets accept a VAR_FILE variant for Docker secrets.
- In Google Cloud, register two redirect URIs: the app sign-in callback and https://&lt;your-domain&gt;/api/gmail/oauth/callback. Set SEED_ADMIN_EMAIL (the first Google sign-in is promoted to admin) and keep ALLOW_FIRST_LOGIN_ADMIN=false, which the env boundary enforces in production.
- Verify with docker compose ps and curl -fsS https://&lt;domain&gt;/api/health (returns {&quot;ok&quot;:true}). Upgrades are git pull &amp;&amp; docker compose up -d --build, with migrations running in the one-shot migrate service before the app restarts.
## Requirements

Google Workspace is effectively mandatory: Google SSO is the only documented auth path and the Gmail API the only mail integration, with GOOGLE_WORKSPACE_DOMAIN available to pin sign-in to one domain. NEXT_PUBLIC_WS_URL must be set at build time; if it is missing the app still starts and looks healthy but the board, inbox, notifications, and presence indicators silently never update. Telemetry is switchable: leave POSTHOG_KEY and POSTHOG_HOST empty or set DISABLE_TELEMETRY, and DISABLE_UPDATE_CHECK=true for deployments that should make no outbound calls. Uploads cap at 25 MiB by default (MAX_FILE_BYTES). No RAM or CPU sizing is documented anywhere. If a CSV import sticks at &quot;uploaded&quot;, the docs point at the worker process: background jobs run only there.

## Best for

Business-development teams already on Google Workspace that want Pipedrive&#x27;s pipeline-and-Gmail loop on their own infrastructure: single-tenant, MIT licensed, no per-seat bill, data in your own Postgres and S3-compatible storage, and an MCP server so assistants can work the CRM under each user&#x27;s permissions.

## Not for

Teams that need products, projects, invoicing, forecasts, multi-currency, workflow automation beyond email scheduling, web forms, or native mobile apps: the README marks all of them out of scope and the docs say plainly that this is not the right tool if you need them. Also not for shops without Google Workspace, and not for bulk integration work: CSV is the documented import route, with no REST API, no webhooks, and no API keys.

## Review notes

Assessed from github.com/sneg55/warpdrive, docs.warpdrivecrm.com (about 25 pages), and warpdrivecrm.com in September 2026; we have not deployed an instance. The repo is young and small: 72 stars, 35 commits, one contributor (Nikita Sawinyh), one release (v1.0.0, July 19, 2026), zero issues and zero pull requests ever filed, latest commit September 7, 2026. The docs site config describes the repo as a public mirror of a private source-of-truth repository, with pull requests merged upstream and synced back on the next release.

The correction that matters: our earlier text said the repo&#x27;s CLAUDE.md and PostHog MCP config help developers work on the code rather than users sell, and recorded no API. Both were wrong. Warpdrive ships a user-facing MCP server as a documented headline feature: 29 tools (13 read, 16 write) at /api/mcp over OAuth 2.1, with no delete tools for CRM records and no send tool, so drafts are written for review and sending stays a human action. What remains true is the absence of a REST API, webhooks, and API keys.

Second correction: our earlier summary implied the README compares Warpdrive with other open-source CRMs. The comparison table is against Pipedrive only, and its out-of-scope rows are verbatim: products, projects, invoicing, forecast, multi-currency, workflow automation (email scheduling only), web forms, marketplace, and native mobile apps. The README calls Warpdrive a focused, self-hosted CRM rather than a feature-for-feature clone, and says it is used in production for a single team&#x27;s BD workflow.

Free applies to the software, not every workflow: contact enrichment requires your own paid Apollo, RocketReach, or GetProspect keys, which are encrypted at rest and put the provider on a 24-hour cooldown when quota runs out. Backups need both a pg_dump and the miniodata volume; the docs note that a database dump alone restores records whose attachments are gone.

## Verdict

A scoped, honestly documented self-hosted Pipedrive alternative whose AI story is an MCP server rather than a model. One maintainer and a private upstream mean you are betting on a person, not a community.

## Pros and cons

## Related concepts

- [CRM](/glossary/crm/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
- [Customer journey](/glossary/customer-journey/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Self-hosted open-source Pipedrive alternative for BD teams: pipelines and Gmail on your own box. It ships with 72 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Warpdrive is open source - MIT licensed and free to self-host; the public repository carries 72 stars; native integrations cover Gmail / Google Workspace, Google Workspace SSO, MinIO / S3-compatible storage. You pay in server time and maintenance, not licences.

A scoped, honestly documented self-hosted Pipedrive alternative whose AI story is an MCP server rather than a model. One maintainer and a private upstream mean you are betting on a person, not a community.

No. The docs are explicit that there is no backfill: the first sync records Gmail&#x27;s current history cursor and starts from there, so mail already in the mailbox is not imported and a freshly connected inbox stays empty until new mail arrives. Inboxes are also personal; colleagues do not see yours and you do not see theirs. Sharing happens by linking a Gmail thread to a deal or contact so it appears on that record&#x27;s timeline.

No on both counts. The MCP server exposes 29 tools (13 read, 16 write) and has no delete tools for CRM records and no send tool: email drafts are written for review and sending stays a human action. Every call runs as the OAuth signed-in user, bounded by that user&#x27;s visibility and permission flags, and writes land in the change log attributed to that user. Access is revoked per client under Settings, Connected apps.

Two volumes, both required: a Postgres dump and the miniodata volume, since attachments live in MinIO and the docs warn that a database dump alone restores records whose attachments are gone. The documented command is docker compose exec -T postgres pg_dump -U warpdrive warpdrive | gzip &gt; backup-$(date +%F).sql.gz, followed by copying the miniodata volume, and they recommend testing a restore before you need one.

## Similar Tools

## Related reading

- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [NocoBase vs NocoDB vs Budibase: pick by team shape, not by spec sheet](/blog/nocobase-vs-nocodb-vs-budibase/)
- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/warpdrive/#app",
    "name": "Warpdrive",
    "description": "Self-hosted open-source Pipedrive alternative for BD teams: pipelines and Gmail on your own box",
    "image": "https://martechsignal.com/og/tools/warpdrive.png",
    "url": "https://martechsignal.com/tools/warpdrive/",
    "sameAs": [
      "https://warpdrivecrm.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/warpdrive/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-07",
    "datePublished": "2026-09-03",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://warpdrivecrm.com",
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
        "name": "CRM",
        "item": "https://martechsignal.com/categories/crm/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Warpdrive",
        "item": "https://martechsignal.com/tools/warpdrive/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Warpdrive?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Self-hosted open-source Pipedrive alternative for BD teams: pipelines and Gmail on your own box. It ships with 72 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Warpdrive cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Warpdrive is open source - MIT licensed and free to self-host; the public repository carries 72 stars; native integrations cover Gmail / Google Workspace, Google Workspace SSO, MinIO / S3-compatible storage. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Warpdrive a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A scoped, honestly documented self-hosted Pipedrive alternative whose AI story is an MCP server rather than a model. One maintainer and a private upstream mean you are betting on a person, not a community."
        }
      },
      {
        "@type": "Question",
        "name": "Does Warpdrive import my existing Gmail when I connect a mailbox?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. The docs are explicit that there is no backfill: the first sync records Gmail's current history cursor and starts from there, so mail already in the mailbox is not imported and a freshly connected inbox stays empty until new mail arrives. Inboxes are also personal; colleagues do not see yours and you do not see theirs. Sharing happens by linking a Gmail thread to a deal or contact so it appears on that record's timeline."
        }
      },
      {
        "@type": "Question",
        "name": "Can an AI assistant delete records or send email through Warpdrive's MCP server?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No on both counts. The MCP server exposes 29 tools (13 read, 16 write) and has no delete tools for CRM records and no send tool: email drafts are written for review and sending stays a human action. Every call runs as the OAuth signed-in user, bounded by that user's visibility and permission flags, and writes land in the change log attributed to that user. Access is revoked per client under Settings, Connected apps."
        }
      },
      {
        "@type": "Question",
        "name": "How do I back up a self-hosted Warpdrive instance?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Two volumes, both required: a Postgres dump and the miniodata volume, since attachments live in MinIO and the docs warn that a database dump alone restores records whose attachments are gone. The documented command is docker compose exec -T postgres pg_dump -U warpdrive warpdrive | gzip > backup-$(date +%F).sql.gz, followed by copying the miniodata volume, and they recommend testing a restore before you need one."
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
    "reviewBody": "Warpdrive is the tiny Pipedrive alternative: pipelines and Gmail on your own server, MIT with no per-seat billing. At 72 stars it is a bet on a codebase, not a product decision.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/warpdrive/#app",
      "name": "Warpdrive",
      "url": "https://martechsignal.com/tools/warpdrive/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 28,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
