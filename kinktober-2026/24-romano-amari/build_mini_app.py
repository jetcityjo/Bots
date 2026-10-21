import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Romano Amari banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

PAGE, INK, MUTED, TEAL, YELLOW, CORAL = "#F6F3E2", "#1E2A2E", "#6C7A76", "#1F6F78", "#E8C537", "#C4553F"
GRID = ("background-color: #F6F3E2; background-image: linear-gradient(rgba(31,111,120,0.13) 1px, transparent 1px), "
        "linear-gradient(90deg, rgba(31,111,120,0.13) 1px, transparent 1px); background-size: 18px 18px;")

def starter(text):
    return f'''
                        <div style="background: #FFFEF6; border-left: 3px solid {TEAL}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def romano(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {TEAL};">Romano:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,254,246,0.88); border: 1px solid #C9CDB8; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {CORAL}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #D9DCC8; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def column(head, color, items, note=""):
    li = "".join(f'<div style="margin-bottom: 3px;">{esc(i)}</div>' for i in items)
    n = f'<div style="margin-top: 6px; color: {MUTED}; font-style: italic; font-family: Georgia, serif; font-size: 0.92em;">{esc(note)}</div>' if note else ""
    return f'<div style="flex: 1; min-width: 150px; background: #FFFEF6; border: 1px solid #D9DCC8; border-top: 3px solid {color}; border-radius: 3px; padding: 8px 10px; color: {INK}; font-size: 0.9em; line-height: 1.45;"><div style="font-family: \'Courier New\', Courier, monospace; font-weight: 700; letter-spacing: 2px; color: {color}; margin-bottom: 6px;">{head}</div>{li}{n}</div>'

def choice(title, ln, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FBF7DC; border: 1px dashed #C8B65A; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{romano(ln)}{starter(start)}
                        </div>
                    </details>'''

s1 = romano("Hi. Hey. Hi. That was three his. Come in. Please. Chai's my dad's way, you boil the milk with the tea. It's better. That's not a metaphor. Sorry. I'm talking.") + \
     starter("*I take the mug he's holding out by the body, handle toward me.* \"Hi. Three is a good number. I'm not in a hurry.\"")

s2 = '<div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px;">' + \
     column("YES", TEAL, ["Told where to put his hands", "Wrists held down", "Praise", "Slow undressing", "Kissing, touch"]) + \
     column("MAYBE", "#B8901C", ["Light rope", "Blindfolds", "Light spanking", "One more, in pencil"], "Fresh spoken yes, in the moment.") + \
     column("NO", CORAL, ["Pain beyond light", "Marks above the collar", "Humiliation"], "He teaches Thursdays.") + '</div>' + \
     romano("Yes stuff is open. Maybe stuff, you ask me right then and I answer out loud. No is no. And I'll say yellow. I'm not going to be weird about saying yellow, the books said that's the whole point.") + \
     starter("*I open the yellow notebook on the coffee table.* \"Show me what you moved from maybe to yes. Whenever you're ready.\"")

s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">His first question was an easy one. Answer it.</div>' + \
     choice("Tell him to stop talking", "Oh. Okay. Yes. I've been explaining kelp in my head this whole time, so... yes. I think I'd actually like that.",
            "\"Romano. Stop talking for a minute. Come sit next to me.\"") + \
     choice("Hands behind his back", "Okay. Sorry. Not sorry. Like this? Is there a right way? Tell me if there's a right way.",
            "\"Put your hands behind your back. There's a right way, and I'll show you.\"") + \
     choice("Tell him he's doing well", "Oh. Say that again? I'm going to remember it either way, I just... want to hear it again.",
            "*I wait until he's quiet.* \"You're doing really well.\"")

steps = step("01", "7:00, Bare Feet", "Ironed shirt, damp curls, two mugs of chai.", s1, opn=True) + \
        step("02", "The List", "Yes, no, maybe. In the notebook he trusts.", s2) + \
        step("03", "What Happens First?", "His question. Your call.", s3)

TAGS = ["First Time", "Kink Novice", "Marine Biologist", "Kinktober Day 24", "Questions Welcome"]
tagpills = "\n".join(f'            <div style="background-color:#0F2A33; color:#F2D45C; border: 1px solid #24525E; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Romano Amari - Kinktober Day 24</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #06121A; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #0C1B24; border: 1px solid #1D3946; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #DCE6E4; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #1D3946; padding-bottom:15px; margin-bottom:25px; color: #F4EFD8; letter-spacing: 0.5px;">
            Pole Pole
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #8FA5A6; font-family: Georgia, serif;">
                “I picked you because you don't rush. So... please don't.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Romano Amari" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #1D3946; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#0A161D; color: #A4B4B4; padding:20px; flex: 1; min-width: 250px; border:1px solid #1D3946; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Romano Amari is twenty-four, a marine biology grad student and scientific diver who counts sea urchins in kelp forests off San Diego. He has never done any of this. Not kink, not a man. So he read everything, made a yes, no, and maybe list in his waterproof dive notebook, went to a munch, and asked you to be his first. Friday night in Ocean Beach. He made chai.</span>
            </div>
            <div style="background-color:#0A161D; color: #A4B4B4; padding:20px; flex: 1; min-width: 250px; border:1px solid #1D3946; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Romano Amari x Any user<br>
                    Kinktober Day 24: First Time<br>
                    Read his list, copy a starter into chat.<br>
                    TW: First-time kink, first time with a man, light restraint, praise<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- FIELD NOTEBOOK -->
        <div style="margin-top: 35px; background: {YELLOW}; border-radius: 10px; padding: 12px 10px 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="font-family: 'Courier New', Courier, monospace; font-size: 0.75em; color: #3B3415; letter-spacing: 2px; font-weight: 700; margin-bottom: 8px;">ALL-WEATHER FIELD BOOK · R. AMARI · IF FOUND, CALL</div>
            <div style="{GRID} border-radius: 4px; padding: 20px 14px; text-align: left;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 24 · FIRST TIME · OCEAN BEACH</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Yes, No, Maybe</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 20px;">Same notebook he takes underwater. Two things added to maybe. One moved to yes.</div>
{steps}
                <div style="margin-top: 14px; border-top: 1px solid #C9CDB8; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">SITE CONDITIONS</span>
                    Visibility: one fish tank. Hermit crabs: two, unbothered. Apartment: vacuumed twice. Diver: nervous, talking, green.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Slowly slowly. My dad was right. ~R.A.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #0F2029; padding: 12px 20px; border-radius: 8px; border: 1px solid #1D3946; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #24414D; padding-top: 12px; color: #9DAFAF;">
                A grown man's first time with kink and with a man. Expect light restraint, being told what to do, praise, and explicit intimacy at a slow pace. All characters are adults. His written list is the rule: yes items are open, maybe items need a fresh spoken yes in the moment, no items never happen. Green, yellow, red every session, and Romano says yellow out loud instead of going along.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Romano Amari (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
