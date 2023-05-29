import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="PassionPassport - About Us", page_icon = "✈️", layout = "centered", initial_sidebar_state = "auto")
st.sidebar.title("PassionPassport")
st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

st.subheader("About Us!")

harry = Image.open("assets/harry.jpg")
brendan = Image.open("assets/brendan.jpg")
vanessa = Image.open("assets/vanessa.jpg")
ryan = Image.open("assets/ryan.jpg")

selected_options = ["Overview", "Summary", "Our Team", "References"]
selected = st.selectbox("Which section would you like to read?", options = selected_options)
st.write("Current selection:", selected)
if selected == "Overview":
    st.subheader("Overview")
    st.markdown("""
    **Overall Theme: Emergence of a Technoworld - A Post COVID-19 Experience**

    Synopsis: The COVID-19 pandemic has catalysed the digitalisation of our everyday lives, whereby buzzwords such as “Go Digital”, “Virtual World” are no longer a mere hype, but are increasingly prevalent and welcomed in today’s world. In fact, key industry players from the traditional and essential sectors, such as the aviation and education industries, have been actively seeking ways to incorporate technology into their daily operations, to effectively transform their businesses from “physically limited” to “virtually unlimited”.

    **Chosen Theme: Re-defining the Post-Pandemic Traveling Landscape**

    Problem Statement: In a post-pandemic era, traveling around the globe has emerged as the top priority in various tourists’ agenda, putting the aviation and tourism sectors under the spotlight! As such, curate an application or software that enhances tourists’ experience and/or optimises the operations of the aviation industry.
    """)

elif selected == "Summary":
    st.subheader("Summary")
    st.markdown("""
    For LifeHack 2023, we have chosen the theme of Re-defining the Post-Pandemic Traveling Landscape, which requires us to ideate an application to reintroduce travel to post-COVID travellers.

    To address this problem statement, we have come up with *PassionPassport*, a web-application that recommends travel itineraries based on one's hobbies.
    
    **Inspiration**

    During COVID-19, most of us had to experience lockdowns within our own countries, and were not allowed to travel abroad for 1-2 years. When the borders were re-opened, many people were excited to travel once again - however the transition was still hard as they may have forgotten how it felt like to travel, including the planning process.
    In addition, with the recent popularity of ChatGPT, we thus planned to build a web application that uses ChatGPT to generate a travel itinerary for users, based on their hobbies as inputs, especially for those who do not know where to travel after so long. 

    **What it does**

    Users can key in an input (e.g a hobby - swimming) for himself, along with another friend's hobby into our web application. Based on the inputs, ChatGPT will then recommend a country as well as a few locations to travel to. A detailed itinerary, including descriptions and images of these key locations, will then be generated to better inform the user of these locations to hype them up for the trip.

    **How we built it**

    We used Streamlit, HTML and CSS as our front-end for our web application, and utilised the OpenAI API as well as Firebase for our back-end.

    **What makes our solution stand out**

    Unlike other solutions that provides limited input choices, our usage of the OpenAI API allows us to customise different itineraries based on different categories of inputs, including hobbies, cost, and even personality traits as examples.

    **Some key challenges we faced**

    A key issue that we've faced is the transition from our typical skillset of HTML/CSS/Javascript to Streamlit, as we wanted to fully utilise the OpenAI API for easier facilitation of the back-end. In addition, we were also new to utilising Firebase to store user data for our login system, to track user history of previous queries using our app.

    **Built with**

    `Firebase` `Python` `Streamlit` `HTML` `CSS` `OpenAI API`

    Github repo: https://github.com/BrendanCheong/lifehack-2023 

    """)

elif selected == "Our Team":
    st.subheader("Our Team")
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(harry)
        with text_column:
            st.subheader("Harry Chang")
            st.write("*Data Science and Analytics*")
            st.markdown("""
            Role: Front-end, Branding Assets, Copywriting

            `Python` `HTML` `CSS` `Streamlit` `R` `Java` `Figma`
            """)
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(brendan)
        with text_column:
            st.subheader("Brendan Cheong")
            st.write("*Business Analytics and Economics*")
            st.markdown("""
            Role: Front-end, Back-end

            `Python` `HTML` `CSS` `Streamlit` `Javascript` `React`
            """)
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(vanessa)
        with text_column:
            st.subheader("Vanessa Mae")
            st.write("*Computer Science*")
            st.markdown("""
            Role: Back-end

            `Python` `HTML` `CSS` `Streamlit` `Javascript` `React` `Firebase`
            """)
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(ryan)
        with text_column:
            st.subheader("Ryan Tan")
            st.write("*Business Analytics*")
            st.markdown("""
            Role: Back-end

            `Python` `HTML` `CSS` `Streamlit` `Firebase`
            """)

elif selected == "References":
    st.subheader("References")
    st.markdown("""
            - Streamlit API Documentation: https://docs.streamlit.io/ 

            - OpenAI API Documentation: https://openai.com/blog/openai-api 
            """)

st.write("*Copyright © 2023 T(P)JC - Harry, Brendan, Vanessa, Ryan*") 

