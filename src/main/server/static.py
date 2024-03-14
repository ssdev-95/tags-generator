import os

template_folder = os.path.abspath(__file__)
template_folder = os.path.dirname(template_folder)
template_folder = os.path.dirname(template_folder)
template_folder = os.path.dirname(template_folder)
template_folder = os.path.join(template_folder,'templates')

static_folder = os.path.join(template_folder,'static')
tmp_folder = os.path.join(static_folder, 'tmp')

PERMANENT_SESSION_LIFETIME = 24 * 60 * 60

config = {
    'template_folder': template_folder,
    'static_folder': static_folder,
    'tmp_folder': tmp_folder,
    'secret_key': os.getenv('SECRET_KEY'),
    'session_lifetime': PERMANENT_SESSION_LIFETIME,
    'session_type': 'filesystem',
    'session_use_signer': True,
    'db_url': os.getenv('DB_URL')
}
