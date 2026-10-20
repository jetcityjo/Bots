import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Ryder banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

GOLD, IVORY, INK, MUTED, EM = "#D6BC86", "#F3EEE2", "#1E2622", "#7E8279", "#1E5A4A"

def starter(text):
    return f'''
                        <div style="background: #FAF7EF; border-left: 3px solid {EM}; padding: 8px 12px; border-radius: 4px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def ryder(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {EM};">Ryder:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #E8E1CF; border: 1px solid #CFC3A3; border-radius: 6px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.1em; color: {EM}; margin-right: 6px;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-left: 6px;">· {esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #CFC3A3; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def ribbon(c, word, meaning):
    return f'<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px; color: {INK};"><span style="display: inline-block; width: 26px; height: 8px; border-radius: 2px; background: {c}; border: 1px solid rgba(0,0,0,0.2);"></span><strong style="min-width: 56px;">{word}</strong><span>{esc(meaning)}</span></div>'

def room(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F0EADC; border: 1px dashed #BDAF8A; border-radius: 6px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{ryder(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = ryder("I already know your name. Tell me your favorite vintage, and I'll make sure your glass is never empty.") + \
     starter("*I hand him my coat.* \"My favorite vintage? Guess first.\"")
s2 = ribbon("#5E9A6B", "Green", "Open to invitations.") + ribbon("#D2A84A", "Yellow", "Watching for now. Ask before you come close.") + \
     ribbon("#B5483E", "Red", "Not tonight.") + \
     '<div style="margin-top: 10px;">' + ryder("You can change it whenever you like. Nobody here takes it personally. Least of all me.") + '</div>' + \
     starter("*I pick a ribbon from the silver bowl and hold out my wrist.* \"Tie it for me?\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">He offers you the house. Choose where the night starts.</div>' + \
     room("The Bar", "Stay here with me. We'll watch the room together, and I'll tell you everyone's secrets. Well. Some of them.",
          "*I take the stool next to him at the bar.* \"Tell me about the couple on the chaise.\"") + \
     room("The Lounge", "Candles, the good chaise, and a few people who've been hoping someone new would wander over. Go on. I'll be watching.",
          "*I walk down into the sunken lounge, ribbon on my wrist.*") + \
     room("The Back Room", "Rope on the wall. Quieter in there. I only go in with people I'm sure of.",
          "\"Show me the back room, Ryder.\"")

steps = step("I", "Arrival", "he takes your coat", s1, opn=True) + \
        step("II", "The Ribbons", "a house tradition", s2) + \
        step("III", "The House", "where the night starts", s3)

TAGS = ["Orgy", "The Host", "Voyeur", "Kinktober Day 2", "Pick a Ribbon"]
tagpills = "\n".join(f'            <div style="background-color:#17241F; color:{GOLD}; border: 1px solid #2F4A40; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ryder James - Kinktober Day 2</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0C100E; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #151B18; border: 1px solid #26332D; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E0E2DA; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #26332D; padding-bottom:15px; margin-bottom:25px; color: #F3EEE2; letter-spacing: 0.5px;">
            You're on the List. Come In.
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #959A8E; font-family: Georgia, serif;">
                “Most people need three drinks to relax. Let's see how many you need.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Ryder James" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #26332D; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#111613; color: #A9AEA3; padding:20px; flex: 1; min-width: 250px; border:1px solid #26332D; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Candlelight, the right wine at the right temperature, and a room full of strangers who'll leave as something else. Ryder James hosts the party you only hear about secondhand. He remembers everyone's favorite vintage. He watches everything. He joins in only when he's sure.</span>
            </div>
            <div style="background-color:#111613; color: #A9AEA3; padding:20px; flex: 1; min-width: 250px; border:1px solid #26332D; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Ryder James x Any user<br>
                    Kinktober Day 2: Orgy<br>
                    Pick a ribbon, copy a starter into chat.<br>
                    TW: Group sex, voyeurism, rope<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- INVITATION -->
        <div style="margin-top: 35px; background-color: {IVORY}; border: 1px solid #CFC3A3; border-top: 6px solid {EM}; border-radius: 10px; padding: 22px 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 8px;">OCT 02 · ORGY</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-style: italic; font-size: 30px; color: {INK}; letter-spacing: 1px;">The Guest List</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 22px;">Saturday. Late. Dress however you'll be most comfortable undressing.</div>
{steps}
            <div style="margin-top: 18px; border-top: 1px solid #CFC3A3; padding-top: 14px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">AFTER THE LAST GUEST</span>
                The candles burn down. The music stops. Ryder pours one scotch and sits in the quiet. Sometimes he pours two.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Stay for one more? ~R</div>
        </div>

        <details style="margin-top: 30px; background: #18201C; padding: 12px 20px; border-radius: 8px; border: 1px solid #26332D; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #2F3D36; padding-top: 12px; color: #9DA297;">
                Ryder hosts adult group gatherings. Expect group sex, voyeurism, exhibitionism, and rope. All characters are adults. Every pairing is consensual, ribbons and colors are honored by every guest, and watching is always allowed.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Ryder James (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
