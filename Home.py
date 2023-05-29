import pyrebase
import streamlit as st
import asyncio
import requests
from datetime import datetime
import re
import openai
import streamlit.components.v1 as components
from streamlit_pills import pills
import pycountry
import pandas as pd
import folium
from streamlit_folium import st_folium, folium_static
from PIL import Image
import streamlit as st

# You can always call this function where ever you want

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo



firebaseConfig = {
  "apiKey": "AIzaSyCgRqAR-Hr5yNeG31Qgd9ROgBpAOZqRtPc",
  "authDomain": "lifehack2023-f362e.firebaseapp.com",
  "projectId": "lifehack2023-f362e",
  "storageBucket": "lifehack2023-f362e.appspot.com",
  "messagingSenderId": "141951242897",
  "appId": "1:141951242897:web:afa573c83b30d45a19e530",
  "measurementId": "G-EDRDB79V2N",
  "databaseURL": "https://lifehack2023-f362e-default-rtdb.asia-southeast1.firebasedatabase.app/"
}


def isFloat(x):
    try:
        float(x)
        return True
    except:
        return False
    
# String will look something like "x: (2.342,3.124),y: (5.2443,1.4536)"
def find_long_and_lat(s):
    lst = []
    curr_left, curr_comma, curr_right = -1, -1, -1
    for i in range(len(s)):
        if (s[i] == "("):
            curr_left = i
        elif (s[i] == ","):
            if (curr_left != -1):
                curr_comma = i
        elif (s[i] == ")"):
            if (curr_comma > curr_left):
                curr_right = i
                long = s[curr_left + 1: curr_comma]
                lat = s[curr_comma + 2: curr_right]
                if ((len(long) > 3) and (long[-1].isalpha())):
                    long = long[-3]
                if ((len(lat) > 3) and (lat[-1].isalpha())):
                    lat = lat[-3]
                if ((isFloat(long)) and (isFloat(lat))):
                    st.text(str(long) + " " + str(lat))
                    lst.append((long, lat))
                curr_left, curr_comma, curr_right = -1, -1, -1
            else:
                curr_left, curr_comma = -1, -1
    if (curr_comma > curr_left): #Check final
        long = s[curr_left + 1: curr_comma]
        lat = s[curr_comma + 2: len(s)]
        if ((len(long) > 3) and (long[-1].isalpha())):
            long = long[-3]
        if ((len(lat) > 3) and (lat[-1].isalpha())):
            lat = lat[-3]
        if ((isFloat(long)) and (isFloat(lat))):
            st.text(str(long) + " " + str(lat))
            lst.append((long, lat))
    return lst





base_url = "https://test.api.amadeus.com/v1/"


openai.api_key = st.secrets['openai_key']
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
st.session_state.authenticated = False
url = "https://test.api.amadeus.com/v1/security/oauth2/token"
data = {
    "grant_type": "client_credentials",
    "client_id": st.secrets["amadeus_key"],
    "client_secret": st.secrets["amadeus_secret"]
}

response = requests.post(url, data=data)
access_token = response.json()["access_token"]

headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}


db = firebase.database()
st.session_state.db = db
storage = firebase.storage()

st.set_page_config(page_title="PassionPassport", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)
# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)



# Authentication
authenticate = st.sidebar.selectbox('Login/Signup', ['Login', 'Signup'])


if authenticate == 'Signup':
    email = st.sidebar.text_input('Enter your email address')
    password = st.sidebar.text_input('Enter your password', type = 'password')
    name = st.sidebar.text_input('Enter your Name')
    place = st.sidebar.text_input('Enter your Location')
    handle = st.sidebar.text_input('Please input your name', value = " ")
    submit = st.sidebar.button('Sign Up')


    if submit :
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is successfully made')
       
        #Signing the user and create a user variable
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        db.child(user['localId']).child("Location").set(place)
        st.title("Hi, " + handle)
        st.info('Login successfully')




if authenticate == 'Login' :
    email = st.sidebar.text_input('Enter your email address')
    password = st.sidebar.text_input('Enter your password', type = 'password')
    submit = st.sidebar.button('Sign Up')
    openai.api_key = st.secrets['openai_key']
    st.subheader("Not sure where to travel? Plan an itinerary with us today!")
    #st.subheader("AI Assistant : Streamlit + OpenAI: `stream` *argument*")
    people_array = ""
    opp_input = st.text_input("Your friend: ",placeholder = "Friends suggestion")
    date = st.date_input("Departure Date")
    adults = st.number_input("Number of adults ")
    for i in range(0, int(adults)) :
        user_input = st.text_area("Person " + str(i) ,placeholder = "Your suggestion", key="input" + str(i))
        people_array += "People " + str(i) + " likes to " + user_input + "."
        chat_gpt = people_array + "Suggest 1 city according to these people in the format 'Bangkok'. City only "
    pressed = st.button('Submit')
        
    res_box = st.empty()
    if pressed :
        completions = openai.ChatCompletion.create(model="gpt-4", messages=[
                            {"role": "assistant",
                            "content": chat_gpt,
                            }],
                            temperature=0.5,
                            max_tokens=1000,
                            frequency_penalty=0.0,)
        
        result = completions.choices[0].message.content
        array = result.split(", ")
        res_box.write(result)
        for answer in array :
            data = requests.get("https://test.api.amadeus.com/v1/reference-data/locations/cities?keyword=" + answer, headers=headers)
            
            res = (data.json()['data'][0])
            dataTwo = requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=SYD&destinationLocationCode=" + res['iataCode'] +"&departureDate=" + str(date) + "&adults=" + str(int(adults)) + "&currencyCode=SGD&max=2", headers=headers)
            dataThree = requests.get("https://test.api.amadeus.com/v2/duty-of-care/diseases/covid19-area-report?countryCode=" + res['address']['countryCode'], headers=headers)

            resTwo = dataTwo.json()['data']
            st.session_state.flight = resTwo
            for ansTwo in resTwo :
                st.text("SGD " + ansTwo['price']['total'])
            secondPrompt = "Plan me an itinerary of " + answer + "to do " + user_input +"and" + opp_input +". Limit to 50 words each day for 5 days"
            completions = openai.ChatCompletion.create(model="gpt-4", messages=[
                            {"role": "assistant", 
                            "content": secondPrompt,
                            }],
                            temperature=0.2,
                            max_tokens=1000,
                            frequency_penalty=0.0,)
            secondResult = completions.choices[0].message.content
            st.text(secondResult)
            st.session_state.itin = secondResult
            thirdResult = ''
            response2 = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                            {"role": "assistant", 
                            "content": "Extract the places' longitude and latitude from this intinerary:" + secondResult + " in the strict number format without degree '(longitude, latitude)'",
                            }],
                temperature=0,
                max_tokens=64,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            thirdResult = response2.choices[0].message.content
            thirdArray = find_long_and_lat(thirdResult)
            mapData = []
            for long, lat in thirdArray:
                if ((isFloat(long)) and (isFloat(lat))):
                    
                    st.text("Longtitude: " + long + ", Latitude: " + lat)
                    mama = requests.get("https://test.api.amadeus.com/v1/shopping/activities?longitude=" + long + "&latitude=" + lat + "&radius=100", headers=headers)
                    i = 0
                    for ans in mama.json()['data'] :
                        i += 1
                        if i == 5 :
                            break
                        st.text(ans['name'])
                        if len(ans['pictures']) != 0:
                            st.image(ans['pictures'][0])
                        if 'shortDescription' in ans:
                            components.html(ans['shortDescription'])
                        object = {
                                'name': ans['name'],
                                'latitude': lat,
                                'longitude': long,
                                'safe': str(dataThree.json()['data']['summary']['text']),
                                'bookingLink': ans['bookingLink'],
                                'price': ans['price']['amount']
                        }
                        if object not in mapData :
                            mapData.append(object)

            st.header("Analysis")

            # Convert latitude and longitude columns to numeric format
            dataMap = pd.DataFrame(mapData)
            dataMap['latitude'] = pd.to_numeric(dataMap['latitude'])
            dataMap['longitude'] = pd.to_numeric(dataMap['longitude'])
            
            st.write(dataMap)
            st.session_state.mapData = mapData
            
       


    if submit :
        user = auth.sign_in_with_email_and_password(email, password)
        bio = st.radio('Jump to', ['Home', 'Meet Up'])
        username = db.child(user['localId']).child("Handle").get()
        st.session_state.name = username
        st.session_state.user = user
        if user is not None :
            st.session_state.authenticated = True
        if bio == 'Home' :
            st.title("Home")
           


        else :    
            st.title("Welcome")    


             


