# Dockerfile
FROM python:3.10

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto para o contêiner
COPY . /app

COPY .env /app/.env

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Configurar variáveis de ambiente para a Groq LLM API
ENV GROQ_API_KEY=${GROQ_API_KEY}

# Expor a porta padrão do Streamlit
EXPOSE 8599

# Executar a aplicação
CMD ["streamlit", "run", "main.py", "--server.port=8599", "--server.address=0.0.0.0"]
