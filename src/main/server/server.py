from flask import Flask

from ...errors.error_handlers import handle_errors
from ...data.db_connector import db_connector
from ...drivers.bcrypt import bcrypt
from ..routes.auth_routes import auth_bp
from ..routes.tag_routes import tags_bp
from .static import config

def create_app():
    app = Flask(
        __name__,
        static_url_path='',
        template_folder=config['template_folder'],
        static_folder=config['static_folder']
    )

    app.config['SESSION_USE_SIGNER'] = config['session_use_signer']
    app.config['SESSION_TYPE'] = config['session_type']
    app.config['PERMANENT_SESSION_LIFETIME'] = config['session_lifetime']

    app.secret_key = config['secret_key']
    app.register_error_handler(500, handle_errors)
    app.register_blueprint(auth_bp)
    app.register_blueprint(tags_bp)

    db_connector.connect()
    bcrypt.init_app(app)
    return app
