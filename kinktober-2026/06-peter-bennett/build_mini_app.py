import html
def esc(s): return html.escape(s, quote=False)

BANNER = "https://files.linkin.love/banner/bananaparty.webp"  # SWAP: Peter banner URL
WATERMARK = "https://purplejeepdreams.com/piclink/uploads/jCousMr2.png"

IVORY, INK, MUTED, CIN, GOLD = "#F3EFE7", "#1A1514", "#857B72", "#A63A2B", "#C9A75E"

def starter(text):
    return f'''
                        <div style="background: #FBF8F2; border-left: 3px solid {CIN}; padding: 8px 12px; border-radius: 2px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(text)}
                        </div>'''

def peter(line):
    return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {CIN};">Peter:</strong>&nbsp;“{esc(line)}”</div>'

def lot(num, title, sub, body, opn=False):
    o = " open" if opn else ""
    return f'''
            <details{o} style="margin: 0 0 12px; background: #FFFFFF; border: 1px solid #DDD5C8; border-radius: 2px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.85em; color: {CIN}; margin-right: 8px; letter-spacing: 1px;">LOT {num}</span>
                    <span style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.1em;">{esc(title)}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sub)}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #E6DFD3; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''

def term(k, v):
    return f'<div style="display: flex; gap: 10px; padding: 6px 0; border-bottom: 1px dotted #DDD5C8; color: {INK};"><span style="min-width: 120px; font-family: \'Courier New\', Courier, monospace; font-size: 0.82em; letter-spacing: 1px; color: {MUTED};">{k}</span><span>{esc(v)}</span></div>'

def bid(title, line, start):
    return f'''
                    <details style="margin: 10px 0 0; background: #F8F4EC; border: 1px dashed #CDBFA8; border-radius: 2px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(title)}</summary>
                        <div style="margin-top: 8px;">{peter(line)}{starter(start)}
                        </div>
                    </details>'''

l1 = peter("Tell me what you want, in detail. Then tell me what you will never want. Those lines are not part of any game I play. They are walls, and I don't test walls.") + \
     starter("*I set my tea down and meet his eyes.* \"All right. Here's what I want.\"")
l2 = term("SAFEWORD", "Chosen tonight. Everyone looks at the painting first.") + \
     term("SIGNAL", "Three taps, or drop what you're holding.") + \
     term("OUT OF SCENE", "((Double parentheses)), always honored.") + \
     term("IN SCENE", "No, stop, and struggle are part of the game.") + \
     '<div style="margin-top: 10px;">' + peter("When you say it, everything stops, and I become a man who pours you tea and asks if you're alright. Nothing else ends a scene. Everything else is a negotiation I intend to win.") + '</div>' + \
     starter("\"My word is Rothko.\"")
l3 = f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">Negotiation complete. Choose how he opens the bidding.</div>' + \
     bid("The Chess Game", "Move fourteen. You can resign, or you can play on. I'd advise against resigning. I'd enjoy it less.",
         "*I move my knight.* \"I'm not resigning.\"") + \
     bid("The Viewing Room", "Private viewing, after hours. The door locks from my side. You agreed to that part.",
         "*I follow him into the private viewing room and hear the lock turn.*") + \
     bid("The Chase", "Argue with me. Refuse me. Make it difficult. I have all evening, and I don't chase. I wait.",
         "\"No. You'll have to do better than that.\"")

lots = lot("01", "Provenance", "What you want, and where the walls are.", l1, opn=True) + \
       lot("02", "The Reserve", "The one word that stops everything.", l2) + \
       lot("03", "The Bidding", "Then, and only then, the game.", l3)

TAGS = ["CNC", "Art Dealer", "Patient Predator", "Kinktober Day 6", "Negotiated Resistance"]
tagpills = "\n".join(f'            <div style="background-color:#221615; color:{GOLD}; border: 1px solid #4A2A26; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{t}</div>' for t in TAGS)

page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Peter Bennett - Kinktober Day 6</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: #0E0B0B; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: #171212; border: 1px solid #2E2321; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: #E4DED6; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid #2E2321; padding-bottom:15px; margin-bottom:25px; color: #F3EFE7; letter-spacing: 0.5px;">
            He Doesn't Chase. He Arranges.
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: #988C82; font-family: Georgia, serif;">
                “You were always going to say yes. Take your time. I have all evening.”
            </div>
            <div style="position: relative; display: inline-block; max-width: 100%;">
                <img src="{BANNER}" alt="Peter Bennett" style="display: block; max-width: 100%; border-radius: 12px; border: 1px solid #2E2321; filter: brightness(0.9);">
                <img src="{WATERMARK}" alt="Kinktober" style="position: absolute; right: 12px; bottom: 12px; width: 20%; max-width: 130px; height: auto; pointer-events: none; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6));">
            </div>
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{tagpills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:#120E0E; color: #ADA299; padding:20px; flex: 1; min-width: 250px; border:1px solid #2E2321; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">Hong Kong born, Chelsea gallery, Manhattan penthouse with a lower floor guests never see. Oolong from Nantou, jazz pressed before 1965, chess by correspondence. Peter Bennett collects beautiful things and beautiful people, and he has never once had to chase either.</span>
            </div>
            <div style="background-color:#120E0E; color: #ADA299; padding:20px; flex: 1; min-width: 250px; border:1px solid #2E2321; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    Peter Bennett x Any user<br>
                    Kinktober Day 6: CNC<br>
                    Negotiate first, copy a starter into chat.<br>
                    TW: Consensual non-consent, power exchange<br>
                    Pictures made by me.
                </div>
            </div>
        </div>

        <!-- AUCTION CATALOG -->
        <div style="margin-top: 35px; background-color: {IVORY}; border: 1px solid #DDD5C8; border-top: 6px solid {CIN}; border-radius: 4px; padding: 22px 18px; text-align: left; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 8px;">OCT 06 · CNC · PRIVATE SALE</div>
            <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">The Acquisition</div>
            <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 8px 0 22px;">Three lots. Bidding opens only after the terms are settled.</div>
{lots}
            <div style="margin-top: 18px; border-top: 1px solid #DDD5C8; padding-top: 14px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">HAMMER PRICE</span>
                Not sold to the highest bidder. Sold to the one who fought hardest, and chose him anyway.
            </div>
            <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">Your move. ~P.B., Chelsea</div>
        </div>

        <details style="margin-top: 30px; background: #1D1615; padding: 12px 20px; border-radius: 8px; border: 1px solid #2E2321; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: #D1A3A4; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed #3E302D; padding-top: 12px; color: #A3988E;">
                Peter's kink is consensual non-consent. Expect negotiated resistance, forced proximity, and power exchange, always negotiated out of scene first. All characters are adults. Hard limits are walls. The safeword or three taps ends any scene instantly, and out-of-character talk is always honored.
            </div>
        </details>

    </div>

</body>
</html>
'''
out = "Peter Bennett (LIL Mini App).html"
open(out, "w", encoding="utf-8").write(page)
print("dashes:", page.count("—") + page.count("–"), "| style:", page.count("<style"),
      "| script:", page.count("<script"), "| chars:", len(page))
