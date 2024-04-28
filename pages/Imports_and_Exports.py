import streamlit as st
import pandas as pd
import os
import folium
from streamlit_folium import folium_static
import numpy as np
from menu import menu


# Set the layout to wide
st.set_page_config(layout="wide")

# Function to load data from CSV
def load_data(file_path):
    return pd.read_csv(file_path, encoding='ISO-8859-1')

# File paths for the datasets
data_1992_path = os.path.join('data', '1992_import_export.csv')
data_2021_path = os.path.join('data', '2021_import_export.csv')
country_locations_path = os.path.join('data', 'country_locations.csv')

# Load the datasets
data_1992 = load_data(data_1992_path)
data_2021 = load_data(data_2021_path)
country_locations = load_data(country_locations_path)

# Streamlit app title
st.title('Modernization of China: A Trade Perspective')

# Streamlit sidebar for user input
col1, col2 = st.columns((1, 7))

with col1:
    year = st.radio('Select the Year', [1992, 2021])
    trade_flow = st.radio('Select Trade Flow', ['Import', 'Export'])

# Filter data based on the selected year
filtered_data = load_data(data_1992_path if year == 1992 else data_2021_path)

# Initialize folium map
m = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB positron')

# Prepare country coordinates for mapping
country_coords = {row['name']: (row['latitude'], row['longitude']) for _, row in country_locations.iterrows()}

# Scaling function for marker sizes
def power_scale(value, power, scale):
    return (value ** power) * scale

# Calculate scaling factor
max_value = filtered_data[f'{trade_flow} (US$ Thousand)'].max()
power = 0.5  # Use square root scaling
scale = 100 / (max_value ** power)

# Plot markers on the map
for index, row in filtered_data.iterrows():
    lat_lon = country_coords.get(row['Partner Name'], (None, None))
    if lat_lon != (None, None):
        trade_value = row[f'{trade_flow} (US$ Thousand)']
        partner_name = row['Partner Name']
        radius = power_scale(trade_value, power, scale)
        radius = max(radius, 1)  # Ensure markers are visible

        # Create CircleMarker for each country
        folium.CircleMarker(
            location=lat_lon,
            radius=radius,
            popup=f"<strong>{partner_name}</strong><br>{trade_flow}: ${trade_value:,.0f},000",
            color='green' if trade_flow == 'Export' else 'blue',
            fill=True,
            fill_color='green' if trade_flow == 'Export' else 'blue'
        ).add_to(m)

# Display map in Streamlit app
with col2:
    folium_static(m)

menu()
