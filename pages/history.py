import pyrebase
import streamlit as st
import streamlit.components.v1 as components

st.subheader("Saved Itineraries")
try :
    st.set_page_config(page_title="PassionPassport - History", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
    st.write(list(st.session_state.db.child(st.session_state.user['localId']).child("itinerary").get().val().values())[0])
except :
    st.error("You need to be logged in")

st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)


# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
st.write("*Copyright © 2023 T(P)JC - Harry, Brendan, Vanessa, Ryan*") 