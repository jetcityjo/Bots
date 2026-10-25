import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Bowie Jackson banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

ENAMEL, NOTE, MARKER, MUTED, JADE, MAT, TAPE = "#E4E7E3", "#F7E37A", "#1F1E1C", "#77796F", "#2F7D5F", "#2C4A7C", "#FAFAF7"
HAND = "'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif"

def starter(text):
    return f'''
                        <div style="background: {TAPE}; border-left: 3px solid {JADE}; padding: 8px 12px; border-radius: 3px; color: {MARKER}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def bowie(line):
    return f'<div style="color: {MARKER}; line-height: 1.6;"><strong style="color: {MAT};">Bowie:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False, rot="0deg"):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 14px; background: {NOTE}; border-radius: 2px; padding: 12px 14px; box-shadow: 0 4px 10px rgba(0,0,0,0.18); transform: rotate({rot});">
                <summary style="cursor: pointer; outline: none; color: {MARKER};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {MAT}; margin-right: 8px; font-weight: 700;">ROUND {num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: #6E6640; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #D9C35A; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def item(mark, color, text):
    return f'<div style="display: flex; gap: 10px; align-items: flex-start; margin-bottom: 5px; color: {MARKER}; line-height: 1.45; font-family: {HAND}; font-weight: 600;"><span style="display: inline-block; min-width: 18px; font-weight: 700; color: {color};">{mark}</span><span>{esc(text)}</span></div>'

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FBF1B4; border: 1px dashed #CDB54A; border-radius: 2px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {MARKER}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{bowie(line)}{starter(start)}
                        </div>
                    </details>'''

YES, NO = "#2F7D5F", "#B3261E"

s1 = item("2x", MAT, "Two taps, anywhere, and he lets go.") + \
     '<div style="margin-top: 10px;">' + bowie("Ten years on the mat. And don't say sorry for tapping. I tapped in front of four thousand people once and my Paw Paw still brings it up.") + '</div>' + \
     starter("*I reach out and tap his taped forearm twice, hard.* \"Like that?\"")

s2 = item("✓", YES, "Hair") + item("✓", YES, "Pinning") + item("✓", YES, "Wrestling") + item("✓", YES, "Trash talk") + \
     item("✓", YES, "Bruises: hips, thighs, ass. Upper arms only under a T-shirt. Nothing past purple.") + \
     item("✗", NO, "Face, neck, strikes") + \
     '<div style="margin-top: 10px;">' + bowie("Same as Wednesday. Trash talk's on there, which, good, I was hoping.") + '</div>' + \
     starter("\"Read it back one more time. Slow. I want to hear you say the part about hair.\"")

s3 = f'<div style="color: #6E6640; font-style: italic; font-family: Georgia, serif;">Couch shoved back. Mat out. He\'s at the edge of it, weight on the balls of his feet.</div>' + \
     choice("Step on the mat", "Okay. Base, frame, all that. You push, I push back, and mostly I take the position.",
            "*I step onto the mat barefoot and square up.* \"Come get your position.\"") + \
     choice("Change the note", "Sure. Tell me and I'll write it. My handwriting is hella bad, so say it slow.",
            "*I take the marker off the fridge.* \"One change before we start.\"") + \
     choice("Trash talk first", "That's it? That's your stance? My Paw Paw stands better than that, and she's eighty-one. Try again.",
            "\"Big talk for a guy with tape on both wrists. Show me.\"")

steps = step("1", "Show Me Your Tap", "Before anything else.", s1, opn=True, rot="-0.6deg") + \
        step("2", "The Note", "On the fridge, in bad handwriting.", s2, rot="0.5deg") + \
        step("3", "The Mat", "Living room, Temescal. Space heater ticking.", s3, rot="-0.3deg")

TAGS = ["Rough Sex", "Pinning", "Tap Out", "Kinktober Day 16", "Bruise Report"]
tagpills = "\n".join(f'            <div style="background-color:#142019; color:#8ED1AE; border: 1px solid #2B4A3A; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

def magnet(color, left):
    return f'<span style="display: inline-block; width: 22px; height: 22px; border-radius: 50%; background: {color}; box-shadow: inset -3px -3px 0 rgba(0,0,0,0.2), 0 2px 3px rgba(0,0,0,0.3); margin: 0 {left};"></span>'

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bowie Jackson - Kinktober Day 16</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0E1012; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #16191C; border: 1px solid #2A3036; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E1E3E2; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2A3036; padding-bottom:15px; margin-bottom:25px; color: #F4F5F2; letter-spacing: 0.5px;">
            Two Taps and I Let Go
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #959A9C; font-family: Georgia, serif;">
                “Okay. Before anything else. Show me your tap.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Bowie Jackson" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2A3036; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#111416; color: #A6ABAD; padding:20px; flex: 1; min-width: 250px; border:1px solid #2A3036; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Bowie Jackson went eleven and four, held a small-promotion lightweight belt, and retired at twenty-eight before a doctor could make him. Now he coaches beginners at Brickyard MMA in West Oakland and works a door on Telegraph, which is mostly talking. You watched him talk two drunk guys out of a fight. Three weeks of texting, dim sum on Wednesday, and tonight the mat is out in his Temescal living room.</span>
            </div>
            <div style="background-color:#111416; color: #A6ABAD; padding:20px; flex: 1; min-width: 250px; border:1px solid #2A3036; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Bowie Jackson x Any user<br>
                    Kinktober Day 16: Rough Sex<br>
                    Read the fridge note, copy a starter into chat.<br>
                    TW: Rough sex, pinning, hair pulling, wrestling, negotiated bruising<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- FRIDGE DOOR -->
        <div style="margin-top: 35px; background: linear-gradient(90deg, #D9DDD8, {ENAMEL} 18%, #EEF0EC 60%, #D3D7D2); border: 1px solid #B9BEB8; border-radius: 14px; padding: 18px 14px 20px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5); position: relative;">
            <div style="position: absolute; right: 10px; top: 40px; width: 8px; height: 120px; background: linear-gradient(#C3C8C2, #9EA49D); border-radius: 4px;"></div>
            <div style="text-align: center; margin-bottom: 10px;">{magnet("#C0392B", "6px")}{magnet(JADE, "6px")}{magnet(MAT, "6px")}</div>
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 16 · ROUGH SEX · SATURDAY, NIGHT OFF</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {MARKER}; letter-spacing: 1px;">The Fridge Note</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 14px 18px;">Negotiated like fight camp. Read back before anything starts.</div>
{steps}
            <div style="margin: 16px 6px 0; background: {TAPE}; border: 1px solid #CFD3CE; border-radius: 3px; padding: 10px 12px; color: {MARKER}; line-height: 1.6; font-size: 0.9em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">FREEZER · FOR AFTER</span>
                ICE 1 · ICE 2 · ICE 3 · ICE 4. Arnica on the nightstand. A quart of his mom's jook. Bruise report by text tomorrow, with a picture.
            </div>
            <div style="text-align: right; margin: 10px 6px 0; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Sik faan. Then text me a picture. ~B.J.</div>
        </div>

        <details style="margin-top: 30px; background: #1A1E21; padding: 12px 20px; border-radius: 8px; border: 1px solid #2A3036; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #343B41; padding-top: 12px; color: #9DA2A4;">
                Consensual rough sex. Expect grip, pinning, wrestling, hair pulling, trash talk, bruises, and a lot of aftercare. No chokes, no strikes. All characters are adults. Two taps or "red" and he lets go.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Bowie Jackson (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
