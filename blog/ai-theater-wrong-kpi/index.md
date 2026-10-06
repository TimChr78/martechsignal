# AI theater: the wrong KPI your team rewards

AI AGENTS · MARKETING AUTOMATION · 9 MIN

## Your team is rewarding AI theater: why 'look, it's working' is beating the metric that matters

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Your team is rewarding AI theater: why 'look, it's working' is beating the metric that matters

SEP 30, 2026

Filed under [Marketing Automation](/categories/marketing-automation/) · [Workflow Automation](/categories/workflow-automation/)

HubSpot published a post this month on the psychology of AI progress indicators. In it, [Phill Agnew](https://blog.hubspot.com/marketing/author/phill-agnew) describes something most of us watched happen in 2025: the major answer engines all started showing their work. Claude, ChatGPT, and Gemini began narrating which sites they searched and which assumptions they second-guessed. Anthropic [gives three official reasons](https://www.anthropic.com/news/visible-extended-thinking) for the visible thinking. It helps people check and trust answers. It reveals mismatches between reasoning and output. And it is, in the company's own words, interesting to watch.

Agnew offers a fourth reason the providers are unlikely to say out loud: watching the machine work makes us value the output more. The article names this the labor illusion, after a [2011 study in Management Science](https://www.hbs.edu/ris/Publication%20Files/Norton_Michael_The%20labor%20illusion%20How%20operational_f4269b70-3732-4fc4-8113-72d0c47533e0.pdf) from two Harvard professors. They had 266 participants use a travel search site. One group got a plain loading wheel. The other watched airlines being searched, with fares stacking up as they were found. The results were identical. The transparent version was perceived as 8.1% higher in value, and in a follow-up with 118 new participants, most picked the slower site with the visible search over a faster blank one, even when the transparent version took 50 seconds longer to return the same results.

A [2022 study in Information and Management](http://doi.org/10.1016/j.im.2021.103571) repeated the pattern with 600 participants across two experiments, one with a car search engine and one with a dating app. A seven-second spinner was the only difference between groups. The people who watched it rated identical recommendations as significantly higher quality.

None of this is a scandal. If visible effort makes customers trust you more, ship the progress bar. That is rational product design, and the psychology is real.

The problem is what happens when the same instinct walks into your team's review meetings.

## We brought the spinner to work

The bias does not stay on marketing pages. Inside teams, the same preference decides what gets praised. An agent that streams its reasoning in the demo reads as more capable than a cron job that quietly returns clean data. An automation with a dashboard full of green checkmarks reads as more valuable than one with no UI whose output actually moved a number. A workflow that visibly grinds through steps at midnight looks like work. Whether anyone needed its output is a separate question nobody asks.

Call it AI theater: building automations whose main measurable achievement is being visible.

Two recent posts in r/MarketingAutomation show the pattern from both sides. One builder celebrated a finished machine. Another described what happened after his met reality.

## The content machine that worked perfectly

The first poster, u/Shot-Hospital7649, spent months learning n8n and AI automation and shipped a real [X content machine](https://www.reddit.com/r/MarketingAutomation/comments/1wp0lp6/i_built_an_x_content_machine_now_i_want_to_build/). Creators submit content, AI checks and edits it, a manager approves or rejects, approved posts publish or schedule, everything gets tracked, the creator gets notified. The poster even handled the edge cases: missing information, past dates, different approval flows, waiting for the scheduled time.

Then the last paragraph of the post goes somewhere most launch posts never go:

> But now I'm at the point where I don't want to keep building random workflows just to say I built 10, 20, or 30 automations. I want to work on something that someone actually needs.

Read that as an honest metric review. The machine scores ten out of ten on effort. It demonstrates skill, it runs, it produces. What it does not have is a single user with a problem. The poster says it directly at the end: he would rather build something useful for one real person than add another automation that just sits in his portfolio.

The machine is the spinner. Building it felt like progress, looked like progress in the feed, and so far serves no need beyond the building.

**Applause and revenue are different metrics.** A pipeline that publishes earns upvotes and portfolio lines. A pipeline that earns replies, leads, or removed manual hours earns budget. Automation forums fill up with the first kind because the second kind is quiet and hard to screenshot.

## Then it started publishing for real

The second poster, u/Psychological-Row938, skipped Zapier and n8n entirely and [built his own pipeline](https://www.reddit.com/r/MarketingAutomation/comments/1wo1gfz/i_built_my_own_marketing_automation_pipeline/) for an iOS fitness app: Python, FFmpeg, Meta's Graph API, Cloudflare Workers, Supabase, and systemd. Research, content, video render, QA, scheduled Instagram and Facebook publishing, comment and DM automation, tracking. On paper it is the more impressive build.

His list of what broke once it started publishing for real is the useful part:

- retries can accidentally create duplicate posts
- missed schedules need safe catch-up logic
- Meta comment to Messenger automation is more fragile than expected
- tiny things like Reel thumbnails become real production issues
- observability and failure recovery matter more than adding more AI
A demo never reaches those failures. The happy path runs on launch day, which is exactly when the team applauds. Duplicates, missed schedules, and dead comment automation surface weeks later, in production, in front of customers. His closing takeaway deserves the emphasis: observability and failure recovery matter more than adding more AI.

Anyone who has read the [silent-failure audit](/blog/silent-failure-audit/) on this site has seen this genre before. An n8n user's WhatsApp automation ran green for three weeks while quietly replying into expired conversations. The checkmarks were honest about the only thing they measure, which is whether the send request succeeded. They said nothing about whether the message arrived.

The demos also flatter the pipeline in a subtler way. If any step in the chain is an LLM call, the output that looked great in the demo is one sample from a distribution. The [determinism audit](/blog/determinism-audit/) showed the same hosted model can return materially different answers on different days. A demo proves the pipeline can produce a good output once. It says nothing about Tuesday.

Demos and production answer different questions:


|  | The demo answers | The metric answers |
| --- | --- | --- |
| **Core question** | Does it run? | Did anyone act on the output? |
| **Best day** | Launch day, live in front of the team | A random Tuesday in month three |
| **Failure handling** | Happy path, by definition | Retries without duplicates, catch-up logic, alerts |
| **Evidence** | Screenshots of the workflow graph | Platform IDs reconciled against published posts |
| **Score kept** | Automations built | Manual hours actually removed |

## What to measure instead

First, count outcomes per automation, not automations. The X-machine poster got there on his own: "ten workflows shipped" is an effort metric. Replies earned and manual hours removed are results metrics. Ask of every workflow the question he asked of his portfolio: who needs this?

Second, measure what happens when things go wrong. The best comment on the self-built pipeline came from u/Visible_Speed8843, and it reads like a checklist for any team running automations. Make every publish attempt carry one stable idempotency key derived from the content item and destination. Record the intended post before calling the platform, then store the returned post ID, and let a retry reconcile against that record instead of firing again. Keep schedule state separate from delivery state. An uncertain submission waits in needs-review until someone confirms the post exists. Translated: a healthy pipeline can prove which posts exist and clean up after its own failures. A theater pipeline has a screenshot.

Third, run a kill review. Another poster in the same subreddit [cleaned up their n8n instance](https://www.reddit.com/r/MarketingAutomation/comments/1vtd951/half_my_workflows_shouldnt_have_existed/) and found more than 40 active workflows where only about 15 saw regular use. Most of the rest, the poster wrote, were built for a question that came up once and never came back. Before your next automation ships, run the [blast radius audit](/blog/automation-blast-radius-audit/) and decide in advance what happens when this thing is confidently wrong at 3am. Kill criteria belong on day one, not after the duplicates reach customers.

The self-built pipeline's author ended his post by asking when to stop extending his own system and move orchestration into something like n8n or Temporal. One commenter's answer was measured: move to n8n when visual maintenance helps a team own the flow. That is the right instinct, and it is bigger than the orchestration question. The stack rarely needs another AI component. It needs the [boring repairs](/blog/why-your-marketing-automation-stack-doesnt-need-another-ai-tool/): failures made visible, retries made safe, outputs checked before anyone applauds.

Visible effort is a fine marketing trick and a poor management metric. The labor illusion studies show people will rate work higher when they can watch it happen. Your KPI review should be the one place that bias is not allowed through the door. Count reconciled outputs, removed manual hours, and failures caught before customers saw them. Teams that measure this way ship less impressive demos and better quarters.

HubSpot's piece closes on the observation that most of us prefer a slower answer engine that shows it is working to a faster one that does not. As a description of customers, that is true and useful. As a standard for your own automation program, run it in reverse. The automations worth keeping are the ones nobody has to watch.

MarTechSignal reviews marketing AI tools on what they can decide, what they can execute, whether outputs are validated before anything ships, and whether you can reconstruct the decision afterwards.

**Sources:** [HubSpot: "The psychology behind why AI shows it's working" by Phill Agnew (updated Sep 21, 2026)](https://blog.hubspot.com/marketing/why-ai-shows-loadtime) · [The "labor illusion" study, Management Science (2011), Harvard](https://www.hbs.edu/ris/Publication%20Files/Norton_Michael_The%20labor%20illusion%20How%20operational_f4269b70-3732-4fc4-8113-72d0c47533e0.pdf) · [Tsekouras, Li & Benbasat, Information and Management (2022)](http://doi.org/10.1016/j.im.2021.103571) · [r/MarketingAutomation: "I built an X content machine. Now I want to build something people actually need."](https://www.reddit.com/r/MarketingAutomation/comments/1wp0lp6/i_built_an_x_content_machine_now_i_want_to_build/) · [r/MarketingAutomation: "I built my own marketing automation pipeline instead of using Zapier/n8n"](https://www.reddit.com/r/MarketingAutomation/comments/1wo1gfz/i_built_my_own_marketing_automation_pipeline/) · [r/MarketingAutomation: "Half my workflows shouldn't have existed"](https://www.reddit.com/r/MarketingAutomation/comments/1vtd951/half_my_workflows_shouldnt_have_existed/)

Tools linked in this post: [HubSpot CRM](/tools/hubspot-crm/) · [n8n](/tools/n8n/) · [Zapier](/tools/zapier/)

## Related reading

- [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/)
- [NocoBase vs NocoDB vs Budibase: pick by team shape, not by spec sheet](/blog/nocobase-vs-nocodb-vs-budibase/)
- [Why Your Marketing Stack Doesn't Need Another AI Tool](/blog/why-your-marketing-automation-stack-doesnt-need-another-ai-tool/)
## Related tools

- [ALwrity](/tools/alwrity/) - AI-first digital marketing platform for content strategy, generation, publishing, SEO, and social
- [ActiveCampaign](/tools/activecampaign/) - AI-powered marketing automation and CRM for small to mid-size businesses
- [HubSpot Marketing Hub](/tools/hubspot-marketing-hub/) - All-in-one marketing automation with AI-powered content, email, and campaign tools
## Comparison guides

- [Best AI Marketing Automation tools (2026): 8 compared](/best/ai-marketing-automation-tools/)
- [Best Zapier alternatives (2026)](/alternatives/zapier/)
## Glossary terms

- [Marketing ops](/glossary/marketing-ops/)
- [Workflow automation](/glossary/workflow-automation/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: [Brandwatch](/tools/brandwatch/)

**MartechSignal**, written by [Tim Christensen](/authors/tim-christensen/)

✓ The metric that survives contact with production
