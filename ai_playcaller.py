import streamlit as st

# ---------------------- PLAY DATABASE ----------------------
play_database = [
    # --- GUN BUNCH OPEN OFFSET ---
    {
        "formation": "Gun Bunch Open Offset",
        "play_name": "RPO Read Bubble",
        "vs_coverages": ["Cover 3", "Cover 4", "Man"],
        "down_distance": "Any",
        "alignment": "Bunch on wide side. X=outside left, B=outside bunch, Y=inside bunch, RB=middle bunch, A=HB",
        "hot_routes": {
            "X": "Bubble (if pre-snap numbers advantage)",
            "B": "Slant",
            "Y": "Block",
            "RB": "Block",
            "A": "Inside Zone run (default)"
        },
        "read_progression": "Read edge defender: If he crashes, throw bubble. If he sits, hand off.",
        "target_zone": "Flat (Bubble) or inside (run)",
        "tip": "Key: Always check numbers before snap—bubble only if outside is light."
    },
    {
        "formation": "Gun Bunch Open Offset",
        "play_name": "RPO Alert Shock",
        "vs_coverages": ["Cover 2", "Cover 4", "Man"],
        "down_distance": "Any",
        "alignment": "Bunch on wide side. X=outside left, B=outside bunch, Y=inside bunch, RB=middle bunch, A=HB",
        "hot_routes": {
            "X": "Now screen",
            "B": "Slant",
            "Y": "Block",
            "RB": "Block",
            "A": "Inside Zone run"
        },
        "read_progression": "If defenders overreact inside, throw X now screen.",
        "target_zone": "Outside left or inside",
        "tip": "Best when slot defender is creeping toward box."
    },
    {
        "formation": "Gun Bunch Open Offset",
        "play_name": "Inside Zone",
        "vs_coverages": ["All"],
        "down_distance": "Any",
        "alignment": "Bunch on wide side.",
        "hot_routes": {
            "X": "Block",
            "B": "Block",
            "Y": "Block",
            "RB": "Block",
            "A": "Inside Zone run"
        },
        "read_progression": "Read play-side A gap.",
        "target_zone": "A/B gap",
        "tip": "Hit where the front is soft—cut back if unbalanced."
    },
    {
        "formation": "Gun Bunch Open Offset",
        "play_name": "Mesh Corner #1",
        "vs_coverages": ["Cover 3", "Cover 2", "Man"],
        "down_distance": "Any",
        "alignment": "Standard bunch; X=outside left, B=outside bunch, Y=inside bunch, RB=middle bunch, A=HB",
        "hot_routes": {
            "X": "Drag",
            "B": "Corner",
            "Y": "Drag",
            "RB": "Wheel",
            "A": "Block"
        },
        "read_progression": "Y Drag → B Corner → X Drag",
        "target_zone": "Sideline (Corner) and shallow crossers",
        "tip": "Drag routes create rubs vs man; corner beats zone."
    },
    {
        "formation": "Gun Bunch Open Offset",
        "play_name": "Mesh Corner #2",
        "vs_coverages": ["Cover 3", "Cover 4", "Man"],
        "down_distance": "Any",
        "alignment": "Standard bunch",
        "hot_routes": {
            "X": "Drag",
            "B": "Corner",
            "Y": "Wheel",
            "RB": "Drag",
            "A": "Block"
        },
        "read_progression": "RB Drag → B Corner → Y Wheel",
        "target_zone": "Shallow middle & sideline",
        "tip": "Wheel can pop vs match or slow zone drops."
    },
    {
        "formation": "Gun Bunch Open Offset",
        "play_name": "Y Trail #1",
        "vs_coverages": ["Cover 1", "Cover 3", "Man"],
        "down_distance": "3rd & Medium",
        "alignment": "Bunch right",
        "hot_routes": {
            "X": "Dig",
            "B": "Post",
            "Y": "Trail (deep crosser)",
            "RB": "Block",
            "A": "Block"
        },
        "read_progression": "Y Trail → B Post → X Dig",
        "target_zone": "Deep middle and sideline",
        "tip": "Trail route destroys man coverage."
    },
    {
        "formation": "Gun Bunch Open Offset",
        "play_name": "Flood",
        "vs_coverages": ["Cover 3", "Cover 2", "Match"],
        "down_distance": "Any",
        "alignment": "Bunch left",
        "hot_routes": {
            "X": "Clearout Streak",
            "B": "Deep Out",
            "Y": "Flat",
            "RB": "Block",
            "A": "Block"
        },
        "read_progression": "Y Flat → B Out → X Streak (clear)",
        "target_zone": "Sideline (flood concept)",
        "tip": "Flood high/low reads zone sideline defenders."
    },
    {
        "formation": "Gun Bunch Open Offset",
        "play_name": "Mesh Spot #1",
        "vs_coverages": ["Cover 2", "Cover 3", "Man"],
        "down_distance": "3rd & Short",
        "alignment": "Bunch right",
        "hot_routes": {
            "X": "Drag",
            "B": "Spot",
            "Y": "Flat",
            "RB": "Block",
            "A": "Block"
        },
        "read_progression": "X Drag → B Spot → Y Flat",
        "target_zone": "Underneath and flat",
        "tip": "Spot is safe checkdown vs zone."
    },

    # --- GUN TIGHT OPEN ---
    {
        "formation": "Gun Tight Open",
        "play_name": "Inside Zone",
        "vs_coverages": ["All"],
        "down_distance": "Any",
        "alignment": "Tight splits; X=outside left, Y=inside left, A=inside right, B=outside right, RB=HB",
        "hot_routes": {
            "X": "Block",
            "Y": "Block",
            "A": "Block",
            "B": "Block",
            "RB": "Inside Zone run"
        },
        "read_progression": "Hit play-side A/B gap",
        "target_zone": "A/B gap",
        "tip": "Trust zone rules, but cut back if the hole's not there."
    },
    {
        "formation": "Gun Tight Open",
        "play_name": "Speed Option",
        "vs_coverages": ["All"],
        "down_distance": "Any",
        "alignment": "Tight splits",
        "hot_routes": {
            "X": "Block",
            "Y": "Block",
            "A": "Block",
            "B": "Block",
            "RB": "Option (pitch read)"
        },
        "read_progression": "Read edge: QB keep or pitch to RB.",
        "target_zone": "Edge/outside",
        "tip": "Option is deadly if end crashes hard."
    },
    {
        "formation": "Gun Tight Open",
        "play_name": "Mtn RPO Read Flat",
        "vs_coverages": ["Cover 2", "Cover 3", "Cover 4"],
        "down_distance": "Any",
        "alignment": "Motions Y to flat",
        "hot_routes": {
            "X": "Slant",
            "Y": "Motion to Flat",
            "A": "Block",
            "B": "Block",
            "RB": "Run/Block"
        },
        "read_progression": "If flat is open, throw. If not, hand off.",
        "target_zone": "Flat or inside",
        "tip": "Watch numbers outside—don't force flat throw."
    },
    {
        "formation": "Gun Tight Open",
        "play_name": "Dig Z Spot",
        "vs_coverages": ["Cover 3", "Man"],
        "down_distance": "3rd & Medium",
        "alignment": "Tight splits",
        "hot_routes": {
            "X": "Dig",
            "Y": "Spot",
            "A": "Block",
            "B": "Fade",
            "RB": "Block"
        },
        "read_progression": "Y Spot → X Dig → B Fade",
        "target_zone": "Middle (dig) and spot window",
        "tip": "Dig route finds hole behind linebackers."
    },
    {
        "formation": "Gun Tight Open",
        "play_name": "Bench Z Spot",
        "vs_coverages": ["Cover 2", "Cover 3", "Match"],
        "down_distance": "Any",
        "alignment": "Tight splits",
        "hot_routes": {
            "X": "Out",
            "Y": "Bench Spot",
            "A": "Block",
            "B": "Fade",
            "RB": "Block"
        },
        "read_progression": "Y Spot → X Out → B Fade",
        "target_zone": "Sideline and bench spot",
        "tip": "Bench concept is deadly vs zone. Fade is bail-out vs press."
    },
    {
        "formation": "Gun Tight Open",
        "play_name": "HB Slip Screen",
        "vs_coverages": ["Blitz", "Cover 1", "Cover 0"],
        "down_distance": "Any",
        "alignment": "Tight splits",
        "hot_routes": {
            "X": "Block",
            "Y": "Block",
            "A": "Block",
            "B": "Block",
            "RB": "Slip Screen"
        },
        "read_progression": "Let rush come, dump to RB.",
        "target_zone": "Screen window",
        "tip": "Use vs aggressive blitzers. Don't throw early!"
    },
    {
        "formation": "Gun Tight Open",
        "play_name": "Mtn PA Cross",
        "vs_coverages": ["Cover 3", "Cover 4", "Man"],
        "down_distance": "Any",
        "alignment": "Tight splits, motion Y",
        "hot_routes": {
            "X": "Post",
            "Y": "Motion Cross",
            "A": "Block",
            "B": "Streak",
            "RB": "Block"
        },
        "read_progression": "Y Cross → X Post → B Streak",
        "target_zone": "Middle and deep",
        "tip": "Crossing routes are money vs man. Post can split zone."
    },

    # --- SHORT YARDAGE (from Gun Normal Flex Snug, Gun Trips HB Wk, etc.) ---
    {
        "formation": "Pistol Wing Flex Close",
        "play_name": "Speed Option",
        "vs_coverages": ["All"],
        "down_distance": "Short yardage",
        "alignment": "Wing flex close",
        "hot_routes": {
            "X": "Block",
            "Y": "Block",
            "A": "Block",
            "B": "Block",
            "RB": "Option pitch"
        },
        "read_progression": "Read EMOL for pitch/keep.",
        "target_zone": "Edge",
        "tip": "Best for 4th and short vs light box."
    },
    {
        "formation": "Gun Normal Flex Snug",
        "play_name": "RPO Alert WR Screens",
        "vs_coverages": ["Blitz", "Cover 0", "Man"],
        "down_distance": "Short yardage",
        "alignment": "Flex snug",
        "hot_routes": {
            "X": "Screen",
            "Y": "Screen",
            "A": "Block",
            "B": "Screen",
            "RB": "Block"
        },
        "read_progression": "Pick best leverage screen.",
        "target_zone": "Perimeter",
        "tip": "If defense loads the box, flip screen to the best side."
    },
    {
        "formation": "Gun Trips HB Wk",
        "play_name": "HB Angle Screen",
        "vs_coverages": ["Blitz", "Cover 1", "Cover 0"],
        "down_distance": "Short yardage",
        "alignment": "Trips left, HB weak",
        "hot_routes": {
            "X": "Block",
            "Y": "Block",
            "A": "Block",
            "B": "Block",
            "RB": "Angle Screen"
        },
        "read_progression": "Let defense come, then dump to RB.",
        "target_zone": "Screen window",
        "tip": "Use angle screen if MLB blitzes."
    },
]

# -------------------- SMART PLAY TYPE TAGGING --------------------
def infer_play_type(play):
    """Infer play type for smarter recommendation"""
    name = play["play_name"].lower()
    if "zone" in name or "option" in name or "inside zone" in name:
        return "run"
    if "rpo" in name:
        return "rpo"
    if "screen" in name:
        return "screen"
    return "pass"

for play in play_database:
    play["play_type"] = infer_play_type(play)

# -------------------- STREAMLIT APP UI/LOGIC --------------------
st.title("AI Offensive Coordinator - Alabama PDF Edition (Smart)")
st.markdown("Select down, distance, and coverage to get your best play for the situation!")

down = st.selectbox("Down", ["1st", "2nd", "3rd", "4th"])
distance = st.selectbox("Distance", ["Short yardage", "Any", "3rd & Medium", "3rd & Short", "3rd & Long"])
coverages = st.multiselect(
    "Pre-Snap Defensive Look (pick 1 or 2)",
    ["Cover 0", "Cover 1", "Cover 2", "Cover 3", "Cover 4", "Match", "Blitz", "Man", "All"],
    max_selections=2
)

def get_priority(play):
    play_type = play.get("play_type", "pass")
    if "Short" in distance:
        return {"run": 0, "rpo": 1, "screen": 2, "pass": 3}[play_type]
    elif "Long" in distance:
        return {"pass": 0, "screen": 1, "rpo": 2, "run": 3}[play_type]
    else:
        return {"pass": 0, "rpo": 1, "screen": 2, "run": 3}[play_type]

if st.button("Get Play Suggestion"):
    matching_plays = []
    exact_match_plays = []
    for play in play_database:
        down_match = (
            play["down_distance"] == distance
            or play["down_distance"] == down
            or (play["down_distance"] == "Any" and distance == "Any")
        )
        coverage_match = (
            any(c in play["vs_coverages"] for c in coverages)
            or play["vs_coverages"] == ["All"]
        )
        if down_match and coverage_match:
            if play["down_distance"] != "Any":
                exact_match_plays.append(play)
            matching_plays.append(play)

    # Prefer exact distance matches, then fall back to 'Any'
    if exact_match_plays:
        plays_to_show = sorted(exact_match_plays, key=get_priority)[:2]
    else:
        plays_to_show = sorted(matching_plays, key=get_priority)[:2]

    if plays_to_show:
        for found_play in plays_to_show:
            st.subheader(f"Play: {found_play['play_name']}")
            st.write(f"**Formation:** {found_play['formation']}")
            st.write(f"**Alignment:** {found_play['alignment']}")
            st.write("**Hot Routes (Button Mapped):**")
            for button, route in found_play['hot_routes'].items():
                st.write(f"- **{button}**: {route}")
            st.write(f"**Read Progression:** {found_play['read_progression']}")
            st.write(f"**Target Zone:** {found_play['target_zone']}")
            st.info(found_play['tip'])
    else:
        st.warning("No match found. Try different down/distance/coverage.")
