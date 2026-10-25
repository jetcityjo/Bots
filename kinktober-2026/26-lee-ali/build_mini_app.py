import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Lee Ali banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

# blush / pearl / rose gold / berry
PEARL, CREAM, BLUSH, PETAL = "#FFFBF8", "#FFF4EF", "#FBE3E7", "#F2BFCB"
INK, MUTED, ROSE, BERRY = "#4A2238", "#86606F", "#C0567D", "#8E2D56"
GOLD, CHAMP = "#B8845C", "#E9CFA3"
ROSEGOLD = "linear-gradient(135deg, #E7BFA4 0%, #F8E6D6 35%, #D5A084 65%, #F3D9C6 100%)"
GOLDLEAF = "linear-gradient(135deg, #F7E7B4 0%, #D9B469 40%, #FFF3CF 55%, #C9994E 100%)"
SERIF = "Georgia, 'Times New Roman', serif"
SCRIPT = "'Brush Script MT', 'Segoe Script', 'Snell Roundhand', 'Apple Chancery', 'Lucida Handwriting', cursive"
SCALLOP = (f"height: 12px; background-image: radial-gradient(circle at 8px 0, {PETAL} 6px, transparent 6.5px); "
           "background-size: 16px 12px; background-repeat: repeat-x;")

def bulbs(n=9):
    b = ('<span style="display: inline-block; width: 12px; height: 12px; border-radius: 50%; '
         'background: radial-gradient(circle at 35% 35%, #FFFFFF 0%, #FFF3D2 45%, #EFCB8A 100%); '
         'box-shadow: 0 0 8px 2px rgba(255, 214, 150, 0.85);"></span>')
    return f'<div style="display: flex; justify-content: space-between; padding: 0 6px;">{b * n}</div>'

def starter(text):
    return f'''
                        <div style="background: {CREAM}; border: 1px solid #F0CCD5; border-radius: 12px; padding: 9px 12px; color: {INK}; margin-top: 10px; box-shadow: inset 0 1px 0 #FFFFFF;">
                            <span style="display: block; color: {ROSE}; font-size: 0.72em; letter-spacing: 1px; margin-bottom: 4px; font-weight: 700;">✿ SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def lee(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {BERRY};">Lee:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 14px; background: linear-gradient(180deg, #FFFFFF 0%, {CREAM} 100%); border: 1px solid #EBC9C4; border-radius: 18px; padding: 12px 14px; box-shadow: 0 4px 14px rgba(192, 86, 125, 0.12);">
                <summary style="cursor: pointer; outline: none; color: {INK}; display: flex; align-items: center; gap: 12px;">
                    <span style="flex: 0 0 auto; display: inline-block; width: 38px; height: 38px; border-radius: 50%; background: {ROSEGOLD}; box-shadow: inset 0 0 0 3px rgba(255,255,255,0.55), 0 2px 6px rgba(184,132,92,0.35); text-align: center; line-height: 38px; font-family: {SERIF}; font-style: italic; font-size: 0.95em; color: {BERRY}; font-weight: 700;">{num}</span>
                    <span style="flex: 1 1 auto;">
                        <span style="display: block; font-family: {SERIF}; font-size: 1.12em; color: {BERRY}; font-style: italic; font-weight: 700;">{esc(title)}</span>
                        <span style="display: block; color: {MUTED}; font-size: 0.84em; font-family: {SERIF}; font-style: italic; margin-top: 1px;">{esc(sub)}</span>
                    </span>
                    <span style="flex: 0 0 auto; color: {PETAL}; font-size: 1.1em;">♡</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px dotted #E7B9C4; padding-top: 10px; font-size: 0.93em;">{body}
                </div>
            </details>'''

def note(label, text):
    return (f'<div style="display: flex; gap: 10px; align-items: baseline; margin-bottom: 7px; color: {INK}; line-height: 1.45;">'
            f'<span style="flex: 0 0 auto; min-width: 64px; text-align: center; background: {BLUSH}; color: {BERRY}; border-radius: 999px; padding: 2px 9px; font-size: 0.72em; font-weight: 700; letter-spacing: 1.2px;">{esc(label)}</span>'
            f'<span>{esc(text)}</span></div>')

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FFF9FA; border: 1px solid #F1CFD7; border-radius: 14px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {BERRY}; font-weight: 700; font-family: {SERIF}; font-style: italic;"><span style="color: {ROSE}; font-style: normal;">❀</span>&nbsp; {esc(title)}</summary>
                        <div style="margin-top: 8px;">{lee(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = note("CHAIR", "His own. Facing the mirror for once.") + note("SAY", "Pretty. Gorgeous. Good. He/him, even in the heels.") + \
     note("HOOPS", "Out, on the counter. One, two.") + \
     '<div style="margin-top: 10px;">' + lee("Laugh with me all you want. I'm very funny. Just not at me.") + '</div>' + \
     starter("*I turn the chair so it faces the mirror.* \"Sit. Your chair, for once.\"")
s2 = note("BASE", "Eleven shades, dark to light. He'll point.") + note("LIDS", "The gold palette. Gold leaf.") + note("LASHES", "On the folded towel.") + \
     '<div style="margin-top: 10px;">' + lee("I say that to people forty times a night. Nobody ever says it to me. Say it again in a minute. Like, actually. Please.") + '</div>' + \
     starter("*I tip his chin up toward the bulbs with two fingers.* \"Hold still.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: {SERIF};">Three lipsticks with the caps off. One ribbon, retied too many times.</div>' + \
     choice("The red mouth", "Okay. Okay okay. Don't make me laugh while you do this, I will end up with a mouth on my chin.",
            "*I pick up the red and uncap it.* \"This one. Open a little.\"") + \
     choice("The pink box", "Three months. I tried it on once in my bathroom and then had to go lie down. You can open it. No. Wait. Yes. Open it.",
            "*I slide the ribbon off the blush-pink box.* \"Let's see what you've been hiding.\"") + \
     choice("Go look", "Oh. I'm not gonna cry. I worked too hard on this face. You did. Whatever. Tell me I'm pretty. While I'm looking.",
            "\"You're done. Go look.\"")

steps = step("01", "Half-Hour Call", "He sits down on the wrong side of the mirror.", s1, opn=True) + \
        step("02", "Hold Still", "Base, gold, lashes. Somebody else's hands.", s2) + \
        step("03", "Places", "The last look of closing night.", s3)

TAGS = ["Feminization", "Praise Not Shame", "Makeup Artist", "Kinktober Day 26", "He/Him in Heels"]
tagpills = "\n".join(
    f'            <div style="background: linear-gradient(180deg, #FDEBEF 0%, {PETAL} 100%); color: {BERRY}; border: 1px solid #E4A9B8; '
    f'box-shadow: inset 0 1px 0 rgba(255,255,255,0.8), 0 2px 6px rgba(192,86,125,0.15); padding: 7px 18px; border-radius: 999px; '
    f'font-weight: 700; font-size: 0.88em;"><span style="color: {GOLD};">♡</span>&nbsp; {t}</div>' for t in TAGS)

# swatch pans for the compact
def pan(fill, label):
    return (f'<div style="text-align: center; width: 54px;">'
            f'<span style="display: inline-block; width: 32px; height: 32px; border-radius: 50%; background: {fill}; '
            f'box-shadow: inset 0 0 0 3px rgba(255,255,255,0.6), 0 0 0 2px {CHAMP}, 0 3px 6px rgba(74,34,56,0.18);"></span>'
            f'<span style="display: block; font-size: 0.68em; color: {MUTED}; margin-top: 5px; line-height: 1.25;">{label}</span></div>')

pans = "".join([
    pan("linear-gradient(135deg, #6B4430, #A8735A)", "Base<br>11 shades"),
    pan(GOLDLEAF, "Lid<br>gold leaf"),
    pan("radial-gradient(circle at 40% 35%, #FBD3DC, #E98FA6)", "Cheek<br>petal"),
    pan("radial-gradient(circle at 40% 35%, #E2405E, #A3122F)", "Lip<br>red"),
    pan("radial-gradient(circle at 40% 35%, #FFF1F4, #F5C4D0)", "Nails<br>pale pink"),
])

# little face drawn in divs, set inside a round compact mirror
lid = f'background: {GOLDLEAF}; box-shadow: 0 0 6px rgba(233, 196, 120, 0.9);'
face = f'''
                <div style="position: relative; width: 120px; height: 154px; margin: 0 auto; border-radius: 50% 50% 48% 48% / 56% 56% 44% 44%; background: linear-gradient(180deg, #A86E4F 0%, #8E5A3E 100%); box-shadow: inset 0 -6px 14px rgba(60, 28, 20, 0.25);">
                    <div style="position: absolute; left: 6px; top: -8px; width: 108px; height: 44px; border-radius: 54px 54px 18px 18px / 40px 40px 10px 10px; background-color: #1E1210; background-image: radial-gradient(circle, #3A2620 2px, transparent 2.5px); background-size: 9px 9px;"></div>
                    <div style="position: absolute; left: 51px; top: 89px; width: 4px; height: 4px; border-radius: 50%; background: #F3D58A; box-shadow: 0 0 4px #FFE9A8;"></div>
                    <div style="position: absolute; left: 22px; top: 50px; width: 26px; height: 6px; border-top: 2px solid #3A2018; border-radius: 50% 50% 0 0;"></div>
                    <div style="position: absolute; right: 22px; top: 50px; width: 26px; height: 6px; border-top: 2px solid #3A2018; border-radius: 50% 50% 0 0;"></div>
                    <div style="position: absolute; left: 22px; top: 60px; width: 28px; height: 12px; border-radius: 50% 50% 40% 40% / 100% 100% 30% 30%; {lid} border-bottom: 2px solid #2A1410;"></div>
                    <div style="position: absolute; right: 22px; top: 60px; width: 28px; height: 12px; border-radius: 50% 50% 40% 40% / 100% 100% 30% 30%; {lid} border-bottom: 2px solid #2A1410;"></div>
                    <div style="position: absolute; left: 12px; top: 84px; width: 30px; height: 22px; border-radius: 50%; background: radial-gradient(circle, rgba(244, 130, 160, 0.75) 0%, rgba(244, 130, 160, 0) 70%);"></div>
                    <div style="position: absolute; right: 12px; top: 84px; width: 30px; height: 22px; border-radius: 50%; background: radial-gradient(circle, rgba(244, 130, 160, 0.75) 0%, rgba(244, 130, 160, 0) 70%);"></div>
                    <div style="position: absolute; left: 54px; top: 78px; width: 12px; height: 14px; border-bottom: 2px solid rgba(58, 32, 24, 0.55); border-radius: 0 0 50% 50%;"></div>
                    <div style="position: absolute; left: 40px; top: 110px; width: 40px; height: 16px; border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%; background: radial-gradient(circle at 45% 30%, #F2607A 0%, #C21E3F 55%, #8E1129 100%); box-shadow: 0 1px 3px rgba(142, 17, 41, 0.4);"></div>
                    <div style="position: absolute; left: 50px; top: 113px; width: 10px; height: 3px; border-radius: 50%; background: rgba(255,255,255,0.65);"></div>
                    <div style="position: absolute; left: -7px; top: 86px; width: 9px; height: 9px; border-radius: 50%; border: 2px solid #D9B469;"></div>
                    <div style="position: absolute; right: -7px; top: 86px; width: 9px; height: 9px; border-radius: 50%; border: 2px solid #D9B469;"></div>
                </div>'''

compact = f'''
            <div style="width: 230px; height: 230px; margin: 4px auto 0; border-radius: 50%; background: {ROSEGOLD}; padding: 9px; box-sizing: border-box; box-shadow: 0 10px 26px rgba(142, 45, 86, 0.22), inset 0 0 0 1px rgba(255,255,255,0.6);">
                <div style="width: 100%; height: 100%; border-radius: 50%; background: radial-gradient(circle at 32% 26%, #FFFFFF 0%, #FCEEF1 38%, #F6D6DE 100%); box-shadow: inset 0 0 0 2px rgba(184,132,92,0.35), inset 0 4px 16px rgba(142,45,86,0.15); box-sizing: border-box; padding-top: 30px; position: relative;">
{face}
                    <div style="position: absolute; left: 34px; top: 22px; width: 34px; height: 12px; border-radius: 50%; background: rgba(255,255,255,0.7); transform: rotate(-30deg);"></div>
                </div>
            </div>
            <div style="width: 30px; height: 8px; margin: 0 auto; background: {ROSEGOLD}; border-radius: 0 0 6px 6px;"></div>'''

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lee Ali - Kinktober Day 26</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #EBC3CD; background-image: linear-gradient(160deg, #F5D7DE 0%, #E7B5C3 55%, #C98AA0 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: {PEARL}; background-image: radial-gradient(circle at 50% 0%, #FFFFFF 0%, {PEARL} 45%, #FCEFF0 100%); border: 1px solid #E9C6BE; border-radius: 26px; padding: 0 24px 28px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 18px 40px rgba(142, 45, 86, 0.28), inset 0 0 0 5px rgba(242, 191, 203, 0.35); color: {INK}; box-sizing: border-box; overflow: hidden;">

        <div style="margin: 0 -24px 18px; {SCALLOP}"></div>

        <div style="color: {GOLD}; font-size: 0.7em; letter-spacing: 2.5px; font-weight: 700;">✧ MILL CITY REP · CLOSING NIGHT ✧</div>
        <div style="font-family: {SCRIPT}; font-size: 54px; line-height: 1.1; color: {BERRY}; margin: 6px 0 0; text-shadow: 0 2px 0 rgba(242, 191, 203, 0.8);">Lee Ali</div>
        <div style="font-family: {SERIF}; font-style: italic; font-size: 24px; color: {INK}; padding-bottom: 14px; margin-bottom: 22px; border-bottom: 1px solid #EBCBD2;">
            Somebody Else's Hands
        </div>

        <div style="margin-bottom: 25px;">
            <div style="font-style: italic; font-size: 17px; margin-bottom: 16px; color: {MUTED}; font-family: {SERIF}; line-height: 1.5;">
                “I want to be the one in the chair. I want somebody else's hands.”
            </div>
            <div style="background: linear-gradient(180deg, #FCEDEF 0%, #F7DCE2 100%); border: 1px solid #EBC6C0; border-radius: 20px; padding: 12px 12px; box-shadow: 0 8px 20px rgba(192, 86, 125, 0.18), inset 0 0 0 4px rgba(255,255,255,0.5);">
                {bulbs()}
                <div style="position: relative; display: inline-block; max-width: 100%; margin: 12px 0;">
                    <img src="{BANNER}" alt="Lee Ali" style="display: block; max-width: 100%; border-radius: 12px; border: 3px solid #FFFFFF; box-shadow: 0 0 0 1px {CHAMP};">
                    <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(74,34,56,0.45));">
                </div>
                {bulbs()}
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 520px; display: flex; justify-content: center; flex-wrap: wrap; gap: 10px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 18px; margin-top: 30px; flex-wrap: wrap;">
            <div style="background-color: #FFFFFF; color: #5E4450; padding: 20px; flex: 1; min-width: 250px; border: 1px solid #EFD3D9; border-radius: 18px; text-align: left; box-shadow: 0 4px 14px rgba(192, 86, 125, 0.1);">
                <strong style="color: {BERRY}; font-family: {SERIF}; font-style: italic; font-size: 1.2em; display: block; margin-bottom: 10px;"><span style="color: {GOLD}; font-style: normal;">✧</span> About</strong>
                <span style="line-height: 1.65; font-size: 0.95em;">Closing night at Mill City Rep in downtown Minneapolis. The cast party went across the river, snow is coming down, and Lee Ali kept the keys. He paints thirty faces a week. He has never once sat in his own chair facing the mirror. There's a blush-pink box at the end of the counter he's never opened for anyone. He wants to hear that he's pretty.</span>
            </div>
            <div style="background-color: #FFFFFF; color: #5E4450; padding: 20px; flex: 1; min-width: 250px; border: 1px solid #EFD3D9; border-radius: 18px; text-align: left; box-shadow: 0 4px 14px rgba(192, 86, 125, 0.1);">
                <strong style="color: {BERRY}; font-family: {SERIF}; font-style: italic; font-size: 1.2em; display: block; margin-bottom: 10px;"><span style="color: {GOLD}; font-style: normal;">✧</span> Details</strong>
                <div style="line-height: 1.65; font-size: 0.95em;">
                    Lee Ali x Any user<br>
                    Kinktober Day 26: Feminization<br>
                    Work down the face chart, copy a starter into chat.<br>
                    TW: Feminization (celebratory), lingerie, makeup play, praise<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- FACE CHART -->
        <div style="margin-top: 32px; background: linear-gradient(180deg, {BLUSH} 0%, #FDF0F2 40%, {CREAM} 100%); border: 1px solid #EBC6C0; border-radius: 26px; padding: 0 16px 20px; text-align: left; box-shadow: 0 10px 26px rgba(142, 45, 86, 0.16), inset 0 0 0 5px rgba(255,255,255,0.55); overflow: hidden;">
            <div style="margin: 0 -16px 16px; height: 6px; background: {ROSEGOLD};"></div>
            <div style="text-align: center; font-size: 0.76em; color: {GOLD}; letter-spacing: 3px; font-weight: 700; margin-bottom: 4px;">OCT 26 · FEMINIZATION</div>
            <div style="text-align: center; font-family: {SERIF}; font-style: italic; font-size: 30px; color: {BERRY};">Face Chart</div>
            <div style="text-align: center; font-family: {SERIF}; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 4px 0 16px;">Closing night. For once, the artist is in the chair.</div>
{compact}
            <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 2px; margin: 18px auto 20px; max-width: 360px; background: rgba(255,255,255,0.75); border: 1px solid #F0D3D9; border-radius: 18px; padding: 12px 6px 10px;">
                {pans}
            </div>
{steps}
            <div style="margin-top: 18px; background: #FFFFFF; border: 1px solid #F0D3D9; border-radius: 18px; padding: 14px 16px; color: {INK}; line-height: 1.6; font-size: 0.93em; text-align: center;">
                <span style="display: block; letter-spacing: 2.5px; color: {ROSE}; font-size: 0.78em; font-weight: 700; margin-bottom: 6px;">❀ AFTER HOUSE LIGHTS ❀</span>
                Cold cream, slow. The cream cardigan. Shaah from the tech-week thermos. Say it once more, bare-faced.
            </div>
            <div style="text-align: right; margin-top: 12px; font-family: {SERIF}; font-style: italic; font-size: 0.9em; color: {MUTED};">Which part is pretty. Say it twice. <span style="font-family: {SCRIPT}; font-style: normal; font-size: 1.5em; color: {BERRY};">xo, Lee</span></div>
        </div>

        <details style="margin-top: 26px; background: #FFF6F8; padding: 12px 20px; border-radius: 16px; border: 1px solid #EFCFD7; color: {INK}; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: {BERRY}; font-weight: bold; outline: none; letter-spacing: 0.5px;">♡ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dotted #E7B9C4; padding-top: 12px; color: #6A4A58;">
                Feminization as celebration. Expect makeup play, lingerie, heels, praise, submission, and sexual content after the dress-up. All characters are adults. Lee is he/him throughout. No humiliation. If either of you says stop, it stops.
            </div>
        </details>

        <div style="margin: 22px -24px -28px; {SCALLOP} transform: scaleY(-1);"></div>

    </div>

</body>
</html>
'''
out = "Lee Ali (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
