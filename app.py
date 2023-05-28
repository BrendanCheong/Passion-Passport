import pyrebase
import streamlit as st
import asyncio
import requests
from datetime import datetime
import openai
from streamlit_pills import pills

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
    data = requests.get(base_url + "/reference-data/recommended-locations")
    st.text(data.json())

    user_input = st.text_input("You: ",placeholder = "Your suggestion", key="input")
    opp_input = st.text_input("Your friend: ",placeholder = "Friends suggestion")
    chat_gpt = "If person A loves to " + user_input + " and person B loves to " + opp_input + ". Suggest 5 cities according to the people's hobbies in the format 'Bangkok (Thailand), Jakarta (Indonesia), Singapore (Singapore), Hanoi (Vietnam), Nagoya (Japan)'"
    pressed = st.button('Submit')
    res_box = st.empty()
    if pressed :
        completions = openai.ChatCompletion.create(model="gpt-4", messages=[
                            {"role": "assistant",
                            "content": chat_gpt,
                            }],
                            temperature=0.5,
                            max_tokens=6000,
                            frequency_penalty=0.0,)
        
        result = completions.choices[0].message.content
        array = result.split(", ")
        res_box.write(result)
        for answer in array :
            st.text(answer)
            secondPrompt = "Plan me an itinerary of " + answer
            completions = openai.ChatCompletion.create(model="gpt-4", messages=[
                            {"role": "assistant", 
                            "content": secondPrompt,
                            }],
                            temperature=0.5,
                            max_tokens=6000,
                            frequency_penalty=0.0,)
            secondResult = completions.choices[0].message.content
            st.text(secondResult)
            res_box.write(secondResult)

       
    if submit :
        user = auth.sign_in_with_email_and_password(email, password)
        bio = st.radio('Jump to', ['Home', 'Meet Up'])
        if bio == 'Home' :
            st.title("Home")
            col1, col2 = st.columns(2)
            with col1:
                availability = st.text_input("When are you available")
                date = st.date_input("Availability")


                post = st.button('Submit')
            with col2 :
                all_users = db.get()
                add_friends = st.text_input("Add Colleagues")
                all_friends = db.child(user['localId']).child("Friends").get()
                res = []
                for users_handle in all_users.each() :
                    res.append(users_handle.val()["Handle"].strip() )
                confirm = st.button('Confirm')
                if confirm :
                    st.text("Confirmed")
                   
                    for name in res :
                        if str(name) == str(add_friends) :
                            st.text("found")
                            friends = {
                                'friend_name': add_friends
                            }
                            results = db.child(user['localId']).child("Friends").push(friends)
                            st.info("Success")


                else :
                    st.info("Error")
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


             


