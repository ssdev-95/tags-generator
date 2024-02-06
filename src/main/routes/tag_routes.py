from flask import Blueprint, request, jsonify

tag_routes_bp = Blueprint('tag_routes', __name__)


@tag_routes_bp.route('/tags/create', methods=['POST'])
def create_tag():
    print(request.json)
    return jsonify({ 'success': 'true' })
