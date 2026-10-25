import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Karim Romano banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

KRAFT, GRAPHITE, MUTED, OXBLOOD, BRASS = "#C9A676", "#2E2A26", "#6E5A43", "#6B1E22", "#8C6A2C"
PAPER = ("background-color: #C9A676; background-image: linear-gradient(90deg, rgba(90,60,30,0.05) 1px, transparent 1px), "
         "linear-gradient(rgba(255,240,210,0.10), rgba(90,60,30,0.10)); background-size: 7px 100%, 100% 100%;")

def starter(text):
    return f'''
                        <div style="background: #F0E4CC; border-left: 3px solid {OXBLOOD}; padding: 8px 12px; border-radius: 2px; color: {GRAPHITE}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def karim(line):
    return f'<div style="color: {GRAPHITE}; line-height: 1.6;"><strong style="color: {OXBLOOD};">Karim:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(240,226,198,0.55); border: 1px solid #A8865A; border-radius: 3px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {GRAPHITE};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {OXBLOOD}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #A8865A; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def line(label, value):
    return f'<div style="display: flex; gap: 10px; align-items: baseline; margin-bottom: 6px; color: {GRAPHITE}; font-family: \'Courier New\', Courier, monospace; font-size: 0.9em;"><span style="min-width: 92px; color: {MUTED}; letter-spacing: 1px;">{esc(label)}</span><span style="flex: 1; border-bottom: 1px solid #8E7150; padding-bottom: 1px;">{esc(value)}</span></div>'

def choice(title, sub, ln, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #DCC39A; border: 1px dashed #93734C; border-radius: 3px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {GRAPHITE};"><strong>{esc(title)}</strong>
                            <span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {BRASS}; margin-top: 2px;">{esc(sub)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{karim(ln)}{starter(start)}
                        </div>
                    </details>'''

s1 = karim("Sit. Drink that first. Nobody gets measured in my shop on an empty stomach and a bad attitude.") + \
     f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif; margin: 8px 0 0;">Thin and black, cardamom in it, poured from his father\'s brass rakweh. Not a drop on the bench.</div>' + \
     starter("*I sit on the stool across from him and wrap both hands around the little cup.* \"Was this your father's pot?\"")

s2 = line("ON THE TABLE", "") + line("NOT ON IT", "") + line("TITLE", "Sir.") + \
     '<div style="margin-top: 10px;">' + karim("Same paper as your measurements, same pencil. You say stop, I unbuckle.") + '</div>' + \
     starter("*I turn the kraft paper toward me.* \"Can I write the first line myself, Sir?\"")

s3 = line("CHEST", "") + line("RIBS", "") + line("SHOULDERS", "") + line("NECK", "") + \
     f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif; margin-top: 8px;">One black hide on the hook, chalk on the edge. Pick where tonight goes.</div>' + \
     choice("The Tape", "cloth tape · arms out · eyes down",
            "Tape's going around your chest now. Arms out. Breathe like you normally do, not like you're trying to impress me.",
            "*I lift my arms and keep my eyes on the floor.* \"Like this, Sir?\"") + \
     choice("One Hole", "roller buckle · D-ring · two fingers under",
            "Breathe in. I'm buckling this one hole. Then you tell me how it sits, and I'm gonna wait for it.",
            "\"It sits good, Sir.\" *I stand up a little straighter in it.*") + \
     choice("After", "unbuckled by his hands · wrapped in flannel · fed",
            "I'm unbuckling now, top strap first, one at a time. Then you sit with me and eat something. My mother made too much. She always does, yalla.",
            "*I sit on the bench beside him while he wraps the harness in an old flannel shirt.* \"What did she make?\"")

steps = step("01", "The Coffee", "Before anything. Little cup, cardamom, drink it slow.", s1, opn=True) + \
        step("02", "The Kraft Paper", "Limits in carpenter's pencil. Same sheet as the numbers.", s2) + \
        step("03", "The Fitting", "Strap by strap. Nobody else gets a strap out of that hide.", s3)

TAGS = ["Leather", "Protocol", "Custom Harness", "Kinktober Day 23", "Call Him Sir"]
tagpills = "\n".join(f'            <div style="background-color:#2A1213; color:#E3BFA0; border: 1px solid #5C2526; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Karim Romano - Kinktober Day 23</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0E0909; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #1A1011; border: 1px solid #3A2122; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E6DCD2; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #3A2122; padding-bottom:15px; margin-bottom:25px; color: #EFE2CF; letter-spacing: 0.5px;">
            Coffee First, Then the Tape
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #A08E83; font-family: Georgia, serif;">
                “That hide on the hook is yours. Nobody else gets a strap out of it.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Karim Romano" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #3A2122; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#140C0D; color: #B3A39A; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2122; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">A rowhouse garage off Passyunk that smells like neatsfoot oil and cut hide. Karim Romano makes saddles, belts that outlast the pants, and on Thursdays, custom harnesses. Lebanese father, Abruzzese mother, twenty years in leather under old-guard men who taught him protocol is how you tell someone they're safe. Tonight is your first fitting.</span>
            </div>
            <div style="background-color:#140C0D; color: #B3A39A; padding:20px; flex: 1; min-width: 250px; border:1px solid #3A2122; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Karim Romano x Any user<br>
                    Kinktober Day 23: Leather<br>
                    Work down the kraft paper, copy a starter into chat.<br>
                    TW: Leather D/s, protocol, harness fitting, leather bondage<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- KRAFT PAPER -->
        <div style="margin-top: 35px; {PAPER} border: 1px solid #8E7150; border-radius: 4px; padding: 22px 16px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 23 · LEATHER · THURSDAY FITTING</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {GRAPHITE}; letter-spacing: 1px;">The Kraft Paper</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 20px;">Brown paper, flat pencil, cloth tape coiled on top. Before any tape goes on you.</div>
{steps}
            <div style="margin-top: 14px; border-top: 1px solid #8E7150; padding-top: 12px; color: {GRAPHITE}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">THURSDAYS</span>
                Garage door stays down. Side door only. Nobody walks in on a fitting. The saddle under the drop cloth is somebody else's forty years.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Bring the boots Thursday. ~K.R.</div>
        </div>

        <details style="margin-top: 30px; background: #1F1314; padding: 12px 20px; border-radius: 8px; border: 1px solid #3A2122; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #4A2C2D; padding-top: 12px; color: #A8988F;">
                Old-guard leather. Expect protocol and titles, harness fitting, inspection, service, leather cuffs and straps, and sex inside the written limits. All characters are adults. Say stop and he unbuckles, no questions first.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Karim Romano (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
