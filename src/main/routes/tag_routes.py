from flask import Blueprint, request, redirect, render_template

from ...validators.tag_creator_validator import TagCreatorValidator
from ...views.http_types.http_request import HttpRequest
from ...views.tag_creator_view import TagCreatorView
from ...views.tag_retrieval_view import TagRetrievalView


tags_bp = Blueprint('tag_routes',__name__)


@tags_bp.route('/tags', methods=['GET'])
def listAllTags():
    tags_view = TagRetrievalView()
    return tags_view.get_all_tags()


@tags_bp.route('/tags/create', methods=['POST'])
def createTag():
    tag_type = request.args.get('type', 'BARCODE')
    allowed_formats = ['SVG','PNG']

    if tag_type == 'BARCODE':
        allowed_formats = allowed_formats + ['JPEG','ICO']

    tc_validator = TagCreatorValidator(allowed_formats)
    tc_validator.validate(request)

    tag_creator_view = TagCreatorView(tag_type)

    body = request.json or  {}
    http_request = HttpRequest(body=body)
    http_response = tag_creator_view.create_tag(http_request)
    tag_id = http_response.body.get('id')

    return redirect(f'/tags/{tag_id}'), http_response.status_code


@tags_bp.route('/tags/create', methods=['GET'])
def createTagPage():
    TYPE = request.args.get('type','BARCODE')
    FORMATS = ['SVG','PNG']

    if TYPE=='BARCODE':
        FORMATS = FORMATS + ['JPEG','ICO']

    return render_template('index.html',type=TYPE,formats=FORMATS)


@tags_bp.route('/tags/<id>', methods=['GET'])
def get_tag_image(id:str):
    tag_view = TagRetrievalView()
    tag = tag_view.get_tag_by_id(id)
    return render_template('tag_view.html',tag_path=tag.path, tag_name=tag.name)
