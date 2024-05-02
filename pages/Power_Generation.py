# Displaying tables and data in dashboard
import pandas as pd
import streamlit as st
from os import path
from menu import menu
import altair as alt


# Set up the page layout to use the full width of the web page
st.set_page_config(page_title="Life Expectancy", page_icon="📈", layout="wide")

st.markdown("# Power Consumption")
st.sidebar.header(" Power Consumption")

menu()

@st.cache_data
def get_data():
    """        """
    URL = 'data/energy-consumption-by-source-and-country.csv'
    df = pd.read_csv(URL)
    return df

with st.container():
    st.subheader('Timeline: 1949 - 2020')
    st.image('static/fossil-fuels-per-capita.png', caption='China_70_years.png')

data = get_data()
#data.rename(columns={
#    'Other renewables (including geothermal and biomass) - TWh':'biomass'}, inplace=True)
#data

#c = (
#   alt.Chart(data)
#   .mark_circle()
#   .encode(x="Entity", y="b", size="c", color="c", tooltip=["a", "b", "c"])
#)

#st.altair_chart(c, use_container_width=True)

    
with st.expander("See explanation"):
    st.write("""
    To ensure everyone has access to clean and safe energy, we need to understand energy consumption and its impacts around the world today and how this has changed over time.

    """)
    st.link_button("Energy", "https://ourworldindata.org/energy")
