from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import SVGWriter


def init():
    app = Flask(__name__)

    @app.route('/code128', methods=['POST'])
    def code_128():
        body = request.json
        tag = Code128(body.get('product_code'), writer=SVGWriter())
        tag_path = f'{tag}'
        tag.save(tag_path)

        return jsonify({ 'tag': tag_path })

    app.run(host='0.0.0.0', port=3001)


if __name__ == '__main__':
    init()
