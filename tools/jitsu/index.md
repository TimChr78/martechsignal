# Jitsu | MartechSignal review

Open-source Segment alternative for event capture and warehouse-first data pipelines

- Page: https://martechsignal.com/tools/jitsu/
- Category: Personalization & CDP
- Pricing: Freemium
- Open source: yes (MIT)
- Last verified: 2026-09-25

Jitsu is an open-source event collection and data pipeline platform, MIT licensed, positioned as a Segment alternative with 5,091 stars on GitHub. It captures events from web, mobile, and server code through an HTML snippet, JavaScript and npm packages, React and React Native SDKs, iOS and Android SDKs, an HTTP API, a pixel API, and a Segment proxy, then routes them to warehouses and SaaS tools. The destination catalog covers BigQuery, Snowflake, Redshift, Postgres, and ClickHouse for storage, and Google Analytics 4, Google Ads, HubSpot, Salesforce, Mixpanel, PostHog, Amplitude, SendGrid, Resend, Hotjar, Microsoft Clarity, and webhooks downstream. Jitsu Functions run in a JavaScript runtime with access to npm packages and key-value storage, so events can be filtered, enriched, or rewritten before delivery. Other documented features include identity stitching, user profiles, sessions, deduplication, schema management, live event debugging, event backups, and a provisioned ClickHouse option.

Billing counts active events, meaning events delivered to at least one destination. Captured events are always free, and a filtering function can drop noise before it counts. The free cloud plan includes 200,000 active events a month and one daily active sync. Business at USD 99 a month includes 2 million active events, then USD 40 per additional million, plus five monthly active syncs at USD 20 each after that. Enterprise is custom. Self-hosting the MIT-licensed code is free with no usage limits, and deployment options cover Jitsu Cloud, a managed single-tenant private cloud on GCP or AWS, and on-premises. The company went through YC S20 and is based in New York City.
