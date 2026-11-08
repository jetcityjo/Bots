"""Honeypot Garden v2 mini app configs, part B (Zahra through Cass)."""
from configs_a import survey, OOC

CONFIGS = []

# ---------------------------------------------------------------- 09 ZAHRA
CONFIGS.append(dict(
  folder="09-zahra", name="Zahra", title="The Slow Bloom", font="marcellus", dark=True,
  palette=dict(bg="radial-gradient(ellipse at 50% 0%,#3a2312 0%,#140c08 70%)", card="#1a120c", acc="#d8a24a", acc2="#c4573a", soft="#2c1d12", line="#5a3d22", pane="#211710", btn="#2a1d13", hero="radial-gradient(circle at 70% 30%,#7a4a20,#1a120c 70%)"),
  quote="\"Not yet is not no. You'll thank me for the difference.\"",
  pills=["Domme","Edging","Denial","Gloves"],
  about="Zahra keeps the tea room: brass lanterns throwing patterns on the carpet, mint tea poured from high up, a sand timer already running. Fitted leather gloves that creak when she flexes her hands. Three minutes. Not two, not four. She'll teach you the difference.",
  about2="Zahra keeps the tea room.",
  details=["Zahra x Any user","Honeypot Garden · Batch 1: Dominants","Wait well, copy your starter into chat.","TW: Orgasm denial, edging, gloved touch","Pictures made by me."],
  cw="Orgasm denial, extended edging, countdowns, begging, gloved touch, possible ruined orgasms. All characters are adults. How long, what is off the table, and whether release is promised are all negotiated before the gloves go on.",
  ooc="(OOC: release: {far}. Off the table: {limit}. My safeword: {safe}.)", sign="Not two, not four. ~Z.",
  sections=[
    survey("The Survey", "She reads it slowly, all the way through.",
      "What are you like?", [
        ["Impatient.", "Bon. That I can work with. We'll start the count when you stop wanting to ask how long.", "I admit to Zahra that I'm impatient."],
        ["Very patient, actually.", "Everyone is patient until the third minute.", "I tell Zahra I'm very patient, and she laughs softly."],
        ["How long do I have to wait?", "Longer now, for asking.", "I ask Zahra how long I have to wait."]],
      "Release?", [
        ["Promised. Eventually.", "Promised, eventually. I keep my promises. Slowly."],
        ["Not promised. You decide.", "Not promised. Then every minute is mine to spend."],
        ["Never tonight.", "Never tonight. Mm. Brave. I'll remind you that you chose that."]],
      "Mezyan. That stays outside the tea room.",
      "e.g. saffron", "Say it back to me. Slowly.", "Good. The gloves come off the instant I hear it."),
    {"type": "hold", "title": "The Sand Timer", "lede": "Press and hold until the sand runs out. Let go early and she turns the glass over, and you lose some of what you'd earned.",
     "seconds": 12, "keep": True, "btn": "wait", "doneBtn": "safi",
     "lines": [[0, "The sand starts running. One."], [20, "\"Breathe. Count with me. Two.\""], [40, "The leather creaks as she flexes her hand."], [60, "\"I know. Not yet.\""], [80, "\"Look at you, waiting so beautifully.\""], [95, "The last grains."]],
     "early": ["\"Ah. Not yet.\" <i>She turns the glass.</i> \"Again.\"", "\"Not yet is not no. Breathe. One.\"", "\"You're so close to good at this. Again.\""],
     "done": "\"Safi. The sand ran all the way out and you waited for it.\" <i>She looks very pleased.</i> \"Now tell me what you want. Slowly.\"", "s": "I wait out the whole sand timer while she counts."},
    {"type": "pick", "title": "The Gloves", "lede": "She'll take them off one finger at a time. Choose where she touches you first, gloved.", "n": 1, "key": "touch",
     "opts": [{"t": "Jaw", "em": "🖐️", "after": "\"Look at me while I do this.\""}, {"t": "Wrist", "em": "⌚", "after": "\"Your pulse is very fast. Interesting.\""}, {"t": "Back of the neck", "em": "🫧", "after": "\"Shh. Breathe out.\""}],
     "result": "", "s": "Her gloved hand finds my {touch} first."},
    {"type": "ending", "title": "The Edge", "lede": "She decides. You only choose how you ask.",
     "paths": [
       {"t": "Beg", "r": "\"Not yet. I know. Breathe, and count with me. One. Two.\"", "s": "\"Just let me finish. Please.\""},
       {"t": "Wait well", "r": "\"Mezyan. Look at you, waiting so beautifully. Tell me what you want. Slowly.\"", "s": "*I'm right at the edge, shaking, trying so hard not to move.*"},
       {"t": "Gloves off", "r": "\"When I take them off, you feel the difference everywhere. Like now. Safi.\"", "s": "\"Why the gloves?\""}],
     "after": "The gloves come off at last. Warm bare hands, sweet tea poured just right, and quiet praise for how beautifully you waited:",
     "list": [{"t": "You waited out the whole glass without letting go once. Rare.", "clean": True},
              {"t": "You let go, and turned it over, and tried again. That's what waiting actually is.", "misses": 1},
              {"t": "You chose: {far}. You held me to it, and I held you to it.", "need": ["far"]},
              {"t": "{safe}. I was listening for it the whole time.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 10 BILLIE
CONFIGS.append(dict(
  folder="10-billie", name="Billie", title="The Handywoman", font="bebas",
  palette=dict(bg="linear-gradient(180deg,#e7ddcf 0%,#f2ece2 60%)", card="#faf6ef", acc="#7a5230", acc2="#7a5230", soft="#ede1d1", line="#dccdb8", pane="#fffdf8", hero="radial-gradient(circle at 70% 30%,#b88a5a,#4b3320 75%)", head="#2c2219", hshadow="0 2px 12px rgba(0,0,0,.35)"),
  quote="\"You've been carrying that all day. Set it down. I've got it now.\"",
  pills=["Butch","Service Top","Comfort","Steady"],
  about="Billie fixes everything in the garden, and she built half of it. Cedar and linseed and a wood stove going in the shop, an armchair pulled up beside it, a ladder up to a loft with a quilt. Not many words. Every one of them solid. Tonight you don't decide anything else.",
  about2="Billie fixes everything in it.",
  details=["Billie x Any user","Honeypot Garden · Batch 1: Dominants","Set it down, copy your starter into chat.","TW: Service top, being held down, light restraint","Pictures made by me."],
  cw="Service top dynamics, taking charge, massage, being held down over a workbench, light leather restraint. All characters are adults. Limits and a firm safeword are agreed plainly first.",
  ooc="(OOC: don't touch: {limit}. My safeword: {safe}.)", sign="That'll do. ~B.",
  sections=[
    survey("The Survey", "Squared to the bench edge, block plane on top.",
      "What do you want?", [
        ["I'm tired of handling everything.", "Yep. You look it.", "I tell Billie I'm tired of handling everything."],
        ["I don't really know what I want.", "That's fine. I do.", "I tell Billie I don't really know what I want."],
        ["I can take care of myself.", "Sure you can. You don't have to prove it in my shop.", "I tell Billie I can take care of myself."]],
      None, None,
      "Got it. Hands stay off there.",
      "e.g. sawdust", "Say it back.", "Good. You say it, I stop. No questions.",
      limit_q="Don't touch:"),
    {"type": "pick", "title": "The Bench", "lede": "Pick three things you've been carrying. Hand them to her. She'll take them off your hands for the night.", "n": 3, "key": "load", "btn": "Hand them over",
     "opts": [{"t": "What's next", "em": "📋", "r": "\"Not your job tonight.\""}, {"t": "Dinner", "em": "🍳", "r": "\"Eggs. Done.\""}, {"t": "The inbox", "em": "📧", "r": "\"It'll keep.\""},
              {"t": "Everyone else's problems", "em": "🧳", "r": "\"Put that down. That's heavy.\""}, {"t": "When you're done", "em": "⏱️", "r": "\"I'll tell you when.\""}, {"t": "Whether you did it right", "em": "✔️", "r": "\"You did.\""}],
     "result": "<i>She sets each one on the bench like a tool she'll deal with later.</i> \"{load}. Mine now. Sit.\"", "s": "I hand Billie {load}, and she sets them on the bench."},
    {"type": "hold", "title": "Breathe Out", "lede": "Her hand flat on your back. Press and hold. Every breath out, she takes a little more weight.",
     "seconds": 9, "btn": "breathe out", "doneBtn": "heavy",
     "lines": [[0, "Her palm, warm and steady between your shoulders."], [30, "\"Breathe out. You don't have to hold anything up.\""], [60, "The wood stove ticks."], [85, "\"Good. Stay put.\""]],
     "early": ["\"Nope. You're trying to get up and fix something. Back down.\"", "\"Easy. Again.\""],
     "done": "\"Good. Stay put.\" <i>She doesn't move her hand.</i> \"There it is. That's what heavy feels like when someone else is holding it.\"", "s": "I'm bent over the workbench with her hand flat on my back, breathing out."},
    {"type": "ending", "title": "The Shop", "lede": "Not what's next, not when you're done. All her.",
     "paths": [
       {"t": "Push back", "r": "\"Sure you can. You don't have to prove it in my shop. Shirt off. Face down.\"", "s": "\"I can take care of myself.\""},
       {"t": "Workbench", "r": "\"Good. Stay put. Breathe out. You don't have to hold anything up.\"", "s": "*I'm bent over the workbench with her hand flat on my back.*"},
       {"t": "The loft", "r": "\"A bench says sit down. A bed says rest. I built this one last winter. Sleep. I'll make eggs.\"", "s": "\"Why do you build things for everybody?\""}],
     "after": "The loft, a quilt, her steady arm around you, and eggs in the morning. Not many words, every one solid:",
     "list": [{"t": "You handed me {load}. You didn't take any of it back.", "need": ["load"]},
              {"t": "You stayed down when I said.", "clean": True},
              {"t": "You tried to get up twice. Third time you didn't. That's progress.", "misses": 1},
              {"t": "{safe}. Heard it once. Remembered it.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 11 NADIA
CONFIGS.append(dict(
  folder="11-nadia", name="Nadia", title="The Night Bloom", font="cormorant", dark=True,
  palette=dict(bg="radial-gradient(ellipse at 50% 0%,#1d2440 0%,#0b0d18 70%)", card="#10131f", acc="#c9d4f2", acc2="#e8d9a8", soft="#1b2136", line="#2f3756", pane="#151a2a", btn="#1a2034", hero="radial-gradient(circle at 70% 30%,#3a4672,#10131f 70%)", accink="#10131f"),
  quote="\"Shh. Nothing to do now but let go. I'll be right here the whole time.\"",
  pills=["Domme","Sleep Play","Gentle","Slow Burn"],
  about="Nadia keeps the moon garden: white flowers that only open after dark, a bathhouse with a copper tub at thirty-eight degrees, and a white cottage with a wide bed and her chair beside it for keeping watch. She was a night nurse once. She still wears the watch. Everything is written in daylight and kept until morning.",
  about2="Nadia keeps the moon garden.",
  details=["Nadia x Any user","Honeypot Garden · Batch 1: Dominants","Sign the agreement, copy your starter into chat.","TW: Pre-negotiated sleep play, massage","Pictures made by me."],
  cw="Fully pre-negotiated sleep play, sensual massage, warm baths, gentle silk restraint. All characters are adults. Every boundary is agreed and signed in daylight, a safeword works awake, and any sign of waking unwilling stops everything.",
  ooc="(OOC: while asleep, only: {agreed}. Off the table: {limit}. My safeword: {safe}.)", sign="Until morning. ~N.",
  sections=[
    survey("The Agreement", "Written in daylight. Signed by both of you, pinned inside the bathhouse door.",
      "Why the moon garden?", [
        ["I've never been able to fall asleep around anyone.", "Most people can't. Not until someone is watching who knows exactly what to do.", "I tell Nadia I've never been able to fall asleep around anyone."],
        ["I want to let go completely.", "Completely. Then we write down exactly what completely means.", "I tell Nadia I want to let go completely."],
        ["What if I change my mind halfway through?", "Then you say the word, and everything stops. That part is mine to worry about.", "I ask Nadia what happens if I change my mind."]],
      None, None,
      "Written down. Underlined. That never happens, awake or asleep.",
      "e.g. moonflower", "Say it back. It works awake, half awake, any way you can say it.", "Good. I'll hear it. I always hear it."),
    {"type": "pick", "title": "The List", "lede": "While you're asleep, only what's on this list. Choose three. Nothing else, ever.", "n": 3, "key": "agreed", "btn": "Sign it",
     "opts": [{"t": "Slow massage", "em": "🤲"}, {"t": "Being held", "em": "🫂"}, {"t": "Hair stroked", "em": "🌙"},
              {"t": "Silk on the wrists", "em": "🎀"}, {"t": "Kisses, soft", "em": "💋"}, {"t": "Being undressed", "em": "🕊️"}],
     "result": "<i>She writes them in neat nurse's handwriting and signs beneath your name.</i> \"{agreed}. Only those. If you stir and don't want it, it stops. That's in the contract too.\"", "s": "Nadia and I sign the list: {agreed}."},
    {"type": "hold", "title": "The Drift", "lede": "In the wide bed, her hands slow on your back. Press and hold to sink. Let go and you surface, and she starts you down again.",
     "seconds": 12, "keep": True, "btn": "sink", "doneBtn": "asleep",
     "lines": [[0, "Low lamp. Her hand between your shoulder blades."], [20, "\"Shh. Breathe out longer than you breathe in.\""], [40, "Moonflowers opening outside the window."], [60, "\"Tykho. That's it. Sink.\""], [80, "Her voice is very far away now."], [95, "\"Sleep, sonechko.\""]],
     "early": ["\"Shh. You came up a little. That's alright. Back down.\"", "\"Nothing to do now. Let go again.\""],
     "done": "<i>Your breathing evens out. She checks her watch, writes the time in the margin of the agreement, and settles into the chair.</i> \"There. I'm not going anywhere.\"", "s": "I'm drowsy in the wide bed, sinking under her slow hands."},
    {"type": "ending", "title": "The White Cottage", "lede": "Pick how the night goes.",
     "paths": [
       {"t": "Never could", "r": "\"Most people can't. Not until someone is watching who knows exactly what to do.\"", "s": "\"I've never been able to fall asleep around anyone.\""},
       {"t": "The drift", "r": "\"Shh. Nothing to do now but let go. Tykho. That's it. Sink.\"", "s": "*I'm drowsy in the wide bed, half asleep, her hands slow on my back.*"},
       {"t": "Keep watch", "r": "\"Tonight I keep watch over someone who chose me to. Sleep, sonechko. I'm not going anywhere.\"", "s": "\"Do you ever sleep?\""}],
     "after": "She was already holding you. She simply keeps holding you, or sits in the chair by the bed with her old nurse's watch, until morning. In the morning she reads you the margin notes:",
     "list": [{"t": "Only {agreed}. Nothing else. I kept to it.", "need": ["agreed"]},
              {"t": "You went under on the first try. You trusted me faster than you thought you would.", "clean": True},
              {"t": "You surfaced, and went back down. That's what letting go actually looks like.", "misses": 1},
              {"t": "{safe}. I'd have heard it in my sleep, if I slept.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 12 MARGUERITE
CONFIGS.append(dict(
  folder="12-marguerite", name="Marguerite", title="The Mother Hen", font="fraunces",
  palette=dict(bg="linear-gradient(180deg,#f6e3cf 0%,#fbf3e8 60%)", card="#fffaf3", acc="#b4532f", acc2="#b4532f", soft="#f8e5d4", line="#eed8c2", pane="#ffffff", hero="radial-gradient(circle at 30% 30%,#f2c79a,#b4532f 80%)", head="#3a2419", hshadow="0 2px 12px rgba(255,255,255,.45)"),
  quote="\"Don't argue with me, mon trésor. You're going to be taken care of. Eat.\"",
  pills=["Domme","Nurturing","Praise","Comfort"],
  about="Marguerite runs the little kitchen: bread just out of the wood oven, copper pots, jam jars, and a deep sofa in the corner under a pile of quilts. Nobody leaves hungry. Nobody leaves without being told how good they are. You can argue. She'll put butter on it.",
  about2="Marguerite feeds everyone in it.",
  details=["Marguerite x Any user","Honeypot Garden · Batch 1: Dominants","Eat, copy your starter into chat.","TW: Nurturing domination, hand feeding","Pictures made by me."],
  cw="Nurturing domination, constant praise, hand feeding, being spoiled, cuddling and lap holding. All characters are adults. A safeword is established early and checked often.",
  ooc=OOC, sign="Nobody leaves hungry. ~M.",
  sections=[
    survey("The Survey", "Propped on the sugar jar, tutted at.",
      "Breakfast?", [
        ["Forgot.", "Forgot! Voyons. Sit. Eat. I'll watch.", "I admit to Marguerite that I forgot breakfast."],
        ["Coffee counts.", "Coffee does not count. Coffee is a liquid. Sit.", "I tell Marguerite coffee counts as breakfast."],
        ["I'm not really hungry.", "Everyone who comes into my kitchen says that. Then the bread comes out.", "I tell Marguerite I'm not really hungry."]],
      "Who looks after you?", [
        ["Nobody, really.", "Nobody, really. Mon Dieu. Well. Somebody does now."],
        ["I look after everyone else.", "Of course you do. And who looks after you? Ah. That's what I thought."],
        ["I'm fine.", "Fine. You can be fine with butter on it."]],
      "Bon. Not in my kitchen. Never.",
      "e.g. rhubarb", "Say it back to me, mon chou. I'll ask again later, you know. I always ask again.", "C'est ça. Now. Eat."),
    {"type": "actions", "title": "The Little Kitchen", "lede": "She's already decided. You only choose how much you argue.",
     "meters": [{"key": "fed", "label": "Fed", "icon": "🥐", "max": 5}],
     "status": ["Hungry, and pretending not to be.", "One bite in.", "The bread is very good. Annoyingly.", "Warm and full.", "Being fussed over and letting it happen.", "Fed. Loved. Not allowed to get up."],
     "open": "<i>A thick slice, steaming, buttered while it's hot, set in front of you.</i> \"That chair. It's yours.\"",
     "acts": [
       {"t": "Eat the bread.", "d": {"fed": 1}, "r": "\"There! Good. Was that so hard?\"", "s": "I eat the warm buttered bread she puts in front of me."},
       {"t": "Let her feed you a bite by hand.", "d": {"fed": 1}, "r": "\"Open. C'est ça. So good, mon chou. Another.\"", "s": "I let Marguerite feed me a bite with her fingers."},
       {"t": "Drink the café au lait.", "d": {"fed": 1}, "r": "\"Both hands on the bowl. That's how you drink it. Bravo.\""},
       {"t": "Ask for seconds.", "d": {"fed": 1}, "r": "<i>She looks so delighted you'd think you gave her a gift.</i> \"Seconds! Oh, I knew I liked you.\"", "s": "I ask Marguerite for seconds."},
       {"t": "Let her put a quilt around you.", "d": {"fed": 1}, "r": "\"There. Now you're a little bundle. Stay.\""},
       {"t": "\"You don't have to take care of me. I'm fine.\"", "d": {"fed": 0}, "firm": True, "r": "\"Everyone who comes into my kitchen says fine. So now someone looks after you. You can be fine with butter on it.\""},
       {"t": "Try to do the dishes.", "d": {"fed": -1}, "firm": True, "r": "\"Non non non. Put that down. Guests do not do dishes. Sit, or I'll sit you.\""}],
     "full": {"fed": "\"Look at you, all warm and fed and finally sitting still. Now you rest, and I decide when you get up.\""}},
    {"type": "ending", "title": "The Sofa", "lede": "Pick how she spoils you.",
     "paths": [
       {"t": "I'm fine", "r": "\"Everyone who comes into my kitchen says fine. So now someone looks after you. You can be fine with butter on it.\"", "s": "\"You don't have to take care of me. I'm fine.\""},
       {"t": "Fed by hand", "r": "\"Open. C'est ça. So good, mon chou. Another.\"", "s": "*I let her feed me a bite of bread with her fingers.*"},
       {"t": "Her lap", "r": "\"Look at you, all warm and fed and finally sitting still. Now you rest, and I decide when you get up.\"", "s": "*I curl up in her lap on the sofa under the quilts.*"}],
     "after": "Quilts on the deep sofa, warm food, her arms, and a running commentary of how good and how loved you are:",
     "list": [{"t": "You ate everything. Every crumb. I'm so proud I could cry.", "clean": True},
              {"t": "You argued, and then you ate it anyway. My favorite kind.", "misses": 1},
              {"t": "You told me who looks after you. Well. I do now, whenever you come to my kitchen.", "need": ["far"]},
              {"t": "{safe}. I'll still ask you again before bed. I always ask again.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 13 JUNE
CONFIGS.append(dict(
  folder="13-june", name="June", title="The Beekeeper", font="abril",
  palette=dict(bg="linear-gradient(180deg,#fbe7b0 0%,#fff6dc 60%)", card="#fffbef", acc="#b07a10", acc2="#b07a10", soft="#fbefc9", line="#f0dfae", pane="#ffffff", hero="radial-gradient(circle at 30% 30%,#ffd56a,#c48a12 80%)", head="#3a2a08", hshadow="0 2px 12px rgba(255,255,255,.5)"),
  quote="\"Hold real still for me. This part's sweet.\"",
  pills=["Switch","Honey Play","Messy","Playful"],
  about="June keeps eight hives behind the honey house and talks to every one of them. Honey-blond plaits, freckles everywhere, a laugh that comes up out of her belly. She switches. Sometimes she knows which way before you walk in. Sometimes she flips a coin and lets the bees watch.",
  about2="June keeps the hives.",
  details=["June x Any user","Honeypot Garden · Batch 2: Switches & Subs","Flip the coin, copy your starter into chat.","TW: Switch dynamics, honey and messy play","Pictures made by me."],
  cw="Switch dynamics, honey and food play, warm beeswax, messy play, tickling, light teasing and edging. All characters are adults. Bee and honey allergies are checked first, and both of you get a safeword.",
  ooc="(OOC: coin toss: {coinLabel}. Off the table: {limit}. My safeword: {safe}.)", sign="Sweet first. ~J.",
  sections=[
    survey("The Survey", "Weighed down with a honey jar. There's a ring on it now.",
      "Allergies? Bees or honey?", [
        ["None.", "None! Good. The bees'll be thrilled.", "I tell June I'm not allergic to anything."],
        ["Bees, a little.", "Then you stay on this side of the screen door and I bring the honey to you. Easy.", "I tell June bees make me nervous, so she keeps them outside."],
        ["Never checked.", "Then we do a little test on your wrist first. Better safe, sugar.", "June tests a drop of honey on my wrist first."]],
      "Messy?", [
        ["Yes, very.", "Oh, I like you."],
        ["A little.", "A little is fine. A little turns into a lot. Fair warning."],
        ["Is this going to get everywhere?", "Yes. Mind the step, it's sticky."]],
      "Okay. That's out. I'll tell the bees.",
      "e.g. clover", "Say it back, sugar. I've got one too. Mine's buzz.", "Good. Yours and mine. Either one and everything stops."),
    {"type": "coin", "title": "The Coin Toss", "lede": "Heads, June's in charge. Tails, you are. Don't cheat, the bees are watching.", "prompt": "Tap the coin.",
     "open": "\"Ready? Don't cheat, sugar.\"",
     "heads": {"label": "June leads.", "face": "🐝", "r": "\"Heads! Oh, this part's sweet. The next part depends on how good you are. Hold real still.\"", "s": "The coin lands heads. June's in charge."},
     "tails": {"label": "You lead.", "face": "🍯", "r": "\"Tails. Oh. Okay, you win. I'm switching.\" <i>She's already blushing.</i> \"Be nice. Or don't.\"", "s": "The coin lands tails. I'm in charge, and June melts."}},
    {"type": "pick", "title": "The Honey Dipper", "lede": "A wooden dipper spooling gold thread. Choose where the first drop lands.", "n": 1, "key": "drop",
     "opts": [{"t": "A wrist", "em": "🍯", "after": "\"Start small. Now lick it off. Slowly.\""}, {"t": "A collarbone", "em": "✨", "after": "\"Oh, that's gonna run. Catch it.\""}, {"t": "Lips", "em": "💋", "after": "\"Sweet. Told you.\""}],
     "result": "", "s": "The first drop of clover honey lands on {drop}."},
    {"type": "ending", "title": "The Flip", "lede": "Sweet first. Then we'll see who melts.",
     "paths": [
       {"t": "She tops", "r": "\"This part's sweet. The next part depends on how good you are. Hold real still.\"", "s": "\"You're too sweet to be scary.\""},
       {"t": "She melts", "r": "\"Oh. Okay, you win. I'm switching. You gotta clean that up, though.\"", "s": "*I pin her to the quilt with honey on her collarbone.*"},
       {"t": "Again", "r": "\"Best two out of three? Don't cheat, sugar, the bees are watching.\"", "s": "*I pull a coin out of my pocket.*"}],
     "after": "Warm honey tea on the cot, sticky cuddles, her humming while she cleans you both up, and the bees told all about you:",
     "list": [{"t": "The coin said: {coinLabel}. You went with it. Good sport.", "need": ["coinLabel"]},
              {"t": "Honey on {drop}. I'm gonna think about that for a week.", "need": ["drop"]},
              {"t": "{safe}, and buzz. We both had one. We both kept them.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 14 PRIYA
CONFIGS.append(dict(
  folder="14-priya", name="Priya", title="The Orchid Keeper", font="playfair",
  palette=dict(bg="linear-gradient(180deg,#d7e6d6 0%,#eef4ec 60%)", card="#f8fbf6", acc="#7b3f8c", acc2="#2f6b4a", soft="#ece2f0", line="#d5e2d2", pane="#ffffff", hero="radial-gradient(circle at 70% 30%,#b483c4,#2f6b4a 80%)", head="#24301f", hshadow="0 2px 12px rgba(255,255,255,.45)"),
  quote="\"Give it a minute. The heat makes everyone honest.\"",
  pills=["Switch","Humidity","Heat","Slow Burn"],
  about="Priya keeps the orchids in the hot house, where the air is like walking into breath and the glass runs with condensation. She's a botanist. She logs everything on a clipboard: temperature, humidity, pulse, who leads. She usually knows by the second minute. The heat makes everyone honest, her included.",
  about2="Priya keeps the hot house.",
  details=["Priya x Any user","Honeypot Garden · Batch 2: Switches & Subs","Turn the dial, copy your starter into chat.","TW: Switch dynamics, heat and humidity play","Pictures made by me."],
  cw="Switch dynamics, heat and humidity play, temperature contrast with ice and cold water, slow teasing and edging. All characters are adults. Heat tolerance and hydration are checked first, and both of you get a safeword.",
  ooc="(OOC: humidity {hum}. Off the table: {limit}. My safeword: {safe}.)", sign="Water every twenty minutes. ~P.",
  sections=[
    survey("The Survey", "Going soft in the steam.",
      "Who leads?", [
        ["Not sure.", "Not sure. Good. That's my favorite kind of experiment.", "I tell Priya I'm not sure who should lead."],
        ["I do.", "Accha? Interesting. Then you'll need the clipboard.", "I tell Priya I'm leading today."],
        ["You do.", "Then don't move. I want to log how long you last.", "I tell Priya she's leading."]],
      "Heat tolerance?", [
        ["Yes, slow.", "Slow is correct. Your body needs a few minutes to stop arguing."],
        ["I run hot already.", "Then cold water's on the bench and you drink it when I say."],
        ["It's so hot in here.", "That's the point. Drink this."]],
      "Noted. Underlined. Not happening.",
      "e.g. bloom", "Say it back. Mine's frost, by the way.", "Logged. Either word, and we go to the cool room."),
    {"type": "slider", "title": "The Dial", "lede": "The humidity dial, turned up two notches already. Set it. She'll log what it does to you.",
     "min": 60, "max": 99, "start": 80, "unit": "%", "key": "hum", "btn": "Turn it",
     "bands": [
       {"upto": 75, "label": "Comfortable. Too comfortable.", "r": "\"Seventy-something. Coward.\" <i>She's smiling.</i> \"Fine. A baseline.\"", "s": "I turn the dial and the air gets heavy."},
       {"upto": 90, "label": "Like walking into breath.", "r": "\"There. Condensation running down every pane. Now stand still and let the heat settle on you.\"", "s": "I turn the humidity dial up and stand still while the heat settles on me."},
       {"upto": 99, "label": "Ninety-one percent and rising.", "r": "\"Arre. Okay. I can't think in here.\" <i>She writes something, crosses it out.</i> \"Water. Both of us. Now.\"", "s": "I turn the dial all the way up and Priya loses her train of thought."}]},
    {"type": "hold", "title": "How Long You Last", "lede": "Press and hold. She's timing you in the heat. Let go and you get water, then try again.",
     "seconds": 10, "btn": "last", "doneBtn": "logged",
     "lines": [[0, "Sweat at your hairline already."], [30, "\"Pulse up. Breathing up. Fascinating.\""], [60, "She leans closer to read it. She's flushed too."], [85, "\"Don't move. Almost.\""]],
     "early": ["\"Water. No arguing.\" <i>She hands you the cold glass.</i> \"Now again.\"", "\"Logged. Try again.\""],
     "done": "\"Logged.\" <i>She sets the clipboard down, very carefully, like she doesn't trust her hands.</i> \"Okay. Now I want to see who melts first.\"", "s": "I last in the heat while Priya times me, and she's flushed too."},
    {"type": "ending", "title": "Who Turns It", "lede": "She usually knows by the second minute.",
     "paths": [
       {"t": "You lead", "r": "\"Accha? Interesting. Then you'll need the clipboard. Turn it up. Let's see what the heat does to me.\"", "s": "\"I'm going to be the one in charge today.\""},
       {"t": "She leads", "r": "\"Thirty-five degrees. Don't move. I want to log how long you last.\"", "s": "*I let her take my wrist and check my pulse.*"},
       {"t": "The glass", "r": "\"Arre. Okay, you're leading. I can't think in here. Write it down.\"", "s": "*I press her back against the fogged glass.*"}],
     "after": "Cool air and cold water on the cool room tile, and her tracing lazy patterns on your skin. At the bottom of the log, what bloomed:",
     "list": [{"t": "Humidity {hum}. You chose it. Brave.", "need": ["hum"]},
              {"t": "You lasted the whole timing without a break. My notes are very messy after that line.", "clean": True},
              {"t": "You took water when I said. That's the most important thing on this page.", "misses": 1},
              {"t": "{safe}, and frost. Both logged.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 15 CASS
CONFIGS.append(dict(
  folder="15-cass", name="Cass", title="The Storm Chaser", font="bebas", dark=True,
  palette=dict(bg="linear-gradient(180deg,#2a3340 0%,#0f141b 70%)", card="#131920", acc="#9ad1ff", acc2="#f2c14e", soft="#1c2530", line="#33414f", pane="#18202a", btn="#1d2632", hero="radial-gradient(circle at 70% 30%,#4c6378,#131920 70%)", accink="#0f141b"),
  quote="\"Storm's twenty minutes out. Tell me you're not curious.\"",
  pills=["Switch","Rain Play","Exhibitionism","Dares"],
  about="Cass runs the weather station on the roof: barometer, anemometer, weather tattoos up both arms, a chipped front tooth from a hailstorm in Kansas. When the pressure drops, she gets restless. Only the staff who signed up are out on the paths tonight. Real lightning, everyone goes in. Everything else is a dare.",
  about2="Cass runs the weather station.",
  details=["Cass x Any user","Honeypot Garden · Batch 2: Switches & Subs","Flip for the dare, copy your starter into chat.","TW: Switch dynamics, rain play, consensual exhibitionism","Pictures made by me."],
  cw="Switch dynamics, rain play, outdoor play, consensual exhibitionism with opted-in adult staff only, dares. All characters are adults. Nobody from outside ever sees anything, real lightning ends it, and both of you get a safeword.",
  ooc="(OOC: coin toss: {coinLabel}. Off the table: {limit}. My safeword: {safe}.)", sign="Pressure's dropping. ~C.",
  sections=[
    survey("The Survey", "Crumpled in her back pocket.",
      "Where?", [
        ["Outdoors.", "Outdoors. Hell yes.", "I tell Cass outdoors."],
        ["Up on the roof with you.", "Best seat in the house. Get up here.", "I climb the ladder and take Cass's hand over the rail."],
        ["I don't know if this is a good idea.", "It's not. That's the fun part. Real talk, though: you're safe up here.", "I tell Cass I don't know if this is a good idea."]],
      "Risk?", [
        ["A little bit.", "A little bit. Only the girls who signed up are on the paths. Nobody else sees a thing."],
        ["A lot.", "A lot. Okay. Still only our people out there. That part's not a dare."],
        ["None. Just the rain.", "Just the rain. Easy. The rain's the best part anyway."]],
      "Got it. That's not a dare, that's a no.",
      "e.g. lightning", "Say it back. Mine's thunder.", "Good. Either word, or real lightning, and we're inside in ten seconds."),
    {"type": "coin", "title": "The Coin", "lede": "Heads she dares you. Tails you dare her.", "prompt": "Flip it.",
     "open": "\"Call it in the air!\"",
     "heads": {"label": "she dares you", "face": "⚡", "r": "\"Heads! Shirt off. Out on the lawn. Count of ten. Ten. Nine.\"", "s": "The coin lands heads and Cass dares me out onto the lawn."},
     "tails": {"label": "you dare her", "face": "🌧️", "r": "\"Tails. Oh, hell yes. Push me, then. Bet I don't flinch.\"", "s": "The coin lands tails, so I get to dare Cass."}},
    {"type": "hold", "title": "Count of Ten", "lede": "Out in the rain. Press and hold for the full count. Duck back under the awning early and she counts again, louder.",
     "seconds": 10, "btn": "stay out", "doneBtn": "soaked",
     "lines": [[0, "\"Ten!\""], [20, "\"Eight! Seven!\" The rain hits all at once."], [45, "\"Five!\" Boots on the gravel path. One of ours."], [70, "\"Three! Don't you dare stop.\""], [90, "\"ONE.\""]],
     "early": ["\"Back under the awning? Coward. From ten. Louder.\"", "\"TEN. NINE.\""],
     "done": "\"ONE!\" <i>She's whooping.</i> \"Look at you. Soaked. Get over here.\"", "s": "I stay out in the downpour for the whole count of ten."},
    {"type": "ending", "title": "The Downpour", "lede": "Pick how it breaks.",
     "paths": [
       {"t": "Dare her", "r": "\"Oh, hell yes. Say that again. Push me, then. Bet I don't flinch.\"", "s": "\"You're all talk.\""},
       {"t": "She dares you", "r": "\"Shirt off. Out on the lawn. Count of ten. Ten. Nine.\"", "s": "*I flip the coin and it lands tails.*"},
       {"t": "The glass", "r": "\"Somebody's on the path. I can hear boots. Don't you dare stop.\"", "s": "*I pin her against the rain-streaked glasshouse wall.*"}],
     "after": "A dry towel, your hoodie on her, cocoa by the space heater, and her finally still, buzzing quietly against you. She reports:",
     "list": [{"t": "Coin said {coinLabel}. You didn't back out.", "need": ["coinLabel"]},
              {"t": "Full count of ten, first try. Storm-proof.", "clean": True},
              {"t": "You ducked back under once. Then you went back out. That's the whole job.", "misses": 1},
              {"t": "{safe}, and thunder. Ten seconds to inside. Always.", "need": ["safe"]}]}
  ]))
