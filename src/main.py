import streamlit as st
from langchain_conf import generate_response

st.title("Chatbot")
user_input = st.text_input("Pergunte ao chatbot:")
if user_input:
    st.session_state.input_text = ""
    response = generate_response(user_input)
    st.write(response)
