import os
from flask import Flask
from src.main.routes.tag_routes import tags_bp
from src.errors.error_handlers import handle_errors

from .static import template_folder, static_folder
from src.data.db_connector import db_connector


SECRET_KEY = os.getenv('SECRET_KEY')

def create_app():
    app = Flask(
        __name__,
        static_url_path='',
        template_folder=template_folder,
        static_folder=static_folder
    )
    app.secret_key = SECRET_KEY
    app.register_error_handler(500, handle_errors)
    app.register_blueprint(tags_bp)
    app.secret_key = SECRET_KEY

    db_connector.connect()
    return app
