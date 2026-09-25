# Loops | MartechSignal review

Email marketing for SaaS: marketing, product, and transactional email in one tool

- Page: https://martechsignal.com/tools/loops/
- Category: Email Marketing
- Pricing: Freemium
- Open source: no
- Last verified: 2026-09-07

Loops is an email platform built for SaaS companies, covering marketing campaigns, product announcements, and transactional email from one dashboard, and deliberately nothing else: there is no SMS, no push, and no in-app messaging. Founded in 2022 by Chris Frantz and Adam Kaczmarek, it went through Y Combinator's W22 batch, and the site names Linear, Perplexity, Framer, Clerk, Reuters, Granola, and Sketch among its customers. Automation was rebuilt and renamed Workflows in May 2026, replacing the original loop builder: workflows trigger on contact property changes, new contacts, or external events, branch on contact properties, and pause on timers. Experiments, added in June 2025, handle split testing. Guardian, introduced in September 2025, runs pre-send checks that flag misplaced variables, missing button links, and missing fallbacks. Deliverability handling is documented rather than claimed: hard bounces and complaints are suppressed, temporary failures retried, and large sends rate-limited. One constraint surprises people: Loops does not accept custom HTML email. Content is built in the editor or in LMX, an XML-based markup, with a Components API that cascades edits into every email using the component; MJML, Emailify, and Email Love files can be imported. Developers get roughly 70 REST endpoints with an OpenAPI spec, official SDKs for JavaScript, Go, Nuxt, PHP, and Ruby, a CLI, webhooks, SMTP for transactional sending, and an MCP server so coding agents can read and write contacts, events, and content. LLM translation, added in January 2026, duplicates an email branch and translates it in one click. Pricing is contact-based: the free plan covers up to 1,000 subscribed contacts and 4,000 sends per rolling 30 days with all features included; paid plans add unlimited sends, no Loops branding, and 1,000 emails per second, with no per-seat fees and no published list prices.
