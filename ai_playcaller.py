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
    # ... (rest of your database unchanged) ...
    # For brevity, paste ALL your previous play entries here
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
    # If it's 3rd & Medium/Long and not the above, it's probably a pass
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
    # Short yardage: prefer run, RPO, screen > pass
    # 3rd & Long: prefer pass > screen > rpo > run
    # Everything else: pass > rpo > run > screen
    play_type = play.get("play_type", "pass")
    if "Short" in distance:
        return {"run": 0, "rpo": 1, "screen": 2, "pass": 3}[play_type]
    elif "Long" in distance:
        return {"pass": 0, "screen": 1, "rpo": 2, "run": 3}[play_type]
    else:
        return {"pass": 0, "rpo": 1, "screen": 2, "run": 3}[play_type]

if st.button("Get Play Suggestion"):
    matching_plays = []
    for play in play_database:
        down_match = (
            play["down_distance"] == "Any"
            or play["down_distance"] == down
            or play["down_distance"] in distance
            or distance in play["down_distance"]
        )
        coverage_match = (
            any(c in play["vs_coverages"] for c in coverages)
            or play["vs_coverages"] == ["All"]
        )
        if down_match and coverage_match:
            matching_plays.append(play)

    # Sort by situation priority
    matching_plays = sorted(matching_plays, key=get_priority)
    # Only show up to the best two matches
    if matching_plays:
        for found_play in matching_plays[:2]:
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
