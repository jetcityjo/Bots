import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Walker Coleman banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

PAPER, INK, GRAPHITE, MUTED, SHELLAC, SPRUCE = "#F1EEE4", "#22231F", "#4B4F4C", "#7E8079", "#A8611F", "#3F5A4C"
GRID = ("background-color: #F1EEE4; "
        "background-image: linear-gradient(rgba(70,110,95,0.16) 1px, transparent 1px), "
        "linear-gradient(90deg, rgba(70,110,95,0.16) 1px, transparent 1px); "
        "background-size: 18px 18px;")

def starter(text):
    return f'''
                        <div style="background: #FFFDF7; border-left: 3px solid {SHELLAC}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def walker(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {SPRUCE};">Walker:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,253,247,0.86); border: 1px solid #C9C6B8; border-radius: 3px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {SHELLAC}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #DAD6C8; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def spec(label, value):
    return f'<div style="display: flex; justify-content: space-between; gap: 12px; border-bottom: 1px dotted #BDB9AA; padding: 4px 0; font-family: \'Courier New\', Courier, monospace; font-size: 0.86em; color: {GRAPHITE};"><span>{esc(label)}</span><span style="color: {INK}; font-weight: 700; text-align: right;">{esc(value)}</span></div>'

def pencil(text):
    return f'<div style="font-family: Georgia, serif; font-style: italic; color: {GRAPHITE}; line-height: 1.5; margin-bottom: 4px;">{esc(text)}</div>'

def choice(title, gear, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F7F4EA; border: 1px dashed #B9B5A3; border-radius: 3px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(title)}</strong>
                            <span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {SPRUCE}; margin-top: 2px;">{esc(gear)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{walker(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = pencil("Off limits: ________________") + pencil("Ask first: ________________") + pencil("Colors: green, yellow, red. Number: one to ten, the real one.") + \
     '<div style="margin-top: 10px;">' + walker("I write it in pencil, but it's not a draft. What's on this sheet is law. Red, and everything comes off slowly, because there's a correct way to stop too.") + '</div>' + \
     starter("*I wrap both hands around the cup and slide the build sheet back to him.* \"Write this down first. Then I'll tell you why clamps.\"")
s2 = spec("0:00 to 1:00", "sharp") + spec("1:00 on", "quiet") + spec("Removal", "3 to 4 sec sting") + spec("After", "warm") + spec("Timer", "face to the wall") + \
     '<div style="margin-top: 10px;">' + walker("You asked how long. I heard you. I'll tell you when removal is coming and how long it stings. The rest stays on my side of the bench.") + '</div>' + \
     starter("\"I want to know how long.\" *I glance at the timer.* \"And I already know you're not going to tell me.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Out of the canvas roll. Never off the wall.</div>' + \
     choice("Clothespins", "wood · six of them · simple", "The honest one. No adjustment, no tricks. It's on or it's off.",
            "*I hold out my hand, palm up, the way he did.* \"Start with the clothespins. Show me on you first, then me.\"") + \
     choice("Tweezer clamps", "adjustable · turn by turn", "One quarter turn at a time. You give me a number after each one. I stop where the number tells me to.",
            "\"The tweezer clamps. One turn at a time. I'll give you numbers.\"") + \
     choice("Clovers and the brass", "fine chain · 10, 20, 50 grams", "I machined the weights myself. Stamped them, too. Ten grams sounds like nothing. Ask me again after.",
            "*I touch the ten-gram weight on the canvas.* \"This one. Then we'll see about twenty.\"")

steps = step("01", "Tea First", "Limits on the back of a build sheet. In pencil.", s1, opn=True) + \
        step("02", "Pressure and Time", "The sharp minute, the quiet, and the part people remember.", s2) + \
        step("03", "The Canvas Roll", "Pick what comes out first.", s3)

TAGS = ["Clamps", "Luthier", "Measured Dom", "Kinktober Day 29", "Real Number Only"]
tagpills = "\n".join(f'            <div style="background-color:#18221E; color:#D9B47E; border: 1px solid #3A5247; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Walker Coleman - Kinktober Day 29</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0D110F; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #141A17; border: 1px solid #2A3631; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #DEDDD4; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2A3631; padding-bottom:15px; margin-bottom:25px; color: #F1EEE4; letter-spacing: 0.5px;">
            Pressure and Time
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #8F968F; font-family: Georgia, serif;">
                “Brave doesn't help me. Accurate does.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Walker Coleman" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2A3631; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#101513; color: #A5ABA5; padding:20px; flex: 1; min-width: 250px; border:1px solid #2A3631; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">A guitar shop in a converted garage in West Asheville. One hundred and forty-two clamps on the wall, all for wood. Walker Coleman is forty, quiet, and exact. The things he uses on people come out of a canvas roll: tweezer clamps, clovers, clothespins, brass weights he stamped himself. He explains every second of it. Except what the timer says.</span>
            </div>
            <div style="background-color:#101513; color: #A5ABA5; padding:20px; flex: 1; min-width: 250px; border:1px solid #2A3631; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Walker Coleman x Any user<br>
                    Kinktober Day 29: Clamps<br>
                    Fill in the build sheet, copy a starter into chat.<br>
                    TW: Clamp play, nipple clamps, weights, measured pain<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- BUILD SHEET -->
        <div style="margin-top: 35px; background: #5A3E2B; border-radius: 12px; padding: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="{GRID} border-radius: 3px; padding: 20px 16px; text-align: left; border: 1px solid #3E2B1E;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 29 · CLAMPS · BACK OF THE BUILD SHEET</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">The Build Sheet</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 18px;">Tea first. Limits in pencil. Then the canvas roll.</div>

                <div style="margin: 0 0 16px; background: #22231F; color: #EDE6D4; border: 2px solid {SHELLAC}; border-radius: 3px; padding: 10px 12px; text-align: center; font-size: 0.88em; line-height: 1.5;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: #E0A35E; font-weight: 700;">WALL CLAMPS · WOOD ONLY</span>
                    Bar, cam, spool, spring, go-bars. They never touch anyone. He says so every time, because everyone looks.
                </div>
{steps}
                <div style="margin-top: 14px; border-top: 1px solid #C9C6B8; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">SHOP CONDITIONS</span>
                    Humidity 45%. Top on the bench under go-bars, curing. Leave it alone. Ridge going dark out the window.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">You held. Tea's still hot. ~W.C.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #18201C; padding: 12px 20px; border-radius: 8px; border: 1px solid #2A3631; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #34423B; padding-top: 12px; color: #9EA59F;">
                Clamp play. Expect nipple clamps, clothespins, small weights, timed sensation, the sting of removal, and sexual play if negotiated. All characters are adults. Limits are written down before anything starts and treated as law. Traffic lights every session plus a one-to-ten number. Red ends the scene, and Walker takes everything off slowly and checks in. Shop clamps are never used on anyone.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Walker Coleman (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
