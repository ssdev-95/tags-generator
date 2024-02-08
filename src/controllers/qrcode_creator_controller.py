from typing import Dict
from src.drivers.qrcode_handler import QrcodeHandler


class QrcodeCreatorController:
    def create(self, product_code: str, extension: str) -> Dict:
        tag_path = self.__create_tag(product_code, extension)
        return self.__format_response(tag_path, extension)


    def __create_tag(self, product_code: str, extension: str) -> str:
        qrc_handler = QrcodeHandler()
        tag_path = qrc_handler.create_qrcode(product_code,extension)
        return tag_path


    def __format_response(self, tag_path: str, extension: str) -> Dict:
        return {
            'type': 'x-image-tag',
            'extension': extension,
            'path': f'{tag_path}.{extension.lower()}'
        }
