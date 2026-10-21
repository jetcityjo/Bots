import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Booker Desmond banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

KRAFT, INK, MUTED, SADDLE, DUST, SAGE = "#C9A97C", "#2A1E12", "#5E4A33", "#7A4A24", "#B8913A", "#5F6B4E"

def starter(text):
    return f'''
                        <div style="background: #F3E9D8; border-left: 3px solid {SADDLE}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: #8A7458; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def booker(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {SADDLE};">Booker:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #E8D8BE; border: 1px solid #A88A5F; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.1em; color: {SADDLE}; margin-right: 6px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #C2A77F; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def note(text):
    return f'<div style="font-family: \'Courier New\', Courier, monospace; color: {INK}; font-size: 0.92em; line-height: 1.5; padding: 2px 0 2px 10px; border-left: 2px solid {DUST}; margin-bottom: 4px;">{esc(text)}</div>'

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F1E5D0; border: 1px dashed #A88A5F; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{booker(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = f'<div style="margin-bottom: 8px; font-family: \'Courier New\', Courier, monospace; font-size: 0.8em; letter-spacing: 2px; color: {MUTED};">POCKET NOTEBOOK · TUESDAY CALL</div>' + \
     note("Green. Go on.") + note("Yellow. Slow down.") + note("Red. Stops everything.") + note("Whoa. Stops everything. Mine too.") + \
     note("Your limits. Wrote down. Law.") + \
     '<div style="margin-top: 10px;">' + booker("What you told me's wrote down in here. Ain't nothing happens past it.") + '</div>' + \
     starter("*I sit down on the cooler.* \"Green. I read it back to myself on the drive out.\"")
s2 = booker("That's horsehair. That's what you get. Not the boots. Not yet.") + \
     '<div style="margin-top: 8px;">' + booker("You missed the welt. Nah, go on and find it. I'll wait.") + '</div>' + \
     starter("*I take the brush handle first and start on the dust at the toe, slow.*")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Brush, then soap and rag, then your knees. Only as far as he allows.</div>' + \
     choice("Wait for it", "You can ask. You did. Now wait.",
            "*I set the rag down, kneel in the dust beside the feed sack, and wait.*") + \
     choice("Ask for the other boot", "That one's still on my foot for a reason. Ask me like you mean it.",
            "\"The right one, Booker. Please. I'll go slow.\"") + \
     choice("Whoa", "Whoa. Boot's down. You're done working. Coat's going around your shoulders, and there's water right there.",
            "\"Whoa.\"")

steps = step("I", "Wrote Down", "Green, yellow, red. And whoa.", s1, opn=True) + \
        step("II", "Dirt First", "The brush. Handle first. Not your hands.", s2) + \
        step("III", "Earned", "Soap, rag, knees in the dust.", s3)

TAGS = ["Boot Worship", "Bronc Rider", "Earned Attention", "Kinktober Day 21", "Whoa Means Stop"]
tagpills = "\n".join(f'            <div style="background-color:#231B10; color:#DDBE73; border: 1px solid #554227; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booker Desmond - Kinktober Day 21</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0D0B08; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #16120C; border: 1px solid #3A2F1E; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E7DECF; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #3A2F1E; padding-bottom:15px; margin-bottom:25px; color: #F1E5CC; letter-spacing: 0.5px;">
            Dirt First
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #A39479; font-family: Georgia, serif;">
                “Take your time. I got all night.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Booker Desmond" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #3A2F1E; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#120F0A; color: #B2A58F; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2F1E; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Saturday night behind the stock pens at the Garvin County fairgrounds. Booker Desmond placed second in the saddle bronc and hasn't looked at the check. He's on his camper step under the sodium lights, one boot off on a feed sack, one still on. Handmade in Guthrie, eleven months' wait, resoled four times. Nobody gets handed them. You earn the brush first.</span>
            </div>
            <div style="background-color:#120F0A; color: #B2A58F; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2F1E; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Booker Desmond x Any user<br>
                    Kinktober Day 21: Boot Worship<br>
                    Take the brush, copy a starter into chat.<br>
                    TW: Boot worship, kneeling, service, slow dominance, light humiliation (negotiated)<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- BOOTMAKER'S SACK -->
        <div style="margin-top: 35px; background-color: {KRAFT}; background-image: linear-gradient(rgba(255,255,255,0.08), rgba(0,0,0,0.06)); border: 1px solid #9C7E55; border-radius: 4px; padding: 22px 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="text-align: center; margin: 0 auto 12px; max-width: 260px; border: 2px solid {SADDLE}; border-radius: 50% / 40%; padding: 8px 10px; color: {SADDLE}; font-family: Georgia, serif; font-size: 0.8em; letter-spacing: 2px; line-height: 1.4;">
                ELLIS TOOMBS · BOOTMAKER<br><span style="font-size: 0.85em;">GUTHRIE, OKLA. · MADE BY HAND</span>
            </div>
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 8px;">OCT 21 · BOOT WORSHIP</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Earned, Not Handed</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 18px;">Traced on this sack in pencil. Saddle brown calfskin, stacked heel, one row of gold stitching.</div>
{steps}
            <div style="margin-top: 18px; border-top: 1px solid #9C7E55; padding-top: 14px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">SUNDAY NIGHTS</span>
                Brush the arena off before the ice. Oil Sundays. Mama calls from Boley and asks if he's eating. He says yes.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Whoa means stop. Same as anything I ride. ~B.D.</div>
        </div>

        <details style="margin-top: 30px; background: #1B160E; padding: 12px 20px; border-radius: 8px; border: 1px solid #3A2F1E; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #4A3C26; padding-top: 12px; color: #A69A85;">
                Boot worship. Expect kneeling, boot care as ritual, service, slow pressure-and-release dominance, light teasing humiliation, and quiet aftercare. All characters are adults. Limits were settled by phone before tonight and are law. Green, yellow, red, and whoa: red or whoa stops everything at once, and Booker can call whoa himself. No bystanders, ever.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Booker Desmond (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
