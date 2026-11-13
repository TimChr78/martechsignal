# MCP, API or CLI: what your stack should expose to agents

AI Agents · MCP · 8 min read

## MCP, API or CLI: what your stack should actually expose to an agent

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · MCP, API or CLI: what your stack should actually expose to an agent

13 Nov 2026

Filed under [Marketing Automation](/categories/marketing-automation/) · [Agent Skills](/categories/agent-skills/)

Two weeks ago we counted how many tools in our directory mention MCP. The answer was 53 of 171 active records, or 31 percent. We re-ran the count on 13 November and it now stands at 55 of 174, with 19 tools listing MCP as a named integration, up from 18. Same method as before: search every active record for "MCP" or "Model Context Protocol" in the fields a buyer reads, meaning tagline, description, AI features, integrations, and the deep dive notes. Two new mentions and one new named integration in a fortnight.

The direction is settled. "Ships an MCP server" has become a checkbox in every vendor deck, the way "has an API" was a checkbox in 2015 and "AI-powered" was in 2023. When a feature reaches checkbox status, the interesting question moves. The question that matters now is what that surface is for, and whether it survives contact with an agent doing real work.

The best builder-side treatment of this we have read is [a long engineering post by Vince Canger at Wasp](https://wasp.sh/blog/2026/11/03/mcp-vs-api-vs-cli-connect-ai-agents-to-your-app), published 3 November. He built one example app with an MCP server, a REST API, and a CLI, all over a single layer of shared operations, and came out with clear advice: ship a high-quality MCP server and a REST API together, put most of the care into the MCP surface, and skip the CLI unless agents need to touch files on the user's machine. It is a good answer to a builder's question. This post is the other side of the table. You are not deciding what to build. You are deciding what to pay for, and the diligence is different.

## Match the surface to the job, not the demo


| The job | The surface that fits | Why |
| --- | --- | --- |
| A human asks, the agent works: pull last week's numbers, compare, draft, act | MCP server | The client (Claude, ChatGPT, Cursor) handles login, loads tool descriptions into context, and can route confirmations straight to the human |
| Anything unattended: nightly sync, bulk export, another vendor's integration, a script you rerun each month | REST API | Nothing needs to be watching. Deterministic, schedulable, auditable |
| The work touches files on the user's machine | CLI | A remote server cannot read your disk, and a CLI moves the file without routing every row through the model |

The row people get wrong is the middle one. Canger's worked example is tagging 300 short links: through MCP tools in an ordinary chat, without code mode, every call and every row passes through the model's context. Code mode, where the client runs the loop in a sandbox and returns only the result, exists in some clients and not others, so a buyer cannot assume it. When a vendor's pitch is that your agent can update ten thousand records, the honest answer is that the job belongs to a script against their API, run by a scheduler. If they have no API worth the name, that pitch is a context bill with your logo on it.

Which surfaces a vendor shipped also tells you which jobs they think you have. MCP with no usable API means they want your agent and their scheduler, on their pricing. API with no MCP means they have not yet met their buyers' assistants. Both surfaces over one shared layer, the architecture Canger advocates, is the only configuration that does not eventually charge someone for the gap. The stickier half of that story is context, which we covered in [the CDP-as-context-layer piece](/blog/cdp-agents-context-layer/): the server is where your agents' working knowledge lives, which is why the shape of its permissions matters at renewal.

## Six questions that separate an agent surface from a logo

Can you scope the connection? The pattern to insist on is per-connection OAuth where the user picks permissions, with read tools available before write tools, so write actions do not even enter the model's context until someone grants them. The pattern to refuse is one master API key pasted into a chat. That is the 2015 integration model wearing this year's clothes, and it hands the agent everything at once.

When the agent reaches for something destructive, who answers? An API can require a confirm parameter, and a CLI can require a -yes flag, but in both cases the question travels back through the model, which can answer it itself. MCP's elicitation does something better: the server asks the client to open a confirmation page for the human, and the model never sees the question. Canger's analogy is worth keeping: a clerk asking your assistant "are you sure?" gets a yes; a text to your phone does not. Client support is uneven, URL-mode elicitation works in some clients and not others, so the diligence question is which clients the flow works in today. If the only gate on "delete campaign" is a flag the model can set, assume it will be set.

What happens when the agent loops? Agents retry, and a confused one will call the same tool over and over. The hardening bar from the Wasp post is concrete: rate limits enforced per connection rather than per user, so one runaway agent cannot lock your team out; 429 responses with a Retry-After header, so the agent waits instead of escalating; and one documented error shape with codes, so both scripts and agents can branch on failure. If none of that is in the docs, the failure modes are a locked account and a surprise bill.

Can the agent rehearse? A dry run, a preview, a diff shown before the write lands. For unattended API jobs this is a staging environment. For in-loop MCP work it is the agent showing you what it is about to change and waiting. Vendors who skipped this tend to describe their agent features with the word "autonomous", which is how you know.

Is the tool schema versioned? Tool names and descriptions are the interface your prompts and playbooks depend on. A renamed tool or a rewritten description breaks them silently. A public changelog for the server is the minimum evidence that schema changes are treated as breaking changes.

Does the server say no anywhere? [NocoDB](/tools/nocodb/)'s documentation states its MCP server does record-level operations only, no table, field, or metadata changes. That is a published limit, and it is more useful than a bigger tool list, because it tells the agent and the buyer what not to attempt. The same instinct covers what the server returns: Canger's link shortener keeps only the hostname from referrer data, because anyone who clicks a link controls that header, and everything a tool returns lands in the model's context alongside your instructions. Prompt injection through your own analytics is a real path, and a server designed with it in mind will say so.

## What we accept as evidence

When a record in our directory lists MCP as a named integration, the bar is the vendor's own documentation, read, not the press release. The 19 tools carrying that listing today include [NocoDB](/tools/nocodb/) with its stated scope limit, [Customer.io](/tools/customer-io/) with setup guides for four clients plus a CLI and an agent skill, [Ahrefs](/tools/ahrefs/) with a named SEO MCP server, and [Nightwatch](/tools/nightwatch/) with a server documented for Claude, Cursor, and ChatGPT. That is four vendors and four genuinely different surfaces, which is the point: the listing records that a server exists and is documented, not that it is good.

What we do not accept, and what we will keep not accepting as the count climbs: an MCP logo on an integrations page with no server URL and no documentation. Tool counts presented as quality claims; one vendor we covered in the census exposes 211 tools by its own documentation, and that is surface area, not care. And "AI-native" launch language with nothing behind it. Our grep finds 55 mentions; our rule counts 19, because a mention can be marketing and a named integration has to at least exist. The gap between those two numbers, 36 tools, is the size of the checkbox.

The next count runs at the end of November, as promised in [the census](/blog/mcp-distribution-channel/). The presence number will keep climbing, because presence is cheap. The number worth watching is different: how many of those servers publish what they refuse to do, how their confirmations reach a human, and where their limits are written down. That list is much shorter than 55, and a vendor's willingness to be on it says more than any integrations page.

**Related reading:** [31% of the tools in our directory now ship an MCP server](/blog/mcp-distribution-channel/) - the census this post builds on. [The fully open-source agentic marketing stack](/blog/open-source-agentic-martech-stack-mcp/) - what 19 self-hostable servers look like assembled into one stack. [Your agents keep failing the same way](/blog/procedural-memory-agents/) - why the surface is only half of what an agent needs.

## Related reading

- [31% of the tools in our directory now ship an MCP server](/blog/mcp-distribution-channel/)
- [Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough](/blog/salesforce-claude-commerce-cloud-agentforce/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
## Related tools

- [Relaticle](/tools/relaticle/) - Open-source CRM with native AI agent support, 37 MCP tools, REST API, Laravel & Filament
- [Cordys CRM](/tools/cordys-crm/) - Open-source AI CRM with built-in agents, conversational analytics, and private deployment
- [Marketing Skills (coreyhaines31)](/tools/marketingskills/) - ~50 marketing skills for Claude Code, Codex, and Cursor by Corey Haines
## Comparison guides

- [Best Agent Skills tools (2026): 8 compared](/best/agent-skills-tools/)
- [Best Chatbots & Conversational AI tools (2026): 6 compared](/best/ai-chatbot-tools/)
## Glossary terms

- [MCP](/glossary/mcp/)
- [AI Agent](/glossary/ai-agent/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.
