import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Esteban Booker banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

SLEEVE, INK, MUTED, PLUM, EUC, EMBER = "#EFE6DA", "#231A21", "#8A7C82", "#6B2F5C", "#4E7C6B", "#C8642E"

def starter(text):
    return f'''
                        <div style="background: #FBF7F1; border-left: 3px solid {EUC}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def esteban(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {PLUM};">Esteban:</strong>&nbsp;“{esc(line)}”</div>'

def track(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #F7F1E8; border: 1px solid #D9CCBE; border-radius: 6px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {EMBER}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #E3D8CB; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FFFCF7; border: 1px dashed #CDB9C4; border-radius: 6px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{esteban(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = esteban("That's yours tonight. Hold it the whole time. You drop it, I stop. No talking required.") + \
     '<div style="margin-top: 8px;">' + esteban("Words get hard later. I'm counting on it. And you're not on my books. You're in my house.") + '</div>' + \
     starter("*I close my hand around the ball.* \"Okay. Nervous is about a three. Ask me again in a minute.\"")
s2 = esteban("When your body finishes, that is not the same thing as us being done. We talked about it. Everybody thinks it's the finish line.") + \
     '<div style="margin-top: 8px;">' + esteban("Oh, you finished. Congratulations. Hand's staying right where it is. Pressure's going feather light. Number.") + '</div>' + \
     starter("\"I already came. Isn't that it?\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">He asks. You answer. He repeats back what he hears.</div>' + \
     choice("Three", "I heard three. Three means we're still working, baby. Lighter. Slower. Somewhere new. Breathe into it.",
            "\"Three. Still three. Don't you dare stop.\"") + \
     choice("Four", "I heard four. Hands off, one flat on the blanket, nowhere that matters. You held at the edge a whole song. Breathe. Longer than that.",
            "\"Four. Give me a second.\"") + \
     choice("Drop the ball", "Done. Hands are up where you can see them. Towel's hot. I'm getting you a coney.",
            "*I open my hand and let the ball roll off the table.*")

tracks = track("A1", "The Ball", "Warm from his pocket. Yours tonight.", s1, opn=True) + \
         track("A2", "Halftime", "You finishing isn't the end.", s2) + \
         track("B1", "Number", "One easy. Five done. He's asking.", s3)

TAGS = ["Overstimulation", "Massage Therapist", "Patient Dom", "Kinktober Day 20", "Drop the Ball"]
tagpills = "\n".join(f'            <div style="background-color:#22161F; color:#E3B9D3; border: 1px solid #4E2A44; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

RECORD = ("width: 128px; height: 128px; margin: 0 auto 14px; border-radius: 50%; "
          f"background: radial-gradient(circle, #EFE6DA 0 4%, {PLUM} 5% 30%, #1B171A 31% 33%, transparent 34%), "
          "repeating-radial-gradient(circle, #1B171A 0 2px, #2C262A 3px 4px); "
          "box-shadow: 0 4px 10px rgba(0,0,0,0.35);")

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Esteban Booker - Kinktober Day 20</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0E0B0E; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #181218; border: 1px solid #36263A; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E6DDE2; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #36263A; padding-bottom:15px; margin-bottom:25px; color: #F1E6EC; letter-spacing: 0.5px;">
            It's Halftime
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #A08F99; font-family: Georgia, serif;">
                “Everybody thinks it's the finish line. It's halftime.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Esteban Booker" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #36263A; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#130E13; color: #B3A5AD; padding:20px; flex: 1; min-width: 250px; border:1px solid #36263A; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">An upstairs flat in a North End two-flat, Detroit. Radiator clanking, a record on low, a padded table in the spare room under a plum blanket. Esteban Booker has spent fifteen years learning where people hold things. He owns a studio on Livernois, and none of this happens there. You're not on his books. You're in his house, with a wooden ball in your hand.</span>
            </div>
            <div style="background-color:#130E13; color: #B3A5AD; padding:20px; flex: 1; min-width: 250px; border:1px solid #36263A; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Esteban Booker x Any user<br>
                    Kinktober Day 20: Overstimulation<br>
                    Learn the number, copy a starter into chat.<br>
                    TW: Overstimulation, post-orgasm play, sensation play, dominance (negotiated)<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- RECORD SLEEVE -->
        <div style="margin-top: 35px; background-color: {SLEEVE}; border: 1px solid #D9CCBE; border-top: 8px solid {PLUM}; border-radius: 10px; padding: 22px 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="{RECORD}"></div>
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 8px;">OCT 20 · OVERSTIMULATION</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Side A, Side B</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 18px;">A lot of bass and not much hurry. He'll flip it when it's time.</div>
{tracks}
            <div style="margin-top: 18px; border-top: 1px solid #D9CCBE; padding-top: 14px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">LINER NOTES</span>
                Recorded upstairs, North End. Radiator on percussion. Towel warmer older than his car. Lemon and honey after, and a coney from up the street, eaten in his bed, crumbs and all.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Flip it when you're ready. ~E.B.</div>
        </div>

        <details style="margin-top: 30px; background: #1D161D; padding: 12px 20px; border-radius: 8px; border: 1px solid #36263A; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #46324A; padding-top: 12px; color: #A496A0;">
                Overstimulation. Expect touch that keeps going after release, multiple orgasms, massage and sensation play, a patient dominant with a wicked sense of humor, and full aftercare. All characters are adults. You are never his client, and nothing happens at his studio. Drop the ball, or say stop, and everything stops.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Esteban Booker (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
