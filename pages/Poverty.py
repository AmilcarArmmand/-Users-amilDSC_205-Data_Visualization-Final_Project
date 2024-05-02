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

menu()

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

    countries = st.multiselect("Choose countries to compare them:", country_options, ["China", "United States"])
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
        ax.set_title('Extreme Poverty')
        ax.set_xlabel('Year')
        ax.set_ylabel('Share of Population')

        ax.legend()
        
        ax.axhline(0, color="grey", linewidth=1, linestyle='--')
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        # Display the chart
        st.pyplot(fig)

except ValueError:
    st.write('Oops')



with st.expander("See explanation"):
    st.write("""
    What is extreme poverty?

    It is living on less than \$2 a day (or actually less than $2.15).  It means having too little money to meet the basic needs that most of us take for granted, such as food, water, electricity and basic healthcare.

    """)
    st.link_button("Share of population living in extreme poverty, 2023", "https://ourworldindata.org/explorers/poverty-explorer?facet=none&Indicator=Share+in+poverty&Poverty+line=%242.15+per+day%3A+International+Poverty+Line&Household+survey+data+type=Show+data+from+both+income+and+consumption+surveys&Show+breaks+between+less+comparable+surveys=false&country=BGD~BOL~KEN~MOZ~NGA~ZMB")
