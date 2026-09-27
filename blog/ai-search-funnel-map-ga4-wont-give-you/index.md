# The AI-search funnel map GA4 won&#x27;t give you

AI SEARCH · ANALYTICS · 11 MIN

Home · Blog · The AI-search funnel map GA4 won't give you

SEP 10, 2026 · Updated SEP 25, 2026

Filed under SEO & Search

Two things landed since we published the 5-layer fix for dashboards that can't see AI search. On May 13, Google shipped a native AI Assistant channel in GA4. On August 31, the Search Console AI performance report went global. Everyone assumed that meant the measurement problem was solved. It wasn't. Both updates tell you a visit came from AI. Neither tells you where in the funnel it came from, and that is the half you actually need.

Layer 3 of the old framework said: segment AI referrals and treat the count as a floor. Fine as far as it goes. But a flat count of ChatGPT sessions is like reporting "search traffic" without separating branded from non-branded. Technically true, useless for decisions. This post builds layer 3 into a funnel you can stand up in GA4 or Umami this week.

## The channel box answers the wrong question

GA4's AI Assistant channel classifies sessions by referrer. When Google detects chatgpt.com, gemini.google.com, copilot.microsoft.com, deepseek.com, or grok.com it overwrites the medium to ai-assistant and files the session in its own channel. That answers "which tool sent this click."

The question a funnel answers is different: what was the visitor doing when they clicked. Consider two real sessions from the same channel:

- Someone asks ChatGPT why SaaS churn spikes in month three, gets an answer citing your blog post, clicks through, reads 90 seconds, leaves. That is awareness. Your brand entered the conversation before the person knew they wanted software.
- Someone asks ChatGPT whether your product is worth the price compared to a named competitor, clicks your pricing page, reads to the bottom, opens the demo form. That is decision stage, one field away from pipeline.
In GA4's Traffic Acquisition report these two sessions are the same row. Same source, same medium, same channel. The only thing separating them is the landing page, and nobody crosses those dimensions by default. Multiply that across a month and the AI Assistant channel reads as one undifferentiated blob, so it gets compared to Organic Search on sessions and engagement rate, loses, and gets deprioritized. I have watched that exact meeting happen over ordinary referral traffic for years. AI referral traffic will get the same treatment unless the report is built differently on purpose.

## Why the defaults hide the stage even when you look

Three mechanical details make this worse, and all three are verifiable in Google's own documentation rather than folklore.

AI Overviews and AI Mode clicks are Organic Search, permanently. The Referer header a browser sends is google.com/search whether the result was a blue link or a citation inside an AI Overview. The rendering happened on Google's side and nothing about it crosses over to your analytics. Google's Default Channel Group reference says this explicitly: Organic Search includes AI Overviews and AI Mode. So your highest-volume AI surface is invisible in GA4 by construction. The GSC AI performance report is the only place it shows up, and that report gives impressions, pages, countries, and devices with no clicks and no query detail. A visibility count, not a performance report.

ChatGPT's own UTM tagging can downgrade a session. OpenAI appends utm_source=chatgpt.com to many outbound links, often with no utm_medium. GA4's rule is that any UTM parameter makes it ignore the referrer, so a source-only tag can drop the session into Unassigned instead of AI Assistant. Worse than no tag at all. If your ChatGPT traffic looks mysteriously small, check Unassigned before concluding nobody is clicking.

Apps strip the referrer entirely. Links opened from the ChatGPT iOS or Android app hand off to the system browser, and the Referer header often does not survive the trip. ChatGPT's Atlas browser has been reported doing the same. Those sessions land in Direct with no signal left to classify. No channel grouping update fixes a missing header.

You cannot repair any of this from the source side. You can work around it from the landing side, which is where the funnel map comes in.

## The map: stage lives on your pages, not in the referrer

Here is the reframe. You cannot control what label arrives with an AI click, but you control which page AI cites for which question. Search Engine Land published the missing piece on August 31: Casey Nifong's prompt mapping framework, which organizes the questions buyers ask AI into four funnel stages, awareness, consideration, evaluation, decision, and tracks visibility separately at each one. Her example of why aggregates lie: a brand appearing in 40% of 100 tracked prompts might be at 70% for branded and comparison prompts and 10% for problem-discovery ones. The single score hides a brand that only exists once buyers already know what they want.

Now run that same logic on the arrival side. Every page on your site belongs to a stage, and AI referrals land on pages. Cross the two and the funnel appears:

The referrer says ChatGPT sent them. The landing page says why. That combination is the funnel GA4 will never hand you pre-assembled, because the stage mapping is a claim about your content that only you can make.

## What to build this week

Five moves, in order. GA4 instructions first, Umami equivalent at the end for the self-hosted crowd.

1. Build a custom channel group that beats the native one to the punch. The AI Assistant channel recognizes five referrers and is not retroactive. Claude and Perplexity are not on Google's list at all, which is a real gap for B2B. Add a custom channel group with a regex covering the full set, chatgpt|openai|perplexity|claude|anthropic|copilot\.microsoft|gemini\.google|grok|deepseek|you\.com|phind|mistral|poe\.com, plus a rule catching medium = ai-assistant. Custom channel groups apply from creation forward, so build it today or lose another month of history to Referral and Direct.

2. Assign content groups to every page, mapped to the four stages. GA4 content groups are set via a content_group parameter in the config tag, or with a lookup table in GTM keyed on page path. Four values is enough: awareness, consideration, evaluation, decision. If your URL structure is sane (/blog/ vs /pricing vs /alternatives/) this is an afternoon of GTM work. If it isn't, it is a week, and that is still worth it because content groups feed every report downstream.

3. Tag the prompt library by stage, per SEL. This is the visibility side of the map and the prerequisite for correlating it with arrivals. Twenty to fifty prompts from real sales calls and support tickets, each tagged awareness / consideration / evaluation / decision, run monthly across the engines your buyers use. Record mention and citation rate per stage, not per aggregate. Nifong's warnings apply: don't build it in a marketing brainstorm, use customer language, and don't weight 50 awareness prompts equally with 10 evaluation ones in a single score.

4. Build one report: stage on rows, AI channel in a filter, key events as the metric. In GA4: Exploration report, free-form, rows = session source/medium + landing page content group, values = sessions, engaged sessions, key events. Filter to your custom AI channel group. Read it as a funnel: how many AI-referred sessions arrive at awareness pages, how many at evaluation pages, and what converts at each. Then compare the shape against your prompt library. If visibility is 70% at decision stage and arrivals are 70% awareness, AI is introducing you early and losing you late, and the fix is comparison and alternatives content, not more blog posts.

5. Sit the GSC AI report on top as the visibility trend. It has no clicks, so it cannot enter the funnel directly. But its impressions trend by page tells you which stage's pages Google's AI surfaces are showing, week over week. Line it up against stage-tagged arrivals in the same dashboard. Rising AI Overview impressions on consideration pages with flat arrivals is a citation-placement problem. Rising impressions and rising arrivals is working.

Umami version, for the self-hosted: Umami's funnel report takes sequential steps with a conversion window, and every report filters by referrer. Create a funnel of view awareness page → view evaluation page → view pricing → demo event, then filter by referrer chatgpt.com and run it again for perplexity.ai and claude.ai. You get per-engine funnels with no channel grouping at all, which is more than GA4's default view gives you. The trade-off is no cross-session stitching, so treat each run as a within-session pathway, not a full journey.

{ &quot;custom_channel_group&quot;: { &quot;name&quot;: &quot;AI search&quot;, &quot;rules&quot;: [ {&quot;channel&quot;: &quot;AI assistants&quot;, &quot;conditions&quot;: [ {&quot;field&quot;: &quot;medium&quot;, &quot;operation&quot;: &quot;matches regex&quot;, &quot;value&quot;: &quot;ai-assistant&quot;}, {&quot;field&quot;: &quot;source&quot;, &quot;operation&quot;: &quot;matches regex&quot;, &quot;value&quot;: &quot;chatgpt|openai|perplexity|claude|anthropic|copilot\\.microsoft|gemini\\.google|grok|deepseek&quot;} ]} ] }, &quot;content_groups&quot;: { &quot;awareness&quot;: [&quot;/blog/&quot;, &quot;/guides/&quot;, &quot;/research/&quot;], &quot;consideration&quot;: [&quot;/features/&quot;, &quot;/use-cases/&quot;, &quot;/how-&quot;], &quot;evaluation&quot;: [&quot;/vs/&quot;, &quot;/alternatives/&quot;, &quot;/compare/&quot;, &quot;/integrations/&quot;], &quot;decision&quot;: [&quot;/pricing&quot;, &quot;/demo&quot;, &quot;/docs/&quot;, &quot;/security&quot;] }, &quot;report&quot;: { &quot;rows&quot;: [&quot;sessionSource&quot;, &quot;sessionMedium&quot;, &quot;contentGroup&quot;], &quot;metrics&quot;: [&quot;sessions&quot;, &quot;engagedSessions&quot;, &quot;conversions&quot;], &quot;filter&quot;: {&quot;channelGroup&quot;: &quot;AI search&quot;} } } What the funnel will probably show, and what not to conclude Set expectations now. AI referrals will arrive concentrated at awareness and evaluation, and thin at consideration. Chat assistants are good at explaining problems and good at building shortlists; the middle of the funnel happens inside the conversation itself, on a surface you will never see a click from. That is consistent with what Nifong's framework predicts on the visibility side and with the confidence-assembly pattern from part one, where buyers bounce between AI, Google, and community sources before committing.

Three traps when reading the result. Don't compare stage conversion rates to organic search's; the populations differ and you will chase ghosts. Don't treat the awareness-page arrival count as the size of your AI influence, because the assistant answered questions about you all week without generating a single click. And don't let the custom channel group's growth become the KPI. The channel count is the floor, same as it was in layer 3. The funnel shape is the insight: where AI introduces you, where it drops you, and which page class to fix next.

⚠️ The verdict: the channel update was never the finish line. GA4 now labels some AI clicks. It still cannot tell an awareness visit from a decision visit, cannot see AI Overviews at all, and will quietly file ChatGPT's own tagged links into Unassigned. The fix is a map with stage on both sides: prompts tagged by funnel stage on the visibility side, landing pages tagged by stage on the arrival side, crossed in one report. That is buildable in a week with tools you already pay for, and it turns "AI sent us 400 sessions" into "AI introduces buyers early, we lose them at evaluation, and the gap is comparison content." The second sentence is the one that gets budget.

This is part of our SEO measurement coverage. Part 1 diagnosed the blindness; this builds the funnel on top of layer 3.

### Check what your analytics stack can actually see

Our directory breaks marketing tools down by what they measure, what they integrate with, and what AI-era pricing looks like. If your funnel map needs a self-hosted analytics layer or a visibility tracker, start with the comparisons.

Sources: Search Engine Land: How to map AI search prompts to every stage of the sales funnel (Casey Nifong, Aug 31, 2026) · Search Engine Land: GSC AI performance reports and Search generative AI control rolling out globally (Barry Schwartz, Aug 31, 2026) · NiceLookingData: AI traffic in GA4, how ChatGPT, Perplexity, Gemini and AI Mode referrals actually show up (Jul 10, 2026), incl. Google's Default Channel Group documentation on the May 13, 2026 ai-assistant medium · Umami funnel report docs · MartechSignal: Your dashboard can't see AI search, here's the 5-layer fix (Aug 22, 2026)

## Related reading

- Your Dashboard Can't See AI Search , Here's the 5-Layer Fix
- Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook
- Your AI Marketing Agent Doesn't Need Better Prompts
## Related tools

- Profound - Enterprise AI marketing platform: answer-engine visibility plus drafting agents
- Nimt.ai - AI search tracking across 8 models with an agent that writes, fixes, and outreaches
- Ahrefs - Brand Radar tracks brand mentions and citations across AI answers, YouTube and Reddit
## Comparison guides

- Best AI SEO tools for AI visibility (2026)
- Best workflow automation tools (2026)
## Glossary terms

- AI Visibility
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: Analytics Tracking Automation
