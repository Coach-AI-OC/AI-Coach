import streamlit as st

# -------------------------
# FORMATIONS & PLAY DATABASE
# -------------------------

play_database = [
    {
        "formation": "Gun Bunch Wide",
        "play_name": "Clearout FL In 2",
        "vs_coverages": ["Cover 3", "Cover 4", "Cover 0"],
        "down_distance": "Any",
        "alignment": "Bunch to the wide side (trips rule)",
        "hot_routes": {
            "X": "Drag",
            "B": "10-yard Out (Stem up 2x)",
            "A": "Fade",
            "RB": "Leave default",
            "Y": "Block"
        },
        "read_progression": "B Out → X Drag → A Fade",
        "target_zone": "Right Deep (Zone 6 or 9 based on side)",
        "tip": "If safety bites on the drag, hit the Out route."
    },
    {
        "formation": "Trips X Nasty",
        "play_name": "Slot Fade H Wheel 1",
        "vs_coverages": ["Cover 3", "Cover 4", "Man"],
        "down_distance": "3rd & Long",
        "alignment": "Trips to the wide side (hash mark rule)",
        "hot_routes": {
            "X": "Streak",
            "B": "Comeback",
            "A": "Drag",
            "RB": "Flat",
            "Y": "Block"
        },
        "read_progression": "RB Flat → A Drag → B Comeback",
        "target_zone": "Wide Side Sideline (Zone 3 or 6)",
        "tip": "Dual flood concept. Hit comeback if user bails."
    },
]

# -------------------------
# STREAMLIT UI
# -------------------------

st.title("AI Offensive Coordinator")
st.markdown("Get your best play call based on down, distance, and up to 2 coverage looks.")

down = st.selectbox("Down", ["1st", "2nd", "3rd", "4th"])
distance = st.selectbox("Distance", ["Short (1-3 yds)", "Medium (4-7 yds)", "Long (8+ yds)"])
coverages = st.multiselect(
    "Pre-Snap Defensive Look (choose 1 or 2)",
    ["Cover 0", "Cover 1", "Cover 2", "Cover 3", "Cover 4", "Cover 6", "Palms", "Tampa 2", "Match"],
    max_selections=2
)

if st.button("Get Play Suggestion"):
    found_play = None
    for play in play_database:
        if any(c in play["vs_coverages"] for c in coverages) and (
            play["down_distance"] == "Any" or (down == "3rd" and "Long" in distance and play["down_distance"] == "3rd & Long")
        ):
            found_play = play
            break

    if found_play:
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
        st.warning("No exact match found for this situation. Try a different input or add more plays to your database.")
