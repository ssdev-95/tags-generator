from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler


class TagCreatorController:
    def create(self, product_code: str) -> Dict:
        tag_path = self.__create_tag(product_code)
        return self.__format_response(tag_path)


    def __create_tag(self, product_code: str) -> str:
        bc_handler = BarcodeHandler()
        tag_path = bc_handler.create_barcode(product_code)
        return tag_path


    def __format_response(self, tag_path) -> Dict:
        return {
            'type': 'x-image-tag',
            'extension': 'png',
            'short-path': tag_path,
            'full-path': f'{tag_path}.png'
        }
