import streamlit as st
import streamlit.components.v1 as components
import pyrebase

def submitForm(s) :
    results = st.session_state.db.child(st.session_state.user['localId']).child("itinerary").push(s)
    st.info("Success")

try :
    st.set_page_config(page_title="PassionPassport - Price", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
    st.write(st.session_state.itin)
    if st.session_state.user is not None :
        with st.form("Form") :
            press = st.form_submit_button("Save")
            if press :
                submitForm(st.session_state.itin)
except :
    st.info("You must be logged in to access this page")

st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)