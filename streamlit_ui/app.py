import streamlit as st
import requests

st.set_page_config(page_title='Chef Cart', layout='centered')
st.title('Chef Cart — Microservices Demo')

st.sidebar.header('Actions')
if st.sidebar.button('View Users'):
    try:
        r = requests.get('http://user_service:5001/users', timeout=3)
        st.json(r.json())
    except Exception as e:
        st.error(f'Error: {e}')

st.sidebar.write('---')
if st.sidebar.button('View Recipes'):
    try:
        r = requests.get('http://recipe_service:5002/recipes', timeout=3)
        st.json(r.json())
    except Exception as e:
        st.error(f'Error: {e}')

st.write('Use buttons in the left to fetch data from microservices')
