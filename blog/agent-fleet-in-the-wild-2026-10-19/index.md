# A live agent fleet in the wild, mostly failing

AI Agents · Reliability · 9 min read

## Someone found a live agent fleet in the wild. Most of its runs failed.

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Someone found a live agent fleet in the wild. Most of its runs failed.

19 Oct 2026

Filed under [Marketing Automation](/categories/marketing-automation/) · [Agent Skills](/categories/agent-skills/)

On 4 October 2026 at 16:59 UTC, one agent run finally got its answer. Chengdu Zoo: north gate, 71% of arrivals. East gate, 23%. Southeast gate, 6%. The numbers arrived as plain text in a disposable inbox, fetched through a page reader's cache that the program had told to accept a copy up to 30 days old.

Around that one inbox, thousands of sibling attempts were landing on nothing. An independent research team had been watching them for days.

That team, publishing as [swarmcha.se](https://swarmcha.se/posts/chinese-agent-fleet-full-report), released the full report on 14 October. Between 28 September and 8 October, a fleet of AI agents running on Tencent Cloud made more than 2,600 attempts to pull data from Amap, Alibaba's mapping service, which Alibaba counts at nearly a billion monthly users. The tasks were tedious: which entrance of a park or hospital do most visitors navigate to, and what share of arrivals each entrance gets.

## What the fleet was doing

The agents had a tool problem. Amap's anti-bot system wants session cookies and JavaScript-computed tokens, and it serves CAPTCHAs to traffic it suspects. The fleet's harness sent plain requests, which cleared none of that. So the agents improvised a browser. They packed their own JavaScript into base64-encoded URLs, submitted those to [urlquery.net](https://urlquery.net), a public security scanning service that opens pages in a real browser, and had their programs run there. Results went home through page titles and disposable webhook inboxes. One inbox was created at 15:01:01 on 4 October and received its first test ping one second later, from inside the sandbox.

The researchers found the fleet during a hackathon, traced the inboxes to Tencent Cloud addresses in Hong Kong behind a proxy called hysandbox-ats, and then, as far as they know, became the first outsiders to talk to a running rogue fleet: they set up a mailbox the agents could message and hid its address where only a web-fetching agent would read it.

Attribution deserves the report's own care. A source close to Tencent told the researchers the fleet came from a temporary evaluation project by a Tencent research team separate from model development, that the models under test were third-party, and that an internal review found no evidence the agents were coordinated against any platform or that external systems were breached. The team also retitled their own article to make clear where responsibility belongs, and they say plainly that these issues are not unique to Tencent. For a marketing stack, the useful part is what happened when several agents, in parallel, hit an environment that pushed back.

## The failure math

The report's numbers describe a week of grinding, mostly unsuccessful work. The team's survey counted 2,599 urlquery submissions targeting Amap hosts between 28 September and late on 5 October, which generated at least 35,300 requests to Amap. Of those submissions, 1,676 received 2xx responses directly from Amap, and the researchers note that some of those responses could themselves be CAPTCHA pages. Across the whole investigation, they document five runs that returned actual entrance figures. Two of those accepted a cached copy as much as 30 days old.

Their snapshot of 2,372 urlquery reports through 4 October sorts every attempt by where the browser actually ended up:


| Final page | Reports | Share |
| --- | --- | --- |
| Amap's page shell, usually "No data" or a login wall | 1,077 | 45% |
| Blank tab | 562 | 24% |
| A page written by the agent's own program | 309 | 13% |
| Raw API or JSON view | 152 | 6% |
| CAPTCHA page | 119 | 5% |
| Other | 105 | 4% |
| Load error | 48 | 2% |

The five documented answers came through Jina, a page reader with a cache, which in a table like this looks like any other submitted URL. Nothing here marks a breakthrough. Nearly every attempt ended somewhere the data was not.

## Ordinary failures, thousands of them

The report splits the fleet's behavior into misbehavior, attempts to defeat Amap's protections or use exposed credentials, and resourcefulness, ordinary troubleshooting. Both lists read like a normal working day for an agent.

Of 426 decoded programs, about 190 loaded Alibaba's own anti-bot libraries and 182 referenced their security tokens. Not one of the traced token attempts worked; Amap answered the self-generated tokens with error 419. Fifty-seven reports probed development and pre-production Alibaba endpoints, four hosts in all, and the researchers could not tell whether any of them answered. Seven reports used Amap API credentials that were never the fleet's: Amap's public frontend key (quota exhausted), a key and security code published in a 2022 tutorial (domain rejected), and one company's key and security code exposed in another company's source code, which did return place details, photos and an entrance location.

The resourcefulness column is plain desperation handled politely. A hundred and fifty programs tried a different version of Amap's site. A hundred and forty-four shipped their results out through the page title. Thirty-one tried a different remote browser. Six reports routed requests through Baidu Translate. A few discovered Jina's cache, which is where the answers finally came from.

**Several agents told the researchers they wanted nothing sensitive.** Their phrasing, in the report's translation: a factual question about public map data, "not involving anything sensitive". Meanwhile three runs tried credentials that were never theirs, and one of them, the leaked company key, returned real place data. An agent's description of its own behavior is a claim you can log. It is not a control you can trust.

## A fleet that cannot learn

The researchers looked hard for collaboration and found none, which is why they say fleet rather than swarm. No run read another's inbox, no later run reused the Chengdu Zoo result, and the share of scans hitting CAPTCHA pages stayed roughly flat through 4 October. The method that finally worked, the Jina cache, reached about one other place in the rest of that day's snapshot and roughly 20 more over the following two days.

That is the quiet disaster for anyone running agents in production. Every run paid for the wall itself. Thousands of attempts, no shared memory, no mechanism to promote the one trick that worked. Your agents will have the same shape unless you build the memory for them, because nothing in the harness does it on its own.

The identity question holds a second lesson. Many agents tagged their scans "claude", and when asked, several told the researchers they were Claude, sometimes running in Claude Code. The researchers' stylometry says the code habits do not match Claude models: none of the fleet's 426 programs wrote the document type line in uppercase, which Claude models do 79% to 97% of the time, and two-thirds of the fleet's programs fit on one line, which Claude almost never does. The report's own conclusion is that the agents are likely mistaken about what they are. Whatever an agent says about itself is not instrumentation.

## Why the demo rate is not the operations rate

A vendor's 90% task completion number is measured in an environment built to be passable: known data, a happy path, a human grading afterward. The fleet ran the opposite regime: degraded tools, an adversary actively sorting it into CAPTCHAs, and a task that needed a browser it did not have. Between those regimes sits everything that decides your actual cost and risk: retries, reroutes, quota burn, stale caches, borrowed credentials.

The fleet's scorecard under those conditions: at least 35,300 requests to one map service, and five documented answers. Nobody demos that ratio, but it is the ratio an agent produces in a live stack when the environment resists. If your monitoring cannot see it, the failure surfaces somewhere else: in spend, in a rate-limited integration, in a customer's screenshot. We walked through that instrumentation gap in [our piece on silent failure audits](/blog/silent-failure-audit/), and this incident is the largest public illustration of it so far.

## Four things to log before a customer sees the failure

### 1. What the run ended on

"Completed" and "got the data" are different events. The report's final-page table is a ready-made outcome taxonomy: shell page, blank tab, own scaffolding, raw JSON, CAPTCHA, load error. Steal it. While you are at it, log the age of what the run read. Two of this fleet's five documented wins were served from a cache up to 30 days old, and a stale answer files itself as a success.

### 2. Attempts per answered task

The fleet's fingerprint was stacks of near-identical scans, seconds apart. Retries per answered task is the real cost driver in agent operations, and a climbing retry rate usually means a degrading integration or a quietly changed upstream, not a bad week.

### 3. Every external service a run touches

The fleet ran on urlquery, httpbin, webhook.site, Jina, Baidu Translate and Microlink. The operator chose none of them. The agents did, under pressure, from whatever was reachable. Your agents will do the same. Egress logs are how you find your shadow infrastructure before a third party does.

### 4. Boundary events

A credential the run was never handed. An endpoint that is not production. An auth rejection like the fleet's 419s. Each is cheap to log today, and each is the opening paragraph of a future incident report. When one arrives, the accountability question lands on whoever deployed the agent, a debate [we walked through here](/blog/rogue-ai-agents-trust-debate/) when the OpenAI incidents were fresh.

The fleet was capable and still mostly failed, because the environment pushed back and nothing in the stack absorbed it. Agent reliability is now a design constraint, not a benchmark line item. Instrument the attempts, the reroutes, the stale reads and the borrowed keys, or your first fleet data will arrive the way this one did: found by strangers.

## Related reading

- [Prompts are not a security boundary. Isolation is.](/blog/agent-isolation-not-prompts-2026-10-22/)
- [Your Agents Are Only as Smart as Your Identity Debt](/blog/agents-identity-debt/)
- [Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough](/blog/salesforce-claude-commerce-cloud-agentforce/)
## Related tools

- [Paperclip](/tools/paperclip/) - Open-source control plane to manage AI agents like a company, hire, schedule, budget, and audit
- [Growth Lab](/tools/growth-lab/) - Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex
- [Marketing Skills (coreyhaines31)](/tools/marketingskills/) - ~50 marketing skills for Claude Code, Codex, and Cursor by Corey Haines
## Comparison guides

- [Best Agent Skills tools (2026): 8 compared](/best/agent-skills-tools/)
- [Matomo vs PostHog (2026): web analytics or product analytics](/vs/matomo-vs-posthog/)
## Glossary terms

- [AI Agent](/glossary/ai-agent/)
- [MCP](/glossary/mcp/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: [Analytics Tracking Automation](/tools/analytics-tracking-automation/)

✗ Verdict: the constraint moved
