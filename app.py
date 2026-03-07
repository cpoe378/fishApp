import streamlit as st
import folium
from streamlit_folium import st_folium
import base64
from pathlib import Path

# 1. Page Config (Mobile first)
st.set_page_config(page_title="Sawpit Fishing App", layout="wide", initial_sidebar_state="collapsed")

# 2. LOGIC: Convert the logo into an HTML-readable format
# This function loads the actual image_0.png file and encodes it
def get_image_base64(image_path):
    img_bytes = Path(image_path).read_bytes()
    encoded_img = base64.b64encode(img_bytes).decode('utf-8')
    return f"data:image/png;base64,{encoded_img}"

# Try to load the logo. If it fails, we fall back to a standard title.
try:
    # IMPORTANT: Ensure 'image_0.png' is in the exact same folder as this script.
    logo_file_path = "image_0.png" 
    logo_base64 = get_image_base64(logo_file_path)

    # 3. Create a custom Header with HTML and CSS
    # We create a flexbox to align the logo and the text on the same line.
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: start; gap: 20px; padding-bottom: 20px;">
            <img src="{logo_base64}" width="80" style="border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.3);">
            <div>
                <h1 style="margin: 0; font-size: 2.8rem; color: #1E1E1E;">Sawpit Fishing</h1>
                <p style="margin: 0; font-size: 1.1rem; color: #555;">Private Spots Network</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

except FileNotFoundError:
    # Fallback if the logo is missing.
    st.title("Sawpit Fishing App (Logo Missing)")
    st.error(f"Error: Could not find '{logo_file_path}'. Make sure it's in the same folder as app.py.")

# 4. (Optional) Password check if needed...

# 5. The Map Logic (The 'Honey Holes')
m = folium.Map(
    location=[29.7604, -95.3698], # Centered on a sample bay
    zoom_start=15,
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri World Imagery'
)

# Custom markers for your club
folium.Marker(
    [29.7604, -95.3698], 
    popup="The Sawpit Hole (Bass)", 
    icon=folium.Icon(color='darkblue', icon='fish', prefix='fa')
).add_to(m)

st_folium(m, use_container_width=True, height=600)



