# lifehack-2023
Theme: Re-defining the Post-Pandemic Travelling Landscape

For LifeHack 2023, we have chosen the theme of Re-defining the Post-Pandemic Traveling Landscape, which requires us to ideate an application to reintroduce travel to post-COVID travellers.

To address this problem statement, we have come up with *PassionPassport*, a web-application that recommends travel itineraries based on one's hobbies.
    
**Inspiration**

During COVID-19, most of us had to experience lockdowns within our own countries, and were not allowed to travel abroad for 1-2 years. When the borders were re-opened, many people were excited to travel once again - however the transition was still hard as they may have forgotten how it felt like to travel, including the planning process. In addition, with the recent popularity of ChatGPT, we thus planned to build a web application that uses ChatGPT to generate a travel itinerary for users, based on their hobbies as inputs, especially for those who do not know where to travel after so long. 

**What it does**

Users can key in an input (e.g a hobby - swimming) for himself, along with another friend's hobby into our web application. Based on the inputs, ChatGPT will then recommend a country as well as a few locations to travel to. A detailed itinerary, including descriptions and images of these key locations, will then be generated to better inform the user of these locations to hype them up for the trip.

**How we built it**

We used Streamlit, HTML and CSS as our front-end for our web application, and utilised the OpenAI API as well as Firebase for our back-end. BeautifulSoup4 was also used to scrape travel  information from online websites.

**What makes our solution stand out**

Unlike other solutions that provides limited input choices, our usage of the OpenAI API allows us to customise different itineraries based on different categories of inputs, including hobbies, cost, and even personality traits as examples.

**Some key challenges we faced**

A key issue that we've faced is the transition from our typical skillset of HTML/CSS/Javascript to Streamlit, as we wanted to fully utilise the OpenAI API for easier facilitation of the back-end. In addition, we were also new to utilising Firebase to store user data for our login system, to track user history of previous queries using our app.

**Built with**

`Firebase` `Python` `Streamlit` `HTML` `CSS` `OpenAI API` `BeautifulSoup4`

**Links**
Devpost: https://devpost.com/software/t-p-jc-passionpassport
Video Demo: https://lnkd.in/gEHWUiKN
Pitch Deck: https://lnkd.in/ggFu3ecD
