"""
SaleCraft Design System v2 - Professional Instagram Carousel Generator
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os, math

# ==========================================
# BRAND TOKENS
# ==========================================
class Brand:
    PINK = (238, 79, 114)
    PINK_LIGHT = (255, 180, 200)
    PINK_GLOW = (238, 79, 114, 60)
    DARK = (18, 18, 28)
    DARK2 = (28, 28, 42)
    DARK3 = (38, 38, 55)
    WHITE = (255, 255, 255)
    OFF_WHITE = (248, 248, 252)
    LIGHT_BG = (245, 245, 248)
    GRAY = (160, 160, 175)
    GRAY_DARK = (100, 100, 120)
    TEXT = (30, 30, 48)
    NAVY = (20, 30, 80)
    SUCCESS = (46, 204, 113)
    INFO = (80, 120, 220)
    WARN = (243, 156, 18)

class Spacing:
    XS = 8
    SM = 16
    MD = 24
    LG = 40
    XL = 60
    XXL = 80

W, H = 1080, 1350
FONT_DIR = "/home/user/fonts"
BG_DIR = "/home/user/bg_images"
OUT_DIR = "/home/user/instagram_v2"
os.makedirs(OUT_DIR, exist_ok=True)

LOGO_PINK = "/root/.claude/uploads/66c41c29-cbb3-4bfa-9a45-be195219f08f/e8e033b1-1000017371.webp"
LOGO_WHITE = "/root/.claude/uploads/66c41c29-cbb3-4bfa-9a45-be195219f08f/92315f26-1000017369.webp"

# ==========================================
# FONT SYSTEM
# ==========================================
def font(weight="bold", size=32):
    weights = {
        "extrabold": "Montserrat-ExtraBold.ttf",
        "bold": "Montserrat-Bold.ttf",
        "semi": "Montserrat-SemiBold.ttf",
        "medium": "Montserrat-Medium.ttf",
        "regular": "Montserrat-Regular.ttf",
    }
    return ImageFont.truetype(os.path.join(FONT_DIR, weights[weight]), size)


# ==========================================
# DRAWING HELPERS
# ==========================================
def pixel_wrap(text, fnt, max_width, draw):
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        test = f"{cur} {word}".strip()
        if draw.textbbox((0,0), test, font=fnt)[2] <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_center(draw, text, y, fnt, fill=Brand.TEXT):
    bbox = draw.textbbox((0,0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, y), text, fill=fill, font=fnt)
    return bbox[3] - bbox[1]


def text_center_shadow(draw, text, y, fnt, fill=Brand.WHITE, shadow=(0,0,0)):
    bbox = draw.textbbox((0,0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    draw.text((x+2, y+2), text, fill=shadow, font=fnt)
    draw.text((x, y), text, fill=fill, font=fnt)
    return bbox[3] - bbox[1]


def multiline_center(draw, lines, y, fnt, fill, spacing=10):
    lh = fnt.getbbox("A")[3]
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0,0), line, font=fnt)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, y + i * (lh + spacing)), line, fill=fill, font=fnt)
    return len(lines) * (lh + spacing)


def load_bg(name):
    bg = Image.open(os.path.join(BG_DIR, f"{name}.png")).convert("RGB")
    return bg.resize((W, H), Image.LANCZOS)


def glass_card(canvas, xy, radius=20, fill_alpha=180, fill_color=(255,255,255), blur=0):
    """Draw a frosted glass card effect."""
    x0, y0, x1, y1 = xy
    overlay = Image.new("RGBA", canvas.size, (0,0,0,0))
    od = ImageDraw.Draw(overlay)
    od.rounded_rectangle(xy, radius=radius, fill=(*fill_color, fill_alpha))
    # Subtle border
    od.rounded_rectangle(xy, radius=radius, outline=(*fill_color, min(fill_alpha + 40, 255)), width=1)
    canvas.paste(Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB"))
    return ImageDraw.Draw(canvas)


def dark_glass_card(canvas, xy, radius=20, alpha=160):
    return glass_card(canvas, xy, radius, alpha, (20, 20, 35))


def draw_circle_icon(draw, cx, cy, r, color, icon_type="search"):
    """Draw a simple icon inside a colored circle."""
    draw.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=color)

    # Draw simple icon shapes
    ic = Brand.WHITE
    if icon_type == "search":
        # Magnifying glass
        mr = r * 0.35
        draw.ellipse([(cx-mr-3, cy-mr-3), (cx+mr-3, cy+mr-3)], outline=ic, width=3)
        draw.line([(cx+mr*0.5, cy+mr*0.5), (cx+r*0.6, cy+r*0.6)], fill=ic, width=3)
    elif icon_type == "cart":
        # Shopping cart
        draw.line([(cx-r*0.4, cy-r*0.2), (cx+r*0.4, cy-r*0.2)], fill=ic, width=3)
        draw.line([(cx-r*0.35, cy-r*0.2), (cx-r*0.25, cy+r*0.2)], fill=ic, width=3)
        draw.line([(cx+r*0.35, cy-r*0.2), (cx+r*0.25, cy+r*0.2)], fill=ic, width=3)
        draw.line([(cx-r*0.25, cy+r*0.2), (cx+r*0.25, cy+r*0.2)], fill=ic, width=3)
        draw.ellipse([(cx-r*0.2-4, cy+r*0.35-4), (cx-r*0.2+4, cy+r*0.35+4)], fill=ic)
        draw.ellipse([(cx+r*0.2-4, cy+r*0.35-4), (cx+r*0.2+4, cy+r*0.35+4)], fill=ic)
    elif icon_type == "check":
        # Checkmark
        pts = [(cx-r*0.3, cy), (cx-r*0.05, cy+r*0.3), (cx+r*0.35, cy-r*0.25)]
        draw.line(pts[:2], fill=ic, width=4)
        draw.line(pts[1:], fill=ic, width=4)
    elif icon_type == "rocket":
        # Simple rocket
        draw.polygon([(cx, cy-r*0.45), (cx-r*0.2, cy+r*0.3), (cx+r*0.2, cy+r*0.3)], fill=ic)
        draw.rectangle([(cx-r*0.08, cy+r*0.1), (cx+r*0.08, cy+r*0.4)], fill=ic)
    elif icon_type == "shield":
        # Shield
        draw.polygon([(cx, cy-r*0.4), (cx-r*0.3, cy-r*0.15), (cx-r*0.3, cy+r*0.15), (cx, cy+r*0.4), (cx+r*0.3, cy+r*0.15), (cx+r*0.3, cy-r*0.15)], fill=ic)
    elif icon_type == "bolt":
        # Lightning bolt
        draw.polygon([(cx-r*0.05, cy-r*0.4), (cx-r*0.25, cy+r*0.05), (cx-r*0.02, cy+r*0.05), (cx+r*0.05, cy+r*0.4), (cx+r*0.25, cy-r*0.05), (cx+r*0.02, cy-r*0.05)], fill=ic)
    elif icon_type == "chart":
        # Bar chart
        draw.rectangle([(cx-r*0.35, cy+r*0.1), (cx-r*0.15, cy+r*0.35)], fill=ic)
        draw.rectangle([(cx-r*0.1, cy-r*0.15), (cx+r*0.1, cy+r*0.35)], fill=ic)
        draw.rectangle([(cx+r*0.15, cy-r*0.35), (cx+r*0.35, cy+r*0.35)], fill=ic)
    elif icon_type == "globe":
        mr = r * 0.35
        draw.ellipse([(cx-mr, cy-mr), (cx+mr, cy+mr)], outline=ic, width=2)
        draw.ellipse([(cx-mr*0.4, cy-mr), (cx+mr*0.4, cy+mr)], outline=ic, width=2)
        draw.line([(cx-mr, cy), (cx+mr, cy)], fill=ic, width=2)


def add_footer(canvas, dark=True):
    draw = ImageDraw.Draw(canvas)
    fy = H - 60
    bg_color = (10, 10, 18) if dark else (235, 235, 240)
    accent = Brand.PINK
    text_c = (130, 130, 150) if dark else Brand.GRAY

    draw.rectangle([(0, fy), (W, H)], fill=bg_color)
    draw.rectangle([(0, fy), (W, fy + 2)], fill=accent)

    logo_path = LOGO_PINK
    logo = Image.open(logo_path).convert("RGBA").resize((34, 34), Image.LANCZOS)
    lx = W // 2 - 50
    canvas.paste(logo, (lx, fy + 13), logo)
    draw.text((lx + 40, fy + 22), "SALECRAFT", fill=text_c, font=font("medium", 13))
    return draw


def add_top_bar(draw, color=Brand.PINK):
    draw.rectangle([(0, 0), (W, 5)], fill=color)


def add_page_indicator(draw, current, total=6):
    """Draw page dots at bottom above footer."""
    dot_r = 5
    gap = 20
    total_w = total * dot_r * 2 + (total - 1) * gap
    start_x = (W - total_w) // 2
    y = H - 80

    for i in range(total):
        cx = start_x + i * (dot_r * 2 + gap) + dot_r
        if i == current:
            draw.ellipse([(cx-dot_r, y-dot_r), (cx+dot_r, y+dot_r)], fill=Brand.PINK)
        else:
            draw.ellipse([(cx-dot_r, y-dot_r), (cx+dot_r, y+dot_r)], fill=Brand.GRAY, outline=Brand.GRAY)


# ==========================================
# SLIDE 1: COVER
# ==========================================
def slide_cover():
    canvas = load_bg("cover_bg")
    draw = ImageDraw.Draw(canvas)

    # Darken overlay for text readability
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 80))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(canvas)

    add_top_bar(draw)

    # SC Logo
    logo = Image.open(LOGO_PINK).convert("RGBA").resize((140, 140), Image.LANCZOS)
    canvas.paste(logo, (W//2 - 70, 200), logo)

    # Title
    text_center_shadow(draw, "GOOGLE", 400, font("extrabold", 82), Brand.WHITE)
    text_center_shadow(draw, "UCP", 490, font("extrabold", 82), Brand.PINK)

    # Subtitle
    text_center(draw, "Universal Commerce Protocol", 600, font("medium", 30), Brand.GRAY)

    # Accent line
    lw = 120
    draw.rectangle([(W//2 - lw//2, 660), (W//2 + lw//2, 663)], fill=Brand.PINK)

    # Tagline
    text_center(draw, "The Future of E-Commerce", 700, font("semi", 34), Brand.PINK_LIGHT)
    text_center(draw, "is Here", 745, font("semi", 34), Brand.PINK_LIGHT)

    # Badge
    badge_f = font("semi", 18)
    bt = "ANNOUNCED AT GOOGLE I/O 2026"
    bb = draw.textbbox((0,0), bt, font=badge_f)
    bw, bh = bb[2] - bb[0] + 40, bb[3] - bb[1] + 24
    bx = W//2 - bw//2
    by = 830
    draw.rounded_rectangle((bx, by, bx+bw, by+bh), radius=bh//2, outline=Brand.PINK, width=2)
    draw.text((bx+20, by+10), bt, fill=Brand.PINK, font=badge_f)

    # Swipe
    text_center(draw, "SWIPE TO LEARN MORE  →", H - 120, font("medium", 16), Brand.GRAY)

    add_page_indicator(draw, 0)
    add_footer(canvas)
    canvas.save(f"{OUT_DIR}/01_cover.png", quality=95)
    print("  Slide 1: Cover")


# ==========================================
# SLIDE 2: WHAT IS UCP
# ==========================================
def slide_what():
    canvas = load_bg("info_bg")
    draw = ImageDraw.Draw(canvas)
    add_top_bar(draw)

    # Header
    text_center(draw, "What is", 50, font("bold", 44), Brand.GRAY_DARK)
    text_center(draw, "Google UCP?", 100, font("extrabold", 52), Brand.TEXT)
    draw.rectangle([(W//2 - 40, 168), (W//2 + 40, 172)], fill=Brand.PINK)

    # Main explanation glass card
    draw = glass_card(canvas, (50, 200, W-50, 440), radius=20, fill_alpha=220, fill_color=(255,255,255))

    body = "An open-source protocol that creates a universal language for AI agents, merchants, and payment providers to work together seamlessly across the entire shopping journey."
    body_font = font("medium", 26)
    lines = pixel_wrap(body, body_font, W - 160, draw)
    y = 230
    for line in lines:
        bbox = draw.textbbox((0,0), line, font=body_font)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw)//2, y), line, fill=Brand.TEXT, font=body_font)
        y += 42

    # 3 capability cards
    caps = [
        ("search", Brand.PINK, "DISCOVER", "AI finds products\nacross all surfaces"),
        ("cart", Brand.INFO, "CART", "Universal Cart\nworks everywhere"),
        ("check", Brand.SUCCESS, "CHECKOUT", "Secure payment\nin a few taps"),
    ]

    card_w = 290
    card_h = 240
    gap = (W - 60 - 3 * card_w) // 2
    card_y = 480

    for i, (icon, color, title, desc) in enumerate(caps):
        cx = 30 + i * (card_w + gap)
        draw = glass_card(canvas, (cx, card_y, cx + card_w, card_y + card_h), radius=16, fill_alpha=230, fill_color=(255,255,255))

        # Icon
        draw_circle_icon(draw, cx + card_w//2, card_y + 55, 30, color, icon)

        # Title
        tf = font("bold", 22)
        tb = draw.textbbox((0,0), title, font=tf)
        draw.text((cx + (card_w - tb[2] + tb[0])//2, card_y + 100), title, fill=color, font=tf)

        # Desc
        df = font("regular", 17)
        for j, dl in enumerate(desc.split("\n")):
            db = draw.textbbox((0,0), dl, font=df)
            draw.text((cx + (card_w - db[2] + db[0])//2, card_y + 140 + j * 24), dl, fill=Brand.GRAY_DARK, font=df)

    # Partners section
    py = 770
    draw = glass_card(canvas, (50, py, W-50, py + 120), radius=16, fill_alpha=200, fill_color=(255, 235, 242))

    text_center(draw, "CO-DEVELOPED WITH INDUSTRY LEADERS", py + 18, font("bold", 18), Brand.PINK)
    text_center(draw, "Shopify  •  Walmart  •  Target  •  Etsy  •  Wayfair", py + 52, font("medium", 18), Brand.TEXT)
    text_center(draw, "Stripe  •  Visa  •  Mastercard  +  20 more", py + 80, font("regular", 16), Brand.GRAY_DARK)

    # Big stat
    text_center(draw, "20+", 940, font("extrabold", 90), Brand.PINK)
    text_center(draw, "Global Partners & Endorsements", 1040, font("medium", 22), Brand.TEXT)

    add_page_indicator(draw, 1)
    add_footer(canvas, dark=True)
    canvas.save(f"{OUT_DIR}/02_what_is_ucp.png", quality=95)
    print("  Slide 2: What is UCP")


# ==========================================
# SLIDE 3: HOW IT WORKS
# ==========================================
def slide_how():
    canvas = load_bg("flow_bg")

    # Slight darken for readability
    overlay = Image.new("RGBA", (W, H), (255, 255, 255, 140))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(canvas)
    add_top_bar(draw)

    text_center(draw, "How UCP Works", 55, font("extrabold", 50), Brand.TEXT)
    draw.rectangle([(W//2 - 40, 120), (W//2 + 40, 124)], fill=Brand.PINK)

    steps = [
        ("search", Brand.PINK, "01", "DISCOVER", "AI agents find your products across\nGoogle Search, Gemini, YouTube & Gmail"),
        ("cart", Brand.INFO, "02", "CART", "Universal Cart collects items across\nretailers and surfaces in one hub"),
        ("check", Brand.SUCCESS, "03", "CHECKOUT", "Secure payment with Google Pay.\nYou stay Merchant of Record."),
    ]

    step_h = 220
    step_gap = 35
    start_y = 170

    for i, (icon, color, num, title, desc) in enumerate(steps):
        sy = start_y + i * (step_h + step_gap)

        draw = glass_card(canvas, (50, sy, W-50, sy + step_h), radius=20, fill_alpha=210, fill_color=(255,255,255))

        # Number + icon
        draw_circle_icon(draw, 130, sy + step_h//2, 38, color, icon)

        # Number overlay
        nf = font("extrabold", 20)
        nb = draw.textbbox((0,0), num, font=nf)
        draw.text((130 - (nb[2]-nb[0])//2, sy + step_h//2 - (nb[3]-nb[1])//2 + 45), num, fill=color, font=nf)

        # Title
        draw.text((200, sy + 35), title, fill=color, font=font("extrabold", 34))

        # Description
        df = font("regular", 22)
        for j, dl in enumerate(desc.split("\n")):
            draw.text((200, sy + 90 + j * 32), dl, fill=Brand.GRAY_DARK, font=df)

        # Arrow
        if i < 2:
            ay = sy + step_h + 5
            ax = W // 2
            draw.polygon([(ax-12, ay), (ax+12, ay), (ax, ay+20)], fill=Brand.PINK)

    # Bottom callout
    by = 960
    draw = glass_card(canvas, (60, by, W-60, by + 70), radius=35, fill_alpha=220, fill_color=(255, 235, 242))
    text_center(draw, "Works across Search, Gemini, YouTube & Gmail", by + 22, font("semi", 20), Brand.PINK)

    add_page_indicator(draw, 2)
    add_footer(canvas)
    canvas.save(f"{OUT_DIR}/03_how_it_works.png", quality=95)
    print("  Slide 3: How it Works")


# ==========================================
# SLIDE 4: UNIVERSAL CART
# ==========================================
def slide_cart():
    canvas = load_bg("info_bg")
    draw = ImageDraw.Draw(canvas)
    add_top_bar(draw)

    text_center(draw, "Universal Cart", 50, font("extrabold", 50), Brand.TEXT)
    text_center(draw, "One cart across all of Google", 115, font("medium", 24), Brand.GRAY_DARK)
    draw.rectangle([(W//2 - 40, 158), (W//2 + 40, 162)], fill=Brand.PINK)

    features = [
        ("search", Brand.PINK, "Cross-Platform", "Shop across Google Search,\nGemini, YouTube & Gmail\nwith one unified cart"),
        ("check", Brand.SUCCESS, "Instant Checkout", "Pay with Google Pay in\njust a few taps. No\nredirects or extra forms"),
        ("shield", Brand.INFO, "Secure & Private", "Tokenized payments with\nfull transparency. You\ncontrol customer data"),
        ("globe", Brand.WARN, "Expanding Now", "US summer 2026.\nCanada, UK & Australia\ncoming next"),
    ]

    cw = (W - 50*3) // 2
    ch = 260

    for i, (icon, color, title, desc) in enumerate(features):
        col, row = i % 2, i // 2
        cx = 50 + col * (cw + 50)
        cy = 200 + row * (ch + 30)

        draw = glass_card(canvas, (cx, cy, cx+cw, cy+ch), radius=18, fill_alpha=230, fill_color=(255,255,255))

        # Top colored accent bar
        draw.rounded_rectangle((cx, cy, cx+cw, cy+5), radius=0, fill=color)

        # Icon
        draw_circle_icon(draw, cx + 50, cy + 55, 25, color, icon)

        # Title
        draw.text((cx + 25, cy + 95), title, fill=color, font=font("bold", 24))

        # Description
        df = font("regular", 18)
        for j, dl in enumerate(desc.split("\n")):
            draw.text((cx + 25, cy + 135 + j * 26), dl, fill=Brand.GRAY_DARK, font=df)

    # CTA bar
    cta_y = 780
    draw.rounded_rectangle((80, cta_y, W-80, cta_y + 65), radius=32, fill=Brand.PINK)
    text_center(draw, "Your customers are already shopping with AI", cta_y + 19, font("bold", 22), Brand.WHITE)

    # Stats
    stats = [("3+", "Google\nSurfaces"), ("20+", "Launch\nPartners"), ("4", "Countries\nExpanding")]
    sw = W // 3
    sy = 890

    for i, (num, label) in enumerate(stats):
        sx = i * sw + sw // 2
        nf = font("extrabold", 56)
        nb = draw.textbbox((0,0), num, font=nf)
        draw.text((sx - (nb[2]-nb[0])//2, sy), num, fill=Brand.PINK, font=nf)

        lf = font("regular", 15)
        for j, ll in enumerate(label.split("\n")):
            lb = draw.textbbox((0,0), ll, font=lf)
            draw.text((sx - (lb[2]-lb[0])//2, sy + 68 + j * 20), ll, fill=Brand.GRAY_DARK, font=lf)

    # Dividers
    for i in range(1, 3):
        dx = i * sw
        draw.line([(dx, sy + 10), (dx, sy + 95)], fill=(210, 210, 220), width=1)

    add_page_indicator(draw, 3)
    add_footer(canvas)
    canvas.save(f"{OUT_DIR}/04_universal_cart.png", quality=95)
    print("  Slide 4: Universal Cart")


# ==========================================
# SLIDE 5: WHY E-COMMERCE NEEDS UCP
# ==========================================
def slide_why():
    canvas = load_bg("dark_benefits_bg")

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 100))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(canvas)
    add_top_bar(draw)

    text_center_shadow(draw, "Why E-Commerce Stores", 50, font("extrabold", 42), Brand.WHITE)
    text_center_shadow(draw, "Need UCP", 105, font("extrabold", 42), Brand.PINK_LIGHT)
    draw.rectangle([(W//2 - 40, 168), (W//2 + 40, 172)], fill=Brand.PINK)

    benefits = [
        ("rocket", Brand.PINK, "Reach AI Shoppers", "Connect with high-intent buyers\ndirectly on Google's AI surfaces"),
        ("shield", Brand.SUCCESS, "Stay in Control", "You remain Merchant of Record\nwith full customer data ownership"),
        ("bolt", Brand.WARN, "Reduce Friction", "Fewer steps from discovery to\npurchase = less abandonment"),
        ("chart", Brand.INFO, "Data is King", "Structured product attributes\nare the new currency for AI"),
    ]

    cw = (W - 50*3) // 2
    ch = 230

    for i, (icon, color, title, desc) in enumerate(benefits):
        col, row = i % 2, i // 2
        cx = 50 + col * (cw + 50)
        cy = 210 + row * (ch + 30)

        draw = dark_glass_card(canvas, (cx, cy, cx+cw, cy+ch), radius=18, alpha=160)

        # Left accent line
        draw.rectangle([(cx, cy+15), (cx+4, cy+ch-15)], fill=color)

        # Icon
        draw_circle_icon(draw, cx + 50, cy + 55, 25, color, icon)

        # Title
        draw.text((cx + 25, cy + 95), title, fill=color, font=font("bold", 23))

        # Desc
        df = font("regular", 18)
        for j, dl in enumerate(desc.split("\n")):
            draw.text((cx + 25, cy + 135 + j * 26), dl, fill=(190, 190, 210), font=df)

    # Warning callout
    wy = 770
    draw = dark_glass_card(canvas, (50, wy, W-50, wy + 100), radius=16, alpha=180)
    draw.rounded_rectangle((50, wy, W-50, wy+100), radius=16, outline=Brand.PINK, width=2)

    text_center(draw, "THE CRITICAL TRADE-OFF", wy + 18, font("bold", 20), Brand.PINK)
    text_center(draw, "Participation increases sales volume, but", wy + 48, font("regular", 18), (190, 190, 210))
    text_center(draw, "non-participation risks invisibility in AI shopping", wy + 73, font("regular", 18), (190, 190, 210))

    # Quote
    text_center(draw, '"Keywords are dead;', 920, font("semi", 26), Brand.WHITE)
    text_center(draw, 'attributes are king."', 958, font("semi", 26), Brand.PINK_LIGHT)
    text_center(draw, "— Industry Analysis on UCP Impact", 1005, font("regular", 15), Brand.GRAY)

    add_page_indicator(draw, 4)
    add_footer(canvas)
    canvas.save(f"{OUT_DIR}/05_why_ecommerce.png", quality=95)
    print("  Slide 5: Why E-Commerce")


# ==========================================
# SLIDE 6: CTA
# ==========================================
def slide_cta():
    canvas = load_bg("cta_bg")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(0, 0), (W, 5)], fill=Brand.WHITE)

    # Logo
    logo = Image.open(LOGO_WHITE).convert("RGBA").resize((100, 100), Image.LANCZOS)
    a = logo.split()[-1].point(lambda p: min(p, 200))
    logo.putalpha(a)
    canvas.paste(logo, (W//2 - 50, 60), logo)

    text_center_shadow(draw, "Get UCP-Ready", 200, font("extrabold", 56), Brand.WHITE, (150, 40, 70))
    text_center_shadow(draw, "Now", 268, font("extrabold", 56), Brand.WHITE, (150, 40, 70))

    draw.rectangle([(W//2 - 50, 345), (W//2 + 50, 348)], fill=Brand.WHITE)

    # Checklist with glass cards
    items = [
        "Optimize your product feed data",
        "Set up Google Merchant Center",
        "Ensure complete product attributes",
        "Shift to structured data thinking",
        "Prepare for AI-driven commerce",
    ]

    iy_start = 390
    for i, item in enumerate(items):
        iy = iy_start + i * 72

        # Glass checkbox card
        draw = glass_card(canvas, (80, iy, W-80, iy+58), radius=14, fill_alpha=50, fill_color=(255,255,255))

        # Checkmark circle
        cr = 16
        ccx, ccy = 115, iy + 29
        draw.ellipse([(ccx-cr, ccy-cr), (ccx+cr, ccy+cr)], fill=Brand.WHITE)
        # Check
        draw.line([(ccx-6, ccy), (ccx-1, ccy+7), (ccx+8, ccy-6)], fill=Brand.PINK, width=3)

        # Text
        draw.text((150, iy + 14), item, fill=Brand.WHITE, font=font("semi", 24))

    # Divider
    dy = iy_start + 5 * 72 + 20
    draw.rectangle([(120, dy), (W-120, dy+1)], fill=(255, 255, 255, 100))

    # URL
    text_center(draw, "START HERE", dy + 25, font("medium", 18), (255, 200, 210))
    text_center_shadow(draw, "developers.google.com/merchant/ucp", dy + 55, font("bold", 20), Brand.WHITE, (150, 40, 70))

    # Save button
    sy = dy + 110
    bw = 380
    draw.rounded_rectangle((W//2 - bw//2, sy, W//2 + bw//2, sy+55), radius=28, fill=Brand.WHITE)
    text_center(draw, "Save this post for later!", sy + 14, font("bold", 22), Brand.PINK)

    add_page_indicator(draw, 5)

    # Footer on pink
    fy = H - 60
    draw.rectangle([(0, fy), (W, H)], fill=(180, 50, 80))
    draw.rectangle([(0, fy), (W, fy + 2)], fill=Brand.WHITE)
    logo_f = Image.open(LOGO_WHITE).convert("RGBA").resize((34, 34), Image.LANCZOS)
    af = logo_f.split()[-1].point(lambda p: min(p, 200))
    logo_f.putalpha(af)
    lx = W//2 - 50
    canvas.paste(logo_f, (lx, fy + 13), logo_f)
    draw = ImageDraw.Draw(canvas)
    draw.text((lx + 40, fy + 22), "SALECRAFT", fill=(255, 200, 210), font=font("medium", 13))

    canvas.save(f"{OUT_DIR}/06_cta.png", quality=95)
    print("  Slide 6: CTA")


# ==========================================
# GENERATE ALL
# ==========================================
if __name__ == "__main__":
    print("Generating v2 carousel with design system...\n")
    slide_cover()
    slide_what()
    slide_how()
    slide_cart()
    slide_why()
    slide_cta()
    print(f"\nAll 6 slides saved to {OUT_DIR}/")
