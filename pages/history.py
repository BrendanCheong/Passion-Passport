import pyrebase
import streamlit as st
import streamlit.components.v1 as components

try :
    st.set_page_config(page_title="Travel App - Hobbies", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
    st.write(list(st.session_state.db.child(st.session_state.user['localId']).child("itinerary").get().val().values())[0])
except :
    st.error("You need to be logged in")