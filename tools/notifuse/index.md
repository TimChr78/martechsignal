# Notifuse | MartechSignal review

Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations

- Page: https://martechsignal.com/tools/notifuse/
- Category: Email Marketing
- Pricing: Open Source
- Open source: yes (AGPL-3.0)
- Last verified: 2026-08-28

Notifuse is a self-hosted email platform for newsletters, marketing campaigns, and transactional email. It's written in Go with a React console, and it aims at the gap between bare-bones senders like Listmonk and full SaaS suites like Mailchimp: you get a drag-and-drop MJML builder, Liquid templating, automations, and a transactional API, while your data stays on your own server. It ships with support for seven sending providers: Amazon SES, Postmark, SendGrid, Mailgun, Mailjet, SparkPost, and plain SMTP.

The AI angle is real but limited, and I'd rather be straight about that. Notifuse has no proprietary AI of its own. Instead it integrates with Anthropic, OpenAI, and Google Gemini to generate email copy and blog posts inside the editor, with Firecrawl for pulling web content into prompts. There's no predictive send-time optimization and no AI segmentation. If a vendor pitch leads with AI, this isn't it. What it does have is solid mechanics: A/B testing on subject lines and content, dynamic segments built from contact properties and activity, and automation flows with 10 node types that stop automatically when a contact replies.

Self-hosting is free under AGPL-3.0 with all features included. Notifuse Cloud starts at $19/month (Lite, 2,500 active contacts) and covers 2,500 active contacts at that entry price with unlimited sends and BYO ESP. The pricing model is the interesting part: every plan includes unlimited email sends because you bring your own ESP. With Amazon SES at roughly $0.10 per 1,000 emails, 50,000 sends costs about $5 on top of the subscription. Contacts inactive for 30 days don't count toward limits, unlike Mailchimp or Klaviyo, which bill every stored contact. No overage fees; if you exceed a tier you get moved up on the next cycle.

The closest comparison in this directory is Listmonk. Listmonk is lighter and faster to run, but it has no visual builder, no automation workflows, and a thinner API. Mautic is the heavier option with true marketing automation and lead scoring, and correspondingly more to maintain. Notifuse sits between the two. BillionMail covers similar ground with its own built-in mail server, while Notifuse assumes you'd rather delegate delivery to a real ESP.

Who should skip it: teams that want deliverability fully managed for them, or anyone who picked up a Mailchimp habit of leaning on built-in AI for everything. You still need someone comfortable configuring DKIM, SPF, and an SES account. For developers, agencies running client workspaces (multi-tenant is built in), and anyone tired of per-email pricing, it's one of the better options in the open-source email space right now.
