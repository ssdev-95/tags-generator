from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity_exception import HttpUnprocessableEntityException


class TagCreatorValidator:
    def __init__(self, allowed_formats:list):
        self.__schema = {
            'product_code': {
                'type': 'string',
                'required': True,
                'empty': False
            },
            'extension': {
                'type': 'string',
                'required': True,
                'empty': False,
                'allowed': allowed_formats
            }
        }


    def validate(self, request)-> None:
        if request.json is None:
            raise HttpUnprocessableEntityException('Missing request body')

        v = Validator()
        if not v.validate(request.json, self.__schema):
            errors = v.errors
            raise HttpUnprocessableEntityException(errors)
