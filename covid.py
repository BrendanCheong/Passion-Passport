import pyrebase
import streamlit as st
import streamlit.components.v1 as components
from bs4 import BeautifulSoup

try :
    st.set_page_config(page_title="PassionPassport - Covid Information", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
    st.subheader("COVID-19 Information")
    if 'covid' in st.session_state : 
        covid = st.session_state.covid
        st.write(covid['area']['name'])
        text1 = covid['summary']['text'] 
        soup1 = BeautifulSoup(text1, "html.parser")
        clean_text1 = soup1.get_text()
        st.write(clean_text1)
        text2 = covid['areaAccessRestriction']['declarationDocuments']['text']
        soup2 = BeautifulSoup(text2, "html.parser")
        clean_text2 = soup2.get_text()
        st.write(clean_text2)
        text3 = covid['areaAccessRestriction']['masks']['text']
        soup3 = BeautifulSoup(text3, "html.parser")
        clean_text3 = soup3.get_text()
        st.write(clean_text3)
        text4 = covid['areaAccessRestriction']['exit']['text']
        soup4 = BeautifulSoup(text4, "html.parser")
        clean_text4 = soup4.get_text()
        st.write(clean_text4)
        
except Exception as e :
    st.error(e)

st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)