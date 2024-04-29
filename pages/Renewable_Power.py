# Displaying tables and data in dashboard
import pandas as pd
import streamlit as st
from os import path
from menu import menu


# Set up the page layout to use the full width of the web page
st.set_page_config(page_title="Life Expectancy", page_icon="📈", layout="wide")

st.markdown("# Power Generaltion")
st.sidebar.header("Power Generation")


st.markdown("[![Click me](./app/static/renewables_1.jpg)](./app/static/renewables_1.jpg)")


menu()
