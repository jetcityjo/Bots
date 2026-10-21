import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Reyes Obi banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

FACE, INK, MUTED, AMBER, NEEDLE, BEZEL = "#F3E2B4", "#221C12", "#806F4E", "#C98A1E", "#B3261E", "#16130E"
GLOW = "background-color: #F3E2B4; background-image: radial-gradient(ellipse at 50% 0%, rgba(255,214,130,0.75), rgba(243,226,180,0) 70%);"

def starter(text):
    return f'''
                        <div style="background: #FFF8E6; border-left: 3px solid {AMBER}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def reyes(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {NEEDLE};">Reyes:</strong>&nbsp;“{esc(line)}”</div>'

def step(time, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,250,236,0.78); border: 1px solid #D6BF86; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.88em; color: {NEEDLE}; margin-right: 8px; font-weight: 700;">{time}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #DCC897; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def light(color, label, text):
    return f'<div style="display: flex; gap: 10px; align-items: flex-start; margin-bottom: 6px; color: {INK}; line-height: 1.45;"><span style="display: inline-block; min-width: 14px; height: 14px; margin-top: 3px; border-radius: 50%; background: {color}; border: 1px solid rgba(0,0,0,0.35);"></span><span><strong style="font-family: \'Courier New\', Courier, monospace; letter-spacing: 1px;">{label}</strong>&nbsp;{esc(text)}</span></div>'

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FBF1D6; border: 1px dashed #C9AE6E; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{reyes(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = reyes("I don't know if the light's on, or what you're wearing, or what you can hear out your window. I'm not going to make it up. So tell me. Where are you?") + \
     starter("\"I'm here. Lights off. Let me tell you where.\"")
s2 = light("#4F8A3C", "GREEN", "Keep going.") + light("#D9A21E", "YELLOW", "Slow down. He waits.") + \
     light(NEEDLE, "RED", "Instruction stops. He talks about something boring until you're fine.") + \
     f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif; margin: 8px 0 10px;">Every instruction is an offer. Your hands are your own. Either of you can hang up, no apology.</div>' + \
     reyes("I can't see you. All I've got is what you say. So if it's yellow, say yellow. If you lie to me on the phone, I've got nothing. Tell me the color, slowly, and mean it.") + \
     starter("\"Green. Slowly, like you asked. Give me the first thing.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">The needles are back at zero. Pick the request.</div>' + \
     choice("Say my name again", "Despacio. Okay. I'll say it once. Then you're going to tell me exactly what it did.",
            "\"Say my name again. The real voice, not the radio one.\"") + \
     choice("The meditation voice", "No. I'm not doing the work voice. That's unfair of you. Fine. Unclench your jaw. See? Now you owe me.",
            "\"Do the app voice. Just once. Tell me to relax.\"") + \
     choice("Don't hang up yet", "I wasn't going to. Stay on. You don't have to talk. I'm just going to listen to you breathe for a while.",
            "\"Don't hang up yet. Play me something down the phone.\"")

steps = step("02:04", "Tell Me Where You Are", "He asks. He doesn't guess.", s1, opn=True) + \
        step("02:09", "One at a Time", "Green, yellow, red. Then the first instruction.", s2) + \
        step("02:51", "Stay On the Line", "Requests taken after sign-off.", s3)

TAGS = ["Phone Sex", "Voice Dom", "Long Distance", "Kinktober Day 11", "After Sign-Off"]
tagpills = "\n".join(f'            <div style="background-color:#1D1608; color:#FFC75E; border: 1px solid #5C4512; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

scale = "".join(
    f'<span style="color: {NEEDLE if v.startswith("+") or v == "0" else MUTED}; font-weight: {700 if v == "0" else 400};">{v}</span>'
    for v in ["-20", "-10", "-7", "-5", "-3", "0", "+3"])

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reyes Obi - Kinktober Day 11</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0B0906; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #15110B; border: 1px solid #3A2E17; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E9DFCB; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #3A2E17; padding-bottom:15px; margin-bottom:25px; color: #F3E2B4; letter-spacing: 0.5px;">
            Two in the Morning, Los Angeles
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #A3927A; font-family: Georgia, serif;">
                “I don't know where you are right now. I want to. Tell me where you are.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Reyes Obi" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #3A2E17; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#110E09; color: #B3A68F; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2E17; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Reyes Obi hosts the overnight on a small listener-funded station in Echo Park, ten to two. Thursdays he runs it from a closet in Highland Park lined with moving blankets, one good mic and two amber VU meters from a swap meet. Weeks ago you called the request line. He didn't have the song. He called back after sign-off to apologize. Now he calls most nights, a little after two.</span>
            </div>
            <div style="background-color:#110E09; color: #B3A68F; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2E17; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Reyes Obi x Any user<br>
                    Kinktober Day 11: Phone Sex<br>
                    Pick up the call, copy a starter into chat.<br>
                    TW: Phone sex, verbal instruction, guided self-touch, praise<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- VU METER -->
        <div style="margin-top: 35px; background: {BEZEL}; border: 1px solid #4A3A1C; border-radius: 14px; padding: 14px 10px 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.06);">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 8px 10px; font-family: 'Courier New', Courier, monospace; font-size: 0.72em; letter-spacing: 2px;">
                <span style="color: #6E5E40;">THE OVERNIGHT · REMOTE</span>
                <span style="background: #2A1210; color: #6B3A34; border: 1px solid #4A2420; border-radius: 3px; padding: 2px 8px;">ON AIR</span>
            </div>
            <div style="{GLOW} border-radius: 8px; padding: 20px 16px; text-align: left;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 11 · PHONE SEX</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">After Sign-Off</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 14px;">The fader's down. The phone rings twice. He knows the number by heart.</div>
                <div style="display: flex; justify-content: space-between; font-family: 'Courier New', Courier, monospace; font-size: 0.78em; border-bottom: 2px solid {INK}; padding: 0 4px 4px; margin: 0 6px 6px;">{scale}</div>
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.72em; letter-spacing: 3px; color: {MUTED}; margin-bottom: 18px;">VU</div>
{steps}
                <div style="margin-top: 14px; border-top: 1px solid #D6BF86; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">PROGRAM LOG · THURS</span>
                    Reno requested the same song three times. Played it twice. Fridge kicked on at 2:06, moved the left needle. Dog across the street had opinions.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Hang up whenever you want. I won't. ~R.O.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1A150D; padding: 12px 20px; border-radius: 8px; border: 1px solid #3A2E17; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #4A3A1C; padding-top: 12px; color: #A89A82;">
                Long-distance phone sex. Expect a voice dom giving slow verbal instructions, guided self-touch, descriptive dirty talk, and praise. All characters are adults. Every instruction is an offer and your hands are your own. Green, yellow, red: red stops all instruction and he just talks until you're okay. Either of you can hang up at any time, no guilt.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Reyes Obi (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
