import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from menu import menu


st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")




st.markdown("""Grain output 700M tons is 1.2 times US production.\n
•  Power generation of 9.2T kw is 2.3 times more than the U.S.\n
•  China produces 19 times more steel than the U.S.\n
•  China produces 20 times more cement than the U.S. \n
•  Ship building produces 70 times more tonnage a year \n
•  China has the 2nd largest merchant fleet (Greece is #1) \n
•  Transportation efficiency of rail, airport, and ports. \n
•  Installed solar power is twice all other countries combined \n
•  The Wind power generates more power than the next 7 countries combined \n
•  In 2020, China graduated 3.57M STEM workers / the U.S. graduated 820k(about 1/3 foreign born) \n
•  Dominated the international Olympiads in biology, chemistry, physics, math, and informatics.""")

menu()
