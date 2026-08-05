import os
from flask import Flask, request, render_template #importando classe flask do framework Flask

app = Flask(__name__) #app -> instância - representa a aplicação web - registra as rotas __name__ guarda o arquivo utilizado na aplicação

@app.route('/') #criando rota
def hello_world(): #função chamada na rota
    return render_template('index.html')

@app.route('/dados', methods=['GET'])
def recebe_dados():
    num = request.args.get('num', default=None, type=int)
    text = request.args.get('text', default=None, type=str)

    if num is None or text is None:
        return render_template('error.html', message="É necessário fornecer os parâmetros numero e texto"), 400

    return render_template('dados.html', num=num, text=text)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    if not nome or not email:
        return render_template('error.html', message="É necessário fornecer 'nome' e 'email'"), 400

    return render_template('cadastro.html', nome=nome, email=email)


if __name__ == '__main__': #irá executar o servidor somente se o arquivo executar diretamente
   debug_mode = os.getenv('FLASK_DEBUG', '0') == '1'
   app.run(debug=debug_mode, host='127.0.0.1')


