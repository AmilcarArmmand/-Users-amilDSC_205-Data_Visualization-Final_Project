import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from menu import menu


# Set up the page layout to use the full width of the web page
st.set_page_config(page_title="Life Expectancy", page_icon="📈", layout="wide")

st.markdown("# Life Expectancy From Birth")
st.sidebar.header("Life Expectancy")
st.write("""
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)""")

menu()

@st.cache_data
def get_data():
    """Convert csv to dataframe"""
    URL = 'data/life-expectancy.csv'
    df = pd.read_csv(URL)
    df.rename(columns={'Period life expectancy at birth - Sex: all - Age: 0': 'life_expectancy'},
              inplace=True)
    return df

st.divider()
try:
    df = get_data()
    data = df.set_index('Entity')
    
    country_options = data.index.unique()
    test = data.reset_index()

    ## widget integration
    countries = st.multiselect("Select countries to compare:",
                               country_options, ["China", "United States"])
    
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
        ax.set_title('Life Expectancy')
        ax.set_xlabel('Year')
        ax.set_ylabel('Age (years)')
        ax.legend()
        
        ax.axhline(0, color="grey", linewidth=1, linestyle='--')
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        
        st.divider()
        # Display the chart
        st.pyplot(fig)

except ValueError:
    st.write('Oops')


