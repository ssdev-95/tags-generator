from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable_entity_exception import HttpUnprocessableEntityException


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error,HttpUnprocessableEntityException):
        return HttpResponse({
            'status_code': error.status_code,
            'body': {
                'errors': [{
                    'title': error.name,
                    'detail': error.message
                    }]
                },
        }, error.status_code)

    return HttpResponse({
        'body': {
            'status_code': 500,
            'errors': [{
                'title': 'InternalServerError',
                'detail': str(error)
            }]
        }
    }, 500)
