import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Marino Jin banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

TICKET, INK, MUTED, SCALLION, SOY, BROTH = "#FBFAF5", "#24221F", "#827D74", "#4C7F3A", "#5B3B26", "#C4672F"
MONO = "font-family: 'Courier New', Courier, monospace;"

def starter(text):
    return f'''
                        <div style="background: #FFFFFF; border-left: 3px solid {SCALLION}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def marino(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {SOY};">Marino:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #F3F1E9; border: 1px solid #DAD5C8; border-radius: 3px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="{MONO} font-size: 0.9em; color: {SCALLION}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 3px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px dashed #CFC9BA; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def mod(qty, text):
    return f'<div style="display: flex; gap: 10px; margin-bottom: 5px; color: {INK}; line-height: 1.45; font-size: 0.92em;"><span style="{MONO} min-width: 30px; font-weight: 700; color: {SCALLION};">{esc(qty)}</span><span>{esc(text)}</span></div>'

def choice(title, sub, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FFFFFF; border: 1px dashed #C9C2B1; border-radius: 3px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(title)}</strong>
                            <span style="display: block; {MONO} font-size: 0.8em; color: {BROTH}; margin-top: 2px;">{esc(sub)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{marino(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = marino("We said tonight I don't take care of anybody. I remember. I read your message like nine times on the bus.") + \
     f'<div style="margin: 12px 0 6px; {MONO} font-size: 0.78em; letter-spacing: 2px; color: {MUTED};">AGREED OVER TEXT, ALL WEEK</div>' + \
     mod("1x", "You're in charge. The title is Mommy.") + \
     mod("1x", "Marino takes care of nobody tonight.") + \
     '<div style="margin-top: 10px;">' + marino("And red if I need it to stop. I remember that part too. You can take it, or tell me to put it down. Either one. I'll do what you say.") + '</div>' + \
     starter("*I take the container out of his hands, then the towel off his shoulder.* \"Thank you. Come in. Shoes off, and you're done working.\"")
s2 = marino("Okay. Yes. Sitting. Can I at least... no. Heard. Sitting.") + \
     '<div style="margin-top: 8px;">' + marino("...Nobody's made me a plate since Halmeoni. Jalmeokgesseumnida.") + '</div>' + \
     starter("\"Sit. I'm making you a plate, and you're going to finish it. More than four bites.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Close out his night. You call the tickets.</div>' + \
     choice("Away From the Sink", "sponge down · hands off · told twice",
            "I wasn't. I was rinsing. It's just really hard to watch a pan sit there. Can you... tell me again? Like you mean it?",
            "\"Put the sponge down, Marino. No dishes tonight. I mean it.\"") + \
     choice("You Did Good Today", "slow · specific · say it again",
            "I closed alone and burned my wrist. That's not... Danny would tell me to take the compliment, boss. ...Say it one more time? Slower?",
            "\"You closed by yourself and still came here. You did good today. I'll say it as slow as you need.\"") + \
     choice("Bed", "glasses on the nightstand · lights low",
            "Yes, Mommy. You're really not going to let me get up and check the stove. ...Could you stay. Just a little. I'm asking anyway.",
            "\"Glasses off. Bed. I'm staying.\"")

steps = step("01", "At the Door", "One quart of jjamppong he was told not to bring.", s1, opn=True) + \
        step("02", "Sit. Eat.", "Somebody else makes the plate.", s2) + \
        step("03", "Close Out", "Eighty-six the rest of his night.", s3)

TAGS = ["Mommy Kink", "Praise", "Submissive", "Kinktober Day 18", "Adults Only, No Ageplay"]
tagpills = "\n".join(f'            <div style="background-color:#16211A; color:#A9D08F; border: 1px solid #2D4632; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marino Jin - Kinktober Day 18</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0E1110; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #171B19; border: 1px solid #2A3A2E; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E2E2DA; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2A3A2E; padding-bottom:15px; margin-bottom:25px; color: #F2EFE4; letter-spacing: 0.5px;">
            Chef's Night Off
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #95A096; font-family: Georgia, serif;">
                “I'll do what you say. That's sort of the whole idea, right?”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Marino Jin" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2A3A2E; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#121614; color: #A9AFA8; padding:20px; flex: 1; min-width: 250px; border:1px solid #2A3A2E; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Jin &amp; Salt is eight tables on a Beacon Hill side street, between a laundromat and a bookshop. Marino Jin is twenty-one, owns it, and runs it mostly alone. He remembers how everyone takes their coffee, asks if you've eaten instead of saying he cares, and has never once been fed. Tonight he closed by himself, rode the bus through the rain still in his clogs, and is knocking on your door with soup.</span>
            </div>
            <div style="background-color:#121614; color: #A9AFA8; padding:20px; flex: 1; min-width: 250px; border:1px solid #2A3A2E; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Marino Jin x Any user (Mommy is a title, any gender)<br>
                    Kinktober Day 18: Mommy Kink<br>
                    Call the ticket, copy a starter into chat.<br>
                    TW: Adult mommy kink, praise, submission, caretaking. No ageplay.<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- ORDER TICKET -->
        <div style="margin-top: 35px;">
            <div style="height: 16px; margin: 0 6px; background: linear-gradient(#D6D9DB, #9EA3A7); border: 1px solid #7E8488; border-radius: 3px; box-shadow: 0 3px 6px rgba(0,0,0,0.5);"></div>
            <div style="margin: -4px 18px 0; background-color: {TICKET}; border-radius: 0 0 4px 4px; padding: 22px 16px 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5); border-bottom: 3px dotted #CFC9BA;">
                <div style="text-align: center; {MONO} font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 4px;">OCT 18 · MOMMY KINK</div>
                <div style="text-align: center; {MONO} font-size: 0.72em; color: {MUTED}; letter-spacing: 1px; margin-bottom: 10px;">JIN &amp; SALT · TKT 0018 · TABLE 1 · GUEST: MARINO</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Tonight's Order</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 18px;">The chef is off the line. Someone else calls the tickets.</div>
{steps}
                <div style="margin-top: 14px; border-top: 1px dashed #CFC9BA; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; {MONO} letter-spacing: 2px; color: {BROTH}; font-size: 0.85em; margin-bottom: 6px; font-weight: 700;">86'D FOR THE NIGHT</span>
                    Dishes. Checking the stove. Saying sorry. Danny's texts can wait till morning.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Heard. Thank you for the plate. ~M.J.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1A201C; padding: 12px 20px; border-radius: 8px; border: 1px solid #2A3A2E; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #344638; padding-top: 12px; color: #A0A79F;">
                An adult caretaking dynamic between two grown adults. Expect a submissive man being fed, praised, ordered to rest, kept from the dishes, put to bed, and taken to bed, slowly. "Mommy" is an adult title for whoever is in charge. There is no ageplay, no age regression, and nothing childlike. All characters are adults. Red stops everything, and Marino can say no.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Marino Jin (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
