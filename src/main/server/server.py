from flask import Flask
from src.main.routes.tag_routes import tags_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tags_bp)

    return app
