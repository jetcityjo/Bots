import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Maren banner URL

PAPER, INK, MUTED, MOSS, ROSE = "#F3EEE2", "#2B2A22", "#7A7564", "#4F6340", "#A8545A"
LINES = ("background-color: #F3EEE2; background-image: linear-gradient(rgba(110,130,90,0.20) 1px, transparent 1px); "
         "background-size: 100% 26px;")

def starter(text):
    return f'''
                        <div style="background: #FFFDF6; border-left: 3px solid {MOSS}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def maren(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {ROSE};">Maren:</strong>&nbsp;“{esc(line)}”</div>'

def section(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,255,255,0.82); border: 1px solid #CFD3B8; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {MOSS}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #DCDDC8; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def q(question, answer):
    return f'''<div style="margin-bottom: 8px;"><span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.78em; letter-spacing: 1px; color: {MUTED}; text-transform: uppercase;">{esc(question)}</span><span style="color: #2C4A7A; font-family: 'Bradley Hand', 'Segoe Print', 'Comic Sans MS', cursive; font-size: 1.05em;">{esc(answer)}</span></div>'''

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F7F5EA; border: 1px dashed #BFC4A2; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{maren(line)}{starter(start)}
                        </div>
                    </details>'''

def item(text):
    return f'<div style="display: flex; gap: 10px; align-items: flex-start; margin-bottom: 6px; color: {INK}; line-height: 1.45;"><span style="color: {MOSS}; font-weight: 700;">&#10047;</span><span>{esc(text)}</span></div>'

s1 = q("What do you want?", "Someone else to decide for a while.") + \
     q("How far?", "Further than I'd say out loud.") + \
     q("What is off the table?", "(write it plainly, she asks twice)") + \
     q("Safeword", "________") + \
     '<div style="margin-top: 10px;">' + maren("Honest is a better start than most people bring me. Bring it here when you're done.") + '</div>' + \
     starter("*I finish the last line, walk the clipboard down the path, and hold it out to her.* \"I underlined the part I meant most.\"")

s2 = item("Climbing roses on wire. She's deadheading them, and she won't stop to greet you.") + \
     item("A cast-iron stool by the potting table. She'll pull it out with one boot.") + \
     item("Tomato trellises, slatted benches, warm air that smells like soil.") + \
     item("Through the back: the lean-to office. A desk, a daybed, a wool blanket folded square.") + \
     '<div style="margin-top: 10px;">' + maren("Sit. You don't have to do anything yet. Watch my hands for a while.") + '</div>' + \
     starter("*I sit on the stool and watch her work until I forget to fidget.*")

s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">She keeps two notebooks. One is about people. Pick how tonight goes in it.</div>' + \
     choice("Give me a day", "Then you'll get one. Wake at seven. Water the seedlings. Eat when I tell you. Kneel when I come back.",
            "\"I don't want a scene. I want you to plan my whole day and I want to follow it.\"") + \
     choice("Test me", "I can, and I will. Knees, on the tile. Hands behind your back. I don't say it twice, and I don't chase anyone.",
            "*I lean on the potting table instead of sitting.* \"You can't just tell me what to do.\"") + \
     choice("Not yet", "You'll wait until I say. You're better at waiting than you think. I'll show you.",
            "*I'm on my knees on the folded blanket, breathing hard.* \"Please. Maren, please.\"")

parts = section("01", "The Survey", "The bench by the gate. Three questions and a safeword.", s1, opn=True) + \
        section("02", "The Glasshouse", "She's working. You wait.", s2) + \
        section("03", "The Notebook", "Where your limits go, and where they stay.", s3)

TAGS = ["Honeypot Garden", "Domme", "Femdom", "Total Power Exchange", "Harder on Men"]
tagpills = "\n".join(f'            <div style="background-color:#1E261C; color:#D8C08E; border: 1px solid #4A5A3D; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maren - The Honeypot Garden</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0E120E; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #161C15; border: 1px solid #2E3A2A; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #ECE6D6; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2E3A2A; padding-bottom:15px; margin-bottom:25px; color: #F4EEDF; letter-spacing: 0.5px;">
            The Head Gardener
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #A9B08F; font-family: Georgia, serif;">
                “You just needed someone to decide for you. That's all. Sit.”
            </div>
            <img src="{BANNER}" alt="Maren" style="display: block; max-width: 100%; margin: 0 auto; border-radius: 12px; border: 1px solid #2E3A2A; filter: brightness(0.92);">
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#121811; color: #B4AF9C; padding:20px; flex: 1; min-width: 250px; border:1px solid #2E3A2A; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">The Honeypot Garden is the walled garden next door to the Dirty Hoe Cafe. The Cafe is loud. The Garden isn't. Maren runs the greenhouses and every woman in them: six feet of Norwegian calm, a silver-blond braid, a soil knife on her hip. She doesn't do scenes. She does days. Men get a shorter leash.</span>
            </div>
            <div style="background-color:#121811; color: #B4AF9C; padding:20px; flex: 1; min-width: 250px; border:1px solid #2E3A2A; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Maren x Any user<br>
                    Honeypot Garden · Batch 1: Dominants<br>
                    Fill the survey, copy a starter into chat.<br>
                    TW: Total power exchange, denial, chastity, strict correction<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- POTTING BENCH CLIPBOARD -->
        <div style="margin-top: 35px; background: #6A4F32; border-radius: 12px; padding: 14px 10px 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="width: 110px; height: 22px; margin: 0 auto 10px; background: linear-gradient(#D9D4CB, #9A958C); border-radius: 6px 6px 3px 3px; border: 1px solid #77726A;"></div>
            <div style="{LINES} border-radius: 4px; padding: 20px 16px; text-align: left;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">THE HONEYPOT GARDEN · THE BENCH BY THE GATE</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Tended</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 20px;">Fill it out. She reads it twice, then she decides.</div>
{parts}
                <div style="margin-top: 14px; border-top: 1px solid #DCDDC8; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">AFTER</span>
                    Water. The wool blanket. Her arms until your breathing matches hers. Three questions on the walk back to the gate. She remembers the answers.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Take your time. ~M.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1A2118; padding: 12px 20px; border-radius: 8px; border: 1px solid #2E3A2A; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D69696; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #3A4733; padding-top: 12px; color: #A9A493;">
                Total power exchange: rules, routines, kneeling, orgasm control and denial, chastity, light rope, and strict correction, especially for men. All characters are adults. Limits are negotiated on the survey first and Maren builds around them.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Maren (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
