from flask import Flask
from src.main.routes.tag_routes import tags_bp




from src.errors.error_handlers import handle_errors

def create_app():
    app = Flask(__name__)
    app.register_error_handler(500, handle_errors)
    app.register_blueprint(tags_bp)

    return app
