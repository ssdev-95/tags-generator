from flask import Blueprint, jsonify, request, redirect, render_template, session
from sqlalchemy import except_

from ...validators.auth_validator import AuthValidator
from ...views.http_types.http_request import HttpRequest
from ...views.authentication_view import AuthenticationView

auth_bp = Blueprint('auth_routes', __name__)


def check_session() -> bool:
    has_session = len(session.values())>0
    is_logged_in = ('is_logged_in' in session) and (session['is_logged_in'] is True)
    return has_session or is_logged_in


@auth_bp.route('/auth/signup', methods=['POST'])
def register_user():
    validator = AuthValidator('signup')
    validator.validate(request)

    auth_view = AuthenticationView()
    http_request = HttpRequest(body=request.form)

    auth_view.register(http_request)
    return redirect('/auth/signin'), 422


@auth_bp.route('/auth/signup', methods=['GET'])
def signup_page():
    if check_session():
        return redirect('/tags/create'), 422

    session['is_logged_in'] = False
    return render_template('signup.html')


@auth_bp.route('/auth/signin', methods=['POST'])
def authenticate_user():
    validator = AuthValidator('signin')
    validator.validate(request)

    auth_view = AuthenticationView()
    http_request = HttpRequest(body=request.form)

    [user, is_logged_in] = auth_view.login(http_request)
    if is_logged_in:
        session['is_logged_in'] = True
        print(f'DEBUG -> {user[0]}')
        return redirect('/tags/create'), 422

    return redirect('/auth/signin'), 422


@auth_bp.route('/auth/signin', methods=['GET'])
def signin_page():
    if check_session():
        return redirect('/tags/create'), 422

    session['is_logged_in'] = False
    return render_template('signin.html')


@auth_bp.route('/auth/signout', methods=['POST'])
def sign_out():
    return redirect('/auth/signin'), 422

@auth_bp.route('/auth/users/<id>', methods=['GET'])
def get_user_data(id:str):
    if id is None:
        return 'No id provided'
    return id
