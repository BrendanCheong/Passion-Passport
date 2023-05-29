import streamlit as st
import streamlit.components.v1 as components
import pyrebase
import pandas as pd


try : 
    st.set_page_config(page_title="PassionPassport - Price", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
    if st.session_state.flight is not None :
        flight = st.session_state.flight
        flights = []
        for flightDetail in flight :
            flightObject = {
                'oneWay': str(flightDetail['oneWay']),
            }
            flight.append(flightObject)
        flightData = pd.DataFrame(flights)
        st.write(flightData)
except:
    st.info("You need to be logged in")

st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)
# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
    

