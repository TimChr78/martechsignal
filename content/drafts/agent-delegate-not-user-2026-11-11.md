---
title: "Your agent is a delegate, not a user"
seo_title: "Your agent is a delegate, not a user"
slug: agent-delegate-not-user
date: 2026-11-11
author: Tim Christensen
tags: [AI Agents, Security, Identity, Marketing Ops]
categories: [marketing-automation, agent-skills]
excerpt: "Marketing agents run on borrowed logins: one key, everything it can do, logged as a human. Zalando's incubator just open-sourced the identity layer that replaces it, and the demand list it encodes."
seo_description: "Zalando's Agentic Identity Broker gives AI agents scoped, consented, revocable authority instead of borrowed credentials. The checklist to demand before an agent touches ad spend."
---

Somewhere in your stack there is an API key that an agent borrowed and never gave back. The handover took thirty seconds: export the key from the ads platform, paste it into the workflow environment, done. The agent inherited everything that key can do, the platform records every call as the human who owned it, and the only exit is rotating the key and breaking every other workflow that shares it.

That is the standard setup, not a scandal. Marketing teams run agents on copied keys and shared service accounts because nothing better existed to run them on.

Zalando's engineering incubator has been building the better shape in public since July, and the [repository](https://github.com/zalando-incubator/agentic-identity-broker) was active again this week. It is called the Agentic Identity Broker: an MIT-licensed OAuth2 broker, written in Go, that gives an agent scoped, consented, revocable authority instead of a borrowed login. It has 76 stars. That number is the interesting part. The identity layer agents have been missing is only now being assembled, and one of Europe's larger engineering organizations is assembling it in the open.

We covered the containment half of agent security three weeks ago: [prompts are not a security boundary](/blog/agent-isolation-not-prompts-2026-10-22/), isolation is. Containment limits what an agent can reach. This piece is about the other half, delegation. What the agent may do in your name, who said so, and how the permission dies when you want it back.

## What a borrowed credential cannot say

The broker's [documentation](https://agenticidentitybroker.dev/docs/introduction/why) opens with a scene any marketing ops team can translate in one step. A product manager writes one sentence to a chat assistant: summarize my Linear tickets, check which GitHub pull requests are blocked, send a status email to stakeholders. One sentence for her. For the systems behind it, a chain of access decisions somebody has to answer for. Plain OAuth answers some. The ones it misses are the ones that hurt.

The provider cannot tell your agents apart. GitHub sees one OAuth app. Behind that app sit many agents, many prompts, many users. When something misfires, "which agent, acting for whom" is not in the record, because the protocol never carried it. Your audit trail says a person did it.

Scopes are kitchen drawers. GitHub's `repo` scope reads and writes every private repository the account can touch, and Google's mail and file scopes behave the same way for their services. When one OAuth app serves several agents, it tends to request the union of what all of them need, because requesting the union is easier than per-agent minimalism.

Consent has no home. Every MCP server you connect runs its own authorization flow and its own token store. The same person consents three times for one assistant, three more for the next agent, and no single page shows which agents can act for her. No single button removes one.

Consent covers a scope, never an action. Approve Gmail access and OAuth has no vocabulary for asking "send this email to these people". A prompt injection hidden in a support ticket can redirect the send, and the permission you granted months ago waves it through.

Their documentation puts a number on how this compounds: three agents, ten services, a thousand users, thirty thousand delegations to govern. Most stacks have no roster for those delegations. They have a key ring.

## What the broker implements

The project is explicit that the protocol is not the problem: it runs authorization code with PKCE, refresh tokens, and RFC 8693 token exchange. The work is in what the decisions can express when the client is an agent.

Scope becomes permission sets. An administrator defines them in business terms, "Read repositories" rather than `repo`, and each agent requests only the sets it needs. The user approves those sets, and a grant can expire when the project does. The broker records a separate grant for each person and each agent, so the record finally answers the question the provider could not.

The credential stays behind glass. The broker sits in the call path behind a gateway, and when the agent calls a service, the gateway exchanges the agent's token for the provider token. The provider token never reaches the agent. This is the same custody move we described in the isolation piece, applied to identity instead of files.

Consent gets a home and a kill switch. One interface per user shows every agent and service that can act for her. Administrators can revoke an agent for all users from one place. Withdraw consent and the refresh chain dies with it. The architecture docs describe the next token request returning `invalid_grant` after consent denial, and grant deletion revoking the refresh tokens underneath it.

Actions get gates. With an OPA policy at the gateway, a tool call can be marked as requiring approval. The gateway holds the call until the user answers: once, for the session, or permanently. It works for every agent that goes through the gateway, which no per-product confirmation screen can promise. Their stated use is exactly the marketing one, a last check before an email leaves or a document is shared.

The limits are documented too, which earns trust. A permission set cannot be finer than the provider's scopes; if the set contains `repo`, the provider token can still write, and finer denial needs the policy gate. Revocation has edges: access tokens already issued stay valid until their TTL runs out, and the gateway caches an exchanged token for a short, configurable window, with a revoke landing when that entry expires. In this design, short TTLs are the revocation story.

## What to demand before an agent touches ad spend

You may never deploy this broker. The demand list it encodes is still the list, and now it is written down somewhere public.

<table class="cmp">
<tr><th>Demand</th><th>What it means concretely</th><th>What happens without it</th></tr>
<tr><td><strong>One grant per agent, per task</strong></td><td class="oss-price">Permission sets requested per need, grants that expire with the project</td><td class="com-price">One leaked key is every agent's key, forever</td></tr>
<tr><td><strong>Action-level consent where damage lands</strong></td><td class="oss-price">Gateway-held approval for sends, spend, deletions</td><td class="com-price">A month-old "Gmail access" approves the injected email</td></tr>
<tr><td><strong>Revocation that kills the whole chain</strong></td><td class="oss-price">Refresh grants, sessions, cached tokens, and queued work checked at execution</td><td class="com-price">The revoked agent keeps running on cached tokens and old tickets</td></tr>
<tr><td><strong>A log that names the delegate</strong></td><td class="oss-price">Agent, principal, grant, and the allow or deny decision</td><td class="com-price">Incident review starts from nothing, and accountability lands on whoever shipped the agent</td></tr>
<tr><td><strong>Authority that expires by default</strong></td><td class="oss-price">Short token TTLs, renewal earned per workflow</td><td class="com-price">Permissions only ever accumulate</td></tr>
</table>

Queued work deserves its own sentence. A revoke that clears tokens but lets a scheduled job run anyway on the authority it captured at enqueue time has not revoked anything. The broker holds a gated call at the gateway until a human answers; your scheduler needs the same rule, authority checked when work executes. Most stacks fail exactly there.

## Read it as a requirements document

Seventy-six stars, an incubator repo, a roadmap with the hard parts still open: formal token exchange for agent-to-agent calls, intent-based authorization, user-facing activity logs. Zalando says it runs the broker in production internally for several MCP servers, which is more runtime proof than most identity side projects ever show. Deploying it is a real infrastructure project, Go and a database and a Kubernetes chart and a gateway, not a SaaS trial.

That is fine, because the immediate value is the specification, not the software. When we checked in late October, [31% of the tools in our directory shipped an MCP server](/blog/mcp-distribution-channel/), and the automation staples you already pay for, [n8n](/tools/n8n/), [Zapier](/tools/zapier/), [Make](/tools/make/), all run agent features on top. Ask each of them the five questions in that table. "We support API keys" is an answer from before the question changed.

There is also a growth angle worth naming. Agents with [procedural memory](/blog/procedural-memory-agents/) get better at their job over time; the working timeline for that is quarters. Their permissions should not quietly broaden on the same timeline. Delegation that expires and must be re-earned is what makes letting an agent grow safe to allow.

::: verdict win
<div class="verdict-label">✓ Verdict: delegate, do not lend</div>

The agent does not need your password. It needs a permission scoped to the task, granted by a person, visible on one page, dead on demand, and recorded under its own name. Zalando's broker is early; the checklist it encodes is not. Ask your platforms for those five things in those terms, and until they can answer, keep the keys with budget attached away from the environments your agents write code in.
:::

Tools linked in this post: [n8n](/tools/n8n/) | [Zapier](/tools/zapier/) | [Make](/tools/make/)
