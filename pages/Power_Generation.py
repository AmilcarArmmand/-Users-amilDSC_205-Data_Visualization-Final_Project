# Displaying tables and data in dashboard
import pandas as pd
import streamlit as st
from os import path


# Set up the page layout to use the full width of the web page
st.set_page_config(page_title="Life Expectancy", page_icon="📈", layout="wide")

st.markdown("# Power Generaltion")
st.sidebar.header("Power Generation")


@st.cache_data
def get_data():
    """        """
    URL = 'data/energy-consumption-by-source-and-country.csv'
    df = pd.read_csv(URL)
    return df


try:
    df = get_data()

except Error:
    st.write('break point')

st.subheader('st.dataframe, width = 600px, height = 200px')
st.dataframe(df, width=600, height=200)

st.subheader('st.table shows the contents of entire DataFrame')
st.table(data=df)


with st.sidebar:
    if st.button("Home"):
        st.switch_page("console.py")
    if st.button("Life Expectancy📈"):
        st.switch_page("pages/Life_Expectancy.py")
    if st.button("Growth Comparison📈"):
        st.switch_page("pages/Growth_Comparison.py")
    if st.button("High Speed Rail📈"):
        st.switch_page("pages/High_Speed_Rail.py")
    if st.button("Imports and Exports"):
        st.switch_page("pages/Imports and Exports.py")
    if st.button("Extreme Poverty"):
        st.switch_page("pages/Poverty.py")
    if st.button("Power Generation"):
        st.switch_page("pages/Power_Generation.py")
    if st.button("Renewable Power_📊"):
        st.switch_page("pages/Renewable_Power.py")
    if st.button("Agricultural Production"):
        st.switch_page("pages/Agri_Production.py")
    if st.button("Inspiration"):
        st.switch_page("pages/inspiration.py")
    if st.button("Trivia 🗃"):
        st.switch_page("pages/media.py")
    if st.button("Photo Gallery"):
        st.switch_page("pages/Session_State_Basics.py")
    
