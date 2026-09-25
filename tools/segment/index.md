# Twilio Segment | MartechSignal review

Customer data platform for collecting, unifying, and activating customer data

- Page: https://martechsignal.com/tools/segment/
- Category: Personalization & CDP
- Pricing: Freemium
- Open source: no
- Last verified: 2026-09-06

Twilio Segment is a developer-first customer data platform: SDKs and server libraries send events to one API, and Segment routes them to analytics tools, ad platforms, and warehouses. Acquired by Twilio for $3.2 billion in 2020, it is now documented on twilio.com; segment.com's docs and pricing paths redirect there. The getting-started guide runs six steps, from a JavaScript, iOS, or PHP quickstart to a full install built on six tracking calls: Identify, Track, Page, Screen, Group, Alias. Web installs use the analytics.js snippet (version 5.2.1, loaded from cdn.segment.com) or the @segment/analytics-next npm package.

The product splits into layers with real gating between them. Connections is the pipeline: sources with a write key, a docs catalog listing 452 destinations, Reverse ETL from BigQuery, Databricks, Postgres, Redshift, and Snowflake, and warehouse syncs. Protocols is the data-quality add-on, Business tier only: a tracking plan, violation reports, enforcement that blocks non-conforming events, and transformations. Unify, formerly Profiles, adds identity resolution and a Profile API; Engage adds audiences, computed traits, SQL traits, and activation over SMS, email, and WhatsApp. One gotcha the docs state plainly: a source with no destinations gets disabled after 14 days.

Pricing is MTU-based. Free covers 1,000 monthly tracked users and 2 sources. Team starts at $120 per month for 10,000 MTUs with unlimited sources, 1 million reverse ETL records, and overages of $10 to $12 per additional 1,000 MTUs. Business is custom, with Protocols, Unify, and Engage above it. Twilio labels the numbers current as of August 2026.

AI reached general availability in June 2025: Predictions with four models (likelihood to purchase, predicted lifetime value, likelihood to churn, custom goals), Predictive Audiences, Recommendations, Generative Audiences from natural-language prompts, and Functions Co-Pilot. Twilio's terms replaced OpenAI with Anthropic's Claude as the model provider for the generative features in August 2025. Documentation is agent-friendly too: every page ships a markdown version, Twilio publishes an MCP endpoint, and llms.txt sits at the root.
