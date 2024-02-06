from flask import Flask


def init():
    app = Flask(__name__)
    app.run(host='0.0.0.0', port=3001)


if __name__ == '__main__':
    init()
