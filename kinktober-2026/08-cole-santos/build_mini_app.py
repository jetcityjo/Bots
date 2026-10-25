import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Cole Santos banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

# Carbon-copy repair ticket: pale green duplicate sheet, carbon violet ink, brass lamp
TICKET, INK, CARBON, MUTED, BRASS = "#E4EDE3", "#1F2522", "#3D3F86", "#76837A", "#A8842F"
RULED = ("background-color: #E4EDE3; background-image: linear-gradient(rgba(61,63,134,0.13) 1px, transparent 1px); "
         "background-size: 100% 28px;")

def starter(text):
    return f'''
                        <div style="background: #F7FAF5; border-left: 3px solid {BRASS}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def cole(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {CARBON};">Cole:</strong>&nbsp;“{esc(line)}”</div>'

def field(label, value):
    return (f'<div style="display: flex; gap: 10px; align-items: baseline; margin-bottom: 6px; line-height: 1.45;">'
            f'<span style="font-family: \'Courier New\', Courier, monospace; font-size: 0.78em; color: {MUTED}; letter-spacing: 1px; min-width: 82px;">{esc(label)}</span>'
            f'<span style="color: {CARBON}; font-family: Georgia, serif; font-style: italic; border-bottom: 1px dotted #9FAEA3; flex: 1;">{esc(value)}</span></div>')

def section(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,255,255,0.72); border: 1px solid #B9C8BC; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {BRASS}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #C7D4CA; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def choice(title, note, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F2F6F0; border: 1px dashed #A9B9AD; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(title)}</strong>
                            <span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {CARBON}; margin-top: 2px;">{esc(note)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{cole(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = field("WORK REQ.", "Orgasm delay and denial.") + field("ARRIVED", "Early. Added to the end.") + field("READ", "Twice before. Once more now.") + \
     '<div style="margin-top: 10px;">' + cole("I read it the way I read a movement. One line at a time. Then we go upstairs, and I keep the time so you don't have to.") + '</div>' + \
     starter("*I take the second stool and watch him turn the ticket over.* \"You can read it a third time. I'll wait.\"")
s2 = field("LIMITS", "Your handwriting. He reads every line.") + field("TONIGHT?", "He tells you before anything starts.") + \
     '<div style="margin-top: 10px;">' + cole("Nothing happens that isn't on the back of this. You want to stop, say so, and we stop.") + '</div>' + \
     starter("\"Tell me now, before we go up. Tonight, or next time?\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Everyone writes something extra at the bottom. Tell him what yours was.</div>' + \
     choice("\"Please.\"", "just the word · no context", "Just the word. No context. I'm going to want the context. Take your time. I've got forty clocks and none of them agree.",
            "\"It means please. That's all it means. I wanted you to have it in writing.\"") + \
     choice("\"Make me ask.\"", "underlined twice", "Properly, then. Not 'please, Cole.' The whole sentence. You'll get it wrong the first time. That's fine. I'm very good at starting over.",
            "*I look at him over the ticket.* \"How do I ask properly? Teach me.\"") + \
     choice("\"Don't let me check the clock.\"", "small letters, near the edge", "That's my job anyway. Take your watch off. Put it on the bench, face down, next to the ticket. You can have it back after... with the real number.",
            "*I unbuckle my watch and set it face down on the bench.* \"Your job, then. All of it.\"")

parts = section("01", "Front: Work Requested", "Carbon pad. Same one he uses downstairs.", s1, opn=True) + \
        section("02", "Back: Limits", "Read once more, in front of you.", s2) + \
        section("03", "The Bottom Line", "The part he reads last.", s3)

TAGS = ["Edging", "Watchmaker", "Counting", "Kinktober Day 8", "I'll Tell You First"]
tagpills = "\n".join(f'            <div style="background-color:#1B2220; color:#D9BC74; border: 1px solid #3A4740; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cole Santos - Kinktober Day 8</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0C0F0E; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #151A18; border: 1px solid #2C3631; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #DFE3DD; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2C3631; padding-bottom:15px; margin-bottom:25px; color: #EDF2EA; letter-spacing: 0.5px;">
            I'll Add It to the End
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #93A098; font-family: Georgia, serif;">
                “Whether you finish tonight is my call, and I'll tell you before we start.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Cole Santos" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2C3631; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#111513; color: #A6B0A9; padding:20px; flex: 1; min-width: 250px; border:1px solid #2C3631; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Santos Watch Repair, Lawrence Avenue, Chicago. Forty-some clocks that never agree, one brass lamp over the bench, an apartment upstairs. Cole Santos kept his Lolo's shop after years as a quality engineer. Before anyone climbs the stairs, he hands them a repair ticket. Then he takes them to the edge, stops, counts out loud, and does it again.</span>
            </div>
            <div style="background-color:#111513; color: #A6B0A9; padding:20px; flex: 1; min-width: 250px; border:1px solid #2C3631; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Cole Santos x Any user<br>
                    Kinktober Day 8: Orgasm Delay/Denial<br>
                    Turn the ticket over, copy a starter into chat.<br>
                    TW: Edging, orgasm denial, counting, rules with resets<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- REPAIR TICKET -->
        <div style="margin-top: 35px; background: #2A2F2C; border-radius: 10px; padding: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="{RULED} border-radius: 4px; padding: 20px 16px; text-align: left;">
                <div style="display: flex; justify-content: space-between; align-items: baseline; font-family: 'Courier New', Courier, monospace; font-size: 0.78em; color: {MUTED}; letter-spacing: 1px; border-bottom: 2px dashed #A9B9AD; padding-bottom: 8px; margin-bottom: 12px;">
                    <span>SANTOS WATCH REPAIR</span><span style="color: #B23A30; font-weight: 700;">No. 0908</span>
                </div>
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 08 · ORGASM DELAY/DENIAL · AFTER HOURS</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">The Repair Ticket</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 20px;">Work requested on the front. Limits on the back. He hasn't decided yet.</div>
{parts}
                <div style="margin-top: 14px; border-top: 1px solid #B9C8BC; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">BENCH NOTES</span>
                    Cuckoo on the east wall, four minutes late. Leave it. Tea tin from Lola on the shelf upstairs. Water first. Then the real number.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Never force it. Find out what it's waiting for. ~C.S.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1A201D; padding: 12px 20px; border-radius: 8px; border: 1px solid #2C3631; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #36423C; padding-top: 12px; color: #9FA9A2;">
                Edging, orgasm delay and denial, counting and permission play, small rules with resets, specific praise, and real aftercare. All characters are adults. If you say stop, he stops.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Cole Santos (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
