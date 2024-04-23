# Displaying tables and data in dashboard
import pandas as pd
import streamlit as st
from os import path


# Set up the page layout to use the full width of the web page
st.set_page_config(page_title="HSP", page_icon="📈", layout="wide")

st.markdown("# High Speed Rail")
st.sidebar.header("High Speed Rail")


@st.cache_data
def get_data(URL):
    """Get data"""
    return pd.read_csv(URL)


URL1 = 'data/HSR.csv'
URL2 = 'data/railways-passengers-carried-passenger-km.csv'


try:
    df_rail = get_data(URL1)
    df_rider = get_data(URL2)

    
except TypeError:
    st.write('break point')

st.subheader('st.dataframe, width = 600px, height = 200px')
st.dataframe(df_rail, width=600, height=200)

st.subheader('st.table shows the contents of entire DataFrame')
st.table(data=df_rail)

st.subheader('st.dataframe, width = 600px, height = 200px')
st.dataframe(df_rider, width=600, height=200)

st.subheader('st.table shows the contents of entire DataFrame')
st.table(data=df_rider)
