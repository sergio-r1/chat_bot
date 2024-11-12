import streamlit as st
from chatbot_config import Chatbot


class ChatbotMain():
    def __init__(self, title):
        self.title = title
        self.chat = Chatbot()
        
    def run(self):
        st.title(self.title)
        user_input = st.text_input("Faça a sua pergunta ao chatbot:")
        if user_input:
            response = self.chat.generate_response(user_input)
            st.write(response)


if __name__ == "__main__":
    app = ChatbotMain("Chatbot")
    app.run()