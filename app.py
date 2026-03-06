import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. Force the page to use the full width of the phone screen
st.set_page_config(page_title="Pro Angler GPS", layout="wide", initial_sidebar_state="collapsed")

# 2. Add some "App-like" styling with CSS
st.markdown("""
    <style>
    .main > div { padding: 0px; }
    iframe { width: 100% !important; height: 80vh !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("📍 Drum Locator")

# 3. Create a Map with Satellite Imagery (Looks more like a pro app)
# We use Esri World Imagery for that "Google Earth" look
m = folium.Map(
    location=[38.394412, -76.490068], 
    zoom_start=15,
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri'
)

# 4. Define your spots with custom "Fish" icons
spots = [
    {"loc": [38.391448, -76.489086], "name": "Deep Hole", "fish": "Fucking Drum"},
    {"loc": [38.390118, -76.485986], "name": "Pier", "fish": "Perch"}
]

for spot in spots:
    folium.Marker(
        location=spot["loc"],
        popup=spot["name"],
        icon=folium.Icon(color='red', icon='fish', prefix='fa')
    ).add_to(m)

# 5. Display the map
st_folium(m, use_container_width=True)

# 6. Add a "Log Visit" button at the bottom
if st.button("➕ Log New Spot at Current GPS"):
    st.write("Feature coming soon: Saving to Database!")