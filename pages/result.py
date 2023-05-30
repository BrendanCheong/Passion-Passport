import streamlit as st
import streamlit.components.v1 as components
import pyrebase

def submitForm(s) :
    results = st.session_state.db.child(st.session_state.user['localId']).child("itinerary").push(s)
    st.info("Success")

try :
<<<<<<< HEAD
    st.set_page_config(page_title="PassionPassport - Price", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
=======
    st.set_page_config(page_title="PassionPassport -Result", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
>>>>>>> e94a37745e14e69a860e6ea36beab09e3b322009

    st.subheader("Passion Passport Result")
    st.write("This is the result from our algorithm to give you the best itinerary in the world")
    if 'itin' in st.session_state :
        itins = st.session_state.itin.split('\n') 
        for itin in itins :
            if len(itin) > 10 :
                components.html('<div style="height: min-content"><p style="font-weight: 400; font-size: 14px; font-family: sans-serif;">' + itin + "</p></div>", height=70)
            else :
                components.html('<p style="font-weight: 800; font-size: 16px; font-family: sans-serif;">' + itin + "</p>", height=40)

    else :
        st.write("Before getting the result, please proceed to the home page and sign in")
    if 'user' in st.session_state:
        with st.form("Form") :
            press = st.form_submit_button("Save")
            if press :
                submitForm(st.session_state.itin)
except :
    st.info("You must be logged in to access this page and you must also run the travel machine")

st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)
# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
st.write("*Copyright © 2023 T(P)JC - Harry, Brendan, Vanessa, Ryan*") 