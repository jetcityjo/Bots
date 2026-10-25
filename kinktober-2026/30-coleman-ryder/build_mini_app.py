import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Coleman Ryder banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

PAGE, INK, MUTED, REDPEN, MAPLE, CORK = "#FBF8F1", "#1F1D22", "#86808A", "#C1272D", "#D2552E", "#9C7650"
TYPE = "'Courier New', Courier, monospace"

def starter(text):
    return f'''
                        <div style="background: #FFFFFF; border-left: 3px solid {REDPEN}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def coleman(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {REDPEN};">Coleman:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #F4EFE3; border: 1px solid #DDD4C2; border-radius: 2px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: {TYPE}; font-size: 0.9em; color: {REDPEN}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-family: {TYPE}; font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #DDD4C2; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def question(n, q, note):
    return f'<div style="margin-bottom: 8px; line-height: 1.45; color: {INK};"><span style="font-family: {TYPE}; color: {REDPEN}; font-weight: 700; margin-right: 6px;">{n}.</span><span style="font-family: {TYPE};">{esc(q)}</span><span style="display: block; font-family: Georgia, serif; font-style: italic; color: {MUTED}; font-size: 0.9em; margin-left: 22px;">{esc(note)}</span></div>'

def choice(title, margin, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #FFFDF8; border: 1px dashed #CDBFA8; border-radius: 2px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(title)}</strong>
                            <span style="display: block; font-family: Georgia, serif; font-style: italic; font-size: 0.82em; color: {REDPEN}; margin-top: 2px;">{esc(margin)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{coleman(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = coleman("You pick. Any kink, any scene, as long as it's two adults who both say yes. I have no idea what you're going to say, which is... yeah. That's the point.") + \
     starter("*I turn the page so the unfinished line faces me and take the pen out of his hand.* \"Writer's choice? Okay. Here's what chapter thirty-one is about.\"")
s2 = question(1, "What's in?", "Say it plainly. I'll write it down exactly.") + \
     question(2, "What's out?", "That goes on its own index card. I don't touch that card.") + \
     question(3, "Who's holding the pen?", "Whoever holds it leads.") + \
     coleman("If you want me to stop, say so and I stop. Otherwise I'm going to ask a lot of follow-up questions. Sorry in advance.") + \
     starter("\"Okay. Three answers. What's in, what's out, and then we argue about the pen.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Third question. Answer it out loud.</div>' + \
     choice("He holds it", "margin note: confident. specific. annoyingly good at this.",
            "Then here's the first line. The rain kept on. He told her where to stand, and he didn't say please. Okay. Stand by the window. The round one.",
            "\"You hold the pen tonight.\" *I set it in his palm and close his fingers around it.*") + \
     choice("You hold it", "margin note: he goes quiet. that's the good kind.",
            "Oh. Okay. Um. Yes. I'm... yes. I'll stop talking now. Mostly. You write the first line.",
            "*I keep the red pen and point it at the rug.* \"My pen. Sit there. I'll read you the first line.\"") + \
     choice("Pass it back and forth", "margin note: switch. both sides of the door.",
            "Every time the pen changes hands, we say so out loud, so nobody has to guess who's leading. Deal?",
            "\"Deal. I start. When I hand you the pen, you take over.\"")

steps = step("01", "Writer's Choice", "Pick the kink. He'll write the first line.", s1, opn=True) + \
        step("02", "Three Questions", "In. Out. The pen.", s2) + \
        step("03", "Who's Holding the Pen", "Whoever holds it leads.", s3)

TAGS = ["Writer's Choice", "Switch", "Collaborative Fiction", "Kinktober Day 30", "Three Questions"]
tagpills = "\n".join(f'            <div style="background-color:#26181D; color:#EE9277; border: 1px solid #5B2F38; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coleman Ryder - Kinktober Day 30</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0F0E13; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #17151C; border: 1px solid #2E2A36; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E4E0E6; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2E2A36; padding-bottom:15px; margin-bottom:25px; color: #FBF8F1; letter-spacing: 0.5px;">
            Chapter Thirty-One Is Yours
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #9A93A0; font-family: Georgia, serif;">
                “Writer's choice. What's chapter thirty-one about?”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Coleman Ryder" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2E2A36; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#131118; color: #ABA4B0; padding:20px; flex: 1; min-width: 250px; border:1px solid #2E2A36; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">An attic off Hawthorne in Portland. Rain on the skylight, a radiator that clanks, a maple gone red out the round window. Coleman Ryder has written thirty erotic romances as Odette Marlowe. The new book, Thirty-One Nights, is done except for the last chapter, which has been one unfinished sentence for eleven days. His outline says writer's choice. So you choose.</span>
            </div>
            <div style="background-color:#131118; color: #ABA4B0; padding:20px; flex: 1; min-width: 250px; border:1px solid #2E2A36; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Coleman Ryder x Any user<br>
                    Kinktober Day 30: Writer's Choice<br>
                    Pick the kink, answer three questions, copy a starter into chat.<br>
                    TW: Varies by the kink you choose, switch dynamics, roleplay<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- MANUSCRIPT PAGE -->
        <div style="margin-top: 35px; background: {CORK}; border-radius: 12px; padding: 14px 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="width: 14px; height: 14px; margin: 0 auto 8px; background: {MAPLE}; border-radius: 50%; border: 2px solid #8E3420; box-shadow: 0 2px 3px rgba(0,0,0,0.4);"></div>
            <div style="background-color: {PAGE}; border-left: 2px solid rgba(193,39,45,0.35); border-radius: 2px; padding: 22px 16px; text-align: left; box-shadow: 0 2px 6px rgba(0,0,0,0.3);">
                <div style="text-align: center; font-family: {TYPE}; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 30 · WRITER'S CHOICE · DRAFT 15</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Chapter Thirty-One</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 4px;">She pressed him against the wall and</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {REDPEN}; margin: 0 0 18px;">WHY</div>
{steps}
                <div style="margin-top: 14px; border-top: 1px solid #DDD4C2; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: {TYPE}; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">NOTE TO SELF</span>
                    Don't sit on nineteen. Somebody proposes in it. Fourteen drafts on the desk, same sentence. Radiator is not a co-author.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {REDPEN};">Not for the book. ~C.R.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1C1922; padding: 12px 20px; border-radius: 8px; border: 1px solid #2E2A36; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #3A3444; padding-top: 12px; color: #A39CA8;">
                Writer's choice: the kink is whatever you pick, so content varies by session. Expect switch dynamics, narrated roleplay, dirty talk, and explicit scenes. No minors, family members, animals, or real people. All characters are adults. Say stop and Coleman stops.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Coleman Ryder (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
