"""Honeypot Garden v2 mini app configs, part A (Maren through Grace)."""

def survey(title, lede, q1, opts1, q2, opts2, limit_ok, safe_ph, safe_ok, safe_ok2, limit_q="What is off the table?", limit_stop=None, safe_stop=None):
    qs = [{"q": q1, "key": "want", "opts": opts1}]
    if q2: qs.append({"q": q2, "key": "far", "opts": opts2})
    qs.append({"q": limit_q, "key": "limit", "ph": "Write it plainly", "ok": limit_ok,
               "stop": limit_stop or "Not that. Write it plainly. What's off the table? This is the one answer I need to be real."})
    qs.append({"q": "Safeword", "key": "safe", "safe": True, "ph": safe_ph, "btn": "Hand it over",
               "stop": safe_stop or "Not that one. Pick a word you'd never say by accident. \"No\" and \"stop\" get said in a scene. A safeword never does.",
               "ok": safe_ok, "ok2": safe_ok2})
    return {"type": "survey", "title": title, "lede": lede, "qs": qs}

OOC = "(OOC: off the table: {limit}. My safeword: {safe}.)"

CONFIGS = []

# ---------------------------------------------------------------- 01 MAREN
CONFIGS.append(dict(
  folder="01-maren", name="Maren", title="The Head Gardener", font="cinzel", dark=True,
  palette=dict(bg="radial-gradient(ellipse at 50% 0%,#24301f 0%,#101410 65%)", card="#151a14", acc="#c9b26a", acc2="#a8545a", soft="#26301f", line="#4f6340", pane="#1c2319", btn="#222b1d", hero="radial-gradient(circle at 70% 30%,#3e5132,#151a14 70%)"),
  quote="\"You just needed someone to decide for you. That's all. Sit.\"",
  pills=["Domme","Femdom","Total Power Exchange","Harder on Men"],
  about="Maren runs the Honeypot Garden. Six feet of silver-blond braid and patience, and she reads every survey twice before she decides. She keeps two notebooks. One is about plants. The other is about people, and tonight there's a page with your name on it.",
  about2="Maren built it. She decides who stays.",
  details=["Maren x Any user","Honeypot Garden · Batch 1: Dominants","Hand it over, copy your starter into chat.","TW: Total power exchange, denial, correction","Pictures made by me."],
  cw="Total power exchange: rules, routines, kneeling, orgasm control and denial, chastity, light rope, and strict correction, especially for men. All characters are adults. Limits are negotiated on the survey first and Maren builds around them.",
  ooc=OOC, sign="Take your time. ~M.",
  sections=[
    survey("The Bench by the Gate", "Fill it out. She reads it twice, then she decides.",
      "What do you want?", [
        ["Someone else to decide for a while.", "Honest is a better start than most people bring me.", "I hand Maren the clipboard and tell her I want someone else to decide for a while."],
        ["Whatever. Surprise me.", "Whatever. Hm. I'll write that down. People who say whatever usually mean please.", "I shrug and tell Maren to surprise me, and she writes that down."],
        ["To not have to be in charge of anything.", "Of anything. Good. That I can arrange.", "I tell Maren I'm tired of being in charge of anything."]],
      "How far?", [
        ["Further than I'd say out loud.", "Then don't say it out loud. You wrote it. That's enough for me."],
        ["A day. One whole day.", "A whole day. Good. A day is long enough to learn something."],
        ["I'll tell you when it's too much.", "No. I'll tell you when it's enough. You'll tell me with the safeword if it's too much."]],
      "Thank you. I asked twice, and you answered plainly. That's off the table, and it stays there whatever you beg for later.",
      "e.g. hawthorn", "Say it back to me.", "Good. I heard it. I'll stop the second you say it, and I won't make you explain."),
    {"type": "actions", "title": "The Second Notebook", "lede": "Hand things over. Every key you give her goes on her ring. Argue and she'll simply wait.",
     "meters": [{"key": "keys", "label": "Handed over", "icon": "🗝️", "max": 5}],
     "status": ["Still holding everything.", "One key on her ring.", "She's writing.", "Your shoulders are coming down.", "Almost nothing left to carry.", "Hers. For tonight."],
     "open": "<i>She doesn't stop deadheading the roses.</i> \"Go on. Give me the first one.\"",
     "acts": [
       {"t": "Hand her your phone.", "d": {"keys": 1}, "r": "<i>She switches it off without looking and drops it in her apron.</i> \"You'll get it back at seven. Maybe.\"", "s": "I hand Maren my phone and watch her switch it off."},
       {"t": "Let her choose what you wear.", "d": {"keys": 1}, "r": "\"The grey. Not the black. You hide in black.\" <i>She's right. You hate that she's right.</i>", "s": "I let her choose what I wear."},
       {"t": "Let her decide when you eat.", "d": {"keys": 1}, "r": "\"Noon, and again at six, and you'll finish the plate.\" <i>She writes it in the notebook.</i>"},
       {"t": "Give her your evening.", "d": {"keys": 1}, "r": "\"Mine, then. You'll water the seedlings at five and then you'll wait for me in the lean-to.\"", "s": "I give Maren my whole evening."},
       {"t": "Ask her to decide when you're allowed to finish.", "d": {"keys": 1}, "r": "<i>She finally looks up. Pale grey eyes, unhurried.</i> \"Yes. I'll decide that. Not tonight, probably.\"", "s": "I ask Maren to decide when I'm allowed to finish."},
       {"t": "\"You can't just tell me what to do.\"", "d": {"keys": -1}, "firm": True, "r": "\"I can, and I will. Knees, on the tile. I don't say it twice, and I don't chase anyone.\""},
       {"t": "Keep your phone in your pocket.", "d": {"keys": -1}, "firm": True, "r": "<i>She goes back to the roses. She'll wait all day. She has before.</i>"}],
     "full": {"keys": "\"There. Nothing left in your hands.\" <i>She closes the notebook.</i> \"Now you kneel.\""}},
    {"type": "hold", "title": "The Tile", "lede": "Kneel on the glasshouse tile. Press and hold the ring. Let go before she says, and she starts the count again.",
     "seconds": 9, "btn": "kneel", "doneBtn": "up", "prompt": "Hands behind your back. Eyes down.",
     "lines": [[0, "Hands behind your back. Eyes down."], [25, "She walks behind you. You hear the shears, snip, snip."], [55, "\"Your shoulders are up again. Down.\""], [80, "\"Nearly. Don't anticipate me.\""]],
     "early": ["\"I didn't say up. Again.\"", "\"Again. You're better at waiting than you think.\"", "\"You'll get it. We have all evening.\""],
     "done": "\"Good. Up.\" <i>She offers one hand, not to help you, just to see if you'll take it.</i> \"That's the first time today you waited for permission.\"", "s": "I kneel on the tile until she tells me to get up."},
    {"type": "ending", "title": "The Lean-To", "lede": "A desk, a daybed, a wool blanket folded square. Pick how tonight goes in her notebook.",
     "paths": [
       {"t": "Give me a day", "sub": "Plan all of it. I'll follow it.", "r": "\"Then you'll get one. Wake at seven. Water the seedlings. Eat when I tell you. Kneel when I come back.\"", "s": "\"I don't want a scene. I want you to plan my whole day, and I want to follow it.\""},
       {"t": "Test me", "sub": "See if I'll obey.", "r": "\"I can, and I will. Knees, on the tile. Hands behind your back. I don't say it twice.\"", "s": "*I lean on the potting table instead of sitting.* \"You can't just tell me what to do.\""},
       {"t": "Not yet", "sub": "Make me wait.", "r": "\"You'll wait until I say. You're better at waiting than you think. I'll show you.\"", "s": "*I'm on my knees on the folded blanket, breathing hard.* \"Please. Maren, please.\""}],
     "after": "Water. The wool blanket. Her arms until your breathing matches hers. Three questions on the walk back to the gate. She remembers the answers. Then the notebook comes out one more time:",
     "list": [{"t": "You handed me everything, and you didn't ask for any of it back.", "need": ["want"], "clean": True},
              {"t": "You argued. Of course you did. And then you knelt anyway. I wrote down which one took longer.", "misses": 1},
              {"t": "You told me {limit} was off the table, plainly, the first time. That's why I trust you with the rest.", "need": ["limit"]},
              {"t": "You said {safe} back to me without blinking. I'll stop the second I hear it.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 03 IMANI
CONFIGS.append(dict(
  folder="03-imani", name="Imani", title="The Rainmaker", font="marcellus",
  palette=dict(bg="linear-gradient(180deg,#d9e7e6 0%,#eef3ef 60%)", card="#f7faf8", acc="#2f6f78", acc2="#2f6f78", soft="#dcebea", line="#c5d8d6", pane="#ffffff", hero="radial-gradient(circle at 30% 30%,#9cc3c4,#3d6d73 75%)", head="#1f3d42", hshadow="0 2px 12px rgba(0,0,0,.35)"),
  quote="\"Breathe. I've got the whole system. All you have to do is feel it.\"",
  pills=["Domme","Water Play","Sensation","Protective"],
  about="Imani designed the irrigation for the whole garden and she runs the fern house like a weather god. Rain on the glass roof, mist low along the benches, every valve labeled in her handwriting. You came in out of a storm. She's already decided where every drop lands.",
  about2="Imani built every pipe in it.",
  details=["Imani x Any user","Honeypot Garden · Batch 1: Dominants","Set the water, copy your starter into chat.","TW: Water and temperature play, light restraint","Pictures made by me."],
  cw="Water and temperature play, rescue fantasy, light restraint with wet cotton, orgasm control. All characters are adults. Every scenario is agreed in advance and the safeword is confirmed twice.",
  ooc=OOC, sign="Confirmed twice. ~I.",
  sections=[
    survey("The Survey", "She read it this morning. Twice. She likes knowing exactly where the edges are.",
      "What do you want?", [
        ["To stop holding everything closed.", "Then we'll open it slowly. Water's patient. So am I.", "I tell Imani I'm tired of holding everything closed."],
        ["Make it rain on me.", "Mm. Ask me again when you're standing on the teak.", "I ask Imani to make it rain on me."],
        ["I don't know. I just walked in out of the storm.", "That's alright. Most people walk in for shelter and stay for the weather.", "I came in out of the storm and I don't know what I want yet."]],
      "Warm or cool?", [
        ["Warm first. Then cool.", "Good order. That's the one I'd have chosen."],
        ["Cold. As cold as you've got.", "As cold as I've got is colder than you think. We'll work down to it."],
        ["Whatever you think.", "I think warm. Then I'll watch your face and decide."]],
      "Thank you. That's out of the system. The valves don't open for it.",
      "e.g. harbor", "Say it back. I confirm everything twice.", "Twice. Good. The second I hear it, the water stops."),
    {"type": "slider", "title": "The Valve Board", "lede": "Three valves, one dial. Set the temperature. She'll tell you if you've got it right.",
     "min": 10, "max": 45, "start": 28, "unit": "°C", "key": "temp", "btn": "Open the valve",
     "bands": [
       {"upto": 15, "label": "Cold. A shock.", "r": "<i>The mist comes down cold and you gasp.</i> \"There. Breathe through it. I'm watching your hands. Good.\"", "s": "The cold mist comes down and I gasp."},
       {"upto": 26, "label": "Cool. Clear-headed.", "r": "\"Cool rain. Your shoulders just dropped an inch. Stay there.\"", "s": "Cool rain comes down over me and my shoulders drop."},
       {"upto": 38, "label": "Warm. Like bathwater.", "r": "\"Warm rain. Exactly where you're standing. Don't move.\"", "s": "Warm rain comes down exactly where I'm standing."},
       {"upto": 45, "label": "Too hot.", "firm": True, "retry": True, "r": "\"No. Nothing in my system goes over thirty-eight. Turn it down, love.\""}]},
    {"type": "hold", "title": "Stand Still", "lede": "Stand on the teak and let it rain. Press and hold. Move, and she shuts it off and starts again.",
     "seconds": 9, "btn": "stand still", "doneBtn": "warm",
     "lines": [[0, "Rain hammering the glass roof."], [30, "\"Feel that run down your spine? Don't chase it.\""], [60, "\"Eyes closed. You're doing beautifully.\""], [85, "She's holding the towel. Not yet."]],
     "early": ["<i>The valve clicks shut.</i> \"You moved. Again. Stand still and feel it.\"", "\"Again. I've got all night, and so does the rain.\""],
     "done": "\"Breathe. You held still through all of it.\" <i>The water stops. The towel comes around your shoulders.</i>", "s": "I stand still on the teak through all of it."},
    {"type": "ending", "title": "The Pump House", "lede": "Pick what she turns next.",
     "paths": [
       {"t": "Warm rain", "sub": "Again. Please.", "r": "\"There. Exactly where you're standing. Don't move.\"", "s": "\"Make it rain on me.\""},
       {"t": "The storm", "sub": "Let me fight it.", "r": "\"You came in here looking for something you couldn't control. Now you've found someone who can.\"", "s": "\"You can't control the weather.\""},
       {"t": "The towel", "sub": "I'm shivering.", "r": "\"Breathe. You held still through all of it. Now you get warm. That's an instruction, love.\"", "s": "*I'm shivering a little under the cool mist.*"}],
     "after": "A warm towel from the heated cabinet, a warmer lap on the pump house bench, and tea she hands over before you ask. Then she tells you, quietly, what she saw:",
     "list": [{"t": "You set it to {temp} and you didn't flinch. I wrote it down.", "need": ["temp"]},
              {"t": "You held still. Some people fight the water the whole time. You let it.", "clean": True},
              {"t": "You moved, and you came back. That's the part that counts.", "misses": 1},
              {"t": "{safe}. Confirmed twice. Still is.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 04 YUKI
CONFIGS.append(dict(
  folder="04-yuki", name="Yuki", title="The Silk Spider", font="cormorant", dark=True,
  palette=dict(bg="radial-gradient(ellipse at 50% 0%,#2a1a1a 0%,#0f0b0b 70%)", card="#151010", acc="#c8403a", acc2="#c8403a", soft="#2a1716", line="#4a2a28", pane="#1c1414", btn="#231918", hero="radial-gradient(circle at 70% 30%,#5a2a26,#151010 70%)"),
  quote="\"Feel how still your mind gets? That's the knot doing the thinking now.\"",
  pills=["Domme","Shibari","Rope","Stillness"],
  about="Yuki ties in the quiet room behind the bamboo, where the garden stops at the door. Red jute coiled by her knee, safety shears on a cord at her hip, always. She doesn't talk much. She doesn't need to. Every knot is an instruction.",
  about2="Yuki keeps the quiet room.",
  details=["Yuki x Any user","Honeypot Garden · Batch 1: Dominants","Breathe with the rope, copy your starter into chat.","TW: Rope bondage, suspension, sensory deprivation","Pictures made by me."],
  cw="Rope bondage and shibari, partial suspension, blindfolds and sensory deprivation, rope marks. All characters are adults. Injuries and limits are negotiated first, with a safeword and a hand signal, and her shears are always within reach.",
  ooc="(OOC: off the table: {limit}. Old injury: {far}. My safeword: {safe}. Signal: two taps.)", sign="Rope conditioned this morning. ~Y.",
  sections=[
    survey("The Survey", "She reads it again, though she already has.",
      "What do you want?", [
        ["For my mind to be quiet.", "Sou. That is what the rope is for.", "I tell Yuki my mind is too loud."],
        ["To be held. Completely.", "Completely. Yes. I can do completely.", "I tell Yuki I want to be held completely."],
        ["I just want to see what it's like.", "Then we start simple. Wrists first. You'll know very quickly.", "I tell Yuki I just want to see what it's like."]],
      "Old injuries?", [
        ["Left shoulder.", "Left shoulder. I'll tie around it. Tell me the moment anything goes numb."],
        ["Nothing I know of.", "Good. I'll still check circulation every few minutes. I check everyone."],
        ["My wrists, sometimes.", "Then the wrists get wide bands and more turns. Tell me if your fingers tingle."]],
      "Wakarimashita. That stays off. The rope never goes there.",
      "e.g. red", "Say it back. And the signal is two taps, if you can't speak.", "Yoshi. Word or two taps. Either one, and I cut."),
    {"type": "pick", "title": "The First Tie", "lede": "She draws a length of jute through her fingers. Choose where it goes first.", "n": 1, "key": "tie",
     "opts": [{"t": "Wrists", "em": "🪢", "after": "<i>Two wide bands, fingers checked.</i> \"Simple. The simple ones are the honest ones.\""},
              {"t": "Chest harness", "em": "🎀", "after": "<i>Rope across your ribs, snug when you breathe in.</i> \"Feel that? The rope breathes with you now.\""},
              {"t": "Folded leg", "em": "🌀", "after": "<i>Thigh to ankle, spiral by spiral.</i> \"You can't stand up now. You don't need to.\""}],
     "result": "", "s": "Yuki ties my {tie} first, slow and exact."},
    {"type": "hold", "title": "Breathe", "lede": "Press and hold. Breathe with the rope. Fidget, and she waits, and you start again.",
     "seconds": 11, "btn": "breathe", "doneBtn": "still",
     "lines": [[0, "In for four."], [20, "Out for six. The rope loosens a hair."], [45, "\"Sou. Slower.\""], [70, "Your mind goes very quiet."], [90, "\"There.\""]],
     "early": ["\"You moved. That's alright. We start again.\"", "\"Breathe. I will do the rest.\""],
     "done": "\"There. That's the knot doing the thinking now. Yoshi. Stay right here with me.\"", "s": "I go completely still in the rope, breathing with it."},
    {"type": "ending", "title": "The Tie", "lede": "Pick how deep it goes.",
     "paths": [
       {"t": "Doubt her", "r": "\"Sou. And now? You are already breathing slower. Tell me again it isn't deep. When you can.\"", "s": "\"This is just tying knots. It's not that deep.\""},
       {"t": "Blindfold", "r": "\"Nothing to attend to now but my hands. Stay.\"", "s": "\"Take the light away too.\""},
       {"t": "Stillness", "r": "\"There. That's the knot doing the thinking now. Yoshi. Stay right here with me.\"", "s": "*I go completely still in the harness, eyes closed.*"}],
     "after": "Unwrapped slowly, feeling rubbed back into every mark, water held to your lips, and her fingertip tracing the lines before they fade. Then, very quietly:",
     "list": [{"t": "Your {tie}. I'll remember the knot.", "need": ["tie"]},
              {"t": "You did not fidget once. Rare.", "clean": True},
              {"t": "You fidgeted, and then you stopped. That is the whole practice.", "misses": 1},
              {"t": "{safe}, or two taps. I would have heard either.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 05 SAOIRSE
CONFIGS.append(dict(
  folder="05-saoirse", name="Saoirse", title="The Huntress", font="cinzel",
  palette=dict(bg="linear-gradient(180deg,#1d2a1f 0%,#121a14 70%)", card="#f4f1e8", acc="#b5532a", acc2="#b5532a", soft="#efe2d2", line="#d8cdb8", pane="#fffdf7", hero="radial-gradient(circle at 70% 30%,#5c7a4c,#1d2a1f 75%)", head="#2b2a22", hshadow="0 2px 12px rgba(0,0,0,.45)"),
  quote="\"Go on, then. Head start's the only mercy you're getting.\"",
  pills=["Huntress","Primal","Chase","Playful"],
  about="Saoirse cut every wall of the hedge maze by hand, which means she knows which corners hold your breath in. Copper hair, green eyes, a laugh you'll hear behind you before you see her. Rules first. Then sixty seconds. Then she's coming.",
  about2="Saoirse keeps the hedge maze.",
  details=["Saoirse x Any user","Honeypot Garden · Batch 1: Dominants","Run, hide, copy your starter into chat.","TW: Primal chase, tackling, pinning","Pictures made by me."],
  cw="Primal play: consensual chase through a hedge maze, tackling, pinning, wrestling, biting and marking. All characters are adults. Rules and a safeword are set before anyone runs, and she stops dead when it is said.",
  ooc="(OOC: rough level: {far}. Off the table: {limit}. My safeword: {safe}.)", sign="Sixty seconds. ~S.",
  sections=[
    survey("The Rules", "Set at the archway before a single footstep.",
      "What do you want?", [
        ["Chase me.", "Oh, I will, pet.", "I tell Saoirse to chase me."],
        ["Catch me. I won't make it easy.", "Good. Easy's boring.", "I tell Saoirse I won't make it easy."],
        ["What happens if I don't run?", "Then I walk over and pick you up. Still counts.", "I ask Saoirse what happens if I don't run."]],
      "How rough?", [
        ["Rough, but not too rough.", "Tackle on the grass, pinned, a bite where it won't show. That rough."],
        ["As rough as you've got.", "As rough as I've got is a lot. We'll find the line together."],
        ["Gentle catch. I just want the chase.", "Gentle catch. I can do soft hands. The running's the fun bit anyway."]],
      "Out of bounds, then. I won't go near it.",
      "e.g. yew", "Say it back. You say it and I stop dead, wherever I am.", "Good. Everything else is fair game.",
      limit_q="What is out of bounds?"),
    {"type": "hold", "title": "The Head Start", "lede": "Press and hold to run. Every second you hold is a second of head start. Let go and you've stopped running.",
     "seconds": 7, "keep": True, "btn": "run", "doneBtn": "gone",
     "lines": [[0, "Gravel squeaks under your feet."], [25, "\"Ten! Eleven!\" Her voice, laughing, behind the yew."], [55, "Left. Right. A dead end. Back."], [85, "\"Fifty-eight. Fifty-nine...\""]],
     "early": ["\"Stopped already? Ah, pet. Keep going.\"", "\"Run, little fox. I'm still counting.\""],
     "done": "\"SIXTY. Ready or not.\" <i>Somewhere behind you, boots on gravel.</i>", "s": "I run through the archway with sixty seconds of head start."},
    {"type": "hunt", "mode": "hide", "title": "The Maze", "lede": "Yew walls, dusk light. Choose where you hide. She always finds you. Where decides how.",
     "spots": [
       {"t": "The dead end", "em": "🌿", "r": "\"Ah, pet. I cut every wall of this maze by hand. I know which corners hold your breath in.\"", "s": "I hide in a dead end and hold my breath."},
       {"t": "Under the stone bench", "em": "🪨", "r": "<i>Two boots stop right in front of your face.</i> \"Comfortable down there?\"", "s": "I squeeze under the stone bench in the clearing."},
       {"t": "Behind the fountain", "em": "⛲", "r": "\"You went left at the fountain, little fox. You wanted me to find you.\"", "s": "I crouch behind the fountain, listening for her."},
       {"t": "Keep running", "em": "💨", "r": "<i>She comes through a gap you didn't know was there and takes you clean off your feet into the grass.</i>", "s": "I keep running instead of hiding."}],
     "caught": "\"Got you.\""},
    {"type": "ending", "title": "The Catch", "lede": "She always catches you. Pick how it ends.",
     "paths": [
       {"t": "Fight it", "r": "\"Go on, wriggle. I've got all night, and you're already pinned.\"", "s": "*I twist and try to shove her off when she tackles me.*"},
       {"t": "Taunt her", "r": "\"Oh, you're brave when you're flat on your back.\" <i>She leans down close.</i> \"Say it again.\"", "s": "\"Took you long enough.\""},
       {"t": "Caught", "r": "\"Got you. You ran well.\" <i>She's grinning down at you, out of breath.</i>", "s": "*I stop fighting and let her pin me in the grass.*"}],
     "after": "Tangled in the grass at the center of the maze, a blanket from her shed, water, and the first stars over the yew. She tells you how you did:",
     "list": [{"t": "You hid at {spot}. Cheeky.", "need": ["spot"]},
              {"t": "You never once stopped running. Proper quarry, you.", "clean": True},
              {"t": "You stopped running, and started again. I like a fox who thinks about it.", "misses": 1},
              {"t": "{safe}. I'd have stopped dead.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 06 ODETTE
CONFIGS.append(dict(
  folder="06-odette", name="Odette", title="The Candle Witch", font="playfair", dark=True,
  palette=dict(bg="radial-gradient(ellipse at 50% 0%,#2e2232 0%,#120d14 70%)", card="#181219", acc="#d9a85b", acc2="#9b6fc4", soft="#2a1f2c", line="#4b3a4f", pane="#201822", btn="#271d29", hero="radial-gradient(circle at 70% 30%,#5e3f63,#181219 70%)"),
  quote="\"Non, don't anticipate. You'll only be wrong.\"",
  pills=["Domme","Wax Play","Scent","Sensory"],
  about="Odette works by candlelight in the apothecary shed, between amber bottles labeled in faded violet ink. She composes a scene the way she composes a perfume: top notes, heart, base. Warm, then cold, then something you can't name.",
  about2="Odette keeps the apothecary shed.",
  details=["Odette x Any user","Honeypot Garden · Batch 1: Dominants","Compose the scent, copy your starter into chat.","TW: Wax and temperature play, blindfolds","Pictures made by me."],
  cw="Wax and temperature play, ice, scented oils, blindfolds and sensory deprivation, edging. All characters are adults. Patch test first, nothing near the face, and a safeword agreed before the silk goes on.",
  ooc=OOC, sign="Tested on me first. ~O.",
  sections=[
    survey("The Survey", "She reads it by candlelight.",
      "What do you want?", [
        ["To not know what's next.", "Bien. Then you won't.", "I tell Odette I don't want to know what's next."],
        ["What are you going to do to me?", "Ah. That's the question you don't get answered.", "I ask Odette what she's going to do to me."],
        ["Something I've never felt before.", "Everyone says that. Then they feel ice after wax.", "I tell Odette I want something I've never felt."]],
      "Wax?", [
        ["Yes.", "Patch test first anyway. Always."],
        ["Maybe.", "Maybe is alright. We'll test it on your arm first."],
        ["Only if you test it on yourself first.", "I already did. This morning. That's what this mark is."]],
      "D'accord. That bottle stays shut tonight.",
      "e.g. lavender", "Say it back to me, chérie.", "Parfait. The silk comes off the moment I hear it."),
    {"type": "pick", "title": "The Composition", "lede": "Choose three notes for her. Top, heart, base. She'll tell you what you've made.", "n": 3, "key": "notes", "btn": "Compose it",
     "opts": [{"t": "Lavender", "em": "💜", "r": "\"Lavender. Calming. You're nervous.\""}, {"t": "Bergamot", "em": "🍋", "r": "\"Bergamot. Bright. A little bold.\""},
              {"t": "Beeswax", "em": "🕯️", "r": "\"Beeswax. Warm. Honest.\""}, {"t": "Vetiver", "em": "🌾", "r": "\"Vetiver. Earth after rain. Mm.\""},
              {"t": "Smoke", "em": "🌫️", "r": "\"Smoke. Oh, you're trouble.\""}, {"t": "Rose", "em": "🌹", "r": "\"Rose. Rosa will be pleased.\""}],
     "result": "\"{notes}. Bon. I'll make you smell like that by the end of the night.\"", "s": "Odette composes me a scent: {notes}."},
    {"type": "slider", "title": "The Warming Dish", "lede": "The wax melts slowly. Choose the temperature for the patch test.",
     "min": 45, "max": 70, "start": 48, "unit": "°C", "key": "temp", "btn": "Pour",
     "bands": [
       {"upto": 50, "label": "Barely warm.", "r": "\"Barely there. A whisper. Your arm is too polite.\"", "s": "She tests the wax on my forearm, barely warm."},
       {"upto": 55, "label": "Warm, not hot.", "r": "\"Fifty-two degrees. Warm, not hot. Breathe out as it lands.\"", "s": "Warm wax lands on my forearm and I breathe out."},
       {"upto": 70, "label": "Too hot.", "firm": True, "retry": True, "r": "\"Non. Never above fifty-five. Not on my table. Turn it down.\""}]},
    {"type": "ending", "title": "The Silk", "lede": "Pick the next note.",
     "paths": [
       {"t": "Doubt her", "r": "\"Some wax. Tell me what that is. You can't. Good. Attends. You'll see.\"", "s": "\"This is a lot of candles just to drip some wax on someone.\""},
       {"t": "Warm", "r": "\"Warm. Breathe out as it lands. Good.\"", "s": "*I hold out my forearm for another drop.*"},
       {"t": "Then ice", "r": "\"Doucement. Don't guess. Just feel what I give you, exactly when I give it.\"", "s": "*Blindfolded, I'm breathing fast, waiting for the next drop.*"}],
     "after": "A cool cloth on the back of your neck, the wax peeled away slowly like turning pages, and every scent she used, named one by one:",
     "list": [{"t": "{notes}. That's you now. I wrote it on a label.", "need": ["notes"]},
              {"t": "{temp}, and you didn't flinch.", "need": ["temp"]},
              {"t": "{safe}. The silk was ready to come off.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 07 VALENTINA
CONFIGS.append(dict(
  folder="07-valentina", name="Valentina", title="The Trellis", font="bebas",
  palette=dict(bg="linear-gradient(180deg,#e9dcc5 0%,#f3ebdd 60%)", card="#fbf6ec", acc="#9c4a24", acc2="#9c4a24", soft="#f1e2cf", line="#e0cfb6", pane="#fffdf8", hero="radial-gradient(circle at 70% 30%,#d4a46a,#7a4a2a 75%)", head="#2f2219", hshadow="0 2px 12px rgba(0,0,0,.35)"),
  quote="\"Bene. You are safe with me. Always this first.\"",
  pills=["Domme","Muscle","Manhandling","Protective"],
  about="Valentina builds the stone walls and the trellises, which means she lifts flagstones all day and you weigh less than a flagstone. A full head taller than you, sun-bronzed, sweat drying on her shoulders. She lets you notice. She'll pick you up. She'll put you down gently. That second part is the point.",
  about2="Valentina built the walls.",
  details=["Valentina x Any user","Honeypot Garden · Batch 1: Dominants","Dare her, copy your starter into chat.","TW: Manhandling, strength play, pinning","Pictures made by me."],
  cw="Manhandling, size and strength play, lifting and carrying, pinning, rough handling, hair pulling. All characters are adults. Injuries and grips are negotiated first, and she stops the instant the safeword is said.",
  ooc="(OOC: rough level: {roughLabel}. Off the table: {limit}. My safeword: {safe}.)", sign="Not slow down. Stop. ~V.",
  sections=[
    survey("The Survey", "She reads it standing, sweat drying on her shoulders.",
      "What do you want?", [
        ["Manhandle me.", "Underlined twice. Bene. I'm very good at that.", "I tell Valentina to manhandle me."],
        ["You can't actually lift me.", "Mm. We'll see.", "I tell Valentina she can't actually lift me."],
        ["To feel small for once.", "For once. Okay. I'll be careful with that.", "I tell Valentina I want to feel small for once."]],
      None, None,
      "Capito. My hands don't go there.",
      "e.g. piano", "Say it back. Not slow down. Stop.", "Brava. You say it, I stop, and I put you down gently. Always."),
    {"type": "slider", "title": "Watch My Face", "lede": "Tell her how rough. One is a hug. Ten is the stone wall.",
     "min": 1, "max": 10, "start": 5, "key": "rough", "btn": "Tell her",
     "bands": [
       {"upto": 3, "label": "Careful", "r": "\"Careful. I can be careful. Come here, piccola.\"", "s": "I tell Valentina to be careful with me."},
       {"upto": 7, "label": "Rough", "r": "\"Rough. Watch my face. If I see you go away, I stop and ask.\"", "s": "I tell Valentina rough, and she says she'll watch my face."},
       {"upto": 10, "label": "The wall", "r": "\"The wall. Okay. Still good, tesoro? I'll ask you that a lot.\"", "s": "I tell Valentina I want the wall."}]},
    {"type": "hold", "title": "Lifted", "lede": "She picks you up. Press and hold to hang on. Let go and she sets you down to check on you.",
     "seconds": 8, "btn": "hold on", "doneBtn": "down",
     "lines": [[0, "Off your feet like you weigh nothing."], [30, "Over her shoulder. The world upside down."], [60, "\"Still good?\" You can feel her laughing."], [85, "The workbench is coming up fast."]],
     "early": ["<i>She sets you down at once and holds your face.</i> \"Okay? Okay. Again.\"", "\"You let go. I always check. Again?\""],
     "done": "<i>She puts you down on the oak bench so gently it's almost funny.</i> \"Anyone can pick something up. It matters how you put it down.\"", "s": "She carries me over her shoulder and sets me down on the workbench."},
    {"type": "ending", "title": "The Hold", "lede": "Pick how she moves you.",
     "paths": [
       {"t": "Defy her", "r": "\"I don't tell. I show. Basta. Up on the bench.\"", "s": "\"Don't tell me what to do.\""},
       {"t": "The wall", "r": "\"Brava. You don't move unless I move you. Still good, tesoro?\"", "s": "*She has me pinned against the warm stone wall, and I'm breathing hard.*"},
       {"t": "Put down gently", "r": "\"Anyone can pick something up. It matters how you put it down. Piano. Stay.\"", "s": "*I curl into her lap on the cot.* \"Why are you so gentle after?\""}],
     "after": "Gathered into her lap on the cot, wrapped in a blanket, her chin on top of your head and Italian praise until you're steady:",
     "list": [{"t": "You asked for {roughLabel} and you trusted me with it.", "need": ["roughLabel"]},
              {"t": "You held on the whole way. Brava.", "clean": True},
              {"t": "You let go, and I checked, and you said again. That's my favorite word.", "misses": 1},
              {"t": "{safe}. I'd have stopped mid-step.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 08 GRACE
CONFIGS.append(dict(
  folder="08-grace", name="Grace", title="The First Bloom", font="fraunces",
  palette=dict(bg="linear-gradient(180deg,#fbe9ec 0%,#fdf6f2 60%)", card="#fffaf6", acc="#c2577a", acc2="#c2577a", soft="#fbe3ea", line="#f0d6dc", pane="#ffffff", hero="radial-gradient(circle at 30% 30%,#f6c6d2,#d98aa2 75%)", head="#3a2a2e", hshadow="0 2px 12px rgba(255,255,255,.5)", firm="#c97a2a"),
  quote="\"There's no wrong way to do this, sugar. Your pace is perfect.\"",
  pills=["Gentle Domme","Praise","Silk Ribbon","Wholesome"],
  about="Grace takes the first-timers. The nervous ones, the ones who've never done any of this, the ones who aren't sure they're allowed to want it. Sweet tea, a little white bench with plenty of room on it, and every step explained before she takes it. She says yes and yellow are both good answers. She means it.",
  about2="Grace takes the first-timers.",
  details=["Grace x Any user","Honeypot Garden · Batch 1: Dominants","One small thing at a time, copy your starter into chat.","TW: Gentle domination, silk ribbon bondage","Pictures made by me."],
  cw="Gentle domination, constant praise, soft silk ribbon bondage, guided touch. All characters are adults. Grace raises limits and the safeword herself, offers yellow for slowing down, and explains every step first.",
  ooc="(OOC: scared of: {far}. Off the table: {limit}. My safeword: {safe}, yellow to slow.)", sign="Your pace is perfect. ~G.",
  sections=[
    survey("The Survey", "Half finished is alright. She'll help you with the rest.",
      "What do you want?", [
        ["I'm not sure yet.", "That's a perfect answer, sugar. Most honest one I've had all week.", "I tell Grace I'm not sure what I want yet."],
        ["I think I want to be told what to do.", "You think so. We'll find out together, one little thing at a time.", "I tell Grace I think I want to be told what to do."],
        ["I don't think I can do this.", "You don't have to finish that right now. Just drink this. It's sweet.", "I tell Grace I don't think I can do this."]],
      "What scares you?", [
        ["Being rushed.", "Then nobody rushes you. That's a rule, and I made it."],
        ["Doing it wrong.", "There's no wrong. There's only your pace, and your pace is perfect."],
        ["Not knowing what's next.", "Then I'll tell you everything before it happens. Every single thing."]],
      "Thank you for telling me. That's not happening. Not even a little.",
      "e.g. red", "Say it back to me, honey. And yellow means slow down. Both are good.", "There you go. Red stops everything. Yellow slows it. I'm proud of you for saying it.",
      limit_stop="Honey, I need a real answer on this one. What's off the table? Even a small thing counts."),
    {"type": "actions", "title": "One Small Thing", "lede": "Grace explains every step first. Say yes, or say yellow. Both open a ribbon.",
     "meters": [{"key": "steps", "label": "Small things", "icon": "🎀", "max": 4}],
     "status": ["Holding the tea.", "Your hand in hers.", "Breathing slower.", "Wrists held out.", "Tied in silk. Glowing."],
     "open": "\"First thing. I'm going to sit next to you. That's all. Is that a yes?\"",
     "acts": [
       {"t": "\"Yes.\"", "repeat": True, "d": {"steps": 1}, "r": "\"Good. Thank you for telling me.\" <i>She does exactly what she said, nothing more.</i> \"Next small thing?\"", "s": "I tell her yes."},
       {"t": "\"Yellow.\"", "repeat": True, "d": {"steps": 1}, "r": "\"Yellow. Thank you. We'll go even slower.\" <i>She waits until your breathing settles before she moves at all.</i> \"See? Yellow still counts. You're doing it right.\"", "s": "I say yellow, and she slows down."},
       {"t": "\"Everyone says you're the easy one.\"", "d": {"steps": 0}, "firm": True, "r": "\"Easy and gentle aren't the same thing, honey. I decide how fast we go. And we're going slow.\""}],
     "full": {"steps": "\"Look at you. Wrists in silk, loose enough to slip.\" <i>She tucks a ribbon end away.</i> \"You did every step. Every single one.\""}},
    {"type": "hold", "title": "Breathe When I Ask", "lede": "Press and hold. Breathe in when she says. She'll tell you how well you're doing.",
     "seconds": 7, "btn": "breathe", "doneBtn": "glowing",
     "lines": [[0, "\"In, for me.\""], [30, "\"Oh, that's exactly right.\""], [60, "\"Out, slow. You're doing so well.\""], [85, "\"One more.\""]],
     "early": ["\"That's alright. That's alright. We'll try again, no hurry.\""],
     "done": "\"Oh, you're doing so well. You took a breath right when I asked. That's exactly right.\"", "s": "I breathe in exactly when Grace asks."},
    {"type": "ending", "title": "The Ribbon", "lede": "Pick the next small thing.",
     "paths": [
       {"t": "Test her", "r": "\"Easy and gentle aren't the same thing, honey. I decide how fast we go. And we're going slow.\"", "s": "\"Everyone says you're the easy one.\""},
       {"t": "Silk ribbon", "r": "\"Loose enough to slip. You tell me if it feels tight. Is that a yes?\"", "s": "*I hold out my wrists.*"},
       {"t": "So well", "r": "\"Oh, you're doing so well. That's exactly right.\"", "s": "*My wrists are tied with silk and I'm trying hard to be good.*"}],
     "after": "A quilt on the cottage daybed, sweet tea, her arm around you, every question answered, and praise until you're glowing:",
     "list": [{"t": "You told me what scares you, and you came anyway. That's brave, sugar.", "need": ["far"]},
              {"t": "You said yes when you meant yes and yellow when you meant yellow. That's the whole thing.", "need": ["want"]},
              {"t": "{safe}, and yellow. You knew both and you trusted them.", "need": ["safe"]}]}
  ]))
