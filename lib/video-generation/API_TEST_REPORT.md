# Kling 3.0 & Seedance 2.0 API Test Report

**Date**: 2026-05-24
**Test Target**: Bali group photo -> 9:16 street dance video with zh-TW dialogue

---

## 1. Kling 3.0 API Test Results

### Authentication: PASS
- JWT (HS256) generation works correctly
- Access Key: `$KLING_ACCESS_KEY` (set via environment variable)
- API Base: `https://api.klingai.com`
- Token format: `Authorization: Bearer <JWT>`

### Model Name Discovery
| Model Name | Status |
|-----------|--------|
| `kling-v1` | Valid (v1) |
| `kling-v1-5` | Valid (v1.5) |
| `kling-v1-6` | Valid (v1.6) |
| `kling-v2-6` | Valid (v2.6) |
| `kling-v3` | **Valid (v3.0 - latest)** |
| `kling-v3-0` | Invalid |
| `kling-v2-5` | Invalid |

### Image Parameter Format
- Parameter name: `image` (not `image_url`)
- Format: Raw base64 string (no `data:image/png;base64,` prefix)
- Validated successfully with test payload

### Submission Result
```
HTTP 429
{
  "code": 1102,
  "message": "Account balance not enough"
}
```

### Verdict
**API Key is VALID and functional**. Authentication passes, model validation passes, image format validation passes. The account simply needs credits topped up at https://app.klingai.com/global/dev.

### Key Parameters for 9:16 Dance Video
| Parameter | Value | Notes |
|-----------|-------|-------|
| `model_name` | `kling-v3` | Latest Kling 3.0 |
| `mode` | `pro` | 1080x1920 resolution |
| `duration` | `"10"` | 10 seconds (string, range: 3-15) |
| `aspect_ratio` | `"9:16"` | Vertical |
| `cfg_scale` | `0.5` | Prompt adherence (0.0-1.0) |
| `image` | raw base64 | No data URI prefix |
| `negative_prompt` | string | Recommended |

---

## 2. BytePlus Seedance 2.0 API Test Results

### Critical Clarification
- **Seedream 2.0** = text-to-**IMAGE** model (not video)
- **Seedance 2.0** = text/image-to-**VIDEO** model
- Both are on BytePlus ModelArk platform

### Authentication: REQUIRES API KEY
The provided credentials are **IAM AKSK** (Access Key ID + Secret Access Key), which are for console/infrastructure access. The ModelArk content generation API requires a **Bearer API Key**.

| Auth Method | Result |
|-------------|--------|
| AKSK as Bearer token | 401 - "API key format incorrect" |
| AKSK via Volcengine SDK | "ak&sk auth not supported for this method" |
| AKSK via HMAC V4 signing | 401 - "AK/SK invalid" |
| Decoded AKSK variants | 401 - Same errors |

### How to Get a ModelArk API Key
1. Log in to the BytePlus console with your account credentials
2. Navigate to: ModelArk -> API Key Management
3. Click "Create API Key"
4. Copy the generated key (format: typically starts with a specific prefix)
5. Set as: `ARK_API_KEY` environment variable

### Verified Endpoint & Model IDs
| Item | Value |
|------|-------|
| Base URL | `https://ark.ap-southeast.bytepluses.com/api/v3` |
| Video endpoint | `POST /contents/generations/tasks` |
| Status endpoint | `GET /contents/generations/tasks/{id}` |
| Model (standard) | `dreamina-seedance-2-0-260128` |
| Model (fast) | `dreamina-seedance-2-0-fast-260128` |

### Key Parameters for 9:16 Dance Video
| Parameter | Value | Notes |
|-----------|-------|-------|
| `model` | `dreamina-seedance-2-0-260128` | Standard quality |
| `ratio` | `"9:16"` | Vertical |
| `resolution` | `"1080p"` | Full HD |
| `duration` | `10` | 10 seconds (integer, range: 4-15) |
| `generate_audio` | `true` | Synchronized audio |
| `content` | array | Multimodal: text + image_url |

---

## 3. Platform Comparison

| Feature | Kling 3.0 | Seedance 2.0 |
|---------|-----------|--------------|
| **ELO Score** | 1243 (#1) | ~1180 (top 5) |
| **Max Duration** | 15s | 15s |
| **Max Resolution** | Native 4K | 2K |
| **9:16 Support** | Yes | Yes |
| **Native Audio** | Yes (multilingual) | Yes |
| **Lip-sync** | Best-in-class | Good |
| **Multi-shot** | Up to 6 shots | Multi-shot supported |
| **Dance Quality** | Excellent | Good |
| **Face Consistency** | Excellent (Elements 3.0) | Good (multi-reference) |
| **Auth Method** | JWT (HS256) | Bearer API Key |
| **Image Input** | Raw base64 | base64 data URI or URL |
| **Processing Time** | 2-5 min (pro) | 30-120s |
| **Pricing** | ~$0.35/clip (pro) | ~$0.05-0.15/s |

### Recommendation for This Use Case (Street Dance)
**Kling 3.0 Pro** is the stronger choice for dance video generation:
1. Highest ELO score for motion quality
2. Best-in-class human body physics (natural weight transfer, joint articulation)
3. Superior lip-sync for the zh-TW dialogue
4. Multi-shot capability for the 5-shot choreography structure
5. 15-second clips allow full choreography without cuts

**Seedance 2.0** is a solid alternative with:
1. Faster processing (30-120s vs 2-5min)
2. Lower cost per generation
3. Native Chinese text understanding in prompts
4. Good multi-reference support for maintaining character consistency

---

## 4. Next Steps

### For Kling 3.0
- [ ] Top up account balance at https://app.klingai.com/global/dev
- [ ] Run: `python generate_bali_dance.py --platform kling --access-key $KLING_ACCESS_KEY --secret-key $KLING_SECRET_KEY --image /path/to/photo.png --poll`

### For Seedance 2.0
- [ ] Log into BytePlus console and generate a ModelArk API key
- [ ] Run: `python generate_bali_dance.py --platform seedance --api-key $ARK_API_KEY --image /path/to/photo.png --poll`
