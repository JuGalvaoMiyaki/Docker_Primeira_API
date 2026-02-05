# Projeto Docker Primeira API

Esse projeto é um projeto Toolbox onde demonstra o desenvolvimento 
de uma aplicação Flask simples, utilizando Docker para construir uma imagem. 
Será possível acessar rotas simples, criar cadastros e enviar dados via query string. 

# 🚀 Tecnologias Utilizadas

## Docker
--Para instalar o Docker no Windows acesse : [Windows Link](https://docs.docker.com/desktop/setup/install/windows-install/)
--Configurar WSL no Windows : [WSL](https://learn.microsoft.com/pt-br/windows/wsl/tutorials/wsl-containers)
--Para Linux e MACOS: [Linux Link ](https://docs.docker.com/desktop/setup/install/linux/) [Mac Link](https://docs.docker.com/desktop/setup/install/mac-install/)

## Python 
--[Python 3](https://www.python.org/)

## Flask
--[Flask](https://flask.palletsprojects.com/)


# 📂 Estrutura do projeto

|--app.py
    |--Dockerfile
        |--README.md
            |--requirements.txt


# ⚙️ Instalação e execução

1 . Clone o repositório 

git clone https://github.com/JuGalvaoMiyaki/Docker_Primeira_API

2 . Crie um ambiente virtual (opcional, mas recomendado)

python -m venv venv                     # Para criar o ambiente virtual
source venv/bin/activate   # Linux/Mac  # Para ativar o ambiente virtual
venv\Scripts\activate      # Windows    #Para ativar o ambiente virtual

3 . Instale as Dependências 

pip install -r requirements.txt

4 . Rode a aplicação

python app.py

A aplicação estará disponível em:

http://localhost:5000

# 🐳 Executando com Docker

1 . Construir a imagem

docker build -t flask-app .

2 . Rodar o container

docker run -p 5000:5000 flask-app

3 . Verifique se a aplicação está rodando

docker ps


# 🔗 Rotas disponíveis

• Método: GET

• Rota: http://localhost:5000/

• Descrição : Retorna Mensagem de Boas Vindas

• Exemplo:
## No browser abra o link : http://localhost:5000/
## Resposta: "Hello, Docker"

• Método: GET  

• Rota: http://localhost:5000/test

• Descrição : Recebe e retorna parâmetros fornecidos pelo usuário

• Parâmetros aceitos: São aceitos somente números inteiros(int) e textos(string)

• Exemplo:
## No browser : localhost:5000/test?num=123&text=ola   #Insira os parâmetros em numero inteiro e texto string
## Resposta: Recebido numero 123 e texto ola

• Método: POST

• Rota: http://localhost:5000/cadastro

• Descrição : Recebe e retorna dados fornecidos pelo usuario via json, nome e email. 

• Exemplo:
## Postman ou Insomnia : localhost:5000/cadastro   #Insira os dados no formulário json
    
** json
{
  "nome": "Maria",
  "email": "maria@email.com"
}

## Resposta: Nome: Maria e Email : maria@email.com

# Erros e respostas esperados

Rota:   http://localhost:5000/test 
    Caso o usuário não forneça parâmetros ou insira um tipo inválido, retornará o erro 400 : 
    - ### "Erro: É necessário fornecer os parâmetros numero e texto" -

Rota:   http://localhost:5000/cadastro
    Caso o usuário não forneça os dados como nome e email, retornará o erro 400 : 
    - ### "Erro: É necessário fornecer 'nome' e 'email'" -


# 📌 Observações 

Quando finalizar, não esqueça de parar o container. 

docker ps                       #verifica o container que esta rodando
docker stop <id_container>      #para o container 

# 👩‍💻 Autor

•Juliana Galvão Miyaki

*Para contribuir com o projeto: juliana.galvao@tbxtech.com* 

*Projeto de estudo com Flask e Docker*

#  Referências Técnicas

Docker: https://docs.docker.com
Python: https://docs.python.org/pt-br/3/
Flask:  https://flask.palletsprojects.com/en/stable/reqcontext/
