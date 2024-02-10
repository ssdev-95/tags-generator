from src.controllers.qrcode_creator_controller import QrcodeCreatorController


def test_create_qrcode():
    [code,extension] = ['1861JF7h81372b-7wjd828Hyq','PNG']
    qr_controller = QrcodeCreatorController()
    response = qr_controller.create(code,extension)

    assert 'path' in response
    assert 'extension' in response
    assert 'type' in response


def test_create_qrcode_with_missing_args():
    [code] = ['1861JF7h81372b-7wjd828Hyq']
    qr_controller = QrcodeCreatorController()

    try:
        qr_controller.create(code,'')
        assert False
    except Exception as err:
        assert isinstance(err,Exception)
