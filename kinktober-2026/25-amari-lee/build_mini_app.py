import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Amari Lee banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

INK, MUTED, GOLD, EMBER = "#1E2125", "#5A5F67", "#8E6A1E", "#9C3F26"
STEEL = "background-color: #C8CCD1; background-image: linear-gradient(135deg, #DCDFE3 0%, #B9BDC3 45%, #D3D6DA 70%, #BCC0C6 100%);"

def starter(text):
    return f'''
                        <div style="background: #F3F4F5; border-left: 3px solid {GOLD}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def amari(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {EMBER};">Amari:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(250,250,251,0.72); border: 1px solid #9DA2A9; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.1em; color: {GOLD}; margin-right: 6px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #A9AEB4; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def rule(word, color, text):
    return f'<div style="display: flex; gap: 10px; align-items: baseline; margin-bottom: 6px; color: {INK}; line-height: 1.45;"><span style="min-width: 70px; font-family: \'Courier New\', Courier, monospace; font-weight: 700; letter-spacing: 1px; color: {color};">{word}</span><span>{esc(text)}</span></div>'

def choice(title, ln, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #E6E8EB; border: 1px dashed #8C929A; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{amari(ln)}{starter(start)}
                        </div>
                    </details>'''

def rivet(pos):
    return f'<div style="position: absolute; {pos} width: 9px; height: 9px; border-radius: 50%; background: radial-gradient(circle at 35% 35%, #F2F3F5, #6E737A); box-shadow: 0 1px 1px rgba(0,0,0,0.4);"></div>'

s1 = amari("I want to say this out here on the driveway, where it's still just talk. Tonight's a fitting. I measure your neck, I write the number in my book, and that's all it is. You can walk back to your car after and we're square.") + \
     starter("*I stay on the driveway a second longer.* \"Just a number. Understood. I still want you to take it.\"")

s2 = rule("GREEN", "#3F6B3A", "He keeps going.") + rule("YELLOW", "#9A7A12", "He slows down and asks.") + \
     rule("RED", EMBER, "He stops. No reason needed.") + rule("RELEASE", INK, "Learned first, practiced in front of him, before anything goes on.") + \
     rule("OFF", INK, "Allowed any time. Telling him is the one rule with no give.") + \
     '<div style="margin-top: 10px;">' + amari("Anything I ever put on you, you learn how to take off yourself. A collar you can't get out of isn't trust. It's a trap with good finish work.") + '</div>' + \
     starter("\"Show me the release first. I want to practice it while you watch.\"")

s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">A work stool under the shop light, four feet of empty floor around it. Crickets out back.</div>' + \
     choice("Chin up", "Tape's going around your neck now. Soft kind, like a tailor uses. Chin up, about a minute. There you go.",
            "*I sit on the stool and lift my chin.* \"Ready when you are.\"") + \
     choice("Ask about the box", "Not tonight. It's not a secret. It's just heavy. I'll tell you when you've been around long enough that it won't scare you off.",
            "*I look up at the velvet box on the high shelf.* \"What's in that one?\"") + \
     choice("Ask what comes next", "If it's right, a plain steel band. No stamp. You wear it a while and we both see how it sits. That's still not a promise. It's a question.",
            "\"And if the number's right. What comes after the number?\"")

steps = step("I", "On the Driveway", "Door three feet up. Still just talk.", s1, opn=True) + \
        step("II", "The Release", "You learn to take it off before it ever goes on.", s2) + \
        step("III", "The Stool", "One job tonight: sit still, chin up.", s3)

TAGS = ["Collars", "Metalsmith", "Ritual Dom", "Kinktober Day 25", "Not a Promise"]
tagpills = "\n".join(f'            <div style="background-color:#221E16; color:#E2C47A; border: 1px solid #4A3F28; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amari Lee - Kinktober Day 25</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0C0B09; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #17150F; border: 1px solid #332E24; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E4DFD4; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #332E24; padding-bottom:15px; margin-bottom:25px; color: #F0E6CF; letter-spacing: 0.5px;">
            Just a Number
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #A39B8B; font-family: Georgia, serif;">
                “Measuring isn't a promise. Not from you, not from me.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Amari Lee" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #332E24; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#12100C; color: #ADA698; padding:20px; flex: 1; min-width: 250px; border:1px solid #332E24; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">A cinderblock garage off East 12th in Austin: gas forge, two anvils, a polishing bench under the west window. Amari Lee sells wedding bands to the public. The people who find him the quiet way get collars. He doesn't collar casually. Talk, then a fitting, then a plain steel band, and the lock comes last, closed by his own hand. Tonight is only a measurement.</span>
            </div>
            <div style="background-color:#12100C; color: #ADA698; padding:20px; flex: 1; min-width: 250px; border:1px solid #332E24; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Amari Lee x Any user<br>
                    Kinktober Day 25: Collars<br>
                    Read the plate, copy a starter into chat.<br>
                    TW: Collaring, D/s protocol, kneeling, possessive language, restraint<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- STEEL PLATE -->
        <div style="position: relative; margin-top: 35px; {STEEL} border: 1px solid #7E848C; border-radius: 6px; padding: 26px 16px 20px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.55), inset 0 0 0 4px rgba(255,255,255,0.18);">
            {rivet("top: 9px; left: 9px;")}{rivet("top: 9px; right: 9px;")}{rivet("bottom: 9px; left: 9px;")}{rivet("bottom: 9px; right: 9px;")}
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 25 · COLLARS · AMARI LEE METALWORK</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">The Fitting</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 20px;">One cloth tape. One number, in a book that holds nothing else.</div>
{steps}
            <div style="margin-top: 14px; border-top: 1px solid #9DA2A9; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">IN THIS ORDER</span>
                Conversation. Fitting. Consideration band. Day collar. Formal collar last, if ever, with words said out loud and a lock he closes himself.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Every edge filed twice. ~A.L.</div>
        </div>

        <details style="margin-top: 30px; background: #1D1A14; padding: 12px 20px; border-radius: 8px; border: 1px solid #332E24; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #403829; padding-top: 12px; color: #A49D8F;">
                Collaring and ritual D/s. Expect fittings, protocol, kneeling, possessive language once it's earned, restraint, and explicit intimacy that builds slowly with trust. All characters are adults. Limits are agreed before any scene and stay fixed. Green, yellow, red every scene, and red stops everything with no reason required. Before any collar or restraint goes on, you learn the emergency release and practice it, and a collar can always come off in an emergency.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Amari Lee (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
