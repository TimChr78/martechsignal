# OpenOutreach review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 7/10 | The software is free (GPLv3) and the run costs are stated plainly: your own LLM keys and mailbox plus BetterContact credits at one credit per verified email (the vendor pricing page: [pricing page](https://openoutreach.app), verified 2026-09-07). |
| Feature depth | 6/10 | LLM keyword generation, per-lead qualification with written reasons and Gaussian Process learning over verdicts make a focused outbound tool, not a suite (vendor documentation: [vendor site](https://openoutreach.app), verified 2026-09-28). |
| Integrations | 5/10 | BetterContact, OpenAI, Anthropic, OpenAI-compatible endpoints, SMTP/IMAP, Google Workspace and Instantly CSV export are documented (vendor documentation: [vendor site](https://openoutreach.app), verified 2026-09-28). |
| AI capability | 8/10 | LLM qualification with a written reason per lead and model learning over your verdicts is agentic in the honest sense (vendor documentation: [vendor site](https://openoutreach.app), verified 2026-09-28). |
| Openness | 9/10 | GPLv3, self-hosted, 3.0k GitHub stars, and you bring your own keys so no usage is locked to a vendor (the source repository: [repository](eracle/OpenOutreach), verified 2026-09-28). |
| Operational maturity | 4/10 | A 3.0k-star self-hosted project with no company behind it; operations are yours (vendor documentation: [vendor site](https://openoutreach.app), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| &#10003; GPL-3.0 licence with free self-hosting | &#10007; No hands-on test - this assessment is based on vendor documentation and the public repository |
| &#10003; AI capabilities: LLM keyword generation from your product description |  |
| &#10003; Active public repository (2,952 GitHub stars counted at last check) |  |
| &#10003; Native integrations include BetterContact (Lead Finder), OpenAI, Anthropic (9 listed) |  |

**What is OpenOutreach?**
Open-source AI lead finder: describe your product and it finds and qualifies the leads. It ships with LLM keyword generation from your product description, 2,952 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does OpenOutreach cost?**
OpenOutreach is open source - GPL-3.0 licensed and free to self-host; the public repository carries 2,952 stars; native integrations cover BetterContact (Lead Finder), OpenAI, Anthropic. You pay in server time and maintenance, not licences.

**Is OpenOutreach a good self-hosted Email Marketing tool in 2026?**
A different shape of cold-outreach tool: lead finding with written reasons instead of a list to upload, priced in data-provider credits rather than seats, and candid about which parts are still experimental.

**Is OpenOutreach an Instantly or Smartlead alternative?**
It solves the other half of the problem. OpenOutreach finds and qualifies leads and can send from your own mailbox, but it also exports a CSV with columns already shaped for Instantly and Smartlead importers (email, first_name, last_name, company, title, website, linkedin_url, reason, lead_id, qualified_at) with no column mapping. A common pattern is OpenOutreach for sourcing and a dedicated sequencer for sending at volume.

**Is OpenOutreach safe for cold email and GDPR?**
The project is explicit that the obligations stay with you: the legal notice covers data-controller duties and sender responsibility and states use at your own risk with no liability assumed. The README argues the tool has zero platform-ToS surface because it is browserless and holds no social-network accounts. Self-hosting keeps prospect data on your servers, which is what makes it interesting for EU teams, but lawful basis, suppression lists, and warm-up are still yours to manage.

**How does OpenOutreach decide which leads to qualify next?**
With a Gaussian Process over 384 dimensional FastEmbed profile embeddings. When negative verdicts outnumber positive ones it exploits, taking the profile with the highest predicted fit probability; otherwise it explores using a BALD score, which favours profiles the model is most uncertain about. Passing qualification gates the paid email lookup. Cold start is seeded with synthetic ideal profiles that are flagged as synthetic and never contacted or exported. The README is candid that this loop is an active experiment not yet shown to beat picking at random.

**What does an OpenOutreach export look like?**
One CSV written to stdout with email, first_name, last_name, company, title, website, linkedin_url, reason, lead_id, and qualified_at. There is no score column by design: the written reason carries the qualification instead. The shape matches Instantly and Smartlead importers without column mapping, so the handoff is a file redirect rather than a transformation. In Docker you get a container that runs one job and exits with no open ports, which suits a scheduled pipeline rather than a dashboard.

- **Pricing:** Open Source
- **Category:** [Email Marketing](/categories/email-marketing/)
- **GitHub:** ★ 2952
- **API:** No
- **Last verified:** 2026-09-07

**Verdict:** OpenOutreach is a tool in Email Marketing with free and open source. The catalog documents 5 AI features, 9 integrations and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

BillionMail

Open-source mail server, newsletter, and email marketing platform, fully self-hosted and free

Notifuse

Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations

Resend

Developer-first email API built around React Email, batch sending, and agent tooling

Eve Marketing Team Template

Open-source team of marketing agents on eve: lead, content, social, SEO, email

Postmark

Transactional email API with separated message streams, an MCP server, and published delivery numbers

[More Email Marketing Tools →](/categories/email-marketing/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- OpenOutreach
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## OpenOutreach review (2026): pricing, AI features, verdict

Open-source AI lead finder: describe your product and it finds and qualifies the leads

Email Marketing · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[Visit OpenOutreach &#8594;](https://openoutreach.app)

[How we review](/methodology/) · No affiliate links

[Visit OpenOutreach &#8594;](https://openoutreach.app)

## MartechSignal Score: 39/60

OpenOutreach is the rare lead tool you can read before you run: GPL, self-hosted, and its qualification reasoning is written down per lead. Budget for your own LLM keys and BetterContact credits.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

OpenOutreach is an open-source AI agent for B2B lead generation, and it inverts the usual cold-email workflow: you do not bring a list. You describe your product and your target market, and the agent finds the people who fit, writes a reason for each one, and emails them from your own mailbox. It is a self-hosted Python CLI installed with two commands, uv tool install openoutreach and then openoutreach, organized as three packages on one Django registry and database: OpenOutFind for discovery, qualification, and CRM, OpenOutSend for the outreach agent, mailbox, and send guards, and OpenOutreach as the wizard that ties them together. Lead discovery runs on BetterContact&#x27;s Lead Finder, a licensed data provider, with a confidence gate that rations the paid email lookups, which cost one credit per verified work email; a free account comes with 40 credits and no card required. The AI work is split into named steps: an LLM turns your product description into search keywords, another pass qualifies candidates against your ICP and writes the plain-language reason (there is deliberately no score column), and the agent writes each opener while send guards handle the sending window, daily cap, and pacing. A Gaussian Process over profile embeddings that learns from your verdicts is documented as an active experiment that has not been shown to beat random ordering. LLM access is verified at the prompt and accepts OpenAI, Anthropic, or any OpenAI-compatible endpoint; any SMTP or IMAP mailbox with an app password works, and Google Workspace works out of the box. A Claude Code plugin is included, and the same logic ships as a skill for Codex or Cursor. CSV export is shaped for Instantly and Smartlead importers with no column mapping. GPLv3, around 2,900 GitHub stars, funded by affiliate links rather than subscriptions.

OpenOutreach homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- LLM keyword generation from your product description
- LLM qualification with a written reason per lead
- Gaussian Process learning over verdicts (experimental)
- Agent-written openers
- Confidence gate on paid email lookups
## Key Integrations

- BetterContact (Lead Finder)
- OpenAI
- Anthropic
- OpenAI-compatible endpoints
- SMTP/IMAP mailboxes
- Google Workspace
- Instantly (CSV export)
- Smartlead (CSV export)
- Claude Code
## Pricing

OpenOutreach is free to self-host under the GPL-3.0 licence.

Free, GPLv3, self-hosted. You pay your own LLM keys and mailbox, plus BetterContact credits for discovery (1 credit per verified work email; free account includes 40 credits, no card)

## How to install

- Install the CLI with uv tool install openoutreach, then run openoutreach to start the wizard. State lives in ~/.openoutreach.
- Describe your product and target from files so you are not re-typing them: openoutreach init --product-docs product.md --target target.md.
- Find before you send: openoutreach find 10 lists candidates with written reasons, openoutreach find 10 emails spends credits on verified addresses, and openoutreach send 5 mails them. openoutreach status and openoutreach run 5 cover the rest of the verb set.
- Configure providers when prompted: OpenAI, Anthropic, or any OpenAI-compatible endpoint for the LLM, and any SMTP/IMAP mailbox with an app password for sending, with Google Workspace working out of the box. Headless setups name missing OPENOUTFIND_* and OUTSEND_* variables instead of prompting.
- Optional: install as a Claude Code plugin with /plugin marketplace add eracle/OpenOutreach then /plugin install openoutreach@openoutreach, or point Codex or Cursor at skills/find-leads/SKILL.md. Server deploys have a Docker Compose file (local.yml) and an image on GitHub Container Registry.
## Best for

Technical founders and small teams that want to generate qualified outbound lists from a product description, keep prospect data on their own infrastructure, and export straight into Instantly or Smartlead.

## Not for

Teams that already hold lead lists and only need sequencing, anyone who wants a graphical interface, and senders unwilling to own SPF, DKIM, warm-up, and data-controller duties.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

OpenOutreach&#x27;s differentiator is the verdict, not the volume: every lead comes back with a written reason in plain language, and the README states there is no score column by design. That is a real advantage if you want to audit why someone was contacted, and a real cost if you want to sort thousands of rows by fit. Researched from the repository and its docs. Not a hands-on review.

The cost structure is unusual and worth understanding before you start. The tool is free, but discovery runs on BetterContact&#x27;s paid Lead Finder at one credit per verified work email, with 40 free credits on a no-card account. A confidence gate rations those paid lookups, and the affiliate link to that provider is the project&#x27;s only stated revenue alongside GitHub Sponsors. Budget in credits, not subscription fees.

The compliance surface is deliberately narrow. The README claims zero platform-ToS exposure because it is browserless and holds no social-network accounts, and the legal notice puts data-controller duties and sender responsibility on you, stating use at your own risk with no liability assumed. Self-hosting means your domain carries the sending reputation, so SPF, DKIM, and warm-up discipline still decide whether any of this works.

The AI layer is documented with unusual honesty. The Gaussian Process model over profile embeddings, which learns from your accept and reject verdicts, is labeled an active experiment and not shown to beat random ordering. Most vendors would have shipped that as a headline feature.

## Verdict

A different shape of cold-outreach tool: lead finding with written reasons instead of a list to upload, priced in data-provider credits rather than seats, and candid about which parts are still experimental.

## Pros and cons

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source AI lead finder: describe your product and it finds and qualifies the leads. It ships with LLM keyword generation from your product description, 2,952 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

OpenOutreach is open source - GPL-3.0 licensed and free to self-host; the public repository carries 2,952 stars; native integrations cover BetterContact (Lead Finder), OpenAI, Anthropic. You pay in server time and maintenance, not licences.

A different shape of cold-outreach tool: lead finding with written reasons instead of a list to upload, priced in data-provider credits rather than seats, and candid about which parts are still experimental.

It solves the other half of the problem. OpenOutreach finds and qualifies leads and can send from your own mailbox, but it also exports a CSV with columns already shaped for Instantly and Smartlead importers (email, first_name, last_name, company, title, website, linkedin_url, reason, lead_id, qualified_at) with no column mapping. A common pattern is OpenOutreach for sourcing and a dedicated sequencer for sending at volume.

The project is explicit that the obligations stay with you: the legal notice covers data-controller duties and sender responsibility and states use at your own risk with no liability assumed. The README argues the tool has zero platform-ToS surface because it is browserless and holds no social-network accounts. Self-hosting keeps prospect data on your servers, which is what makes it interesting for EU teams, but lawful basis, suppression lists, and warm-up are still yours to manage.

With a Gaussian Process over 384 dimensional FastEmbed profile embeddings. When negative verdicts outnumber positive ones it exploits, taking the profile with the highest predicted fit probability; otherwise it explores using a BALD score, which favours profiles the model is most uncertain about. Passing qualification gates the paid email lookup. Cold start is seeded with synthetic ideal profiles that are flagged as synthetic and never contacted or exported. The README is candid that this loop is an active experiment not yet shown to beat picking at random.

One CSV written to stdout with email, first_name, last_name, company, title, website, linkedin_url, reason, lead_id, and qualified_at. There is no score column by design: the written reason carries the qualification instead. The shape matches Instantly and Smartlead importers without column mapping, so the handoff is a file redirect rather than a transformation. In Docker you get a container that runs one job and exits with no open ports, which suits a scheduled pipeline rather than a dashboard.

## Similar Tools

## Related reading

- [OpenAI Isn't Building Ads. It's Building Agents That Spend Money Without You.](/blog/openai-agent-ads-spending-without-you/)
- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
- [The AI-search funnel map GA4 won't give you](/blog/ai-search-funnel-map-ga4-wont-give-you/)
## Also featured in

- [Best AI Email Marketing tools (2026): 8 compared](/best/ai-email-marketing-tools/) &mdash; Best for email marketing teams that want agent-written openers and can host it themselves, with a free starting tier.
- [Best Open-Source Marketing Tools (2026): 8 compared](/best/open-source-marketing-tools/) &mdash; Email marketing teams that want agent-written openers and self-hosting
### Quick Facts

Related guides: [Ai Email Marketing Tools](/best/ai-email-marketing-tools/) · [Open Source Marketing Tools](/best/open-source-marketing-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/openoutreach/#app",
    "name": "OpenOutreach",
    "description": "Open-source AI lead finder: describe your product and it finds and qualifies the leads",
    "image": "https://martechsignal.com/og/tools/openoutreach.png",
    "url": "https://martechsignal.com/tools/openoutreach/",
    "sameAs": [
      "https://openoutreach.app"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/openoutreach/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-26",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://openoutreach.app",
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
        "name": "Email Marketing",
        "item": "https://martechsignal.com/categories/email-marketing/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "OpenOutreach",
        "item": "https://martechsignal.com/tools/openoutreach/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is OpenOutreach?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source AI lead finder: describe your product and it finds and qualifies the leads. It ships with LLM keyword generation from your product description, 2,952 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does OpenOutreach cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "OpenOutreach is open source - GPL-3.0 licensed and free to self-host; the public repository carries 2,952 stars; native integrations cover BetterContact (Lead Finder), OpenAI, Anthropic. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is OpenOutreach a good self-hosted Email Marketing tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A different shape of cold-outreach tool: lead finding with written reasons instead of a list to upload, priced in data-provider credits rather than seats, and candid about which parts are still experimental."
        }
      },
      {
        "@type": "Question",
        "name": "Is OpenOutreach an Instantly or Smartlead alternative?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "It solves the other half of the problem. OpenOutreach finds and qualifies leads and can send from your own mailbox, but it also exports a CSV with columns already shaped for Instantly and Smartlead importers (email, first_name, last_name, company, title, website, linkedin_url, reason, lead_id, qualified_at) with no column mapping. A common pattern is OpenOutreach for sourcing and a dedicated sequencer for sending at volume."
        }
      },
      {
        "@type": "Question",
        "name": "Is OpenOutreach safe for cold email and GDPR?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The project is explicit that the obligations stay with you: the legal notice covers data-controller duties and sender responsibility and states use at your own risk with no liability assumed. The README argues the tool has zero platform-ToS surface because it is browserless and holds no social-network accounts. Self-hosting keeps prospect data on your servers, which is what makes it interesting for EU teams, but lawful basis, suppression lists, and warm-up are still yours to manage."
        }
      },
      {
        "@type": "Question",
        "name": "How does OpenOutreach decide which leads to qualify next?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "With a Gaussian Process over 384 dimensional FastEmbed profile embeddings. When negative verdicts outnumber positive ones it exploits, taking the profile with the highest predicted fit probability; otherwise it explores using a BALD score, which favours profiles the model is most uncertain about. Passing qualification gates the paid email lookup. Cold start is seeded with synthetic ideal profiles that are flagged as synthetic and never contacted or exported. The README is candid that this loop is an active experiment not yet shown to beat picking at random."
        }
      },
      {
        "@type": "Question",
        "name": "What does an OpenOutreach export look like?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "One CSV written to stdout with email, first_name, last_name, company, title, website, linkedin_url, reason, lead_id, and qualified_at. There is no score column by design: the written reason carries the qualification instead. The shape matches Instantly and Smartlead importers without column mapping, so the handoff is a file redirect rather than a transformation. In Docker you get a container that runs one job and exits with no open ports, which suits a scheduled pipeline rather than a dashboard."
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
    "reviewBody": "OpenOutreach is the rare lead tool you can read before you run: GPL, self-hosted, and its qualification reasoning is written down per lead. Budget for your own LLM keys and BetterContact credits.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/openoutreach/#app",
      "name": "OpenOutreach",
      "url": "https://martechsignal.com/tools/openoutreach/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 39,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
