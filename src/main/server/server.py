from flask import Flask
from src.main.routes.tag_routes import tag_routes_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tag_routes_bp)

    return app
