import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from os import path
from menu import menu


# Set up the page layout to use the full width of the web page
st.set_page_config(page_title="Extreme Poverty", page_icon="📈", layout="wide")

st.markdown("# Extreme Poverty")
st.sidebar.header("Extreme Poverty")
st.write("""
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)""")


@st.cache_data
def get_data():
    """        """
    URL = 'data/poverty.csv'
    df = pd.read_csv(URL)
    df.rename(columns={'$2.15 a day - Share of population in poverty':'poverty'},
              inplace=True)
    return df.set_index("Entity")


try:
    df = get_data()
    data = df.loc[:, ['Year', 'poverty']]
    country_options = data.index.unique()

    countries = st.multiselect("Choose countries", country_options, ["China", "United States"])
    if not countries:
        st.error("Please select at least one country.")
    else:
        # Filter data for a specific country, for example "United States"
        country_data = {}

        # Loop through the selected countries and extract the data.
        for country in countries:
            country_data[country] = data.loc[country]

        fig = plt.figure()
        ax = fig.add_subplot()

        # Create a line plot for each country.
        for country, data in country_data.items():
            ax.plot(data['Year'], data['poverty'], label=country)

        # Create a line chart
        ax.set_title('Poverty')
        ax.set_xlabel('Year')
        ax.set_ylabel('Share of Population')

        # Display the chart
        st.pyplot(fig)

except ValueError:
    st.write('Oops')

menu()
