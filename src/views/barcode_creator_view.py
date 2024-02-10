from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.barcode_creator_controller import BarcodeCreatorController

class BarcodeCreatorView:
    def create_tag(self, http_request: HttpRequest) -> HttpResponse:
        request_body = http_request.body
        product_code = request_body['product_code']
        extension = request_body['extension']

        tag_creator = BarcodeCreatorController()
        response_body = tag_creator.create(product_code, extension)

        return HttpResponse(response_body, 201)
