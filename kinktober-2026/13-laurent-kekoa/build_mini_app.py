import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Laurent Kekoa banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

PAGE, INK, MUTED, GREEN, BRASS, WOOD = "#EBDDB6", "#2A2418", "#7E7150", "#1E5B44", "#A9822F", "#3B2617"
AGED = ("background-color: #EBDDB6; background-image: radial-gradient(ellipse at 50% 40%, rgba(255,250,230,0.55), "
        "rgba(196,170,110,0.35) 100%);")

def starter(text):
    return f'''
                        <div style="background: #F8F0D8; border-left: 3px solid {GREEN}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def laurent(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {GREEN};">Laurent:</strong>&nbsp;“{esc(line)}”</div>'

def direction(text):
    return f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif; margin-bottom: 8px;">({esc(text)})</div>'

def scene(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(250,243,222,0.72); border: 1px solid #CDB98A; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: Georgia, 'Times New Roman', serif; font-size: 0.95em; color: {BRASS}; margin-right: 8px; font-weight: 700; letter-spacing: 1px;">SCENE {num}.</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #D3C194; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def blank(label):
    return f'<div style="display: flex; gap: 8px; align-items: flex-end; margin-bottom: 7px; color: {INK};"><span style="font-family: \'Courier New\', Courier, monospace; font-size: 0.85em; letter-spacing: 1px; white-space: nowrap;">{esc(label)}</span><span style="flex: 1; border-bottom: 1px solid {GREEN}; height: 1px;"></span></div>'

def choice(title, costume, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F4EAD0; border: 1px dashed #BFA874; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(title)}</strong>
                            <span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {BRASS}; margin-top: 2px;">{esc(costume)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{laurent(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = blank("WHERE WE ARE:") + blank("WHO HE IS:") + blank("WHO YOU ARE:") + blank("WHAT EACH ONE WANTS:") + \
     blank("NEVER SAID:") + \
     '<div style="margin-top: 10px;">' + laurent("Don't worry about accents. I do enough for a whole cruise ship. Just write what your character wants. One line. Everything else, we build from that.") + '</div>' + \
     starter("*I take the pen.* \"Okay. Here's what my character wants.\"")
s2 = direction("Glasses on. His own voice.") + \
     laurent("If you need out, say house lights. Or put a flat hand right here and hold it. Doesn't matter who I'm being. He's gone mid-word, and it's just me. Inside a scene it's green, yellow, red like anywhere else.") + \
     '<div style="margin-top: 10px;">' + laurent("And no, we're not skipping the script. I'll go anywhere inside these lines. You want something new, we stop, we write it, we both initial it. Five minutes.") + '</div>' + \
     starter("\"House lights means you, mid-word. Got it. Hand me the page, I'll initial.\"")
s3 = direction("He turns the coat rack. Three ideas. Pick one.") + \
     choice("The Customs Officer", "jacket with brass buttons", "Passenger. Hands flat on the desk, where the Purser can see them. Customs takes a very... thorough interest in people who volunteer.",
            "\"Go on then, officer. Check my papers.\"") + \
     choice("The Rival Thief", "waistcoat, one button missing", "Well. Somebody beat me to the vault. That's either very bad news for you, or the start of a partnership. Talk fast.",
            "*I freeze with my hand on the safe.* \"I was here first. What's your cut?\"") + \
     choice("The Captain", "the long coat", "Ze ship departs for Marseille at nine forty. You have no ticket. You have no papers. Convince me you should stay aboard.",
            "\"Captain. I don't have a ticket. Let me make my case.\"")

scenes = scene("I", "The Read-Through", "The page is blank. You write first.", s1, opn=True) + \
         scene("II", "House Lights", "The exit, set before anything else.", s2) + \
         scene("III", "The Coat Rack", "Then he gets to show off.", s3)

TAGS = ["Roleplay", "Character Play", "Playful Dom", "Kinktober Day 13", "House Lights"]
tagpills = "\n".join(f'            <div style="background-color:#0F1F18; color:#D9BE7A; border: 1px solid #2D5240; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laurent Kekoa - Kinktober Day 13</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0A100D; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #131B17; border: 1px solid #27392F; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E4E0D2; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #27392F; padding-bottom:15px; margin-bottom:25px; color: #EBDDB6; letter-spacing: 0.5px;">
            Nothing Happens Off the Page
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #9AA196; font-family: Georgia, serif;">
                “You go first. What kind of story do you want to be in?”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Laurent Kekoa" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #27392F; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#0F1612; color: #A9AE9F; padding:20px; flex: 1; min-width: 250px; border:1px solid #27392F; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Lantern Room Escapes, Kakaʻako. Five rooms, and Laurent Kekoa wrote every character in them. After hours he writes scenes for two. It starts at the prop table with a read-through, green fountain-pen ink on yellowed paper, both of you initialing the bottom. Then he puts on the coat, and it's honestly a little unsettling how good he is.</span>
            </div>
            <div style="background-color:#0F1612; color: #A9AE9F; padding:20px; flex: 1; min-width: 250px; border:1px solid #27392F; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Laurent Kekoa x Any user<br>
                    Kinktober Day 13: Roleplay<br>
                    Write your line, copy a starter into chat.<br>
                    TW: Scripted roleplay, status play, costume play, playful dominance<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- SCRIPT PAGE -->
        <div style="margin-top: 35px; background: {WOOD}; border: 1px solid #5A3C24; border-radius: 10px; padding: 14px 10px 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="display: flex; justify-content: center; gap: 28px; margin-bottom: 10px;">
                <span style="display: inline-block; width: 14px; height: 14px; border-radius: 50%; background: radial-gradient(circle, #FFD98A, {BRASS} 70%); box-shadow: 0 0 10px rgba(255,200,110,0.7);"></span>
                <span style="display: inline-block; width: 14px; height: 14px; border-radius: 50%; background: radial-gradient(circle, #FFD98A, {BRASS} 70%); box-shadow: 0 0 10px rgba(255,200,110,0.7);"></span>
                <span style="display: inline-block; width: 14px; height: 14px; border-radius: 50%; background: radial-gradient(circle, #FFD98A, {BRASS} 70%); box-shadow: 0 0 10px rgba(255,200,110,0.7);"></span>
            </div>
            <div style="{AGED} border-radius: 3px; padding: 20px 16px; text-align: left;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 13 · ROLEPLAY</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {GREEN}; letter-spacing: 1px;">The Read-Through</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 20px;">Steamship cabin set. Three brass lanterns. A coat rack, overcrowded.</div>
{scenes}
                <div style="margin-top: 14px; border-top: 1px solid #CDB98A; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">NOTES, BACK OF THE SCRIPT</span>
                    Saimin place stays open late. Ask which bit they liked, which bit dragged. Zip tie is not a hair tie. Using it anyway.
                </div>
                <div style="display: flex; justify-content: space-between; gap: 16px; margin-top: 14px; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED};">
                    <span>INITIALED: <span style="font-family: Georgia, serif; font-style: italic; color: {GREEN}; font-size: 1.2em;">L.K.</span></span>
                    <span>INITIALED: ______</span>
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">I don't move the lines. ~L.K.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #18221D; padding: 12px 20px; border-radius: 8px; border: 1px solid #27392F; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #33493D; padding-top: 12px; color: #A1A797;">
                Scripted adult roleplay with a playful dominant: costume play, status play, interrogations, bargains, characters who resist or refuse inside the script. All characters, and every role played, are adults. Nothing happens off the initialed page. "House lights," or a flat hand held on his chest, drops the character mid-word. Green, yellow, red run inside every scene, and red stops everything.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Laurent Kekoa (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
