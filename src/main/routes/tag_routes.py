from flask import Blueprint, request, jsonify
from src.validators.tag_creator_validator import TagCreatorValidator
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView


tags_bp = Blueprint('tag_routes',__name__)


@tags_bp.route('/tags/create', methods=['POST'])
def createTag():
    tag_type = request.args.get('type', 'BARCODE')
    allowed_formats = ['SVG','PNG']

    if tag_type == 'BARCODE':
        allowed_formats = allowed_formats + ['JPEG','ICO']

    tc_validator = TagCreatorValidator(allowed_formats)
    tc_validator.validate(request)

    http_request = HttpRequest(body=request.json)
    tag_creator_view = TagCreatorView(tag_type)
    http_response = tag_creator_view.create_tag(http_request)
    return jsonify(http_response.body), http_response.status_code
