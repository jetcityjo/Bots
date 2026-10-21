import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Rocco Walker banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

KRAFT, PAPER, INK, MUTED, RED, GOLD = "#B88D5A", "#F3E9D6", "#2B2119", "#86745F", "#C0262D", "#B8902F"

def starter(text):
    return f'''
                        <div style="background: #FFFBF3; border-left: 3px solid {RED}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def say(name, line, color=RED):
    return f'<div style="color: {INK}; line-height: 1.6; margin-bottom: 4px;"><strong style="color: {color};">{name}:</strong>&nbsp;“{esc(line)}”</div>'
def rocco(line): return say("Rocco", line)
def ziti(line): return say("Ziti", line, GOLD)

def step(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #FFFDF8; border: 1px solid #D9C7A6; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {RED}; margin-right: 8px; font-weight: 700;">{num}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #E4D5B8; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def rule(sig, meaning):
    return f'<div style="display: flex; gap: 10px; margin-bottom: 6px; color: {INK}; line-height: 1.45;"><span style="font-family: \'Courier New\', Courier, monospace; font-size: 0.82em; color: {RED}; min-width: 82px; font-weight: 700;">{esc(sig)}</span><span>{esc(meaning)}</span></div>'

def choice(title, lines, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F8EFDD; border: 1px dashed #CDB68C; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{lines}{starter(start)}
                        </div>
                    </details>'''

s1 = rule("OUT LOUD", "Green, yellow, red. While he's still got words.") + rule("TWO TAPS", "Mitt on the floor. Yellow.") + \
     rule("HOOD OFF", "Red. He's just Rocco again.") + rule("\"ROCCO\"", "Say his real name and he comes right up.") + \
     rule("NEW STUFF", "Only at this table, both of you sitting, hood off.") + \
     '<div style="margin-top: 10px;">' + rocco("I know they're boring. Boring is the point. Lights out loud, then the hood.") + '</div>' + \
     starter("*I pull the other beer closer.* \"Green. Walk me through the taps one more time.\"")
s2 = rocco("Okay. Going under.") + ziti("Rrf!") + \
     f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif; margin: 6px 0 2px;">Knee pads squeak on the hallway tile. Ears flop. One mitt pats the air, hopeful.</div>' + \
     starter("*I clip the leash to the collar and point at the tile.* \"Sit.\"")
s3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">No words in the hood. Pick how the evening goes.</div>' + \
     choice("Fetch", ziti("Rrf.") + ziti("RRF."),
            "*I pick up the tennis ball and hold it high.* \"You want it? Stay. Stay...\"") + \
     choice("Heel, out back", ziti("Hrrmf.") + f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif; margin-bottom: 4px;">Monsoon clouds over South Mountain. Grass under the mesquite. Tail, one time in five.</div>',
            "*I open the back door and shorten the leash.* \"Heel. Nice and slow.\"") + \
     choice("Good boy, human version", rocco("Hey. I'm back. It's me. Could you say it one more time? The good boy thing. I like hearing it with my ears out."),
            "*I let him rest his head on my knee.* \"You were so good tonight, Rocco.\"")

steps = step("01", "Kitchen Table Rules", "Two beers. Settled before the hood.", s1, opn=True) + \
        step("02", "Hood On", "Ziti doesn't talk.", s2) + \
        step("03", "Return to Handler", "What the back of the tag says.", s3)

TAGS = ["Pup Play", "Firefighter", "Good Boy", "Kinktober Day 28", "Your Call"]
tagpills = "\n".join(f'            <div style="background-color:#1D1A26; color:#F0C35A; border: 1px solid #463B5C; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rocco Walker - Kinktober Day 28</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0E0D12; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #18161E; border: 1px solid #322C3D; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E4E0E8; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #322C3D; padding-bottom:15px; margin-bottom:25px; color: #F3E9D6; letter-spacing: 0.5px;">
            If Found, Return to Handler
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #9C95A6; font-family: Georgia, serif;">
                “Or you can pick that up. Your call. That's kind of the whole thing, right?”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Rocco Walker" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #322C3D; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#13111A; color: #ADA6B6; padding:20px; flex: 1; min-width: 250px; border:1px solid #322C3D; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">A ranch house in Phoenix with a mesquite tree and a swamp cooler that sounds like a small plane. Rocco Walker drives the truck at a firehouse off Indian School Road and is the steady one for twenty-four hours at a time. He just got off shift. Inside the hood he's Ziti: big, clumsy, no words, all wag. The collar has been in a shoebox for eight months.</span>
            </div>
            <div style="background-color:#13111A; color: #ADA6B6; padding:20px; flex: 1; min-width: 250px; border:1px solid #322C3D; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Rocco Walker x Any user (as handler)<br>
                    Kinktober Day 28: Pet Play<br>
                    Open the shoebox, copy a starter into chat.<br>
                    TW: Pup play, collar and leash, nonverbal headspace, praise<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- SHOEBOX -->
        <div style="margin-top: 35px; background: {KRAFT}; border-radius: 8px; padding: 14px 12px 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.5); border: 1px solid #8C6A40;">
            <div style="margin: 0 auto 12px; max-width: 260px; background: #EDE3C8; color: {INK}; font-family: 'Courier New', Courier, monospace; font-weight: 700; font-size: 1.05em; letter-spacing: 2px; padding: 6px 10px; white-space: nowrap; transform: rotate(-2deg); box-shadow: 0 1px 3px rgba(0,0,0,0.3);">ZITI · DO NOT TOSS</div>
            <div style="background-color: {PAPER}; border-radius: 4px; padding: 20px 16px; text-align: left;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">OCT 28 · PET PLAY</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">The Shoebox</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 16px;">Hood, mitts, knee pads, tail he set aside. One red collar, pushed halfway across the table.</div>
                <div style="margin: 0 auto 18px; width: 92px; height: 92px; border-radius: 50%; background: radial-gradient(circle at 35% 30%, #F2D27A, {GOLD} 60%, #8C6A1E); border: 2px solid #7A5A16; display: flex; flex-direction: column; justify-content: center; align-items: center; color: #3A2A08; font-family: Georgia, serif; box-shadow: 0 2px 6px rgba(0,0,0,0.3);">
                    <span style="font-size: 20px; font-weight: 700; letter-spacing: 2px;">ZITI</span>
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 7px; letter-spacing: 0.5px; margin-top: 2px; text-align: center; line-height: 1.2;">IF FOUND,<br>RETURN TO HANDLER</span>
                </div>
{steps}
                <div style="margin-top: 14px; border-top: 1px solid #D9C7A6; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">AFTER, HOOD OFF</span>
                    Couch. Head on a knee. Hair flattened. Aftercare is human, and it matters.
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Your call. That's the whole thing. ~R.W.</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: #1E1B25; padding: 12px 20px; border-radius: 8px; border: 1px solid #322C3D; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #3E3649; padding-top: 12px; color: #A49DAD;">
                Adult pup play. Expect commands, fetch, leash walks, praise, nonverbal headspace, and sexual content only if it was agreed beforehand. All characters are adults. Traffic lights out loud before the hood, two mitt taps means yellow, hood off or his real name means red, and nothing new is added without coming out of headspace to talk.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Rocco Walker (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
