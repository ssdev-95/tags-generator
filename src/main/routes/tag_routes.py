from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handlers import handle_errors
from src.validators.tag_creator_validator import TagCreatorValidator
from src.views.barcode_creator_view import BarcodeCreatorView
from src.views.qrcode_creator_view import QrcodeCreatorView


tag_routes_bp = Blueprint('tag_routes', __name__)


@tag_routes_bp.route('/tags/barcode/create', methods=['POST'])
def create_barcode_tag():
    allowed_formats = ['SVG','PNG','JPEG','ICO']
    http_response = None

    try:
        tc_validator = TagCreatorValidator(allowed_formats)
        tc_validator.validate(request)

        tag_creator = BarcodeCreatorView()
        http_request = HttpRequest(body=request.json)
        http_response = tag_creator.create_tag(http_request)
    except Exception as err:
        http_response = handle_errors(err)

    return jsonify(http_response.body), http_response.status_code


@tag_routes_bp.route('/tags/qrcode/create', methods=['POST'])
def create_qrcode_tag():
    allowed_formats = ['SVG','PNG']
    http_response = None

    try:
        tc_validator = TagCreatorValidator(allowed_formats)
        tc_validator.validate(request)
        tag_creator = QrcodeCreatorView()
        http_request = HttpRequest(body=request.json)
        http_response = tag_creator.create_tag(http_request)
    except Exception as err:
        http_response = handle_errors(err)

    return jsonify(http_response.body), http_response.status_code
