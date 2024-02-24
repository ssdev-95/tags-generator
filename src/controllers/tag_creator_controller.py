from typing import Dict
from src.drivers.tag_creator_handler import TagCreatorHandler


class TagCreatorController:
    def __init__(self, handler:TagCreatorHandler):
        self.tag_creator = handler


    def create(self, product_data:str, extension:str) -> Dict:
        tag_path = self.tag_creator.create_tag(product_data, extension)
        return self.__format_response__(tag_path, extension)


    def __format_response__(self,tag_path:str,extension:str) -> Dict:
        return {
            'type': 'x-image-tag',
            'extension': extension,
            'path': f'{tag_path}'
        }
