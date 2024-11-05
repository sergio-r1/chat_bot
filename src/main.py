import streamlit as st
from langchain_conf import generate_response

st.title("Chatbot")
user_input = st.text_input("Faça a sua pergunta ao chatbot:")
if user_input:
    response = generate_response(user_input)
    st.write(response)
