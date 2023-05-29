import streamlit as st
import streamlit.components.v1 as components
import pyrebase
import pandas as pd


try : 
    st.set_page_config(page_title="Travel App - Hobbies", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
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
    

