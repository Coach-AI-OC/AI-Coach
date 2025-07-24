import streamlit as st

# ---------------------- PLAY DATABASE ----------------------
play_database = [
    # ... [Your entire play database list goes here, unchanged] ...
    # (Paste all plays from previous message)
]

# -------------------- STREAMLIT APP UI/LOGIC --------------------
st.title("AI Offensive Coordinator - Alabama PDF Edition")
st.markdown("Select down, distance, and coverage to get your play!")

down = st.selectbox("Down", ["1st", "2nd", "3rd", "4th"])
distance = st.selectbox("Distance", ["Short yardage", "Any", "3rd & Medium", "3rd & Short"])
coverages = st.multiselect(
    "Pre-Snap Defensive Look (pick 1 or 2)",
    ["Cover 0", "Cover 1", "Cover 2", "Cover 3", "Cover 4", "Match", "Blitz", "Man", "All"],
    max_selections=2
)

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
