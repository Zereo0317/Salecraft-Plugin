"""
SaleCraft Design System v3 - MOBILE-FIRST
All sizing optimized for phone viewing (~390px display width)
Min body text: 40px | Min header: 70px | Single-column | One idea per slide
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, textwrap

# ==========================================
# BRAND TOKENS
# ==========================================
PINK = (238, 79, 114)
PINK_LIGHT = (255, 180, 200)
DARK = (18, 18, 28)
DARK2 = (28, 28, 42)
WHITE = (255, 255, 255)
OFF_WHITE = (248, 248, 252)
GRAY = (160, 160, 175)
GRAY_DARK = (90, 90, 110)
TEXT = (30, 30, 48)
SUCCESS = (46, 204, 113)
INFO = (80, 120, 220)
WARN = (243, 156, 18)

W, H = 1080, 1350
FONT_DIR = "/home/user/fonts"
BG_DIR = "/home/user/bg_images"
OUT_DIR = "/home/user/instagram_v3"
os.makedirs(OUT_DIR, exist_ok=True)

LOGO_PINK = "/root/.claude/uploads/66c41c29-cbb3-4bfa-9a45-be195219f08f/e8e033b1-1000017371.webp"
LOGO_WHITE = "/root/.claude/uploads/66c41c29-cbb3-4bfa-9a45-be195219f08f/92315f26-1000017369.webp"


def font(weight="bold", size=40):
    weights = {
        "extrabold": "Montserrat-ExtraBold.ttf",
        "bold": "Montserrat-Bold.ttf",
        "semi": "Montserrat-SemiBold.ttf",
        "medium": "Montserrat-Medium.ttf",
        "regular": "Montserrat-Regular.ttf",
    }
    return ImageFont.truetype(os.path.join(FONT_DIR, weights[weight]), size)


def pixel_wrap(text, fnt, max_width, draw):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        test = f"{cur} {word}".strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= max_width:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = word
    if cur: lines.append(cur)
    return lines


def center_text(draw, text, y, fnt, fill=TEXT):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(((W - tw) // 2, y), text, fill=fill, font=fnt)
    return th


def center_text_shadow(draw, text, y, fnt, fill=WHITE, shadow=(0,0,0)):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    draw.text((x + 3, y + 3), text, fill=shadow, font=fnt)
    draw.text((x, y), text, fill=fill, font=fnt)
    return bbox[3] - bbox[1]


def center_multiline(draw, text, y, fnt, fill, max_w=900, spacing=16):
    lines = pixel_wrap(text, fnt, max_w, draw)
    lh = fnt.getbbox("Ag")[3]
    for i, line in enumerate(lines):
        center_text(draw, line, y + i * (lh + spacing), fnt, fill)
    return len(lines) * (lh + spacing)


def load_bg(name):
    bg = Image.open(os.path.join(BG_DIR, f"{name}.png")).convert("RGB")
    return bg.resize((W, H), Image.LANCZOS)


def glass_card(canvas, xy, radius=24, alpha=200, color=(255,255,255)):
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rounded_rectangle(xy, radius=radius, fill=(*color, alpha))
    od.rounded_rectangle(xy, radius=radius, outline=(*color, min(alpha + 30, 255)), width=2)
    result = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
    canvas.paste(result)
    return ImageDraw.Draw(canvas)


def dark_glass(canvas, xy, radius=24, alpha=170):
    return glass_card(canvas, xy, radius, alpha, (22, 22, 38))


def draw_icon(draw, cx, cy, r, color, icon_type):
    """Large, bold icons visible on mobile."""
    draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=color)
    ic = WHITE
    lw = max(4, r // 8)

    if icon_type == "search":
        mr = r * 0.32
        draw.ellipse([(cx - mr - 4, cy - mr - 4), (cx + mr - 4, cy + mr - 4)], outline=ic, width=lw)
        draw.line([(cx + mr * 0.4, cy + mr * 0.4), (cx + r * 0.55, cy + r * 0.55)], fill=ic, width=lw + 1)
    elif icon_type == "cart":
        bw = r * 0.5
        draw.rounded_rectangle([(cx - bw, cy - bw * 0.4), (cx + bw, cy + bw * 0.6)], radius=4, outline=ic, width=lw)
        draw.line([(cx - bw - r * 0.15, cy - bw * 0.6), (cx - bw, cy - bw * 0.4)], fill=ic, width=lw)
        draw.ellipse([(cx - bw * 0.5 - 5, cy + bw * 0.7 - 5), (cx - bw * 0.5 + 5, cy + bw * 0.7 + 5)], fill=ic)
        draw.ellipse([(cx + bw * 0.3 - 5, cy + bw * 0.7 - 5), (cx + bw * 0.3 + 5, cy + bw * 0.7 + 5)], fill=ic)
    elif icon_type == "check":
        draw.line([(cx - r * 0.3, cy + r * 0.05), (cx - r * 0.05, cy + r * 0.3), (cx + r * 0.35, cy - r * 0.25)], fill=ic, width=lw + 2, joint="curve")
    elif icon_type == "rocket":
        draw.polygon([(cx, cy - r * 0.4), (cx - r * 0.22, cy + r * 0.35), (cx + r * 0.22, cy + r * 0.35)], fill=ic)
        draw.line([(cx - r * 0.3, cy + r * 0.2), (cx - r * 0.18, cy + r * 0.05)], fill=ic, width=lw)
        draw.line([(cx + r * 0.3, cy + r * 0.2), (cx + r * 0.18, cy + r * 0.05)], fill=ic, width=lw)
    elif icon_type == "shield":
        pts = [(cx, cy - r * 0.4), (cx + r * 0.35, cy - r * 0.15),
               (cx + r * 0.35, cy + r * 0.1), (cx, cy + r * 0.4),
               (cx - r * 0.35, cy + r * 0.1), (cx - r * 0.35, cy - r * 0.15)]
        draw.polygon(pts, outline=ic, fill=None)
        draw.polygon(pts, fill=ic)
    elif icon_type == "bolt":
        draw.polygon([(cx + r * 0.05, cy - r * 0.4), (cx - r * 0.2, cy + r * 0.05),
                       (cx + r * 0.02, cy + r * 0.05), (cx - r * 0.05, cy + r * 0.4),
                       (cx + r * 0.2, cy - r * 0.05), (cx - r * 0.02, cy - r * 0.05)], fill=ic)
    elif icon_type == "chart":
        draw.rectangle([(cx - r * 0.35, cy + r * 0.05), (cx - r * 0.12, cy + r * 0.35)], fill=ic)
        draw.rectangle([(cx - r * 0.1, cy - r * 0.2), (cx + r * 0.12, cy + r * 0.35)], fill=ic)
        draw.rectangle([(cx + r * 0.15, cy - r * 0.35), (cx + r * 0.38, cy + r * 0.35)], fill=ic)
    elif icon_type == "globe":
        mr = r * 0.38
        draw.ellipse([(cx - mr, cy - mr), (cx + mr, cy + mr)], outline=ic, width=lw)
        draw.arc([(cx - mr * 0.45, cy - mr), (cx + mr * 0.45, cy + mr)], 0, 360, fill=ic, width=lw - 1)
        draw.line([(cx - mr, cy), (cx + mr, cy)], fill=ic, width=lw - 1)


def add_footer(canvas, dark=True):
    draw = ImageDraw.Draw(canvas)
    fy = H - 70
    draw.rectangle([(0, fy), (W, H)], fill=(10, 10, 18) if dark else (235, 235, 240))
    draw.rectangle([(0, fy), (W, fy + 3)], fill=PINK)
    logo = Image.open(LOGO_PINK).convert("RGBA").resize((42, 42), Image.LANCZOS)
    lx = W // 2 - 55
    canvas.paste(logo, (lx, fy + 14), logo)
    tc = (140, 140, 155) if dark else GRAY_DARK
    draw.text((lx + 50, fy + 25), "SALECRAFT", fill=tc, font=font("semi", 18))
    return draw


# ==========================================
# SLIDE 1: COVER (one big message)
# ==========================================
def slide_1():
    canvas = load_bg("cover_bg")
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 90))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(0, 0), (W, 6)], fill=PINK)

    logo = Image.open(LOGO_PINK).convert("RGBA").resize((160, 160), Image.LANCZOS)
    canvas.paste(logo, (W // 2 - 80, 160), logo)

    center_text_shadow(draw, "GOOGLE", 380, font("extrabold", 100), WHITE)
    center_text_shadow(draw, "UCP", 490, font("extrabold", 100), PINK)

    center_text(draw, "Universal Commerce Protocol", 630, font("medium", 36), GRAY)

    lw = 140
    draw.rectangle([(W // 2 - lw // 2, 700), (W // 2 + lw // 2, 704)], fill=PINK)

    center_text(draw, "The Future of", 750, font("semi", 44), PINK_LIGHT)
    center_text(draw, "E-Commerce is Here", 810, font("semi", 44), PINK_LIGHT)

    # Large badge
    bt = "GOOGLE I/O 2026"
    bf = font("bold", 26)
    bb = draw.textbbox((0, 0), bt, font=bf)
    bw, bh = bb[2] - bb[0] + 60, bb[3] - bb[1] + 36
    bx, by = W // 2 - bw // 2, 920
    draw.rounded_rectangle((bx, by, bx + bw, by + bh), radius=bh // 2, outline=PINK, width=3)
    draw.text((bx + 30, by + 14), bt, fill=PINK, font=bf)

    center_text(draw, "SWIPE  →", H - 130, font("semi", 24), GRAY)
    add_footer(canvas)
    canvas.save(f"{OUT_DIR}/01_cover.png", quality=95)
    print("  Slide 1: Cover")


# ==========================================
# SLIDE 2: WHAT IS UCP (simple explanation)
# ==========================================
def slide_2():
    canvas = load_bg("info_bg")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(0, 0), (W, 6)], fill=PINK)

    center_text(draw, "What is", 60, font("bold", 48), GRAY_DARK)
    center_text(draw, "Google UCP?", 120, font("extrabold", 64), TEXT)
    draw.rectangle([(W // 2 - 50, 205), (W // 2 + 50, 210)], fill=PINK)

    # Single glass card with large readable text
    draw = glass_card(canvas, (60, 250, W - 60, 640), radius=24, alpha=230)

    body = "A new open-source protocol that lets customers buy your products directly inside Google Search, Gemini, YouTube & Gmail."
    center_multiline(draw, body, 290, font("semi", 36), TEXT, max_w=860, spacing=18)

    # Simple highlight
    center_text(draw, "No redirects.", 570, font("extrabold", 40), PINK)

    # Partner bar - LARGE text
    py = 690
    draw = glass_card(canvas, (60, py, W - 60, py + 200), radius=24, alpha=210, color=(255, 235, 242))

    center_text(draw, "Built with", py + 25, font("medium", 30), GRAY_DARK)
    center_text(draw, "Shopify • Walmart", py + 75, font("bold", 38), TEXT)
    center_text(draw, "Target • Etsy • Wayfair", py + 125, font("bold", 38), TEXT)
    center_text(draw, "+ Stripe, Visa, Mastercard & 20 more", py + 175, font("medium", 22), GRAY_DARK)

    # Big number
    center_text(draw, "20+", 950, font("extrabold", 120), PINK)
    center_text(draw, "Global Partners", 1080, font("semi", 32), TEXT)

    add_footer(canvas, dark=True)
    canvas.save(f"{OUT_DIR}/02_what_is_ucp.png", quality=95)
    print("  Slide 2: What is UCP")


# ==========================================
# SLIDE 3: HOW - DISCOVER
# ==========================================
def slide_3():
    canvas = load_bg("flow_bg")
    overlay = Image.new("RGBA", (W, H), (255, 255, 255, 160))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(0, 0), (W, 6)], fill=PINK)

    center_text(draw, "How It Works", 50, font("extrabold", 56), TEXT)
    draw.rectangle([(W // 2 - 50, 122), (W // 2 + 50, 127)], fill=PINK)

    # Step 1: DISCOVER
    sy = 180
    draw = glass_card(canvas, (60, sy, W - 60, sy + 300), radius=24, alpha=230)
    draw_icon(draw, 160, sy + 80, 50, PINK, "search")
    draw.text((230, sy + 50), "STEP 1", fill=GRAY, font=font("bold", 24))
    draw.text((230, sy + 85), "DISCOVER", fill=PINK, font=font("extrabold", 48))
    center_multiline(draw, "AI agents find your products across Google Search, Gemini, YouTube & Gmail", sy + 180, font("medium", 34), GRAY_DARK, max_w=840, spacing=14)

    # Arrow
    draw.polygon([(W // 2 - 15, sy + 315), (W // 2 + 15, sy + 315), (W // 2, sy + 340)], fill=PINK)

    # Step 2: CART
    sy2 = sy + 365
    draw = glass_card(canvas, (60, sy2, W - 60, sy2 + 300), radius=24, alpha=230)
    draw_icon(draw, 160, sy2 + 80, 50, INFO, "cart")
    draw.text((230, sy2 + 50), "STEP 2", fill=GRAY, font=font("bold", 24))
    draw.text((230, sy2 + 85), "CART", fill=INFO, font=font("extrabold", 48))
    center_multiline(draw, "Universal Cart collects items from multiple retailers in one smart hub", sy2 + 180, font("medium", 34), GRAY_DARK, max_w=840, spacing=14)

    # Arrow
    draw.polygon([(W // 2 - 15, sy2 + 315), (W // 2 + 15, sy2 + 315), (W // 2, sy2 + 340)], fill=PINK)

    # Step 3: CHECKOUT
    sy3 = sy2 + 365
    draw = glass_card(canvas, (60, sy3, W - 60, sy3 + 300), radius=24, alpha=230)
    draw_icon(draw, 160, sy3 + 80, 50, SUCCESS, "check")
    draw.text((230, sy3 + 50), "STEP 3", fill=GRAY, font=font("bold", 24))
    draw.text((230, sy3 + 85), "CHECKOUT", fill=SUCCESS, font=font("extrabold", 48))
    center_multiline(draw, "Secure Google Pay checkout. You stay Merchant of Record.", sy3 + 180, font("medium", 34), GRAY_DARK, max_w=840, spacing=14)

    add_footer(canvas)
    canvas.save(f"{OUT_DIR}/03_how_it_works.png", quality=95)
    print("  Slide 3: How it Works")


# ==========================================
# SLIDE 4: UNIVERSAL CART (one feature, big)
# ==========================================
def slide_4():
    canvas = load_bg("info_bg")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(0, 0), (W, 6)], fill=PINK)

    center_text(draw, "Universal Cart", 55, font("extrabold", 60), TEXT)
    center_text(draw, "One cart. Every surface.", 130, font("medium", 34), GRAY_DARK)
    draw.rectangle([(W // 2 - 50, 185), (W // 2 + 50, 190)], fill=PINK)

    # Feature list - single column, large items
    features = [
        ("search", PINK, "Cross-Platform", "Works across Search, Gemini,\nYouTube & Gmail"),
        ("check", SUCCESS, "Instant Checkout", "Google Pay in a few taps.\nNo redirects."),
        ("shield", INFO, "You Stay in Control", "Full customer data ownership.\nTokenized payments."),
        ("globe", WARN, "Expanding Globally", "US this summer. Canada,\nUK & Australia next."),
    ]

    fy = 230
    card_h = 190
    gap = 25

    for i, (icon, color, title, desc) in enumerate(features):
        cy = fy + i * (card_h + gap)
        draw = glass_card(canvas, (60, cy, W - 60, cy + card_h), radius=20, alpha=230)

        # Colored left bar
        draw.rectangle([(60, cy + 20), (67, cy + card_h - 20)], fill=color)

        # Large icon
        draw_icon(draw, 140, cy + card_h // 2, 42, color, icon)

        # Title - LARGE
        draw.text((200, cy + 30), title, fill=color, font=font("bold", 36))

        # Description - readable size
        df = font("regular", 28)
        for j, dl in enumerate(desc.split("\n")):
            draw.text((200, cy + 85 + j * 38), dl, fill=GRAY_DARK, font=df)

    # Bottom CTA
    cta_y = fy + 4 * (card_h + gap) + 20
    draw.rounded_rectangle((80, cta_y, W - 80, cta_y + 80), radius=40, fill=PINK)
    center_text(draw, "AI shopping is already here", cta_y + 20, font("bold", 32), WHITE)

    add_footer(canvas)
    canvas.save(f"{OUT_DIR}/04_universal_cart.png", quality=95)
    print("  Slide 4: Universal Cart")


# ==========================================
# SLIDE 5: WHY YOUR STORE NEEDS THIS
# ==========================================
def slide_5():
    canvas = load_bg("dark_benefits_bg")
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 120))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(0, 0), (W, 6)], fill=PINK)

    center_text_shadow(draw, "Why Your Store", 55, font("extrabold", 52), WHITE)
    center_text_shadow(draw, "Needs UCP", 120, font("extrabold", 52), PINK_LIGHT)
    draw.rectangle([(W // 2 - 50, 195), (W // 2 + 50, 200)], fill=PINK)

    # Single column benefits - LARGE
    benefits = [
        ("rocket", PINK, "Reach AI Shoppers", "High-intent buyers on\nGoogle's AI surfaces"),
        ("shield", SUCCESS, "Stay in Control", "You = Merchant of Record.\nYour data. Your customers."),
        ("bolt", WARN, "Kill Cart Abandonment", "Discovery → purchase\nin fewer steps"),
        ("chart", INFO, "Data > Keywords", "Structured attributes are\nthe new SEO"),
    ]

    by = 240
    card_h = 185
    gap = 22

    for i, (icon, color, title, desc) in enumerate(benefits):
        cy = by + i * (card_h + gap)
        draw = dark_glass(canvas, (60, cy, W - 60, cy + card_h), radius=20, alpha=170)

        # Left accent
        draw.rectangle([(60, cy + 20), (67, cy + card_h - 20)], fill=color)

        draw_icon(draw, 140, cy + card_h // 2, 42, color, icon)

        draw.text((200, cy + 25), title, fill=color, font=font("bold", 36))

        df = font("regular", 28)
        for j, dl in enumerate(desc.split("\n")):
            draw.text((200, cy + 80 + j * 38), dl, fill=(200, 200, 220), font=df)

    # Quote - LARGE
    qy = by + 4 * (card_h + gap) + 15
    draw = dark_glass(canvas, (60, qy, W - 60, qy + 130), radius=20, alpha=170)
    draw.rounded_rectangle((60, qy, W - 60, qy + 130), radius=20, outline=PINK, width=3)

    center_text(draw, '"Keywords are dead;', qy + 20, font("bold", 36), WHITE)
    center_text(draw, 'attributes are king."', qy + 68, font("bold", 36), PINK_LIGHT)

    add_footer(canvas)
    canvas.save(f"{OUT_DIR}/05_why_ecommerce.png", quality=95)
    print("  Slide 5: Why E-Commerce")


# ==========================================
# SLIDE 6: CTA - GET READY
# ==========================================
def slide_6():
    canvas = load_bg("cta_bg")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(0, 0), (W, 6)], fill=WHITE)

    logo = Image.open(LOGO_WHITE).convert("RGBA").resize((120, 120), Image.LANCZOS)
    a = logo.split()[-1].point(lambda p: min(p, 200))
    logo.putalpha(a)
    canvas.paste(logo, (W // 2 - 60, 50), logo)

    center_text_shadow(draw, "Get UCP-Ready", 210, font("extrabold", 64), WHITE, (150, 40, 70))
    draw.rectangle([(W // 2 - 60, 295), (W // 2 + 60, 299)], fill=WHITE)

    # Large checklist items
    items = [
        "Optimize product feed data",
        "Set up Merchant Center",
        "Complete product attributes",
        "Structured data > keywords",
        "Prepare for AI commerce",
    ]

    iy_start = 340
    item_h = 80
    gap = 18

    for i, item in enumerate(items):
        iy = iy_start + i * (item_h + gap)

        draw = glass_card(canvas, (70, iy, W - 70, iy + item_h), radius=16, alpha=60, color=(255, 255, 255))

        # Large check circle
        cr = 22
        ccx, ccy = 120, iy + item_h // 2
        draw.ellipse([(ccx - cr, ccy - cr), (ccx + cr, ccy + cr)], fill=WHITE)
        draw.line([(ccx - 8, ccy + 2), (ccx - 2, ccy + 10), (ccx + 10, ccy - 6)], fill=PINK, width=4)

        # Text - LARGE
        draw.text((160, iy + 18), item, fill=WHITE, font=font("bold", 32))

    # Divider
    dy = iy_start + 5 * (item_h + gap) + 10
    draw.rectangle([(140, dy), (W - 140, dy + 2)], fill=(255, 255, 255, 120))

    # URL - readable
    center_text(draw, "START HERE", dy + 30, font("medium", 24), (255, 210, 220))
    center_text_shadow(draw, "developers.google.com", dy + 65, font("bold", 30), WHITE, (150, 40, 70))
    center_text_shadow(draw, "/merchant/ucp", dy + 105, font("bold", 30), WHITE, (150, 40, 70))

    # Save button - LARGE
    sy = dy + 170
    bw = 500
    draw.rounded_rectangle((W // 2 - bw // 2, sy, W // 2 + bw // 2, sy + 75), radius=38, fill=WHITE)
    center_text(draw, "Save this post!", sy + 18, font("bold", 32), PINK)

    # Footer
    fy = H - 70
    draw.rectangle([(0, fy), (W, H)], fill=(180, 50, 80))
    draw.rectangle([(0, fy), (W, fy + 3)], fill=WHITE)
    logo_f = Image.open(LOGO_WHITE).convert("RGBA").resize((42, 42), Image.LANCZOS)
    af = logo_f.split()[-1].point(lambda p: min(p, 200))
    logo_f.putalpha(af)
    lx = W // 2 - 55
    canvas.paste(logo_f, (lx, fy + 14), logo_f)
    draw = ImageDraw.Draw(canvas)
    draw.text((lx + 50, fy + 25), "SALECRAFT", fill=(255, 200, 215), font=font("semi", 18))

    canvas.save(f"{OUT_DIR}/06_cta.png", quality=95)
    print("  Slide 6: CTA")


# ==========================================
if __name__ == "__main__":
    print("Generating v3 MOBILE-FIRST carousel...\n")
    slide_1()
    slide_2()
    slide_3()
    slide_4()
    slide_5()
    slide_6()
    print(f"\nAll 6 slides → {OUT_DIR}/")
