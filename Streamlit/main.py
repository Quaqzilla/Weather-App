import streamlit as st
import requests

API_KEY = "3f6afd6c89a3475eb0c175627251506"

def weather(city):
    base_url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

st.markdown("<h1 style = 'text-align :center;'>Weather Application 🌤</h1>", unsafe_allow_html=True)
#Input area
weather_input = st.chat_input("Enter City Name")

#Display area
weather_output = st.container(height=300)

#Weather processing
if weather_input:
    weather_info = weather(weather_input)
    if weather_info:
        location = weather_info['location']['name']
        icon_url = "https:" + weather_info['current']['condition']['icon']
        Condition = weather_info['current']['condition']['text']
        temperature = weather_info['current']['temp_c']

        # Added a placeholder image for the weather icon
        weather_output.markdown(f"""
        <div style='display: flex; flex-direction: row; gap: 10px; align-items: center; justify-content: space-evenly; margin-top: 25px'>
        <div><img src={icon_url} alt='weather-img' width='80'></div>

        <div style = '
        display: flex; 
        flex-direction: column;
        gap: 5px;
        background-color: rgb(51, 50, 50);
        padding: 10px 20px;
        border-radius: 15px;
        '>
        <h1>{location}</h1>
        <h6>{Condition}</h6>
        <h4>{temperature}C</h4>
        </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        weather_output.error('City not found try again')


