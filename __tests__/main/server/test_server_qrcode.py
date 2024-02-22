import json
from src.main.server.server import create_app
from src.errors.error_types.http_unprocessable_entity_exception import HttpUnprocessableEntityException


flask_app = create_app()
flask_app.secret_key = 'The_Dumbest_Secret_Key_That_Someone_Can_Write_Right_Here_And_Now_Buddies'


def test_create_qrcode():
    with flask_app.test_client() as client:
        try:
            data=json.dumps({'product_code':'2952$34$2929927','extension':'PNG'})
            content_type='application/json'
            response = client.post('/tags/create?type=QRCODE', data=data, content_type=content_type)
            assert response.status_code == 201
        except Exception:
            assert False


def test_create_qrcode_with_no_body():
    with flask_app.test_client() as client:
        try:
            content_type='application/json'
            client.post('/tags/create?type=QRCODE', content_type=content_type)
        except Exception as e:
            assert isinstance(e, HttpUnprocessableEntityException)


def test_create_qrcode_with_wrong_fields():
    with flask_app.test_client() as client:
        try:
            data=json.dumps({'code':'2952$34$2929927','format':'PNG'})
            content_type='application/json'
            client.post('/tags/create?type=QRCODE', data=data, content_type=content_type)
        except Exception as e:
            assert isinstance(e, HttpUnprocessableEntityException)


def test_create_qrcode_with_wrong_extension():
    with flask_app.test_client() as client:
        try:
            data=json.dumps({'product_code':'2952$34$2929927','extension':'JPG'})
            content_type='application/json'
            client.post('/tags/create?type=QRCODE', data=data, content_type=content_type)
        except Exception as e:
            assert isinstance(e, HttpUnprocessableEntityException)
