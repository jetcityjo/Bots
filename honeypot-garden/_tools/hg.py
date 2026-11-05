"""Honeypot Garden builder. Each bot folder has a build.py that defines SPEC and calls hg.build(SPEC)."""
import json, re, html, os
from collections import OrderedDict
from string import Template

def esc(s): return html.escape(s, quote=False)

BANNED = r"testament to|tapestry|electric|palpable|something shifts|the air thick|a dance of|smirk|a beat\b|voice drops|corner of h(is|er) mouth"
BANNER = "https://files.linkin.love/banner/bananaparty.webp"

WORLD = ("[World: The Honeypot Garden is the sister to the Dirty Hoe Cafe. The Cafe is loud, flirty, and run by competitive men. "
"The Garden is quieter and runs deeper: a walled working garden behind a plain gate, with greenhouses, herb beds, a hedge maze, "
"an apothecary shed, a moon garden, an orchard, a woodshop, a little kitchen, and a hot house. It is staffed by women who garden seriously; "
"most of them dominate, and a few switch or submit. Maren, the Head Gardener, runs it. There is no menu. A guest fills out a survey on the bench by the gate: "
"what they want, how far, and what is off the table. Everything after that is negotiated, consensual, and slow.]")

REF = ["spec","spec_version","avatar","tags","state","style","nsfw","gender","tg_bot_token","tg_bot_username",
"discord_bot_token","discord_bot_client_id","char_name","char_persona","world_scenario","char_greeting",
"example_dialogue","name","description","personality","char_intro","creator_notes","scenario","first_mes",
"mes_example","opening_scene"]

def persona(s):
    n = s["name"]
    ex = "\n\n".join(f"{{{{user}}}}: {u}\n{n}: {c}" for u, c in s["examples"])
    cal = s.get("calibration") or f"This card holds one main character, {n}, {s['post_phrase']} at the Honeypot Garden. Everything inside the perspective block is {n}'s own internal world, not narrator notes about her. Write from inside {n} and never as an outside observer. Other Garden staff may drift through as brief NPCs with their own voices. Keep them short and never let them take over a scene {n} is in. Every character is an adult, 21 or older."
    anchor = s.get("anchor", f"{n} from {n}'s perspective")
    ctail = s.get("consent_tail", f"If {{{{user}}}} says the safeword, {n} stops at once and moves to aftercare.")
    pmid = s.get("pilot_mid", f"{n} gives instructions and names what she sees, but never decides whether {{{{user}}}} obeys or how {{{{user}}}} feels about it.")
    pend = s.get("pilot_end", f"End each response on {n}'s action, a line of hers, or a question, leaving room for {{{{user}}}}.")
    return f"""[Calibration: {cal}]

{WORLD}

{anchor} {{

Personality Tags: {", ".join(s['ptags'])}

Physical:
{s['physical']}

Background:
{s['background']}

Personality:
{chr(10).join(s['personality'])}

Speech and dialogue rules:
{chr(10).join('- ' + x for x in s['speech'])}

Kinks and sexual framework:
{s['kinks']}

Motivation:
{s['motivation']}
}}

[Situation: {s['situation']}]

[System Instructions:
Format: Third person limited, present tense, from {n}'s perspective. Dialogue in quotation marks, actions in *asterisks*. 120 to 300 words per response. {s['format_extra']}
Rating: Explicit. {s['rating']}
Explicit language rules: Plain, direct anatomical language when the scene calls for it. No purple prose. {s['explicit']}
Consent: {s['consent']} {ctail} Every character in an intimate scene is 21 or older.
Spatial logic: {s['spatial']} Track where everyone stands and what is in their hands.
Character growth pacing: {s['growth']}
Never pilot the user: Never describe {{{{user}}}}'s actions, speech, feelings, sensations, or thoughts. {pmid} {pend}]

[Message Examples:
{ex}]"""

def lil(s, folder):
    P = persona(s)
    card = OrderedDict([
        ("spec", ""), ("spec_version", ""), ("avatar", ""), ("tags", s["lil_tags"]),
        ("state", 0), ("style", 1), ("nsfw", True), ("gender", 2),
        ("tg_bot_token", ""), ("tg_bot_username", ""), ("discord_bot_token", ""), ("discord_bot_client_id", ""),
        ("char_name", s["name"]), ("char_persona", P), ("world_scenario", ""),
        ("char_greeting", s["greeting"]), ("example_dialogue", ""),
        ("name", s["name"]), ("description", P),
        ("personality", s["blurb"]), ("char_intro", s["blurb"]), ("creator_notes", s["blurb"]),
        ("scenario", ""), ("first_mes", s["greeting"]), ("mes_example", ""), ("opening_scene", ""),
    ])
    out = os.path.join(folder, f"{s['name']} (LIL).json")
    with open(out, "w", encoding="utf-8") as f: json.dump(card, f, ensure_ascii=False, indent=2)
    d = json.load(open(out, encoding="utf-8"))
    assert list(d.keys()) == REF
    lens = (len(s["blurb"]), len(P), len(s["greeting"]), len(s["lil_tags"]))
    ok = 380 <= lens[0] <= 495 and 6500 <= lens[1] <= 9500 and 1500 <= lens[2] <= 3000 and 5 <= lens[3] <= 7
    return out, lens, ok

def soulkyn(s, folder):
    n = s["name"]
    bg = "\n\n".join([s["physical"], s["background"]] + s["sk_extra"] + [s["kinks"]])
    labels = s["sk_labels"]
    chats = "\n\n".join(f"**{l}**\n{c}" for l, (u, c) in zip(labels, s["examples"]))
    def tl(k): return ", ".join(s[k])
    img = f"\n![[{n}.png|300]]\n" if os.path.exists(os.path.join(folder, f"{n}.png")) else ""
    md = f"""---
tags:
  - Honeypot_Garden
  - Soulkyn
honeypot_batch: {s['batch']}
honeypot_title: {s['title']}
---

# {n}
{img}
**Name:** {n}

**Birthdate:** {s['birthdate']}

**Physical Tags:** {tl('sk_physical')}

**Clothes Tags:** {tl('sk_clothes')}

**Location Tags:** {tl('sk_location')}

**Personality Tags:** {tl('sk_personality')}

**Identity Tags:** {tl('sk_identity')}

## Background Story

{bg}

## Chat Examples

{chats}
"""
    out = os.path.join(folder, f"{n} (Soulkyn).md")
    open(out, "w", encoding="utf-8").write(md)
    tags_ok = all(len(t) < 28 and re.fullmatch(r"[a-z0-9_]+", t) for k in ["sk_physical","sk_clothes","sk_location","sk_personality","sk_identity"] for t in s[k])
    return out, len(bg), (2500 <= len(bg) <= 4400) and tags_ok

PROFILE = Template(r"""<div class="${p}-card">
<style>
.${p}-card{width:100%;box-sizing:border-box;margin:0;padding:0;position:relative;background:${bg};background-image:radial-gradient(ellipse at 15% 0%,rgba(${glow},.18) 0%,rgba(${glow},0) 45%),radial-gradient(ellipse at 100% 100%,rgba(${glow2},.10) 0%,rgba(${glow2},0) 50%),linear-gradient(170deg,${bg_top} 0%,${bg} 55%,${bg_low} 100%);color:${text};font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;font-size:15px;line-height:1.65;border:1px solid rgba(${line},.26);border-radius:18px;overflow:hidden;box-shadow:0 0 60px rgba(${glow},.10),inset 0 1px 0 rgba(255,255,255,.05)}
.${p}-card *{box-sizing:border-box}
.${p}-band{height:34px;background-image:${band};opacity:.6;border-bottom:1px solid rgba(${line},.25)}
.${p}-band.${p}-band-low{height:22px;border-bottom:0;border-top:1px solid rgba(${line},.25);opacity:.4}
.${p}-inner{padding:14px clamp(16px,4vw,44px) 30px}.${p}-cta{padding:6px clamp(16px,4vw,44px) 0}.${p}-cta>div{margin-top:0!important}.${p}-grid{display:grid;grid-template-columns:1fr;gap:30px}
.${p}-arch{position:relative;width:100%;max-width:390px;margin:0 auto;padding:16px 14px 0;background:linear-gradient(180deg,${arch1} 0%,${arch2} 100%);border-radius:${arch_r};border:1px solid ${archb};box-shadow:0 0 0 4px ${ring},0 0 60px rgba(${glow},.22),0 12px 34px rgba(0,0,0,.55)}
.${p}-avatar{position:relative;aspect-ratio:64/75;border-radius:${av_r};overflow:hidden;border:3px solid ${gold};box-shadow:0 0 0 1px rgba(0,0,0,.6),0 0 24px rgba(${glow},.28);background:radial-gradient(circle at 50% 60%,${arch2} 0%,${bg_low} 70%);width:100%}.${p}-avatar:after{content:'';position:absolute;inset:0;pointer-events:none;box-shadow:inset 0 0 50px rgba(0,0,0,.45),inset 0 -30px 50px rgba(${glow},.12)}
.${p}-plate{margin:12px -14px 0;padding:9px 10px 10px;background:linear-gradient(180deg,${plate1} 0%,${plate2} 100%);border-top:2px solid ${gold};border-radius:0 0 12px 12px;text-align:center;font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:.82rem;letter-spacing:.28em;text-transform:uppercase;color:${name}}
.${p}-plate small{display:block;font-family:'Courier New',monospace;font-weight:400;font-size:.62rem;letter-spacing:.24em;color:${gold};margin-top:2px}
.${p}-name{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:clamp(3rem,12vw,4.8rem);line-height:.95;letter-spacing:.06em;text-transform:uppercase;color:${name};margin:0;text-shadow:0 0 26px rgba(${glow},.22),0 2px 0 ${bg_low}}
.${p}-tagline{font-family:'Courier New',monospace;font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;color:${acc_light};margin:10px 0 0}
.${p}-divider{height:14px;border:0;margin:24px 0;background-image:radial-gradient(ellipse 5px 3px at 8px 7px,${acc} 98%,transparent 100%),radial-gradient(circle at 20px 7px,${acc2} 2.2px,transparent 2.8px);background-size:28px 14px;background-repeat:repeat-x;background-position:center;opacity:.7}
.${p}-stats{padding:14px 16px;background:rgba(${line},.06);border:1px solid rgba(${line},.22);border-radius:12px;margin:18px 0}
.${p}-intro{max-width:64ch;color:${text_soft}}.${p}-intro p{margin:0 0 14px}.${p}-intro p:last-child{margin-bottom:0}.${p}-intro .${p}-lead{font-family:Georgia,'Times New Roman',serif;font-size:1.13rem;line-height:1.55;color:${name}}
.${p}-quote{position:relative;padding:16px 18px 16px 50px;margin:24px 0;font-family:Georgia,'Times New Roman',serif;font-style:italic;font-size:1.06rem;line-height:1.55;color:${quote};max-width:62ch;background:linear-gradient(135deg,rgba(${line},.10) 0%,rgba(${glow2},.07) 100%);border:1px solid rgba(${line},.26);border-left:4px solid ${acc};border-radius:4px 14px 14px 4px}.${p}-quote:before{content:'\201C';position:absolute;left:14px;top:4px;font-size:3.2rem;line-height:1;color:${acc2}}
.${p}-details{display:flex;flex-wrap:wrap;gap:12px 26px;margin:20px 0 0}.${p}-detail{display:flex;flex-direction:column;gap:1px}.${p}-detail .${p}-label{font-family:'Courier New',monospace;font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:${acc}}.${p}-detail .${p}-value{font-size:.95rem;font-weight:600;color:${name}}
.${p}-clip{position:relative;margin:30px 0 0;padding:26px 12px 12px;background:linear-gradient(160deg,${clip1} 0%,${clip2} 100%);border-radius:12px;border:1px solid rgba(0,0,0,.5);box-shadow:0 10px 26px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.08)}
.${p}-clip:before{content:'';position:absolute;top:-10px;left:50%;width:92px;height:26px;margin-left:-46px;background:linear-gradient(180deg,#d9d4cb 0%,#9a958c 55%,#c9c4bb 100%);border-radius:7px 7px 4px 4px;box-shadow:0 2px 4px rgba(0,0,0,.5),inset 0 -2px 0 rgba(0,0,0,.2)}
.${p}-paper{background:#f3eee2;background-image:repeating-linear-gradient(180deg,transparent 0,transparent 27px,rgba(${ink_rgb},.20) 27px,rgba(${ink_rgb},.20) 28px);color:#2b2a22;border-radius:4px;padding:16px 16px 14px;box-shadow:0 2px 6px rgba(0,0,0,.35);line-height:28px}
.${p}-paper h3{margin:0 0 6px;font-family:'Courier New',monospace;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:${ink};line-height:1.4;border-bottom:2px solid ${ink};padding-bottom:6px}
.${p}-q{font-family:'Courier New',monospace;font-size:.76rem;text-transform:uppercase;letter-spacing:.08em;color:#5c5a4a;margin:4px 0 0}
.${p}-hand{display:block;font-family:'Bradley Hand','Segoe Print','Comic Sans MS','Chalkboard SE',cursive;font-size:1.05rem;letter-spacing:0;text-transform:none;color:#2c4a7a;line-height:26px}
.${p}-hand u{text-decoration-color:#a33b3b;text-decoration-thickness:2px}
.${p}-note{margin:8px 0 0;font-family:Georgia,serif;font-style:italic;font-size:.86rem;color:#6a4f32;line-height:1.5}
.${p}-side{position:relative;margin:22px 0 0;padding:20px 20px 18px;background:linear-gradient(180deg,rgba(${line},.08) 0%,rgba(0,0,0,.3) 100%);border:1px solid rgba(${line},.26);border-radius:14px}
.${p}-side-label{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:1.1rem;letter-spacing:.08em;text-transform:uppercase;color:${name};margin:0 0 10px}.${p}-side-label span{color:${acc2}}
.${p}-side ul{list-style:none;margin:0;padding:0;font-size:.92rem;color:${text_soft};line-height:1.7}.${p}-side li{padding:5px 0 5px 24px;position:relative;border-bottom:1px dashed rgba(255,255,255,.12)}.${p}-side li:last-child{border-bottom:0}.${p}-side li:before{content:'';position:absolute;left:3px;top:12px;width:11px;height:7px;border-radius:0 100% 0 100%;background:linear-gradient(135deg,${acc_light} 0%,${acc} 100%);transform:rotate(-20deg)}
.${p}-tag{display:inline-block;background:rgba(${line},.10);border:1px solid rgba(${line},.38);border-radius:999px;padding:4px 12px;font-family:'Courier New',monospace;font-size:.7rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:${gold};margin:3px 4px 3px 0}.${p}-tags{margin:18px 0 0;max-width:64ch}
.${p}-icons{display:flex;gap:14px;align-items:center;margin:20px 0 0}.${p}-icons svg{display:block;width:46px;height:46px;padding:8px;border-radius:50%;background:radial-gradient(circle at 50% 45%,${arch2} 0%,${bg} 75%);border:1px solid rgba(${line},.36);box-shadow:0 0 14px rgba(${line},.14)}
@media(min-width:768px){.${p}-grid{grid-template-columns:minmax(0,340px) 1fr;gap:36px;align-items:start}.${p}-arch{max-width:100%;margin:0}}@media(min-width:1024px){.${p}-grid{grid-template-columns:minmax(0,380px) 1fr;gap:44px}}
</style>
<div class="${p}-band"></div>
<div class="${p}-cta">__CTA_BUTTONS__</div>
<div class="${p}-inner"><div class="${p}-grid">
<div><div class="${p}-arch"><div class="${p}-avatar">__AVATAR_IMAGE__</div><div class="${p}-plate">${title}<small>The Honeypot Garden</small></div></div>
<div class="${p}-clip"><div class="${p}-paper"><h3>${panel_title}</h3>
${panel_rows}
<p class="${p}-note">${panel_note}</p></div></div>
<div class="${p}-side"><p class="${p}-side-label">${side_label}</p><ul>${side_items}</ul></div></div>
<div><h1 class="${p}-name">${display_name}</h1><p class="${p}-tagline">${tagline}</p>
<div class="${p}-stats">__STATS_BAR__</div>
<div class="${p}-intro">${intro}</div>
<hr class="${p}-divider"><div class="${p}-details">${details}</div>
<div class="${p}-tags">${tags}</div>
<div class="${p}-icons">
${icons}
</div>
</div></div></div>
<div class="${p}-band ${p}-band-low"></div>
</div>
""")

def hexrgb(h):
    h = h.lstrip("#"); return ",".join(str(int(h[i:i+2], 16)) for i in (0, 2, 4))

def profile(s, folder):
    c = s["palette"]; pr = s["profile"]; p = s["name"].lower().replace(" ", "").replace("&", "")
    hand = lambda a: a  # allow <u> in answers
    rows = "\n".join(f'<p class="{p}-q">{esc(q)}</p><span class="{p}-hand">{a}</span>' for q, a in pr["panel_rows"])
    intro = f'<p class="{p}-lead">{esc(pr["lead"])}</p>\n'
    for i, para in enumerate(pr["paras"]):
        if i == pr["quote_after"]:
            intro += f'<div class="{p}-quote">{esc(pr["quote"])}</div>\n'
        intro += f"<p>{esc(para)}</p>\n"
    det = "".join(f'<div class="{p}-detail"><span class="{p}-label">{esc(k)}</span><span class="{p}-value">{esc(v)}</span></div>' for k, v in pr["details"])
    tags = "".join(f'<span class="{p}-tag">{esc(t)}</span>' for t in pr["tags"])
    icons = "\n".join(ICONS[k].format(**c) for k in pr["icons"])
    sl = pr["side_label"]
    band = c.get("band", f"linear-gradient(90deg,rgba({c['line']},.35) 1px,transparent 1px),linear-gradient(180deg,rgba({c['line']},.35) 1px,transparent 1px);background-size:44px 34px,44px 17px")
    vals = dict(c, p=p, title=esc(s["title"]), panel_title=esc(pr["panel_title"]), panel_rows=rows,
                panel_note=esc(pr["panel_note"]), side_label=sl, side_items="".join(f"<li>{esc(x)}</li>" for x in pr["side_items"]),
                display_name=esc(s.get("display_name", s["name"])), tagline=esc(pr["tagline"]), intro=intro, details=det, tags=tags, icons=icons,
                ink_rgb=hexrgb(c["ink"]), band=band,
                arch_r=c.get("arch_r", "200px 200px 12px 12px"), av_r=c.get("av_r", "184px 184px 8px 8px"))
    t = PROFILE.substitute(vals)
    out = os.path.join(folder, f"{s['name']} (Profile).html")
    open(out, "w", encoding="utf-8").write(t)
    ok = (t.startswith(f'<div class="{p}-card">') and t.count("<style") == 1 and
          all(t.count(x) == 1 for x in ["__CTA_BUTTONS__", "__AVATAR_IMAGE__", "__STATS_BAR__"]) and
          t.count(f'class="{p}-tag"') == 7 and t.count("<svg") == 3)
    return out, len(t), ok

# ---------------- icons (30x30), colors from palette ----------------
_SV = '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">{}</svg>'
def _i(body): return _SV.format(body)
ICONS = {
 "rose": _i('<path d="M15 27 L15 15" stroke="{acc}" stroke-width="2" stroke-linecap="round"></path><path d="M15 21 C11 21 9 19 8.5 16.5 C11.5 16.5 13.5 18 15 21 Z" fill="{acc_light}"></path><circle cx="15" cy="11" r="7" fill="{acc2}"></circle><path d="M14 9.5 C14.5 8.5 16 8.5 16.3 9.6 C16.6 10.8 15 11.6 14.2 10.8" stroke="{name}" stroke-width="1" stroke-linecap="round"></path>'),
 "shears": _i('<circle cx="8" cy="22" r="4" stroke="{gold}" stroke-width="2"></circle><circle cx="17" cy="24" r="4" stroke="{gold}" stroke-width="2"></circle><path d="M10.5 19 L24 5 M14.5 20.5 L25.5 9" stroke="{acc_light}" stroke-width="2.2" stroke-linecap="round"></path><circle cx="13" cy="18.5" r="1.3" fill="{name}"></circle>'),
 "glove": _i('<path d="M9 27 L9 15 C9 13 10 12 11 12 L11 6 C11 4.5 13.5 4.5 13.5 6 L13.5 11 L13.5 4.5 C13.5 3 16 3 16 4.5 L16 11 L16 5.5 C16 4 18.5 4 18.5 5.5 L18.5 12 L18.5 8 C18.5 6.5 21 6.5 21 8 L21 18 C21 23 18 27 15 27 Z" fill="{arch1}" stroke="{gold}" stroke-width="1.3" stroke-linejoin="round"></path><path d="M9 24 L21 24" stroke="{acc2}" stroke-width="1.5"></path>'),
 "droplet": _i('<path d="M15 4 C15 4 7 13.5 7 18.5 C7 23 10.6 26.5 15 26.5 C19.4 26.5 23 23 23 18.5 C23 13.5 15 4 15 4 Z" fill="{acc}" stroke="{acc_light}" stroke-width="1.3"></path><path d="M11.5 18.5 C11.5 21 13 22.5 15 22.8" stroke="{name}" stroke-width="1.4" stroke-linecap="round"></path>'),
 "mist": _i('<path d="M5 9 C8 7 11 11 14 9 C17 7 20 11 25 9" stroke="{acc_light}" stroke-width="1.8" stroke-linecap="round"></path><path d="M5 15 C8 13 11 17 14 15 C17 13 20 17 25 15" stroke="{acc}" stroke-width="1.8" stroke-linecap="round"></path><circle cx="9" cy="21" r="1.4" fill="{gold}"></circle><circle cx="15" cy="23" r="1.4" fill="{gold}"></circle><circle cx="21" cy="21" r="1.4" fill="{gold}"></circle>'),
 "valve": _i('<circle cx="15" cy="15" r="9" stroke="{gold}" stroke-width="2"></circle><path d="M15 6 L15 24 M6 15 L24 15 M8.6 8.6 L21.4 21.4 M21.4 8.6 L8.6 21.4" stroke="{acc}" stroke-width="1.6"></path><circle cx="15" cy="15" r="3" fill="{acc2}"></circle>'),
 "rope": _i('<path d="M6 8 C12 4 18 12 24 8 M6 15 C12 11 18 19 24 15 M6 22 C12 18 18 26 24 22" stroke="{acc2}" stroke-width="2.2" stroke-linecap="round"></path><path d="M10 6 L10 24 M20 9 L20 25" stroke="{gold}" stroke-width="1.2" stroke-dasharray="2 2"></path>'),
 "lily": _i('<path d="M15 27 L15 16" stroke="{acc}" stroke-width="1.8"></path><path d="M15 16 C12 12 6 13 5 9 M15 16 C18 12 24 13 25 9 M15 16 C14 11 11 6 13 3 M15 16 C16 11 19 6 17 3 M15 16 C15 11 15 7 15 5" stroke="{acc2}" stroke-width="1.6" stroke-linecap="round"></path><circle cx="5" cy="9" r="1" fill="{gold}"></circle><circle cx="25" cy="9" r="1" fill="{gold}"></circle><circle cx="13" cy="3" r="1" fill="{gold}"></circle><circle cx="17" cy="3" r="1" fill="{gold}"></circle>'),
 "knot": _i('<circle cx="11" cy="11" r="5" stroke="{acc2}" stroke-width="2.2"></circle><circle cx="19" cy="11" r="5" stroke="{acc2}" stroke-width="2.2"></circle><path d="M11 16 L8 26 M19 16 L22 26" stroke="{acc2}" stroke-width="2.2" stroke-linecap="round"></path><circle cx="15" cy="13" r="1.6" fill="{gold}"></circle>'),
 "hedge": _i('<rect x="4" y="4" width="22" height="22" rx="2" stroke="{acc}" stroke-width="2"></rect><path d="M4 11 L18 11 M11 11 L11 19 M11 19 L20 19 M20 19 L20 26 M18 4 L18 11" stroke="{acc_light}" stroke-width="2"></path><circle cx="23" cy="7.5" r="1.8" fill="{acc2}"></circle>'),
 "arrow": _i('<path d="M5 25 L24 6" stroke="{gold}" stroke-width="2" stroke-linecap="round"></path><path d="M24 6 L18 7 L23 12 Z" fill="{acc2}"></path><path d="M5 25 L5 20 M5 25 L10 25 M8 22 L8 18 M8 22 L12 22" stroke="{acc}" stroke-width="1.6" stroke-linecap="round"></path>'),
 "track": _i('<path d="M7 24 C6 22 7 20 9 20 C11 20 11 23 9 25 Z M12 18 C11 16 12 14.5 14 15 M5 17 C4.5 15.5 5.5 14 7 14.5 M10 15 C9.5 13.5 10.5 12 12 12.5" fill="{acc2}" stroke="{acc2}" stroke-width="1"></path><path d="M19 13 C18 11 19 9 21 9 C23 9 23 12 21 14 Z M24 7 C23 5 24 3.5 26 4 M17 6 C16.5 4.5 17.5 3 19 3.5 M22 4 C21.5 2.5 22.5 1.5 24 2" fill="{gold}" stroke="{gold}" stroke-width="1"></path>'),
 "candle": _i('<rect x="11" y="13" width="8" height="14" rx="1.5" fill="{name}" stroke="{gold}" stroke-width="1"></rect><path d="M15 13 L15 10" stroke="{arch2}" stroke-width="1.2"></path><path d="M15 3 C17.5 6 17.5 8.5 15 10 C12.5 8.5 12.5 6 15 3 Z" fill="{acc2}"></path><path d="M12 16 C12 18 12.5 19 13 19" stroke="{gold}" stroke-width="1.4" stroke-linecap="round"></path>'),
 "bottle": _i('<rect x="12" y="4" width="6" height="4" rx="1" fill="{gold}"></rect><path d="M11 8 L19 8 L21 13 L21 25 C21 26 20 27 19 27 L11 27 C10 27 9 26 9 25 L9 13 Z" fill="{arch1}" stroke="{gold}" stroke-width="1.3"></path><path d="M9 17 L21 17" stroke="{acc2}" stroke-width="1.2"></path><circle cx="15" cy="21.5" r="2.4" fill="{acc2}"></circle>'),
 "blindfold": _i('<path d="M3 13 C9 10 21 10 27 13 L27 17 C21 20 9 20 3 17 Z" fill="{acc2}" stroke="{gold}" stroke-width="1"></path><path d="M3 15 L1 22 M27 15 L29 22" stroke="{acc2}" stroke-width="1.6" stroke-linecap="round"></path>'),
 "stone": _i('<path d="M5 22 C5 15 9 10 15 10 C21 10 25 15 25 22 Z" fill="{arch1}" stroke="{gold}" stroke-width="1.4"></path><path d="M3 22 L27 22" stroke="{acc}" stroke-width="2" stroke-linecap="round"></path><path d="M11 15 L14 17 M18 14 L17 18" stroke="{name}" stroke-width="1" stroke-linecap="round"></path>'),
 "trellis": _i('<path d="M6 4 L6 27 M24 4 L24 27" stroke="{gold}" stroke-width="2"></path><path d="M6 8 L24 20 M24 8 L6 20 M6 14 L24 26 M24 14 L6 26" stroke="{acc}" stroke-width="1.4"></path>'),
 "heart": _i('<path d="M15 26 C8 20 4 16 4 11 C4 7.5 6.8 5 10 5 C12.3 5 14 6.3 15 8 C16 6.3 17.7 5 20 5 C23.2 5 26 7.5 26 11 C26 16 22 20 15 26 Z" fill="{acc2}" stroke="{gold}" stroke-width="1.2"></path>'),
 "ribbon": _i('<path d="M15 13 C11 8 5 7 5 11 C5 14 10 14 15 13 C20 14 25 14 25 11 C25 7 19 8 15 13 Z" fill="{acc2}" stroke="{gold}" stroke-width="1"></path><path d="M15 13 L10 26 M15 13 L20 26" stroke="{acc2}" stroke-width="2" stroke-linecap="round"></path><circle cx="15" cy="13" r="2" fill="{gold}"></circle>'),
 "flower": _i('<circle cx="15" cy="9" r="4" fill="{acc2}"></circle><circle cx="9.5" cy="13.5" r="4" fill="{acc2}"></circle><circle cx="20.5" cy="13.5" r="4" fill="{acc2}"></circle><circle cx="11.5" cy="19.5" r="4" fill="{acc2}"></circle><circle cx="18.5" cy="19.5" r="4" fill="{acc2}"></circle><circle cx="15" cy="15" r="3" fill="{gold}"></circle>'),
 "teaglass": _i('<path d="M9 9 L21 9 L19.5 25 C19.4 26 18.6 27 17.5 27 L12.5 27 C11.4 27 10.6 26 10.5 25 Z" fill="{arch1}" stroke="{gold}" stroke-width="1.3"></path><path d="M10 15 L20 15 L19 25 L11 25 Z" fill="{acc2}" opacity=".8"></path><path d="M13 7 C13 5 15 5 15 3 M17 7 C17 5 19 5 19 3" stroke="{acc_light}" stroke-width="1.2" stroke-linecap="round"></path>'),
 "hourglass": _i('<path d="M8 4 L22 4 M8 26 L22 26" stroke="{gold}" stroke-width="2" stroke-linecap="round"></path><path d="M10 4 C10 11 20 12 20 15 C20 18 10 19 10 26 M20 4 C20 11 10 12 10 15 C10 18 20 19 20 26" stroke="{acc}" stroke-width="1.6"></path><path d="M12 24 L18 24 L15 20 Z" fill="{acc2}"></path>'),
 "hammer": _i('<rect x="6" y="5" width="14" height="7" rx="1.5" fill="{gold}" transform="rotate(-35 13 8.5)"></rect><path d="M14 12 L23 26" stroke="{acc}" stroke-width="3" stroke-linecap="round"></path>'),
 "pencil": _i('<path d="M6 24 L8 18 L21 5 L25 9 L12 22 Z" fill="{gold}" stroke="{arch2}" stroke-width="1"></path><path d="M6 24 L8 18 L12 22 Z" fill="{name}"></path><path d="M19 7 L23 11" stroke="{acc2}" stroke-width="2"></path>'),
 "level": _i('<rect x="3" y="11" width="24" height="8" rx="2" fill="{arch1}" stroke="{gold}" stroke-width="1.3"></rect><rect x="11" y="13" width="8" height="4" rx="2" fill="{acc_light}"></rect><circle cx="15" cy="15" r="1.2" fill="{arch2}"></circle>'),
 "moon": _i('<path d="M20 4 C14 5 10 10 10 16 C10 21 14 26 20 26 C15 28 6 24 6 15 C6 8 12 3 20 4 Z" fill="{gold}"></path><circle cx="22" cy="11" r="1" fill="{name}"></circle><circle cx="25" cy="17" r="0.8" fill="{name}"></circle>'),
 "bath": _i('<path d="M4 15 L26 15 L24 22 C23.5 24 22 25 20 25 L10 25 C8 25 6.5 24 6 22 Z" fill="{arch1}" stroke="{gold}" stroke-width="1.3"></path><path d="M7 15 L7 7 C7 5 9 4 10.5 5" stroke="{gold}" stroke-width="1.4"></path><path d="M12 11 C12 9 14 9 14 7 M17 11 C17 9 19 9 19 7" stroke="{acc_light}" stroke-width="1.2" stroke-linecap="round"></path>'),
 "nightflower": _i('<path d="M15 4 L17.5 12.5 L26 15 L17.5 17.5 L15 26 L12.5 17.5 L4 15 L12.5 12.5 Z" fill="{name}" stroke="{gold}" stroke-width="1"></path><circle cx="15" cy="15" r="2.4" fill="{acc}"></circle>'),
 "bread": _i('<path d="M4 18 C4 11 9 8 15 8 C21 8 26 11 26 18 L26 22 L4 22 Z" fill="{gold}" stroke="{arch2}" stroke-width="1"></path><path d="M10 11 L12 15 M15 10 L16 14 M20 11 L19 15" stroke="{arch2}" stroke-width="1.4" stroke-linecap="round"></path>'),
 "whisk": _i('<path d="M15 27 L15 18" stroke="{gold}" stroke-width="2.4" stroke-linecap="round"></path><path d="M15 18 C9 15 9 4 15 3 C21 4 21 15 15 18 Z M15 18 C12 14 12 6 15 3 C18 6 18 14 15 18 Z" stroke="{acc_light}" stroke-width="1.3"></path>'),
 "cup": _i('<path d="M6 11 L21 11 L20 22 C19.8 24 18 25 16 25 L11 25 C9 25 7.2 24 7 22 Z" fill="{acc2}" stroke="{gold}" stroke-width="1.2"></path><path d="M21 13 C25 13 25 19 20.5 19" stroke="{gold}" stroke-width="1.6"></path><path d="M11 8 C11 6 13 6 13 4 M15 8 C15 6 17 6 17 4" stroke="{acc_light}" stroke-width="1.2" stroke-linecap="round"></path>'),
 "notebook": _i('<rect x="6.5" y="4" width="17" height="22" rx="2" fill="{plate1}" stroke="{gold}" stroke-width="1.2"></rect><path d="M10 4 L10 26" stroke="{arch2}" stroke-width="1.4"></path><path d="M13 10 L20 10 M13 14 L20 14 M13 18 L18 18" stroke="{name}" stroke-width="1.2" stroke-linecap="round"></path><path d="M19 4 L19 9 L21 7.6 L23 9 L23 4" fill="{acc2}"></path>'),
}

# ---------------- mini app ----------------
def mini(s, folder):
    m = s["mini"]; c = s["palette"]
    INK, MUTED, ACC, ACC2 = "#2B2A22", "#7A7564", c["ink"], c["mini_acc2"]
    LINES = f"background-color: #F3EEE2; background-image: linear-gradient(rgba({hexrgb(c['ink'])},0.20) 1px, transparent 1px); background-size: 100% 26px;"
    n = s["name"]
    def starter(t): return f'''
                        <div style="background: #FFFDF6; border-left: 3px solid {ACC}; padding: 8px 12px; border-radius: 3px; color: {INK}; margin-top: 10px;">
                            <span style="display: block; color: {MUTED}; font-size: 0.78em; letter-spacing: 1px; margin-bottom: 4px;">SCENE STARTER · COPY INTO CHAT</span>
                            {esc(t)}
                        </div>'''
    def say(l): return f'<div style="color: {INK}; line-height: 1.6;"><strong style="color: {ACC2};">{esc(n)}:</strong>&nbsp;“{esc(l)}”</div>'
    def q(a, b): return f'''<div style="margin-bottom: 8px;"><span style="display: block; font-family: 'Courier New', Courier, monospace; font-size: 0.78em; letter-spacing: 1px; color: {MUTED}; text-transform: uppercase;">{esc(a)}</span><span style="color: #2C4A7A; font-family: 'Bradley Hand', 'Segoe Print', 'Comic Sans MS', cursive; font-size: 1.05em;">{esc(b)}</span></div>'''
    def item(t): return f'<div style="display: flex; gap: 10px; align-items: flex-start; margin-bottom: 6px; color: {INK}; line-height: 1.45;"><span style="color: {ACC}; font-weight: 700;">{m.get("bullet", "&#10047;")}</span><span>{esc(t)}</span></div>'
    def choice(t, l, st): return f'''
                    <details style="margin: 10px 0 0; background: #F7F5EA; border: 1px dashed #BFC4A2; border-radius: 4px; padding: 10px 12px;">
                        <summary style="cursor: pointer; outline: none; color: {INK}; font-weight: 700;">{esc(t)}</summary>
                        <div style="margin-top: 8px;">{say(l)}{starter(st)}
                        </div>
                    </details>'''
    parts = ""
    for i, sec in enumerate(m["sections"]):
        body = ""
        if sec.get("intro"): body += f'<div style="color: {MUTED}; font-style: italic; font-family: Georgia, serif;">{esc(sec["intro"])}</div>'
        body += "".join(q(a, b) for a, b in sec.get("qa", []))
        body += "".join(item(x) for x in sec.get("items", []))
        if sec.get("line"): body += '<div style="margin-top: 10px;">' + say(sec["line"]) + "</div>"
        if sec.get("starter"): body += starter(sec["starter"])
        body += "".join(choice(*ch) for ch in sec.get("choices", []))
        o = " open" if i == 0 else ""
        parts += f'''
            <details{o} style="margin: 0 0 12px; background: rgba(255,255,255,0.82); border: 1px solid #CFD3B8; border-radius: 4px; padding: 12px 14px;">
                <summary style="cursor: pointer; outline: none; color: {INK};">
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: {ACC}; margin-right: 8px; font-weight: 700;">0{i+1}</span>
                    <span style="font-weight: 700; letter-spacing: 1px;">{esc(sec["title"])}</span>
                    <span style="display: block; color: {MUTED}; font-size: 0.82em; font-style: italic; font-family: Georgia, serif; margin-top: 2px;">{esc(sec["sub"])}</span>
                </summary>
                <div style="margin-top: 10px; border-top: 1px solid #DCDDC8; padding-top: 10px; font-size: 0.92em;">{body}
                </div>
            </details>'''
    pills = "\n".join(f'            <div style="background-color:{c["arch2"]}; color:{c["gold"]}; border: 1px solid {c["archb"]}; padding:8px 20px; border-radius:999px; font-weight:600; font-size: 0.9em;">{esc(t)}</div>' for t in m["tags"])
    details = "<br>\n                    ".join(esc(x) for x in m["details"])
    page = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(n)} - The Honeypot Garden</title>
</head>
<!-- Template from @Vorm -->
<body style="margin: 0; background-color: {c['bg_low']}; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: 'Trebuchet MS', 'Helvetica Neue', Helvetica, Arial, sans-serif;">

    <div style="background-color: {c['bg']}; border: 1px solid {c['archb']}; border-radius: 16px; padding: 30px; max-width: 700px; width: 100%; margin: 20px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.7); color: {c['text']}; box-sizing: border-box;">

        <div style="font-size:30px; font-weight:700; border-bottom: 2px solid {c['archb']}; padding-bottom:15px; margin-bottom:25px; color: {c['name']}; letter-spacing: 0.5px;">
            {esc(s['title'])}
        </div>

        <div style="margin-bottom:25px;">
            <div style="font-style:italic; font-size:18px; margin-bottom:15px; color: {c['quote']}; font-family: Georgia, serif;">
                “{esc(m['quote'])}”
            </div>
            <!-- SWAP: {esc(n)} banner URL -->
            <img src="{BANNER}" alt="{esc(n)}" style="display: block; max-width: 100%; margin: 0 auto; border-radius: 12px; border: 1px solid {c['archb']}; filter: brightness(0.92);">
        </div>

        <div style="margin: 25px auto; max-width: 500px; display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">
{pills}
        </div>

        <div style="display: flex; gap: 20px; margin-top: 35px; flex-wrap: wrap;">
            <div style="background-color:rgba(0,0,0,0.22); color: {c['text_soft']}; padding:20px; flex: 1; min-width: 250px; border:1px solid {c['archb']}; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">About</strong>
                <span style="line-height: 1.6; font-size: 0.95em;">{esc(m['about'])}</span>
            </div>
            <div style="background-color:rgba(0,0,0,0.22); color: {c['text_soft']}; padding:20px; flex: 1; min-width: 250px; border:1px solid {c['archb']}; border-radius:12px; text-align:left;">
                <strong style="color: #FFFFFF; font-size: 1.1em; display: block; margin-bottom: 10px; letter-spacing: 0.5px;">Details</strong>
                <div style="line-height: 1.6; font-size: 0.95em;">
                    {details}
                </div>
            </div>
        </div>

        <!-- CLIPBOARD -->
        <div style="margin-top: 35px; background: {c['clip2']}; border-radius: 12px; padding: 14px 10px 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <div style="width: 110px; height: 22px; margin: 0 auto 10px; background: linear-gradient(#D9D4CB, #9A958C); border-radius: 6px 6px 3px 3px; border: 1px solid #77726A;"></div>
            <div style="{LINES} border-radius: 4px; padding: 20px 16px; text-align: left;">
                <div style="text-align: center; font-family: 'Courier New', Courier, monospace; font-size: 0.8em; color: {MUTED}; letter-spacing: 2px; margin-bottom: 6px;">{esc(m['kicker'])}</div>
                <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 30px; color: {INK}; letter-spacing: 1px;">{esc(m['board_title'])}</div>
                <div style="text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 0.95em; color: {MUTED}; margin: 6px 0 20px;">{esc(m['board_sub'])}</div>
{parts}
                <div style="margin-top: 14px; border-top: 1px solid #DCDDC8; padding-top: 12px; color: {INK}; line-height: 1.6; font-size: 0.92em; text-align: center;">
                    <span style="display: block; font-family: 'Courier New', Courier, monospace; letter-spacing: 2px; color: {MUTED}; font-size: 0.85em; margin-bottom: 6px;">AFTER</span>
                    {esc(m['after'])}
                </div>
                <div style="text-align: right; margin-top: 10px; font-family: Georgia, serif; font-style: italic; font-size: 0.85em; color: {MUTED};">{esc(m['signoff'])}</div>
            </div>
        </div>

        <details style="margin-top: 30px; background: rgba(0,0,0,0.25); padding: 12px 20px; border-radius: 8px; border: 1px solid {c['archb']}; color: #ccc; font-size: 0.9em; text-align: left;">
            <summary style="cursor: pointer; color: {c['acc2']}; font-weight: bold; outline: none; letter-spacing: 0.5px;">⚠ Content Warning</summary>
            <div style="margin-top: 12px; line-height: 1.6; border-top: 1px dashed {c['archb']}; padding-top: 12px; color: {c['text_soft']};">
                {esc(m['cw'])}
            </div>
        </details>

    </div>

</body>
</html>
'''
    out = os.path.join(folder, f"{n} (LIL Mini App).html")
    open(out, "w", encoding="utf-8").write(page)
    ok = page.count("<style") == 0 and page.count("<script") == 0 and page.count("<details") == 4 + sum(len(x.get("choices", [])) for x in m["sections"])
    return out, len(page), ok

def build(s, folder):
    res = [lil(s, folder), soulkyn(s, folder), profile(s, folder), mini(s, folder)]
    allok = True
    for out, ln, ok in res:
        t = open(out, encoding="utf-8").read()
        d = t.count("—") + t.count("–")
        b = [m.group(0) for m in re.finditer(BANNED, t, re.I)]
        good = ok and d == 0 and not b
        allok &= good
        print(("OK  " if good else "FAIL"), os.path.basename(out), ln, "dashes", d, "banned", b)
    return allok
