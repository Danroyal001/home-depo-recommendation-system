import streamlit as st

st.title("Projects")

if "search_term" not in st.session_state:
    st.session_state["search_term"] = ""

st.write("You have entered", st.session_state["search_term"])
