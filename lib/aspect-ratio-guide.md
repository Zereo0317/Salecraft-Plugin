# Aspect Ratio Guide

## Supported Ratios

A session generates LPs at exactly **one** aspect ratio. The whole stripe set inherits that ratio. Allowed values:

| Ratio | Name (Chinese in chat) | Pixel example | Use Case |
|-------|------------------------|---------------|----------|
| **9:16** | 直版（手機直拿）| 1080 × 1920 | IG Story / TikTok / Reels / mobile-first DTC |
| **16:9** | 橫版（桌機寬）| 1920 × 1080 | Desktop hero / Google Ads / presentations / B2B |
| **1:1** | 方版 | 1080 × 1080 | IG / FB feed square posts |
| **4:5** | IG portrait feed | 1080 × 1350 | IG / FB tall feed posts (more screen real estate than 1:1) |
| **4:3** | 橫版偏方 | 1600 × 1200 | Slide-deck style, classic 4:3 monitors |
| **3:4** | 直版偏方 | 1200 × 1600 | Print portrait, magazine-style |
| **3:2** | 橫版偏寬 | 1500 × 1000 | DSLR landscape photo feel |
| **2:3** | 直版偏寬 | 1000 × 1500 | DSLR portrait photo feel |
| **21:9** | 超寬橫版 | 2520 × 1080 | Cinematic banners, ultra-wide hero |

`9:16` is the default when none is specified or an unknown value is sent.

## Setting It on a Session

Aspect ratio lives on `wizard_shared_data.aspect_ratio` (single string). It must be written **before** `generate_session` fires — set during Step 5 of the Wizard 6-step.

```
mcp_tool_call("landing_ai_mcp", "update_session", {
  "user_token": token,
  "session_id": session_id,
  "data_json": json_dumps({
    "wizard_shared_data": {"aspect_ratio": "16:9"}
  })
})
```

Then trigger generation:

```
mcp_tool_call("landing_ai_mcp", "generate_session", {
  "user_token": token,
  "session_id": session_id,
  "ta_group_ids_json": json_dumps([...]),
  "requested_stripe_count": 8
})
```

## Two Ratios for the Same Brand → Two Sessions

Backend generates **one ratio per session**. Sending a list (`["16:9","9:16"]`) or `"both"` is silently coerced back to `9:16`. To deliver two ratios:

1. Confirm with user: "兩個比例需要分兩次扣點生成、總費用會是 2× — 確定嗎？"
2. Run session #1 with `aspect_ratio="16:9"` (full Wizard 6-step)
3. `create_session` again, copy brand / TA / spec, only `aspect_ratio="9:16"` differs
4. Run session #2
5. Report both campaign URLs together when both finish

(Same pattern as different `requested_stripe_count` for different TAs — backend can't fan out.)

## Inferring From Conversation

| User signal | Infer |
|-------------|-------|
| "IG 限時 / TikTok / Reels / Shorts" | `9:16` |
| "桌機官網 / Google Ads / 簡報 / YouTube ad" | `16:9` |
| "IG 方版貼文 / FB 方版貼文 / Meta feed square" | `1:1` |
| "IG 動態消息直拿 / FB feed portrait / 4:5 廣告" | `4:5` |
| (none of the above) | `9:16` (broadest reach) |

When inferred, **announce** the choice and the reason on Step 5c so the user can override (per CLAUDE.md Rule 6.5 NO SILENT DEFAULTS).

## Speaking Ratios to the User

Per CLAUDE.md L307 (零術語 rule): never write the bare numeric ratio to the user. Always pair with a Chinese descriptor:

- ❌ "比例選 9:16 可以嗎？"
- ✅ "用直版（手機直拿、IG Story 那種尺寸）可以嗎？"

DB always stores the literal string (`"9:16"` etc.) — the rule is for chat output only.

## Image Export Sizes (post-gen)

Each per-stripe image inherits the session's aspect ratio. Approximate exported pixel sizes (Gemini Image API "2K" target):

| Ratio | Approximate per-stripe pixels |
|-------|-------------------------------|
| 9:16 | 1536 × 2752 |
| 16:9 | 2752 × 1536 |
| 1:1  | 2048 × 2048 |
| 4:5  | 1856 × 2320 |

Stripe images are downloaded via `download_stripe(campaign_id, stripe_idx)` (free) or via the assembled LP image at `Project.result_image_url`.

## Ad Creative Sizing (separate from LP)

`generate_ad` and `generate_carousel` are independent tools that take their own `aspect_ratio` parameter (only `9:16` / `4:5` / `1:1` are valid for ads — see [`mcp-patterns.md`](./mcp-patterns.md) "Ad Campaign Creation"). LP aspect_ratio does **not** control ad output.

| Platform | Required Ad Ratio | Size |
|----------|-------------------|------|
| Meta Feed (IG / FB post) | `1:1` | 1080×1080 |
| Meta / IG Stories / Reels | `9:16` | 1080×1920 |
| IG portrait feed | `4:5` | 1080×1350 |
| TikTok Feed | `9:16` | 1080×1920 |

The `generate_ad` tool re-renders LP content for the chosen platform ratio independently of the underlying LP aspect_ratio.
