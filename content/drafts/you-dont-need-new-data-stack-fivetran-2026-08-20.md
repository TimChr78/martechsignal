---
title: "You Don't Need a New Data Stack for AI — Fivetran Just Proved It"
seo_title: "You Don't Need a New Data Stack for AI — Fivetran"
slug: you-dont-need-new-data-stack-fivetran
date: 2026-08-20
author: MartechSignal
tags: [AI, Data Stack, Marketing Operations]
---
Every AI platform vendor wants to sell you the same story: your data stack is legacy, your warehouse is a bottleneck, and the fix is a migration project with two commas and an eighteen-month timeline. Fivetran just published the counter-argument, with receipts.

Earlier this month, Fivetran and data consultancy phData put out a post called ["Building healthcare AI without rebuilding your data platform."](https://www.fivetran.com/blog/building-healthcare-ai-without-rebuilding-your-data-platform) The title is the thesis. Healthcare is one of the most data-hostile industries that exists: thousands of vendor systems per organization, Epic instances nobody wants to touch, compliance review on every connector, and [37% of hospitals running at a loss](https://cthosp.org/daily-news-clip/37-of-hospitals-still-losing-money/) or on margins under 2%. If you can make AI-ready data work there without a rebuild, the "you need a new platform" pitch gets a lot harder to defend anywhere else. Including in your marketing stack.

## What the legacy stack broke

The post's diagnosis is specific, and it will sound familiar if you have ever owned a marketing data pipeline. Healthcare organizations built their integration layer over the past decade using hand-coded ETL: each pipeline took months to build, pulled a fixed subset of fields, and served one dashboard on a weekly or daily batch schedule. Then a new use case arrived, and the whole engineering effort started over from scratch.

That was tolerable when the consumer of the data was a dashboard a human looked at on Monday morning. It is not tolerable when the consumer is an AI agent that reads continuously and acts on what it reads. The post's two measures for an AI pipeline are time to deliver the data and how fresh it stays. Hand-built ETL fails both.

Their fix is not a new platform. It is three changes to how data moves:

1. Replicate everything from the source, not just the fields today's use case asks for. When a new question shows up, the data is already in the warehouse.
2. Keep it current with change data capture, so agents and dashboards work from the same live state.
3. Let schema changes propagate automatically. When a source adds a column or restructures a table, the pipeline adapts and sends a notification instead of breaking at 2am.

None of that requires ripping out what you have. It requires replacing the hand-coded pipes with managed ones and pointing them at the warehouse you already run.

## Four years of roadmap, done in six months

The evidence is [Inova Health](https://www.fivetran.com/case-studies/inova-health-compresses-4-year-roadmap-into-6-months-to-power-ai), a Northern Virginia health system with 26,000 employees and 4 million patient visits a year. Inova had data scattered across on-prem systems, Epic, SharePoint, flat files, and vendor APIs, with a backlog of pipeline requests that kept growing. Their modernization plan was scoped at four years.

They standardized on Fivetran for ingestion, dbt for transformations, and Databricks as the destination, and finished in six months. The reported numbers: $800,000 in third-party spend eliminated, data movement costs cut up to 8x per terabyte per source, and a backlog of more than 500 pipeline requests cleared.

One detail matters more than the headline. Inova's Adobe Experience Platform integration had been stalled for months on fragmented pipelines and complex APIs. With managed connectors, they had it running in under a week. That is a marketing system. The same bottleneck your team knows, solved by swapping custom engineering for a connector, not by buying a new platform.

::: callout
**The numbers are vendor-reported.** Inova's chief data and AI officer is on record backing them ("We accelerated a 4-year roadmap into 6 months"), and the case study is on Fivetran's site, so treat the figures as the best available rather than audited. The shape of the story, though, matches what Gartner and others report independently: the projects that stall are the ones that over-build.
:::

## The failure data points the same direction

The failure evidence is not from Fivetran, which is what makes it useful. dbt Labs published ["Why agentic projects fail and how to fix them"](https://www.getdbt.com/blog/why-agentics-projects-fail-and-how-to-fix-them) on August 14, and its central finding is that the limiting factor is almost never the model. It is data quality and governance. Gartner projects more than 40% of agentic AI projects will be canceled by the end of 2027, and Fivetran's own 2026 readiness index found only 15% of organizations are fully ready, even after spending millions.

The spread between winners and losers is not who bought the fancier platform. Wayfair's supplier agents now handle 41,000 support tickets a month, and C.H. Robinson's agents create 5,500 shipping orders a day while saving 600 person-hours daily. Klarna's agent, built to do the work of over 850 employees, became what one analyst called the poster child for bad AI deployments, with quality problems and falling customer satisfaction. Same model generation, opposite outcomes. The difference was what the agents had to work with.

MarTech made the same point from the budget side on August 18: ["You wouldn't purchase a forklift to carry a coffee cup,"](https://martech.org/how-to-stop-overpaying-for-ai-complexity/) their piece opens, arguing that most teams should start with the lightest approach that can do the job. A rebuild is a forklift. Most teams are carrying coffee cups.

One disclosure before this goes further: Fivetran and dbt Labs [completed their merger on June 1, 2026](https://www.getdbt.com/blog/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents). Two of the three sources in this post are the same company. The Gartner projections and the Klarna/Wayfair outcomes are not theirs, but you should know who is making which argument.

## What marketing ops should copy from healthcare

Translate the healthcare architecture into marketing terms and it maps almost one-to-one.

<div class="flow-strip">
  <div class="flow-step"><span class="flow-label">REPLICATE</span><span class="flow-sub">CRM, ad platforms, MAP, CDP events into the warehouse</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step"><span class="flow-label">MODEL</span><span class="flow-sub">dbt turns raw tables into tested, documented context</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step ai"><span class="flow-label">ACTIVATE</span><span class="flow-sub">warehouse segments written back to CRM and ad platforms</span></div>
</div>

The third step is the one most marketing teams are missing, and it is the reason the rebuild pitch keeps losing. Fivetran's healthcare post leans on Activations, which write trusted data from the warehouse back into operational systems like CRMs and EMRs, creating, updating, and deleting records so the frontline works from the same state as the warehouse. The marketing version is identical: audience segments and scores computed in the warehouse get pushed back into your CRM, ESP, and ad platforms, instead of living in a dashboard nobody acts on.

Notice what that does to the CDP question. You do not need to buy a new platform to get warehouse-native activation. You need a pipe with data flowing both directions.

<table class="cmp">
<tr><th></th><th>Rip-and-replace pitch</th><th>Lean activation (the Fivetran/Inova model)</th></tr>
<tr><td>Starting point</td><td>New platform, migration project</td><td>Existing warehouse, CRM, and MAP</td></tr>
<tr><td>Timeline</td><td>12-18 months typical</td><td>Months; Inova did 4 years of scope in 6</td></tr>
<tr><td>New use case cost</td><td>Engineering project per use case</td><td>Connector plus a dbt model; data already present</td></tr>
<tr><td>Data freshness</td><td>Depends on the rebuild finishing</td><td>Continuous (CDC) from day one</td></tr>
<tr><td>Risk profile</td><td>High; migration is the project</td><td>Incremental; each connector is testable</td></tr>
<tr><td>Failure mode</td><td>Becomes the 40% Gartner cancels</td><td>Smaller surface, easier to unwind</td></tr>
</table>

Salesforce's commerce research agrees on the direction, if not the vendor. Their August 13 piece declares the experimentation phase over: pilots have proven their point, and more than a third of agentic AI users have shifted from testing to scaling. The same research found organizations with unified data report 40% better AI and automation outcomes, while only 27% have fully unified customer data. The gap is not missing platforms. It is unconnected ones. (Salesforce.com blocks automated access, so those figures come from our newsletter scan of the post rather than a direct fetch.)

## What it costs

Verified from [fivetran.com/pricing](https://www.fivetran.com/pricing) as of this writing, because "usage-based" is where vendor pricing goes to hide:

- Pricing is consumption-based on monthly active rows (MAR), with a free plan covering 500,000 MAR for connections, enough to pilot a handful of sources.
- Fivetran's own examples on the Standard plan (1-200 employees): Google Analytics 4 at median usage runs about $11/month, Google Ads about $44, Facebook Ads about $17, and Marketo about $424 at roughly 848,000 MAR. Marketo is the expensive one, and it is expensive because marketing automation generates a lot of rows.
- Transformations get 5,000 model runs free per month, then $0.01 per run, dropping to $0.002 above 100,000 runs.
- Plans tier from Free through Standard, Enterprise (1-minute syncs, hybrid deployment), and Business Critical (customer-managed keys, PCI DSS Level 1). Healthcare-grade compliance is on the top tier, not the base.

Consumption pricing is honest but not automatically cheap: it scales with your row volume, and a marketing stack syncing full event histories can climb. Inova's claim of an 8x cost reduction per terabyte is about replacing third-party spend, not about Fivetran being free. Budget accordingly.

::: verdict win
**The verdict: the rebuild pitch loses.** The evidence from this month, from a vendor case, an industry failure analysis, and independent analyst projections, all lands on the same answer. AI-ready data comes from automating movement and activation on the stack you already own, not from an eighteen-month migration. The teams winning with agents built narrow, well-fed workflows on live data. The teams in the 40% cancellation pile bought platforms first and asked questions later. If someone is quoting you a migration, ask them what happens to your next use case while it runs.
:::

## What to do this week

::: wf-step
**Inventory your hand-coded pipelines.** Every integration someone built as a script or a point-to-point connector is the legacy ETL problem in miniature: fixed fields, batch schedule, breaks on schema change. You cannot prioritize what you have not listed.
:::

::: wf-step
**Pick one agent use case and trace its data path.** Pick the narrow, high-volume kind dbt recommends: clear success criteria, reversible actions, authoritative data available. Then ask how fresh that data really is. If the answer is "it syncs nightly," that is your first gap, and it costs a connector, not a platform.
:::

::: wf-step
**Price the activation loop, not the platform.** Estimate MAR for the two or three sources that feed your use case using Fivetran's estimator, and compare that monthly number against the annual quote for whatever new platform is in your pipeline. One of those numbers is an experiment. The other is a marriage.
:::

::: wf-step
**Keep governance boring on purpose.** The healthcare lesson is that compliance is a configuration, not a rebuild: encryption and a BAA on the ingestion layer, documented and tested dbt models on top, approval workflows where your policies require them. The organizations getting canceled are the ones that made governance an afterthought, not the ones that skipped the fancy platform.
:::

The short version: your data stack probably does not need replacing. It needs its pipes automated, its data fresh, and its warehouse talking back to the systems where the work happens. Fivetran just showed a health system doing exactly that, four years of work in six months, in one of the hardest environments on earth. The next time a vendor tells you AI requires a rebuild, ask them to explain Inova.

<div class="cta-strip">
<h3>Compare data tools before you sign anything</h3>
<p>Our directory breaks down data and activation tools by pricing model, connector coverage, and what they write back to your operational systems. Check the rebuild quote against the lean option.</p>
<a class="btn" href="/tools/">BROWSE THE TOOL DIRECTORY →</a>
</div>

**Sources:** [Fivetran: Building healthcare AI without rebuilding your data platform (Aug 10, 2026)](https://www.fivetran.com/blog/building-healthcare-ai-without-rebuilding-your-data-platform) · [Fivetran: Inova Health case study](https://www.fivetran.com/case-studies/inova-health-compresses-4-year-roadmap-into-6-months-to-power-ai) · [Fivetran pricing (retrieved Aug 20, 2026)](https://www.fivetran.com/pricing) · [dbt Labs: Why agentic projects fail and how to fix them (Aug 14, 2026)](https://www.getdbt.com/blog/why-agentics-projects-fail-and-how-to-fix-them) · [Salesforce: The Experimentation Phase of AI Is Over (Aug 13, 2026)](https://salesforce.com/blog/commerce-leaders-ai-focus) (bot-blocked; figures from newsletter scan) · [MarTech: How to stop overpaying for AI complexity (Aug 18, 2026)](https://martech.org/how-to-stop-overpaying-for-ai-complexity) · [Fivetran + dbt Labs merger announcement (Jun 1, 2026)](https://www.getdbt.com/blog/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents)
