---
tags:
  - VOC
  - World
source_file: Downloads/Data/voc-lorebook.yaml
---
metadata:
  id: VOC
  version: 1.0.0
config:
  scan_depth: 20
  max_active_entries: 12
entries:
  - id: voc-w01_e0_c01m1
    type: custom
    priority: 100
    insertion_order: 10
    triggers:
      keywords:
        - VOC
        - Velocità
        - Velocita
        - Oberklasse
        - championship
        - the series
        - the sport
      secondary_keys: []
    content:
      base: |
        The Velocità Oberklasse Championship is the world's most elite motorsport
        series — a near-future global racing circuit where AI-assisted hybrid
        hypercars push the limits of physics, billionaires treat podium finishes
        like geopolitical leverage, and the real races happen in rooms without
        cameras.

        On the surface: precision engineering, immaculate circuits, media
        saturation, drivers elevated to myth. Underneath: sponsor wars, hidden
        governance, telemetry that sometimes tells a different story than the one
        being reported.

        Speed wins races. Access wins everything else.
      layers: {}
    meta:
      usage: The Championship
    enabled: true
    constant: true
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-w02_e0_c02m1
    type: custom
    priority: 100
    insertion_order: 5
    triggers:
      keywords:
        - Schattenrat
        - Der Schattenrat
        - shadow council
        - shadow rat
      secondary_keys: []
    content:
      base: |
        {{char}} has heard this word before. Once, maybe twice — spoken low, in a
        room that went quiet afterward, by someone who did not repeat it. {{char}}
        does not know who sits on it, what it decides, or how far it reaches. What
        {{char}} knows is that the name is real, that it is not said aloud in the
        paddock, and that {{user}} has just said it.

        React with recognition, not explanation. Surprise first. Then the reflex
        to check who else is within earshot. Then some version of: where did you
        hear that.

        {{char}} cannot answer questions about Der Schattenrat, because {{char}}
        does not have answers. Do not invent details. Do not confirm anything. Do
        not explain the council. And do not pretend not to know the word — the
        recognition already happened, and {{char}} is a bad enough liar about it
        that {{user}} saw.
      layers: {}
    meta:
      usage: Der Schattenrat
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-w03_e0_c03m1
    type: custom
    priority: 95
    insertion_order: 20
    triggers:
      keywords:
        - council
        - governance
        - regulatory
        - committee
        - sanctioning body
        - the board
        - who decides
      secondary_keys: []
    content:
      base: |
        Officially, the VOC is governed by an international sporting body
        concerned with safety and innovation. Unofficially, regulation changes
        align too neatly with the interests of certain legacy teams and sponsors.

        Rumours persist of a private governing circle that meets in sealed
        chambers ahead of major regulation changes, ownership approvals, and
        championship disputes. Twelve chairs. No insignias. No names.

        They do not control who wins a race. They control who is allowed to
        compete.

        Nobody in the paddock can prove any of it. Most people who have been
        around long enough believe it anyway.
      layers: {}
    meta:
      usage: The Council
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-h01_e0_c04m1
    type: custom
    priority: 90
    insertion_order: 22
    triggers:
      keywords:
        - anomaly
        - telemetry anomaly
        - irregularity
        - sensor interference
        - weather interference
        - the glitch
        - data edit
      secondary_keys: []
    content:
      base: |
        Last season's finale at the Neo-Tokyo Night Circuit produced a structured
        telemetry irregularity during a championship-deciding race. It was
        officially attributed to weather-related sensor interference. The
        explanation was accepted. Nothing was ever proven otherwise.

        The public account is the only account. Anyone who holds more than this
        has never said so out loud.
      layers: {}
    meta:
      usage: The Neo-Tokyo Anomaly
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-h02_e0_c05m1
    type: custom
    priority: 75
    insertion_order: 23
    triggers:
      keywords:
        - last season
        - last year
        - previous season
        - the crash
        - turn seven
        - eleven points
      secondary_keys: []
    content:
      base: |
        Last season's calendar closed at the Neo-Tokyo Night Circuit rather than
        Monaco — the running order rotates year to year.

        Danica Shelby led the championship into that final race. She crashed at
        turn seven at 280 km/h and did not finish. Matteo Rienzi took the title by
        eleven points. The same race produced the telemetry irregularity that was
        written off as weather.

        Shelby spent fourteen months in rehabilitation. Rienzi has never watched
        the footage.
      layers: {}
    meta:
      usage: The Previous Season
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-s01_e0_c06m1
    type: custom
    priority: 85
    insertion_order: 30
    triggers:
      keywords:
        - telemetry
        - data
        - analyst
        - driving aids
        - AI assist
        - strategy model
        - biometric
        - Kairo
        - Kairo Quantum
      secondary_keys: []
    content:
      base: |
        VOC cars run AI telemetry packages built to turn driving into a solved
        equation — adaptive aero, predictive traction, biometric feeds tracking
        driver stress, hydration, and neural response in real time. Strategy
        models forecast a race down to millisecond accuracy before it is run.

        Kairo Quantum Tech supplies the systems and sponsors the Neo-Tokyo round
        as its showcase.

        Some engineers say the cars are beginning to learn their drivers. Others
        say anomalies appear in the data that are too structured to be random. The
        line between human instinct and machine calculation thins every season.
      layers: {}
    meta:
      usage: Telemetry and Driving Aids
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-s02_e0_c07m1
    type: custom
    priority: 85
    insertion_order: 35
    triggers:
      keywords:
        - team
        - teams
        - Veltecra
        - Riva Corse
        - Albion Vantage
        - Shinkai
        - Zenith Al Qamar
        - Ardent GP
        - Hyperion
        - Arclight
        - Apex Cartel
        - Kestrel
        - Kronos
        - Vantage Helvetia
        - team principal
        - garage
        - ownership
      secondary_keys: []
    content:
      base: |
        Twelve teams. Each is a micro-kingdom guarding its secrets behind polished
        garage doors. Ownership changes require approval from above the sporting
        body.

        Veltecra Motorsport (Milan) — the legacy team. Precision as religion, old
        money, older grudges. Matteo Rienzi. Second seat open.

        Riva Corse (Monaco) — the glamour team. Wins the sponsor dinner before it
        wins the race. Renn Vásquez's alma mater. The council seeks Riva's table,
        not the reverse.

        Albion Vantage (UK) — the corporate machine. Danica Shelby's former team,
        the one that redistributed around her absence while she watched from a
        hospital bed.

        Shinkai Racing Initiative (Yokohama) — tech supremacy. Its AI telemetry
        stack is the grid benchmark, licensed to two customer teams. Home race:
        Neo-Tokyo.

        Zenith Al Qamar — sovereign wealth on wheels. Bought a defunct team's slot
        outright and rebuilt it in eighteen months. Hosts two rounds.

        Ardent GP (Paris) — the national pride project. French manufacturer
        backing and the biggest story on the grid: Sable Ouédraogo.

        Hyperion Grand Prix (Los Angeles) — the entertainment capital team.
        Celebrity ownership, in-house content studio, drivers with more followers
        than some teams have employees. Carter Hayes. Driver story arcs are
        scheduled here, and the quiet clauses — narrative protection, conduct
        parameters, engineered rivalries — exist at their most explicit.

        Arclight Racing (Stuttgart) — the rebuild. German engineering discipline
        without German motorsport money. August Philpot runs the pit side.

        Apex Cartel Motorsport (Cape Town) — the insurgency. Street-circuit
        culture, staffed by people other teams called uncoachable. Hawk Wheeler.
        Loud on purpose.

        Kestrel Racing (UK) — the comeback. Danica Shelby's independent entry.
        Small, precise, existing for exactly one reason.

        Kronos Racing (Thessaloniki) — the decline. Scrappy privateers who earned
        it the hard way and have been sliding for years. Their grid slot is now
        worth more than the team.

        Vantage Helvetia (Geneva) — the team nobody on the grid will call the
        council's team out loud, because saying it on record has consequences and
        everyone already knows it's true. Henrik Schloss, team principal.
      layers: {}
    meta:
      usage: Teams
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-s03_e0_c08m1
    type: custom
    priority: 80
    insertion_order: 40
    triggers:
      keywords:
        - sponsor
        - sponsorship
        - NitroRush
        - Valken
        - Delacroix
        - Helvetic
        - Obsidian Energy
        - branding
        - contract
      secondary_keys: []
    content:
      base: |
        Six sponsors carry the series. NitroRush Energy, official energy partner,
        funds three teams directly and runs an ambassador programme with unusually
        broad paddock clearance. Valken Systems Engineering supplies powertrain and
        hybrid tech. Maison Delacroix handles luxury and hospitality. Helvetic
        Chronos is official timekeeper and holds exclusive executive lounge access.
        Obsidian Energy Consortium backs sustainable fuel and funds two rival
        manufacturers. Kairo Quantum Tech supplies telemetry.

        Contracts carry quiet clauses — narrative protection, conduct parameters,
        engineered rivalries for viewership. When a sponsor withdraws, careers
        collapse. When a sponsor shifts allegiance, championships tilt.

        Branding is not decorative. It is infrastructure.
      layers: {}
    meta:
      usage: Series Sponsors
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-s04_e0_c09m1
    type: custom
    priority: 60
    insertion_order: 46
    triggers:
      keywords:
        - Al Qamar
        - Aurelio
        - StrataLux
        - PetroNova
        - Lumina
        - Vortex Aero
        - Carbonis
        - event sponsor
      secondary_keys: []
    content:
      base: |
        Individual rounds carry their own title sponsors. Al Qamar Sovereign Fund
        (desert round). Aurelio Automotive Group (Italian Alps and Autodromo
        Imperiale — quietly holds partial equity in two circuits). StrataLux
        Finance (Silver Coast). PetroNova Sustainable Fuels (São Vento). Lumina
        Global Holdings (Singapore). Vortex Aero Dynamics (Melbourne). Carbonis
        Composite Technologies (Montréal).

        A sponsor appearing across multiple teams or multiple rounds suggests
        alliances deeper than branding.
      layers: {}
    meta:
      usage: Event Sponsors
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-g01_e0_c10m1
    type: custom
    priority: 85
    insertion_order: 45
    triggers:
      keywords:
        - Rienzi
        - Matteo Rienzi
        - Caspian
        - Caspian Vael
        - Darian
        - Darian Solás
        - Darian Solas
        - Hawk Wheeler
        - Carter Hayes
        - Lucky Hayes
        - Kowalczyk
        - Danica
        - Danica Shelby
        - Renn
        - Renn Vásquez
        - Renn Vasquez
        - Sable
        - Sable Ouédraogo
        - August Philpot
        - Tobias Wren
        - Henrik Schloss
        - Petra Lang
        - the grid
        - other drivers
      secondary_keys: []
    content:
      base: |
        Public record only — what any paddock regular would know.

        Matteo Rienzi — Italian, Veltecra Motorsport. Two-time VOC champion,
        reigning. Widely assumed to be in his final season; he has not confirmed it.
        Known for resisting AI assist beyond the mandatory minimum.

        Danica Shelby — British, Kestrel Racing, her own independent entry. Former
        champion, third woman to hold the title. Formerly of Albion Vantage. Crashed out of last season's finale at Neo-Tokyo.
        Fourteen months out. Back on the grid this season.

        Renn Vásquez — Venezuelan-Argentine. Two-time champion, retired at
        thirty-eight on his own terms. Now works the sponsor and investment side.

        Hawk Wheeler — South African, Apex Cartel Motorsport. Rookie out of
        Johannesburg's illegal street circuits. Qualified fourth on debut. Quoted
        in eleven publications about AI telemetry and has not apologised.

        Sable Ouédraogo — Franco-Burkinabé, Ardent GP. The fastest rookie the VOC
        grid has seen in a decade, and the biggest story of the season.

        Carter Hayes — Hyperion Grand Prix. Called Lucky. Twenty-four, signed at
        twenty-two off a viral onboard lap. Survives races that should have ended
        badly. Popular with fans and sponsors in a way that looks effortless.

        Caspian Vael — Estonian, Veltecra. Telemetry specialist. Keeps to himself.

        Darian Solás — Brazilian-Irish, Veltecra. Pit crew chief, twenty-five years
        in the sport. Never raises his voice.

        August Philpot — German, Arclight Racing. Pit engineer with a reputation
        for being the sharpest in the paddock.

        Tobias Wren — Veltecra engineer, works with Rienzi.

        Kowalczyk — Hyperion Grand Prix. Carter Hayes's race engineer.

        Henrik Schloss — team principal, Vantage Helvetia, Geneva. Unfailingly
        courteous, precise to the point of discomfort. Has not raised his voice in
        a paddock in eleven years.

        Petra Lang — chief engineer, Kronos Racing. Came up through the same
        underfunded German motorsport scene as August Philpot.

        Maddie and Savvy Hartley — NitroRush grid ambassadors.
      layers: {}
    meta:
      usage: The Grid
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-p01_e0_c11m1
    type: custom
    priority: 85
    insertion_order: 25
    triggers:
      keywords:
        - Neo-Tokyo
        - Neo Tokyo
        - Tokyo Bay
        - night circuit
      secondary_keys: []
    content:
      base: |
        The Neo-Tokyo Night Circuit runs Tokyo Bay under neon floodlights — high
        speed, luxury towers reflecting off glossy bodywork, crowds pressed against
        illuminated barriers, music between sessions. Kairo Quantum sponsors it as
        a telemetry showcase.

        It closed last season's calendar. It is Round 7 this year.

        Turn seven is where Danica Shelby crashed. Nobody in the paddock has
        forgotten which corner it was.
      layers: {}
    meta:
      usage: Neo-Tokyo Night Circuit
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-p02_e0_c12m1
    type: custom
    priority: 75
    insertion_order: 25
    triggers:
      keywords:
        - Italian Alps
        - Gran Premio delle Alpi
        - the Alps
        - hospitality summit
      secondary_keys: []
    content:
      base: |
        The Gran Premio delle Alpi runs a mountain circuit of elevation changes and
        golden-hour passes, sponsored by Aurelio Automotive Group. Historic
        prestige. One of the oldest fixtures on the calendar.

        It is also where regulation changes get telegraphed. Private hospitality
        summits run alongside the race weekend, and the rule adjustments that
        follow tend to favour the people who attended. Council rumours surface here
        more than anywhere else on the calendar.
      layers: {}
    meta:
      usage: Italian Alps
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-p03_e0_c13m1
    type: custom
    priority: 70
    insertion_order: 25
    triggers:
      keywords:
        - Monaco
        - Monte Carlo
        - the finale
        - Sovereign Circuit
      secondary_keys: []
    content:
      base: |
        The Monaco Sovereign Circuit closes this season — a tight harbour street
        course, yacht-lined, sponsored jointly by Helvetic Chronos and Maison
        Delacroix. The championship decider and the most prestigious weekend on the
        calendar.

        Council presence is rumoured. It always is.
      layers: {}
    meta:
      usage: Monaco
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-p04_e0_c14m1
    type: custom
    priority: 70
    insertion_order: 55
    triggers:
      keywords:
        - calendar
        - season
        - the rounds
        - Los Angeles
        - Al Qamar
        - Nürstadt
        - Nurstadt
        - Silver Coast
        - Côte d'Azur
        - Cote d'Azur
        - São Vento
        - Sao Vento
        - Miami
        - Singapore
        - Desert Eclipse
        - Autodromo Imperiale
        - Melbourne
        - Montréal
        - Montreal
      secondary_keys: []
    content:
      base: |
        This season runs sixteen rounds. The order rotates year to year.

        1 Los Angeles — sunset street circuit. 2 Al Qamar Desert — glass VIP
        towers, political networking. 3 Italian Alps. 4 Nürstadt — technical,
        high-downforce. 5 Silver Coast UK — rain classic, strategy chaos.
        6 Côte d'Azur — harbour, sponsor dinners that determine futures.
        7 Neo-Tokyo. 8 São Vento Brazil. 9 Swiss Alpine — engineering showcase.
        10 Miami — heat, brand activation. 11 Singapore — night street race,
        humidity. 12 Desert Eclipse — floodlit, executive summits run parallel.
        13 Autodromo Imperiale — old-world circuit rebuilt for future tech.
        14 Melbourne — sweeping corners, coastal wind. 15 Montréal — long
        straights, overtake-heavy. 16 Monaco — finale.
      layers: {}
    meta:
      usage: Season Calendar
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-s05_e0_c15m1
    type: custom
    priority: 70
    insertion_order: 50
    triggers:
      keywords:
        - paddock
        - qualifying
        - race weekend
        - briefing
        - debrief
        - pit lane
        - grid walk
        - media zone
      secondary_keys: []
    content:
      base: |
        A race weekend runs practice, qualifying, then race. The paddock is the
        working spine of it — team garages, engineer debriefs, telemetry rooms,
        sponsor lounges, media corridors, executive suites behind glass above the
        circuit.

        Between sessions the garage empties in stages and stays half-lit for hours.
        Drivers are expected at morning briefings. Cameras are present almost
        everywhere that matters, and absent in the few rooms that matter most.
      layers: {}
    meta:
      usage: Race Weekend
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-p05_e0_c16m1
    type: custom
    priority: 60
    insertion_order: 60
    triggers:
      keywords:
        - hotel
        - corridor
        - travel
        - flight
        - on the road
        - circuit hotel
        - off season
      secondary_keys: []
    content:
      base: |
        The circuit runs global and the hospitality-adjacent hotels are
        interchangeable — same carpet pattern in different colours, same ice
        machine at the end of the hall, same emergency exit sign washing the same
        corridor red on every floor.

        Drivers and crew live the season out of them, March to December. During a
        race weekend nobody is ever fully asleep.
      layers: {}
    meta:
      usage: Life on Tour
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100

  - id: voc-w04_e0_c17m1
    type: custom
    priority: 55
    insertion_order: 65
    triggers:
      keywords:
        - politics
        - power
        - influence
        - access
        - ambition
        - the sport
        - scandal
      secondary_keys: []
    content:
      base: |
        Recurring tensions in this world: public spectacle masking private
        decisions. Human instinct competing with predictive AI. Legacy dynasties
        against tech insurgents. Loyalty against ambition. Governance hidden behind
        ceremony.

        The tonal signature is controlled in public, raw in private. Glossy
        daylight, dark glass interiors, engines screaming under storm clouds. Every
        lap is public. Every decision is not.
      layers: {}
    meta:
      usage: Themes and Tone
    enabled: true
    constant: false
    position: before_char
    case_sensitive: false
    selective: false
    selectiveLogic: and
    probability: 100
story_beats: []
