# Chatbot de Aprendizado Contínuo
---

## Passos para executar o projeto

- **Fazer o clone do projeto**:
  - Contido no repositório:
    ```bash
    git clone https://github.com/sergio-r1/chat_bot.git
    ```

- **Obter a chave de API**:
  - O projeto utiliza a LLM da Groq. Para obter a chave, basta se cadastrar através do [link](https://console.groq.com/keys "https://console.groq.com/keys") para o site e criar a sua chave.
  - Com a chave da API, ainda é necessário atualizar o arquivo `.env`. É possível seguir o formato do exemplo contido no projeto.

- **Build do container**:
  - Após clonar o projeto, obter a chave da API e atualizar a chave da API no arquivo `.env`, será possível rodar o projeto através do comando abaixo. Esse comando irá criar o container e instalar todas as dependências do projeto.
    ```bash
    docker-compose up --build -d
    ```

- **Acessando a interface do usuário**:
  - Para acessar a interface, é necessário digitar a seguinte URL no navegador: `http://localhost:8599/`, inserir uma mensagem na caixa de texto e enviar. A resposta será escrita abaixo da caixa de texto.


## Implementação



## Exemplos de uso

