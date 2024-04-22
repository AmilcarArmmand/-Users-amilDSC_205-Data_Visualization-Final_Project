import streamlit as st
import pandas as pd
import altair as alt
from os import path


# Set up the page layout to use the full width of the web page
st.set_page_config(page_title="Life Expectancy", page_icon="📈", layout="wide")

st.markdown("# Life Expectancy From Birth")
st.sidebar.header("Life Expectancy")
st.write("""Include periods in the lines to indicate life expectancy in a given year.
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
    #st.table(data=data)
    countries = st.multiselect("Choose countries", country_options, ["China", "United States"])
    if not countries:
        st.error("Please select at least one country.")
    else:
        # Filter data for a specific country, for example "United States"
        filtered_data = data[data.index == countries]

        # Create a line chart
        #chart = alt.Chart(filtered_data).mark_line().encode(
        #    x='Year:Q',  # Quantitative scale for Year
        #    y='life_expectancy:Q',  # Quantitative scale for life expectancy
        #    tooltip=['Year', 'life_expectancy']  # Show tooltip on hover
        #).properties(
        #    title='Life Expectancy Over the Years in the United States',
        #    width=600,
        #    height=400
        #)

        # Display the chart
        
        #data = df.loc[countries]
        #data /= 1000000.0
        #st.write("### Gross Agricultural Production ($B)", data.sort_index())

        #data = data.T.reset_index()
        #data = pd.melt(data, id_vars=["index"]).rename(columns={"index": "Year", "value": "life_expectancy"})
        #chart = (alt.Chart(data).mark_area(opacity=0.3).encode(x="Year:T",                                                               y=alt.Y("Life Expectancy ($B):Q", stack=None), color="Region:N",   ))

        #st.altair_chart(chart, use_container_width=True)
except ValueError:
    st.write('Oops')
    
