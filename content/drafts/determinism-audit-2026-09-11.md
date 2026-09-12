---
title: "Most of your marketing AI agents should be if/then"
seo_title: "Most of your marketing AI agents should be if/then"
slug: determinism-audit
date: 2026-09-11
author: Tim Christensen
tags: [AI Agents, Marketing Automation]
categories: [agent-skills]
---
An open-source project called the Agentic Determinism Index [landed on Hacker News on September 1](https://news.ycombinator.com/item?id=49522378). It collected 5 points and three comments. One commenter said it would matter for regulated industries. Marketing ops is not a regulated industry, which is exactly why nobody is going to run this audit for us.

The repo ([lemma-ventures/agentic-determinism-index](https://github.com/lemma-ventures/agentic-determinism-index), MIT licensed, 4 stars at time of writing) asks hosted LLM APIs one narrow question: "If I send you the exact same request N times, concurrently, and again across days, how identical are your answers?" Byte-level comparison. No intelligence benchmark, no quality judgment. Just reproducibility, measured per provider, per model, per serving stack, over time.

The answers should change how you staff your agent roadmap. Same model, same weights, different serving paths, wildly different scores from the September 12 reference snapshot:

| Serving path | Model | Score | Mode share |
|---|---|---|---|
| Cerebras via OpenRouter | gpt-oss-120b | 100.0 | 100%, byte-exact in 5/5 runs |
| Groq via OpenRouter | llama-3.1-8b-instruct | 89.25 | 95% |
| DeepInfra via OpenRouter | llama-3.1-8b-instruct | 44.5 | 60% |
| OpenRouter (routed) | llama-3.1-8b-instruct | 31.87 | 44% |
| OpenRouter | gpt-4o-mini | 36.49 | 42% |
| Amazon Bedrock via OpenRouter | nova-lite-v1 | 14.62 | 20% |

Look at the three middle rows. The identical Llama model scores 89 on one provider and 32 on another. The repo states the lesson plainly: determinism is a property of the deployment, not the weights. You are not buying "GPT-4o-mini." You are buying whatever tuple of provider, snapshot, parameters, batching behavior, and GPU class answered the phone that day, and the index's stack-drift timeline shows that tuple churning constantly. One entry logged 13 backend fingerprint changes for a single (provider, model) pair in ten days. On August 26, NVIDIA's hosted API returned HTTP 410 Gone for a pinned Llama checkpoint overnight. Teams that had built on that string lost the ability to reproduce yesterday's outputs.

## Why ops should care more than infra teams

Mode share is the fraction of responses that match the most common answer. A 95% mode share sounds safe right up until you remember that agents chain calls. The repo does the arithmetic: if a model repeats 80% of the time per call, a 10-call trajectory repeats far less often than 80% of the time. Do the naive math yourself and 0.8 to the tenth power is about 11%. Independence is an assumption, but the direction is not: every step you add to an agent multiplies the odds that the full path drifts.

Your six-step campaign agent that "usually works" is not usually working. Its complete trajectory, start to finish, is closer to a coin flip than the per-call number suggests. When your agent tests are flaky, some of that is your code and some is the serving layer underneath, and until you measure, you are guessing which.

Meanwhile the trade press has moved on to the next thing. MarTech's season-four premiere of Conversations with MarTech, published September 2, is titled ["What's next in content operations? Agents (what else?)"](https://martech.org/whats-next-in-content-operations-agents-what-else/). Orange Logic SVP Misti Vogt makes a real case: DAM buying is shifting back to IT, assets need structured metadata so systems can reason about them, and "brand agents" can check finished creative against brand guidelines before it enters formal review. Some of that is genuinely useful. Some of it is a lookup table wearing a trench coat. A compliance check against fixed brand rules is if/then work, and if/then does not drift when the batch size changes.

That is the problem in one sentence: marketing ops decides which steps need determinism by superstition instead of policy, and superstition sounds like "it has been fine so far."

## The audit: four tiers by blast radius

This extends the [blast-radius quadrants](/blog/automation-blast-radius-audit/) from last week to anything you currently call an agent. One question per item: if it acts unexpectedly today, what breaks?

| Tier | What breaks | Typical occupants |
|---|---|---|
| 1 | Nothing | Internal tagging suggestions, meeting summaries, draft briefs a human reads first anyway |
| 2 | A draft gets weird | Ad copy variants, blog drafts, email subject tests, anything behind human review |
| 3 | A customer sees it | Live chat replies, on-site personalization, triggered sends, social responses |
| 4 | Money moves | Bid changes, budget pacing, list selection that gates a paid send |

The classification does the arguing for you.

**Tier 1 and 2: reclassify as automation.** Most of what gets called an agent in a marketing stack lives here, and per-token nondeterminism buys you nothing a human reviewer does not already absorb. If the job is "route this lead when field X exceeds Y," that is an if statement, and an if statement costs nothing per run, never drifts, and needs no prompt. Where a step genuinely needs language (summarize this ticket, extract entities from this brief), keep the LLM call but stop calling the whole pipeline an agent, and validate the output against a schema before anything downstream trusts it. The index has a metric for exactly this, whether parsed and canonicalized JSON agrees even when the raw bytes do not, because structured output is where a probabilistic step can be made safe enough to keep.

**Tier 3: this is where agent value actually concentrates, and only with guardrails.** A customer-facing judgment call is the one place where flexible reasoning earns its variance. But it needs what the tier-2 toys never got: [campaign state the agent can read](/blog/ai-agents-need-campaign-state/) so its decisions are grounded in facts instead of a prompt's memory of facts, and an [approval trail](/blog/autonomous-stack-loophole-approval-step/) so that when something weird reaches a customer you can reconstruct who decided what, and when.

**Tier 4: no model in the decision path.** If money moves, the decision logic is deterministic code with a human approval above a threshold. An LLM can draft the recommendation. It does not get to execute it. A 20% mode share on a bid-adjustment path means the same market conditions produce a different budget decision one run in five, and you will never be able to explain why to finance.

## Run it in an afternoon

::: wf-step
**Step 1: Inventory everything called an agent.** Include the things nobody calls an agent: the ChatGPT step inside a Zap, the summarizer node in n8n, the vendor feature that quietly started routing through a model after an update. Ignore the label and ask one question instead: does an LLM influence an outcome?
:::

::: wf-step
**Step 2: Assign a blast-radius tier to each item.** Nothing / a draft gets weird / a customer sees it / money moves. When two people disagree on a tier, write down both answers. The disagreement is the finding: it means nobody ever decided this on purpose.
:::

::: wf-step
**Step 3: Locate the actual model call inside each item.** Most "agents" are a fixed pipeline with one probabilistic step buried in the middle. Once you can point at it, you have four options: replace it with rules, gate it behind a human, constrain and validate its output, or keep it and pin the serving stack. Options get cheaper as the tier goes down.
:::

::: wf-step
**Step 4: Write the policy, one line per tier.** For example: tier 1-2 defaults to deterministic automation, model calls require validation; tier 3 requires state, approval trail, and a kill switch; tier 4 requires deterministic logic and human sign-off above a money threshold. Put it where the next tool purchase will trip over it.
:::

One honest disclosure, because the index deserves it. Lemma Ventures, the maintainer, builds deterministic-inference infrastructure and says so in the README: they have a commercial interest in reproducible serving. The leaderboard is v0.1 with 23 reference runs so far, and the first full analysis lands after about a month of data. Every score is recomputable from raw transcripts under MIT, which is the right design for a number you are supposed to distrust by default. I would not bet a vendor choice on the current rankings. I would absolutely bet an audit on the question.

## "Agent" is a budget decision

The label hides the economics. Deterministic serving exists today. SGLang ships a deterministic-inference mode, vLLM ships batch-invariance, and in Thinking Machines' testing the deterministic path ran at roughly half the default throughput. Half. And almost nobody pays that price, which tells you what most of these workloads were actually worth: they never needed the reasoning, they needed the reasoning to be cheap, and "agent" is how the invoice gets approved.

When a vendor sells you an agent for a tier-1 job, you are paying per token for variance you did not order. When you build one yourself for the same job, you are paying for it in debugging time every time the trajectory drifts. The audit is how you stop buying risk you do not need, and how you make sure the risk you do keep is sitting in tier 3, pointed at customers, with guardrails around it.

::: verdict warn
**The verdict: sort your stack by what breaks, then buy determinism where it matters and nowhere else.** The same Llama model scores 89 on one serving path and 32 on another, and agent chains multiply that variance with every step. Most of what marketing calls an agent lands in tiers 1 and 2, where a wrong output costs nothing and an if/then would have been free, stable, and explainable. Real agent value concentrates in tier 3, customer-visible judgment, and only when it has state, approval trails, and a kill switch. Tier 4, where money moves, is not an agent conversation at all. Run the inventory, assign the tiers, write the one-line policy per tier. An afternoon now beats a post-mortem after the first customer sees a 20% mode share up close.
:::

<div class="cta-strip">
<h3>Compare AI agent tools on the questions that matter</h3>
<p>Our directory reviews marketing AI tools on what they can decide, what they can execute, whether outputs are validated before anything ships, and whether you can reconstruct the decision afterwards.</p>
<a class="btn" href="/categories/agent-skills/">BROWSE AGENT SKILLS →</a>
</div>

**Sources:** [Agentic Determinism Index, GitHub repo (MIT, retrieved Sep 12, 2026)](https://github.com/lemma-ventures/agentic-determinism-index) · [ADI reference leaderboard, run of Sep 12, 2026](https://lemma-ventures.github.io/agentic-determinism-index/) · [Hacker News thread, Sep 1, 2026](https://news.ycombinator.com/item?id=49522378) · [Lemma Ventures: "Yes, LLMs can be deterministic. But most hosted stacks are not." (Sep 1, 2026)](https://lemma.ventures/blog/your-model-is-not-non-deterministic.html) · [MarTech: "What's next in content operations? Agents (what else?)" (Sep 2, 2026)](https://martech.org/whats-next-in-content-operations-agents-what-else/)
