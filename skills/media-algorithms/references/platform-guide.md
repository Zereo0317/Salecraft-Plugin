# Media Systems & Platform Engineering -- Complete Reference

This reference contains the full technical breakdown of recommendation system architectures, per-platform signal optimization, attention economy principles, and GEO implementation for the `media-algorithms` skill.

---

## Part 1: Recommendation System Architecture Deep Dive

### Evolution Timeline

**Gen 1 -- Collaborative Filtering (1990s-2000s)**
- Method: "Users who liked A also liked B" (user-user or item-item similarity)
- Limitation: Cold-start problem (new items/users get no signal), sparsity
- Where it survives: Amazon "frequently bought together," basic e-commerce recommendations
- Seller implication: Reviews and purchase volume directly drive visibility. Getting the first 50 reviews is critical.

**Gen 2 -- Matrix Factorization (2006-2015)**
- Breakthrough: Netflix Prize (2006). Decompose user-item matrix into latent factors.
- Method: SVD, ALS, NMF -- discover hidden dimensions (e.g., "action-comedy-90s" as a latent factor)
- Seller implication: The algorithm discovers niches automatically. Products that clearly belong to a specific niche get better recommendations than generic products.

**Gen 3 -- Deep Learning (2016-2021)**
- **DLRM (Deep Learning Recommendation Model)**: Meta's architecture. Dense features (user age, time) + sparse features (user ID, item ID) through embedding tables + MLP.
- **Two-Tower Model**: Separate user tower and item tower, compute similarity in embedding space. Used by YouTube for candidate retrieval. Enables fast retrieval from millions of items.
- **Wide & Deep (Google, 2016)**: Wide component memorizes specific feature interactions; Deep component generalizes. YouTube uses this for final ranking after Two-Tower retrieval.
- Seller implication: Content metadata (title, description, tags) feeds the dense features. Engagement signals (likes, shares, comments, saves) feed the interaction features. Both matter; neither alone is sufficient.

**Gen 4 -- Transformer + Real-time Learning (2021-present)**
- **TikTok Monolith**: Collisionless embedding tables + real-time parameter update (no batch delay). Multi-task learning head predicts like, share, comment, and completion simultaneously.
- **Real-time update advantage**: Traditional systems update models hourly/daily. Monolith updates embedding tables with each interaction. A video that gets 10 completions in 5 minutes immediately gets boosted -- no waiting for batch update.
- Seller implication: First-hour performance matters more than ever. Content is tested in real-time and promoted or suppressed within minutes, not days.

---

## Part 2: Per-Platform Deep Dive

### TikTok -- Monolith Architecture

**Architecture**:
- Collisionless embedding: Unlike traditional hash-based embedding (where different items can share slots = collision), Monolith assigns unique embedding to each item. Every video gets its own learned representation.
- Real-time training: Model parameters update with streaming user interactions. No batch gap.
- Multi-task learning: Single model predicts multiple objectives simultaneously (like probability, share probability, completion probability, follow probability). Final ranking is weighted combination.

**Signal hierarchy** (from most to least influential):
1. **Completion rate / Dwell time**: THE dominant signal. A 15s video watched to the end = stronger signal than a 60s video watched 40%. Replays are even stronger.
2. **Share**: Strongest explicit engagement signal. Shares indicate content worth spreading beyond personal feed.
3. **Comment**: High-intent engagement. Comments that generate replies = conversation = even stronger.
4. **Like**: Weakest explicit signal. Easy to give; doesn't indicate deep engagement.
5. **Follow (from video)**: Strong long-term signal for creator authority.

**Cold-start mechanism**:
- New videos shown to ~80 cold-start users (interest-matched via hashtags, sounds, and creator's existing audience overlap)
- If completion rate and engagement exceed threshold in first 80-200 views, video enters broader distribution
- This means: genuinely good content from zero-follower accounts can reach millions. TikTok is the most meritocratic Gen 4 platform for new sellers.

**Content optimization for product sellers**:
- **Ideal length**: 15-30 seconds for cold-start testing. The algorithm can test more 15s videos in the same time budget.
- **Process reveals**: "How it's made" content consistently achieves >80% completion. Showing raw ingredients becoming finished product is hypnotic.
- **Before/after**: Transformation content (skincare results, cooking process, cleaning) drives high completion and saves.
- **Sound strategy**: Trending sounds get a distribution boost (sound is a clustering feature in Monolith). But avoid sounds that don't match brand tone -- forced trend-following reads as inauthentic.
- **Posting frequency**: 1-3/day during growth phase. Algorithm tests each video independently; more videos = more lottery tickets.
- **TikTok Shop integration**: Product links in video increase commercial intent signal. The algorithm now has a commerce-weighted ranking head.

---

### YouTube -- Two-Tower Candidate Recall + Wide & Deep Ranking

**Architecture (two-stage)**:

**Stage 1: Candidate Generation (Two-Tower)**
- User tower: Watch history, search history, demographics, device, time
- Video tower: Title, description, tags, thumbnail features, channel authority, video features
- Computes similarity between user embedding and video embedding
- Retrieves ~hundreds of candidates from millions of videos
- **Seller implication**: Title + description + tags determine whether the video even enters the candidate pool. SEO-style keyword optimization matters here.

**Stage 2: Ranking (Wide & Deep)**
- Wide component: Memorizes specific user-video interactions (e.g., "users who watched video A for >70% also watched video B")
- Deep component: Neural network generalizing from features
- Originally optimized for **watch time**. Since 2022, shifted toward **satisfaction signals**: likes, shares, "not interested" absence, return visits.

**Signal hierarchy**:
1. **Click-through rate (thumbnail + title)**: Determines candidate selection. Without clicks, the ranking model never evaluates the video.
2. **Watch duration / satisfaction**: Determines ranking position. Watch >50% + like + subscribe = strongest signal.
3. **Session contribution**: Does the video lead to more YouTube watching? Videos that start long sessions get boosted (YouTube optimizes for platform session time).
4. **Freshness**: New videos get temporary boost, but evergreen content accumulates authority over time.

**Content optimization for product sellers**:
- **Thumbnail investment**: Thumbnail is ~60% of click decision. Use high contrast, readable text (3-4 words max), expressive face or dramatic product shot. A/B test thumbnails.
- **Title formula**: "[Curiosity element] + [Keyword] + [Qualifier]" -- e.g., "I Tested 10 Organic Serums for 30 Days (Surprising Results)"
- **First 30 seconds**: Must deliver on title promise or tease clear value. YouTube measures early drop-off heavily.
- **Chapters/timestamps**: Help YouTube understand content structure; enables deep-link recommendations to specific segments.
- **Ideal length**: 8-15 minutes for monetization + depth; 60-90 seconds for Shorts (separate algorithm, similar to TikTok).
- **Series format**: Multi-video series on a topic builds session contribution signals. "Complete Guide to [Product Category]" as a playlist.

---

### Instagram -- Meta DLRM Family

**Architecture**: Meta's internal recommendation system uses DLRM variants. Feed, Reels, Explore, and Stories each have separate ranking models but share infrastructure.

**Feed ranking signals**:
1. **Relationship signals**: How often the user interacts with the creator. DMs, story replies, comment threads, saves.
2. **Interest signals**: Content category match based on user's historical engagement.
3. **Timeliness**: Recency matters; chronological component in ranking.
4. **Engagement velocity**: Engagement rate in first 30 minutes post-publication strongly predicts broader distribution.

**Reels ranking** (distinct from Feed):
- More similar to TikTok: content-based discovery, not relationship-based
- Completion rate is primary signal
- Audio/music trends get distribution boost
- Text overlay and hook quality affect early retention

**Content optimization for product sellers**:
- **Carousel posts**: Highest save rate among formats. Educational carousels ("5 Things to Look for in Organic Skincare") get saved as reference material. Saves are heavily weighted by Meta's ranking.
- **Stories for engagement velocity**: Post story announcing new post; existing audience swipes to post; early engagement spikes; algorithm distributes wider.
- **DM strategy**: Instagram increasingly weights DM activity. Direct conversation with customers signals strong relationship.
- **Reels frequency**: 3-5/week for growth. Instagram currently prioritizes Reels in Explore and Feed.
- **Hashtag strategy (current)**: 5-10 relevant hashtags; avoid banned/overused tags. Hashtags function as clustering features for content-based recommendation.
- **Shopping integration**: Product tags in posts/stories signal commercial intent; enables shopping-tab discovery.

---

### X/Twitter -- Heavy Ranker

**Architecture** (partially open-sourced March 2023):
- **Heavy Ranker**: Neural network scoring each tweet for each user
- **Community detection (SimClusters)**: Users clustered into interest communities; content distributed within communities first, then cross-community based on engagement

**Confirmed signals** (from open-source code):
1. **Author reputation within community**: High-reputation authors in a specific community get preferential distribution
2. **Recency**: Strong chronological component
3. **Engagement ratio**: Likes/impressions, replies/impressions, retweets/impressions
4. **Content type**: Images and videos get multiplier; links get penalty (X wants users to stay on platform)
5. **Thread engagement**: Multi-tweet threads that maintain engagement across tweets get boosted

**Content optimization for product sellers**:
- **Thread format**: Product storytelling as threads. First tweet = hook; subsequent tweets = story/evidence; last tweet = CTA. Threads maintain engagement across multiple impressions.
- **Quote-tweet strategy**: Quote-tweeting relevant conversations in adjacent communities bridges the user into new SimClusters.
- **Image-first**: Always include image/video. Link-only tweets get suppressed.
- **Engagement bait vs genuine conversation**: X's community detection rewards genuine conversation within interest groups. Forced engagement bait ("like if you agree") is less effective than genuine question-asking.

---

### Bluesky / Threads / Mastodon

**Bluesky -- Open Algorithm Marketplace**:
- Users can choose different feed algorithms (custom feeds)
- Default: reverse-chronological with light algorithmic suggestions
- Custom feeds can be built by anyone; creates niche discovery opportunities
- **Seller strategy**: Currently small but engaged audience. Early mover advantage in custom feed presence. Content about craft/process performs well with early adopter demographic.

**Threads -- Meta Infrastructure, Early Stage**:
- Uses Meta's DLRM backbone; behaves like early-era Instagram
- Currently rewards: frequent posting (2-4/day), text-first content, conversation threads
- Chronological + light recommendation hybrid
- **Seller strategy**: Low-effort cross-posting from Instagram. Text-based product insights and conversations. Community building through reply engagement.

**Mastodon -- Federated, No Algorithm**:
- Pure chronological timeline. No algorithmic recommendation at all.
- Discovery: hashtags, boosts (retweets), instance-local timelines
- **Seller strategy**: Only worthwhile if target audience is tech-savvy/privacy-conscious. Focus on hashtag strategy and instance community engagement.

---

## Part 3: Attention Economy Principles

### Wu -- Attention Merchants
Tim Wu's framework: Attention is harvested from audiences and resold to advertisers. The entire content ecosystem exists to extract and monetize attention.

**Seller implication**:
- Sellers are both attention merchants (capturing customer attention) and attention commodities (paying platforms for access to attention)
- The cost of attention is rising yearly. Organic reach declines as platforms monetize more aggressively.
- **Response**: Build owned attention assets (email list, LINE, membership community) that don't depreciate as platform organic reach declines.

### Hari -- Stolen Focus
Johann Hari's thesis: Modern technology fragments attention. The average attention span on mobile content is 1.5 seconds before scroll/skip decision.

**Seller implication -- The 1.5-Second Rule**:
- Every piece of content must pass the 1.5-second test: "Is this worth my time?"
- Hook types for product sellers:
  - **Visual arrest**: Unexpected color, texture, motion in first frame
  - **Statement disruption**: "Everything you know about [X] is wrong"
  - **Result reveal**: Show the outcome before the process
  - **Social proof anchor**: "200,000 people can't be wrong"
  - **Personal vulnerability**: "I almost gave up on this product"
- After the hook: deliver substance within 15 seconds or lose the viewer permanently

---

## Part 4: Information Ecology

### Benkler -- Network Propaganda
Yochai Benkler's research: The information ecosystem is shaped by propaganda networks, not individual bad actors. Disinformation spreads through legitimate-looking networks of websites, social accounts, and influencers.

**Seller implication**:
- Build content that is clearly authentic and verifiable
- Cite real sources (studies, certifications, customer testimonials with permission)
- Platforms increasingly use provenance signals to rank content; authentic content gets structural advantage

### Vosoughi -- Fake News Spreads 6x Faster
MIT study: False news stories spread 6 times faster than true stories on social media. Novelty and emotional arousal drive sharing; truth does not.

**Seller implication**:
- **Temptation**: Exaggerated claims spread faster. "This cream removes wrinkles in 24 hours" gets more shares than "This cream improves hydration over 4 weeks."
- **Reality**: Exaggerated claims trigger platform moderation, customer complaints, and brand distrust. The 6x speed advantage is a trap.
- **Alternative**: Use "surprising but true" framing. "Clinical study: 89% of participants saw improvement in 28 days" is both shareable and defensible.

---

## Part 5: GEO Implementation Guide

### LLM Gatekeepers: The New Search Intermediaries

Claude, ChatGPT, Gemini, and Perplexity are increasingly where consumers start product research. "Best organic serum for sensitive skin" asked to ChatGPT replaces the same Google search.

**How LLMs select sources to cite**:
1. **Training data presence**: Was the brand mentioned in high-quality training data (authoritative websites, reviews, articles)?
2. **Web search results** (for real-time systems like Perplexity): Domain authority, content relevance, freshness
3. **Content structure**: LLMs extract from structured content (lists, tables, headers, FAQ) far better than from unstructured prose
4. **Citation network**: Pages that cite and are cited by authoritative sources get higher trust weighting

### GEO Three-Dimension Implementation

**Dimension 1: Training Data Content Density**
- Publish frequently on owned domain with brand + category keywords
- Get mentioned on authoritative third-party sites (review sites, industry publications, comparison articles)
- Maintain Wikipedia/Wikidata presence if brand is notable enough
- Every quality page indexed = one more chance of training data inclusion

**Dimension 2: Real-time Domain Authority**
- For systems with web access: domain authority (backlinks, domain age, traffic) matters
- Publish fresh content regularly (weekly blog minimum)
- Build backlinks from authoritative domains in the product category
- Technical SEO: fast load, mobile-optimized, clean crawlability

**Dimension 3: LLM-Parseable Content Structure**
- Use definition lists (`<dl><dt><dd>`) for product specifications
- Use comparison tables for vs-competitor content
- Use bullet lists for feature enumeration
- Use FAQ format with clear Q&A structure
- Avoid hiding content in JavaScript tabs/accordions (LLMs can't click)
- Implement `llms.txt` at site root with machine-readable brand summary
- Add JSON-LD schema: Product, Organization, FAQ, BreadcrumbList

### `/llms.txt` Template for Product Sellers

```
# [Brand Name]
## Overview
[Brand Name] is a [product category] brand specializing in [key differentiator].
Founded in [year], based in [location].

## Products
- [Product 1]: [One-line description with key feature]
- [Product 2]: [One-line description with key feature]

## Key Claims & Evidence
- [Claim 1]: [Evidence/certification]
- [Claim 2]: [Evidence/certification]

## Certifications
- [Certification 1] (issued by [authority], [year])
- [Certification 2]

## Contact
- Website: [URL]
- Customer service: [email/phone]

## Authoritative References
- [Link to press coverage]
- [Link to third-party review]
- [Link to clinical study]
```

### GEO Monitoring
- Search the brand name on ChatGPT, Gemini, Perplexity monthly
- Track: Does the AI mention the brand? In what context? Accurately?
- If misrepresented: publish correction content on high-authority pages; submit feedback to AI providers
- If absent: increase content density using Dimension 1-3 strategies

---

## Part 6: Platform Governance Intelligence

### Klonick -- "The New Governors"
Platforms are private entities making public governance decisions. Content moderation policies, algorithm changes, and feature launches are legislative acts that reshape seller economics.

### Gillespie -- Content Moderation as Market Architecture
Content moderation decisions determine what products can be advertised, what claims can be made, and what content formats are promoted. A moderation policy change can eliminate an entire marketing channel overnight.

**Monitoring checklist for product sellers**:
- Follow platform policy blogs (Meta Newsroom, TikTok Newsroom, YouTube Creator Blog)
- Track category-specific policy changes (health claims, financial claims, beauty claims)
- Maintain content within policy boundaries; avoid "edge case" tactics that risk moderation
- Diversify across platforms to hedge against policy risk

---

## Quick Reference: Platform Selection Cheat Sheet

| Factor | TikTok | YouTube | Instagram | X/Twitter | Website/GEO |
|--------|--------|---------|-----------|-----------|-------------|
| Best for | Impulse visual | Considered purchase | Lifestyle brand | Thought leadership | Long-term authority |
| Key signal | Dwell time | CTR + satisfaction | Engagement velocity | Community reputation | Domain authority |
| Content length | 15-30s | 8-15min (long) / 60-90s (Shorts) | Carousel / 15-30s Reels | Thread / image tweet | 1500+ words |
| Posting frequency | 1-3/day | 1-2/week | 3-5/week | 3-5/day | 1-2/week |
| Cold-start friendly | Very (80-item test) | Moderate | Low (relationship-dependent) | Low | N/A (SEO timeline) |
| Commerce integration | TikTok Shop | Shopping shelf | IG Shopping | None | Direct |
| Best product type | Visual, emotional, demo-able | Complex, educational | Aesthetic, lifestyle | Niche, opinion-driven | All |
