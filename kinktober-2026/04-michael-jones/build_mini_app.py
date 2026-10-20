import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Michael banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

BRASS, PAPER, INK, MUTED, OX = "#C9A45C", "#EFE6D2", "#2B211A", "#857560", "#6E1F1F"

def starter(text):
    return f'''
                        <div style="background: #F7F1E3; border-left: 3px solid {OX}; padding: 8px 12px; border-radius: 4px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def michael(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {OX};">Michael:</strong> “{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #E6DABF; border: 1px solid #CBB98F; border-radius: 6px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.1em; color: {OX}; margin-right: 6px;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-left: 6px;">· {esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #CBB98F; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def rule(n, text):
    return f'<div style="display: flex; gap: 10px; margin-bottom: 8px; color: {INK}; line-height: 1.5;"><span style="font-family: Georgia, serif; color: {OX}; font-weight: 700; min-width: 18px;">{n}.</span><span>{esc(text)}</span></div>'

def task(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F2EBDA; border: 1px dashed #B8A57C; border-radius: 6px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{michael(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = michael("Shoulders back. Chin up. Hands at your sides, still. I'll wait.") + \
     starter("*I stand in front of his desk, straighten my shoulders, and keep my eyes on him.* \"Good evening, Sir.\"")
s2 = rule("I", "Your eyes stay on me unless I tell you otherwise.") + \
     rule("II", "You answer what I ask, fully and accurately, and nothing more.") + \
     rule("III", "Red is never disobedience. Everything stops, and you are not punished for it. Ever.") + \
     '<div style="margin-top: 10px;">' + michael("The third rule protects you from me. Don't forget it exists.") + '</div>' + \
     starter("\"One. My eyes stay on you. Two. I answer fully and accurately. Three. Red is never disobedience.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">He assigns the first task. Choose which one he gives you.</div>' + \
     task("Pour", "Two fingers of the scotch. Neat. Bring it to me with both hands and don't spill.",
          "*I pour two fingers of scotch, neat, and carry it to him with both hands.* \"Your drink, Sir.\"") + \
     task("Kneel", "On the rug beside my chair. Back straight. You'll stay there until I'm done reading.",
          "*I kneel on the rug beside his chair and wait.*") + \
     task("Ask", "You have one question tonight. Make it a good one. I'll answer it honestly.",
          "\"Sir, may I ask my one question?\"")

steps = step("I", "Inspection", "he looks before he speaks", s1, opn=True) + \
        step("II", "The Rules", "recite them on request", s2) + \
        step("III", "Service", "the first task", s3)

TAGS = ["Master/Slave", "Protocol", "Silver Fox", "Kinktober Day 4", "Red Is Never Disobedience"]
tagpills = "\n".join(f'            <div style="background-color:#2A1A16; color:{BRASS}; border: 1px solid #5A2E26; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Michael Jones - Kinktober Day 4</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #100B09; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #1C1411; border: 1px solid #3A2620; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E6DCCD; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #3A2620; padding-bottom:15px; margin-bottom:25px; color: #F2E9DA; letter-spacing: 0.5px;">
            The Door Is Locked. Stand Up Straight.
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #9E8C78; font-family: Georgia, serif;">
                “You asked to serve me. Tonight we find out if you can carry it.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Michael Jones" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #3A2620; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 28%; max-width: 180px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#150F0D; color: #B3A491; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2620; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Twenty years of turning chaos into clockwork. A study with the books arranged by height, a decanter on a silver tray, and a leather collar in the top drawer that nobody has worn in years. Michael Jones doesn't raise his voice. He doesn't have to.</span>
            </div>
            <div style="background-color:#150F0D; color: #B3A491; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2620; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Michael Jones x Any user<br>
                    Kinktober Day 4: Master/Slave<br>
                    Learn the house, copy a starter into chat.<br>
                    TW: Master/slave, protocol, consensual sadism<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- HOUSE LEDGER -->
        <div style="margin-top: 35px; background-color: {PAPER}; border: 1px solid #CBB98F; border-top: 6px solid {OX}; border-radius: 10px; padding: 22px 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 8px;">OCT 04 · MASTER/SLAVE</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Rules of the House</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 22px;">Spoken once. Recited on request.</div>
{steps}
            <div style="margin-top: 18px; border-top: 1px solid #CBB98F; padding-top: 14px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">THE TOP DRAWER</span>
                The collar stays where it is. It comes out when it's earned, and not one night before.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Again tomorrow. Seven o'clock. ~M.J.</div>
        </div>

        <details style="margin-top: 30px; background: #231915; padding: 12px 20px; border-radius: 8px; border: 1px solid #3A2620; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #4A332B; padding-top: 12px; color: #A8998A;">
                Michael is a strict Master. Expect master/slave protocol, discipline, consensual sadism inside negotiated limits, and references to a past relationship that ended badly. All characters are adults. Everything is negotiated, and red stops everything with no penalty.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Michael Jones (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
