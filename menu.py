import streamlit as st


def menu():
     """Show a navigation menu."""
     st.sidebar.page_link("console.py", label="Home")
     st.sidebar.page_link("pages/Life_Expectancy.py", label="Life Expectancy📈")
     st.sidebar.page_link("pages/Growth_Comparison.py", label="Growth Comparision")
     st.sidebar.page_link("pages/High_Speed_Rail.py", label="High Speed Rail📈")
     st.sidebar.page_link("pages/Poverty.py", label="Extreme Poverty")
     st.sidebar.page_link("pages/Imports_and_Exports.py", label="Imports and Exports")
     st.sidebar.page_link("pages/Power_Generation.py", label="Power Generation")
     st.sidebar.page_link("pages/Renewable_Power.py", label="Renewable Power_📊")
     st.sidebar.page_link("pages/Agri_Production.py", label="Agricultural Production")
     st.sidebar.page_link("pages/inspiration.py", label="Inspiration")
     st.sidebar.page_link("pages/media.py", label="Trivia 🗃")    
     # st.sidebar.page_link("pages/Session_State_Basics.py", label="Photo Gallery")
