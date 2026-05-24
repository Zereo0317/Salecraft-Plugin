#!/usr/bin/env python3
"""
Optimized Video Generation Prompts for Bali Street Dance Video

Target: 6 people from Bali group photo performing street dance
Format: 9:16 vertical (1080x1920 or higher)
Duration: 10-15 seconds
Language: Traditional Chinese (Taiwan) for dialogue
Audio: Background music + character dialogue

Photo Description (reference):
- Front row left: Young man with curly hair, black leather jacket, white tee, earring
- Front row center: Young man in dark navy open-collar shirt (selfie position)
- Back row left: Blonde young man in light blue shirt
- Back row center-left: Man in white button-up shirt
- Back row center-right: Man with glasses in pink/salmon shirt
- Back row right: Older man (most senior)
- Setting: Modern lab/workspace with Bali sunset + temple visible through windows
"""


# ============================================================
# KLING 3.0 OPTIMIZED PROMPT
# ============================================================
# Kling best practices:
# - Think like a director: write scene directions
# - Prioritize physics over appearance
# - Use cinematic language (tracking shot, dolly, crane)
# - Name real light sources
# - Anchor limbs to actions
# - cfg_scale 0.5 recommended
# - Describe motion explicitly

KLING_PROMPT = """Low-angle tracking shot slowly orbiting clockwise. 9:16 vertical frame. Interior of a modern beachside lab in Bali, golden sunset streaming through floor-to-ceiling windows, silhouette of a traditional Balinese temple visible outside.

SHOT 1 (0-3s): Six friends stand together in the lab. A funky hip-hop beat drops. The young man in the dark navy open-collar shirt (front center) snaps his head to the beat, then initiates with a sharp chest pop followed by a fluid body wave — the motion ripples from his chest down through his torso to his hips. His feet pivot on the ball of the foot, weight shifting naturally. Arms swing out with controlled power.

SHOT 2 (3-6s): The curly-haired young man in the black leather jacket over white tee explodes with popping — each joint locks and releases in rapid succession. His right arm extends into a precise tutting formation, fingers spread at exact 90-degree angles. His left arm mirrors with a slight delay, creating a wave effect. His earring swings with the motion. Meanwhile, the blonde young man in the blue shirt behind him hits a locking sequence — sharp wrist snaps, pointing freeze, then a sudden full-body freeze in an exaggerated pose.

SHOT 3 (6-10s): All six break into synchronized choreography. The man in the white button-up shirt does crisp robot-style isolations — his head moves independently from his torso, which moves independently from his hips. The man with glasses in the pink shirt performs a stunning wave that travels from his right fingertip, across his shoulders, and out through his left fingertip. The older man adds solid rhythmic footwork — a clean two-step with confident head nods and shoulder rolls, his experience showing in the precision of his timing.

SHOT 4 (10-13s): Camera drops to low angle. Each dancer hits their signature move in rapid succession — freeze frame moments punctuated by explosive transitions. The navy-shirt guy does a powerful krump-style chest pump. The leather-jacket guy spins with a smooth pirouette. Energy peaks with all six moving in perfect sync for two beats.

SHOT 5 (13-15s): They all freeze in a dramatic group pose — arms extended at different angles, weight on different legs, creating a dynamic human sculpture. After one beat of stillness, they break into laughter. The Bali sunset blazes golden behind them through the windows. Camera slowly pulls back.

Style: Professional street dance music video. Warm golden-hour rim lighting. Skin pores and fabric textures visible. Film grain. Each person maintains their exact clothing and distinct facial features from the original photo. High-energy hip-hop choreography with clean technique.

[前排深色襯衫男生，年輕有活力的清亮男聲]: "欸！準備好了嗎？三、二、一，開始！"
[皮衣捲髮男生，興奮高亢的語氣]: "這個節奏也太猛了吧！跟上跟上！"
[粉色衣服戴眼鏡男生，驚喜開心地笑]: "哈哈哈！我居然也可以跳成這樣！太扯了！"
[金髮藍衣男生，用力喊]: "再來一次！這次更猛的！"
[白襯衫男生，沉穩但興奮]: "穩住穩住，節奏抓好！"
[年長男生，笑著說]: "年輕人，讓你們看看什麼叫薑是老的辣！"
"""

KLING_NEGATIVE_PROMPT = (
    "blurry, distorted faces, extra limbs, extra fingers, deformed hands, "
    "missing fingers, low quality, watermark, text overlay, static image, "
    "frozen pose, cartoonish, 3D render, smooth plastic skin, floating limbs, "
    "sliding feet, morphing text, unnatural smile, dead eyes, "
    "inconsistent clothing, wrong number of people"
)


# ============================================================
# SEEDANCE 2.0 OPTIMIZED PROMPT
# ============================================================
# Seedance best practices:
# - Structure: Action + Scene + Style + Camera
# - Support multi-reference images
# - Camera movements: dolly_in, pan_left, orbit_left, crane_up, zoom_in
# - Max duration: 15 seconds at 1080p
# - Supports zh-TW text naturally

SEEDANCE_PROMPT = """電影級垂直影片 (9:16)。峇厘島海邊實驗室內，六位好友從靜態合照突然爆發成一場專業街舞表演。

場景設定：現代化實驗室空間，落地玻璃窗外是峇厘島金色夕陽與傳統廟宇剪影。溫暖的金色光線從窗戶灑入，在每個人身上形成漂亮的輪廓光。

【開場 — 0至3秒】
鏡頭從低角度緩慢推進。六個人站在實驗室中央，面對鏡頭。前排穿深色海軍藍開領襯衫的年輕男生突然隨著節拍點頭，然後做出一個從胸口開始的Body Pop，波浪般的動作從胸口延伸到腹部再到臀部。他的腳掌以前腳掌為軸心旋轉，重心自然轉移。

【爆發 — 3至7秒】
穿黑色皮衣搭白色T恤的捲髮男生接著爆發出精準的Popping——每個關節快速鎖定和釋放。右手臂伸展成幾何Tutting造型，手指以精確的90度角展開。耳環隨動作擺盪。與此同時，後排穿淺藍色襯衫的金髮男生做出Locking動作——俐落的手腕翻轉、指向定格，然後突然全身凍結在一個誇張的姿勢。

【齊舞高潮 — 7至11秒】
六人同時進入齊舞段落。穿白色襯衫的男生做出乾淨的機器人式分離動作——頭部、軀幹、臀部各自獨立移動。戴眼鏡穿粉色衣服的男生表演一個驚豔的Wave——波浪從右手指尖出發，穿過雙肩，從左手指尖流出。年紀最長的男生用穩健紮實的Two-Step加入，自信地點頭和肩膀搖擺。鏡頭順時針環繞拍攝。

【收尾 — 11至15秒】
每個人輪流做出各自的招牌動作——快速的定格瞬間穿插爆發性的轉場。最後六人同時定格在一個戲劇性的群體姿勢——手臂以不同角度伸展，重心落在不同的腿上。靜止一拍後，所有人爆發出笑聲。峇厘島夕陽在身後閃耀金光。鏡頭緩慢後拉。

影片風格：專業街舞MV質感、電影級色彩調校、溫暖金色調、高能量嘻哈編舞、每個人保持原始照片中的外觀與服裝。24fps，流暢運鏡。

人物對話（繁體中文-台灣口語）:
前排深色襯衫男生說：「欸！準備好了嗎？三、二、一，開始！」
皮衣捲髮男生興奮地喊：「這個節奏也太猛了吧！跟上跟上！」
戴眼鏡粉色衣服男生驚喜地笑：「哈哈哈！我居然也可以跳成這樣！太扯了！」
金髮藍衣男生大喊：「再來一次！這次更猛！」
白襯衫男生沉穩地說：「穩住穩住，節奏抓好！」
年長男生笑著說：「年輕人，讓你們看看什麼叫薑是老的辣！」
"""

SEEDANCE_NEGATIVE = (
    "模糊, 變形的臉, 多餘的手臂, 畸形的手, 低畫質, 浮水印, "
    "靜止不動, 卡通風格, 塑膠感皮膚, 漂浮的四肢, 滑動的腳"
)


# ============================================================
# GENERATION PARAMETERS
# ============================================================

KLING_PARAMS = {
    "model_name": "kling-v3",
    "mode": "pro",          # 1080x1920 for 9:16
    "duration": "10",        # 10 seconds (can go up to 15)
    "aspect_ratio": "9:16",
    "cfg_scale": 0.5,        # recommended default
    "generate_audio": True,
    "prompt": KLING_PROMPT,
    "negative_prompt": KLING_NEGATIVE_PROMPT,
}

SEEDANCE_PARAMS = {
    "model": "dreamina-seedance-2-0-260128",
    "ratio": "9:16",
    "resolution": "1080p",
    "duration": 10,           # 10 seconds (can go up to 15)
    "generate_audio": True,
    "watermark": False,
    "return_last_frame": True,
    "prompt": SEEDANCE_PROMPT,
}
