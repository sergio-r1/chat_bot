import streamlit as st
from langchain_conf import generate_response


class ChatbotMain():
    def __init__(self, title):
        self.title = title
        
    def run(self):
        st.title(self.title)
        user_input = st.text_input("Faça a sua pergunta ao chatbot:")
        if user_input:
            response = generate_response(user_input)
            st.write(response)


if __name__ == "__main__":
    app = ChatbotMain("Chatbot interativo")
    app.run()