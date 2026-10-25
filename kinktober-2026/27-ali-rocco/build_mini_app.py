import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Ali Rocco banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

PAPER, INK, MUTED, RED, BRASS, GRID = "#F2E3A0", "#22241F", "#7A7558", "#A8261E", "#8E6B22", "rgba(70,100,80,0.20)"
GRIDBG = (f"background-color: {PAPER}; background-image: linear-gradient({GRID} 1px, transparent 1px), "
          f"linear-gradient(90deg, {GRID} 1px, transparent 1px); background-size: 22px 22px;")

def starter(text):
    return f'''
                        <div style="background: #FFFBEA; border-left: 3px solid {RED}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def ali(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {RED};">Ali:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,252,236,0.88); border: 1px solid #CDBB72; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {BRASS}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #DCCB86; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def light(color, word, text):
    return f'<div style="display: flex; gap: 10px; align-items: center; margin-bottom: 6px; color: {INK}; line-height: 1.45;"><span style="display: inline-block; min-width: 14px; height: 14px; border-radius: 50%; background: {color}; border: 1px solid rgba(0,0,0,0.35);"></span><span><strong>{esc(word)}</strong> · {esc(text)}</span></div>'

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FBF4D4; border: 1px dashed #BFAE62; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{ali(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = light(BRASS, "Bell", "Shot-glass size, on a leather loop. Yours to hold.") + light(RED, "Light", "One red work bulb.") + \
     light("#5E6B58", "Frame", "Steel, bolted to the floor, cuffs hanging open.") + light("#B98A4A", "Tea", "Tulip glass, steaming on the windowsill.") + \
     '<div style="margin-top: 10px;">' + ali("On patrol we checked the beacons every morning, bluebird days too. Same here. We do the boring part once, properly, and then I'm not stopping every two minutes to ask you stuff.") + '</div>' + \
     starter("*I nod at the steel frame.* \"Okay. Show me the gear first.\"")
s2 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif; margin-bottom: 8px;">Brass, shot-glass size, worn smooth on one side. Worn smooth on one side from his thumb.</div>' + \
     ali("Sorry. I do that every Thursday. Everybody jumps. You hold it. Can't talk, let go. I hear it, I'm there.") + \
     starter("*I hold the bell out over the floor and open my hand.*")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Two weeks of talking. Pick where it starts.</div>' + \
     choice("The frame", "Aferin. Hands up. Cuffs are open, and the bell goes in your right hand.",
            "\"Put me on the frame.\"") + \
     choice("The blindfold", "Yavaş. Everything gets louder with this on. The chairs downstairs. The tea cooling. Me.",
            "\"Blindfold first.\"") + \
     choice("The after", "Water first. Then tea. Then you tell me how it was, and tomorrow I text you and you tell me again.",
            "\"Blanket, water, and you stay a while after.\"")

steps = step("01", "Dig the Pit", "Check the gear before anything steep.", s1, opn=True) + \
        step("02", "Drop the Bell", "We practice stopping first.", s2) + \
        step("03", "The Line Down", "Further than you've ever gone.", s3)

TAGS = ["Safewords", "Dungeon Monitor", "Ex Ski Patrol", "Kinktober Day 27", "Ring the Bell"]
tagpills = "\n".join(f'            <div style="background-color:#1F1C14; color:#E3C26A; border: 1px solid #4E4426; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ali Rocco - Kinktober Day 27</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0D0E0F; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #171819; border: 1px solid #303234; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E2E0D8; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #303234; padding-bottom:15px; margin-bottom:25px; color: #F2E3A0; letter-spacing: 0.5px;">
            Practice Stopping First
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #9A988E; font-family: Georgia, serif;">
                “Two weeks we've been talking about tonight.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Ali Rocco" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #303234; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#121314; color: #A9A79E; padding:20px; flex: 1; min-width: 250px; border:1px solid #303234; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">The Switchyard, a members-only play space in an old rail warehouse in RiNo, Denver. Ali Rocco walks the floor, teaches the Thursday consent class, and keeps a double teapot going at the DM station. He spent twelve winters on ski patrol and still checks the gear before anything steep. Room Four is upstairs. One red light, a steel frame, and a brass bell.</span>
            </div>
            <div style="background-color:#121314; color: #A9A79E; padding:20px; flex: 1; min-width: 250px; border:1px solid #303234; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Ali Rocco x Any user<br>
                    Kinktober Day 27: Safewords<br>
                    Work the route plan, copy a starter into chat.<br>
                    TW: BDSM, restraint, impact play, blindfolds, deep headspace<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- FIELD BOOK -->
        <div style="margin-top: 35px; background: #3B4A3E; border-radius: 10px; padding: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="font-family: 'Courier New', Courier, monospace; font-size: 0.72em; color: #D8D2B0; letter-spacing: 3px; text-align: center; margin-bottom: 8px;">FIELD BOOK · A. ROCCO</div>
            <div style="{GRIDBG} border-radius: 4px; padding: 20px 16px; text-align: left;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 27 · SAFEWORDS</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Route Plan: Room Four</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 20px;">Dig the pit. Check the beacon. Know your way out.</div>
{steps}
                <div style="margin-top: 14px; border-top: 1px solid #CDBB72; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">DM STATION</span>
                    Tea in a tulip glass on the windowsill. Chairs still stacking downstairs. Text goes out tomorrow: how are you, really.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Water first. Then we talk. ~A.R.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1C1D1E; padding: 12px 20px; border-radius: 8px; border: 1px solid #303234; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #3C3E40; padding-top: 12px; color: #A09E96;">
                Dominant BDSM scene in a play space. Expect restraint, slow-building impact, blindfolds, and scenes that go deep into headspace. All characters are adults. Saying red, or letting go of the bell, stops everything.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Ali Rocco (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
