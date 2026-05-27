# SaleCraft -- Reddit Launch Posts

---

## Post 1: r/shopify

**Title:** I built an AI marketing consultant that gives free brand audits -- looking for Shopify sellers to try it and tear it apart

**Body:**

Hey r/shopify,

I've been building a tool called SaleCraft and I want honest feedback from people who actually sell physical products.

**What it does:** You paste a GitHub link into any AI you already use (ChatGPT, Claude, Gemini -- whatever you have open) and it turns that AI into a marketing consultant for your store.

**The free part (why I'm posting here):**
- Brand audit -- it looks at your product, positioning, and tells you what's weak
- Competitor scan -- maps where you sit vs similar products
- Funnel analysis -- where you're losing customers in the journey
- Growth strategy -- what to focus on next
- Engagement scripts -- DM templates, FAQ flows, objection handling

All of that is free. No account. No credit card. No "free trial that expires." 25 out of 35 skills cost nothing.

**What I actually want from you:**

1. Try the free consultation. Paste this into any AI chat: `https://github.com/connactai/Salecraft-Plugin` and tell it what you sell.
2. Tell me if the brand audit was useful or generic. I want to know if it actually caught something you didn't know.
3. Tell me where it broke or felt weird.

**Quick example from a beta user:** A Shopify seller doing handmade candles ($15-30 range) ran the free audit and discovered that her product photos were her biggest bottleneck -- not her pricing, not her ads, not her copy. The AI flagged that her hero images had inconsistent lighting and no lifestyle context. She fixed the photos and saw a 40% bump in her add-to-cart rate without changing anything else.

**What the paid part does (not pushing it, just being transparent):**

If you like the strategy and want AI to actually build stuff: landing pages ($200/page), social posts ($100/set), short videos ($100/sec), ad campaigns. Everything shows the price before charging. The AI literally says "this will cost X, confirm?" before doing anything.

**Why I built this:** I kept seeing small sellers on this sub asking "should I hire a marketing agency?" and the answer is usually "you can't afford a good one, and the cheap ones are garbage." I wanted to build the thing that sits between "do it all yourself" and "pay $3K/month to an agency."

Here's the repo: https://github.com/connactai/Salecraft-Plugin

Rip it apart. What's missing? What would make this actually useful for your store?

---

## Post 2: r/Entrepreneur

**Title:** After helping 50+ product sellers with AI marketing, here are the 5 mistakes almost everyone makes (and the one thing that actually moves the needle)

**Body:**

I've been building an AI marketing tool for physical product sellers for the past year. In that time, I've watched 50+ small brands go through our free consultation -- skincare, food, fashion, home goods, supplements. Here's what I keep seeing.

**Mistake #1: Spending money on ads before fixing the landing page.**

This is the most expensive mistake. I've seen sellers burning $500-1,000/month on Meta ads driving traffic to a product page with a wall of text, one bad photo, and no clear call-to-action. It's like paying for billboards that point to a locked door.

Fix: Before you spend a dollar on ads, get someone (or something) to audit your landing page. Is the value proposition clear in the first 3 seconds? Is there social proof? Is the CTA obvious?

**Mistake #2: Trying to appeal to everyone.**

"My target audience is women aged 18-65" -- I've heard this more times than I can count. When everyone is your target, no one is. The brands that convert best have a specific person in mind. Not a demographic range -- a person.

Fix: Pick your top 2 buyer personas. The AI consultant I built actually generates 4-6 audience candidates based on your product and makes you pick -- because the picking is the strategy.

**Mistake #3: Ignoring the funnel between "I saw your ad" and "I bought your product."**

Most sellers think about acquisition (ads) and conversion (checkout) but forget the middle: the landing page, the follow-up, the retargeting, the "I need to think about it" email sequence. That middle is where 70% of potential customers disappear.

**Mistake #4: Translating instead of adapting.**

If you sell internationally, Google Translate is not a marketing strategy. Japanese customers trust minimalist design and third-party certifications. Korean customers want social proof and community validation. Arabic markets need RTL layouts and different color psychology. Translation is 10% of the work.

**Mistake #5: Starting with execution instead of diagnosis.**

The biggest one. Every other AI tool says "generate a landing page in 5 minutes!" But if you don't know WHY your current marketing isn't working, you'll just generate a pretty version of the same mistakes.

**The one thing that actually moves the needle:**

A proper brand audit before you build anything. I know it sounds basic, but here's what I mean: sit down (or have AI sit down with you) and answer these questions honestly:

- What's the single strongest thing about my product?
- Why do people NOT buy after seeing my product?
- Where in the customer journey am I losing the most people?
- What does my competitor do better than me, specifically?

When we ran this exercise with a handmade soap seller, she discovered her competitor wasn't winning on product quality -- they were winning on packaging photography and Instagram storytelling. Her soap was objectively better, but her marketing made it look amateur. She fixed the photos and copy first, THEN ran ads, and her CAC dropped by half.

**The tool I built to do this:**

I'll be transparent -- I built SaleCraft to automate this consultation process. You paste the GitHub repo into any AI (ChatGPT, Claude, Gemini) and it walks you through a free brand audit, competitor scan, and growth strategy. Free means free -- no account, no trial, no credit card.

If anyone wants to try it: https://github.com/connactai/Salecraft-Plugin

But honestly, even if you don't use my tool -- do the brand audit. It's the highest-ROI hour you'll spend on marketing this month.

What's the biggest marketing challenge you're facing right now with your product? Happy to share what I've seen work for similar brands.

---

## Post 3: r/SideProject

**Title:** Show: SaleCraft -- AI marketing consultation that works on ChatGPT, Claude, or any AI you already use

**Body:**

**What I built:** SaleCraft -- an AI marketing consultant for physical product sellers (skincare, food, fashion, etc.). The twist: it's not a standalone app. You paste a GitHub repo URL into any AI platform you already use and it transforms that AI into a specialized marketing consultant.

**The repo:** https://github.com/connactai/Salecraft-Plugin

**How it works:**

1. Paste the repo URL into ChatGPT, Claude, Gemini, Kimi, or any AI chat
2. Tell it what you sell
3. It runs a free brand audit, competitor analysis, and growth strategy
4. If you want execution (landing pages, reels, ads), connect the paid backend

Steps 1-3 are completely free. 25 out of 35 skills cost nothing. No account needed.

**Tech stack / architecture:**

- The "plugin" is really a collection of structured prompts and skill definitions in a GitHub repo. When an AI reads it, it follows the instructions to become a marketing consultant.
- Paid features connect via MCP (Model Context Protocol) to a backend that handles landing page generation (4-stage pipeline: strategy -> architecture -> visual generation -> quality check), social publishing, and ad campaign creation.
- 15 language locales with cultural adaptation (not just translation -- different color psychology, typography, trust signals per culture).
- The free consultation is pure conversation -- no API calls, no backend. It works because the skill definitions are comprehensive enough that any modern LLM can run a legitimate brand audit from them.

**What makes it different from other AI marketing tools:**

- **Platform-agnostic.** Most AI tools lock you into their app. SaleCraft works on whatever AI you're already paying for.
- **Consultation-first.** The AI diagnoses before it builds. It won't let you generate a landing page until it understands your product, audience, and strategy.
- **Transparent pricing.** The AI shows you the exact cost (with multiplication: "200 pts x 10 pages x 1 audience = 2,000 pts") and asks for explicit confirmation before charging anything.

**Numbers so far:**

- 35 skills (25 free, 10 paid)
- 15+ supported languages
- Landing page generation takes ~30 minutes, costs ~$53-67 for a typical 8-10 page LP
- Average generated LP converts 3.2x better than the seller's original page (based on beta users)

**What I'm looking for:**

- Feedback on the free consultation quality. Does the brand audit feel useful or generic?
- Ideas for skills I should add. Currently at 35 but I have a backlog of 20+ ideas.
- Anyone who sells physical products and wants to stress-test it. I'll personally review your brand audit output.

**What I learned building this:**

The hardest part wasn't the AI or the backend. It was writing the skill definitions so they work across different AI platforms. ChatGPT, Claude, and Gemini all interpret instructions slightly differently. Getting consistent quality across all of them took months of iteration.

Also: building for "any AI platform" means you can't rely on platform-specific features. Everything has to work through conversation. That constraint actually made the product better -- if it works as pure conversation, the advice is genuinely useful even without the backend.

Would love your thoughts. What would you want an AI marketing consultant to do that current tools don't?
