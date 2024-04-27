import streamlit as st
import numpy as np


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': "## DSC-205 Final Project by Conner Broderick and Amilcar Armmand. This is an *extremely* cool app!"
    }
)

st.write("# The Modernization of China :cn:")

st.sidebar.success("Select a  above.")

st.markdown(
    """
    **👈 Select a page from the sidebar**
    
"""
)
st.divider()

#with st.sidebar:
   # if st.button("Home"):
    #    st.switch_page("console.py")
#    if st.button("Life Expectancy"):
#        st.switch_page("pages/Life_Expectancy.py")
#    if st.button("Growth Comparison"):
#        st.switch_page("pages/Growth_Comparison.py")
#    if st.button("High Speed Rail"):
#        st.switch_page("pages/High_Speed_Rail.py")
#    if st.button("Imports and Exports"):
#        st.switch_page("pages/Imports and Exports.py")
#    if st.button("Extreme Poverty"):
#        st.switch_page("pages/Poverty.py")
#    if st.button("Power Generation"):
#        st.switch_page("pages/Power_Generation.py")
#    if st.button("Renewable Power"):
#        st.switch_page("pages/Renewable_Power.py")
#    if st.button("Agr"):
#        st.switch_page("pages/3_📊_DataFrame.py")
#    if st.button("Inspiration"):
#        st.switch_page("pages/3_📊_DataFrame.py")
#    if st.button("Trivia"):
#        st.switch_page("pages/3_📊_DataFrame.py")
#    if st.button("Photo Gallery"):
#        st.switch_page("pages/Session_State_Basics.py")

with st.container():
    tab1, tab2, tab3, tab4 = st.tabs(["Menu items", "📈 Chart", "📈 Chart", "🗃 Data"])

    with tab1:
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            if st.button("Home"):
                st.switch_page("console.py")
            if st.button("Life_Expectancy"):
                st.switch_page("pages/Life_Expectancy.py")
            if st.button("Growth_Comparison"):
                st.switch_page("pages/Growth_Comparison.py")
            if st.button("High_Speed_Rail"):
                st.switch_page("pages/High_Speed_Rail.py")
            if st.button("Imports_and_Exports"):
                st.switch_page("pages/Imports and Exports.py")
            if st.button("Extreme_Poverty"):
                st.switch_page("pages/Poverty.py")
        with col2:
            if st.button("Power_Generation"):
                st.switch_page("pages/Power_Generation.py")
            if st.button("Renewable_Power"):
                st.switch_page("pages/Renewable_Power.py")
            if st.button("Agro"):
                st.switch_page("pages/3_📊_DataFrame.py")
            if st.button("Inspiration"):
                st.switch_page("pages/3_📊_DataFrame.py")
            if st.button("Trivia"):
                st.switch_page("pages/3_📊_DataFrame.py")
            if st.button("Photo_Gallery"):
                st.switch_page("pages/Session_State_Basics.py")
        with tab2:
            with st.container():
                st.header("tab2")
                st.write("This is inside the container")

                # You can call any Streamlit command, including custom components:
                st.bar_chart(np.random.randn(50, 3))

        with tab3:
            with st.container():
                st.header("tab3")
                st.write("bar charts with year slider")

        with tab4:
            with st.container():
                st.header("tab4")
                st.write("tables/df for exploration")

st.divider()

footer = st.container()
st.write("This will show last.")
footer.write("This will show first. Explainer insert")
footer.write("This will show second. Explainer insert")
# Code to create the link button
st.link_button("Go to project repo.", "https://github.com/AmilcarArmmand/DSC_205-Data_Visualization-Final_Project")
