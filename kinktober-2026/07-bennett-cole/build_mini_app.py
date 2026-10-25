import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Bennett banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

LABEL, INK, MUTED, BLUE, AMBER, LEAF = "#F2E9D5", "#24201B", "#857A69", "#2D4E7A", "#B97A2E", "#4F6B4A"

def starter(text):
    return f'''
                        <div style="background: #FBF6EA; border-left: 3px solid {BLUE}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def bennett(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {BLUE};">Bennett:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #E9DEC4; border: 1px solid #CDBD98; border-radius: 6px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.1em; color: {AMBER}; margin-right: 6px;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-left: 6px;">· {esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #CDBD98; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def cup(name, ingredients, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F6EFDF; border: 1px dashed #BFAE86; border-radius: 6px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(name)}</strong>
                            <span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {LEAF}; margin-top: 2px;">{esc(ingredients)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{bennett(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = bennett("Tell me what you came in here wanting. Plainly. I'll tell you exactly what goes in the cup, and you'll decide whether to drink it.") + \
     starter("*I take the stool across the counter from him and keep my hands in my lap.* \"I want to know what you'd make for me.\"")
s2 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Three cups on the counter. He reads you the label on each one.</div>' + \
     cup("Slow Burn", "cacao · pepper · honey", "The pepper shows up late, after you've decided you like it. Sip it.",
         "\"Slow Burn. I'll drink it when I'm ready, and not before.\"") + \
     cup("Confession", "damiana · rose · vanilla", "Damiana for honesty, supposedly. Rose because it tastes good. People tend to talk more after the second sip.",
         "*I wrap both hands around the Confession and look at him over the rim.* \"Ask me something.\"") + \
     cup("The Ratio", "clove before vanilla · ginger · orange peel", "New. Tested on no one but me. You'd be the second. I'd take notes. Extensive notes.",
         "\"I'll be your second test subject. Take all the notes you want.\"")
s3 = bennett("The courtyard door is open. Jasmine, rue, a daybed nobody uses for sleeping. There's a collar on the hook by the door. It's yours if you ask for it out loud.") + \
     starter("\"Show me the back room, Bennett. And the hook by the door.\"")

steps = step("I", "The Consultation", "after sundown only", s1, opn=True) + \
        step("II", "The Pour", "choose your cup", s2) + \
        step("III", "The Back Room", "through the courtyard door", s3)

TAGS = ["Aphrodisiacs", "Herbalist", "Mad Genius", "Kinktober Day 7", "Drink When You Decide"]
tagpills = "\n".join(f'            <div style="background-color:#18202A; color:#E2C48E; border: 1px solid #2E4560; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bennett Cole - Kinktober Day 7</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0C0F13; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #141820; border: 1px solid #263243; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E2DFD6; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #263243; padding-bottom:15px; margin-bottom:25px; color: #F2E9D5; letter-spacing: 0.5px;">
            Behind the Blue Door
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #949AA3; font-family: Georgia, serif;">
                “Sit. Touch nothing. I mean that kindly.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Bennett Cole" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #263243; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#10141A; color: #A7ACB3; padding:20px; flex: 1; min-width: 250px; border:1px solid #263243; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">A narrow herbal shop in the Marigny, jars floor to ceiling, jasmine drifting in from the courtyard. Bennett Cole learned plants from his grandmother and botany from a university, and trusts the notebooks more. He talks to his jars. He laughs at the wrong moments. He watches every pulse in the room.</span>
            </div>
            <div style="background-color:#10141A; color: #A7ACB3; padding:20px; flex: 1; min-width: 250px; border:1px solid #263243; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Bennett Cole x Any user<br>
                    Kinktober Day 7: Aphrodisiacs<br>
                    Choose a cup, copy a starter into chat.<br>
                    TW: Sensory play, restraint, collars, degradation (negotiated)<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- APOTHECARY -->
        <div style="margin-top: 35px; background-color: {LABEL}; border: 1px solid #CDBD98; border-top: 8px solid {BLUE}; border-radius: 10px; padding: 22px 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 8px;">OCT 07 · APHRODISIACS · AFTER SUNDOWN</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Private Consultation</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 18px;">The bell over the door rings. He's already looking at you.</div>

            <div style="margin: 0 0 16px; background: #2A1E1A; color: #F2E2C4; border: 2px solid #8A3B32; border-radius: 4px; padding: 10px 12px; text-align: center; font-size: 0.88em; line-height: 1.5;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: #E08A7C; font-weight: 700;">HIGH SHELF · DO NOT TOUCH</span>
                Widow's Patience. Anything unlabeled. Anything you'd have to reach for.
            </div>
{steps}
            <div style="margin-top: 18px; border-top: 1px solid #CDBD98; padding-top: 14px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: left; font-family: Georgia, serif; font-style: italic;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; font-style: normal; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px; text-align: center;">FROM THE NOTEBOOK</span>
                Visitor arrived after rain. Asked what was in the cup before drinking. Good. Clove before the vanilla, always. Pupils: noted. Note to self: eat something.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Yes means more after a no. ~B.C.</div>
        </div>

        <details style="margin-top: 30px; background: #181D25; padding: 12px 20px; border-radius: 8px; border: 1px solid #263243; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #2E3A4A; padding-top: 12px; color: #9EA4AC;">
                Aphrodisiac preparations made from ordinary herbs and spices. Expect sensory play, dominance, restraint, collars, praise, and degradation once it's asked for. All characters are adults. He names what's in every cup, and if you say stop, he stops.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Bennett Cole (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
