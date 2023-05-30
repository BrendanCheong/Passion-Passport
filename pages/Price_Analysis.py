import streamlit as st
import streamlit.components.v1 as components
import pyrebase
import pandas as pd


try : 
    st.set_page_config(page_title="PassionPassport - Price Analysis", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
    currentDB = st.session_state.db.child(st.session_state.user['localId'])
    flights = []
    # st.write(currentDB.child['ticket_price'].get())
    flightsFirebase = currentDB.child('ticket_price').get().val().values()
    flights.extend(flightsFirebase)
    if 'flight' in st.session_state :
        flight = st.session_state.flight
        for flightDetail in flight :
            flightObject = {
                'oneWay': str(flightDetail["oneWay"]),
                "lastTicketingDate": flightDetail["lastTicketingDate"],
                'seats_available': flightDetail["numberOfBookableSeats"],
                'price': flightDetail['price']['total']

            }
            flights.append(flightObject)
        
            currentDB.child(st.session_state.user['localId']).child('ticket_price').push(flightObject)
    flightData = pd.DataFrame(flights)
    st.write(flightData)
except Exception as e:
    st.info(e)

st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)
# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
st.write("*Copyright © 2023 T(P)JC - Harry, Brendan, Vanessa, Ryan*") 
    

