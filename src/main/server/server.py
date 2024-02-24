import os
from flask import Flask
from src.main.routes.tag_routes import tags_bp
from src.errors.error_handlers import handle_errors


template_folder = os.path.abspath(__file__)
template_folder = os.path.dirname(template_folder)
template_folder = os.path.dirname(template_folder)
template_folder = os.path.dirname(template_folder)
template_folder = os.path.join(template_folder,'templates')
static_folder = os.path.join(template_folder,'static')

SECRET_KEY = os.getenv('SECRET_KEY')

def create_app():
    app = Flask(
        __name__,
        template_folder=template_folder,
        static_url_path='',
        static_folder=static_folder
    )

    app.secret_key = SECRET_KEY
    app.register_error_handler(500, handle_errors)
    app.register_blueprint(tags_bp)
    app.secret_key = SECRET_KEY

    return app
