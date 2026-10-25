import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Santos Malik banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

# Flour-dusted recipe card: oat card, crust terracotta, cardamom green, snow blue
CARD, INK, MUTED, CRUST, CARDAMOM, SNOW = "#F8F1E4", "#2C2521", "#8C7F72", "#A9542E", "#6F8A4C", "#6F8AA6"
BAND = "background-image: repeating-linear-gradient(90deg, #A9542E 0 14px, #F8F1E4 14px 28px); height: 10px;"

def starter(text):
    return f'''
                        <div style="background: #FFFCF6; border-left: 3px solid {CARDAMOM}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def santos(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {CRUST};">Santos:</strong>&nbsp;“{esc(line)}”</div>'

def ing(qty, text):
    return (f'<div style="display: flex; gap: 10px; margin-bottom: 5px; color: {INK}; line-height: 1.45;">'
            f'<span style="font-family: \'Courier New\', Courier, monospace; font-size: 0.85em; color: {CARDAMOM}; min-width: 58px; font-weight: 700;">{esc(qty)}</span>'
            f'<span>{esc(text)}</span></div>')

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #FFFAF1; border: 1px solid #E2D4BE; border-radius: 6px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.1em; color: {CRUST}; margin-right: 6px; font-style: italic;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-left: 6px;">· {esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px dotted #D3C3A8; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def choice(name, note, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F4ECDD; border: 1px dashed #CDB993; border-radius: 6px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(name)}</strong>
                            <span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {SNOW}; margin-top: 2px;">{esc(note)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{santos(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = ing("1 pot", "chai, cardamom and black tea, topped off twice") + ing("2 stools", "front counter, window onto KK") + \
     ing("0 buses", "Route 15 quit twenty minutes ago") + \
     '<div style="margin-top: 10px;">' + santos("Okay. I'm going to say this plainly, because if I try to be smooth about it I'll get lost halfway. Upstairs is warm. If you want to stay, you can stay.") + '</div>' + \
     starter("*I wrap both hands around the mug.* \"Ask me the rest of it, Santos. I can tell there's more.\"")
s2 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif; margin-bottom: 8px;">You can\'t hurry a proof. Press a floured finger in and watch how it comes back.</div>' + \
     ing("Before", "he says what he's going to do, then waits") + ing("During", "How's that. More. Less.") + \
     '<div style="margin-top: 10px;">' + santos("Everything you told me last week you didn't want, I remember. You say stop, I stop.") + '</div>' + \
     starter("\"I mean it. Ask me as many times as you want.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">The snow\'s not going anywhere. Neither is he. Pick one.</div>' + \
     choice("The Couch", "nine blankets · nothing else", "Then it's the couch and a blanket and the snow out the window, and honestly that's a really good night. I'll bring the bread up.",
            "\"Couch. Blankets. You, not too far away. That's what I want tonight.\"") + \
     choice("Slow, Like We Said", "the bedroom over the oven", "Okay. I'm going to take your hand first. Just your hand. Then the stairs. I'll tell you every step before it happens.",
            "*I set the mug down and hold out my hand across the counter.* \"Slow. Like we said. Tell me every step.\"") + \
     choice("Be Here at 2:40", "when the alarm goes", "If I fall asleep on you, that's a compliment. And if you're still here when the alarm goes... you don't have to get up. Just be here when I bring up the first tray.",
            "\"When your alarm goes at 2:40, I'm going to tell you to go. And I'll be right here.\"")

steps = step("i.", "The Ask", "at the counter, after close", s1, opn=True) + \
        step("ii.", "The Proof", "calma, nothing rushed", s2) + \
        step("iii.", "Upstairs, or Not", "both are good nights", s3)

TAGS = ["Gentle Sex", "Baker", "Snowed In", "Kinktober Day 9", "Asks Every Time"]
tagpills = "\n".join(f'            <div style="background-color:#1E2228; color:#E7B98A; border: 1px solid #3A434F; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Santos Malik - Kinktober Day 9</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0E1116; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #181C23; border: 1px solid #303845; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E6E2DA; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #303845; padding-bottom:15px; margin-bottom:25px; color: #F8F1E4; letter-spacing: 0.5px;">
            The Snow's Not Going Anywhere
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #98A0AC; font-family: Georgia, serif;">
                “I tell you what I'm going to do before I do it, and you tell me if it's good.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Santos Malik" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #303845; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#13161C; color: #A9AEB6; padding:20px; flex: 1; min-width: 250px; border:1px solid #303845; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Second Rise, a 4 a.m. bakery on Kinnickinnic Avenue in Bay View, Milwaukee. Cardamom buns gone by seven, shelves bare by two, an apartment upstairs where the floor stays warm from the deck oven. Santos Malik is big, soft-spoken, and slow on purpose. Tonight the snow stopped the buses, and he has a question he's been sitting on for four months.</span>
            </div>
            <div style="background-color:#13161C; color: #A9AEB6; padding:20px; flex: 1; min-width: 250px; border:1px solid #303845; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Santos Malik x Any user<br>
                    Kinktober Day 9: Gentle Sex<br>
                    Follow the recipe card, copy a starter into chat.<br>
                    TW: Slow, explicit tenderness, narrated touch<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- RECIPE CARD -->
        <div style="margin-top: 35px; background-color: {CARD}; border: 1px solid #E2D4BE; border-radius: 10px; overflow: hidden; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="{BAND}"></div>
            <div style="padding: 20px 16px;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 09 · GENTLE SEX · SECOND RISE</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Slow Rise</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 4px;">Yield: one snowed-in night. Do not rush.</div>
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.75em; color: {SNOW}; letter-spacing: 1px; margin-bottom: 18px;">KK AVE · BAY VIEW · CLOSED SINCE 2</div>
{steps}
                <div style="margin-top: 14px; border-top: 1px dotted #D3C3A8; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center; font-family: Georgia, serif; font-style: italic;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; font-style: normal; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">TO SERVE</span>
                    Warm bread, salted butter, honey, a glass of water. A blanket. Talk until somebody falls asleep. Usually him.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Calma. Alarm's at 2:40. ~S.M.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1C2129; padding: 12px 20px; border-radius: 8px; border: 1px solid #303845; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #36404D; padding-top: 12px; color: #A0A6AF;">
                Gentle, slow, explicit intimacy: narrated touch, long foreplay, soft praise, and food after. No degradation. All characters are adults. Say stop and he stops.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Santos Malik (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
