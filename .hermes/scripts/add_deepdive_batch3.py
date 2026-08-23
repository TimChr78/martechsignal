#!/usr/bin/env python3
"""Batch 3: add deep_dive (hands_on + verdict) to 30 martechsignal tool pages."""
import json

DD = {
"adcreative-ai": {
 "hands_on": [
  "Upload your brand assets and logo, tell AdCreative.ai who you sell to, and it generates dozens of image and video ad variations in minutes, each with a predicted performance score. That is the whole pitch, and it holds up when the bottleneck is volume: teams that test ten creative angles a week go from a two-week designer and copywriter cycle to a working session. The scoring rewards proven formats, so you spend your human time on the winners.",
  "The limits show up in the details. The prediction score is a model estimate, not a guarantee, and output drifts toward the generic if your brand assets are thin, so higher-end brands still want a designer to pass over the finalists. Video generation is improving but trails specialist tools. Pricing runs on credits, and heavy testing burns through the top tiers quickly, so the monthly cost grows with your iteration speed."
 ],
 "verdict": "Buy it when ad volume is your bottleneck and speed matters. Skip it if your brand needs art direction no template can give."
},
"ai-business-skills": {
 "hands_on": [
  "AI Business Skills drops 63 marketing skills into Claude Code, split between Vietnamese-market and global editions, plus a Design Master skill covering eight design types from personal brand to infographic. Install once and your agent gets structured playbooks with Vietnamese 2025-2026 benchmarks, budget allocations, and platform context where Facebook and TikTok dominate. The pack comes from Over Powers Agency, a working Vietnamese shop, so the workflows carry real campaign patterns.",
  "The trade-off is that one agency's playbook shapes every skill. The global-market entries carry less differentiation than the Vietnamese ones, and quality varies across the 63, so you will keep some and rewrite others. It is MIT-licensed and free, which makes the trial cost a single clone. VN teams get the clear win; everyone else gets a solid starting point to customize."
 ],
 "verdict": "The strongest free skill pack for Vietnamese-market marketing teams. Global agencies will find it useful mainly as a starting point."
},
"ai-marketing-claude": {
 "hands_on": [
  "Type /market audit with a URL and five parallel agents score content, conversion optimization, SEO and discoverability, competitive positioning, and brand trust, each out of 100, and return a structured report in minutes. Add reportlab and the same run produces a client-ready PDF. For freelancers and small agencies this compresses a paid audit into an afternoon, and the consistency is repeatable across prospects. The pack ships 15 commands, with /market copy earning its keep daily.",
  "The caveat: the 0-100 scores are heuristics from the agents, not measured benchmarks, so the report needs a human read before it goes to a prospect. Output quality tracks whatever model you run, and brand-specific nuance still requires edits. It is open-source, so you can tighten the scoring prompts to your own methodology. Audit outputs win clients, but a steady feed of on-brand copy is what keeps them."
 ],
 "verdict": "Best as a proposal-generation engine for agencies selling audits. For steady content work, the writing skills are the lasting value."
},
"albert-ai": {
 "hands_on": [
  "Albert runs paid media the way a trading desk runs markets: give it accounts, budgets, and conversion goals, and it plans, launches, and optimizes campaigns across search, social, display, and video on its own. The engine ingests creative, audience, and conversion data, then runs micro-experiments on audience, creative, bid, placement, and timing. Teams that trust automation get genuinely hands-off paid media. Albert has been at this since 2012, so the autonomy claims carry real mileage.",
  "It only works well when your conversion signal is strong and your budget is big enough to feed the experiment engine. Brand safety and creative direction still need human review, because an autonomous optimizer will happily burn spend on whatever converts. Pricing is enterprise and opaque, and small accounts starve the system of the data it needs, so mid-market teams often watch it struggle rather than shine."
 ],
 "verdict": "Strong for enterprise media teams with large budgets and mature conversion tracking. Smaller advertisers cannot feed its experiment engine."
},
"alwrity": {
 "hands_on": [
  "ALwrity is a self-hosted Python platform that generates blog posts, social content, email copy, and ad creative, and grounds that output in SEO research, competitor analysis, and web scraping instead of pure model luck. Install it on your own infrastructure and it replaces several content and SEO subscriptions with one system you control, with no per-seat fees and full data ownership. For privacy-minded operators that trade is attractive on its face.",
  "The cost of that control is operations. You own installation, updates, and reliability, and the polish of hosted platforms is absent. The star count, roughly 1,100, reflects a niche community, so troubleshooting is mostly on you and documentation is thinner than commercial rivals. Technical marketers comfortable on a server will feel at home. Marketers without a dev teammate should not start here."
 ],
 "verdict": "A capable self-hosted content engine for technical marketers. Everyone else gets better results from maintained hosted tools."
},
"analytics-tracking-automation": {
 "hands_on": [
  "Give this skill a URL and it walks the full GA4 and GTM setup: it analyzes the site, groups pages by business purpose, designs a GA4 event schema, produces GTM-ready outputs, and runs you through verification before anything goes live. Shopify storefronts get their own handling. A workflow that normally costs a $2,000 consultant becomes a session that leaves reviewable artifacts at every step, so nothing happens invisibly.",
  "The honest caveats: the schema it proposes is a starting point, not the final word, and your team should sign off before publishing, since a bad event model is worse than none. The project is young with a small community, and the skill is only as current as the GA4 interface it documents. For teams stuck with no tracking at all, it is a fast rescue that beats another quarter of guessing."
 ],
 "verdict": "Free and fast if tracking keeps slipping through the cracks. Review every schema it proposes before publishing anything."
},
"anyword": {
 "hands_on": [
  "Anyword's whole argument is measurable copy: paste a draft and a score on a 0-100 scale, trained on millions of real campaigns, tells you how the copy will perform before you send it. Email, ads, landing pages, and social each score against their own benchmarks, and the suggestion engine tightens weak lines. It sits on top of any LLM, so teams already using ChatGPT or Jasper can layer the scoring on without switching tools.",
  "Treat the score as a strong prior, not a prophecy. The model rewards copy patterns that historically convert, which pushes you toward consensus phrasing, and pricing is per seat, so a full growth team clears the entry tier fast. Writers with a mature process and their own testing rhythm will find it redundant. The API, though, makes it easy to slot scoring into an existing content pipeline."
 ],
 "verdict": "Valuable when you need an instant, numbers-based copy check across many channels. Established writers can pass."
},
"bloomreach": {
 "hands_on": [
  "Bloomreach bundles what most commerce stacks sell separately: campaign orchestration, site search and merchandising, and a customer data engine that stitches behavioral, transactional, and demographic data into one profile. For retailers drowning in point solutions, one contract and one profile graph is a real simplification, and it operates across email, SMS, web, mobile app, and paid channels. Founded in 2009, it carries two decades of ecommerce data plumbing behind the AI polish.",
  "Simplification has a price. Implementation is a services-led project, the platform expects dedicated teams, and pricing sits at enterprise levels, so mid-market stores feel the weight before they feel the value. Search and personalization quality depends on the data you feed the engine, and the breadth means months of tuning before the unified profile changes how you sell. This is a platform decision, not a tool purchase."
 ],
 "verdict": "The right platform for large retailers consolidating search, CDP, and messaging. Mid-market stores will find it heavy."
},
"brandwatch": {
 "hands_on": [
  "Brandwatch's strength is listening at scale: it analyzes billions of conversations across social, blogs, forums, and news, and turns them into trend, sentiment, and competitive intelligence your strategy team can act on. The query layer lets researchers ask questions in natural language instead of writing regex, and the management suite around it handles publishing and influencer work. Listening is the reason you buy it, and it is the deepest engine in the category.",
  "The catch is scope. This is an enterprise suite priced for enterprise budgets, and the scheduling and engagement features are competent but secondary to specialists like Sprout or Buffer. Large query datasets demand real research skills, or you drown in dashboards. Buy it for the insight engine and keep a lighter, cheaper tool for daily posting. Small teams should not touch it."
 ],
 "verdict": "The listening leader for enterprise consumer-intelligence teams. Posting-only teams should pick a cheaper scheduler instead."
},
"buffer": {
 "hands_on": [
  "Buffer is the simplest serious scheduler on the market, and its free tier is the best in the category: three channels, scheduling, link shortening, and a landing page builder at no cost. The AI assistant drafts posts and suggests times, and the interface stays clean where rivals pile on menus. Small teams get posting done in minutes without a training session, which is exactly the promise the product makes and keeps.",
  "The business is simplicity, so the analytics stay shallow, listening barely exists, and advanced workflows like multi-brand permissioning or approval chains are thin. You outgrow it the moment you need reporting depth or serious collaboration. For its real audience, solo creators and small social teams, nothing else beats the price-to-effort ratio, and the free tier costs nothing to confirm that for yourself."
 ],
 "verdict": "Start here, especially on the free tier. Plan to graduate to Sprout when reporting depth and approvals matter."
},
"chatbotx": {
 "hands_on": [
  "ChatbotX is the open-source answer to ManyChat: self-hosted chat marketing with flows for lead capture, qualification, and automated sales conversations across messaging channels, plus an agentic AI layer that moves past rigid scripts. The API opens custom integrations with your CRM and product stack, and because you host it, customer data never leaves your infrastructure. The repo sits at 524 stars, early but active, and the MIT license makes experimentation free.",
  "That ownership is the whole trade. Deployment, maintenance, scaling, and security are yours, the community is small next to ManyChat's, and there is no vendor support to call. Non-technical marketers will stall at installation. Teams with engineering muscle and privacy requirements get the control they want without licensing fees, which is a fair swap only if you count your own time as cheap."
 ],
 "verdict": "Right for technical teams that want ManyChat-style automation without lock-in. Everyone else should stay hosted."
},
"chatfuel": {
 "hands_on": [
  "Chatfuel is built around the social sales funnel: comment-to-DM automations pull engagement into conversations, DM funnels capture and qualify leads, and product catalog conversations close sales inside Instagram, WhatsApp, Facebook Messenger, and TikTok. Over 18,000 businesses run reply-and-convert loops on it, and the platform has been at this since 2015, so the flow library is mature and the channel quirks are already worked out.",
  "It is flow automation first and open-ended AI second, so builders who want free-form chatbot behavior will feel constrained. Pricing starts around $39 a month and per-channel plans stack up when you run several networks, with advanced features shifting by tier. DTC brands that sell in DMs get the most value; B2B lead capture feels cramped next to general-purpose chatbot builders."
 ],
 "verdict": "A strong fit for DTC brands selling through DMs on Instagram and TikTok. B2B teams need a more general builder."
},
"clerk-io": {
 "hands_on": [
  "Clerk.io sells personalization as four modular products: site search that routes around zero-result dead ends, product recommendations across every page type, behavior-triggered email feeds, and dynamic audience segments built on intent signals. Each module installs over your existing store and the models learn from browsing and sales data quickly, so you buy only the pieces you need. That modular entry is the honest way into personalization.",
  "The modular model means the full stack gets expensive, and merchandising rules need real configuration to stop recommendations going generic. The engine needs traffic to learn from, so small catalogs and low-traffic stores see modest gains while paying the same integration effort. It suits mid-size ecommerce with genuine sales volume and a merchandiser who will tune the rules. Plan the rollout module by module instead of switching everything at once."
 ],
 "verdict": "Solid modular pick for mid-size stores with traffic to feed the models. Thin catalogs get little from it."
},
"codex-seo": {
 "hands_on": [
  "Codex SEO is the OpenAI Codex port of Claude SEO from the same author, covering the full surface: technical audits, on-page analysis, E-E-A-T content checks, schema, Core Web Vitals, GEO and AEO for AI search, backlinks, local and ecommerce SEO, hreflang, and semantic clustering. The difference is the runtime: 24 TOML agent profiles, deterministic headless runners, and a Python virtualenv under ~/.codex instead of Claude's subagent model.",
  "Everything depends on your team's stack. If you run Codex, you get the same workflows Claude shops enjoy, 26 of them across the suite and 534 stars and climbing. If you run Claude Code, stay with the original. Setup is developer work: venv management, agent config, and no UI or support when things break. The output ceiling is whatever model you point at it."
 ],
 "verdict": "The right SEO skill pack for Codex-based teams. Claude Code users should stick with the original Claude SEO."
},
"contentbot": {
 "hands_on": [
  "ContentBot's differentiator is AI Flows: multi-step automations where the AI generates copy, checks it against brand guidelines, formats for the target channel, and schedules or publishes, all in one pipeline. Over 200,000 users run this cheaper, workflow-first alternative to Jasper and Copy.ai, and for teams producing recurring content, removing the manual handoffs between tools is the win that matters. The free tier is enough to test one flow before you commit to a plan.",
  "Quality is where it yields. Output reads competent rather than distinctive, and long-form brand writing still favors Jasper, whose model templates run deeper. Flows need tuning so the guideline checks stay meaningful and the pipeline stops auto-publishing mediocrity. Teammates who review every draft will find the workflows save less than promised, so match it to your review culture before you commit."
 ],
 "verdict": "Good value for high-volume, template-driven content pipelines. Teams doing premium long-form writing should stay with Jasper."
},
"copy-ai": {
 "hands_on": [
  "Copy.ai stopped being a copywriter and became a GTM orchestration layer: prospecting, inbound, content, and deal execution workflows live in one surface. The Prospecting Cockpit is the flagship, bundling company research, enriched contacts, and personalized outreach, while the inbound side covers lead qualification and meeting prep. Content generation still exists, but it now feeds the workflows rather than standing alone as the product.",
  "The pivot means writing depth trails dedicated content tools, and heavy users feel the seat and credit pricing. It shines for small GTM teams that want research, outreach, and content in one place, and for agencies running many accounts from one cockpit. Pure content shops get more from a dedicated AI writer at a lower price, so match the purchase to the motion you run day to day."
 ],
 "verdict": "Buy it for the GTM workflows and prospecting cockpit, not for copywriting. Pure content teams have cheaper options."
},
"django-crm": {
 "hands_on": [
  "Django CRM, also sold as Bottle CRM, is a multi-tenant, self-hosted CRM on Django and SvelteKit covering leads, accounts, contacts, opportunities, campaigns, cases, and email marketing. The multi-tenant design is the standout for agencies running several brands or client books from one instance, and the API plus Django's ecosystem cover custom needs. No per-seat fees, roughly 2,400 stars, and an active release cadence.",
  "The AI layer is absent, which is fine only if you know that coming in. Email stays basic, integrations are whatever you build, and the UI is traditional rather than modern, with Twenty and SuiteCRM framing the trade-offs. Django shops get a pragmatic middle; teams without Django skills inherit a maintenance burden that cheap software never pays for. Budget for that engineering time before you count the savings from skipping per-seat fees."
 ],
 "verdict": "A sensible self-hosted CRM for Django teams managing multiple brands. Others get faster value from hosted CRMs."
},
"dynamic-yield": {
 "hands_on": [
  "Dynamic Yield, now under Mastercard, is the most decorated personalization vendor in the category: eight consecutive Gartner Magic Quadrant Leader placements, most recently 2026. Its Experience OS makes real-time decisions that match content, products, and offers to each visitor across web, mobile, email, and push, with A/B testing and recommendations layered in. The commerce heritage shows in how natively it handles product feeds and merchandising.",
  "Everything about it assumes scale. Contracts are enterprise, implementation runs through services, and the platform needs real traffic and a dedicated team before the personalization math pays off. Mastercard's ownership direction is still settling, so roadmap questions linger. Mid-market teams end up paying for capability they cannot staff, which is the classic enterprise-tool trap. Demo it against your real traffic before any contract talk."
 ],
 "verdict": "The safest enterprise bet in personalization, with the analyst streak to prove it. Too heavy for mid-market."
},
"email-marketing-bible": {
 "hands_on": [
  "The Email Marketing Bible is a 55,000-word skill file built by the founder of SmartrMail, an email SaaS that sent 6 billion messages before its acquisition, and it reads like a brain transplant for your agent: 908 cited sources, 19 industry playbooks, and 47 email designs. The agent stops guessing about deliverability, flow priority, and vertical benchmarks, and MCP controls reach into real ESPs.",
  "The install is heavy by skill standards, and the value lands only if your model reads and applies it, then does the actual sending work. You still own list hygiene, sender reputation, and compliance, because a knowledge base cannot rescue a dirty list. For DTC teams already running agents, this is the fastest deliverability education they will get, and the cited sources beat forum advice."
 ],
 "verdict": "The fastest path to email-competent agents, with real ESP control via MCP. List hygiene stays on you."
},
"freshsales": {
 "hands_on": [
  "Freshsales is the credible mid-market alternative to HubSpot for sales teams that want communication built in: native phone, email, and chat without bolt-on tools, plus Freddy AI doing lead scoring, deal insights, and predictive contact scoring from engagement patterns. The AI surfaces at-risk deals and ready leads without demanding a data science team, and pricing undercuts HubSpot at equivalent seats.",
  "The ecosystem is the gap. Freshworks' marketplace and integrations trail HubSpot's, the admin surface shows its age in places, and the AI needs transaction history before its scoring warms up. Marketing-heavy teams still lean HubSpot for the shared database. Sales-led mid-market buyers get a lot of CRM for the money, and Freddy AI is genuinely useful rather than a checkbox feature."
 ],
 "verdict": "The smart budget CRM for sales-led mid-market teams that want built-in phone and email. Marketing-led stacks still favor HubSpot's ecosystem."
},
"google-meta-ads-ga4-mcp": {
 "hands_on": [
  "This MCP server hands your AI agent read and write access to Google Ads, Meta Ads, and GA4: roughly 150 Google Ads tools for campaign, keyword, bidding, budget, and conversion work, 80-plus Meta tools across campaigns, creatives, lookalikes, and lead forms, and GA4 reporting to reconcile spend against conversions. You ask for a performance summary or a paused ad set and it executes, no dashboard hopping.",
  "The power cuts both ways. This is real spend and real changes executed from chat, so guardrails matter: review every write, keep human approval in the loop, and scope the API keys tightly. Setup means Google Cloud project work and a Meta app registration, so it is for teams comfortable with MCP plumbing. For those teams, the workflow compression is dramatic and the 1,000-plus stars show rapid adoption."
 ],
 "verdict": "High-value tooling for performance teams already running agents and MCP. Keep human approval on every write."
},
"growth-lab": {
 "hands_on": [
  "Growth Lab turns Claude Code or Codex into a growth operator: describe the outcome, and the agent reads your product from a codebase, prototype, or URL, researches real search queries, creates SEO pages around them, publishes, pings IndexNow, then reads the performance data and decides what to do next. It is a loop rather than one-shot generation, and the research and results share one workspace, so context stops leaking between tools.",
  "Publishing from an agent means you own the pipeline: hosting, deploys, and content review on your side, which is a real commitment. The project is young at 308 stars, and the results ceiling is your model's judgment, so weak pages can ship at loop speed if you skip review. The Xiaohongshu growth loops are a rare China-market angle in Western tooling."
 ],
 "verdict": "Promising for teams ready to run self-hosted SEO loops with agent review. Everyone else should wait for maturity."
},
"heap": {
 "hands_on": [
  "Heap's pitch is capture everything, analyze later: install one snippet and every click, pageview, form fill, swipe, and scroll is recorded, so you can run retroactive analysis on interactions you never tagged. That ends the classic pain of needing six months of data on a feature nobody instrumented. The Contentsquare acquisition adds digital experience analytics alongside the product analytics, widening the lens.",
  "Autocapture generates noise as surely as it generates coverage, so curation and chart hygiene become your job, and event volume drives pricing, which climbs faster than teams expect. Privacy review matters more than ever when everything is recorded. Teams with disciplined tagging may prefer Mixpanel's precision, but teams that keep discovering untagged events will find Heap forgiving in exactly the way they need."
 ],
 "verdict": "Choose it when you keep discovering untagged events after the fact. Disciplined taggers get more from Mixpanel."
},
"hootsuite": {
 "hands_on": [
  "Hootsuite is the enterprise social suite: one dashboard across 20-plus networks with bulk scheduling, a content library, AI-optimized post times, listening, employee advocacy, and social commerce. For multi-region teams, the permissions, approval flows, and governance are the point, and the 2026 AI layer across captions and publishing is the broadest in the category. This is the platform you buy when scale is the requirement.",
  "Scale has a price: entry plans start near $99 a month, the interface is dense, and small teams pay for governance features they never open. Listening and advocacy modules add on, so the full stack lands well above the entry number. If you are a five-person brand on three channels, Buffer or Later delivers the same posting with less friction and a fraction of the cost."
 ],
 "verdict": "The right call for multi-team, multi-brand social programs with governance needs. Small teams overpay for it."
},
"hypotenuse-ai": {
 "hands_on": [
  "Hypotenuse AI positions itself around product content: bulk on-brand product descriptions, category page copy, SEO metadata, and attribute enrichment across catalogs of thousands of SKUs, generated from minimal input like a product name, specs, and an image. A data cleaning layer standardizes messy product attributes first. For catalog-heavy retailers, this replaces a content team's grunt work in a way a general writer cannot.",
  "Input quality decides output quality: inconsistent feeds produce inconsistent descriptions, and credit-based pricing gets real at catalog scale, so budget before you scale. It is a specialist, not a general AI writer, and the long-form article side is shallow next to dedicated tools. Teams fighting duplicate and thin product copy across thousands of SKUs get the clearest win here. Start with one category and validate quality before scaling the whole catalog."
 ],
 "verdict": "A strong specialist for bulk product catalog content at scale. General writing needs are better served elsewhere."
},
"jasper": {
 "hands_on": [
  "Jasper has grown from a GPT-3 wrapper into an enterprise marketing workspace with over 100 specialized agents, and the flagship idea is Campaigns: one brief feeds brand context, audience data, and goals into agents that produce coordinated blog, social, email, and ad assets, with brand voice governance enforced across everything. Analytics track what the platform produces, closing the loop for teams that report on output.",
  "The brand controls are the reason enterprises pay, and the price has climbed with the repositioning, so freelancers and small teams pay for depth they never touch. Output still needs human editing to stand out, and agent sprawl can feel like overhead next to a raw model. Teams needing governed, on-brand, multichannel volume get the most value; solo users get more from a model plus prompts."
 ],
 "verdict": "Best for enterprises needing brand-governed, multichannel output at scale. Solo users get more from raw models."
},
"krayin-crm": {
 "hands_on": [
  "Krayin CRM is the Laravel-native open-source CRM: leads, contacts, organizations, pipeline, activities, and basic email integration, MIT-licensed with more than 23,000 GitHub stars, plus a multi-tenant SaaS edition for operators running several business units from one deployment. If your team already ships Laravel, it slots in without a new language, database, or deployment model, and you can fork and brand it freely.",
  "Simple is the whole story: no genuine AI scoring despite the marketing, no predictive analytics, basic IMAP and SMTP email rather than deep Gmail or Outlook sync, and sparse integrations you will build yourself. The UI reads as functional admin panel rather than modern design. For Laravel shops that want a self-hosted base to extend, it is the honest budget pick; others will feel the gaps."
 ],
 "verdict": "A solid Laravel-native base for self-hosted teams that will extend it. Everyone else gets more from hosted CRMs."
},
"line-harness": {
 "hands_on": [
  "L Harness is the zero-license alternative to the paid LINE marketing tools: step delivery with minute-level delays and conditional branching, tag-based segment broadcasts, LIFF forms, rich menus, behavior-based lead scoring, Google Calendar booking, and affiliate tracking with last-touch attribution, all deployed to your own Cloudflare account in about five minutes via the setup CLI. The software itself costs nothing, so the barrier to entry is Cloudflare comfort rather than budget.",
  "You still pay LINE's per-message fees and any Cloudflare usage past the free tier, and operations, updates, and incident response are yours, with no SLA to lean on. Documentation is Japanese-first, the project sits pre-1.0 at v0.21.x with 568 stars, and it has existed for only months. The MCP server for Claude Code control is genuinely unusual, but the use case is strictly Japan-focused LINE marketing."
 ],
 "verdict": "The first credible free alternative to L-Step for LINE marketing in Japan. Outside Japan there is no use case."
},
"langchain": {
 "hands_on": [
  "LangChain is the framework under a large share of AI agent software: n8n's AI Agent nodes run on it, and countless marketing AI tools wrap it. For developers it standardizes chaining LLM calls, giving models tools, and parsing structured output, which is why it passed 100,000 GitHub stars. Marketers never open it directly; they use the products built on top of it.",
  "The abstraction moves fast, breaking changes are part of life, and you own the engineering, deployment, and cost control. If you are building custom marketing agents, it saves enormous groundwork; if you are not a developer, the right move is to buy a product built on it rather than touch the framework. The huge community and documentation make it the safest framework bet available."
 ],
 "verdict": "For engineers building custom marketing AI: the standard foundation. Marketers should buy the products built on it."
},
"laudspeaker": {
 "hands_on": [
  "Laudspeaker is the open-source Braze alternative: self-hosted customer engagement with behavioral triggers, journey automation, welcome and activation flows, re-engagement emails, and in-app messages, with data that stays yours and an API your engineers can extend. More than 2,600 stars and an active repo keep it alive, and cloud plans exist if you prefer managed hosting over running it yourself. The onboarding flows cover the standard product-led growth playbook out of the box.",
  "The open-source bargain applies: deployment, maintenance, and reliability land on your team, and the message templates and channel coverage are thinner than Braze's catalog. It suits technical growth teams and privacy-constrained companies where lock-in is the bigger risk than ops effort. Non-technical marketers will bounce off the setup, and enterprises that need support should stay hosted. Judge your team's ability to run services before choosing self-hosted over cloud."
 ],
 "verdict": "The open-source Braze alternative for technical growth teams that want data ownership. Others go hosted."
}
}

def wc(p): return len(p.split())

TARGETS = list(DD.keys())
with open('tools/tools.json') as f:
    tools = json.load(f)

by = {t['slug']: t for t in tools}
missing = [s for s in TARGETS if s not in by]
print("missing slugs:", missing)
count = 0
for s in TARGETS:
    if s in by:
        by[s]['deep_dive'] = DD[s]
        count += 1
print("added deep_dive to:", count)

with open('tools/tools.json', 'w') as f:
    json.dump(tools, f, indent=2)

# word counts sanity
for s in TARGETS:
    dd = DD[s]
    for i, p in enumerate(dd['hands_on']):
        n = wc(p)
        if n < 60 or n > 100: print(f"LEN hands_on[{i}] {s}: {n}")
    v = wc(dd['verdict'])
    if v < 15 or v > 25: print(f"LEN verdict {s}: {v}")
print("word count check done")