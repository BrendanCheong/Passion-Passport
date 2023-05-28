import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import folium
from streamlit_folium import st_folium, folium_static


st.set_page_config(page_title="Travel App - Hobbies", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")

st.header("Travel App - Hobbies")
mapData = st.session_state.mapData
st.write(mapData)
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

st.write("Hobbies")