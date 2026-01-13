import requests
from settings.settings import settings
import streamlit as st

api_astronomy_key = settings.api_astro_key
url = f"https://api.nasa.gov/planetary/apod?api_key={api_astronomy_key}"

response1 = requests.get(url=url)
data = response1.json()

title = data["title"]
explanation = data["explanation"]
image_data = data["url"]

image_filepath = "img.png"
response2 = requests.get(image_data)
with open(image_filepath,"wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)

