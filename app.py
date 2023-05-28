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

base_url = "https://test.api.amadeus.com/v1/"


openai.api_key = st.secrets['openai_key']
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

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

def extract_numbers(s):
    result = re.search('\((.*?),\s*(.*?)\)', s)
    if result:
        first_number = float(result.group(1))
        second_number = float(result.group(2))
        return first_number, second_number
    else:
        return None, None
    
# String will look something like "x = (2.342,3.124),y = (5.2443,1.4536)"
def find_long_and_lat(s):
    # Split by the first parenthesis, so it looks something like this
    # [x = , 2.342,3.124)y = , 5.2443,1.4536)]
    lst = []
    lst1 = s.split("(")
    for i in range (1, len(lst1)):
        # Split by comma, so it looks something like this
        # [2.342, 3.124)y =], then take the first element for long
        lst2 = lst1[i].split(",")
        if len(lst2) == 2:
            currLong = lst2[0]
            # If got the degree, need remove
            if (currLong[-1].isalpha()):
                currLong = currLong[:-3]
            # Split by second parenthesis for the second element, so it looks like
            # [3.124, y =], then take the first element for lat
            currLat = lst2[1].split(")")[0]
            # If got the degree, need remove
            if (currLat[-1].isalpha()):
                currLat = currLat[:-3]
            lst.append((currLong, currLat))
    return lst

db = firebase.database()
storage = firebase.storage()


st.sidebar.title("Work App")


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
        db.child(user['localId']).child("Friends").set(["SAs"])
        st.title("Hi, " + handle)
        st.info('Login successfully')




if authenticate == 'Login' :
    email = st.sidebar.text_input('Enter your email address')
    password = st.sidebar.text_input('Enter your password', type = 'password')
    submit = st.sidebar.button('Sign Up')
    openai.api_key = st.secrets['openai_key']


    st.subheader("AI Assistant : Streamlit + OpenAI: `stream` *argument*")

    people_array = ""
    opp_input = st.text_input("Your friend: ",placeholder = "Friends suggestion")
    date = st.date_input("Departure Date")
    adults = st.number_input("Number of adults ")
    for i in range(0, int(adults)) :
        user_input = st.text_input("You: ",placeholder = "Your suggestion", key="input" + str(i))
        people_array += "People " + str(i) + " likes to " + user_input + "."
    chat_gpt = people_array + "Suggest 2 cities according to the people's hobbies in the format 'Bangkok, Jakarta, Singapore, Hanoi, Nagoya'"
    pressed = st.button('Submit')
    res_box = st.empty()
    if pressed :
        completions = openai.ChatCompletion.create(model="gpt-4", messages=[
                                          {"role": "assistant", 
                                           "content": chat_gpt,
                                           }],
                                          temperature=0.5,
                                          max_tokens=100,
                                          frequency_penalty=0.0,)
        result = completions.choices[0].message.content
        array = result.split(", ")
        res_box.write(result)
        for answer in array :
            data = requests.get("https://test.api.amadeus.com/v1/reference-data/locations/cities?keyword=" + answer, headers=headers)

            res = (data.json()['data'][0])
            dataTwo = requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=SYD&destinationLocationCode=" + res['iataCode'] +"&departureDate=2023-11-01&adults=" + str(int(adults)) + "&currencyCode=SGD&max=2", headers=headers)
            st.text(dataTwo.json())
            resTwo = dataTwo.json()['data']
            for ansTwo in resTwo :
                st.text("SGD " + ansTwo['price']['total'])
            secondPrompt = "Plan me an itinerary of " + answer + "to do " + user_input +"and" + opp_input
            completions = openai.ChatCompletion.create(model="gpt-4", messages=[
                            {"role": "assistant", 
                            "content": secondPrompt,
                            }],
                            temperature=0.2,
                            max_tokens=1000,
                            frequency_penalty=0.0,)
            secondResult = completions.choices[0].message.content
            st.text(secondResult)
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
            st.text(thirdResult)
            thirdArray = find_long_and_lat(thirdResult)
            for loc in thirdArray:
                long, lat = loc[0], loc[1]
                if ((long.isnumeric()) and (lat.isnumeric())):
                    st.text("Longtitude: " + long + ", Latitude: " + lat)
                    mama = requests.get("https://test.api.amadeus.com/v1/shopping/activities?longitude=" + long + "&latitude=" + lat + "&radius=100", headers=headers)
                    for ans in mama.json()['data'] :
                        st.text(ans['name'])
                        st.image(ans['pictures'][0])
                        if 'shortDescription' in ans:
                            components.html(ans['shortDescription'])
       
    if submit :
        user = auth.sign_in_with_email_and_password(email, password)
        bio = st.radio('Jump to', ['Home', 'Meet Up'])
        if bio == 'Home' :
            st.title("Home")
           











        else :    
            st.title("Meet up")    
            all_friends = db.child(user['localId']).child("Friends").get()
            if all_friends.val() is not None:    
                res= []
                for friend in reversed(all_friends.each()):
                        ans = friend.val()["Handle"]
                        res.append(ans)
                all = st.selectbox("Colleague ", res)


            else :
                st.text("Add your colleague")


             


