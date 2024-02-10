import json
from src.main.server.server import create_app


flask_app = create_app()


def test_create_qrcode():
    with flask_app.test_client() as client:
        data=json.dumps({'product_code':'2952$34$2929927','extension':'PNG'})
        content_type='application/json'
        response = client.post('/tags/qrcode/create', data=data, content_type=content_type)
        assert response.status_code == 201


def test_create_qrcode_with_no_body():
    with flask_app.test_client() as client:
        content_type='application/json'
        response = client.post('/tags/qrcode/create', content_type=content_type)
        assert response.status_code == 500


def test_create_qrcode_with_wrong_fields():
    with flask_app.test_client() as client:
        data=json.dumps({'code':'2952$34$2929927','format':'PNG'})
        content_type='application/json'
        response = client.post('/tags/qrcode/create', data=data, content_type=content_type)
        assert response.status_code == 422


def test_create_qrcode_with_wrong_extension():
    with flask_app.test_client() as client:
        data=json.dumps({'product_code':'2952$34$2929927','extension':'JPG'})
        content_type='application/json'
        response = client.post('/tags/qrcode/create', data=data, content_type=content_type)
        assert response.status_code == 422
