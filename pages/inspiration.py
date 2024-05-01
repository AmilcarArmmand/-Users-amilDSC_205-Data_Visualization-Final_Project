import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from menu import menu
from pathlib import Path

st.set_page_config(page_title="Inspiration", page_icon="📊")

st.markdown("# ")
st.sidebar.header("Inspiration")

menu()

with st.container():
    st.subheader('Timeline: 1949 - 2020')
    st.image('https://github.com/AmilcarArmmand/DSC_205-Data_Visualization-Final_Project/blob/4a4645fac0c30a9675b2f06acbde3b89ffd1946c/static/China_70_years_Shareable-1.jpg?raw=true', caption='China_70_years.png')
    


