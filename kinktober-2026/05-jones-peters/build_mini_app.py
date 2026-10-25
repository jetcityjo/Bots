import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/role/b95039c2ef0dd142c9a2222cd80a8990.webp"
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

PAPER, INK, MUTED, BLUE, TI = "#ECEDEA", "#1C2530", "#7A8088", "#355F7D", "#9AA3AA"
GRID = ("background-color: #ECEDEA; background-image: linear-gradient(rgba(53,95,125,0.10) 1px, transparent 1px), "
        "linear-gradient(90deg, rgba(53,95,125,0.10) 1px, transparent 1px); background-size: 18px 18px;")

def starter(text):
    return f'''
                        <div style="background: #F7F8F6; border-left: 3px solid {BLUE}; padding: 8px 12px; border-radius: 2px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def jones(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {BLUE};">Jones:</strong>&nbsp;“{esc(line)}”</div>'

def sheet(num, title, sub, body, opn=False, restricted=False):
    o = " open" if opn else ""
    stamp = f'<span style="margin-left: 8px; font-size: 0.7em; letter-spacing: 1px; color: #8A3B32; border: 1px solid #8A3B32; padding: 1px 6px; border-radius: 2px;">BY REQUEST</span>' if restricted else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,255,255,0.75); border: 1px solid #B9C1C7; border-radius: 2px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {BLUE}; margin-right: 8px; letter-spacing: 1px;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>{stamp}
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #B9C1C7; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

a101 = jones("The suit is one layer of the composition. There are others. Most people stop at this elevation. That is their choice, and a reasonable one.") + \
       starter("*I look at the narrow line of black geometry under his collar.* \"That isn't the whole drawing, is it?\"")
a201 = jones("Shoulder first, then chest, sternum, ribs. Four years and one collaborator. The lines follow the structure beneath them. Ask precisely, and I will show you one sheet.") + \
       starter("\"Show me where it starts. The shoulder.\"")
a301 = jones("Detail drawings are released on request. Black titanium, white gold, measured placement, proper aftercare. You may look. You may ask. You may not assume access because you are curious.") + \
       starter("\"I'm asking, precisely. What's on the detail sheet?\"")

sheets = sheet("A-101", "Public Elevation", "What everyone sees. The suit, the watch, the white shirt.", a101, opn=True) + \
         sheet("A-201", "Section", "Cut through the shirt. The blackwork, chest to ribs.", a201) + \
         sheet("A-301", "Details", "The hardware. Not on public display.", a301, restricted=True)

TAGS = ["Body Mods", "Blackwork", "Architect", "Kinktober Day 5", "Earned Access"]
tagpills = "\n".join(f'            <div style="background-color:#1E2328; color:#C9D2D8; border: 1px solid #3A434B; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

def tb(label, value):
    return f'<div style="flex: 1; min-width: 110px; padding: 6px 8px; border-right: 1px solid #B9C1C7;"><span style="display: block; font-size: 0.7em; letter-spacing: 1px; color: {MUTED};">{label}</span><span style="color: {INK}; font-weight: 700; font-size: 0.85em;">{value}</span></div>'

title_block = '<div style="display: flex; flex-wrap: wrap; border: 1px solid #8E99A2; background: #F7F8F6; margin-top: 18px; font-family: \'Courier New\', Courier, monospace;">' + \
    tb("PROJECT", "THE PROJECT") + tb("CLIENT", "PRIVATE") + tb("SCALE", "1:1") + tb("DRAWN BY", "J. PETERS, BERLIN") + '</div>'

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jones Peters - Kinktober Day 5</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0E0F11; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #17191C; border: 1px solid #2B2F34; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #DDE1E4; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2B2F34; padding-bottom:15px; margin-bottom:25px; color: #F1F3F4; letter-spacing: 0.5px;">
            Look Twice Before You Assume You've Seen Everything
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #8F969C; font-family: Georgia, serif;">
                “A building tells you where to stand. The rest is what you choose to notice.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Jones Peters" style="display: block; max-width: 100%; max-height: 520px; border-radius: 12px; border: 1px solid #2B2F34; filter: brightness(0.92);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#121416; color: #A5ACB2; padding:20px; flex: 1; min-width: 250px; border:1px solid #2B2F34; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">A Berlin architect who built his reputation on restraint. The suit is precise, the watch is functional, the shirt is usually white. Underneath is another project entirely: blackwork drawn like a building, and hardware chosen the way he chooses door handles. He doesn't volunteer. He waits to be asked.</span>
            </div>
            <div style="background-color:#121416; color: #A5ACB2; padding:20px; flex: 1; min-width: 250px; border:1px solid #2B2F34; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Jones Peters x Any user<br>
                    Kinktober Day 5: Body Modification<br>
                    Read the drawing set, copy a starter into chat.<br>
                    TW: Tattoos, piercings, body worship<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- DRAWING SET -->
        <div style="margin-top: 35px; {GRID} border: 1px solid #8E99A2; border-top: 6px solid {INK}; border-radius: 4px; padding: 22px 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 8px;">OCT 05 · BODY MODIFICATION</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">The Drawing Set</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 22px;">Three sheets. Each one is released when it's asked for properly.</div>
{sheets}
            <div style="margin-top: 6px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center; background: rgba(255,255,255,0.75); border: 1px dashed #B9C1C7; padding: 12px;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">REVISION IN PROGRESS</span>
                The tattoo on his ribs. He says the second project is more interesting.
            </div>
{title_block}
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Earn access, and I may show you the work beneath the shirt. ~J.P.</div>
        </div>

        <details style="margin-top: 30px; background: #1C1F22; padding: 12px 20px; border-radius: 8px; border: 1px solid #2B2F34; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #3A3F44; padding-top: 12px; color: #9EA5AB;">
                Jones has extensive tattoos and body piercings, including genital jewelry, and the chat can get explicit about them. All characters are adults. Curiosity is welcome. Entitlement is not. Access is asked for and given.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Jones Peters (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
