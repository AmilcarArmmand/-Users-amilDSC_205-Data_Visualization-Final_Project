import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from menu import menu


st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)

st.markdown("[![Click me](./app/static/China_70_years_Shareable-1.jpg)](./app/static/China_70_years_Shareable-1.jpg)")
st.markdown("[![Click me](./app/static/gross_production.png)](./app/static/gross_production.png)")
st.markdown("[![Click me](./app/static/patent_grants.jpg)](./app/static/patent_grants.jpg)")
st.markdown("[![Click me](./app/static/new_three_industies.jpg)](./app/static/new_three_industies.jpg)")


menu()
