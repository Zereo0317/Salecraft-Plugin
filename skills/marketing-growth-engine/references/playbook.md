# Marketing & Growth Engine -- Complete Playbook Reference

This reference contains the full frameworks, benchmark tables, diagnostic checklists, and implementation guides for the `marketing-growth-engine` skill.

---

## Part 1: Unit Economics Deep Dive

### COGS Breakdown for Physical Products

Before calculating margins, ensure COGS includes ALL variable costs:

| Cost Component | Includes | Common Blind Spots |
|----------------|----------|-------------------|
| Raw materials | Ingredients, fabrics, components | Minimum order quantities inflating per-unit cost |
| Manufacturing | Labor, machine time, QC | Defect rate (typically 2-5% waste) |
| Packaging | Box, label, insert, tissue, tape | Custom packaging vs generic (3-10x cost difference) |
| Shipping (inbound) | Factory to warehouse | Customs, duties, insurance for imported goods |
| Shipping (outbound) | Warehouse to customer | Free shipping threshold absorbs margin |
| Payment processing | Credit card fees, platform fees | 2.5-3.5% typically forgotten in margin calc |
| Returns | Reverse logistics + restocking | Return rate: 5-10% fashion, 2-3% consumables |
| Platform fees | Amazon 15%, Shopee 5-10%, Shopify 0-2% | Variable vs fixed fee structures |

### True Contribution Margin Calculator

```
Revenue per unit:                    $___
- COGS (all-in):                     $___
= Gross profit per unit:             $___
- Variable marketing per unit:        $___  (ad spend / units sold)
- Variable ops per unit:              $___  (pick/pack, CS per order)
= Contribution margin per unit:       $___
= Contribution margin %:              ___%

Target: > 40% for DTC, > 25% for marketplace
```

### LTV Calculation Methods

**Simple LTV** (for brands with < 12 months data):
```
LTV = AOV x Purchase Frequency (annual) x Average Lifespan (years)

Example: $45 AOV x 4 purchases/year x 2.5 years = $450 LTV
```

**Cohort LTV** (for brands with > 12 months data):
```
Track each monthly cohort's cumulative revenue over time.
Month 0 cohort: M0=$45, M3=$65, M6=$95, M12=$140
This gives the actual revenue curve, not an estimate.
```

**Predictive LTV** (for brands with > 24 months data):
```
Use BG/NBD model (Buy 'til You Die):
- Estimates probability that a customer is still "alive"
- Predicts future purchase frequency
- Libraries: lifetimes (Python), BTYD (R)
```

### CAC by Channel Benchmarks (Physical Products, 2025)

| Channel | Typical CAC Range | Best For |
|---------|-------------------|----------|
| Meta Ads (FB/IG) | $15-60 | Visual products, impulse purchases |
| Google Search | $20-80 | High-intent, specific product searches |
| TikTok Ads | $8-35 | Trendy products, younger demographics |
| Influencer/KOL | $10-50 (varies wildly) | Trust-dependent categories (beauty, health) |
| SEO/Content | $5-20 (amortized) | Long-term, compounds over time |
| Referral | $5-15 | High-satisfaction products |
| Offline events | $30-100 | High-ticket, relationship products |

**CAC trend**: Rising 15-25% annually across paid channels due to competition. Brands that don't invest in owned channels (SEO, email, community) face unsustainable CAC inflation.

---

## Part 2: Sharp's Laws of Brand Growth (How Brands Grow)

Byron Sharp's empirical research at the Ehrenberg-Bass Institute challenged conventional marketing wisdom. Key findings:

### Law 1: Penetration > Loyalty
Growth comes from acquiring new buyers, not from increasing purchase frequency of existing buyers. Even the most "loyal" brands grow primarily through penetration.

**Implication for product sellers**:
- Stop over-investing in loyalty programs for a small base
- Invest in reach -- getting the brand in front of people who have never tried it
- "Heavy buyers" are statistically rare and unreliable; "light buyers" are the growth engine

### Law 2: Differentiation ≠ Growth
Consumers perceive far less differentiation between brands than marketers believe. In blind tests, even "loyalists" often can't distinguish their preferred brand.

**Implication**:
- Stop obsessing over "what makes us unique" if it doesn't drive purchase
- Focus on **mental availability** (being thought of) and **physical availability** (being easy to buy)
- "Distinctive" (recognizable brand assets: color, logo, shape, jingle) matters more than "differentiated" (functionally better)

### Law 3: Double Jeopardy
Small brands suffer twice: fewer buyers AND those buyers are slightly less loyal. This is statistical, not strategic -- it happens because small brands have fewer mental and physical availability points.

**Implication**:
- Don't compare loyalty metrics against market leaders -- the comparison is structurally unfair
- Focus all energy on increasing penetration; loyalty will follow naturally
- Market share is the best predictor of both penetration and loyalty

### Mental Availability Building

| Tactic | What It Does | Example |
|--------|-------------|--------|
| Category Entry Points (CEPs) | Associate brand with buying situations | "When you want a natural face cream..." |
| Distinctive Brand Assets | Visual/sonic cues that trigger brand recall | Tiffany blue, Coca-Cola's contour bottle, Netflix "tudum" |
| Consistent Reach | Regular presence across touchpoints | Weekly content + monthly ads + quarterly events |
| Emotional Priming | Associate brand with feelings, not just features | "The feeling of putting on a clean, perfectly fitting shirt" |

### Physical Availability Checklist

- [ ] Product available on the #1 platform where target customers shop
- [ ] Listed in top 3 search results for primary category keyword
- [ ] Purchase process < 3 clicks from discovery
- [ ] Multiple payment options (credit card, mobile pay, BNPL)
- [ ] Shipping speed competitive with category norm
- [ ] Reorder friction minimized (subscription, one-click reorder)

---

## Part 3: Marketing Mix Modeling (MMM) In Detail

### What MMM Measures

MMM decomposes total sales into:
1. **Base sales**: Sales that would happen without marketing (brand equity, distribution, seasonality)
2. **Incremental sales**: Sales attributable to each marketing channel
3. **Adstock effect**: How marketing impact decays over time (TV ad seen Monday still drives sales Thursday)
4. **Diminishing returns**: Each additional dollar in a channel has slightly less impact

### Google Meridian (Open Source)

**Architecture**: Bayesian hierarchical model with geo-level data
**Requirements**: 2+ years of weekly data, 3+ marketing channels, geo-level granularity preferred
**Output**: Per-channel ROI, optimal budget allocation, response curves

**For small brands**: Meridian is powerful but data-hungry. Brands spending < $5K/month on marketing rarely have enough data for reliable MMM.

### Meta Robyn (Open Source)

**Architecture**: Ridge regression + evolutionary optimization (Nevergrad)
**Advantage**: Faster to set up than Meridian; handles fewer data points slightly better
**Output**: Similar to Meridian -- per-channel decomposition, budget optimizer

### Simplified MMM for Small Brands

For brands that can't run full MMM, apply the principle:

**Monthly Channel Scorecard**:
```
Channel: ___________
Spend this month: $___
New customers attributed: ___
Revenue from new customers: $___
Simple ROI: (Revenue - Spend) / Spend = ___x

Trend (3 months):
  Month 1: ___x ROI, $___ spend
  Month 2: ___x ROI, $___ spend
  Month 3: ___x ROI, $___ spend

Verdict: [ ] Scale  [ ] Maintain  [ ] Optimize  [ ] Cut
```

---

## Part 4: Geo-Lift / Causal Inference

### Why Geo-Lift Matters

The fundamental marketing measurement problem: "Would this customer have bought anyway?" Correlation (ad seen -> purchase) ≠ causation (ad caused purchase). Geo-lift testing solves this.

### How to Run a Geo-Lift Test

1. **Select test and control regions**: Similar demographics, similar baseline sales
   - Example: Test in Taipei, control in Kaohsiung (similar size, different media market)
2. **Run campaign in test region only**: 4-8 weeks minimum
3. **Measure sales lift**: Test region sales vs control region sales, normalized for baseline differences
4. **Calculate incrementality**: Lift / Total test region sales = % of sales truly incremental

### Simplified A/B for Smaller Brands

No geographic segmentation capability? Try:
- **Time-based**: 2 weeks on, 2 weeks off, 2 weeks on. Measure sales pattern.
- **Holdout**: Show ads to 90% of audience, withhold from 10%. Compare conversion.
- **Platform-provided**: Meta's Conversion Lift, Google's Brand Lift studies (requires minimum spend)

---

## Part 5: Growth Stage Playbooks

### Stage 1: Pre-Product-Market-Fit (0-100 customers)

**Objective**: Validate that people will pay for the product
**Metrics that matter**: Conversion rate from first touchpoint, repeat purchase rate, qualitative feedback
**Budget allocation**: 90% product/experience, 10% marketing (just enough to get test customers)

**Checklist**:
- [ ] 10 customers acquired through personal network (proof of demand)
- [ ] 5+ unsolicited positive feedback messages
- [ ] Repeat purchase rate > 20% within 60 days
- [ ] Unit economics positive at current scale (even if barely)
- [ ] Clear articulation of ONE value proposition in ONE sentence

### Stage 2: Traction (100-1,000 customers)

**Objective**: Find one scalable acquisition channel
**Metrics**: CAC by channel, activation rate, 30-day retention
**Budget allocation**: 60% one primary channel testing, 20% product, 20% retention

**Checklist**:
- [ ] Tested 3+ acquisition channels, identified 1 winner
- [ ] CAC of winning channel < 1/3 of LTV
- [ ] Activation metric defined and > 40%
- [ ] Basic email/LINE welcome sequence live
- [ ] Customer referral mechanism exists (even manual)

### Stage 3: Growth (1,000-10,000 customers)

**Objective**: Scale winning channel + add second channel
**Metrics**: LTV/CAC, CAC payback, Magic Number, retention curves
**Budget allocation**: 50% primary channel, 20% secondary channel testing, 15% brand, 15% retention

**Checklist**:
- [ ] Primary channel CAC stable at scale (not degrading > 10%/month)
- [ ] Secondary channel identified and showing positive early signals
- [ ] LTV/CAC > 3 on primary channel
- [ ] CAC payback < 12 months
- [ ] Brand building investment started (content, PR, community)
- [ ] Email/LINE generating > 20% of revenue

### Stage 4: Scale (10,000+ customers)

**Objective**: Build brand moat + optimize efficiency
**Metrics**: Rule of 40, NRR (if applicable), market share, brand awareness
**Budget allocation**: 60% brand building, 40% performance (IPA optimal)

**Checklist**:
- [ ] 3+ acquisition channels performing
- [ ] Organic/brand search growing faster than paid
- [ ] Customer referral contributing > 15% of new customers
- [ ] Brand recognized in category without prompting
- [ ] Operating leverage: revenue growing faster than costs

---

## Part 6: Diagnostic Checklists

### "Growth Is Stalling" Diagnostic

```
1. Is CAC rising?
   -> Yes: Ad fatigue, audience saturation, or competition. Refresh creative, expand targeting, add new channel.
   -> No: Continue.

2. Is conversion rate dropping?
   -> Yes: Product-market fit erosion, competitive pressure, or LP quality. Survey recent non-converters.
   -> No: Continue.

3. Is retention dropping?
   -> Yes: Product quality issue, onboarding failure, or competitor poaching. Interview churned customers.
   -> No: Continue.

4. Is market saturated?
   -> Yes: Expand to adjacent market, launch new product, or increase share of wallet.
   -> No: Continue.

5. Is the brand being outspent?
   -> Yes: Shift to defensible channels (community, content, referral) that big spenders can't easily replicate.
```

### "Should I Increase Ad Spend?" Diagnostic

```
Magic Number Check:
Net new revenue this quarter: $___
Marketing spend last quarter: $___
Magic Number = $___ / $___ = ___

> 0.75: YES, increase spend. Unit economics support it.
0.5-0.75: MAYBE. Optimize targeting and creative first. Test 20% increase.
< 0.5: NO. Fix product, targeting, or funnel before spending more.

CAC Trend Check:
CAC this month: $___
CAC 3 months ago: $___
Change: ___%

Rising > 10%: CAUTION. Ad fatigue or competition. Don't scale into deteriorating economics.
Stable: PROCEED with increase.
Declining: ACCELERATE. Capture the efficiency window.
```

### "Brand Building vs Performance" Budget Diagnostic

```
Brand awareness (unaided, in target market):
> 50%: Increase brand spend to defend (60-70%)
20-50%: Balance 50/50
< 20%: Performance-heavy (70/30) to build initial customer base

Organic search brand mentions (monthly):
Growing: Brand building is working. Maintain or increase.
Flat: Brand building underinvesting. Increase brand %.
Declining: Urgent. Brand is losing relevance. Major brand investment needed.

CAC trend across channels:
Declining: Performance is efficient. Can shift more to brand.
Rising: Over-reliance on performance. Need brand to lower long-term CAC.
```

---

## Part 7: NRR and Repeat Economics for Physical Products

### Net Revenue Retention (NRR) Adapted for Products

SaaS NRR measures expansion revenue from existing customers. For product brands:

**Product NRR** = (Revenue from customers who bought in prior period, in current period) / (Revenue from those same customers in prior period)

- NRR > 110%: Customers are buying more over time (upsell/cross-sell working)
- NRR 90-110%: Healthy retention, stable base
- NRR < 90%: Customers are leaving or buying less. Retention problem.

### Repeat Purchase Engineering

| Tactic | Mechanism | Best For |
|--------|-----------|----------|
| **Subscription/Auto-replenish** | Reduce friction to zero | Consumables (skincare, supplements, coffee) |
| **Bundle/Cross-sell at checkout** | Increase AOV | Complementary product lines |
| **Post-purchase education** | Increase product usage | Complex products (skincare routines, cooking) |
| **Loyalty program** | Reward frequency | High-frequency categories (food, beauty) |
| **Referral incentive** | Existing customers as acquisition channel | High-satisfaction products |
| **Replenishment reminder** | Time-based trigger | Products with predictable usage cycle |
| **Limited edition/seasonal** | Create urgency for repeat | Fashion, food, collectible |

---

## Part 8: The Blitzscaling Autopsy

### Why "Grow at All Costs" Died

The zero-interest-rate era (2009-2021) subsidized growth:
- Cheap capital = investors funded unprofitable growth
- Platform organic reach was abundant = free distribution
- Competition was lower = CAC was affordable
- Consumer attention was cheaper = ad costs were manageable

Post-2022 reality:
- Capital is expensive = investors demand profitability
- Platform organic reach is scarce = pay-to-play
- Competition is extreme = CAC is inflated
- Consumer attention is fragmented = ad effectiveness declining

### Efficient Growth Principles

1. **Profitable unit economics BEFORE scaling**: Every new customer should be profitable at the individual level
2. **Owned channels as insurance**: Email list, LINE, community -- assets that don't depreciate when platform algorithms change
3. **Brand as CAC reducer**: Organic brand search traffic has $0 marginal CAC. Brand building is a long-term CAC investment.
4. **Compound growth > linear growth**: Content, SEO, community, referral -- channels that compound over time
5. **Cash flow awareness**: Even profitable growth can kill a business if it grows faster than cash flow supports (inventory, manufacturing lead times, payment terms)

### Physical Product Cash Flow Trap

```
WARNING: Physical products have a cash flow trap that digital products don't.

Timeline:
Month 0: Place manufacturing order. Pay 30% deposit = -$30K
Month 2: Goods arrive. Pay remaining 70% = -$70K
Month 2-3: Start selling. Revenue trickles in = +$20K
Month 4-6: Revenue ramps. Break even on this batch.
Month 3: Need to place NEXT order to avoid stockout = -$30K again

Total cash tied up: $80-110K continuously.
"Growing" means this number grows FASTER than revenue.

Solution: Negotiate payment terms, use inventory financing,
          or grow at a pace cash flow supports.
```

---

## Part 9: GEO as Growth Channel (Execution Detail)

### Integration with Growth Strategy

GEO (Generative Engine Optimization) represents a new growth channel with unique economics:
- **CAC**: Near-zero marginal cost once content infrastructure exists
- **Compounding**: Content indexed in AI training data creates durable discovery
- **Defensibility**: Authority built through GEO is harder to replicate than ad spend
- **Limitation**: Slow to build (months to years), hard to measure directly

### GEO Growth Metrics

| Metric | How to Measure | Target |
|--------|---------------|--------|
| AI citation frequency | Monthly searches of brand name in ChatGPT/Gemini/Perplexity | Increasing month-over-month |
| Structured content coverage | % of product pages with JSON-LD schema | 100% |
| llms.txt deployed | Exists at site root | Yes |
| FAQ coverage | # of "People Also Ask" questions with published answers | Top 20 questions in category |
| Authority backlinks | # of authoritative sites linking to brand content | Growing, 10+ for established brands |

### Priority Matrix

| Product Type | GEO Priority | Why |
|-------------|-------------|-----|
| Health/wellness | HIGH | Consumers increasingly ask AI for health product recommendations |
| Beauty/skincare | HIGH | "Best X for Y skin type" is a primary AI query pattern |
| Food/beverage | MEDIUM | AI recommendations for specialty/artisan food growing |
| Fashion/apparel | MEDIUM | More visual; AI less dominant in discovery |
| Electronics/accessories | HIGH | Comparison queries heavily moved to AI |
| Home/furniture | MEDIUM | Mixed visual + spec-driven; AI for spec comparison |
