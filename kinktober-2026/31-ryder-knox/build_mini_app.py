import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Ryder Knox banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

PAPER, INK, MUTED, PUMPKIN, RED = "#F4EFE4", "#25201B", "#867B6E", "#D9732B", "#A3302A"
LINES = ("background-color: #F4EFE4; background-image: linear-gradient(rgba(120,140,170,0.18) 1px, transparent 1px); "
         "background-size: 100% 26px;")

def starter(text):
    return f'''
                        <div style="background: #FFFDF8; border-left: 3px solid {PUMPKIN}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def ryder(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {RED};">Ryder:</strong>&nbsp;“{esc(line)}”</div>'

def section(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,255,255,0.82); border: 1px solid #D8CDB8; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {RED}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #E2D8C5; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def box(checked, text):
    mark = "&#10003;" if checked else "&nbsp;"
    return f'<div style="display: flex; gap: 10px; align-items: flex-start; margin-bottom: 6px; color: {INK}; line-height: 1.45;"><span style="display: inline-block; min-width: 16px; height: 16px; border: 1.5px solid {INK}; border-radius: 2px; text-align: center; font-size: 13px; line-height: 16px; color: {RED}; font-weight: 700;">{mark}</span><span>{esc(text)}</span></div>'

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FBF7EE; border: 1px dashed #CBBFA6; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{ryder(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = box(True, "Written clear-headed, before the cycle.") + box(True, "What's in, in detail.") + box(True, "What's out. Those stay out.") + \
     box(False, "Claiming bite. (Only if you write it here. Never mid-cycle.)") + \
     '<div style="margin-top: 10px;">' + ryder("I read the plan. I follow the plan. Nothing happens in that nest that you didn't write down with a clear head.") + '</div>' + \
     starter("*I hand him my plan.* \"Read it again. I meant every line.\"")
s2 = box(True, "Every blanket he owns, plus a few he bought.") + box(True, "Electrolytes in the fridge, caps loosened.") + \
     box(True, "His flannel. It smells like nothing yet. That's the point.") + box(True, "Blackout curtains. Reading lamp. A cool cloth.") + \
     '<div style="margin-top: 10px;">' + ryder("You build the nest however you want. I don't touch it unless you ask. Then I'm very good at it.") + '</div>' + \
     starter("*I start pulling blankets onto the bed.* \"Give me the flannel. And come hold this corner.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Your plan, your line. Tell him how you meant it.</div>' + \
     choice("Partner", "You meant it? On purpose? Okay. Okay. Give me a second. Nobody's ever...okay. I'm here.",
            "\"Partner, Ryder. On purpose. Not because you're safe. Because I want you.\"") + \
     choice("Sitter, for now", "That's completely fine. I'm still right here, and I'm still the best there is at this. Line stays open.",
            "\"Can we start with sitter tonight? And see?\"") + \
     choice("Take care of him first", "Me? I'm working. I'm...you want to what? Okay. Nobody's ever offered that. I don't know what to do with my hands.",
            "*I take the clipboard out of his hands and set it down.* \"Sit. Tonight somebody takes care of you, too.\"")

parts = section("01", "The Plan", "Signed before the cycle. Law once it starts.", s1, opn=True) + \
        section("02", "The Nest", "Suite one. Build it your way.", s2) + \
        section("03", "Partner: Ryder Knox", "The line nobody has ever filled in with his name.", s3)

TAGS = ["Omegaverse", "Beta", "Caretaker", "Kinktober Day 31", "Picked on Purpose"]
tagpills = "\n".join(f'            <div style="background-color:#241A14; color:#F0B07A; border: 1px solid #5A3622; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ryder Knox - Kinktober Day 31</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0F0D0C; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #1A1513; border: 1px solid #33271F; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E8E0D5; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #33271F; padding-bottom:15px; margin-bottom:25px; color: #F4EFE4; letter-spacing: 0.5px;">
            Nobody Ever Picks the Beta
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #9C8F80; font-family: Georgia, serif;">
                “If you meant it, I'd really like to have been picked on purpose.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Ryder Knox" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #33271F; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#15110F; color: #B0A598; padding:20px; flex: 1; min-width: 250px; border:1px solid #33271F; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">A converted firehouse in Northeast Minneapolis. Three nest suites upstairs, a brass pole with a sign that says NOPE. Ryder Knox is a beta: no heat, no rut, barely a scent, and the steadiest pair of hands in the city. Six years of being everyone's safe choice. Tonight, Halloween, someone chose him.</span>
            </div>
            <div style="background-color:#15110F; color: #B0A598; padding:20px; flex: 1; min-width: 250px; border:1px solid #33271F; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Ryder Knox x Any user (alpha, beta, or omega)<br>
                    Kinktober Day 31: Omegaverse<br>
                    Fill in the plan, copy a starter into chat.<br>
                    TW: Omegaverse heats and ruts, nesting<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- CLIPBOARD -->
        <div style="margin-top: 35px; background: #8A5A33; border-radius: 12px; padding: 14px 10px 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="width: 110px; height: 22px; margin: 0 auto 10px; background: linear-gradient(#C9CCD0, #8E9298); border-radius: 6px 6px 3px 3px; border: 1px solid #6E7278;"></div>
            <div style="{LINES} border-radius: 4px; padding: 20px 16px; text-align: left;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">KNOX CYCLE CARE · OCT 31 · SUITE ONE</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">The Heat Plan</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 20px;">Heat or rut. Filed clear-headed. He's read yours three times.</div>
{parts}
                <div style="margin-top: 14px; border-top: 1px solid #D8CDB8; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">OVERNIGHT NOTES</span>
                    First snow. Jack-o'-lantern still lit. Devil horns stay on till midnight, per the neighbor kids. Legally binding.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Green, yellow, red. I'm right here. ~R.K.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1F1916; padding: 12px 20px; border-radius: 8px; border: 1px solid #33271F; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #43352B; padding-top: 12px; color: #A59A8D;">
                Omegaverse. Expect heats, ruts, nesting, and explicit caretaking intimacy. All characters are adults. The plan, written clear-headed before the cycle, is law: Ryder never goes past it, no claiming bite unless it's written in, and red stops everything.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Ryder Knox (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
