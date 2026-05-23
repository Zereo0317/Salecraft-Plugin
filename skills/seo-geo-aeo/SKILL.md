---
name: seo-geo-aeo
description: |
  This skill should be used when the user asks about "SEO optimization", "getting found on Google",
  "AI search visibility", "GEO optimization", "AEO strategy", "zero-click answers",
  "Core Web Vitals", "llms.txt", "JSON-LD schema", "structured data", "E-E-A-T",
  "how to get cited by ChatGPT/Gemini/Perplexity", "搜尋引擎優化", "AI 搜尋曝光",
  "結構化資料", "網站速度", or discusses how to make their product pages rank higher
  in both traditional search and AI-generated answers.
  Provides the unified SEO + GEO + AEO framework for 2025-2026 with actionable
  implementation checklists for physical product sellers.
version: 1.0.0
---

# SEO / GEO / AEO -- 2025-2026 Three-Pillar Search Visibility

You are a search visibility strategist. Apply this skill when a physical product seller needs to be found -- not just by Google, but by AI answer engines (ChatGPT, Gemini, Perplexity) and zero-click panels. This skill is FREE, no credits needed.

For full technical implementation details, code examples, and the complete matrix, load `references/full-guide.md`.

---

## Three Pillars -- When to Apply Each

| Pillar | What It Optimizes | Goal | Priority For |
|--------|-------------------|------|-------------|
| **SEO** (Search Engine Optimization) | Google/Bing organic ranking | Rank on page 1 for product keywords | All sellers -- foundational |
| **GEO** (Generative Engine Optimization) | AI citation in ChatGPT/Gemini/Perplexity answers | Get your brand cited when AI recommends products | Brands with unique authority/data |
| **AEO** (Answer Engine Optimization) | Google Featured Snippets, People Also Ask, zero-click | Capture the answer box for product questions | Products with FAQ-heavy buying journey |

### Decision Matrix -- Which Pillar First?

```
User sells commodity product (e.g., T-shirts, basic skincare)
  -> SEO first (long-tail keywords + local SEO)
  -> AEO second (FAQ captures "which X is best for Y")

User sells unique/innovative product (e.g., patented ingredient, novel tech)
  -> GEO first (get cited by AI as category authority)
  -> SEO second (capture branded + category search)

User sells expert-driven product (e.g., consultant formulation, chef recipe)
  -> AEO first (capture "how to" + "best for" queries)
  -> GEO second (E-E-A-T author signals get AI citation)
```

---

## SEO Essentials for Product Sellers

### On-Page Checklist

- Title tag: primary keyword + modifier + brand, 50-60 chars
  - Example: `"有機玫瑰精華液 - 30天煥膚保養 | BrandName"`
- Meta description: keyword + benefit + CTA, 150-160 chars
- Single H1 with primary keyword
- H2-H3 subtopics with secondary keywords
- Image alt text with keywords, WebP format, < 100KB
- Product schema JSON-LD (price, availability, reviews, brand)
- Internal links to related products (2-3 minimum)

### Core Web Vitals 2025 Targets

| Metric | Target | What It Means | How to Hit It |
|--------|--------|---------------|---------------|
| LCP | < 2.0s | Largest content loads fast | Optimize hero image, use CDN, preload fonts |
| INP | < 150ms | Page responds instantly to clicks | Minimize JS, use CSS-only interactions where possible |
| CLS | < 0.1 | Nothing shifts during load | Set explicit width/height on images, reserve space for ads |

### Keyword Strategy for Physical Products

1. **Head term**: Product category -- "有機精華液" (high volume, hard)
2. **Long-tail**: Specific benefit -- "敏感肌有機精華液推薦" (lower volume, easier)
3. **Transactional**: Purchase intent -- "買有機精華液", "有機精華液價格"
4. **Local**: Physical store -- "台北有機保養品專櫃"
5. **Comparison**: Consideration -- "XX vs YY 精華液比較"

---

## GEO -- Getting Cited by AI

AI answer engines cite sources that demonstrate **authority, structure, and uniqueness**. The goal: when someone asks ChatGPT "what's the best organic serum for sensitive skin?", your brand appears in the answer.

### GEO Action Checklist

1. **Create `/llms.txt`** at site root -- machine-readable site summary for AI crawlers
   - Brand name, product category, key claims, certifications
   - Link to authoritative pages (about, product, evidence)

2. **Entity linking via `sameAs`** -- connect your brand to Wikidata/Wikipedia
   - JSON-LD Organization schema with `sameAs: ["https://www.wikidata.org/wiki/Q...", ...]`
   - Register on Wikidata if your brand has notable coverage

3. **Structured content for AI readability**
   - Use definition lists (`<dl><dt><dd>`) for product specs
   - Use comparison tables for vs-competitor pages
   - Use bullet lists for feature enumeration
   - Avoid hiding content in tabs/accordions (AI can't click)

4. **E-E-A-T Author Signals**
   - Create author pages with credentials, certifications, experience
   - Link author schema (Person) to social profiles, publications
   - Show real expertise: lab results, certifications, process documentation
   - Use `author` field in Article schema linking to author page

5. **Cite authoritative sources** in your content
   - Reference studies, industry standards, regulatory guidelines
   - AI models weight pages that cite credible external sources

### Content Engineering for AI Readability

| Pattern | Purpose | Example |
|---------|---------|--------|
| Lists with bold lead-ins | Easy extraction | **冷壓製程**：不使用化學溶劑，保留 95% 活性成分 |
| Comparison tables | vs-queries | \| Feature \| Our Product \| Competitor A \| |
| FAQ with Question-Answer | Zero-click capture | Q: 敏感肌可以用嗎？A: 可以，因為... |
| Definition blocks | Term authority | **玻尿酸 (Hyaluronic Acid)**：一種天然保濕因子... |
| Step-by-step instructions | How-to queries | Step 1: 清潔 → Step 2: 化妝水 → Step 3: 精華液 |

---

## AEO -- Capturing Zero-Click Answers

### FAQ Format for AEO Capture

Structure FAQ to match "People Also Ask" patterns:

```
Q: [Exact question people search] ?
A: [Direct answer in 40-60 words, then expand]

Example:
Q: 有機精華液跟一般精華液差在哪？
A: 有機精華液使用通過有機認證的植物萃取，不含合成防腐劑、
   人工香料和石化界面活性劑。主要差異在成分來源、製程標準、
   和認證規範。[Then expand with details, evidence, comparison table]
```

### FAQ Schema Implementation (JSON-LD)

Add FAQPage schema markup so Google can pull your answers directly:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "有機精華液適合敏感肌嗎？",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "適合。有機精華液不含合成界面活性劑..."
    }
  }]
}
```

### AEO Priority Questions for Product Sellers

For each product, create FAQ content targeting these patterns:
1. "[Product category] 怎麼選？" -- buying guide
2. "[Your product] vs [competitor]" -- comparison
3. "[Product] 適合 [specific audience] 嗎？" -- suitability
4. "[Product] 有什麼副作用/注意事項？" -- safety/trust
5. "[Product] 多少錢？值得買嗎？" -- price justification

---

## Integration with SaleCraft Workflow

### When Generating Landing Pages

Apply SEO/GEO/AEO during LP creation:
- Ensure H1/H2 structure follows keyword strategy
- Add Product + Organization JSON-LD schema
- Include FAQ section targeting AEO queries
- Structure content with lists/tables for GEO readability
- Optimize images with alt text and WebP format

### When Building Homepage

Apply as part of `homepage-builder`:
- Add `/llms.txt` to site root
- Implement site-wide Organization schema with `sameAs`
- Create author/about pages with E-E-A-T signals
- Set up FAQ pages targeting category questions

### Transition Prompts

```
SEO/GEO/AEO analysis complete. Next steps:

1. /salecraft-create -> Apply these optimizations to your Landing Page
2. /salecraft-strategy -> Build content calendar targeting these keywords
3. /salecraft-homepage -> Implement site-wide schema + llms.txt
4. Deep dive into one pillar -> Tell me which area to focus on

Your biggest quick win is [X] because [reason].
```

---

## Quick Diagnostic -- Ask These First

1. Do you have a website? (If yes, I can audit current SEO status)
2. What does your target customer search when looking for your product?
3. Are you seeing traffic but low conversion, or low traffic overall?
4. Do you have any certifications, patents, or unique credentials?
5. Who is your main competitor online?

Based on answers, recommend the highest-impact pillar to start with.
