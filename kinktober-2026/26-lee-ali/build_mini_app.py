import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Lee Ali banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

PAPER, INK, MUTED, ROSE, GOLD = "#FBF2F0", "#2A1E22", "#8C7A80", "#B4446A", "#C29A45"

def starter(text):
    return f'''
                        <div style="background: #FFFAF8; border-left: 3px solid {ROSE}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def lee(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {ROSE};">Lee:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #FFFFFF; border: 1px solid #E8D3D3; border-radius: 6px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {GOLD}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #EEDCDC; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def note(label, text):
    return f'<div style="display: flex; gap: 10px; margin-bottom: 6px; color: {INK}; line-height: 1.45;"><span style="font-family: \'Courier New\', Courier, monospace; font-size: 0.82em; color: {GOLD}; min-width: 74px; font-weight: 700; letter-spacing: 1px;">{esc(label)}</span><span>{esc(text)}</span></div>'

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FDF4F4; border: 1px dashed #DDBFC4; border-radius: 6px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
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
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Three lipsticks with the caps off. One ribbon, retied too many times.</div>' + \
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
tagpills = "\n".join(f'            <div style="background-color:#2A1820; color:#F2B8C6; border: 1px solid #5C3445; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lee Ali - Kinktober Day 26</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #110C0F; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #1C1418; border: 1px solid #3A2630; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #EADDE0; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #3A2630; padding-bottom:15px; margin-bottom:25px; color: #FBF2F0; letter-spacing: 0.5px;">
            Somebody Else's Hands
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #A0898F; font-family: Georgia, serif;">
                “I want to be the one in the chair. I want somebody else's hands.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Lee Ali" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #3A2630; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#171013; color: #B5A3A8; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2630; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Closing night at Mill City Rep in downtown Minneapolis. The cast party went across the river, snow is coming down, and Lee Ali kept the keys. He paints thirty faces a week. He has never once sat in his own chair facing the mirror. There's a blush-pink box at the end of the counter he's never opened for anyone. He wants to hear that he's pretty.</span>
            </div>
            <div style="background-color:#171013; color: #B5A3A8; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2630; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Lee Ali x Any user<br>
                    Kinktober Day 26: Feminization<br>
                    Work down the face chart, copy a starter into chat.<br>
                    TW: Feminization (celebratory), lingerie, makeup play, praise<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- FACE CHART -->
        <div style="margin-top: 35px; background-color: {PAPER}; border: 1px solid #E3CACC; border-top: 8px solid {GOLD}; border-radius: 10px; padding: 22px 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 8px;">OCT 26 · FEMINIZATION</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Face Chart: L. Ali</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 14px;">Closing night. For once, the artist is in the chair.</div>
            <div style="text-align: center; margin: 0 0 18px; font-size: 18px; letter-spacing: 6px; color: {GOLD};">&#9675; &#9675; &#9675; &#9675; &#9675; &#9675;</div>
{steps}
            <div style="margin-top: 18px; border-top: 1px solid #E3CACC; padding-top: 14px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">AFTER HOUSE LIGHTS</span>
                Cold cream, slow. The cream cardigan. Shaah from the tech-week thermos. Say it once more, bare-faced.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Which part is pretty. Say it twice. ~L.A.</div>
        </div>

        <details style="margin-top: 30px; background: #21181C; padding: 12px 20px; border-radius: 8px; border: 1px solid #3A2630; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #48313B; padding-top: 12px; color: #A8979C;">
                Feminization as celebration. Expect makeup play, lingerie, heels, praise, submission, and sexual content after the dress-up. All characters are adults. Lee is he/him throughout. No humiliation. If either of you says stop, it stops.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Lee Ali (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
