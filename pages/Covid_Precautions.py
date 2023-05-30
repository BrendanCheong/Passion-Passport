import pyrebase
import streamlit as st
import streamlit.components.v1 as components

try :
    st.set_page_config(page_title="PassionPassport - COVID Information", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
    st.subheader("COVID-19 Travel Information")
    if 'covid' in st.session_state : 
        covid = st.session_state.covid
        st.image("https://img.freepik.com/free-vector/covid-safe-travel-banner-design-with-passengers-wearing-masks_1308-87504.jpg")
        st.title(covid['area']['name'])
        st.subheader("Covid Situation")
        components.html('<p style="font-family: sans-serif; font-weight: 400">' + covid['summary']['text'] + "</p>", height=200)
        st.divider()

        st.subheader("What you need to declare")
        components.html('<p style="font-family: sans-serif; font-weight: 400">' + covid['areaAccessRestriction']['declarationDocuments']['text'] + "</p>", height=200)
        st.divider()

        st.subheader("Masks Requirements")
        components.html('<p style="font-family: sans-serif; font-weight: 400">' + covid['areaAccessRestriction']['masks']['text'] + "</p>", height=200)
        st.divider()

except Exception as e :
    st.error(e)

st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)