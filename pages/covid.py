import pyrebase
import streamlit as st
import streamlit.components.v1 as components

try :
    st.set_page_config(page_title="PassionPassport - About Us", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
    st.subheader("All information regarding the covid situation in your destination journey")
    if 'covid' in st.session_state : 
        covid = st.session_state.covid
        st.write(covid['area']['name'])
        components.html(covid['summary']['text'])
        components.html(covid['areaAccessRestriction']['declarationDocuments']['text'])
        components.html(covid['areaAccessRestriction']['masks']['text'])
        components.html(covid['areaAccessRestriction']['exit']['text'])
except Exception as e :
    st.error(e)