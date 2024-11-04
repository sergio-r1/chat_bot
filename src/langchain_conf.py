from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192"
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente amigável."),
    ("human", "{input}"),
])

chain = prompt_template | chat

def generate_response(user_input):
    response = chain.invoke({"input": user_input})

    response_content = response.content
    return response_content
