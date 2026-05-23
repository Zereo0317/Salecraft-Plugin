---
name: media-algorithms
description: |
  Platform algorithm optimization guide for physical product sellers. Covers recommendation
  system architecture (collaborative filtering, deep learning, Transformer-based), per-platform
  signal optimization (TikTok Monolith, YouTube Two-Tower, X/Twitter Heavy Ranker,
  Bluesky/Threads/Mastodon), attention economy principles, and Generative Engine
  Optimization (GEO) for LLM-era discovery.
  This skill should be used when the user asks about "which platform should I use",
  "how does the algorithm work", "why is my reach dropping", "TikTok algorithm",
  "Instagram algorithm changes", "YouTube recommendations", "how to go viral",
  "content strategy by platform", "attention economy", "platform selection",
  "algorithm hacking", "GEO optimization for AI search", "getting recommended by
  ChatGPT/Perplexity", discusses content distribution strategy, or needs help
  choosing between platforms for their product type. Provides architecture-informed
  tactics, not generic "post at 7pm" advice.
  FREE -- no credits required.
version: 1.0.0
---

# Media Systems & Platform Algorithm Optimization

Provide architecture-informed platform strategy for physical product sellers. Not "post at 7pm" advice -- deep understanding of how recommendation systems work and how to engineer content that the algorithm rewards.

**This skill is 100% FREE. No credits are deducted.**

## Core Principle

> Every platform is a recommendation engine with specific reward functions. Understand the reward function, and content strategy becomes engineering instead of guessing.

Load `references/platform-guide.md` for the complete per-platform technical breakdown, signal optimization matrices, and GEO implementation guide.

---

## When to Use

- User asks "which platform should I focus on?"
- User reports declining reach or engagement
- Before `plan-funnel-review` -- platform selection determines funnel architecture
- During `publish-social` -- optimize content for platform-specific signals
- When user asks about AI search visibility (ChatGPT, Perplexity, Gemini citing products)

---

## Recommendation System Architecture (Why It Matters)

Understanding the evolution explains why different platforms behave differently:

| Generation | Method | Platform Example | Implication for Sellers |
|------------|--------|-----------------|------------------------|
| Gen 1 | Collaborative Filtering | Early Amazon | "People who bought X also bought Y" -- bundle strategy |
| Gen 2 | Matrix Factorization | Netflix 2010s | Latent factors determine visibility -- niche = advantage |
| Gen 3 | Deep Learning (DLRM, Two-Tower) | YouTube, Meta | Hundreds of signals; content quality + engagement depth matter |
| Gen 4 | Transformer + Real-time | TikTok Monolith | Real-time behavior dominance; cold-start friendly; dwell-time is king |

**Key insight**: Gen 4 systems (TikTok) are the most meritocratic for new sellers. Gen 3 systems (YouTube, Meta) reward accumulated authority. Gen 1-2 systems (Amazon, Shopee) reward purchase history and reviews.

---

## Platform Selection Matrix

Ask these three questions to recommend platform priority:

1. **Product visual appeal**: High (fashion, food, beauty) vs Low (supplements, electronics components)
2. **Purchase consideration time**: Impulse (< $30, emotional) vs Considered (> $100, rational)
3. **Current assets**: Video capability? Photography? Writing? Community?

### Decision Tree

```
High visual + Impulse buy + Video capable
  -> TikTok (primary) + Instagram Reels (secondary)
  -> Content: Hook-in-1.5s + product demo + CTA

High visual + Considered buy + Photo capable
  -> Instagram Feed/Stories (primary) + Pinterest (secondary)
  -> Content: Lifestyle imagery + educational carousel + social proof

Low visual + Considered buy + Writing capable
  -> YouTube (primary) + Blog/SEO (secondary)
  -> Content: Deep-dive review + comparison + how-to

Any product + Existing community
  -> LINE/WhatsApp (primary) + existing platform (secondary)
  -> Content: Exclusive offers + behind-scenes + direct conversation

Any product + AI search visibility goal
  -> Website + GEO optimization (primary)
  -> Content: Structured data + llms.txt + FAQ schema
```

---

## The 1.5-Second Hook Rule

Attention economy research (Wu, Hari) shows: users decide to stay or scroll within 1.5 seconds. This applies to every platform.

### Hook Engineering for Product Sellers

| Hook Type | Template | Best For |
|-----------|----------|----------|
| **Curiosity Gap** | "Most people don't know this about [product category]..." | Educational/myth-busting |
| **Visual Disruption** | Unexpected visual in first frame (close-up texture, slow-mo pour, before/after) | Visually rich products |
| **Social Proof Shock** | "10,000 people bought this in 3 days. Here's why." | Trending/popular products |
| **Problem-Agitate** | "Your [routine/habit] is probably wrong. Let me show you." | Problem-solving products |
| **Result First** | Show the end result immediately, then explain how | Transformation products (beauty, fitness, cooking) |

**Rule**: The hook promises; the content delivers. Empty hooks (clickbait) trigger negative engagement signals that hurt algorithmic ranking.

---

## Per-Platform Signal Optimization (Summary)

Detailed breakdowns in `references/platform-guide.md`.

### TikTok (Monolith Architecture)
- **Dominant signal**: Dwell time (watch duration / video length ratio)
- **Cold-start advantage**: 80 items shown to cold-start users; new accounts get real testing
- **Key tactic**: Optimize for completion rate. 15-30s videos with high replay value outperform 60s+ with drop-off.
- **Product seller hack**: "Process reveal" content (showing how the product is made) consistently achieves high completion rates

### YouTube (Two-Tower + Wide & Deep)
- **Dominant signal**: Shifted from watch time to satisfaction signals (likes, shares, "not interested" absence)
- **Key tactic**: Click-through rate on thumbnail + title determines candidate recall. Invest heavily in thumbnails.
- **Product seller hack**: Comparison and "honest review" formats perform well in candidate recall because they match high-intent search queries

### Instagram (Meta DLRM-family)
- **Dominant signal**: Engagement velocity in first 30 minutes
- **Key tactic**: Notify your existing community (Stories, DMs, email) when posting to spike early engagement
- **Product seller hack**: Carousel posts (educational, step-by-step) have highest save rates, which Meta weights heavily

### X/Twitter (Heavy Ranker)
- **Partially open-sourced 2023**: Confirmed signals include recency, author reputation, and engagement ratio
- **Community detection**: Content distributed within detected interest communities first
- **Product seller hack**: Thread format for product storytelling; quote-tweet strategy for reaching adjacent communities

### Bluesky / Threads / Mastodon
- **Bluesky**: Open algorithm marketplace; users choose their feed algorithm. Currently chronological-dominant.
- **Threads**: Meta's DLRM backbone; behaves like early Instagram. Currently rewards frequent posting.
- **Mastodon**: Pure chronological. Federated. No algorithmic boost. Community-driven discovery only.

---

## Information Ecology Warning

Benkler (Network Propaganda) and Vosoughi research show: false/sensational content spreads 6x faster than accurate content. This creates a dilemma for product sellers.

**Rules for product sellers**:
- Never use false claims for algorithmic advantage -- short-term reach, long-term brand destruction
- Use "surprising but true" angles instead of fabrication
- Cite sources for health/efficacy claims -- platforms increasingly penalize unsubstantiated claims
- Build credibility through consistency, not virality

---

## GEO: LLM as New Gatekeepers

Claude, ChatGPT, Gemini, Perplexity are the new search intermediaries. When someone asks "what's the best organic face cream?", the AI's answer determines discovery.

### Three GEO Dimensions

1. **Training Data Content Density**: How much quality content about the brand exists in AI training data? More indexed pages with the brand name + category = higher recall probability.
2. **Real-time Domain Authority**: For AI systems with web access (Perplexity, Gemini), domain authority and freshness matter. Publish regularly on the brand's owned domain.
3. **LLM-Parseable Content Structure**: AI extracts from structured content (lists, tables, FAQ, definition blocks) far better than from flowing prose or images.

### GEO Action Items for Product Sellers

Detailed implementation in `references/platform-guide.md` and cross-reference with `seo-geo-aeo` skill.

1. Create `/llms.txt` at website root
2. Implement FAQ schema (JSON-LD) for product questions
3. Publish structured comparison content (tables, lists)
4. Build citation network (link to authoritative sources; get linked by authoritative sources)
5. Maintain consistent brand entity across all indexed platforms

---

## Platform Governance Context

Klonick's "New Governors" framework: platforms are private governments making public speech decisions. Gillespie's content moderation research: platforms shape markets through moderation policies, not just algorithms.

**Practical impact**: Platform policy changes (e.g., Instagram reducing product link reach, TikTok Shop integration, Meta ad policy shifts) are governance decisions that reshape seller economics. Monitor platform policy announcements as regulatory intelligence.

---

## Handoff

After platform strategy is established:
- Feed into `plan-funnel-review` -- design funnel architecture around chosen platforms
- Feed into `publish-social` -- apply signal optimization to actual content creation
- Feed into `seo-geo-aeo` -- deep-dive GEO implementation
- Feed into `engage-operator` -- design platform-specific interaction flows

### Transition Prompts

```
Platform strategy mapped. Based on your product and resources:

1. /plan-funnel-review -> Design your customer journey across these platforms
2. /salecraft-create -> Generate optimized content for your primary platform
3. /salecraft-engage -> Build interaction scripts for platform-specific conversations
4. /seo-geo-aeo -> Deep-dive into AI search visibility (GEO)

Your highest-ROI platform move right now is [X] because [reason].
```

---

## SaleCraft Scope & Pricing

### This skill is FREE
No credits required. Platform strategy is part of SaleCraft's free strategic consultation.
