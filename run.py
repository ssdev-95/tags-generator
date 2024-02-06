from src.main.server.server import create_app

app = create_app()


@app.route('/', methods=['GET'])
def hello():
    return 'hello, world'


if __name__ == '__main__':
    app.run('0.0.0.0', port=3001, debug=True)
