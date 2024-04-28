# Displaying tables and data in dashboard
import pandas as pd
import streamlit as st
from os import path
from menu import menu


# Set up the page layout to use the full width of the web page
st.set_page_config(page_title="HSP", page_icon="📈", layout="wide")

st.markdown("# High Speed Rail")
st.sidebar.header(" High Speed Rail")


tab1, tab2, tab3 = st.tabs(["📈 Chart", "📈 Chart", "🗃 Data"])

@st.cache_data
def get_data(URL):
    """Get data"""
    return pd.read_csv(URL)


URL_hsr = 'data/HSR.csv'
URL_passenger = 'data/railways-passengers-carried-passenger-km.csv'

try:
    data = get_data(URL_hsr)
    df_rail = data.rename(columns={'Unnamed: 0': 'year',
                             'Length\u00a0of\u00a0High\u00a0Speed\u00a0Railway\u00a0in\u00a0Operation\u00a0(km)': 'high_speed_rail_length',
                             'As\u00a0Percentage\u00a0of\u00a0Total\u00a0Railway\u00a0Length\u00a0(%)': 'high_speed_rail_percentage',
                             'Passenger\u00a0Traffic\u00a0(10,000\u00a0persons)': 'passenger_traffic',
                             'As\u00a0Percentage\u00a0of\u00a0Total\u00a0Railway\u00a0Traffic\u00a0(%)': 'percent_total_rail_traffic',
                             'Passenger-Kilometers\u00a0(100\u00a0million\u00a0person-km)': 'passengers_per_km',
                             'As\u00a0Percentage\u00a0of\u00a0Total\u00a0Railway\u00a0Passenger-Kilometers\u00a0(%)': 'percent_total_railway_passPerKm'})

    rail_data = df_rail.set_index('year')

    df_passenger = get_data(URL_passenger)
    passenger_data = df_passenger.index.unique()

    with st.container():
        with tab1:
            st.subheader("Total km of rail.")
            st.bar_chart(rail_data)

        with tab2:
            st.subheader("2")
            st.line_chart(passenger_data)

    tab3.subheader("Data")
    tab3.write(passenger_data)

    
except TypeError:
    st.error('This is an error', icon="🚨")
    st.write('break point')


st.subheader('st.dataframe, width = 600px, height = 200px')
st.dataframe(passenger_data, width=600, height=200)

st.subheader('st.table shows the contents of entire DataFrame')
st.table(data=passenger_data)


menu()
