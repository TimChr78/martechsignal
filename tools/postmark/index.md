# Postmark | MartechSignal review

Transactional email API with separated message streams, an MCP server, and published delivery numbers

- Page: https://martechsignal.com/tools/postmark/
- Category: Email Marketing
- Pricing: Freemium
- Open source: no
- Last verified: 2026-09-07

Postmark is a transactional email service owned by ActiveCampaign, which acquired it from Wildbit in May 2022 and kept it as a standalone product: the site footer still reads Made with heart at ActiveCampaign, and the company's own FAQ says there is no plan to roll Postmark into ActiveCampaign's marketing platform. Focus is the product. Postmark runs parallel but separate sending infrastructure for transactional and broadcast traffic and states that the two never intersect, including IP ranges, so a marketing blast cannot degrade password-reset deliverability. Servers expose message streams, three by default (outbound transactional, broadcasts, inbound) and up to ten per server, with inbound processing reserved for Pro and Platform plans. Speed claims are specific rather than vague: up to 4x faster than the competition, and a March 2026 post details the completed migration from PowerMTA to the open-source KumoMTA, with average queue times of about 1.2 seconds to Gmail and 6.3 seconds to Apple. Full message content and history is stored for 45 days by default, adjustable from 7 to 365 days with the retention add-on, while aggregate statistics are kept indefinitely. Pricing was restructured in August 2025: Free (100 emails a month, no overages), then Basic $15, Pro $16.50, and Platform $18 a month, all starting at 10,000 emails, with published volume tiers up to 1.5 million messages and no annual billing. The REST API is the same well-documented surface as ever, with official libraries for seven supported languages plus WordPress, Craft, and Zapier options. 2026 shipped a bulk email API (500 messages per request, 50MB payloads), webhooks that verify themselves, IP allowlisting, an MCP server with 24 tools, and agent skills. What Postmark does not do matters as much: no list management, no campaign builder, no automation. It pairs with a marketing ESP rather than replacing one.
