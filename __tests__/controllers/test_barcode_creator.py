from src.controllers.barcode_creator_controller import BarcodeCreatorController


def test_create_barcode():
    [code,extension] = ['1861JF7h81372b-7wjd828Hyq','PNG']
    bc_controller = BarcodeCreatorController()
    response = bc_controller.create(code,extension)

    assert 'path' in response
    assert 'extension' in response
    assert 'type' in response


def test_create_barcode_with_missing_args():
    [code] = ['1861JF7h81372b-7wjd828Hyq']
    bc_controller = BarcodeCreatorController()

    try:
        bc_controller.create(code, '')
        assert False
    except Exception as err:
        assert isinstance(err,Exception)
