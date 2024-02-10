from typing import Dict
from src.validators.tag_creator_validator import TagCreatorValidator


class MockRequest:
    def __init__(self, json:Dict):
        self.json = json


def test_create_qrcode():
    validator = TagCreatorValidator(['PNG','SVG'])
    mock_request = MockRequest(json={'product_code': 'mocked-product-code', 'extension': 'SVG'})
    validator.validate(mock_request)


def test_create_qrcode_w_error():
    validator = TagCreatorValidator(['PNG','SVG'])
    mock_request = MockRequest(json={'product_code': 'mocked-product-code', 'extension': 'JPG'})

    try:
        validator.validate(mock_request)
        assert False
    except Exception:
        assert True
