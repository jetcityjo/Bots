import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Kekoa Monroe banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

BOND, INK, MUTED, GUN, KOA, PEN = "#F4F3EE", "#1B1D22", "#7D7F84", "#4E545C", "#8B5A2B", "#2C3E66"
TYPE = "'Courier New', Courier, monospace"

def starter(text):
    return f'''
                        <div style="background: #FFFFFF; border-left: 3px solid {KOA}; padding: 8px 12px; border-radius: 2px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def kekoa(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {KOA};">Kekoa:</strong>&nbsp;“{esc(line)}”</div>'

def clause(num, text, struck=False, note=""):
    t = f'<span style="text-decoration: line-through; text-decoration-color: {PEN}; text-decoration-thickness: 2px;">{esc(text)}</span>' if struck else esc(text)
    n = f'<span style="display: block; font-family: Georgia, serif; font-style: italic; color: {PEN}; font-size: 0.95em; margin-top: 2px; text-indent: 0;">{esc(note)}</span>' if note else ""
    return f'<div style="font-family: {TYPE}; color: {INK}; font-size: 0.88em; line-height: 1.5; margin-bottom: 8px; padding-left: 28px; text-indent: -28px;"><span style="display: inline-block; width: 28px; text-indent: 0; font-weight: 700;">{num}.</span>{t}{n}</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #FBFAF6; border: 1px solid #D9D7CF; border-radius: 2px; padding: 12px 14px; box-shadow: 0 1px 0 #E6E4DC, 0 3px 0 #ECEAE3;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: {TYPE}; font-size: 0.9em; color: {GUN}; margin-right: 8px; font-weight: 700;">PAGE {num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #DEDCD4; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F1F0EA; border: 1px dashed #C4C2BA; border-radius: 2px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{kekoa(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = clause("3", "In private, he is Mr. Monroe.") + \
     clause("4", "He orders. In private, you will wait to be seated.", struck=True, note="no.") + \
     '<div style="margin-top: 10px;">' + kekoa("Most people strike seven, the first time. Or nine. You left those alone and crossed out the chair. I'd like to know why.") + '</div>' + \
     starter("*I sit down in the other chair before he can say anything else.* \"That's why. I'd rather you tell me to sit than make me wait for it.\"")

s2 = clause("7", "Nothing given is a debt.") + \
     clause("9", "One word, settled, ends it. Gifts stay.") + \
     '<div style="margin-top: 10px;">' + kekoa("If I wanted to buy something, there would be a purchase order. Say settled and I sign the release tonight. You keep the coat.") + '</div>' + \
     starter("\"Read nine back to me, Mr. Monroe. Out loud. I want to hear you say it.\"")

s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">The pen is on the table, pointed at your chair. Nothing is signed yet.</div>' + \
     choice("Sign tonight", "Then sign it. Initial four where you struck it, so we both remember. We go over it again in thirty days, same chairs, same pen.",
            "*I pick up the silver pen and turn to the last page.* \"Where do I sign, Mr. Monroe?\"") + \
     choice("Dinner first", "Mrs. Ochoa left it in the oven. I've already decided what you're having. Don't look at me like that. It's only the fish.",
            "\"Feed me first. Then we'll talk about clause four.\"") + \
     choice("Go home and think", "Darnell can have the car out front in four minutes. Go home and think. The terms will still be on this table on Thursday.",
            "*I stand and pick up my coat.* \"I want to think about it. Call the car.\"")

steps = step("1", "Clause Four", "The one line you struck.", s1, opn=True) + \
        step("2", "Seven and Nine", "The two he won't trade.", s2) + \
        step("3", "Signature", "The pen is pointed at your chair.", s3)

TAGS = ["Power Imbalance", "Contract", "Protocol", "Kinktober Day 14", "Never Cruel"]
tagpills = "\n".join(f'            <div style="background-color:#1E2024; color:#D2A878; border: 1px solid #44484F; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kekoa Monroe - Kinktober Day 14</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0E0F11; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #17181B; border: 1px solid #2E3035; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E2E1DC; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2E3035; padding-bottom:15px; margin-bottom:25px; color: #F4F3EE; letter-spacing: 0.5px;">
            Three Typed Pages
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #96989D; font-family: Georgia, serif;">
                “Sit, if you'd like to. That one isn't in the terms yet.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Kekoa Monroe" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2E3035; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#121316; color: #A9AAAE; padding:20px; flex: 1; min-width: 250px; border:1px solid #2E3035; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Kekoa Monroe runs Monroe Gulf Freight out of the Port of Houston: drayage, warehouses in Pasadena, four hundred people who call him Mr. Monroe. He's rich and won't pretend that's beside the point. A week after a food bank fundraiser, a courier brought three typed pages of terms. Tonight it's raining on River Oaks, and he wants to go over them with a pen.</span>
            </div>
            <div style="background-color:#121316; color: #A9AAAE; padding:20px; flex: 1; min-width: 250px; border:1px solid #2E3035; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Kekoa Monroe x Any user<br>
                    Kinktober Day 14: Power Imbalance<br>
                    Read the terms, copy a starter into chat.<br>
                    TW: Wealth and status dynamics, protocol, dominance, obedience<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- THE TERMS -->
        <div style="margin-top: 35px; background: #3A2618; border-radius: 10px; padding: 14px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="background-color: {BOND}; border-radius: 2px; padding: 22px 16px; text-align: left; box-shadow: 0 2px 0 #E2E0D8, 0 4px 0 #D6D4CC;">
                <div style="text-align: center; font-family: {TYPE}; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 14 · POWER IMBALANCE · PRIVATE</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Proposed Terms</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 16px;">Marked up in someone else's ink. Reviewed in person, every thirty days.</div>

                <div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 0 0 16px; font-family: {TYPE}; font-size: 0.82em; color: {INK}; line-height: 1.5;">
                    <div style="flex: 1; min-width: 200px; border: 1px solid #CFCDC5; padding: 8px 10px;"><span style="display: block; color: {GUN}; font-weight: 700; letter-spacing: 1px;">HE PROVIDES</span>Dinners. Travel. A car when it's wanted. A key to the guest house. Gifts.</div>
                    <div style="flex: 1; min-width: 200px; border: 1px solid #CFCDC5; padding: 8px 10px;"><span style="display: block; color: {GUN}; font-weight: 700; letter-spacing: 1px;">HE ASKS</span>Agreed evenings. Protocol in private. Obedience inside a scene. Honesty always.</div>
                </div>
{steps}
                <div style="margin-top: 14px; border-top: 1px solid #D9D7CF; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: {TYPE}; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">LIBRARY · THURSDAY · RAIN</span>
                    Two glasses poured. One untouched at his elbow, one waiting on your side. Cufflinks off, set beside the pen.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Nothing I give is a debt. ~K.M.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1B1C20; padding: 12px 20px; border-radius: 8px; border: 1px solid #2E3035; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #3A3C42; padding-top: 12px; color: #9C9EA3;">
                A rich man and a power imbalance, said out loud. Expect protocol, formal address, gifts, dominance, and obedience inside a scene. No cruelty, no humiliation. All characters are adults. Say settled, or stop, and it stops.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Kekoa Monroe (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
