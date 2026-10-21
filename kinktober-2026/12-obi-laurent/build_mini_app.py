import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Obi Laurent banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

TAG, INK, MUTED, EMBER, GLASS, ICE = "#F1F0EA", "#1F2224", "#73797C", "#C8501A", "#2E8A86", "#5B8FB0"
STEEL = ("background-color: #A9B0B3; background-image: repeating-linear-gradient(90deg, rgba(255,255,255,0.10) 0px, "
         "rgba(255,255,255,0.10) 1px, rgba(0,0,0,0.04) 2px, rgba(0,0,0,0) 4px);")

def starter(text):
    return f'''
                        <div style="background: #FFFFFF; border-left: 3px solid {GLASS}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def obi(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {EMBER};">Obi:</strong>&nbsp;“{esc(line)}”</div>'

def step(num, temp, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #E7E8E3; border: 1px solid #C3C7C4; border-left: 5px solid {temp}; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.88em; color: {temp}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #C9CCC8; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def row(item, rule):
    return f'<div style="display: flex; gap: 10px; justify-content: space-between; border-bottom: 1px dotted #B8BCB8; padding: 4px 0; color: {INK}; font-size: 0.95em;"><span style="font-weight: 700;">{esc(item)}</span><span style="font-family: \'Courier New\', Courier, monospace; color: {MUTED}; text-align: right;">{esc(rule)}</span></div>'

def choice(title, temp_label, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F4F4F0; border: 1px dashed #AEB4B1; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK};"><strong>{esc(title)}</strong>
                            <span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {GLASS}; margin-top: 2px;">{esc(temp_label)}</span>
                        </summary>
                        <div style="margin-top: 8px;">{obi(line)}{starter(start)}
                        </div>
                    </details>'''

s1 = row("Wax", "low-temp only · from height") + row("Oil", "warmed over water · never a stove") + \
     row("Ice", "never still · he counts") + row("Steel, glass", "body-safe · from the freezer or ice bowl") + \
     row("Anything from downstairs", "never") + \
     f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif; margin: 10px 0;">Green, keep going. Yellow, say warmer, cooler, or slower. Red, ice back in the bucket and he brings water.</div>' + \
     obi("Yes, every single thing, on my wrist first. I have a scar that says so. You can laugh. I'm still doing it in front of you, so you never have to wonder.") + \
     starter("\"Do the wrist thing. I want to watch you test it.\"")
s2 = obi("Cold. I'll count so it never sits anywhere too long. Four. Five. Six. Then it moves. Tell me the color when I ask. I want to hear you say it.") + \
     starter("\"Start cold. Count out loud.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Hot after cold. He names it before it lands.</div>' + \
     choice("The candles", "low-temp · from height · wrist first", "This one's hotter. Wrist first. One drop, watch it go cloudy. Okay. Now it's allowed near you.",
            "\"Light one of the candles. I want to see how high you hold it.\"") + \
     choice("The oil", "warmed in water · palms first", "Dousman. Here comes warm. My hands have been in the bowl a while. Say the color again. I like hearing it.",
            "\"Warm your hands in the oil. Then tell me before you touch me.\"") + \
     choice("The teal glass", "made by him · from the ice bowl", "Same teal as the vase. I made it to go in ice or warm water, nowhere else. Cold first, or do you want me to warm it?",
            "*I point at the teal piece in its bowl of ice.* \"That one. The one that looks like the vase.\"")

steps = step("01", EMBER, "Wrist First", "The rules, quick. Then he stops talking.", s1, opn=True) + \
        step("02", ICE, "Cold", "Freezer spoon, ice bucket, counted.", s2) + \
        step("03", EMBER, "Here Comes Warm", "Pick the heat.", s3)

TAGS = ["Temperature Play", "Wax and Ice", "Switch", "Kinktober Day 12", "Wrist First"]
tagpills = "\n".join(f'            <div style="background-color:#1F1712; color:#F2A36B; border: 1px solid #5E3420; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Obi Laurent - Kinktober Day 12</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0D1011; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #171B1C; border: 1px solid #2D3537; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E3E3DE; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2D3537; padding-bottom:15px; margin-bottom:25px; color: #F1F0EA; letter-spacing: 0.5px;">
            Two Thousand Degrees Downstairs
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #97A0A2; font-family: Georgia, serif;">
                “I handle fire all day. I'm very, very good at not letting it bite.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Obi Laurent" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2D3537; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#121617; color: #A9B0B1; padding:20px; flex: 1; min-width: 250px; border:1px solid #2D3537; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Laurent Glass, an old brick warehouse in the Bywater. The furnace never drops below two thousand degrees, and Obi Laurent lives in the hot loft above it. He has a burn across his left palm and a habit everyone laughs at: nothing touches you until it's touched the inside of his wrist. You met him at an art walk, in front of a teal vase. Tonight is the first time.</span>
            </div>
            <div style="background-color:#121617; color: #A9B0B1; padding:20px; flex: 1; min-width: 250px; border:1px solid #2D3537; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Obi Laurent x Any user<br>
                    Kinktober Day 12: Temperature Play<br>
                    Pick hot or cold, copy a starter into chat.<br>
                    TW: Wax, ice, warm oil, chilled metal and glass, sensation play<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- SHOP TAG ON STEEL -->
        <div style="margin-top: 35px; {STEEL} border: 1px solid #7E8689; border-radius: 10px; padding: 16px 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="height: 10px; margin: 0 6px 12px; border-radius: 5px; background: linear-gradient(90deg, {ICE}, #D9E4E8 45%, #F0C27A 65%, {EMBER});"></div>
            <div style="background: {TAG}; border-radius: 4px; padding: 20px 16px; text-align: left; box-shadow: 0 2px 6px rgba(0,0,0,0.25);">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 12 · TEMPERATURE PLAY</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">Loft Schedule</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 20px;">Everything on the low table, tested twice. On his wrist.</div>
{steps}
                <div style="margin-top: 14px; border-top: 1px solid #C3C7C4; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">SHOP NOTES</span>
                    Furnace idling. Loft at eighty-five, both fans on. Ice bucket sweating. Pikliz in the fridge if you're brave. Nothing from downstairs comes up here.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Pa pè. Tell me the color. ~O.L.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1B2021; padding: 12px 20px; border-radius: 8px; border: 1px solid #2D3537; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #3A4446; padding-top: 12px; color: #9EA6A8;">
                Temperature and sensation play: ice, low-temperature wax, warm oil, chilled steel and glass, with a dominant-leaning switch. All characters are adults. Limits are law. Every source is tested on his own wrist first, ice is counted and never left in one spot, nothing from the shop floor ever touches skin, and red stops everything: ice back in the bucket, water, and a skin check.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Obi Laurent (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
