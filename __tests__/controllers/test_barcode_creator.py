from src.controllers.tag_creator_controller import TagCreatorController
from src.drivers.barcode_handler import BarcodeHandler


def test_create_barcode():
    [code,extension] = ['1861JF7h81372b-7wjd828Hyq','PNG']
    tag_handler = BarcodeHandler()
    bc_controller = TagCreatorController(tag_handler)
    response = bc_controller.create(code,extension)

    assert 'path' in response
    assert 'extension' in response
    assert 'type' in response


def test_create_barcode_with_missing_args():
    [code] = ['1861JF7h81372b-7wjd828Hyq']
    tag_handler = BarcodeHandler()
    bc_controller = TagCreatorController(tag_handler)

    try:
        bc_controller.create(code, '')
        assert False
    except Exception as err:
        assert isinstance(err,Exception)


def test_create_barcode_with_missing_proper_handler():
    [code,extension] = ['1861JF7h81372b-7wjd828Hyq','PNG']
    try:
        bc_controller = TagCreatorController(None)
        bc_controller.create(code, extension)
        assert False
    except Exception:
        assert True
