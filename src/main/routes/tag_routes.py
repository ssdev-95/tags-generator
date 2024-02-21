from flask import Blueprint, request, jsonify, redirect, render_template, flash
from src.validators.tag_creator_validator import TagCreatorValidator
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView


tags_bp = Blueprint('tag_routes',__name__)


@tags_bp.route('/tags/create', methods=['POST'])
def createTag():
    http_request = HttpRequest(body=request.json,query_params=request.args)

    tag_type = http_request.query_params.get('type', 'BARCODE')
    allowed_formats = ['SVG','PNG']

    if tag_type == 'BARCODE':
        allowed_formats = allowed_formats + ['JPEG','ICO']

    tc_validator = TagCreatorValidator(allowed_formats)
    tc_validator.validate(request)

    tag_creator_view = TagCreatorView(tag_type)
    http_response = tag_creator_view.create_tag(http_request)

    flash('Success', 'success')
    return redirect('/tags/create'), http_response.status_code


@tags_bp.route('/tags/create', methods=['GET'])
def createTagPage():
    TYPE = request.args.get('type','BARCODE')
    FORMATS = ['SVG','PNG']

    if TYPE=='BARCODE':
        FORMATS = FORMATS + ['JPEG','ICO']

    return render_template('index.html',type=TYPE,formats=FORMATS)
