import pyrebase
import streamlit as st
import streamlit.components.v1 as components

try :
    st.set_page_config(page_title="PassionPassport - About Us", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
    st.subheader("All information regarding the covid situation in your destination journey")
    if 'covid' in st.session_state : 
        covid = st.session_state.covid
        st.write(covid['area']['name'])
        st.subheader("Covid Situation")
        components.html('<p style="font-family: sans-serif; font-weight: 400">' + covid['summary']['text'] + "</p>")
        st.divider()

        st.subheader("What you need to declare")
        components.html('<p style="font-family: sans-serif; font-weight: 400">' + covid['areaAccessRestriction']['declarationDocuments']['text'] + "</p>")
        st.divider()

        st.subheader("Masks Requirements")
        components.html('<p style="font-family: sans-serif; font-weight: 400">' + covid['areaAccessRestriction']['masks']['text'] + "</p>")
        st.divider()

        st.subheader("Exit Requirements")
        components.html('<p style="font-family: sans-serif; font-weight: 400">' + covid['areaAccessRestriction']['exit']['text'] + "</p>")
        st.divider()
except Exception as e :
    st.error(e)