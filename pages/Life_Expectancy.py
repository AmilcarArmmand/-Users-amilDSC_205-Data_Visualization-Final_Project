import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from os import path


# Set up the page layout to use the full width of the web page
st.set_page_config(page_title="Life Expectancy", page_icon="📈", layout="wide")

st.markdown("# Life Expectancy From Birth")
st.sidebar.header("Life Expectancy")
st.write("""
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)""")


@st.cache_data
def get_data():
    """        """
    URL = 'data/life-expectancy.csv'
    df = pd.read_csv(URL)
    df.rename(columns={'Period life expectancy at birth - Sex: all - Age: 0': 'life_expectancy'},
              inplace=True)
    return df.set_index("Entity")


try:
    df = get_data()
    data = df.loc[:, ['Year', 'life_expectancy']]
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
            ax.plot(data['Year'], data['life_expectancy'], label=country)

        # Create a line chart
        ax.set_title('Life')
        ax.set_xlabel('Year')
        ax.set_ylabel('Age')

        # Display the chart
        st.pyplot(fig)

except ValueError:
    st.write('Oops')
