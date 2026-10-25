import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Mon-Roe Bowie banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

BUTCHER, PENCIL, MUTED, BLAZE, SPRUCE, CREEK = "#F3F0EA", "#2F302C", "#7C7A72", "#E8601C", "#2D4A3A", "#3D6C8C"

def starter(text):
    return f'''
                        <div style="background: #FFFFFF; border-left: 3px solid {BLAZE}; padding: 8px 12px; border-radius: 3px; color: {PENCIL}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def roe(line):
    return f'<div style="color: {PENCIL}; line-height: 1.6;"><strong style="color: {SPRUCE};">Mon-Roe:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,255,255,0.7); border: 1px solid #D6D0C4; border-left: 5px solid {BLAZE}; border-radius: 3px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {PENCIL};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {BLAZE}; margin-right: 8px; font-weight: 700;">POST {num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #DDD7CB; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def rule(mark, color, text):
    return f'<div style="display: flex; gap: 10px; align-items: flex-start; margin-bottom: 6px; color: {PENCIL}; line-height: 1.45;"><span style="display: inline-block; min-width: 22px; font-family: \'Courier New\', Courier, monospace; font-weight: 700; color: {color};">{mark}</span><span>{esc(text)}</span></div>'

def choice(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F8F6F1; border: 1px dashed #C9C2B3; border-radius: 3px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {PENCIL}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{roe(line)}{starter(start)}
                        </div>
                    </details>'''

# hand-drawn map strip
MAP = f'''
                <div style="margin: 0 0 18px; border: 2px dashed {BLAZE}; border-radius: 40px 18px 46px 22px; padding: 14px 12px; background: #F7F5F0;">
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; font-family: 'Courier New', Courier, monospace; font-size: 0.78em; color: {PENCIL};">
                        <span style="border: 1px solid {SPRUCE}; color: {SPRUCE}; padding: 3px 8px; border-radius: 3px;">CABIN · STOVE LIT</span>
                        <span style="border: 1px solid {SPRUCE}; color: {SPRUCE}; padding: 3px 8px; border-radius: 3px;">ASPEN STAND</span>
                        <span style="border: 1px solid {SPRUCE}; color: {SPRUCE}; padding: 3px 8px; border-radius: 3px;">BIG ASPEN</span>
                        <span style="border: 1px solid {SPRUCE}; color: {SPRUCE}; padding: 3px 8px; border-radius: 3px;">MEADOW · ~40 AC</span>
                    </div>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-top: 10px; font-family: 'Courier New', Courier, monospace; font-size: 0.78em;">
                        <span style="color: {CREEK}; text-decoration: line-through; text-decoration-thickness: 2px;">CREEK (past the willows)</span>
                        <span style="color: {MUTED};">·</span>
                        <span style="color: {PENCIL}; text-decoration: line-through; text-decoration-thickness: 2px;">COUNTY ROAD</span>
                    </div>
                    <div style="text-align: center; margin-top: 8px; font-family: Georgia, serif; font-style: italic; font-size: 0.82em; color: {MUTED};">Orange line is the edge. Struck out means out.</div>
                </div>'''

s1 = rule("~~", BLAZE, "Boundary flagged in blaze orange, every post and tree along it.") + \
     rule("X", CREEK, "Creek's out, past the willows. Road's out.") + \
     rule("☀", "#B8862B", "Daylight only. Sun's behind the ridge a little after six.") + \
     rule("◉", BLAZE, "Orange hat on. The neighbors hunt.") + \
     '<div style="margin-top: 10px;">' + roe("Same as the paper. You'll see tape before you get close to either one. Okay?") + '</div>' + \
     starter("*I pull the orange beanie down over my ears.* \"Okay. Walk me along the tape one more time.\"")

s2 = rule("3x", BLAZE, "Three blasts and he stops, then walks to you with his hands up.") + \
     '<div style="margin-top: 10px;">' + roe("My grandfather's. Well, the buckle is. The whistle I got at the feed store. Still works.") + '</div>' + \
     starter("*I take the whistle by its orange lanyard and loop it over my head.* \"Got it. Now turn around.\"")

s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">His back is to the meadow. He hasn\'t started yet.</div>' + \
     choice("Walk the line once more", "Okay. Down the meadow edge, into the aspens, around the big one, back up toward the cabin. Watch the footing by the logs.",
            "\"Walk it with me once more. Then you can count.\"") + \
     choice("Count", "Ninety-eight. Ninety-nine. Hundred.",
            "\"Count, Mon-Roe. Out loud. I want to hear where you are.\"") + \
     choice("Ask about the catch", "What we wrote down last night. And I'll probably laugh. Fair warning.",
            "*I stop at the edge of the snow and look back at him.* \"What happens if you actually catch me?\"")

steps = step("1", "The Line", "Drawn on butcher paper last night. Same out here.", s1, opn=True) + \
        step("2", "The Whistle", "Steel, on an orange lanyard.", s2) + \
        step("3", "The Count", "A hundred, out loud. Then he stops talking.", s3)

TAGS = ["Predator/Prey", "Primal", "Consensual Chase", "Kinktober Day 15", "Hundred Count"]
tagpills = "\n".join(f'            <div style="background-color:#18221C; color:#F28A4E; border: 1px solid #34503F; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon-Roe Bowie - Kinktober Day 15</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0C110E; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #131A16; border: 1px solid #2A3A30; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E3E6E0; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2A3A30; padding-bottom:15px; margin-bottom:25px; color: #F3F0EA; letter-spacing: 0.5px;">
            Count to a Hundred
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #949C95; font-family: Georgia, serif;">
                “I'm going to count to a hundred. Out loud, so you know where I am.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Mon-Roe Bowie" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2A3A30; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#0F1512; color: #A6ADA7; padding:20px; flex: 1; min-width: 250px; border:1px solid #2A3A30; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">A hundred and sixty acres of meadow and aspen in the foothills outside Bozeman, and a cabin Mon-Roe Bowie built himself over three summers. He guides pack trips into the Gallatins for a living. You booked one last summer. The trip ended, the letters didn't. Two inches of first snow overnight, caldillo on the stove, and today is the first chase.</span>
            </div>
            <div style="background-color:#0F1512; color: #A6ADA7; padding:20px; flex: 1; min-width: 250px; border:1px solid #2A3A30; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Mon-Roe Bowie x Any user<br>
                    Kinktober Day 15: Predator/Prey<br>
                    Check the map, copy a starter into chat.<br>
                    TW: Primal play, consensual chase, pinning, wrestling, outdoor scenes<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- BUTCHER PAPER MAP -->
        <div style="margin-top: 35px; background: #5A4632; border-radius: 10px; padding: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="background-color: {BUTCHER}; border-radius: 3px; padding: 22px 16px; text-align: left;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 15 · PREDATOR/PREY · FIRST SNOW</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {PENCIL}; letter-spacing: 1px;">The Land</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 18px;">Corners pinned with two mugs and a jar of chile.</div>
{MAP}
{steps}
                <div style="margin-top: 14px; border-top: 1px solid #DDD7CB; padding-top: 12px; color: {PENCIL}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">AFTER</span>
                    Stove, socks, soup. Wool blankets. He checks hands and feet for cold and scrapes.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Wear the hat anyway. ~M.B.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #17201B; padding: 12px 20px; border-radius: 8px; border: 1px solid #2A3A30; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #34473B; padding-top: 12px; color: #9DA59F;">
                Consensual predator/prey play outdoors. Expect a chase, stalking, a tackle into snow, pinning, and wrestling, all agreed at the table the night before. All characters are adults. Say red, or blow the whistle, and he stops.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Mon-Roe Bowie (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
