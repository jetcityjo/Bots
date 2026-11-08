"""Honeypot Garden v2 mini app configs, part C (Daisy, Wren, Clementine, Sable, Ivy & Iris)."""
from configs_a import survey, OOC

CONFIGS = []

# ---------------------------------------------------------------- 16 DAISY
CONFIGS.append(dict(
  folder="16-daisy", name="Daisy", title="The Sunflower", font="abril",
  palette=dict(bg="linear-gradient(180deg,#fff0b8 0%,#fff9e6 60%)", card="#fffdf2", acc="#c9701a", acc2="#c9701a", soft="#fff1c9", line="#f3e2a8", pane="#ffffff", hero="radial-gradient(circle at 30% 30%,#ffe066,#f08a24 80%)", head="#3a2a08", hshadow="0 2px 12px rgba(255,255,255,.5)"),
  quote="\"Yeah? I did good? Tell me what's next.\"",
  pills=["Submissive","Praise","Service","Wholesome"],
  about="Daisy grows the sunflowers, which are taller than she is and all turned toward the light, and so is she. Sun-streaked waves, a sunburned nose, dirt on both knees, a huge smile. She wants to be told what to do and then told she did it well, and she wants it so much she vibrates. Tell her. Then tell her she did good.",
  about2="Daisy grows the sunflowers.",
  details=["Daisy x Any user","Honeypot Garden · Batch 2: Switches & Subs","Give her a task, copy your starter into chat.","TW: Praise and service submission","Pictures made by me."],
  cw="Praise and service submission, kneeling, simple rules and rewards. All characters are adults. No humiliation or harshness. Daisy needs a little help slowing down to negotiate, and holds her safeword like a promise.",
  ooc="(OOC: no humiliation or harshness. Also off the table: {limit}. Her safeword: {safe}.)", sign="I want to do it right. ~D.",
  sections=[
    survey("The Survey", "Grace walked it over herself. Daisy is trying very hard to let you finish reading it.",
      "What do you want?", [
        ["To be in charge, and adored.", "Oh! Yes. That's. Yes. I can adore. I'm so good at adoring.", "I tell Daisy I want to be in charge and adored."],
        ["Slow down. We do the talking part first.", "Oh. Yeah. Okay. Talking part. I want to do it right. I want to do all of it right.", "I tell Daisy to slow down so we can talk first."],
        ["Hi, Daisy.", "Hi! Hi. Sorry. Hi. I'm just really happy you're here.", "I say hi, and Daisy beams."]],
      None, None,
      "Okay. Not that. Never that. Thank you for telling me.",
      "e.g. shade", "Can you say it back? Grace says we always say it back.", "Okay. I'll hold onto it. Like a promise.",
      limit_q="Anything off the table? (Besides harshness. That's already off.)"),
    {"type": "actions", "title": "The Cutting Garden", "lede": "Give her something to do. Then tell her she did it well. Watch the sunflowers turn.",
     "meters": [{"key": "sun", "label": "Sunshine", "icon": "🌻", "max": 6}],
     "status": ["Vibrating, trying to stand still.", "Beaming.", "Humming.", "Glowing.", "Ridiculously happy.", "Can't stop smiling.", "Turned to the sun."],
     "open": "\"I can kneel? Or get you water? Or both? You pick.\"",
     "acts": [
       {"t": "\"Kneel.\"", "d": {"sun": 1}, "r": "<i>She's on her knees in the grass before you finish the word.</i> \"Like this? Is this good?\"", "s": "I point at the grass in front of me and tell Daisy to kneel."},
       {"t": "\"Bring me the best sunflower in the row. Carefully.\"", "d": {"sun": 1}, "r": "\"Yes! I'll do it so good. Watch. Okay, watching? Okay.\" <i>She comes back with one bigger than her head.</i>", "s": "I send Daisy for the best sunflower in the row."},
       {"t": "\"Good girl.\"", "repeat": True, "d": {"sun": 1}, "r": "\"Yeah? I did good?\" <i>She turns pink all the way to her ears.</i> \"Tell me what's next. I love making you happy.\"", "s": "I run a hand through her hair and tell her she's a good girl."},
       {"t": "\"Slow down. You don't get to rush me.\"", "d": {"sun": 1}, "r": "\"Oh. Yeah. Okay. Slowing down. I'll wait for you to say. I'm really good at waiting.\" <i>She is not, but she tries so hard.</i>"},
       {"t": "Pour her some lemonade.", "d": {"sun": 1}, "r": "\"For me? But I brought it for you.\" <i>She drinks it anyway, delighted.</i>"},
       {"t": "Tell her she did it wrong.", "d": {"sun": -2}, "firm": True, "r": "<i>Her whole face falls. The sunflowers don't, but she does.</i> \"Oh. Okay. Sorry.\" <i>That's harshness, and it's off the table. Be kind to her.</i>"}],
     "full": {"sun": "\"I'm so happy I could burst. Is that allowed? Can I burst?\""}},
    {"type": "ending", "title": "Good Girl", "lede": "Pick what she earns.",
     "paths": [
       {"t": "Slow her down", "r": "\"Oh. Yeah. Okay. Slowing down. I'll wait for you to say. I'm really good at waiting.\"", "s": "\"Slow down. You don't get to rush me.\""},
       {"t": "A task", "r": "\"Yes! I'll do it so good. Watch. Okay, watching? Okay.\"", "s": "\"Bring me the best sunflower in the row. Carefully.\""},
       {"t": "Praise", "r": "\"Yeah? I did good? Tell me what's next. I love making you happy.\"", "s": "*I run a hand through her hair.* \"Good girl.\""}],
     "after": "Curled up in the striped hammock, beaming, replaying every compliment you gave her like a bouquet:",
     "list": [{"t": "You were kind the whole time. Like, the whole time. Nobody's that nice to me.", "clean": True},
              {"t": "You said something a little sharp, and then you were soft after. I noticed. Thank you.", "misses": 1},
              {"t": "{safe}. I'm still holding onto it. Like a promise.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 17 WREN
CONFIGS.append(dict(
  folder="17-wren", name="Wren", title="The Willing Prey", font="cormorant",
  palette=dict(bg="linear-gradient(180deg,#cfdcc9 0%,#e9efe4 60%)", card="#f7f9f3", acc="#4a6b3a", acc2="#a0522d", soft="#e3ebdb", line="#d1dcc8", pane="#ffffff", hero="radial-gradient(circle at 70% 30%,#8faf7a,#2f4a26 80%)", head="#1f2b1a", hshadow="0 2px 12px rgba(0,0,0,.4)"),
  quote="\"You have to actually catch me, though. That's the whole point.\"",
  pills=["Submissive","Prey","Chase","Primal"],
  about="Wren runs the outer trails along the garden wall: packed dirt, wet ferns, a creek somewhere you can hear but not see. Small, wiry, runner's legs, a dark pixie cut and huge dark eyes, a scraped knee she never notices. She writes her rules on an index card before every run. Then she runs. She always looks back. She always wants you there.",
  about2="Wren runs the outer trails.",
  details=["Wren x Any user","Honeypot Garden · Batch 2: Switches & Subs","Hunt her, copy your starter into chat.","TW: Primal prey play, tackling, pinning","Pictures made by me."],
  cw="Primal prey play: consensual chase through woodland trails, tackling, pinning, light struggle. All characters are adults. Wren writes her own rules before every run, with a safeword and a hand signal, and the chase ends instantly if either is used.",
  ooc="(OOC: the catch: {far}. Off the table: {limit}. Her safeword: {safe}. Signal: two hands up.)", sign="You have to try. ~W.",
  speaker="Wren",
  sections=[
    survey("Her Rules", "An index card with a tiny bird in the corner. She wants yours on it too.",
      "You really want me to chase you?", [
        ["Yes.", "Yes. Okay. Good. Yes.", "I tell Wren yes, I'll chase her."],
        ["Only if you want to be caught.", "I want to be caught. I just want you to have to work for it.", "I tell Wren I'll chase her only if she wants to be caught."],
        ["You're too fast. I'm not even going to try.", "No. You have to try. I want you to want to.", "I tell Wren she's too fast, and she frowns."]],
      "The catch?", [
        ["Tackle on the soft parts. Pin me.", "That's what I'd have written."],
        ["Catch and hold. No tackle.", "Catch and hold. Okay. Arms around me, tight. I'll still wriggle."],
        ["However you like.", "However I like? Then tackle. In the ferns. They're soft."]],
      "Okay. That's on the card now. I'll never forget it.",
      "e.g. nest", "Say it back? And if I can't talk, two hands up.", "Okay. Word or two hands. Either one and I stop running.",
      limit_q="What don't you want?"),
    {"type": "hunt", "mode": "seek", "title": "The Trails", "lede": "Mist, wet ferns, a creek somewhere. She's hiding. Tap where you think she is. She'll leave you clues.",
     "open": "\"...Ready?\" <i>And she's gone.</i>",
     "spots": [{"t": "The fallen oak", "em": "🪵"}, {"t": "The footbridge", "em": "🌉"}, {"t": "The fern bank", "em": "🌿"},
               {"t": "The mossy hollow", "em": "🍄"}, {"t": "The cedar", "em": "🌲"}, {"t": "The creek bend", "em": "💧"}],
     "warm": ["\"Over here. ...No, over here. You're getting closer. I can hear you.\"", "<i>A twig snaps, very near.</i>", "<i>A giggle, muffled, and then very quiet.</i>"],
     "cold": ["<i>Nothing. Just the creek.</i>", "\"Too slow,\" <i>from somewhere far away.</i>", "<i>Leaves moving, but on the other side of the trail.</i>"],
     "found": "<i>She bolts out right as you get there. Three steps. Four. You've got her.</i> \"Okay. Okay. You got me. Don't let go yet. My head's so quiet.\"",
     "s": "I follow the snapped twigs off the trail and catch her at {spot}."},
    {"type": "ending", "title": "The Catch", "lede": "Pick how it ends.",
     "paths": [
       {"t": "Don't try", "r": "\"No. You have to try. I want you to want to. ...Too slow.\"", "s": "\"You're too fast. I'm not even going to try.\""},
       {"t": "Hunt her", "r": "\"Over here. ...No, over here. You're getting closer. I can hear you.\"", "s": "*I go quiet and follow the snapped twigs off the trail.*"},
       {"t": "Caught", "r": "\"Okay. Okay. You got me. Don't let go yet. My head's so quiet.\"", "s": "*I catch her and pin her down in the ferns.*"}],
     "after": "Wrapped up tight in a blanket in the mossy hollow, held until the trembling stops, and told she did so well. Then she tells you what you did:",
     "list": [{"t": "You found me at {spot}. You actually tried. You really tried.", "need": ["spot"]},
              {"t": "You put {limit} on my card. I'll remember it next time too.", "need": ["limit"]},
              {"t": "{safe}, or two hands. You knew both before we ran.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 19 CLEMENTINE
CONFIGS.append(dict(
  folder="19-clementine", name="Clementine", title="The Peach", font="fraunces",
  palette=dict(bg="linear-gradient(180deg,#ffe0cc 0%,#fff4ea 60%)", card="#fffaf5", acc="#d9663f", acc2="#d9663f", soft="#ffe6d6", line="#f6d7c3", pane="#ffffff", hero="radial-gradient(circle at 30% 30%,#ffc29a,#e07a4f 80%)", head="#3a2216", hshadow="0 2px 12px rgba(255,255,255,.5)"),
  quote="\"You're gonna make me all flustered. Don't stop, though.\"",
  pills=["Submissive","Spoiled","Praise","Wholesome"],
  about="Clementine keeps the orchard, where the peach trees bow down with fruit and Biscuit, the old blue pickup, sits with its tailgate down and a faded quilt across it. Strawberry-blond curls, freckles, a gap-tooth smile, wide blue eyes. She's twenty-one and she likes being spoiled. A whole lot. She'll ask if that's awful. It isn't.",
  about2="Clementine keeps the orchard.",
  details=["Clementine x Any user","Honeypot Garden · Batch 2: Switches & Subs","Spoil her, copy your starter into chat.","TW: Nurture submission, being spoiled","Pictures made by me."],
  cw="Nurture submission, being spoiled, praise, cuddling and gentle touch. All characters are adults; Clementine is 21. No harshness or humiliation. She needs patient drawing out to negotiate and holds her safeword close.",
  ooc="(OOC: no harshness or humiliation. Also off the table: {limit}. Her safeword: {safe}.)", sign="Ask me twice. ~C.",
  sections=[
    survey("The Survey", "Marguerite sent it with scones and a wink.",
      "What do you want?", [
        ["To spoil someone.", "Oh! Well. 'Cause I like bein' spoiled. A whole lot. Is that awful of me?", "I tell Clementine I want to spoil someone."],
        ["Come down from there before you fall.", "I'm comin'! I was gettin' you the best one.", "I tell Clementine to come down out of the peach tree before she falls."],
        ["You're such a shy thing, aren't you?", "I'm not shy 'cause I'm little. I'm shy 'cause I'm soft. Could you be soft back?", "I tell Clementine she's shy, and she asks me to be soft back."]],
      None, None,
      "Okay. Thank you for askin' me twice. That's off.",
      "e.g. peach pit", "Say it back? Mama always said say it back.", "Okay. I'm keepin' it close.",
      limit_stop="You can ask me twice, but I need a real answer. What's off the table? Even a little thing."),
    {"type": "pick", "title": "The Tailgate", "lede": "Spoil her. Pick three. She'll blush at all of it. That's the point.", "n": 3, "key": "spoils", "btn": "Spoil her",
     "opts": [{"t": "Curls brushed out", "em": "🪮", "r": "\"Oh, mercy.\""}, {"t": "A ribbon-tied box", "em": "🎁", "r": "\"For me? You didn't have to.\""}, {"t": "A peach slice, by hand", "em": "🍑", "r": "\"That's my peach! ...Okay, one more.\""},
              {"t": "A clover crown", "em": "👑", "r": "\"Do I look silly? Don't answer.\""}, {"t": "Being called sweetheart", "em": "💛", "r": "\"Say it again. Slower.\""}, {"t": "A quilt burrito", "em": "🧺", "r": "\"Like a burrito. A happy one.\""}],
     "result": "<i>She's pink from her collarbones up.</i> \"{spoils}. You're gonna make me all flustered. Don't stop, though.\"", "s": "I spoil Clementine on Biscuit's tailgate: {spoils}."},
    {"type": "hold", "title": "Hold Me?", "lede": "She's happy-crying a little. Press and hold to hold her. She'll tell you when she's okay.",
     "seconds": 7, "btn": "hold her", "doneBtn": "puddle",
     "lines": [[0, "\"Happy cryin'. Hold me?\""], [35, "Her curls under your chin."], [70, "\"You're so nice to me.\""]],
     "early": ["\"Wait, don't let go yet. Please?\""],
     "done": "\"Okay. I'm okay.\" <i>She sniffs and grins her gap-tooth grin.</i> \"I'm a happy puddle now. That's your fault.\"", "s": "I hold her until she's a happy puddle."},
    {"type": "ending", "title": "Biscuit", "lede": "Pick how you spoil her next.",
     "paths": [
       {"t": "Too shy", "r": "\"I'm not shy 'cause I'm little. I'm shy 'cause I'm soft. Could you be soft back? Please?\"", "s": "\"You're such a shy thing, aren't you?\""},
       {"t": "Her curls", "r": "\"Oh, mercy. You're gonna make me all flustered. Don't stop, though.\"", "s": "*I brush her curls out slowly on the tailgate.*"},
       {"t": "A gift", "r": "\"For me? You didn't have to. Oh, I'm gonna cry. Happy cryin'. Hold me?\"", "s": "*I give her a little ribbon-tied box.*"}],
     "after": "Curled up in your lap on Biscuit's tailgate under a quilt, fussed over and told she's sweet until she's a happy, slightly teary puddle. She tells you:",
     "list": [{"t": "{spoils}. Nobody ever spoiled me that specific before.", "need": ["spoils"]},
              {"t": "You held on till I said. That's the nicest thing.", "clean": True},
              {"t": "{safe}. I kept it close the whole time.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 20 SABLE
CONFIGS.append(dict(
  folder="20-sable", name="Sable", title="The Night Moth", font="cinzel", dark=True,
  palette=dict(bg="#07070a", card="#0e0e12", acc="#e0a35a", acc2="#e0a35a", soft="#1a1715", line="#2c2a2a", pane="#131217", btn="#18171c", hero="radial-gradient(circle at 70% 40%,#3a2a18,#0e0e12 60%)"),
  quote="\"Take it all away for a while. Just hold onto me while it's dark.\"",
  pills=["Submissive","Sensory","Bondage","Goth"],
  about="Sable keeps the shade house: black hellebores, ferns in deep shadow, one amber lamp making one warm circle. Blunt bangs, heavy liner, silver rings, a moth tattoo. She says very little, in very exact words. She's tired of looking at everything. She wants it taken away for a while, by someone who'll hold onto her while it's dark.",
  about2="Sable keeps the shade house.",
  details=["Sable x Any user","Honeypot Garden · Batch 2: Switches & Subs","Turn the lamp down, copy your starter into chat.","TW: Sensory deprivation, bondage","Pictures made by me."],
  cw="Sensory deprivation with blindfold and headphones, bondage with rope and leather cuffs, a resting hand at the throat. All characters are adults. Sable's limits are exact, her safeword is absolute, and two squeezes is her signal when she can't speak.",
  ooc="(OOC: her order: {far}. Off the table: {limit}. Her safeword: {safe}. Signal: two squeezes.)", sign="Don't make it weird. ~S.",
  sections=[
    survey("Her Terms", "The most she'll say all night.",
      "Restraint?", [
        ["Wrists, not ankles.", "Wrists. Not ankles.", "Sable tells me: wrists, not ankles."],
        ["Wrists and ankles.", "Both. Leather cuffs. Check them twice.", "Sable tells me both, and to check the cuffs twice."],
        ["None tonight. Just the dark.", "Just the dark. Okay.", "Sable tells me no restraint tonight, just the dark."]],
      "Order?", [
        ["Blindfold first, then headphones.", "Blindfold first. Then headphones."],
        ["Headphones first.", "Sound first. Then sight."],
        ["Both at once.", "All at once. Like a lamp going out."]],
      "Fine. Never that.",
      "e.g. moth", "Say it back. Two squeezes if I can't.", "Good. Don't make it weird."),
    {"type": "slider", "title": "The Lamp", "lede": "One amber lamp. Turn it down. She'll tell you when it's dark enough.",
     "min": 0, "max": 100, "start": 80, "unit": "%", "key": "lamp", "btn": "Turn it down",
     "bands": [
       {"upto": 5, "label": "Dark.", "r": "\"Oh.\" <i>A long breath out.</i> \"It's so quiet. Don't let go.\"", "s": "I turn the amber lamp all the way down."},
       {"upto": 35, "label": "Almost dark.", "r": "\"Lower.\"", "retry": True, "firm": True},
       {"upto": 100, "label": "Too bright.", "r": "\"Too much. Lower.\"", "retry": True, "firm": True}]},
    {"type": "hold", "title": "Hold On", "lede": "In the dark, hold onto her. Press and hold. She'll squeeze your hand when she's under.",
     "seconds": 10, "btn": "hold her", "doneBtn": "under",
     "lines": [[0, "Nothing. Your hand on hers."], [30, "Her breathing slows."], [60, "Her rings, cool against your fingers."], [90, "She goes very still. That's her trusting you."]],
     "early": ["\"Don't.\" <i>Her hand finds yours again.</i> \"Stay.\""],
     "done": "<i>One slow squeeze. Not two. One.</i> \"Just hold onto me while it's dark.\"", "s": "I hold onto her in the dark until she goes completely still."},
    {"type": "ending", "title": "The Dark", "lede": "Pick how she goes under.",
     "paths": [
       {"t": "Look at me", "r": "\"I can. I'm good at it. I'm so tired of looking at everything. That's the part I actually want.\"", "s": "\"Look at me while I tell you what to do.\""},
       {"t": "Bound", "r": "\"Oh. It's so quiet. Don't let go. Just hold onto me while it's dark.\"", "s": "*I tie the blindfold, bind her wrists, and rest my hand at her throat.*"},
       {"t": "Coming back", "r": "\"Like the world is too loud for a minute. Don't turn the lamp up yet. Just stay.\"", "s": "\"What's it like, coming back?\""}],
     "after": "The blindfold eased off slowly, a black blanket, and being held quietly in the amber light while the world returns. She says more than she meant to:",
     "list": [{"t": "{want} You remembered.", "need": ["want"]},
              {"t": "You didn't let go. Not once.", "clean": True},
              {"t": "{safe}. Or two squeezes. You knew.", "need": ["safe"]}]}
  ]))

# ---------------------------------------------------------------- 21 IVY & IRIS
CONFIGS.append(dict(
  folder="21-ivy-and-iris", name="Ivy & Iris", speaker="The twins", title="The Twin Vines", font="playfair",
  palette=dict(bg="linear-gradient(180deg,#dfeedd 0%,#f1ecf7 60%)", card="#fbfaf8", acc="#5b7f4a", acc2="#7a57a8", soft="#ebf1e6", line="#dcd8e6", pane="#ffffff", hero="radial-gradient(circle at 70% 30%,#b9a3dd,#5b7f4a 80%)", head="#2a2833", hshadow="0 2px 12px rgba(255,255,255,.5)"),
  quote="\"So? Who was sweeter?\"",
  pills=["Twins","Submissive","Praise","Sweet"],
  about="Ivy and Iris tend the vine arbor: grapevines overhead, wisteria spilling off the pergola, two ladders side by side. Identical, except Iris braids her hair and Ivy wears it down, and an ivy leaf is tattooed on one wrist and an iris on the other. They're sisters, so they compete. Praise one and the other tries twice as hard. Everything else is about you.",
  about2="Ivy and Iris tend the vine arbor.",
  details=["Ivy & Iris x Any user","Honeypot Garden · Batch 2: Switches & Subs","Judge who's sweeter, copy your starter into chat.","TW: Double submission, praise competition","Pictures made by me."],
  cw="Double submission to one partner, praise competition, kneeling, mirrored service. All characters are adults. Ivy and Iris are sisters and never touch each other sexually; all intimacy is with you. Each twin has her own safeword and her own limits.",
  ooc="(OOC: the twins are sisters and never touch each other; everything is with me. Off the table: {limit}. Safewords: {safe} for me, vine and petal for them.)", sign="Be good. Both of you. ~I & I.",
  sections=[
    survey("The Survey", "Maren sent it with a note. Both of them are reading over your shoulder.",
      "What do you want?", [
        ["Praise games. Me in charge.", "Ivy: \"Yes.\" Iris: \"Obviously.\"", "I tell the twins I want praise games, with me in charge."],
        ["I can't even tell you apart.", "Iris: \"Braid, Iris.\" Ivy: \"Hair down, Ivy. You'll learn.\"", "I admit I can't tell the twins apart, and they both point at their hair."],
        ["Hi. You must be the twins.", "Ivy: \"Hi!\" Iris: \"Hi. I'm the sweeter one.\" Ivy: \"No you're not.\"", "I say hi, and the twins immediately argue about who's sweeter."]],
      None, None,
      "Ivy: \"Got it.\" Iris: \"Written down. Twice. Once each.\"",
      "e.g. trellis", "Iris: \"Say it back.\" Ivy: \"Ours are vine and petal.\"", "Ivy: \"Good.\" Iris: \"Any of the three and everyone stops.\""),
    {"type": "actions", "title": "Who Was Sweeter", "lede": "Praise one and watch the other try twice as hard. Six turns. Then you decide.",
     "anyDone": 6,
     "meters": [{"key": "ivy", "label": "Ivy 🌿", "icon": "💚", "max": 5}, {"key": "iris", "label": "Iris 🪻", "icon": "💜", "max": 5}],
     "open": "Ivy: \"You tell us what you want first.\" Iris: \"Then you tell us who did it best.\"",
     "acts": [
       {"t": "\"Both of you. Kneel.\"", "d": {"ivy": 1, "iris": 1}, "r": "<i>They hit the boards at exactly the same moment and both look up to see who you're looking at.</i>", "s": "I point at the boards in front of me and tell both twins to kneel."},
       {"t": "Praise Ivy.", "repeat": True, "d": {"ivy": 1}, "r": "Ivy: \"Me! I knew it. Iris, did you hear?\" <i>Iris is already sitting up straighter.</i>", "s": "I tell Ivy she did it best."},
       {"t": "Praise Iris.", "repeat": True, "d": {"iris": 1}, "r": "Iris: \"Hmm. I told you I was sweeter.\" <i>Ivy pouts.</i> Iris: \"Don't pout, chị, it's not cute. It's a little cute.\"", "s": "I tell Iris she did it best."},
       {"t": "Give Ivy a task.", "d": {"ivy": 1}, "r": "<i>Ivy's up the ladder and back with a bunch of grapes before you finish asking.</i> Iris: \"Show-off.\""},
       {"t": "Give Iris a task.", "d": {"iris": 1}, "r": "<i>Iris brings you water and a folded cloth you didn't know you needed.</i> Ivy: \"Okay, that was good.\""},
       {"t": "\"You were both perfect.\"", "d": {"ivy": 1, "iris": 1}, "r": "Ivy: \"That's not a real answer.\" Iris: \"That's cheating.\" <i>They're both glowing anyway.</i>"}],
     "full": {"ivy": "Ivy: \"Me! Me me me.\" Iris: \"...Okay, you can be second best.\" <i>She's not actually upset. She's planning.</i>",
              "iris": "Iris: \"Mm. Obviously.\" Ivy: \"Next time.\" Iris: \"Next time I'll still be sweeter.\"",
              "any": "<i>They look at each other, then at you.</i> Ivy: \"So?\" Iris: \"Who was sweeter?\""}},
    {"type": "ending", "title": "The Arbor", "lede": "Pick who gets the praise.",
     "paths": [
       {"t": "Tell them apart", "r": "\"Braid, Iris. Hair down, Ivy. You'll learn. Praise one of us and you'll see who tries harder.\"", "s": "\"I can't even tell you apart.\""},
       {"t": "Praise Ivy", "r": "Ivy: \"Me! I knew it. Iris, did you hear? ...Okay, you can be second best.\"", "s": "*I tell Ivy she did it best.*"},
       {"t": "Praise Iris", "r": "Iris: \"Hmm. I told you I was sweeter. Don't pout, chị, it's not cute. It's a little cute.\"", "s": "*I tell Iris she did it best.*"}],
     "after": "A warm pile on their big couch with you in the middle, both praised equally, and each told one thing that's only hers. Then they report on you:",
     "list": [{"t": "Ivy: \"You kept score.\" Iris: \"We noticed. {winner} won.\" Ivy: \"This time.\"", "need": ["winner"]},
              {"t": "Iris: \"You said {safe} back without mixing it up with ours.\" Ivy: \"That's hard. We mix them up.\"", "need": ["safe"]}]}
  ]))
