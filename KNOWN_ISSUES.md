# SaleCraft Plugin — Known Issues

## RESOLVED

### 1. update_stripe_texts was silently ignoring updates
- **Root cause**: Plugin docs used wrong JSON format
- **Fix**: Backend expects `{"index": N, "headline": "...", "subheadline": "..."}` — fields set directly
- **Status**: FIXED in plugin skills + CLAUDE.md

### 2. update_brand not persisting extra fields (tagline, value_proposition, etc.)
- **Root cause**: MCP wrapper only accepted 5 fixed params, ignored `data_json`
- **Fix**: Added `data_json` parameter support to `update_brand` in MCP wrapper
- **Status**: FIXED

### 3. regenerate_stripe 3-step flow was not documented
- **Root cause**: Plugin skill only called `regenerate_stripe` but missed the required `complete_regeneration` step
- **Fix**: Documented full 3-step flow (trigger -> poll -> confirm) in edit-landing skill + CLAUDE.md
- **Status**: FIXED

### 5. Inline image upload (base64)
- **Status**: FIXED
- **Solution**: Added `upload_base64` MCP tool — accepts base64 data directly, no disk save needed
- **Flow**: User provides image → AI reads as base64 → `upload_base64` → public_url
- **Works on**: Any AI platform that can read image data as base64

### Resolved in v0.3.0
- **Missing hooks**: Added SessionStart, PreToolUse (paid action guard), and Stop (brand-memory auto-save) hooks
- **No agents**: Added strategy-advisor, content-optimizer, and campaign-auditor specialized agents
- **No knowledge skills**: Added 8 knowledge-based skills covering SEO/GEO/AEO, PRISM influence framework, cognitive-behavioral science, content engineering, social theory, media algorithms, marketing growth, and personal OS/charisma
- **Skill count discrepancy**: CLAUDE.md referenced 25 skills but directory had 27; now 35 skills total with accurate count
- **No progressive disclosure**: New knowledge skills use references/ subdirectories for detailed content

## OPEN

### 4. AI image generation may render metadata as visible text
- **Status**: Open (backend prompt engineering issue)
- **Symptom**: Debug-style text (font/size/color info) rendered in stripe images
- **Impact**: Unprofessional-looking stripes with debug-style text
- **Workaround**: Regenerate the stripe — usually resolves on retry

### 6. Image generation can hang
- **Status**: Known backend issue (not plugin-related)
- **Symptom**: `progress_stage: "producing"` stays at 70% for extended time
- **Workaround**: Wait up to 10 min; if still stuck, the backend may eventually complete or timeout
