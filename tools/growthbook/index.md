# GrowthBook | MartechSignal review

Open-source feature flags and A/B testing with a visual editor and attribute-based targeting

- Page: https://martechsignal.com/tools/growthbook/
- Category: Personalization & CDP
- Pricing: Freemium
- Open source: yes (MIT)
- Last verified: 2026-09-25

GrowthBook is an open-source feature flag and A/B testing platform with 8,430 GitHub stars, built warehouse-native: experiments are analyzed in your own data warehouse instead of a vendor copy of your events. Flags support attribute-based targeting and gradual rollouts, and every cloud plan includes unlimited flags, experiments, and traffic. The statistics engine runs frequentist and Bayesian analysis, and Pro adds multi-arm bandits, split URL tests, a power calculator, and customizable dashboards.

Cloud pricing starts at zero. Starter is free for up to 3 users and 1 project. Pro runs USD 40 per seat per month for up to 30 users and 3 projects. Enterprise is custom and adds ramp schedules, approval workflows, SSO and SCIM, exportable audit logs, and a 99.99% uptime SLA. A managed warehouse is available for teams without their own: 1 million events a month on Starter, 2 million on Pro and then USD 30 per million. Supported warehouses include Snowflake, BigQuery, Databricks, ClickHouse, Trino, and Adobe Experience Platform Query Service.

The AI surface is real and dated. A hosted MCP server at mcp.growthbook.io connects to Claude, Cursor, and VS Code over OAuth so agents can create flags and read experiment results. The AI Visual Editor is a Pro feature, GrowthBook AI usage is metered per plan, and Enterprise can bring its own LLM provider. Version 5.1 added a Slack app and contextual bandits. Self-hosting is documented alongside cloud. The repository is MIT licensed except for three enterprise directories under a separate GrowthBook Enterprise License. The company was founded in 2020 by Graham McNicoll and Jeremy Dorn.
