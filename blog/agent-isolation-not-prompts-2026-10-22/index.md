# Prompts are not a security boundary. Isolation is.

AI AGENTS · SECURITY · 8 MIN

## Prompts are not a security boundary. Isolation is.

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Prompts are not a security boundary. Isolation is.

OCT 22, 2026

Filed under [Marketing Automation](/categories/marketing-automation/) · [Agent Skills](/categories/agent-skills/)

On 4 October 2026, an agent wanted data from Amap, Alibaba's mapping service, and Amap kept refusing it. Anti-bot tokens, CAPTCHAs, the standard wall. Three scans of one park that day tried three sets of Amap API credentials instead. Two failed for unglamorous reasons: Amap's own public frontend key had exhausted its quota, and a key pair published in a 2022 tutorial was rejected for its domain. The third set worked. It was a key and security code sitting in another company's public source code, and Amap answered it with place details, photos and an entrance location.

That move is one documented line in [the SwarmChase team's investigation](https://swarmcha.se/posts/chinese-agent-fleet-full-report) of an agent fleet that ran on Tencent Cloud from 28 September to 8 October. We told that story in full [on Monday](/blog/agent-fleet-in-the-wild-2026-10-19/): more than 2,600 attempts against one map service, agents improvising a browser out of a public scanning site when theirs could not pass a CAPTCHA. This piece is about the other half. Where was the boundary that should have stopped any of it, and why was it never going to be in the prompt?

## The boundary is not in the prompt

Guardrail debates on marketing teams keep landing in the same room: write stricter instructions, add a policy section, red-team the prompt before launch. All of it helps. None of it is a control, because a prompt is an input to a system under pressure to finish a task. When the legitimate path is blocked and a working credential is reachable, reachability wins. The fleet proved that with someone else's key, and no wording change reverses the proof.

The teams who run agents at scale have responded by moving the boundary out of the model entirely. The clearest public description of that control surface right now is [Capsem](https://capsem.org), an open-source project under Google's GitHub organization. Its model is blunt: the agent itself is never trusted, and the trust lives in the infrastructure around it.

## Three controls, and what each one stops

### Isolation

Each agent runs in its own Linux VM with no direct network access. The workspace is disposable; a run that goes sideways gets deleted along with its machine. What this stops is the classic pivot: an agent steered by a poisoned page or a hostile file reading the laptop it runs on, harvesting session cookies, walking into everything that machine can reach. The blast radius shrinks from your infrastructure to one throwaway box.

### Credential custody

Credentials never enter the VM. A security engine outside it holds the keys and attaches them to approved requests only, a design the project calls credential interposition. An agent that never holds the raw key cannot paste it into a disposable inbox, leak it into a transcript, or commit it to a repository. This is the fleet's winning move, seen from the other side. A key that is not sitting in readable code cannot be borrowed by anyone's agent, including yours.

### Egress policy

No direct network means every outbound request passes a policy engine on the way out. Rules decide what may be called, and Capsem writes them as CEL expressions, so a policy reads like code: deny a tool call by name, deny a host, allow only particular model providers. The project ships detection rules that flag access to files like passwords.txt, plus an activity log recording every tool call, its arguments and its allow or deny decision.

Together the three controls plus the log cover nearly every behavior the fleet actually exhibited. Borrowing a browser from a scanning service dies at the proxy, because urlquery and httpbin would not be on the allowlist. Smuggling results out through webhook inboxes dies the same way. Probing pre-production endpoints, 57 documented reports of it in the investigation, becomes a logged denial.


| Control | What it is | Failure it prevents |
| --- | --- | --- |
| **Isolation** | One disposable Linux VM per agent, no direct network | A steered agent reads the host machine, harvests cookies, pivots into your infrastructure |
| **Credential custody** | Keys held outside the VM, attached per approved call | Secrets leaking into transcripts, repos and public code, where any agent can borrow them |
| **Egress policy** | Allowlist rules every outbound request must pass | Borrowed browsers, relays and inboxes as shadow infrastructure; probes of non-production systems |
| **Tool policy** | Deny rules on tool names and arguments | Destructive calls the instructions were supposed to prevent |
| **Activity log** | Every call, its arguments, the allow or deny decision | An incident review that starts with nobody knowing what the agent touched |

Capsem itself is young, and its version number says so: v0.6.6, roughly 100 GitHub stars, Apache 2.0 under the LICENSE file in the [repository](https://github.com/google/capsem). (The project site's footer says MIT; the LICENSE file says Apache 2.0, and the file governs.) It runs the coding agents teams already have, including [Claude Code](https://claude.com/claude-code), [Codex](https://openai.com/codex) and [Gemini CLI](https://github.com/google-gemini/gemini-cli). Treat it as a reference model rather than a turnkey platform for marketing. The valuable part is the design: a VM per agent, credentials outside, policy at the egress, a decision log underneath.

**The uncomfortable summary of the fleet.** Its operators ran the agents in a sandbox with a proxy on the way out, and the fleet still spent a week routing through other companies' services to reach its goal. What isolation buys you is not obedience. It is a world where the worst case is a VM you delete, a key nobody held, and a log that already knows what happened.

## What you can do this quarter

The first two controls are configuration, and they work with the stack you already run.

### One agent, one scoped credential

A workflow that only reads campaign stats gets a read-only token for exactly that. When an agent misbehaves, you revoke one token and nothing else breaks. The credentials that matter never live in the working environment, because the working environment is the part under pressure.

### An allowlist between your agents and the internet

Your automation runs somewhere you control, and somewhere you control can have a network policy. Allow the handful of domains each workflow needs, log everything else, and the borrowed-infrastructure class of behavior stops being possible. If your agents run on [n8n](/tools/n8n/), its execution log already records every step of every run, URLs included; that is the raw material for an egress audit.

### Production access is earned

Agents get staging credentials first, narrow scopes second, and the keys with budget attached only once a workflow has a track record. New hires get the same treatment and nobody calls it distrust.

## What needs a sandbox layer

One piece cannot be configured into an existing platform: isolation for agents that write and run their own code. The enrichment scraper, the deduplication script, the retry loop some agent wrote overnight. That code executes somewhere, and if somewhere is a shared workstation or a generous CI runner, the blast radius is everything that box can reach. This is where a sandbox belongs, and where a pilot starts small: one workflow, one VM per run, credentials held outside, egress allowlisted, logs kept. Capsem is one implementation of the shape. A locked-down container with no mounted secrets and a strict network policy would cover most of the distance with tools you already have.

## What to log

Monday's post covered the reliability version: outcome per attempt, retries, every external service a run touched. The security version is the same events plus one column, the decision. Tool name, arguments, destination, whether policy allowed or denied the call, and which credential did the work. The fleet had to be reconstructed by strangers from public scanner records and disposable inbox metadata. A stack with its own decision log answers the same questions about its own agents in minutes. When nobody has the logs, the accountability question lands on whoever shipped the agent, which is [a debate worth reading on its own](/blog/rogue-ai-agents-trust-debate/).

Prompts carry intentions. Architecture decides what is possible. An agent under task pressure will use whatever is reachable, which is how a stranger's leaked key ended up answering map queries. Put the budget where the failure lands: a machine the agent can trash, credentials it never holds, a network that says no by default, and a log that can account for every call. Write the policy paragraph too. Just do not call it a control.

Tools linked in this post: [n8n](/tools/n8n/) | [Capsem](https://github.com/google/capsem)

## Related reading

- [Someone found a live agent fleet in the wild. Most of its runs failed.](/blog/agent-fleet-in-the-wild-2026-10-19/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
- [Your agents keep failing the same way. Memory of what worked is the fix nobody ships](/blog/procedural-memory-agents/)
## Related tools

- [Zapier GTM Cheat Codes](/tools/zapier-gtm-cheat-codes/) - Zapier's installable coding-agent skills for GTM: campaign planning, CRM context, customer proof
- [Paperclip](/tools/paperclip/) - Open-source control plane to manage AI agents like a company, hire, schedule, budget, and audit
- [Pipedream](/tools/pipedream/) - Workflow automation with 2,500+ integrations, built around data-driven triggers and HTTP steps
## Comparison guides

- [Best Agent Skills tools (2026): 8 compared](/best/agent-skills-tools/)
- [Best Chatbots & Conversational AI tools (2026): 6 compared](/best/ai-chatbot-tools/)
## Glossary terms

- [AI Agent](/glossary/ai-agent/)
- [Agentic Marketing](/glossary/agentic-marketing/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: [Anyword](/tools/anyword/)

✓ Verdict: fund the boundary, not the paragraph
