# Chatwoot review (2026): pricing, AI features, verdict


| Pros | Cons |
| --- | --- |
| &#10003; Open-source licensing with free self-hosting | &#10007; Paid plans start at $19/mo once past the free tier |
| &#10003; AI capabilities: captain Assistant (AI chatbot) |  |
| &#10003; Established community (36,644 GitHub stars) |  |
| &#10003; Native integrations include Slack, Linear, Dialogflow (6 listed) |  |

**What is Chatwoot?**
Open-source customer engagement suite with Captain AI and full self-hosting. It ships with captain Assistant (AI chatbot), 36,644 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Chatwoot cost?**
Chatwoot has a free tier; paid plans start at $19/mo. Community Edition free self-hosted (MIT Expat; the enterprise/ directory is separately licensed). Cloud: Hacker free (2 agents), Startups $19, Business $39, Enterprise $99 per agent/mo billed annually. Captain AI credits $20 per 1,000. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Chatwoot a good self-hosted Chatbots &amp; Conversational AI tool in 2026?**
The strongest self-hostable support inbox in open source, with real AI now bolted on behind a paid licence; budget for infrastructure and for writing your own integrations.

**How much RAM and CPU does self-hosted Chatwoot need?**
The requirements page states 4GB RAM as the required minimum and 4 cores as the recommended minimum, each supporting up to 10,000 conversations a day, with 8GB and 8 cores supporting 20,000. It also asks for at least 1GB of swap, Redis 7.0 or higher, and Ruby 3.2 or later for source installs. Postgres is the only supported database, and the production compose image ships Postgres 16 with pgvector for the AI features.

**Can I use Captain AI on a self-hosted Chatwoot instance?**
Yes, but not on the free community edition: the guide lists Chatwoot Enterprise Edition with a paid plan and a valid OpenAI API key as prerequisites. The default model is gpt-4o-mini and a self-hosted OpenAI-compatible endpoint can be supplied instead, and the docs note that in a self-hosted setup Captain only sends data to the model you choose. Captain has to be enabled in the Super Admin Console and then toggled on in the account&#x27;s Premium Features.

**What do Chatwoot&#x27;s AI credits cover and how do they bill?**
Every Captain action consumes 1 credit per message because a fixed model configuration is used, and the documented credit-consuming actions include assistant responses, Copilot lookups, editor actions such as rephrase, summarize, and suggest a reply, label suggestions, workflow model calls, and audio transcription. Paid cloud plans include 300 credits monthly on Startups, 500 on Business, and 800 on Enterprise, additional credits bill at $20 per 1,000, and purchased credits expire after 6 months and require an active subscription.

- **Pricing:** Open Source
- **Category:** [Chatbots &amp; Conversational AI](/categories/chatbots/)
- **GitHub:** ★ 36644
- **Founded:** 2019
- **HQ:** Distributed team across the US and India; YC profile lists San Francisco
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Chatwoot is a tool in Chatbots &amp; Conversational AI with free and open source. The catalog documents 6 AI features, 6 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Intercom

AI-first customer service platform with Fin AI agent and omnichannel messaging

Tidio

AI-powered live chat and chatbot platform with Lyro AI agent for customer support

Cordys CRM

Open-source AI CRM with built-in agents, conversational analytics, and private deployment

Scrunch

The AI Customer Experience Platform: monitor, optimize and serve your site to AI agents

[More Chatbots &amp; Conversational AI Tools →](/categories/chatbots/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Chatbots &amp; Conversational AI](/categories/chatbots/)
- Chatwoot
## Chatwoot review (2026): pricing, AI features, verdict

Open-source customer engagement suite with Captain AI and full self-hosting

Chatbots &amp; Conversational AI · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[How we review](/methodology/) · No affiliate links

[Visit Chatwoot &#8594;](https://www.chatwoot.com)

Not yet scored against the rubric; scored pages show six pillars.

## Overview

Chatwoot is an open-source customer engagement platform that folds website live chat, email, WhatsApp, Telegram, Facebook, Instagram, SMS, LINE, TikTok, and an API channel into one team inbox, self-hostable or rented as cloud. The stack is Ruby on Rails with Vue, Sidekiq, Redis, and Postgres 16 with pgvector, and the repo sits near 36,600 GitHub stars with v4.17.1 released in August 2026. Self-hosting is genuinely first-class: the Docker guide pulls chatwoot/chatwoot:latest, fetches the production compose file and .env example from the repo, runs db:chatwoot_prepare, then docker compose up -d, and a Linux installer script (cwctl) targets Ubuntu 24.04 with Heroku and DigitalOcean one-click paths documented. Documented sizing is 4GB RAM and 4 cores for up to 10,000 conversations a day, doubling for 20,000. AI arrives as Captain, positioned as the AI agent for customer support: an Assistant that answers first-response questions from your help centre, a Copilot that drafts and translates replies for agents, Memories that keep per-customer notes, reply suggestions, summarization, and content gap detection that surfaces questions your help centre does not answer. Captain is credit-metered, 1 credit per message, with 300,500, and 800 monthly credits on the paid cloud tiers and extra credits at $20 per 1,000; on self-hosted installs it requires Enterprise Edition with a paid plan plus your own OpenAI API key. Cloud pricing per agent per month billed annually is $0 (Hacker, 2 agents, 500 conversations), $19 (Startups), $39 (Business), and $99 (Enterprise with SSO and audit logs). Documented integrations are thinner than our earlier record claimed: Slack, Linear, Dialogflow, Google Translate, Cloudflare RealtimeKit, and LeadSquared are live, with Shopify and HubSpot listed for Q4 2026, so plan on the REST API and webhooks for the rest.

Chatwoot homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Captain Assistant (AI chatbot)
- Captain Copilot (agent assist)
- Captain Memories (auto customer notes)
- AI reply suggestions
- AI conversation summarization
- Smart FAQs content gap detection
## Key Integrations

- Slack
- Linear
- Dialogflow
- Google Translate
- Cloudflare RealtimeKit
- LeadSquared
## Pricing

Chatwoot is free to self-host, paid plans start at $19/mo as of 2026-09.

Community Edition free self-hosted (MIT Expat; the enterprise/ directory is separately licensed). Cloud: Hacker free (2 agents), Startups $19, Business $39, Enterprise $99 per agent/mo billed annually. Captain AI credits $20 per 1,000

Current plans and limits live on the [Chatwoot pricing page](https://www.chatwoot.com/pricing).

## How to install

- Docker, the documented default: wget -O .env https://raw.githubusercontent.com/chatwoot/chatwoot/develop/.env.example, wget -O docker-compose.yaml https://raw.githubusercontent.com/chatwoot/chatwoot/develop/docker-compose.production.yaml, then docker compose run --rm rails bundle exec rails db:chatwoot_prepare and docker compose up -d.
- The production compose file pairs chatwoot/chatwoot:latest with pgvector/pgvector:pg16 and redis:alpine, so Postgres with pgvector and Redis arrive with the stack. Upgrades are docker compose pull, docker compose up -d, then the db:chatwoot_prepare step again.
- Linux VM alternative: wget https://get.chatwoot.app/linux/install.sh, chmod +x install.sh, ./install.sh --install. The same script installs as cwctl for day-two management, and the docs target Ubuntu 24.04.
- Hosted paths also documented: a Heroku deploy button and DigitalOcean 1-Click Kubernetes, plus a Helm chart for Kubernetes and an AWS guide.
- For the community edition image specifically, the -ce tags (latest-ce) exclude the enterprise directory code; the self-hosted FAQ covers what the paid Enterprise Edition unlocks.
## Requirements

4GB RAM and 4 cores is the documented minimum and supports up to 10,000 conversations a day (8GB and 8 cores for 20,000), with at least 1GB of swap, Redis 7.0 or higher, Ruby 3.2 or later for source installs, and Postgres as the only supported database. Self-hosting means you own upgrades, backups, and channel credentials.

## Best for

Technical support and success teams that want a self-hosted inbox across web chat, WhatsApp, email, and social DMs without per-seat SaaS costs, and that can run Rails, Postgres, and Redis themselves. The API, webhooks, and agent bots make it a reasonable base for custom support tooling.

## Not for

Teams that expect a broad native integration catalog out of the box (six integrations are live; Shopify and HubSpot are roadmap items for Q4 2026), and non-technical teams that want AI features without an OpenAI key: Captain on self-hosted requires Enterprise Edition with a paid plan.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from the repository, developers.chatwoot.com, and chatwoot.com (September 2026). Not a hands-on review. The repo is healthy: 36,581 stars, v4.17.1 released August 27, 2026, and a commit log that has not slowed since the 2019 open-sourcing.

The pricing correction is significant. Our record listed Hacker at $19/month and Startups at $49/month, and both are wrong against the current page: the ladder is Hacker at $0 (2 agents, 500 conversations a month, live chat only), Startups at $19, Business at $39, and Enterprise at $99, all per agent per month billed annually, with conversation retention rising from 30 days to 1, 2, then 3 years. The self-hosted page mirrors it with Community Edition free, Premium Support at $19, and Enterprise Edition at $99 per agent monthly.

The license needs qualifying too. The LICENSE file grants MIT Expat to content outside named directories and states that everything under the enterprise/ directory follows enterprise/LICENSE, which is why GitHub reports the repo license as NOASSERTION rather than MIT. Calling the whole project MIT, as we did, overstates it: the community edition is MIT, and the AI and premium features live behind the enterprise directory and its paid licence.

Two data fixes follow from that. Our AI list included sentiment analysis, which appears nowhere in the Captain documentation, and auto-replies, which is not an official feature name; the documented set is Assistant, Copilot, Memories, reply suggestions, summarization, and content gap detection, with label suggestions and audio transcription also consuming credits. Our integration list named WhatsApp and Telegram, which are channels rather than integrations, plus Zapier, Salesforce, Google Analytics, and HubSpot, none of which appear on the live integrations page: the shipped list is Slack, Linear, Dialogflow, Google Translate, Cloudflare RealtimeKit, and LeadSquared.

Company facts were also off: Bangalore appears on no live page, the team page describes a distributed team across the United States and India, and the Y Combinator profile lists founding year 2020, the W21 batch, and San Francisco as headquarters. The project itself was open-sourced in 2019, which is the year worth keeping in the timeline.

## Verdict

The strongest self-hostable support inbox in open source, with real AI now bolted on behind a paid licence; budget for infrastructure and for writing your own integrations.

## Pros and cons

## Related concepts

- [Chatbot](/glossary/chatbot/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source customer engagement suite with Captain AI and full self-hosting. It ships with captain Assistant (AI chatbot), 36,644 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Chatwoot has a free tier; paid plans start at $19/mo. Community Edition free self-hosted (MIT Expat; the enterprise/ directory is separately licensed). Cloud: Hacker free (2 agents), Startups $19, Business $39, Enterprise $99 per agent/mo billed annually. Captain AI credits $20 per 1,000. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

The strongest self-hostable support inbox in open source, with real AI now bolted on behind a paid licence; budget for infrastructure and for writing your own integrations.

The requirements page states 4GB RAM as the required minimum and 4 cores as the recommended minimum, each supporting up to 10,000 conversations a day, with 8GB and 8 cores supporting 20,000. It also asks for at least 1GB of swap, Redis 7.0 or higher, and Ruby 3.2 or later for source installs. Postgres is the only supported database, and the production compose image ships Postgres 16 with pgvector for the AI features.

Yes, but not on the free community edition: the guide lists Chatwoot Enterprise Edition with a paid plan and a valid OpenAI API key as prerequisites. The default model is gpt-4o-mini and a self-hosted OpenAI-compatible endpoint can be supplied instead, and the docs note that in a self-hosted setup Captain only sends data to the model you choose. Captain has to be enabled in the Super Admin Console and then toggled on in the account&#x27;s Premium Features.

Every Captain action consumes 1 credit per message because a fixed model configuration is used, and the documented credit-consuming actions include assistant responses, Copilot lookups, editor actions such as rephrase, summarize, and suggest a reply, label suggestions, workflow model calls, and audio transcription. Paid cloud plans include 300 credits monthly on Startups, 500 on Business, and 800 on Enterprise, additional credits bill at $20 per 1,000, and purchased credits expire after 6 months and require an active subscription.

## Similar Tools

## Related reading

- [Salesforce Made Agentforce Free. What Marketing Ops Can Build With It.](/blog/salesforce-agentforce-free-marketing-ops/)
- [Link Building Won't Get You Into AI Answers. Community Signals Will.](/blog/link-building-wont-get-you-into-ai-answers/)
- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
### Quick Facts

Related guides: [Ai Chatbot Tools](/best/ai-chatbot-tools)

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/chatwoot/#app",
    "name": "Chatwoot",
    "description": "Open-source customer engagement suite with Captain AI and full self-hosting",
    "image": "https://martechsignal.com/og/tools/chatwoot.png",
    "url": "https://martechsignal.com/tools/chatwoot/",
    "sameAs": [
      "https://www.chatwoot.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/chatwoot/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-07",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 19,
      "priceCurrency": "USD",
      "url": "https://www.chatwoot.com/pricing",
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
        "name": "Chatbots & Conversational AI",
        "item": "https://martechsignal.com/categories/chatbots/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Chatwoot",
        "item": "https://martechsignal.com/tools/chatwoot/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Chatwoot?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source customer engagement suite with Captain AI and full self-hosting. It ships with captain Assistant (AI chatbot), 36,644 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Chatwoot cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Chatwoot has a free tier; paid plans start at $19/mo. Community Edition free self-hosted (MIT Expat; the enterprise/ directory is separately licensed). Cloud: Hacker free (2 agents), Startups $19, Business $39, Enterprise $99 per agent/mo billed annually. Captain AI credits $20 per 1,000. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Chatwoot a good self-hosted Chatbots & Conversational AI tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The strongest self-hostable support inbox in open source, with real AI now bolted on behind a paid licence; budget for infrastructure and for writing your own integrations."
        }
      },
      {
        "@type": "Question",
        "name": "How much RAM and CPU does self-hosted Chatwoot need?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The requirements page states 4GB RAM as the required minimum and 4 cores as the recommended minimum, each supporting up to 10,000 conversations a day, with 8GB and 8 cores supporting 20,000. It also asks for at least 1GB of swap, Redis 7.0 or higher, and Ruby 3.2 or later for source installs. Postgres is the only supported database, and the production compose image ships Postgres 16 with pgvector for the AI features."
        }
      },
      {
        "@type": "Question",
        "name": "Can I use Captain AI on a self-hosted Chatwoot instance?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, but not on the free community edition: the guide lists Chatwoot Enterprise Edition with a paid plan and a valid OpenAI API key as prerequisites. The default model is gpt-4o-mini and a self-hosted OpenAI-compatible endpoint can be supplied instead, and the docs note that in a self-hosted setup Captain only sends data to the model you choose. Captain has to be enabled in the Super Admin Console and then toggled on in the account's Premium Features."
        }
      },
      {
        "@type": "Question",
        "name": "What do Chatwoot's AI credits cover and how do they bill?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Every Captain action consumes 1 credit per message because a fixed model configuration is used, and the documented credit-consuming actions include assistant responses, Copilot lookups, editor actions such as rephrase, summarize, and suggest a reply, label suggestions, workflow model calls, and audio transcription. Paid cloud plans include 300 credits monthly on Startups, 500 on Business, and 800 on Enterprise, additional credits bill at $20 per 1,000, and purchased credits expire after 6 months and require an active subscription."
        }
      }
    ]
  }
]
```
