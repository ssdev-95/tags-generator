from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView


tag_routes_bp = Blueprint('tag_routes', __name__)


@tag_routes_bp.route('/tags/create', methods=['POST'])
def create_tag():
    tag_creator = TagCreatorView()
    http_request = HttpRequest(body=request.json)
    http_response = tag_creator.create_tag(http_request)

    return jsonify(http_response.body), http_response.status_code
