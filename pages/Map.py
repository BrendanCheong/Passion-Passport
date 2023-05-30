import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import folium
from streamlit_folium import st_folium, folium_static


st.set_page_config(page_title="PassionPassport - Map", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

try :
    st.header("Map Data")
<<<<<<< HEAD
<<<<<<< HEAD:pages/hobbies.py
    st.write("*A detailed map that displays locations to carry out your recommended activities!*")
    st.text("To view information here, please create an itinerary on our home page first!")
=======
    st.text("To be able to see something here, you need to do the travel analysis first!")

>>>>>>> e94a37745e14e69a860e6ea36beab09e3b322009:pages/Map.py
=======
    st.write("*A detailed map that displays locations to carry out your recommended activities!*")
    st.text("To view information here, please create an itinerary on our home page first!")
>>>>>>> 783eeb382ed13569874106dedaef67b36914ccbe
    if 'mapData' in st.session_state :
        mapData = st.session_state.mapData
        dataMap = pd.DataFrame(mapData)
        dataMap['latitude'] = pd.to_numeric(dataMap['latitude'])
        dataMap['longitude'] = pd.to_numeric(dataMap['longitude'])
        m = folium.Map(location=[dataMap.latitude.mean(), dataMap.longitude.mean()], 
                        zoom_start=12, control_scale=True)

        #Loop through each row in the dataframe
        for i,row in dataMap.iterrows():
            #Setup the content of the popup
            html = f'''
                <p>{str(row["name"])}<p/>
                <p>{str(row['safe'])}</p>
                '''
            iframe = folium.IFrame(html)
            
            
            #Initialise the popup using the iframe
            popup = folium.Popup(iframe, min_width=300, max_width=300)
            
            #Add each row to the map
            folium.Marker(location=[row['latitude'],row['longitude']],
                        popup = popup, c=row['name']).add_to(m)

        st_data = st_folium(m, width=700)
except Exception as e :
    st.error(e)


#st.write("Hobbies")
st.write("*Copyright © 2023 T(P)JC - Harry, Brendan, Vanessa, Ryan*") 