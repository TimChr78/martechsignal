# BillionMail review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- BillionMail
Re-check pending: pricing last verified 2026-09-07 (25 days ago).

## BillionMail review (2026): pricing, AI features, verdict

Open-source mail server, newsletter, and email marketing platform, fully self-hosted and free

Email Marketing · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit BillionMail →](https://www.billionmail.com)

[How we review](/methodology/) · No affiliate links

[Visit BillionMail →](https://www.billionmail.com)

## MartechSignal Score: 39/60

BillionMail is the full self-hosted mail stack: Postfix, Dovecot and a newsletter UI under AGPL, free with no cloud tier at all. Bring deliverability knowledge or pay someone who has it.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | Free under AGPL-3.0 with no paid tiers or cloud edition; optional deployment service at $98.9 per instance (the vendor pricing page: [vendor site](https://www.billionmail.com), verified 2026-09-07). |
| Feature depth | 6/10 | Mail server, newsletters and email marketing in one self-hosted stack cover the sending loop (vendor documentation: [vendor site](https://www.billionmail.com), verified 2026-09-28). |
| Integrations | 6/10 | Postfix, Dovecot, Rspamd, Roundcube and SMTP relays (SES, Mailgun, custom) plus REST and Send APIs (vendor documentation: [vendor site](https://www.billionmail.com), verified 2026-09-28). |
| AI capability | 5/10 | BYO-model template generation with six named model vendors and website profiling for brand-aware output (vendor documentation: [vendor site](https://www.billionmail.com), verified 2026-09-28). |
| Openness | 9/10 | AGPL-3.0 with the whole mail stack self-hosted (the source repository: [repository](https://github.com/Billionmail/BillionMail), verified 2026-09-28). |
| Operational maturity | 4/10 | Founded 2025 with an optional deployment service (vendor documentation: [vendor site](https://www.billionmail.com), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

BillionMail is a fully self-hosted email stack in one open-source project: a Linux mail server built from Postfix, Dovecot and Rspamd, plus newsletter and email marketing tooling (campaign tasks, an HTML and drag-and-drop template builder, contact management, open and click tracking) and Roundcube webmail, all AGPL-3.0 with no paid tiers. Install it on a Linux box (the documented minimum is 1 core, 1 GB RAM and 20 GB disk, with outbound port 25) and you own sending, deliverability setup and data end to end: DNS helpers walk you through SPF, DKIM, DMARC and PTR records, Let's Encrypt certificates come free, and an IP warmup mode caps your sending rate while a domain builds reputation. For marketing teams the pitch is independence from per-contact SaaS pricing; the trade is that you run the mail server, watch the blocklists and handle upgrades yourself. The API surface is practical: a management API with Swagger documentation and a Send API with single and batch endpoints authenticated by API key, for triggering sends from your own systems, plus outbound SMTP relay support for AWS SES, Mailgun or a custom relay when you would rather not deliver directly. AI template generation is real but modest: since v4.0 you can generate email templates from a prompt, with Anthropic, OpenAI, Gemini, DeepSeek, Grok and Kimi supported as configurable providers. Context worth weighing: the project started in February 2025 with a small core team, the last tagged release is v4.9 from December 2025 and the most recent commit landed in June 2026, so development has slowed sharply, and webhooks and journey automation are absent from the documented feature set. The homepage courts cold emailers with unlimited sending and no built-in speed limit, but the project's own framing is mail server plus newsletter plus campaigns. This assessment is based on the repository, the docs site and the release notes.

BillionMail homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI email template generation (BYO model: OpenAI, Anthropic, Gemini, DeepSeek, Grok, Kimi)
- AI website profiling for brand-aware templates
## Key Integrations

- Postfix
- Dovecot
- Rspamd
- Roundcube webmail
- SMTP relay (AWS SES, Mailgun, custom)
- REST management API with Swagger
- Send API (single and batch)
## Pricing

BillionMail is free to self-host under the AGPL-3.0 licence, paid plans start at $98.9/mo as of 2026-09.

Free and open source (AGPL-3.0), no paid tiers or cloud edition. Optional paid deployment service at $98.9 per instance.

## How to install

- Install script (docs quickstart): cd /opt && git clone https://github.com/aaPanel/BillionMail && cd BillionMail && bash install.sh. The clone URL still uses the old aaPanel path, which redirects to the current Billionmail org.
- Docker route (docs): cd /opt && git clone https://github.com/aaPanel/BillionMail && cd BillionMail && cp env_init .env && docker compose up -d. The docs literally print the command as docker compose up -d || docker-compose up -d to cover both Compose versions. The compose file runs Postfix, Dovecot, Rspamd, Roundcube, PostgreSQL 17, Redis and the billionmail/core panel container.
- Manage with the bm script: bm help for commands, bm default to print the access URL and credentials, bm update to upgrade, plus bm start, restart, status, stop, change-password, change-user and change-port. On the Docker install the docs use bash bm.sh default.
- Requirements per the docs: Linux only, on amd64 or arm64, with 1 core, 1 GB RAM and 20 GB disk as the minimum. Outbound port 25 must be open unless you use an SMTP relay; Postfix listens on 25, 465 and 587, and Dovecot serves IMAP on 143 and 993 and POP3 on 110 and 995.
- Change the defaults before exposing the panel: the admin login ships as billion/billion in env_init, and the docs print default database and Redis passwords.
- Keep in mind the default branch is dev and the README predates the shipped product, so prefer tagged releases and the docs site over the README when following setup steps.
## Best for

Technical teams and agencies that want to own their email infrastructure outright, send newsletters and campaigns from their own server with their own IPs, and accept deliverability work as part of the job.

## Not for

Teams that need marketing automation journeys, webhooks or a vendor to carry deliverability risk, buyers who require evidence of active development (no release since December 2025), and senders who cannot open outbound port 25 or run a mail server at all.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

BillionMail is two products in one container set. The base is a conventional Linux mail server: Postfix for SMTP, Dovecot for IMAP and POP, Rspamd for filtering, PostgreSQL and Redis underneath, Roundcube for webmail. On top sits the marketing layer the project exists for: campaign tasks with a from address, subject, recipient groups and template, an HTML plus drag-and-drop template editor, contact lists with CSV import, template variables, spintax for content variation, and open and click tracking that you can switch off globally or per campaign. Docs for all of it live at billionmail.com/start rather than in the README.

The README undersells the shipped product, and that is worth knowing when you evaluate: it still describes a future open-source mail server awaiting development, while the release notes show a working platform through v4.9 (December 2025) with retention policies, DKIM key-length options and tracking toggles. The docs site is the real reference. Conversely, a homepage section headed Cold Email Partner pitches unlimited sending with no built-in speed limit; that is the marketing-est sentence in the project, and the feature set around it (warmup-based rate limiting, DNS guidance, unsubscribe handling) is ordinary email infrastructure rather than a cold-outreach workflow.

Deliverability tooling is the practical reason to pick this over a plain sender. Domain setup covers A, MX, SPF, DKIM and DMARC with a PTR reminder and free Let's Encrypt certificates on port 80, the IP warmup system enforces sending-rate limits while reputation builds, and an SMTP relay option routes outbound mail through AWS SES, Mailgun or a custom relay, one relay per domain, when direct delivery is not viable. Security note from the docs: the default admin credentials in env_init are billion/billion, and the default database and Redis passwords are printed in the documentation, so changing them before exposure is not optional.

The AI story is narrower than the marketing implies, so here is exactly what is documented. AI email template generation arrived in v4.0: describe the email, get a template, with Anthropic, OpenAI, Gemini, DeepSeek, Grok and Kimi as configurable providers and a setup notice that blocks AI features until a model is configured. Release notes also describe website profiling to pull brand information from a domain. There is no documented send-time optimization, predictive sending or AI segmentation; scheduling is a plain send-time field, and timing quality comes from warmup and rate limits, not a model.

This assessment is based on the repository, the docs site and the release notes. The risk profile comes from cadence, not features: roughly 15 named contributors with four accounts producing most commits, no release since December 2025, and no commit since June 11, 2026. Also note the repository moved: the canonical repo is Billionmail/BillionMail, older aaPanel/BillionMail links redirect there, the default branch is dev, and the README still points at the old URLs.

## Verdict

A genuinely complete open-source mail server with a usable campaign layer on top, priced at zero and paid for in operations time. Judge the stalled commit cadence as seriously as the feature list.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ AGPL-3.0 licence with free self-hosting | ✗ Paid plans start at $98.9/mo |
| ✓ AI capabilities: AI email template generation (BYO model: OpenAI, Anthropic, Gemini, DeepSeek, Grok, Kimi) |  |
| ✓ Active public repository (15,815 GitHub stars counted at last check) |  |
| ✓ Native integrations include Postfix, Dovecot, Rspamd (7 listed) |  |

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is BillionMail?**
BillionMail: Open-source mail server, newsletter, and email marketing platform, fully self-hosted and free. BillionMail ships with AI email template generation (BYO model: OpenAI, Anthropic, Gemini, DeepSeek, Grok, Kimi). The public repository carries 15,815 stars.

**How much does BillionMail cost?**
BillionMail has a free tier; paid plans start at $98.9/mo. Free and open source (AGPL-3.0), no paid tiers or cloud edition. Optional paid deployment service at $98.9 per instance. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is BillionMail a good self-hosted Email Marketing tool in 2026?**
A genuinely complete open-source mail server with a usable campaign layer on top, priced at zero and paid for in operations time. Judge the stalled commit cadence as seriously as the feature list.

**Is BillionMail really free, and is there a paid plan?**
The software is AGPL-3.0 with no Pro, Enterprise or cloud edition: there is no pricing page because every feature ships in the single free project. The only paid offering is a done-for-you deployment package listed on the support page at $98.9 per instance with seven days of support. Your real costs are infrastructure and deliverability: a server with outbound port 25, DNS records, warmup time and blocklist monitoring.

**BillionMail vs Listmonk: which self-hosted sender should you pick?**
Listmonk is a lean newsletter and mailing-list manager: one Go binary, PostgreSQL, strong at lists and campaign sending, but it is not a mail server, so you bring your own SMTP provider. BillionMail is the whole stack: Postfix, Dovecot and Rspamd plus campaigns, contacts, templates, DNS and DMARC tooling, IP warmup and webmail, so you can deliver directly from your own IPs. Pick Listmonk for simplicity and a long, steady release history; pick BillionMail when owning the mail server itself, mailboxes included, is the point and you accept a younger project whose development has slowed.

**Does BillionMail have AI features?**
One documented one: AI email template generation, added in v4.0, where you describe the email and the editor produces a template, with Anthropic, OpenAI, Gemini, DeepSeek, Grok and Kimi as configurable providers, plus website profiling that pulls brand details from a domain. There is no documented send-time optimization or predictive sending; scheduling is a plain send-time field, and timing quality comes from warmup and rate limits rather than a model. You must configure your own provider key, since AI features stay disabled until a model is set up.

## Similar Tools

- [Notifuse](/tools/notifuse/): Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations
- [Listmonk](/tools/listmonk/): Open-source self-hosted newsletter and mailing list manager with a fast Go backend
- [Resend](/tools/resend/): Developer-first email API built around React Email, batch sending, and agent tooling
- [React Email Editor](/tools/react-email-editor/): Drag-n-Drop Email Editor Component for React.js
## Related reading

- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [OpenAI Isn't Building Ads. It's Building Agents That Spend Money Without You.](/blog/openai-agent-ads-spending-without-you/)
- [Fifty days of open-source MarTech, audited](/blog/oss-martech-50-day-checkin/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Email Marketing](/categories/email-marketing/)
- **GitHub:** ★ 15815
- **Founded:** 2025
- **API:** Yes
- **Repository checked:** 2026-10-02
- **Page updated:** 2026-09-07

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Email Marketing Tools →](/categories/email-marketing/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
