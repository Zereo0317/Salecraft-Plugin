---
name: prism-influence
description: |
  This skill should be used when the user asks about "persuasion strategy", "influence tactics",
  "how to convince customers", "message design", "communication psychology", "copywriting persuasion",
  "how to handle objections psychologically", "customer personality", "brand positioning psychology",
  "warmth vs competence", "Cialdini principles", "說服策略", "影響力心理學", "訊息設計",
  "怎麼讓客人相信我", "品牌信任感", "溝通策略", "怎麼寫文案更有說服力",
  or discusses how to design marketing messages that resonate with specific personality types,
  build trust through psychological positioning, or overcome customer resistance.
  Provides the PRISM strategic communication framework for designing psychologically-optimized
  marketing messages for physical product sellers. FREE -- no credits needed.
version: 1.0.0
---

# PRISM Framework -- Strategic Communication & Influence for Product Marketing

Apply this skill when a physical product seller needs to design persuasive marketing messages, understand customer psychology, build trust positioning, or overcome objections at the psychological level. This skill is FREE, no credits needed.

For complete pillar details, decision trees, and the full impression engineering architecture, load `references/framework.md`.

---

## The PRISM 5-Phase Cycle

Every marketing message design follows this cycle. Do not skip phases.

```
P - Profile        Who is the target? (personality, values, fears)
R - Read Context    What situation are they in? (buying stage, mood, channel)
I - Identify Strategy   Which persuasion lever fits this profile + context?
S - Shape Message   Craft the message using the chosen strategy
M - Monitor Feedback   Measure response, adjust next cycle
```

### Phase 1: Profile -- Know Your Customer

Before writing a single word of copy, answer these about the target customer:

| Dimension | What to Assess | Product Marketing Application |
|---|---|---|
| **Big Five Personality** | Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism | Which tone and style resonates |
| **Core Values** | Security? Achievement? Belonging? | Which benefit angle to lead with |
| **Decision Style** | Analytical vs. intuitive vs. social proof-driven | How much evidence to provide |
| **Pain Sensitivity** | Loss-averse vs. gain-seeking | Frame as "avoid loss" or "achieve gain" |
| **Trust Baseline** | Skeptical vs. trusting | How many trust signals needed |

**Quick profiling for product sellers** -- ask the user:

1. Describe your typical customer in one sentence (age, situation, what they care about)
2. When they buy your product, what emotion drives the purchase? (fear of missing out? desire for status? need for safety? curiosity?)
3. What is their biggest hesitation before buying?

### Phase 2: Read Context

| Context Factor | Low-Involvement Purchase | High-Involvement Purchase |
|---|---|---|
| Price relative to income | < 1% monthly income | > 5% monthly income |
| Risk perception | Low (can return/replace) | High (health, appearance, commitment) |
| Decision time | Seconds to minutes | Days to weeks |
| Primary strategy | Peripheral cues (social proof, aesthetics) | Central route (evidence, logic, E-E-A-T) |

### Phase 3: Identify Strategy -- Persuasion Lever Selection

| Customer Profile | Best Persuasion Lever | Message Pattern |
|---|---|---|
| High Openness + Gain-seeking | **Novelty + Curiosity** | "全新概念..." / "你沒試過的..." |
| High Conscientiousness + Analytical | **Evidence + Authority** | "SGS 認證..." / "臨床實證..." |
| High Agreeableness + Belonging | **Social Proof + Community** | "10,000+ 媽媽的選擇" / "回購率 87%" |
| High Neuroticism + Loss-averse | **Scarcity + Safety** | "限量 200 組" / "不含 12 種有害成分" |
| High Extraversion + Status-seeking | **Exclusivity + Identity** | "行家才懂的..." / "KOL 愛用款" |

### Phase 4: Shape Message

#### Cialdini's 7 Principles Applied to Product Copy

| Principle | Trigger Phrase | Product Marketing Example |
|---|---|---|
| **Reciprocity** | "Free value first" | 免費試用包、免費保養諮詢 → 買正裝 |
| **Commitment/Consistency** | "Small yes first" | 先加 LINE → 領試用 → 回購 |
| **Social Proof** | "Others like you chose..." | "87% 回購率" / "2,000+ 五星評價" |
| **Authority** | "Expert endorses..." | "皮膚科醫師推薦" / "SGS 檢驗通過" |
| **Liking** | "We're like you" | 品牌故事共鳴、創辦人跟你一樣的痛 |
| **Scarcity** | "Limited / disappearing" | "限量 200 組" / "特價倒數 48 小時" |
| **Unity** | "We're in this together" | "台灣媽媽一起守護孩子的肌膚" |

#### Warmth-Competence Positioning (Fiske Model)

Every brand is perceived along two dimensions. Map the brand and adjust messaging:

```
                High Competence
                      |
        Envy          |       Admiration
    (luxury brands    |    (premium brands
     without story)   |     with heart)
                      |
 Low Warmth ----------+------------ High Warmth
                      |
        Contempt      |       Pity / Patronizing
    (cheap knockoffs) |    (charity brands
                      |     without quality)
                      |
                Low Competence
```

**Product seller positioning strategies:**

| Current Perception | Goal | Message Adjustment |
|---|---|---|
| High competence, low warmth | Move to Admiration quadrant | Add founder story, customer care, community |
| High warmth, low competence | Move to Admiration quadrant | Add certifications, test results, expert endorsements |
| Low both | Build competence first | Lead with quality proof, then add personality |
| High both (Admiration) | Maintain | Balance warmth and competence in all content |

### Phase 5: Monitor Feedback

After deploying the message, track these indicators:

| Indicator | Measures | Tool |
|---|---|---|
| Click-through rate | Message relevance | Ad manager / Analytics |
| Time on page | Content engagement | Google Analytics |
| Scroll depth | Content interest curve | SaleCraft scroll tracking |
| Add-to-cart rate | Purchase intent | E-commerce analytics |
| Comment sentiment | Emotional resonance | Social media monitoring |
| DM/inquiry rate | Trust level achieved | CRM / LINE OA |

Iterate: if CTR is high but conversion is low, the hook works but the trust-building (Phase 3 strategy) needs adjustment. Feed findings back to Phase 1 for the next cycle.

---

## Quick-Reference: Message Design Checklist

Before sending any marketing message to production, verify:

```
Target personality profiled (at least decision style + pain sensitivity)
Context assessed (high vs. low involvement purchase)
Primary persuasion lever selected (not "all of them")
Warmth-competence balance checked
Opening line matches customer's emotional state
Evidence calibrated to decision style (analytical = data; intuitive = story)
CTA matches the buying stage (awareness = learn more; consideration = try; decision = buy)
Scarcity/urgency is truthful (fake urgency destroys trust permanently)
Social proof is specific and verifiable (not "many customers love us")
Brand voice is consistent with positioning quadrant
```

---

## Integration with SaleCraft Workflow

### When to Apply PRISM

| SaleCraft Skill | PRISM Phase Focus | Application |
|---|---|---|
| `saleskit` consultation | Phase 1 (Profile) | Profile the user's target customer during discovery |
| `plan-cgo-review` | Phase 2 (Context) | Assess purchase involvement level for strategy |
| `plan-funnel-review` | Phase 3 (Strategy) | Select persuasion lever for each funnel stage |
| `engage-operator` | Phase 4 (Shape) | Design DM scripts with psychological triggers |
| `conversion-closer` | Phase 4 (Shape) | Craft objection handling with personality-matched responses |
| `generate-landing` | Phase 4 (Shape) | LP copy follows PRISM message architecture |
| `growth-retro` | Phase 5 (Monitor) | Analyze which PRISM strategies worked |

---

## Ethical Boundaries

Apply PRISM to help customers find products that genuinely serve them, not to manipulate:

- **Truthful scarcity only** -- never fake "last 3 items" if inventory is full
- **Genuine social proof** -- never fabricate reviews or testimonials
- **Real authority** -- never invent certifications or expert endorsements
- **Transparent framing** -- customers should feel informed, not tricked
- **Reciprocity with real value** -- free samples must be genuinely useful

Violation of these principles destroys long-term brand equity and may violate consumer protection laws.
