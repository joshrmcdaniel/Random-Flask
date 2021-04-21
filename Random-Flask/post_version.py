from flask import Flask

app = Flask(__name__)


@app.route('/post/<int:id>')
def post(id):
    return f'This is post {id}'


@app.route('/version/<float:v>')
def version(v):
    return f'Version: {v}'


if __name__ == '__main__':
    app.run()
