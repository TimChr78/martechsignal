# Email Marketing Bible | MartechSignal review

55K-word email marketing skill with 908 sources, 19 playbooks, and ESP control via MCP

- Page: https://martechsignal.com/tools/email-marketing-bible/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-08-28

Email Marketing Bible is what happens when someone who ran an email SaaS (SmartrMail, ~28,000 customers, 6 billion emails sent, acquired in 2022) distills everything into a 55,000-word skill file. It's not a prompt pack. It's a knowledge base with 908 cited sources, 19 industry playbooks, and 47 curated email designs. Install it and your AI agent stops guessing about email. It knows what a good open rate is for your vertical, why your emails land in spam, and which flow to build first for a DTC skincare brand doing $2M/year.

The practical capabilities: it builds welcome, cart, post-purchase, and win-back flows from a prompt, then reviews exits, timing, and copy before anything goes live. It audits your ESP setup for missing flows, broken segments, and deliverability problems. It drafts copy using proven frameworks (PAS, AIDA, BAB) and strips AI tells before send. The anti-slop rules are explicit: no "we hope this email finds you well, " no generic personalization, no AI voice. It designs emails in MJML or React Email with dark-mode and mobile checks. And it drives your ESP through MCP connectors for Klaviyo, Mailchimp, Resend, beehiiv, Omnisend, and nitrosend, with a hard rule that nothing sends without your approval.

Installation is one git clone into ~/.claude/skills/. It works wherever the skill format is read: Claude Code, Claude Desktop, and MCP-compatible agents. The compliance gate covers GDPR, CAN-SPAM, CASL, CCPA, and the Australian Spam Act as a decision gate before any send. That's not a feature list item. It's a workflow step that blocks non-compliant campaigns.

Against a SaaS tool like Klaviyo or Mailchimp, this doesn't replace the ESP. It makes the AI operating the ESP competent. Against hiring an email consultant, it's cheaper and available at 2am. The 19 industry playbooks mean a nonprofit gets different advice than a B2B SaaS company. The limitation is that it's a knowledge layer, not an execution platform. You still need an ESP and an agent runtime. But if you're already running Claude Code and an ESP, this is the difference between your agent sending generic slop and sending email that actually converts.
