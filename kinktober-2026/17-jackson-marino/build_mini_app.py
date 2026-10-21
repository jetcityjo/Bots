import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Jackson Marino banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

CANVAS, INK, MUTED, NAVY, MANILA, SHEARS = "#ECE5D4", "#1F2328", "#7D786C", "#1B2E45", "#A9834C", "#E05A1A"
ROPE = "background: repeating-linear-gradient(135deg, #B8935A 0 7px, #8C6A38 7px 11px, #C7A56E 11px 14px);"
CHALK = ("background-color: #ECE5D4; background-image: linear-gradient(90deg, transparent 49.6%, rgba(27,46,69,0.10) 49.6%, "
         "rgba(27,46,69,0.10) 50.4%, transparent 50.4%);")

def starter(text):
    return f'''
                        <div style="background: #FAF7EF; border-left: 3px solid {SHEARS}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def jackson(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {NAVY};">Jackson:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #FBF8F0; border: 1px solid #CFC5AE; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="display: inline-block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: #F4EEE0; background: {NAVY}; border-radius: 3px; padding: 1px 7px; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 3px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #DCD3BE; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def color(word, swatch, text):
    return f'<div style="display: flex; gap: 10px; align-items: baseline; margin-bottom: 5px; color: {INK}; line-height: 1.45;"><span style="display: inline-block; width: 11px; height: 11px; border-radius: 50%; background: {swatch}; flex: none;"></span><span style="min-width: 62px; font-family: \'Courier New\', Courier, monospace; font-size: 0.85em; font-weight: 700; letter-spacing: 1px;">{esc(word)}</span><span>{esc(text)}</span></div>'

def choice(title, sub, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F5F0E3; border: 1px dashed #BBA982; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(title)}</strong>
                            <span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MANILA}; margin-top: 2px;">{esc(sub)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{jackson(line)}{starter(start)}
                        </div>
                    </details>'''

GROMMET = "position: absolute; width: 14px; height: 14px; border-radius: 50%; background: radial-gradient(circle, #2A2A2A 0 3px, #C9B27A 3px 6px, #8E7A48 6px 7px);"

s1 = jackson("Put your hand on that. Rub it between your fingers. If it scratches, I want to know now. Not twenty minutes in.") + \
     f'<div style="margin: 12px 0 6px; font-family: \'Courier New\', Courier, monospace; font-size: 0.78em; letter-spacing: 2px; color: {MUTED};">SAID ONCE. SAID EVERY TIME.</div>' + \
     color("GREEN", "#4E8A4A", "Keep going.") + \
     color("YELLOW", "#D9A62A", "He slows down. You talk.") + \
     color("RED", "#B8322A", "Every line comes off. At once.") + \
     color("NUMB", "#5C7894", "Cold, tingly, sharp. Say it right then. Not after.") + \
     '<div style="margin-top: 10px;">' + jackson("Fine isn't a color. Numb, cold, tingly, or green. Those are your words.") + '</div>' + \
     starter("*I run the line through my fist the way he did.* \"Soft. It doesn't scratch. Say the colors one more time anyway.\"")
s2 = jackson("Two fingers under the wrap. That's what it stays at. You want to feel held, I add a wrap. I don't crank the one you've got.") + \
     '<div style="margin-top: 8px;">' + jackson("Squeeze. Good. Fingers. Good. Now quit trying to impress me.") + '</div>' + \
     starter("*I hold both wrists out to him over the sail bench.* \"Wrists first. Show me the bowline.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Floor work only. Everything agreed over coffee. Everything off in ten seconds.</div>' + \
     choice("Chest Harness", "bight · half hitches · nothing near the throat",
            "Arms down. Breathe out. I'm going to put a lot of line on you and none of it goes anywhere near your neck. Color?",
            "\"Green. Chest next. Take your time with it.\"") + \
     choice("Made Fast to the Chair", "round turn and two half hitches · each rung",
            "Feet flat. One ankle to each rung. You can still wiggle your toes. You'd better, I'll be checking.",
            "*I sit in the old chair and set my feet against the rungs.* \"Make them fast, sailor.\"") + \
     choice("Ease Off", "end to end · slow · the marks",
            "Hold still. I take it off slow. There. Look at that. Gone by morning. Pity. Tea's my mother's. Don't tell her it's good.",
            "\"Leave the blanket for a minute. Tell me what the marks look like.\"")

steps = step("01", "Hands on the Line", "Three-strand manila. A season behind his boat.", s1, opn=True) + \
        step("02", "Wrists First", "Bowline. Clove hitch. Old, boring knots.", s2) + \
        step("03", "Make Fast", "Pick where the next line goes.", s3)

TAGS = ["Rope Bondage", "Sailor's Knots", "Dominant", "Kinktober Day 17", "Shears on the Belt"]
tagpills = "\n".join(f'            <div style="background-color:#18201F; color:#F09A62; border: 1px solid #2F4140; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jackson Marino - Kinktober Day 17</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0D1212; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #151C1C; border: 1px solid #2B3938; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #DDE1DC; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2B3938; padding-bottom:15px; margin-bottom:25px; color: #ECE5D4; letter-spacing: 0.5px;">
            Old, Boring Knots
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #8F9A97; font-family: Georgia, serif;">
                “They hold under load and they let go when you ask. That's all I want out of a knot.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Jackson Marino" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2B3938; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#111717; color: #A6AEAB; padding:20px; flex: 1; min-width: 250px; border:1px solid #2B3938; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Marino Sail &amp; Rigging, second floor over a lobster dealer off Commercial Street, Portland, Maine. Pine floor, three work lamps, a half-finished jib, the foghorn every thirty seconds. Jackson Marino is the third Marino to run the loft. He ties with sailor's knots and manila broken in behind his own sloop. Floor work only. The orange shears on his belt have never been needed. He wears them anyway.</span>
            </div>
            <div style="background-color:#111717; color: #A6AEAB; padding:20px; flex: 1; min-width: 250px; border:1px solid #2B3938; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Jackson Marino x Any user<br>
                    Kinktober Day 17: Rope Bondage<br>
                    Feel the line, copy a starter into chat.<br>
                    TW: Rope bondage, restraint, dominance, rope marks<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- SAIL PATCH -->
        <div style="margin-top: 35px; {ROPE} border-radius: 10px; padding: 9px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="position: relative; {CHALK} border-radius: 4px; padding: 26px 16px 20px; text-align: left;">
                <span style="{GROMMET} left: 8px; top: 8px;"></span>
                <span style="{GROMMET} right: 8px; top: 8px;"></span>
                <span style="{GROMMET} left: 8px; bottom: 8px;"></span>
                <span style="{GROMMET} right: 8px; bottom: 8px;"></span>
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 17 · ROPE BONDAGE</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {NAVY}; letter-spacing: 1px;">The Knot Board</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 18px;">Chalked on canvas at the loft. Shoes off. Floor's for canvas.</div>

                <div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 0 0 16px;">
                    <div style="flex: 1; min-width: 200px; background: {NAVY}; color: #E9E3D3; border-radius: 4px; padding: 10px 12px; font-size: 0.86em; line-height: 1.55;">
                        <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: #F09A62; font-weight: 700; margin-bottom: 4px;">ON THE BOARD</span>
                        Bowline. Clove hitch. Figure eight. Round turn and two half hitches.
                    </div>
                    <div style="flex: 1; min-width: 200px; background: #FAF7EF; color: {INK}; border: 2px solid {SHEARS}; border-radius: 4px; padding: 10px 12px; font-size: 0.86em; line-height: 1.55;">
                        <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {SHEARS}; font-weight: 700; margin-bottom: 4px;">NOT ON THIS BOAT</span>
                        Knots that cinch. Line across the throat. Suspension. Being left tied and alone.
                    </div>
                </div>
{steps}
                <div style="margin-top: 14px; border-top: 1px solid #CFC5AE; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">LOFT LOG</span>
                    Fog in for the night. Horn every thirty seconds. Space heater ticking. Ginger tea in the dented thermos. Shears on the belt, still unused.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Two fingers under every wrap. ~J.M.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #182020; padding: 12px 20px; border-radius: 8px; border: 1px solid #2B3938; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #33433F; padding-top: 12px; color: #9DA6A2;">
                Adult rope bondage on the floor: wrists, chest harness, ankles to a chair, the sail bench. Expect restraint, dominance, teasing, rope marks, and sex inside the ties once it's negotiated. All characters are adults. Limits and old injuries are law, traffic lights every session, red takes every line off at once, numb or cold or tingly gets reported right then, and nobody is ever left tied and alone.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Jackson Marino (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
