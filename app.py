import streamlit as st

from apputil import lowest_score, sort_names, ways


st.write(
'''
# Week 2 Exercises

Test the coin-change and student-score functions below.
''')

st.subheader("Coins")
amount = st.number_input("Exercise Input: ", 
                         value=None, 
                         min_value=0,
                         step=1, 
                         format="%d")

if amount is not None:
    st.write(f"There are {ways(amount)} different ways to make {amount} cents using only pennies and nickels.")

st.subheader("Student scores")
names_text = st.text_input(
    "Names (comma separated)",
    "Hannah, Astrid, Abdul, Mauve, Jung",
)
scores_text = st.text_input(
    "Scores (comma separated)",
    "99, 71, 85, 62, 91",
)

try:
    names = [name.strip() for name in names_text.split(",") if name.strip()]
    scores = [float(score.strip()) for score in scores_text.split(",")]

    if len(names) != len(scores) or not names:
        st.error("Enter the same non-zero number of names and scores.")
    else:
        st.write(f"Lowest score: {lowest_score(names, scores)}")
        st.write("Highest to lowest:", sort_names(names, scores).tolist())
except ValueError:
    st.error("Each score must be a number.")
