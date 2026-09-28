# Microsoft Just Removed the Steering Wheel From Search Ads


| Decision | Before this week | Where it lives now |
| --- | --- | --- |
| **Who sees your ad** | Your keyword list, your match types | Search term matching, if you opt in |
| **What the ad says** | Your written assets | AI-generated variations, selected at auction |
| **Where the click lands** | Your final URL | Final URL expansion picks the page |
| **What a click can cost** | Max CPC, set by hand | Gone for new standalone campaigns, Oct 1 |

TC **[Tim Christensen](/authors/tim-christensen/)**

ADVERTISING · MICROSOFT · 9 MIN

## Microsoft Just Removed the Steering Wheel From Search Ads

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Microsoft Just Removed the Steering Wheel From Search Ads

AUG 31, 2026 · Updated SEP 09, 2026

Filed under [Advertising & Paid Media](/categories/advertising/)

Microsoft Advertising made two announcements in the same week, and neither one is dramatic on its own. On August 19, the platform began rolling out AI Max globally, a suite that lets its AI pick your search queries, write ad variations, and choose landing pages. The next day, advertisers got an email: starting October 1, new standalone campaigns using Maximize Conversions, Maximize Conversion Value, or Maximize Clicks can no longer carry a Max CPC bid limit. One announcement adds automation. The other removes the last price control an advertiser could set by hand.

Search Engine Land covered them as two product updates. They are one story. Read together, they answer a question nobody asked out loud: how much of the campaign should the advertiser still be driving?

## What AI Max actually does

AI Max is a single toggle on a Search campaign that switches on three features at once, and Microsoft wants you running all three together:

- **Search term matching** expands your reach past your keyword list. It reads your keywords, ads, and landing pages, adds intent and contextual signals, and enters you into searches you never bid on, including conversational queries in Bing's AI experiences and Copilot.
- **Text customization** takes your existing assets and website content, generates additional message variations, and picks the combination it thinks fits each auction.
- **Final URL expansion** stops sending every click to the page you chose and routes people to whichever page on your site Microsoft decides matches their intent.
That is the full decision chain of a search ad. Who sees it, what it says, where the click lands. Before this week, an advertiser set all three by hand.

Microsoft is not presenting this as a takeover. Navah Hopkins, the Microsoft Ads Liaison, wrote that "brand controls and reporting are critical to trusting AI as a partner in campaign management," and the launch ships with term exclusions for generated text, URL rules, ad group settings, and a new search term landing page report that shows which query landed on which page. AI Max is opt-in for new and existing campaigns. Every one of those caveats matters, and every one of them has an expiration date. More on that below.

## The quieter change: no bid cap on new campaigns

The email went out on August 20 and was easy to miss. "Max CPC will no longer be available when creating new non-portfolio campaigns," Microsoft wrote. From October 1, if you build a new campaign on standalone Maximize Conversions, Maximize Conversion Value, or Maximize Clicks, you cannot attach the one number that says "never pay more than this for a single click."

Hopkins' explanation, posted on LinkedIn: advertisers who use conversion-based bidding with target CPA and target ROAS "have an easier time meeting their goals than those who rely on legacy controls like Max CPC," because Max CPCs "override stated goals and can lead to spend pacing irregularities." Microsoft encourages advertisers to run optimization experiments removing Max CPC now, so they can see how campaigns behave before the option disappears.

Note what survives. Campaigns created before October 1 keep their Max CPC settings. Portfolio bid strategies, Target Impression Share, and eCPC keep the control too. So the ceiling is not being torn out of existing accounts. It is being removed from the path every future campaign has to walk down.

## Why the pair matters

Taken one at a time, both changes have a reasonable defense. Together they close the loop:

Max CPC deserves a moment on its own, because it was never a performance tool. It was a seatbelt. People used it on low-volume Bing queries where a single bad match could mean a nine-dollar click from a search that had nothing to do with the product. Search Engine Land put it plainly: this removes a safeguard against unexpectedly expensive clicks, and advertisers will now lean on budgets and conversion targets instead.

Microsoft's complaint that Max CPC "overrides stated goals" is a true statement. It is also a description of what a control is for. A ceiling overrides the system's judgment about your money on purpose. That is the whole point of owning one. When the platform calls your last manual safeguard a source of "pacing irregularities," it is telling you that smooth spend matters more to it than your comfort with any individual click.

**"Opt-in" has a short half-life on ad platforms.** Advertisers already using autogenerated text assets or Predictive matching did not get to opt in to AI Max. Microsoft moved those features under the AI Max umbrella and switched the settings on in their campaigns. The Max CPC email closes with "further updates on Max CPC will be provided in the future," which is platform language for: existing campaigns keep the ceiling for now, and "for now" is not a promise. The toggle you leave off this quarter may be the default you audit next year.

## Give Microsoft what it is owed

This is not a robbery, and pretending otherwise would be lazy. AI Max is genuinely optional today. Existing campaigns lose nothing on October 1. Portfolio strategies keep Max CPC, which gives sophisticated accounts a workaround. The reporting Microsoft shipped with the launch, especially the landing page report showing which query mapped to which page, is more transparency than the equivalent Google features offered at their launch. And the underlying argument has some truth in it: a Max CPC set too low can starve a conversion-based bidding strategy of the auctions it needs, and target-based bidding does outperform manual caps in most head-to-head tests.

Microsoft is also not inventing this playbook. Google set its own AI Max migration timeline for Search campaigns starting in September, automatically moving campaign-level broad match and automatically created assets into the same umbrella. Bing is following the industry's center of gravity. The direction is not a Microsoft decision. The direction is the industry.

That is precisely why it deserves a skeptical read instead of a product-update read. When both platforms walk the same road, the question for the practitioner is not whether the road exists but who is driving by the time you reach the end of it.

## What is left for the human in the loop

More than the headlines suggest, less than the job description says. The levers that survive October 1:

**Budgets.** Daily and lifetime budgets are the last hard number the machine cannot talk its way around. If you run Microsoft Ads without a ceiling on clicks, your budget is now your ceiling. Size it for the worst auction the algorithm might find, not the average one.

**Targets, used as levers rather than promises.** Hopkins points out that campaigns can over-achieve on target CPA and target ROAS regardless of budget status, and suggests conversion value rules as a way to steer the algorithm. That is a real input, but it only works if your conversion values are honest. Feed it self-reported conversions and you are handing the machine a map you drew yourself.

**Exclusions and URL rules.** Negative keywords, term exclusions for generated text, and URL restrictions are now the steering. They used to be hygiene. They are the difference between "AI finds high-intent queries" and "AI spent the budget on a query containing your competitor's refund policy."

**Measurement that lives outside the platform.** We argued that [attribution was always a fiction](/blog/multi-touch-attribution-was-always-a-fiction/) and the defensible number is what your own systems confirm. That argument gets sharper every time a platform removes a control and asks you to trust its targets instead. The gap between Microsoft-reported conversions and revenue your finance team recognizes is where the truth about automated bidding lives.

**The experiment Microsoft is suggesting, run on purpose.** Hopkins encourages testing Max CPC removal via optimization experiments before October 1. Do that test, and read it for what it is: a preview of your campaign's behavior once the steering wheel is gone. If the version without the cap spends more for the same conversions, you have your answer about what the change is for.

**The verdict: the machine still needs a driver, but the controls are moving behind a panel only Microsoft can open.** AI Max hands query selection, creative, and landing pages to the platform's models, and the Max CPC removal takes the last per-click price limit off new campaigns. Both are defensible as product decisions. Both point the same way. The advertiser's job is being rewritten from driving to instrumentation: set the budget, set honest targets, maintain the exclusions, and verify the outcome with numbers the platform did not generate. Do that and you can run AI Max with the toggle on and sleep at night. Skip it and you are not managing a campaign. You are funding one.

### Ad platforms, cataloged and compared

Advertising platforms and the measurement layer that keeps them honest. Pricing and AI feature breakdowns side by side, so you can see what each one still lets you control.

**Sources:** [Search Engine Land: Microsoft Advertising rolls out AI Max globally for Search campaigns](https://searchengineland.com/microsoft-advertising-rolls-out-ai-max-globally-for-search-campaigns-485530) · [Search Engine Land: Microsoft Advertising removes Max CPC from new standalone bidding campaigns](https://searchengineland.com/microsoft-advertising-removes-max-cpc-from-new-standalone-bidding-campaigns-485598) · [Navah Hopkins on LinkedIn: AI Max rollout](https://www.linkedin.com/posts/navahhopkins_ai-max-is-here-microsoft-advertising-has-share-7495901209418088449-W0t-/) · [Navah Hopkins on LinkedIn: Max CPC changes](https://www.linkedin.com/posts/navahhopkins_microsoft-advertising-is-investing-extensively-share-7496203436984627201-uiIA/) · [Search Engine Land: Google sets AI Max migration timeline for Search campaigns](https://searchengineland.com/google-sets-ai-max-migration-timeline-for-search-campaigns-485006)

## Related reading

- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
- [Your Dashboard Can't See AI Search, Here's the 5-Layer Fix](/blog/dashboard-cant-see-ai-search-5-layer-fix/)
- [The AI-search funnel map GA4 won't give you](/blog/ai-search-funnel-map-ga4-wont-give-you/)
## Related tools

- [Albert AI](/tools/albert-ai/) - Autonomous AI platform that manages and optimizes digital advertising campaigns
- [Revive Adserver](/tools/revive-adserver/) - Free open source ad server for publishers, ad networks and advertisers
- [Nosto](/tools/nosto/) - AI-powered ecommerce personalization with product recommendations and merchandising
## Comparison guides

- [Best n8n alternatives (2026)](/alternatives/n8n/)
- [Best Zapier alternatives (2026)](/alternatives/zapier/)
## Glossary terms

- [DSP](/glossary/dsp/)
- [SEO](/glossary/seo/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: [SuiteCRM](/tools/suitecrm/)

**MartechSignal**, written by [Tim Christensen](/authors/tim-christensen/)


```json
{
  "@context": "https://schema.org",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelectors": [
      "h1",
      "article h2"
    ]
  },
  "@type": "BlogPosting",
  "headline": "Microsoft Just Removed the Steering Wheel From Search Ads",
  "description": "Microsoft Advertising made two announcements in the same week, and neither one is dramatic on its own. On August 19, the platform began rolling out AI.",
  "author": {
    "@type": "Person",
    "name": "Tim Christensen",
    "url": "https://martechsignal.com/authors/tim-christensen/",
    "@id": "https://martechsignal.com/authors/tim-christensen/#person",
    "sameAs": [
      "https://www.linkedin.com/in/tchristensen78",
      "https://github.com/timchr78"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://martechsignal.com/#organization",
    "name": "MartechSignal",
    "url": "https://martechsignal.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://martechsignal.com/logo.png"
    }
  },
  "datePublished": "2026-08-31",
  "dateModified": "2026-09-09",
  "mainEntityOfPage": "https://martechsignal.com/blog/microsoft-search-ads-steering-wheel/",
  "image": {
    "@type": "ImageObject",
    "url": "https://martechsignal.com/og/microsoft-search-ads-steering-wheel.png",
    "width": 1200,
    "height": 630
  },
  "isPartOf": {
    "@type": "Blog",
    "@id": "https://martechsignal.com/blog/#blog"
  },
  "inLanguage": "en",
  "wordCount": 1702,
  "articleSection": "advertising"
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://martechsignal.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://martechsignal.com/blog/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Microsoft Just Removed the Steering Wheel From Search Ads",
      "item": "https://martechsignal.com/blog/microsoft-search-ads-steering-wheel/"
    }
  ]
}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
