import streamlit as st
from streamlit_globe import streamlit_globe


st.subheader("Globe")
pointsData=[{'lat': 35.86166, 'lng': 104.195397, 'size': 0.3, 'color': 'red'}]
labelsData=[{'lat': 35.86166, 'lng': 104.195397, 'size': 0.3, 'color': 'red', 'text': 'Yuzhong County, Lanzhou, China'}]
streamlit_globe(pointsData=pointsData, labelsData=labelsData, daytime='day', width=800, height=600)
