# OpenOutreach review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- OpenOutreach
Re-check pending: pricing last verified 2026-09-07 (28 days ago).

## OpenOutreach review (2026): pricing, AI features, verdict

Open-source AI lead finder: describe your product and it finds and qualifies the leads

Email Marketing · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit OpenOutreach →](https://openoutreach.app)

[How we review](/methodology/) · No affiliate links

[Visit OpenOutreach →](https://openoutreach.app)

## MartechSignal Score: 39/60

OpenOutreach is the rare lead tool you can read before you run: GPL, self-hosted, and its qualification reasoning is written down per lead. Budget for your own LLM keys and BetterContact credits.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 7/10 | The software is free (GPLv3) and the run costs are stated plainly: your own LLM keys and mailbox plus BetterContact credits at one credit per verified email (the vendor pricing page: [vendor site](https://openoutreach.app), verified 2026-09-07). |
| Feature depth | 6/10 | LLM keyword generation, per-lead qualification with written reasons and Gaussian Process learning over verdicts make a focused outbound tool, not a suite (vendor documentation: [vendor site](https://openoutreach.app), verified 2026-09-28). |
| Integrations | 5/10 | BetterContact, OpenAI, Anthropic, OpenAI-compatible endpoints, SMTP/IMAP, Google Workspace and Instantly CSV export are documented (vendor documentation: [vendor site](https://openoutreach.app), verified 2026-09-28). |
| AI capability | 8/10 | LLM qualification with a written reason per lead and model learning over your verdicts is agentic in the honest sense (vendor documentation: [vendor site](https://openoutreach.app), verified 2026-09-28). |
| Openness | 9/10 | GPLv3, self-hosted, and you bring your own keys so no usage is locked to a vendor (the source repository: [repository](https://github.com/eracle/OpenOutreach), verified 2026-09-28). |
| Operational maturity | 4/10 | A 3.0k-star self-hosted project with no company behind it; operations are yours (vendor documentation: [vendor site](https://openoutreach.app), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

OpenOutreach is an open-source AI agent for B2B lead generation, and it inverts the usual cold-email workflow: you do not bring a list. You describe your product and your target market, and the agent finds the people who fit, writes a reason for each one, and emails them from your own mailbox. It is a self-hosted Python CLI installed with two commands, uv tool install openoutreach and then openoutreach, organized as three packages on one Django registry and database: OpenOutFind for discovery, qualification, and CRM, OpenOutSend for the outreach agent, mailbox, and send guards, and OpenOutreach as the wizard that ties them together. Lead discovery runs on BetterContact's Lead Finder, a licensed data provider, with a confidence gate that rations the paid email lookups, which cost one credit per verified work email; a free account comes with 40 credits and no card required. The AI work is split into named steps: an LLM turns your product description into search keywords, another pass qualifies candidates against your ICP and writes the plain-language reason (there is deliberately no score column), and the agent writes each opener while send guards handle the sending window, daily cap, and pacing. A Gaussian Process over profile embeddings that learns from your verdicts is documented as an active experiment that has not been shown to beat random ordering. LLM access is verified at the prompt and accepts OpenAI, Anthropic, or any OpenAI-compatible endpoint; any SMTP or IMAP mailbox with an app password works, and Google Workspace works out of the box. A Claude Code plugin is included, and the same logic ships as a skill for Codex or Cursor. CSV export is shaped for Instantly and Smartlead importers with no column mapping. GPLv3, around 3,157 GitHub stars, funded by affiliate links rather than subscriptions.

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

OpenOutreach's differentiator is the verdict, not the volume: every lead comes back with a written reason in plain language, and the README states there is no score column by design. That is a real advantage if you want to audit why someone was contacted, and a real cost if you want to sort thousands of rows by fit. Researched from the repository and its docs. Not a hands-on review.

The cost structure is unusual and worth understanding before you start. The tool is free, but discovery runs on BetterContact's paid Lead Finder at one credit per verified work email, with 40 free credits on a no-card account. A confidence gate rations those paid lookups, and the affiliate link to that provider is the project's only stated revenue alongside GitHub Sponsors. Budget in credits, not subscription fees.

The compliance surface is deliberately narrow. The README claims zero platform-ToS exposure because it is browserless and holds no social-network accounts, and the legal notice puts data-controller duties and sender responsibility on you, stating use at your own risk with no liability assumed. Self-hosting means your domain carries the sending reputation, so SPF, DKIM, and warm-up discipline still decide whether any of this works.

The AI layer is documented with unusual honesty. The Gaussian Process model over profile embeddings, which learns from your accept and reject verdicts, is labeled an active experiment and not shown to beat random ordering. Most vendors would have shipped that as a headline feature.

## Verdict

A different shape of cold-outreach tool: lead finding with written reasons instead of a list to upload, priced in data-provider credits rather than seats, and candid about which parts are still experimental.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ GPL-3.0 licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: LLM keyword generation from your product description |  |
| ✓ Active public repository (3,157 GitHub stars counted at last check) |  |
| ✓ Native integrations include BetterContact (Lead Finder), OpenAI, Anthropic (9 listed) |  |

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is OpenOutreach?**
OpenOutreach: Open-source AI lead finder: describe your product and it finds and qualifies the leads. OpenOutreach ships with LLM keyword generation from your product description. The public repository carries 3,157 stars.

**How much does OpenOutreach cost?**
OpenOutreach is open source - GPL-3.0 licensed and free to self-host; the public repository carries 3,157 stars; native integrations cover BetterContact (Lead Finder), OpenAI, Anthropic. You pay in server time and maintenance, not licences.

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

## Similar Tools

- [BillionMail](/tools/billionmail/): Open-source mail server, newsletter, and email marketing platform, fully self-hosted and free
- [Notifuse](/tools/notifuse/): Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations
- [Resend](/tools/resend/): Developer-first email API built around React Email, batch sending, and agent tooling
- [Eve Marketing Team Template](/tools/eve-marketing-team/): Open-source team of marketing agents on eve: lead, content, social, SEO, email
- [Postmark](/tools/postmark/): Transactional email API with separated message streams, an MCP server, and published delivery numbers
## Related reading

- [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/)
- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
## Also featured in

- [Best AI Email Marketing tools (2026): 8 compared](/best/ai-email-marketing-tools/) — Best for email marketing teams that want agent-written openers and can host it themselves, with a free starting tier.
- [Best Open-Source Marketing Tools (2026): 8 compared](/best/open-source-marketing-tools/) — Email marketing teams that want agent-written openers and self-hosting
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Email Marketing](/categories/email-marketing/)
- **GitHub:** ★ 3157
- **API:** No
- **Repository checked:** 2026-10-05
- **Page updated:** 2026-09-07

Related guides: [Ai Email Marketing Tools](/best/ai-email-marketing-tools/) · [Open Source Marketing Tools](/best/open-source-marketing-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Email Marketing Tools →](/categories/email-marketing/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
