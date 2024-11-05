# Chatbot de Aprendizado Contínuo
---

## Passos para executar o projeto
Para executar o projeto é necessário seguir os passos a seguir:
- **Fazer o clone do projeto**:
  - Contido no repositório:
    ```bash
    git clone https://github.com/sergio-r1/chat_bot.git
    ```

- **Obter a chave de API**:
  - O projeto utiliza a LLM da Groq. Para obter a chave, basta se cadastrar através do [link](https://console.groq.com/keys "https://console.groq.com/keys") para o site e criar a sua chave.
  - Com a chave da API, ainda é necessário atualizar o arquivo `.env`. Crie um arquivo .env seguindo o formato do exemplo contido no projeto.

- **Build do container**:
  - Após clonar o projeto, obter a chave da API e atualizar a chave da API no arquivo `.env`, será possível rodar o projeto através do comando abaixo. Esse comando irá criar o container e instalar todas as dependências do projeto.
    ```bash
    docker-compose up --build -d
    ```
    A flag `-d` serve para executar os containers em segundo plano, liberando o terminal após o build do container. O seu uso é opcional.

- **Acessando a interface do usuário**:
  - Para acessar a interface, é necessário digitar a seguinte URL no navegador: `http://localhost:8599/`, inserir uma mensagem na caixa de texto e enviar. A resposta será escrita abaixo da caixa de texto. Por padrão, a biblioteca `streamlit` usa a porta 8501, no entanto, preferi usar a porta 8599 nesse projeto.


## Implementação
Conforme a documentação fornecida para esse desafio, segue abaixo as funcionalidades que foram implementadas e as não implementadas.
- **Funcionalidades implementadas no projeto**:
  - Interface gráfica para o chatbot que contém campo de entrada de texto e exibição da resposta do chatbot.
  - Armazenamento das informações relevantes feitas de buffer de memória.
  - Conteinerização do projeto

- **Funcionalidades não implementadas no projeto**:
  - Suporte a personalização de usuário.
  - Uso de langGraph.
  - Banco de dados vetorial para salvar as preferências de uso do usuário e interações relevantes.
  - Testes unitários e de integração.
