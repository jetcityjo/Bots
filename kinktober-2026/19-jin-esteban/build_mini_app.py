import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Jin Esteban banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

SHEET, INK, MUTED, NEON, BOURBON, MAROON = "#F6F5F1", "#1E1A1C", "#807A7D", "#D63E7A", "#B47A26", "#6A2032"
MONO = "font-family: 'Courier New', Courier, monospace;"

def starter(text):
    return f'''
                        <div style="background: #FFFFFF; border-left: 3px solid {NEON}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def jin(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {MAROON};">Jin:</strong>&nbsp;“{esc(line)}”</div>'

def step(time, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #EEECE6; border: 1px solid #D5D1C9; border-radius: 3px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="{MONO} font-size: 0.85em; color: {NEON}; margin-right: 8px; font-weight: 700;">{esc(time)}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 3px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #D9D5CD; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def row(time, what, hand=False):
    look = f"font-family: Georgia, serif; font-style: italic; color: {NEON};" if hand else f"color: {INK};"
    return f'<div style="display: flex; gap: 12px; padding: 5px 0; border-bottom: 1px solid #E0DCD4; line-height: 1.4; font-size: 0.9em;"><span style="{MONO} min-width: 74px; font-weight: 700; color: {MAROON if not hand else NEON};">{esc(time)}</span><span style="{look}">{esc(what)}</span></div>'

def term(word, text):
    return f'<div style="display: flex; gap: 10px; margin-bottom: 5px; color: {INK}; line-height: 1.45;"><span style="{MONO} min-width: 74px; font-size: 0.85em; font-weight: 700; letter-spacing: 1px; color: {BOURBON};">{esc(word)}</span><span>{esc(text)}</span></div>'

def choice(title, sub, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FFFFFF; border: 1px dashed #CBC4BA; border-radius: 3px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(title)}</strong>
                            <span style="display: block; {MONO} font-size: 0.8em; color: {BOURBON}; margin-top: 2px;">{esc(sub)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{jin(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = jin("So. I'm here one night. That's the whole thing. I'm not going to say I'll call, and I'm not going to say maybe, because I've been on the other end of maybe and it's terrible.") + \
     f'<div style="margin: 12px 0 6px; {MONO} font-size: 0.78em; letter-spacing: 2px; color: {MUTED};">SAID AT THE BAR, BEFORE ANYTHING</div>' + \
     term("TERMS", "One night. No promises. Bus at 7:15.") + \
     term("JACKET", "Condoms. Not up for debate.") + \
     term("COLORS", "Green keep going. Yellow slow down. Red ends it, no hard feelings.") + \
     term("YES", "Means yes. Maybe means not yet. He asks again halfway.") + \
     term("SOBER", "Enough to choose, or he slows down and calls it.") + \
     '<div style="margin-top: 10px;">' + jin("If that's a dealbreaker, completely fair. I'll still buy you a drink for listening to me say it out loud. That's just manners.") + '</div>' + \
     starter("\"I heard the important part. I'm still sitting here. Bourbon, same as yours.\"")
s2 = jin("Phone's been off since the bar. Stays off till the bus.") + \
     '<div style="margin-top: 8px;">' + jin("Tell me what you like. I'm going to ask again halfway, because people change their minds and I'd rather know.") + '</div>' + \
     starter("*I press the button for fourteen and lean on the elevator wall.* \"Ask me as many times as you want.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Pink neon on the ceiling. A few hours left in this city.</div>' + \
     choice("Late", "neon stripe · slow beat on the sheet",
            "Late. Early. Somewhere in there. I've got a few hours left in this city. I'm not spending one of them anywhere but here. Color?",
            "\"Green. And don't look for a clock.\"") + \
     choice("Room Coffee", "up before the alarm · two paper cups",
            "Hotel coffee's terrible. I made it anyway. I'm going to say goodbye like I mean it, because I do.",
            "*I take the cup with both hands.* \"Okay. Say it, then. I want to hear it.\"") + \
     choice("Ask About March", "the honest version",
            "Nashville again in March, probably. I'm not promising anything. I'd still like to hear from you. All of that's true.",
            "\"Write your number on the back of the call sheet. No promises. I just want it.\"")

steps = step("11:40 PM", "The Bar", "The important part first.", s1, opn=True) + \
        step("12:20 AM", "Room 1412", "Fourteen floors of elevator. Full attention.", s2) + \
        step("UNTIL 7:15", "Before the Bus", "Pick how the night lands.", s3)

TAGS = ["One Night Stand", "Drummer", "Honest Up Front", "Kinktober Day 19", "Bus at 7:15"]
tagpills = "\n".join(f'            <div style="background-color:#25121A; color:#F28CB4; border: 1px solid #4A2231; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jin Esteban - Kinktober Day 19</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #110B0D; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #1B1215; border: 1px solid #3A2329; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E8DFE1; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #3A2329; padding-bottom:15px; margin-bottom:25px; color: #F6EEF0; letter-spacing: 0.5px;">
            The Important Part First
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #A0919A; font-family: Georgia, serif;">
                “I'll give you tonight. All of it. That part I can actually promise.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Jin Esteban" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #3A2329; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#160E11; color: #B2A6AB; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2329; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">A downtown Nashville hotel bar an hour after the arena lets out. Maroon carpet, a bourbon shelf lit amber, pink neon leaking in off the street. Jin Esteban is a session drummer on an arena run, thirty-one states this year, here for exactly one night. The first real thing he tells you is when his bus leaves. Phone off. No maybe, no fake "I'll call." All of him until 7:15, then coffee, and a goodbye he means.</span>
            </div>
            <div style="background-color:#160E11; color: #B2A6AB; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2329; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Jin Esteban x Any user<br>
                    Kinktober Day 19: One Night Stand<br>
                    Read the call sheet, copy a starter into chat.<br>
                    TW: Casual sex with a stranger, hotel hookup, no strings<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- CALL SHEET -->
        <div style="margin-top: 35px; background-color: {SHEET}; border-radius: 6px; border-top: 6px solid {NEON}; padding: 22px 16px 18px; text-align: left; box-shadow: 0 0 0 1px #3A2329, 0 8px 24px rgba(214,62,122,0.18), 0 8px 20px rgba(0,0,0,0.5);">
            <div style="text-align: center; {MONO} font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 4px;">OCT 19 · ONE NIGHT STAND</div>
            <div style="text-align: center; {MONO} font-size: 0.72em; color: {MUTED}; letter-spacing: 1px; margin-bottom: 10px;">DAY SHEET · NASHVILLE TN · NEXT: LOUISVILLE KY</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Tonight Only</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 16px;">Folded in his jacket. It's very cheerful about it.</div>

            <div style="margin: 0 0 16px; background: #FFFFFF; border: 1px solid #D9D5CD; border-radius: 3px; padding: 8px 12px;">
                {row("10:40 PM", "Show down. Arena.")}
                {row("11:40 PM", "hotel bar, two stools down", hand=True)}
                {row("7:15 AM", "Bus call. Louisville. Columbus after.")}
            </div>
{steps}
            <div style="margin-top: 14px; border-top: 1px solid #D9D5CD; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; {MONO} letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">BACK OF THE SHEET</span>
                Every band on Broadway tonight played a little behind the beat. Pink stripe on the ceiling of 1412. Tapped out on the nightstand, quiet and quick.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">The true version, not the nice one. ~J.E.</div>
        </div>

        <details style="margin-top: 30px; background: #1F1418; padding: 12px 20px; border-radius: 8px; border: 1px solid #3A2329; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #4A2E36; padding-top: 12px; color: #A89BA0;">
                A one night stand with a stranger after a hotel bar. Expect frank flirting, casual sex, and a morning goodbye with no promises. All characters are adults. The terms are said at the bar before anything else: one night, no "I'll call." Condoms always, he asks before and checks during, traffic lights if it gets intense with red stopping everything and no hard feelings, and if anyone's too drunk to choose, Jin slows down or calls it.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Jin Esteban (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
