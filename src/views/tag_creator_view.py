from typing import Dict
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from src.controllers.tag_creator_controller import TagCreatorController
from src.drivers.tag_creator_handler import TagCreatorHandler

from src.drivers.barcode_handler import BarcodeHandler
from src.drivers.qrcode_handler import QrcodeHandler

class TagCreatorView:
    def __init__(self, tag_type:str):
        self.__tag_type__ = tag_type
        
    def create_tag(self, http_request: HttpRequest) -> HttpResponse:

        tag_creator_handler:TagCreatorHandler

        request_body = http_request.body
        product_code = request_body['product_code']
        extension = request_body['extension']

        if (self.__tag_type__.upper() == 'QRCODE'):
            tag_creator_handler = QrcodeHandler()
        else:
            tag_creator_handler = BarcodeHandler()

        tag_creator = TagCreatorController(tag_creator_handler)
        response_body = tag_creator.create(product_code, extension)

        return HttpResponse(response_body, 201)
