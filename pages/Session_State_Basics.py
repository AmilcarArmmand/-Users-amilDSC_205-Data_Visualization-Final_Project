import streamlit as st
import pandas as pd


st.title("Session State Testing")

"st.session_state_object:", st.session_state

## widget integration
number = st.slider("A number", 1, 10, key="slider")

st.write(st.session_state)

col1, buff, col2 = st.columns([1,0.5,3])

option_names = ["a", "b", "c"]

next = st.button("Next option")

if next:
    if st.session_state["radio_option"] == 'a':
        st.session_state.radio_option = 'b'
    elif st.session_state["radio_option"] == 'b':
        st.session_state.radio_option = 'c'
    else:
        st.session_state.radio_option = 'a'

option = col1.radio("Pick an option", option_names, key="radio_option")
st.session_state

if option == 'a':
    col2.write("You picked 'a' :smile:")
elif option == 'b':
    col2.write("You picked 'b' :heart:")
else:
    col2.write("You picked 'c' :rocket:")


def miles_to_km():
    st.session_state.km = st.session_state.miles*(1.609344)


def km_to_miles():
    st.session_state.miles = st.session_state.km/(1.609344)
    
    
with col1:
    miles = st.number_input("Miles:", key="miles",
                            on_change = miles_to_km)

with col2:
    kilometers = st.number_input("kilometers:", key="km",
                                 on_change = km_to_miles)


@st.cache_data(persist=True)
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up
    data = pd.read_csv(url)
    return data


@st.cache_data
def get_api_data():
    data = api.get(...)
    st.success("Fetched data from API!")  # 👈 Show a success message
    return data


@st.cache_data
def show_data():
    st.header("Data analysis")
    data = api.get(...)
    st.success("Fetched data from API!")
    st.write("Here is a plot of the data:")
    st.line_chart(data)
    st.write("And here is the raw data:")
    st.dataframe(data)


@st.cache_data(experimental_allow_widgets=True)  # 👈 Set the parameter
def get_data():
    num_rows = st.slider("Number of rows to get")  # 👈 Add a slider
    data = api.get(..., num_rows)
    return data


URL = 'data/energy-consumption-by-source-and-country.csv'
try:
    df = fetch_and_clean_data(URL)
    st.dataframe(df)

except TypeError:
    st.write('break point')
