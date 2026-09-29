import streamlit as st
import requests

st.title("Hello Sameehah ")

if st.button("Say Hello"):
    response = requests.get("http://127.0.0.1:8000/hello")

    data = response.json()

    st.success(data["message"])