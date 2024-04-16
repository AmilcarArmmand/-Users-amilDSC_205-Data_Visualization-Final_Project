import streamlit as st


st.set_page_config(
    page_title="Frontpage",
    page_icon="👋",
)

st.write("# The Modernization of China :cn:")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    
"""
)
