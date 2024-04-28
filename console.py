import streamlit as st
import numpy as np
from menu import menu


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

st.sidebar.success("Select a category below.")

st.markdown(
    """
    **👈 Select a page from the sidebar**
    
"""
)
st.divider()



with st.container():
    tab1, tab2, tab3, tab4 = st.tabs(["Menu items", "📈 Chart", "📈 Chart", "🗃 Data"])

    with tab1:
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            st.subheader("col 1")
            
        with col2:
            st.subheader("col 2")
            
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

menu()
