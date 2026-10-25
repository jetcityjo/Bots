import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Malik Reyes banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

# Yellowed fight poster off Tito's wall: newsprint, poster blue, poster red, canvas grey
POSTER, INK, MUTED, BLUE, RED, CANVAS = "#ECDDB6", "#1D1C1A", "#7C715C", "#284A8A", "#B8352A", "#D8D2C4"

def starter(text):
    return f'''
                        <div style="background: #FBF6E8; border-left: 3px solid {RED}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def malik(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {BLUE};">Malik:</strong>&nbsp;“{esc(line)}”</div>'

def tale(left, label, right):
    return (f'<div style="display: flex; align-items: baseline; margin-bottom: 4px; font-size: 0.88em; color: {INK};">'
            f'<span style="flex: 1; text-align: right; font-weight: 700;">{esc(left)}</span>'
            f'<span style="min-width: 92px; text-align: center; font-family: \'Courier New\', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 1px;">{esc(label)}</span>'
            f'<span style="flex: 1; text-align: left; font-weight: 700;">{esc(right)}</span></div>')

def rnd(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(251,246,232,0.85); border: 2px solid {INK}; border-radius: 2px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: Georgia, 'Times New Roman', serif; font-weight: 700; font-size: 0.95em; color: {RED}; margin-right: 8px; letter-spacing: 1px;">ROUND {num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px; text-transform: uppercase;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #BFAF8A; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def choice(title, note, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F4EBD2; border: 1px dashed #A8987A; border-radius: 2px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(title)}</strong>
                            <span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {BLUE}; margin-top: 2px;">{esc(note)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{malik(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = tale("49", "AGE", "Late 20s") + tale("Reading glasses", "EQUIPMENT", "None") + tale("Knees, weather", "FORECAST", "Clear") + \
     tale("0 wins", "RECORD", "3 weeks undefeated") + \
     '<div style="margin-top: 10px;">' + malik("You deserve somebody with more years in front of him than behind him. That's the argument. And I know. I been making it for three weeks and losing every round.") + '</div>' + \
     starter("*I lean on the ring apron next to him.* \"Make the argument again. I've got an answer ready.\"")
s2 = f'<div style="margin: 0 0 6px; font-family: \'Courier New\', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 1px;">THE WRAPS</div>' + \
     f'<div style="color: {INK}; line-height: 1.6;">Same as fight night: thumb loop, flat across the back of the hand, snug, never tight. Only here it\'s both wrists, and he\'s the one tying them off. In for four, out for four. Hands up. Look at him.</div>' + \
     '<div style="margin-top: 10px;">' + malik("You say stop, I stop. Rest of the time, breathe and look at me.") + '</div>' + \
     starter("*I hold out my wrists.* \"Wrap them like you'd wrap mine for a fight.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">His call is already made. He just argues for exercise. Now yours.</div>' + \
     choice("Three Blocks", "his place", "Okay. Get your bag. Lemme hit the last light.",
            "\"Your place. Three blocks. Get the light, Malik.\"") + \
     choice("The Train", "and Tuesday at six", "Then I walk you to the train, and I still see you Tuesday at six, and we never talk about this. You get to pick that. I mean it.",
            "\"Walk me to the train tonight. Ask me again Tuesday.\"") + \
     choice("Stop Arguing", "c'mere", "I'm too old for you. I'm gonna keep saying it. Come here anyway.",
            "*I take the hand he's holding out, palm up.* \"Say it as many times as you want. I'm still here.\"")

rounds = rnd("ONE", "The Argument", "He's forty-nine. He'll tell you.", s1, opn=True) + \
         rnd("TWO", "The Corner", "Short instructions. Calm. Right.", s2) + \
         rnd("THREE", "Your Call", "Mine's already made.", s3)

TAGS = ["Age Gap", "Older Man", "Boxing Coach", "Kinktober Day 10", "Losing Every Round"]
tagpills = "\n".join(f'            <div style="background-color:#1F1F21; color:#E8D9A8; border: 1px solid #45454A; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Malik Reyes - Kinktober Day 10</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0F0F10; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #1A1A1C; border: 1px solid #36363A; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E4E2DC; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #36363A; padding-bottom:15px; margin-bottom:25px; color: #F2EBD6; letter-spacing: 0.5px;">
            I Just Argue for Exercise
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #9D9A92; font-family: Georgia, serif;">
                “I'm too old for you. I'm gonna keep saying it. Come here anyway.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Malik Reyes" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #36363A; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#141416; color: #ABA9A2; padding:20px; flex: 1; min-width: 250px; border:1px solid #36363A; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Tito's Boxing Club, up a flight of stairs over a laundromat on Westchester Avenue in the Bronx. The 6 train rattles the speed bags. Malik Reyes is forty-nine, a widower, an old amateur middleweight who taught you to wrap your hands eight months ago. Three weeks ago you kissed him in the back office. He's been telling you he's too old ever since. He keeps losing.</span>
            </div>
            <div style="background-color:#141416; color: #ABA9A2; padding:20px; flex: 1; min-width: 250px; border:1px solid #36363A; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Malik Reyes x Any user (adult, late twenties)<br>
                    Kinktober Day 10: Age Gap<br>
                    Go three rounds, copy a starter into chat.<br>
                    TW: Age gap between adults, grief, hand wrap restraint<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- FIGHT POSTER -->
        <div style="margin-top: 35px; background-color: {POSTER}; background-image: linear-gradient(rgba(120,90,40,0.10), rgba(255,255,255,0) 40%, rgba(120,90,40,0.14)); border: 1px solid #BFAF8A; border-radius: 4px; padding: 0 0 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="background: {RED}; color: #FBF6E8; text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; letter-spacing: 2px; padding: 7px 10px; font-weight: 700;">OCT 10 · AGE GAP · THURSDAY 11:10 PM</div>
            <div style="padding: 18px 16px 0;">
                <div style="text-align: center; font-family: Georgia, serif; font-size: 0.8em; color: {MUTED}; letter-spacing: 3px; margin-bottom: 4px;">TITO'S BOXING CLUB PRESENTS</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-weight: 700; font-size: 30px; color: {BLUE}; letter-spacing: 2px; line-height: 1.15;">ONE MORE ROUND</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 6px;">Under the last bank of lights. Gate half down. No spin studio.</div>
                <div style="height: 3px; background: {BLUE}; margin: 10px 0 2px;"></div>
                <div style="height: 1px; background: {RED}; margin: 0 0 18px;"></div>
{rounds}
                <div style="margin-top: 14px; border-top: 2px solid {INK}; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">CORNER NOTES</span>
                    Stopwatch off, set on the apron. Wraps squared up for no reason. After: water, his old Tito's sweatshirt, and a plate of food.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Breathe. Look at me. ~M.R.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1F1F22; padding: 12px 20px; border-radius: 8px; border: 1px solid #36363A; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #45454A; padding-top: 12px; color: #A3A099;">
                An age gap between two grown adults: a forty-nine-year-old widower and a member in their late twenties. Expect protective dominance, gruff tenderness, grief, explicit intimacy, and hand wraps as light restraint. No age-play. All characters are adults. You say stop, he stops.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Malik Reyes (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
