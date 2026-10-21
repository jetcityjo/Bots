import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Desmond Karim banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

VELLUM, INK, MUTED, INDIGO, LAMP = "#E8E9E2", "#26272C", "#7C7E80", "#4A3F72", "#C98F1E"

def starter(text):
    return f'''
                        <div style="background: #F8F8F4; border-left: 3px solid {LAMP}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def desmond(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {INDIGO};">Desmond:</strong>&nbsp;“{esc(line)}”</div>'

def detail(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,255,255,0.55); border: 1px solid #C4C6BF; border-radius: 3px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="display: inline-block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {INDIGO}; border: 1.5px solid {INDIGO}; border-radius: 50%; width: 26px; height: 26px; line-height: 26px; text-align: center; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 4px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #D2D4CC; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def rule(left, right):
    return f'<div style="display: flex; gap: 10px; margin-bottom: 6px; color: {INK}; line-height: 1.45; font-size: 0.95em;"><span style="min-width: 92px; font-family: \'Courier New\', Courier, monospace; font-size: 0.85em; letter-spacing: 1px; color: {INDIGO}; font-weight: 700;">{esc(left)}</span><span>{esc(right)}</span></div>'

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F4F4EF; border: 1px dashed #B9BBB3; border-radius: 3px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{desmond(line)}{starter(start)}
                        </div>
                    </details>'''

TAPE = "position: absolute; width: 64px; height: 18px; background: rgba(226,214,170,0.85); box-shadow: 0 1px 2px rgba(0,0,0,0.2);"

s1 = rule("LAMP ON", "Bolt's open. Walk in. He won't stop.") + \
     rule("LAMP OFF", "He's just your neighbor. No game.") + \
     rule("CURTAINS", "Drawn. Always. Nobody else sees.") + \
     rule("COLORS", "Green go on. Yellow slow down or step back.") + \
     rule("RED", "Game over on the spot. Dark for a week.") + \
     rule("MARGINS", "Your limits. Touch only by invitation.") + \
     '<div style="margin-top: 10px;">' + desmond("Green, yellow, red, same as on the paper. Your margins are the margins.") + '</div>' + \
     starter("*I check the transom. Yellow square, lamp on. I fit the spare key in the lock.*")
s2 = desmond("Tuesday. You said you might try a Tuesday. I was starting to think you'd lost the key.") + \
     '<div style="margin-top: 8px;">' + desmond("Before anything else. The door's right there behind you. Either side of it is a right answer, and I mean that. I'd like this side.") + '</div>' + \
     starter("\"You're not even going to stop?\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Distance and angle are yours to set. He asks. He doesn\'t assume.</div>' + \
     choice("Stay in the doorway", "Then that's your sightline. Good one, actually. I'd have put a window right where you're standing.",
            "*I lean on the doorframe and stay right there.* \"Don't mind me.\"") + \
     choice("Tell him what to show you", "Say it however you want. Plainly is fine. I don't embarrass.",
            "\"Slower. And keep your eyes on me while you do it.\"") + \
     choice("Ask to come closer", "Inside your margins, yes. Pull the stool over. Not the drafting one, it rolls.",
            "\"Can I come closer, Desmond? I'm asking.\"")

details = detail("1", "Lamp On", "The terms, as drawn and signed.", s1, opn=True) + \
          detail("2", "The Door", "Either side of it is a right answer.", s2) + \
          detail("3", "Sightlines", "What do you want to see?", s3)

TAGS = ["Caught in the Act", "Exhibitionist", "Architect", "Kinktober Day 22", "Lamp's On"]
tagpills = "\n".join(f'            <div style="background-color:#1C1A26; color:#E8C77A; border: 1px solid #3D3758; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desmond Karim - Kinktober Day 22</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0C0C11; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #14141B; border: 1px solid #2C2B3A; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E2E1E6; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2C2B3A; padding-bottom:15px; margin-bottom:25px; color: #F0EEF4; letter-spacing: 0.5px;">
            He Doesn't Stop
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #9A98A6; font-family: Georgia, serif;">
                “Either side of it is a right answer, and I mean that.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Desmond Karim" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2C2B3A; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#101016; color: #A9A8B3; padding:20px; flex: 1; min-width: 250px; border:1px solid #2C2B3A; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Third floor of a Fort Greene brownstone, across the landing from you. Desmond Karim designs the insides of old buildings for a living, mostly light and who can see what from where. The two of you drew up the rules on tracing paper at his kitchen table and both signed. When the lamp in his transom is on, the bolt is open. You walk in. He doesn't stop.</span>
            </div>
            <div style="background-color:#101016; color: #A9A8B3; padding:20px; flex: 1; min-width: 250px; border:1px solid #2C2B3A; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Desmond Karim x Any user<br>
                    Kinktober Day 22: Caught in the Act<br>
                    Read the drawing, copy a starter into chat.<br>
                    TW: Exhibitionism, voyeurism, masturbation, eye contact play (pre-negotiated)<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- TRACING PAPER -->
        <div style="position: relative; margin-top: 40px; background-color: {VELLUM}; background-image: linear-gradient(rgba(255,255,255,0.35), rgba(255,255,255,0)); border: 1px solid #C4C6BF; border-radius: 2px; padding: 26px 18px 22px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="{TAPE} left: -10px; top: -8px; transform: rotate(-12deg);"></div>
            <div style="{TAPE} right: -10px; top: -8px; transform: rotate(10deg);"></div>
            <div style="margin: 0 auto 14px; width: 120px; height: 34px; background: #FBE7A6; border: 3px solid #3A3328; border-radius: 60px 60px 0 0; box-shadow: 0 0 22px rgba(232,180,60,0.75);"></div>
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 8px;">OCT 22 · CAUGHT IN THE ACT</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">The Agreement</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 18px;">Pencil on trace. Taped inside his closet door. Two signatures.</div>
{details}
            <div style="margin-top: 18px; border-top: 1px solid #C4C6BF; padding-top: 14px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">MARGIN NOTE · ADDED LATER, PENCIL</span>
                <span style="font-family: Georgia, serif; font-style: italic;">ask about the window seat.</span><br>
                Tea after. Mint, too much sugar, his Teta's way.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Nobody gets caught by accident. ~D.K.</div>
        </div>

        <details style="margin-top: 30px; background: #191920; padding: 12px 20px; border-radius: 8px; border: 1px solid #2C2B3A; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #3A394A; padding-top: 12px; color: #9E9DA8;">
                Exhibitionism and voyeurism. Expect a man walked in on mid-act who keeps going, sustained eye contact, calm narration, and touch only by invitation. All characters are adults. The scene is pre-negotiated and signed. Every time, Desmond offers the door first and only goes on once you stay. Green, yellow, red: red ends the game at once and it stays dark for a week. Curtains drawn, and nobody but you ever sees.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Desmond Karim (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
