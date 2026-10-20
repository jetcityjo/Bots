import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: James banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

JUTE, WASHI, INK, MUTED = "#C8A97E", "#EDE6D8", "#2A2724", "#8C8478"

def starter(text, c=JUTE):
    return f'''
                        <div style="background: #F6F1E7; border-left: 3px solid {c}; padding: 8px 12px; border-radius: 4px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def james(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: #7A5C3A;">James:</strong> “{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #E4DCCB; border: 1px solid #CDBFA6; border-radius: 6px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.15em; color: #7A5C3A; margin-right: 6px;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-left: 6px;">· {esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #CDBFA6; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def color(c, word, meaning):
    return f'<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px; color: {INK};"><span style="display: inline-block; width: 14px; height: 14px; border-radius: 999px; background: {c}; border: 1px solid rgba(0,0,0,0.2);"></span><strong style="min-width: 56px;">{word}</strong><span>{esc(meaning)}</span></div>'

def tie(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F0E9DC; border: 1px dashed #B9A887; border-radius: 6px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{james(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = james("Limits. Injuries, old or new. What you want from tonight. What scares you. I don't build on anything I haven't checked.") + \
     starter("*I sit down across the low table from him.* \"Ask me whatever you need to.\"")
s2 = color("#6E9B6A", "Green", "Keep going.") + color("#D2A84A", "Yellow", "Slow down. Something needs to change.") + \
     color("#B5483E", "Red", "Everything stops. He cuts if he has to.") + \
     '<div style="margin-top: 10px;">' + james("The shears stay within reach the whole time. That's not a threat. It's a promise.") + '</div>' + \
     starter("\"Green. Yellow. Red.\" *I say them back to him, one at a time.*")
s3 = '<div style="color: ' + MUTED + '; font-style: italic; font-family: Georgia, serif;">He takes your weight in stages. Green at every one, or you come down.</div>' + \
     tie("1. The Harness", "Arms behind you. The chest harness carries the load, so it has to be right. Breathe into it, not against it.",
         "*I turn my back to him and cross my wrists behind me.* \"Like this?\"") + \
     tie("2. Partial", "One foot stays on the mat. Let the ring take the rest. Tell me where you feel the rope pulling.",
         "\"Green. I'm ready to let go a little more.\"") + \
     tie("3. All the Way Up", "Both feet off. I have you. Look at me, not the floor. Hands, squeeze. Good. You're flying.",
         "\"Green. Take me all the way up.\"")

steps = step("一", "The Conversation", "before the rope comes out", s1, opn=True) + \
        step("二", "The Colors", "say them back to him", s2) + \
        step("三", "The Lift", "harness, partial, then up", s3)

TAGS = ["Suspension", "Shibari", "Silent Dominant", "Kinktober Day 3", "Consent First"]
tagpills = "\n".join(f'            <div style="background-color:#2A241C; color:{JUTE}; border: 1px solid #5A4A34; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>James Michaels - Kinktober Day 3</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0F0E0D; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #1A1917; border: 1px solid #2E2B27; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E2DDD4; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2E2B27; padding-bottom:15px; margin-bottom:25px; color: {WASHI}; letter-spacing: 0.5px;">
            Nothing Begins Without Yes
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #9A9184; font-family: Georgia, serif;">
                “Stability is a choice. The foundation has to be sound first.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="James Michaels" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2E2B27; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 28%; max-width: 180px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#141312; color: #ADA597; padding:20px; flex: 1; min-width: 250px; border:1px solid #2E2B27; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">An architectural consultant by day. By night, a dim loft studio with jute coils along the wall. James used to be a competitive gymnast, and he still knows exactly how long a body can hold still. Tonight he takes you off the floor.</span>
            </div>
            <div style="background-color:#141312; color: #ADA597; padding:20px; flex: 1; min-width: 250px; border:1px solid #2E2B27; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    James Michaels x Any user<br>
                    Kinktober Day 3: Suspension Bondage<br>
                    Work through the protocol, copy a starter into chat.<br>
                    TW: Suspension bondage, restraint, power exchange<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- THE PROTOCOL: washi panel -->
        <div style="margin-top: 35px; background-color: {WASHI}; border: 1px solid #CDBFA6; border-top: 6px solid #7A5C3A; border-radius: 10px; padding: 22px 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 8px;">OCT 03 · SUSPENSION BONDAGE</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">The Protocol</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 22px;">Three steps. He won't skip one. Neither will you.</div>
{steps}
            <div style="margin-top: 18px; border-top: 1px solid #CDBFA6; padding-top: 14px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">AFTERCARE</span>
                Down slowly, onto the mat. Water. The folded blanket. Rope marks checked one by one. Quiet, for as long as it takes.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">I don't leave until you're steady. ~J</div>
        </div>

        <details style="margin-top: 30px; background: #211F1C; padding: 12px 20px; border-radius: 8px; border: 1px solid #2E2B27; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #3A3631; padding-top: 12px; color: #A39B8F;">
                James is a silent dominant and shibari rigger. Expect suspension bondage, rope restraint, and power exchange. All characters are adults. Everything is negotiated, the safety shears stay in reach, and red means stop.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "James Michaels (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
