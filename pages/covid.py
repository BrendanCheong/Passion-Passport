import pyrebase
import streamlit as st
import streamlit.components.v1 as components

try :
    st.set_page_config(page_title="PassionPassport - Covid Information", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
    st.subheader("All information regarding the Covid situation in your destination journey")
    if 'covid' in st.session_state : 
        covid = st.session_state.covid
        st.write(covid['area']['name'])
        components.html(covid['summary']['text'])
        components.html(covid['areaAccessRestriction']['declarationDocuments']['text'])
        components.html(covid['areaAccessRestriction']['masks']['text'])
        components.html(covid['areaAccessRestriction']['exit']['text'])
except Exception as e :
    st.error(e)

st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)