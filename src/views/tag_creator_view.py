from typing import Dict
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:
    def validate_request(self, http_request_body: Dict):
        valid_formats = ['SVG','PNG','JPEG','ICO']
        if http_request_body is None:
            return False

        for key in ['product_code', 'extension']:
            if key not in http_request_body:
                return False

        if http_request_body['extension'].upper() not in valid_formats:
            return False

        return True

    def create_tag(self, http_request: HttpRequest) -> HttpResponse:
        request_body = http_request.body
        if not self.validate_request(request_body):
            return HttpResponse(status_code=400, body={ "success":"false" })

        product_code = request_body['product_code']
        extension = request_body['extension']

        tg_creator = TagCreatorController()
        response_body = tg_creator.create(product_code, extension)

        return HttpResponse(status_code=201, body=response_body)
