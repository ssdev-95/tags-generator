from src.controllers.tag_retrieval_controller import TagRetrievalController
from src.errors.error_types.http_entity_not_found_exception import HttpEntityNotFoundException


class TagRetrievalView:
    def __init__(self):
        self.__controller:TagRetrievalController = TagRetrievalController()


    def get_tag_by_path(self,tag_path:str):
        tag = self.__controller.find_tag_by_path(tag_path)
        if tag is None:
            raise HttpEntityNotFoundException('No Tag Found For Given Tag_Path')

        return tag


    def get_tag_by_id(self, tag_id:str):
        tag = self.__controller.find_tag_by_id(tag_id)
        
        if tag is None:
            raise HttpEntityNotFoundException('No Tag Found For Given Tag_Id')

        return tag


    def get_all_tags(self):
        return self.__controller.find_all_tags()
