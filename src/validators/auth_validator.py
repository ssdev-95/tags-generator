from cerberus import Validator

from src.errors.error_types.http_unprocessable_entity_exception import HttpUnprocessableEntityException

schemas = {
    'signin': {
        'credential': {
            'type': 'string',
            'required': True,
            'empty': False,
        },
        'password': {
            'type': 'string',
            'required': True,
            'empty': False
        }
    },
    'signup': {
        'username': {
            'type': 'string',
            'required': True,
            'empty': False,
        },
        'email': {
        },
        'password': {
            'type': 'string',
            'required': True,
            'empty': False
        },
        'password_confirmation': {
            'type': 'string',
            'required': True,
            'empty': False
        }
    }
}

class AuthValidator():
    def __init__(self, schema:str) -> None:
        self.__schema = schemas[schema]

    def validate(self, request) -> None:
        error = 'Some required fields are missing'

        if request.form is None:
            raise HttpUnprocessableEntityException(error)

        v = Validator()

        if not v.validate(request.form, self.__schema):
            print(f'{v.errors}')
            raise HttpUnprocessableEntityException(error)

        if request.form.get('password') != request.form.get('password_confirmation'):
            print('PASSWORD AND CONFIRMATION DOES NOT MATCH')
            raise HttpUnprocessableEntityException('Credentials Does Not Match Any')
