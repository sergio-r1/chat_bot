from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

__all__ = ['Chatbot']

class ConfigChatbot():
    
    memory = ConversationBufferMemory()

    chat = ChatGroq(
        temperature=0,
        model="llama3-70b-8192"
    )

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente amigável. Aqui está o contexto anterior: {history}"),
        ("human", "{input}")
    ])

    chain = ConversationChain(
        llm=chat,
        prompt=prompt_template,
        memory=memory
    )


class Chatbot():
    
    def __init__(self):
        self.config = ConfigChatbot()
        
    
    def generate_response(self, user_input):
        try:
            response = self.config.chain.invoke({"input": user_input})
            
            if isinstance(response, dict) and "response" in response:
                return response["response"]
            elif isinstance(response, dict) and "content" in response:
                return response["content"]
            else:
                return "Algo inesperado aconteceu. \nPeço desculpas pelo inconveniente."
        except ValueError as ve:
            raise ValueError(f"Erro de Valor: {str(ve)}")
        except Exception as e:
            raise RuntimeError(f"Ocorreu um erro ao gerar a resposta: {str(e)}")
