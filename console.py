import streamlit as st
import numpy as np
from menu import menu


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': "## DSC-205 Final Project by Conner Broderick and Amilcar Armmand. This is an *extremely* cool app!"
    }
)

st.write("# The Modernization of China :cn:")

st.sidebar.success("Select a category below.")

st.markdown(
    """
    **👈 Select a page from the sidebar**
""")
st.divider()

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.subheader("The Rapid Growth of China")
    st.write("Since the establishment of the PRC in 1949, China has transformed from an impoverished agrarian society into a formidable global economic power. This transition was marked by significant events, including Mao Zedong's industrialization efforts during the First 5-Year Plan, and later, the opening of Special Economic Zones in the 1980s which encouraged foreign investment and technological advancement. China's economic reforms propelled rapid industrial growth, dramatically increasing agricultural and manufacturing productivity. Joining key international bodies and initiatives such as the UN and WTO further integrated China into the global economy. In the 21st century, China continued to expand its global influence through initiatives like the Belt and Road and Made in China 2025, reinforcing its position as a central hub in global trade and high-tech manufacturing. Despite challenges like an aging population and trade disputes, China's economic growth trajectory has remained remarkably resilient.")
    st.write("Source: [70 Years of China's Economic Growth](https://www.visualcapitalist.com/china-economic-growth-history/)")
with col2:
    st.subheader("Rise in Trade")
    st.write("China's transformation into a global economic powerhouse is a result of ambitious reforms starting in the 1970s, leading to its emergence as the world's manufacturing center and a leading exporter by joining international trade frameworks like GATT and the WTO. These reforms, along with China's integration into global value chains and technological advances, have seen it rapidly expand its exports, demonstrating resilience against trade tensions and the pandemic. Yet, the future may bring a shift as China's economy matures towards domestic consumption, labor costs rise, and technological changes prompt manufacturing reshoring, potentially marking a peak in its export-led growth in the face of global geopolitical changes and the push for sustainability.")
    st.write("Source: [UNCTAD - China's Rise as a Trade Titan](https://unctad.org/news/china-rise-trade-titan)")
with col3:
    st.subheader("High Speed Rails")

st.divider()

footer = st.container()
footer.write("👈 Select a page from the sidebar")
# Code to create the link button
st.link_button("Go to project repo.", "https://github.com/AmilcarArmmand/DSC_205-Data_Visualization-Final_Project")

menu()
