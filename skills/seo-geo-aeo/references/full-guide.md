# SEO / GEO / AEO -- Complete Technical Implementation Guide (2025-2026)

> This reference supplements `SKILL.md`. Load it when the user needs code examples, detailed schema markup, Next.js architecture specifics, or the full implementation matrix.

---

## 1. Three-Pillar Architecture Overview

### 1.1 Pillar Relationship Map

```
                   ┌──────────────────┐
                   │   User Query     │
                   └────────┬─────────┘
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
     ┌──────────┐    ┌──────────┐    ┌──────────┐
     │   SEO    │    │   GEO    │    │   AEO    │
     │ Google   │    │ ChatGPT  │    │ Featured │
     │ Bing     │    │ Gemini   │    │ Snippets │
     │ Organic  │    │ Perplexity│   │ PAA Box  │
     └──────────┘    └──────────┘    └──────────┘
     Page 1 rank     AI citation     Zero-click
                                      answer
```

### 1.2 Implementation Priority by Product Type

| Product Type | SEO Priority | GEO Priority | AEO Priority | Rationale |
|---|---|---|---|---|
| Commodity (T-shirts, basic skincare) | ★★★ | ★ | ★★ | High competition -- win on long-tail SEO + FAQ AEO |
| Innovative/patented product | ★★ | ★★★ | ★★ | Unique data = AI citation magnet |
| Expert-driven (formulations, recipes) | ★★ | ★★ | ★★★ | E-E-A-T signals + FAQ capture |
| Local retail (bakery, cafe) | ★★★ | ★ | ★★ | Local SEO + Google Business Profile |
| Premium/luxury | ★★ | ★★★ | ★ | Brand authority + AI recommendation |
| Health supplements | ★★★ | ★★ | ★★★ | Regulatory trust + FAQ heavy buying journey |

---

## 2. Next.js 15 Technical Architecture

### 2.1 React Server Components (RSC) for SEO

RSC renders HTML on the server. Search engines and AI crawlers see complete content without JavaScript execution.

```tsx
// app/products/[slug]/page.tsx -- Server Component (default)
import { getProduct } from '@/lib/api';
import { ProductSchema } from '@/components/structured-data';

export async function generateMetadata({ params }) {
  const product = await getProduct(params.slug);
  return {
    title: `${product.name} - ${product.benefit} | ${product.brand}`,
    description: product.metaDescription,
    openGraph: {
      title: product.name,
      description: product.shortDescription,
      images: [{ url: product.heroImage, width: 1200, height: 630 }],
    },
  };
}

export default async function ProductPage({ params }) {
  const product = await getProduct(params.slug);
  return (
    <>
      <ProductSchema product={product} />
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      {/* All content server-rendered -- fully crawlable */}
    </>
  );
}
```

### 2.2 Partial Pre-Rendering (PPR)

PPR combines static shell + streaming dynamic content. The static shell is instantly crawlable; dynamic parts stream in.

```tsx
// next.config.js
module.exports = {
  experimental: {
    ppr: true,
  },
};

// app/products/[slug]/page.tsx
import { Suspense } from 'react';

export default async function ProductPage({ params }) {
  const product = await getProduct(params.slug);
  return (
    <>
      {/* Static shell -- instantly crawlable */}
      <h1>{product.name}</h1>
      <ProductSchema product={product} />
      <ProductDetails product={product} />

      {/* Dynamic part -- streams in */}
      <Suspense fallback={<ReviewsSkeleton />}>
        <ProductReviews slug={params.slug} />
      </Suspense>
    </>
  );
}
```

### 2.3 llms.txt Implementation

Place at site root `/llms.txt`. This file helps AI crawlers understand your site structure.

```
# [Brand Name]
> [One-sentence brand description with category and key differentiator]

## Products
- [Product A]: [key claim, certification, price range]
- [Product B]: [key claim, certification, price range]

## Evidence & Certifications
- SGS certified: [report number]
- [Certification body]: [certificate number]
- Published in: [journal/publication name]

## Key Pages
- About: https://example.com/about
- Products: https://example.com/products
- Evidence: https://example.com/evidence
- FAQ: https://example.com/faq

## Contact
- Email: hello@example.com
- LINE: @brandname
```

**Physical product example (Chinese)**:

```
# 月光有機保養
> 台灣製造有機保養品牌，專注冷壓萃取天然植物精華，通過 SGS 及 ECOCERT 雙認證。

## 產品
- 玫瑰精華液 30ml：冷壓玫瑰萃取，5% 玻尿酸，SGS 檢驗通過，NT$1,280
- 茶樹淨膚水 150ml：澳洲茶樹精油，無酒精配方，ECOCERT 認證，NT$680

## 認證與實證
- SGS 檢驗報告：FA/2024/12345
- ECOCERT 有機認證：EC-2024-TW-001
- 成分透明度：全產品 INCI 成分表公開

## 重要頁面
- 品牌故事：https://moonlight.com.tw/about
- 全產品：https://moonlight.com.tw/products
- 認證文件：https://moonlight.com.tw/certifications
- 常見問題：https://moonlight.com.tw/faq

## 聯繫
- LINE 官方帳號：@moonlight-organic
- Email：hello@moonlight.com.tw
```

---

## 3. JSON-LD Schema.org Deep Implementation

### 3.1 Product Schema (with Offer, Review, Brand)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "有機玫瑰精華液 30ml",
  "description": "冷壓萃取大馬士革玫瑰，含 5% 高分子玻尿酸，無添加合成防腐劑。",
  "image": [
    "https://example.com/images/rose-serum-hero.webp",
    "https://example.com/images/rose-serum-texture.webp",
    "https://example.com/images/rose-serum-ingredients.webp"
  ],
  "brand": {
    "@type": "Brand",
    "name": "月光有機保養"
  },
  "sku": "ML-RS-30",
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/products/rose-serum",
    "priceCurrency": "TWD",
    "price": "1280",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "月光有機保養"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "126"
  },
  "review": [
    {
      "@type": "Review",
      "author": { "@type": "Person", "name": "小美" },
      "datePublished": "2025-03-15",
      "reviewBody": "用了兩週，膚質明顯改善，保濕效果很好。",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5"
      }
    }
  ]
}
```

### 3.2 Organization Schema with sameAs (Entity Linking)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "月光有機保養",
  "url": "https://moonlight.com.tw",
  "logo": "https://moonlight.com.tw/logo.svg",
  "description": "台灣有機保養品牌，專注冷壓萃取天然植物精華",
  "foundingDate": "2020",
  "founder": {
    "@type": "Person",
    "name": "陳小明",
    "sameAs": [
      "https://www.linkedin.com/in/xiaoming-chen",
      "https://www.wikidata.org/wiki/Q123456789"
    ]
  },
  "sameAs": [
    "https://www.facebook.com/moonlightorganic",
    "https://www.instagram.com/moonlight_organic",
    "https://www.wikidata.org/wiki/Q987654321"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "availableLanguage": ["zh-TW", "en"]
  }
}
```

### 3.3 Article Schema with Person (E-E-A-T Author Authority)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "敏感肌保養完整指南：皮膚科醫師推薦的 5 個關鍵步驟",
  "author": {
    "@type": "Person",
    "name": "Dr. 林雅文",
    "url": "https://moonlight.com.tw/authors/dr-lin",
    "jobTitle": "皮膚科專科醫師",
    "sameAs": [
      "https://www.linkedin.com/in/dr-lin-dermatology",
      "https://scholar.google.com/citations?user=XXXXX"
    ],
    "alumniOf": {
      "@type": "CollegeOrUniversity",
      "name": "台大醫學院"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "月光有機保養",
    "logo": { "@type": "ImageObject", "url": "https://moonlight.com.tw/logo.svg" }
  },
  "datePublished": "2025-05-01",
  "dateModified": "2025-05-15"
}
```

### 3.4 FAQPage Schema

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "有機精華液跟一般精華液差在哪？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "有機精華液使用通過有機認證的植物萃取，不含合成防腐劑、人工香料和石化界面活性劑。主要差異在成分來源（認證有機農場）、製程標準（冷壓 vs 化學萃取）、和第三方認證規範（如 ECOCERT、USDA Organic）。"
      }
    },
    {
      "@type": "Question",
      "name": "敏感肌可以用有機精華液嗎？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "大多數有機精華液適合敏感肌，因為不含常見刺激成分（SLS、Paraben、人工香料）。建議選擇通過皮膚刺激性測試的產品，使用前在手腕內側做 24 小時貼膚測試。"
      }
    }
  ]
}
```

### 3.5 LocalBusiness Schema (for physical stores)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "月光有機保養 信義旗艦店",
  "image": "https://moonlight.com.tw/stores/xinyi-store.webp",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "信義路五段 7 號 2F",
    "addressLocality": "台北市",
    "addressRegion": "信義區",
    "postalCode": "110",
    "addressCountry": "TW"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 25.0330,
    "longitude": 121.5654
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "10:00",
      "closes": "21:00"
    }
  ],
  "telephone": "+886-2-1234-5678",
  "priceRange": "$$"
}
```

---

## 4. Entity Linking via Wikidata

### 4.1 When to Create a Wikidata Entry

| Criteria | Wikidata Eligible | Alternative |
|---|---|---|
| Brand has Wikipedia article | Yes -- link directly | N/A |
| Brand has press coverage in 3+ reliable sources | Yes -- create entry with sources | N/A |
| Brand has official government registration | Possibly -- with registration as source | Link to government registry via sameAs |
| Brand is new, no coverage | Not yet | Build coverage first, revisit later |

### 4.2 Wikidata Property Mapping for Product Brands

| Wikidata Property | Label | Use |
|---|---|---|
| P31 | instance of | Q4830453 (business) |
| P17 | country | Q865 (Taiwan) |
| P571 | inception | founding year |
| P856 | official website | URL |
| P452 | industry | Q3044454 (cosmetics industry) |
| P159 | headquarters location | city |

### 4.3 sameAs Best Practice

Order of priority for `sameAs` links:

1. **Wikidata** -- strongest entity signal for AI
2. **Wikipedia** -- if article exists
3. **LinkedIn company page** -- professional authority
4. **Facebook page** -- verified business identity
5. **Instagram** -- brand presence
6. **Government registry** -- legal entity verification
7. **Industry certification databases** -- trust signal

---

## 5. Core Web Vitals 2025 Standards

### 5.1 Updated Targets

| Metric | 2024 Target | 2025 Target | Change | Measurement Tool |
|---|---|---|---|---|
| LCP (Largest Contentful Paint) | < 2.5s | **< 2.0s** | Tightened | Lighthouse / CrUX |
| INP (Interaction to Next Paint) | < 200ms | **< 150ms** | Tightened | Lighthouse / CrUX |
| CLS (Cumulative Layout Shift) | < 0.1 | < 0.1 | Unchanged | Lighthouse / CrUX |

### 5.2 LCP Optimization Playbook

```
LCP Budget Breakdown (target: < 2.0s)
├── DNS + TLS + TTFB:     < 800ms
├── Resource load (hero):  < 700ms
├── Render delay:          < 500ms
└── Total:                 < 2,000ms
```

**Action items for product pages:**

1. **Hero image**: WebP/AVIF, responsive `srcset`, `fetchpriority="high"`, preload
   ```html
   <link rel="preload" as="image" href="/hero.webp"
         imagesrcset="/hero-400.webp 400w, /hero-800.webp 800w, /hero-1200.webp 1200w"
         imagesizes="100vw" fetchpriority="high">
   ```

2. **Font loading**: `font-display: swap`, preload critical font
   ```html
   <link rel="preload" as="font" href="/fonts/brand.woff2"
         type="font/woff2" crossorigin>
   ```

3. **CDN**: Serve static assets from edge. Use `next/image` with `priority` prop for hero.

4. **Server response**: Edge-rendered or cached. PPR delivers static shell under 200ms.

### 5.3 INP Optimization with Tailwind CSS v4 Zero-Runtime

Tailwind CSS v4 compiles to pure CSS at build time -- zero runtime JavaScript for styling. This directly reduces INP because no JS executes on user interactions for style changes.

**Before (runtime CSS-in-JS, bad for INP):**
```jsx
// styled-components -- runs JS on every render
const Button = styled.button`
  background: ${props => props.primary ? '#2fa067' : '#ccc'};
`;
```

**After (Tailwind v4, zero runtime):**
```jsx
// Pure CSS class -- no JS at interaction time
<button className="bg-green-600 hover:bg-green-700 active:scale-95
                   transition-all duration-150">
  立即購買
</button>
```

**INP budget for product pages:**

| Interaction | Target | How |
|---|---|---|
| Add to cart click | < 50ms visual | CSS-only button state + async cart update |
| Image gallery swipe | < 80ms | CSS scroll-snap, no JS carousel |
| FAQ accordion toggle | < 50ms | `<details>/<summary>` native HTML, no JS |
| Color/size selector | < 50ms | CSS-only radio input styling |
| Navigation menu | < 50ms | CSS-only `:hover` / `:focus-within` |

### 5.4 CLS Prevention Checklist

```
□ All images have explicit width + height attributes
□ Embeds (video, maps) have reserved space via aspect-ratio CSS
□ Web fonts use font-display: swap with fallback metrics
□ No content injected above the fold after load (ads, banners)
□ Dynamic content (reviews, recommendations) has skeleton placeholder
□ No lazy-loaded images above the fold
```

---

## 6. Content Engineering for AI Readability

### 6.1 Structural Patterns That AI Extractors Prefer

| Pattern | HTML | Why AI Likes It | Product Use Case |
|---|---|---|---|
| Definition list | `<dl><dt><dd>` | Clear term-definition pairs | Product specs, ingredient glossary |
| Comparison table | `<table>` with `<thead>` | Structured data grid | vs-competitor, feature comparison |
| Ordered list with bold lead | `<ol><li><strong>` | Scannable, extractable steps | Usage instructions, buying guide |
| FAQ with QA structure | `<details><summary>` or schema | Direct Q&A mapping | Product FAQ, buying decision FAQ |
| Stat callout | Heading + number + unit + source | Citable claim | "95% 活性成分保留率（SGS 報告）" |

### 6.2 Content Template: Product Authority Page

```markdown
# [Product Name] -- [Primary Benefit Phrase]

> [40-word summary answering "what is this and why should I care"]

## What Is [Product]?

[Definition paragraph -- 60-80 words, direct, factual]

**Key specifications:**

| Spec | Value |
|------|-------|
| Volume | 30ml |
| Key ingredient | 5% 大馬士革玫瑰萃取 |
| Certification | ECOCERT, SGS |
| Skin type | All skin types, including sensitive |

## How It Works

1. **[Step 1 bold lead]**: [explanation, 20-30 words]
2. **[Step 2 bold lead]**: [explanation]
3. **[Step 3 bold lead]**: [explanation]

## [Product] vs [Competitor Category]

| Feature | [Your Product] | [Generic Alternative] |
|---------|---------------|----------------------|
| Extraction method | Cold-press (冷壓) | Chemical solvent |
| Active retention | 95% | ~60% |
| Certification | ECOCERT + SGS | None |
| Price per ml | $42.7 | $25-35 |

## Frequently Asked Questions

**Q: [Exact search query]?**
A: [40-60 word direct answer]. [Then expand with evidence].

**Q: [Second search query]?**
A: [Direct answer]. [Expand].

## Evidence & Certifications

- **SGS Report FA/2024/12345**: [what it tested, result]
- **ECOCERT Certificate**: [scope, validity]
- **[Published study]**: [finding, journal name, year]

## About the Author

[Author name], [credentials]. [2-sentence bio with verifiable expertise].
[Link to author page with full credentials].
```

### 6.3 Anti-Patterns (Content Structures AI Cannot Parse)

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Content in JavaScript tabs/accordions | AI crawlers cannot click | Use `<details>` or render all content server-side |
| Key info only in images | AI cannot read image text | Duplicate as HTML text + alt text |
| Infinite scroll product listings | AI stops crawling | Paginated URLs with `<link rel="next">` |
| Product specs in PDF only | AI cannot index | Extract to HTML, link PDF as supplement |
| Pricing hidden behind "Request Quote" | AI skips unpriced products | Show starting price or range |

---

## 7. E-E-A-T Author Authority Signals

### 7.1 Author Page Checklist

```
□ Full name (real name, not pen name)
□ Professional photo
□ Credentials / certifications relevant to product domain
□ Professional affiliations
□ Published works / media appearances
□ Social profile links (LinkedIn, Google Scholar)
□ Years of experience in the domain
□ Specific expertise areas listed
□ Link to Organization schema with sameAs
```

### 7.2 Author Authority Building Plan for Product Sellers

| Timeline | Action | SEO/GEO Impact |
|---|---|---|
| Week 1-2 | Create author page with credentials | Person schema indexed |
| Week 3-4 | Publish 3 expert articles with author byline | E-E-A-T signals established |
| Month 2 | Get 1 guest post on industry publication | External authority backlink |
| Month 3 | Create or update Wikidata entry for brand | Entity linking active |
| Month 4+ | Regular content with author byline + citations | Cumulative authority growth |

---

## 8. AEO Capture Strategy

### 8.1 Question Research for Physical Products

| Question Type | Pattern | Example | Priority |
|---|---|---|---|
| Selection guide | "[Category] 怎麼選？" | "有機精華液怎麼選？" | ★★★ |
| Comparison | "[A] vs [B]" | "冷壓精華 vs 一般精華" | ★★★ |
| Suitability | "[Product] 適合 [audience] 嗎？" | "有機精華液適合敏感肌嗎？" | ★★★ |
| Safety | "[Product] 有副作用嗎？" | "玻尿酸精華液有副作用嗎？" | ★★ |
| Price justification | "[Product] 多少錢？值得嗎？" | "有機精華液值得買嗎？" | ★★ |
| How-to | "[Product] 怎麼用？" | "精華液正確使用方法" | ★★ |
| Difference | "[A] 跟 [B] 差在哪？" | "精華液跟精華露差在哪？" | ★★ |

### 8.2 Answer Engineering Formula

```
Direct Answer Layer (40-60 words)
  ├── State the answer immediately (no preamble)
  ├── Include 1-2 key facts/numbers
  └── End with a transition to expanded content

Expansion Layer (200-400 words)
  ├── Evidence (certification, study, data)
  ├── Comparison table (if applicable)
  ├── Step-by-step (if how-to)
  └── Related FAQ links (internal linking)

Trust Layer
  ├── Author byline with credentials
  ├── Last updated date
  ├── Source citations
  └── Schema markup (FAQPage + Article)
```

---

## 9. Integration Checklist for SaleCraft LP Generation

When generating a Landing Page through SaleCraft, verify these SEO/GEO/AEO elements:

### Pre-Generation (during consultation)

- [ ] Primary keyword identified from user's product description
- [ ] 3-5 long-tail keywords for FAQ section
- [ ] Competitor URLs collected for gap analysis
- [ ] Author/brand credentials documented for E-E-A-T

### Post-Generation (during review)

- [ ] H1 contains primary keyword
- [ ] H2-H3 hierarchy is logical and keyword-rich
- [ ] Product JSON-LD schema is present and valid
- [ ] FAQ section has 3-5 questions matching "People Also Ask" patterns
- [ ] All images have descriptive alt text
- [ ] Images are WebP format, < 100KB each
- [ ] Meta title is 50-60 characters with keyword + brand
- [ ] Meta description is 150-160 characters with CTA
- [ ] Content uses AI-readable structures (lists, tables, definitions)
- [ ] External authoritative sources are cited
- [ ] Author/brand credentials are visible

### Site-Wide (during homepage-builder)

- [ ] `/llms.txt` created at site root
- [ ] Organization schema with `sameAs` to Wikidata
- [ ] Author pages created with Person schema
- [ ] FAQ index page targeting category-level questions
- [ ] Sitemap.xml includes all product and content pages

---

## 10. Measurement & Iteration

### 10.1 KPI Matrix by Pillar

| Pillar | Metric | Tool | Target | Check Frequency |
|---|---|---|---|---|
| SEO | Organic click-through rate | Google Search Console | > 3% for top queries | Weekly |
| SEO | Core Web Vitals pass rate | PageSpeed Insights / CrUX | 100% good on all 3 | Monthly |
| SEO | Indexed pages | Google Search Console | All product pages indexed | Weekly |
| GEO | AI citation count | Manual checks on ChatGPT/Gemini/Perplexity | 1+ citation per product category | Monthly |
| GEO | llms.txt crawl logs | Server access logs | Regular crawl activity | Monthly |
| AEO | Featured snippet wins | Google Search Console (position 0) | 1+ per product category | Weekly |
| AEO | PAA (People Also Ask) appearances | Manual + Semrush | 3+ PAA appearances | Monthly |

### 10.2 Iteration Cycle

```
Month 1: Foundation
  → Implement Product + Organization schema
  → Create author pages
  → Add FAQ section to top 3 product pages
  → Create /llms.txt

Month 2: Content
  → Publish 4 expert articles with structured content
  → Build comparison pages for top 2 competitors
  → Submit Wikidata entry (if eligible)

Month 3: Optimization
  → Analyze GSC data for new FAQ opportunities
  → Check AI citation status (manual tests)
  → Optimize Core Web Vitals based on CrUX data
  → Expand FAQ coverage based on PAA trends

Month 4+: Scale
  → Monthly content with AI-readable formatting
  → Track competitor GEO/AEO moves
  → Update /llms.txt with new products/evidence
  → Build external authority through guest content
```
