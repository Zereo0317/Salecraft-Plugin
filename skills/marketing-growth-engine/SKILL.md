---
name: marketing-growth-engine
description: |
  Growth strategy framework for physical product brands covering unit economics,
  channel selection, Marketing Mix Modeling, causal inference, and efficient growth
  principles. Integrates Sharp's Laws of Brand Growth, IPA effectiveness research,
  blitzscaling post-mortem analysis, and modern measurement frameworks.
  This skill should be used when the user asks about "growth strategy", "unit economics",
  "LTV/CAC ratio", "how to measure marketing ROI", "brand building vs performance marketing",
  "customer acquisition cost", "Marketing Mix Modeling", "how brands grow",
  "North Star Metric", "activation rate", "Rule of 40", "efficient growth",
  "PLG vs sales-led", "why is my CAC so high", "scaling my brand", "channel strategy",
  discusses marketing budget allocation, needs help choosing between brand and performance
  spending, or wants to understand whether growth metrics are healthy.
  Provides benchmark-backed diagnostic frameworks with specific numbers and thresholds.
  FREE -- no credits required.
version: 1.0.0
---

# Marketing & Growth Engine for Physical Product Brands

Provide growth strategy frameworks with benchmark numbers, measurement systems, and diagnostic checklists specifically adapted for physical product sellers. Not SaaS growth hacking -- tangible product economics.

**This skill is 100% FREE. No credits are deducted.**

## Core Principle

> Growth without unit economics is just expensive failure. Measure first, then scale what works.

Load `references/playbook.md` for complete frameworks, benchmark tables, and diagnostic checklists.

---

## When to Use

- User asks "how do I grow my brand?" or "is my growth healthy?"
- Before `plan-cgo-review` -- establish measurement framework
- After `growth-retro` -- diagnose why a campaign over/under-performed
- When user debates: brand building vs performance marketing budget split
- When user reports high CAC, low repeat rate, or stagnant growth

---

## Unit Economics: The Foundation

Before any growth strategy, establish unit economics health. Unhealthy economics + scaling = faster death.

### Physical Product Unit Economics Dashboard

| Metric | Formula | Healthy Threshold | Red Flag |
|--------|---------|-------------------|----------|
| **Gross Margin** | (Revenue - COGS) / Revenue | > 60% for DTC, > 40% for wholesale | < 30% |
| **CAC** | Total acquisition spend / New customers | < 1/3 of first-order AOV | > first-order AOV |
| **LTV** | AOV x Purchase frequency x Lifespan | LTV/CAC >= 3 | LTV/CAC < 1.5 |
| **CAC Payback** | CAC / Monthly gross profit per customer | < 12 months | > 18 months |
| **Repeat Purchase Rate** | Customers with 2+ orders / Total customers | > 30% (consumables), > 15% (durables) | < 10% |
| **Contribution Margin** | Gross margin - variable costs (shipping, packaging, payment fees) | > 40% DTC | < 20% |

### Diagnostic Flow

```
Step 1: Calculate gross margin
  -> Below 30%? Fix COGS before any marketing spend.
  -> Above 50%? Proceed to CAC analysis.

Step 2: Calculate CAC by channel
  -> Which channel has lowest CAC?
  -> Is any channel CAC > first-order AOV? Cut it.

Step 3: Calculate LTV (12-month cohort)
  -> LTV/CAC >= 3? Scale that channel.
  -> LTV/CAC 1.5-3? Optimize before scaling.
  -> LTV/CAC < 1.5? Fix retention before acquiring.

Step 4: CAC Payback period
  -> < 6 months? Aggressive growth is safe.
  -> 6-12 months? Moderate growth, watch cash flow.
  -> > 12 months? Cash flow risk. Fix unit economics first.
```

---

## The Brand/Performance Split: IPA 60/40 Rule

The IPA (Institute of Practitioners in Advertising) analyzed 996 campaigns and found the optimal split for long-term profit growth:

- **60% Brand Building**: Emotional, broad-reach, long-term memory building
- **40% Performance Marketing**: Rational, targeted, short-term activation

### Physical Product Adaptation

| Growth Stage | Brand % | Performance % | Rationale |
|--------------|---------|---------------|----------|
| Launch (0-6mo) | 30% | 70% | Need initial customers and data; performance proves product-market fit |
| Growth (6-24mo) | 50% | 50% | Balance acquisition with brand building; start loyalty programs |
| Scale (24mo+) | 60% | 40% | IPA optimal; brand reduces long-term CAC |
| Market Leader | 70% | 30% | Defend position through mental availability |

**Key insight from Sharp (How Brands Grow)**: Differentiation does NOT drive growth. **Mental availability** (being thought of in buying situations) + **Physical availability** (being easy to find and buy) = growth. Penetration (reaching new buyers) matters more than loyalty (getting existing buyers to buy more).

---

## Measurement: The MMM Revival

### Why MMM Came Back

Apple ATT (2021) + third-party cookie death = Multi-Touch Attribution (MTA) collapsed. Marketers lost cross-platform tracking. Marketing Mix Modeling (MMM) -- a 60-year-old statistical method -- returned as the primary measurement framework.

**Open-source tools**:
- Google Meridian: Bayesian MMM with geo-level data
- Meta Robyn: Automated MMM with ridge regression + evolutionary optimization

### MMM for Small Product Brands

Full MMM requires 2+ years of data and statistical expertise. For smaller brands, apply the principle with simpler methods:

1. **Geo-Lift Testing**: Run marketing in City A, not in City B (control). Compare sales lift. True incrementality measurement without cookies.
2. **Holdout Testing**: Withhold 10% of audience from a campaign. Compare conversion rates. Simple but powerful.
3. **Pre/Post Analysis**: Measure baseline metric, run campaign, measure post. Control for seasonality. Rough but better than nothing.

**The question these answer**: "Did my marketing actually cause sales, or would they have happened anyway?"

---

## North Star Metric + Activation

Every brand needs ONE metric that captures value creation. For product brands:

| Business Type | North Star Metric | Why |
|---------------|-------------------|-----|
| Consumable DTC (skincare, food, supplements) | Monthly repeat purchase rate | Repeat = product-market fit confirmation |
| Durable DTC (furniture, electronics, fashion) | Referral rate | High-ticket items rely on WOM |
| Marketplace seller (Shopee, Amazon) | Organic search rank for primary keyword | Platform organic = free traffic = sustainable |
| Local retail (restaurant, salon, gym) | Weekly active customers | Frequency = neighborhood habit |

### Activation Metric (The "Aha Moment")

Activation = the moment a new customer experiences enough value to come back. Famous benchmarks:

| Company | Activation Metric | Threshold |
|---------|-------------------|----------|
| Slack | Messages sent by team | 2,000 messages |
| Facebook | Friends added | 7 friends in 10 days |
| Dropbox | Files in folder | 1 file in 1 folder on 1 device |

**Physical product activation examples**:
- Skincare: Customer uses product for 7 consecutive days (sample/travel size drives this)
- Food: Customer orders 2nd time within 30 days
- Fashion: Customer posts product on social media (organic UGC = activation signal)
- Subscription box: Customer opens box within 48 hours of delivery

Identify the user's activation metric and design the first 7 days of customer experience around hitting it.

---

## Growth Motion: PLG vs Sales-Led vs Community-Led

### The PLG Myth (Busted)

Pure Product-Led Growth (PLG) -- where the product sells itself without human sales -- is a myth even for software. Notion, Figma, and Slack all needed sales teams to convert enterprise customers. For physical products, PLG is even less viable: customers need to see, touch, taste, or trust the product.

### Growth Motion Selection for Physical Products

| Motion | When It Works | Example | Cost |
|--------|--------------|---------|------|
| **Product-Led** | Product is visually stunning + shareable | Unboxing-worthy packaging, photogenic food | Low marginal cost, high product cost |
| **Content-Led** | Product needs education | Supplements, technical gear, specialized food | Medium (content creation time) |
| **Community-Led** | Product has identity/lifestyle component | Fitness, outdoor, artisan craft | Low cost, high time investment |
| **Sales-Led** | High-ticket or B2B | Custom furniture, catering, wholesale | High (per-customer cost) |
| **Founder-Led** | Founder has personal brand/charisma | Beauty founders, chef-entrepreneurs | Low cost if founder is willing |

Most successful product brands combine 2-3 motions. Start with one, add others as the team grows.

---

## Blitzscaling Post-Mortem: Lessons for Product Brands

The post-zero-interest-rate era (2022+) killed blitzscaling for most categories. Cautionary examples:

| Company | Peak Valuation | Outcome | Lesson |
|---------|---------------|---------|--------|
| WeWork | $47B | Bankruptcy | Growth without unit economics = expensive death |
| Bird Scooters | $2.5B | Bankruptcy | Hardware + logistics + no margin = impossible |
| Klarna | $46B -> $6.7B (-85%) | Survived, painfully | Buy-now-pay-later subsidizing growth = unsustainable |
| FTX | $32B | Fraud/collapse | Growth metrics can mask fundamental problems |

**Lesson for product sellers**: Profitable growth > fast growth. The "grow at all costs" era is over. Investors, platforms, and customers all reward sustainability now.

---

## Efficient Growth Metrics

### Rule of 40
Originally SaaS: Growth Rate % + Free Cash Flow Margin % >= 40%. Adapted for product brands:

**Product Brand Rule of 40**: Revenue Growth Rate % + Gross Margin % >= 40%
- Growing 20% with 25% gross margin = 45% (healthy)
- Growing 50% with -15% net margin = 35% (dangerous -- growing into losses)
- Growing 5% with 60% gross margin = 65% (very healthy, can invest in growth)

### Magic Number (for paid acquisition)
Net New Revenue in Quarter / Sales & Marketing Spend in Previous Quarter

- Magic Number > 0.75: Invest more in acquisition
- Magic Number 0.5-0.75: Optimize before scaling
- Magic Number < 0.5: Fix product or targeting before spending more

---

## GEO Execution Layer

Cross-reference with `seo-geo-aeo` and `media-algorithms` skills. Growth strategy must include AI discoverability.

### GEO as Growth Channel

Traditional funnel: Awareness (ads) -> Consideration (content) -> Conversion (LP/store)
GEO funnel: AI query -> AI cites brand -> Direct consideration -> Conversion

GEO is a **zero-CAC channel** once established. The investment is content creation and authority building, not per-click spend.

Implementation priority for the user's product type:
1. FAQ-heavy products (health, beauty, tech): Implement FAQ schema immediately
2. Comparison products (similar alternatives exist): Publish structured comparison tables
3. Unique/innovative products: Focus on entity establishment (Wikidata, authoritative mentions)

---

## Handoff

After establishing growth framework:
- Feed into `plan-cgo-review` -- apply unit economics to product prioritization
- Feed into `plan-funnel-review` -- design funnel with proper measurement
- Feed into `growth-retro` -- use these benchmarks to evaluate campaign results
- Feed into `media-algorithms` -- choose platforms based on growth stage and motion

### Transition Prompts

```
Growth framework established. Based on your unit economics:

1. /plan-cgo-review -> Prioritize products using growth metrics
2. /plan-funnel-review -> Design measurable funnel
3. /growth-retro -> Evaluate past campaigns against benchmarks
4. /salecraft-strategy -> Full strategic plan with budget allocation

Your most critical metric to fix right now is [X] because [reason].
```

---

## SaleCraft Scope & Pricing

### This skill is FREE
No credits required. Growth strategy is part of SaleCraft's free strategic consultation.
