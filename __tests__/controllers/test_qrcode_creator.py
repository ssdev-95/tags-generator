from src.controllers.tag_creator_controller import TagCreatorController
from src.drivers.qrcode_handler import QrcodeHandler


def test_create_qrcode():
    [code,extension] = ['1861JF7h81372b-7wjd828Hyq','PNG']
    tag_handler = QrcodeHandler()
    qr_controller = TagCreatorController(tag_handler)
    response = qr_controller.create(code,extension)

    assert 'path' in response
    assert 'extension' in response
    assert 'name' in response


def test_create_qrcode_with_missing_args():
    [code] = ['1861JF7h81372b-7wjd828Hyq']
    tag_handler = QrcodeHandler()
    qr_controller = TagCreatorController(tag_handler)

    try:
        qr_controller.create(code,'')
        assert False
    except Exception as err:
        assert isinstance(err,Exception)


def test_create_qrcode_with_missing_proper_handler():
    [code,extension] = ['1861JF7h81372b-7wjd828Hyq','PNG']

    try:
        qr_controller = TagCreatorController(None)
        qr_controller.create(code, extension)
        assert False
    except Exception:
        assert True
