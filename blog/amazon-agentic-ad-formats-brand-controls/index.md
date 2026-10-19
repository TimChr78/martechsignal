# Amazon's Agentic Ads Ship With Brand Controls

AI · ADVERTISING · 7 MIN

## Amazon's Ad Agents Come With Instructions. Google's Came With Promises.

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Amazon's Ad Agents Come With Instructions. Google's Came With Promises.

OCT 09, 2026

Filed under [Advertising & Paid Media](/categories/advertising/)

Two stories ran on AdExchanger the same day, September 29. [James Hercher covered Amazon's unBoxed announcements](https://www.adexchanger.com/platforms/amazon-gets-conversational-with-new-agentic-ad-formats-and-brand-controls/) in San Francisco, where the company turned its ad platform into a chatbot and launched conversational ad formats. [Joanna Gerber covered OpenAI's ad lead](https://www.adexchanger.com/ai/openai-says-sponsored-chats-are-the-future-but-publisher-monetization-isnt-a-priority/) telling Programmatic IO in New York that sponsored agents are the future of AI-native advertising.

Read together, they describe the same move arriving with two different sets of paperwork. Set next to [Google's August release](/blog/google-ad-agents-control-gap/), which shipped agentic features with a "stay firmly in the driver's seat" promise and no control layer, Amazon's version is the same movie with a different ending.

## What Amazon actually announced

The scale of the rebrand is easy to miss. The [Amazon DSP](https://advertising.amazon.com/) becomes a default agentic chatbot experience, and the Amazon Ads console itself is renamed the Amazon Ads Agent. Hercher's piece gives the buying side one line and moves on, and none of the brand-control machinery below applies to it. The shopping side carries the detail:

- **Sponsored Prompts**, Amazon's first chatbot ads, work like Sponsored Listings: they suggest a product in response to a search or a recent purchase.
- **Branded Conversations** turn a sponsored prompt into a multi-turn shopping conversation "informed by brand-provided inputs," in the words of Amjad Jbara, director of applied science for sponsored products at Amazon Ads.
In the unBoxed demo, a shopper searching "coffee maker" sees a sponsored "Help me decide" prompt. Amazon generates the prompt text itself; the sponsored label is the disclosure. Clicking it opens a conversation with suggested follow-ups like "works with capsules" and "maximum automation," rendered in the brand's colors, fonts and imagery.

One detail in that demo deserves more attention than the branding options. Hercher notes that responses get whittled down early, "often even quickly identifying one particular product, which is sponsored."

On a search results page, a sponsored listing competes against visible alternatives. In a Branded Conversation, the agent narrows to a single product, and that product is the one paying. The alternatives never appear. Whether shoppers register that difference is an open question the announcement does not address.

## What brands get to tell the agent

Amazon's control mechanism for these conversations is a new input layer called Conversational Briefs. Advertisers can tell Amazon which products are often purchased together, and a free text field carries product descriptions, features and use cases into the agent's recommendations.

The edges are drawn just as clearly. Hercher asked whether a brand can make its favorable reviews more visible in AI results or feed them into a Branded Conversation, and Jbara's answer was "No."

OpenAI's Sponsored Agents, announced earlier in September, sit in an interesting spot next to this. The brand supplies the agent's entire knowledge base, which Colleen Coulter, OpenAI's global ad solutions lead, says keeps responses accurate and brand-safe. As of the September 29 coverage, OpenAI has disclosed no equivalent of Amazon's review restriction, because it has no review graph to restrict.


|  | Amazon, Branded Conversations | OpenAI, Sponsored Agents |
| --- | --- | --- |
| **Format** | Multi-turn shopping chat inside Amazon's own assistant | Chat with a brand-sponsored agent after clicking an ad in ChatGPT |
| **Brand input** | Conversational Briefs: co-purchase pairings, free-text product details | The knowledge base: product feed, help center, brand-supplied corpus |
| **Off limits to the brand** | Reviews. Brands cannot pick which ones the AI surfaces | Nothing comparable disclosed yet |
| **Where trust signals live** | Amazon's review graph, fed by a paid review-collection product | The brand's own materials, so accuracy is the brand's problem |

The review restriction pairs with a second announcement. Request Reviews for Sponsored Ads nudges buyers to leave ratings for products with fewer than 1,000 reviews. It runs on cost per click, appears on the homepage, the order page and in email confirmations, allows no incentives such as samples or discounts, and caps at 1,000 collected reviews. You can pay for a click that never produces a review, and you pay the same whether the reviews come back glowing or brutal.

Put those two together and the design is legible. Amazon treats reviews as shopper data, not brand copy. The one input that most changes how the agent talks about you is the one you cannot edit, while a paid product exists to grow it. Brands get real inputs into the agent, and Amazon keeps the inputs that carry trust.

## The Google comparison, one month later

[Google's agentic announcement in August](/blog/google-ad-agents-control-gap/) came with the opposite paperwork. Ask Advisor reads accounts, summarizes and recommends, and Google's framing promised advertisers would stay "firmly in the driver's seat." Nobody's money moves yet. But when practitioners mapped the roadmap, approval workflows and guardrails turned out to be custom builds, something agencies assemble themselves if they have the engineering budget. The platform shipped interpretation. The control layer shipped as homework.

Amazon's release hands over a written contract instead: what you may tell the agent, what you may not, and what happens if you lie to it. On that last point, Jbara says Amazon "will give feedback" through the console when an advertiser submits false or improper information. A contract you can argue with beats a slogan you cannot. It also locks in Amazon's side of the argument, which is the part brands should read twice.

## The value question Amazon never has to face

[Sponsored Agents](/blog/openai-agent-ads-spending-without-you/) are the public version of the ad type spotted in ChatGPT Ads Manager in July, where a click opens a conversation instead of a page. Advertisers get a format that needs no landing page and captures leads inside the chat. It also moves the burden of proof onto content someone else paid to create, and OpenAI's answer to that is thinner than Amazon's.

Gerber's piece lays out the tension. Publishers are watching search traffic fall, get no baseline payment when AI trains on their content, and are told that citations plus engagement "insights" make up the difference. ChatGPT Ads recently passed a $1 billion run rate (checked October 9, 2026, per AdExchanger), which is real money and still a long way from the $100 billion ad revenue goal by 2030 that the same outlet reports OpenAI is chasing. Asked point blank whether that goal is real, Coulter declined to comment, citing OpenAI's filed S-1.

Amazon never faces this question because its loop is closed. The shopper, the purchase history, the reviews and the conversation all live inside one company's walls. OpenAI's conversational ads stand on an open internet it does not pay for, at least not at baseline. The formats are near-identical; the foundations are not. That difference will shape these products more than any demo.

For brands, Amazon's arrangement is the better deal on the table so far. Real inputs into what the agent says about your products, a stated rule for what you cannot touch, and a console reprimand instead of a silent account penalty when you step over the line. It is control as Amazon defines it, and the definition deserves scrutiny: the sharpest lever stays platform-owned while Amazon sells you a cost-per-click product to grow it. But a written contract beats a driver's-seat slogan. Take the inputs and document what you fed the agent, because the contract itself looks like the negotiation for the next year.

Tools linked in this post: [Amazon Ads](https://advertising.amazon.com/) | [ChatGPT](https://chatgpt.com/)

## Related reading

- [OpenAI Isn't Building Ads. It's Building Agents That Spend Money Without You.](/blog/openai-agent-ads-spending-without-you/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
- [Rogue agents, watchdog chips, and nobody accountable: the trust debate in four acts](/blog/rogue-ai-agents-trust-debate/)
## Related tools

- [Smartly.io](/tools/smartly-io/) - AI advertising platform spanning creative production, media buying, and measurement
- [Growth Lab](/tools/growth-lab/) - Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex
- [Scrunch](/tools/scrunch/) - The AI Customer Experience Platform: monitor, optimize and serve your site to AI agents
## Comparison guides

- [Jasper vs Writer (2026): pricing, AI features, verdict](/vs/jasper-vs-writer/)
- [Matomo vs PostHog (2026): web analytics or product analytics](/vs/matomo-vs-posthog/)
## Glossary terms

- [DSP](/glossary/dsp/)
- [AI Visibility](/glossary/ai-search-visibility/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: [Brevo](/tools/brevo/)

**MartechSignal**, written by [Tim Christensen](/authors/tim-christensen/)
