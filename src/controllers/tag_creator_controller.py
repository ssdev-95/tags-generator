from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler


class TagCreatorController:
    def create(self, product_code: str, extension: str) -> Dict:
        tag_path = self.__create_tag(product_code, extension)
        return self.__format_response(tag_path, extension)


    def __create_tag(self, product_code: str, extension: str) -> str:
        bc_handler = BarcodeHandler()
        tag_path = bc_handler.create_barcode(product_code,extension.lower())
        return tag_path


    def __format_response(self, tag_path: str, extension: str) -> Dict:
        return {
            'type': 'x-image-tag',
            'extension': extension,
            'path': f'{tag_path}.{extension.lower()}'
        }
