from flask import Flask, request #importando classe flask do framework Flask

app = Flask(__name__) #app -> instância - representa a aplicação web - registra as rotas __name__ guarda o arquivo utilizado na aplicação

@app.route('/') #criando rota
def hello_world(): #função chamada na rota
    return 'Hello, Docker!' #retorno da função

@app.route('/test', methods=['GET'])
def teste():
    num = request.args.get('num', default=None, type=int)
    text = request.args.get('text', default=None, type=str)

    if num is None or text is None:
        return "Erro: É necessário fornecer os parâmetros numero e texto", 400

    return f'Recebido número: {num} e texto: "{text}".'

@app.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    if not nome or not email: return "Erro: É necessário fornecer 'nome' e 'email'", 400

    return f'Nome "{nome}" e Email "{email}"'


if __name__ == '__main__': #irá executar o servidor somente se o arquivo executar diretamente
   app.run(debug=True, host='0.0.0.0')


