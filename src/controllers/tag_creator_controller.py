from typing import Dict
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.drivers.tag_creator_handler import TagCreatorHandler
from src.data.models.Tag import Tag
from src.data.db_connector import db_connector


class TagCreatorController:
    def __init__(self, handler:TagCreatorHandler):
        self.tag_creator = handler


    def create(self, product_data:str, extension:str) -> Dict:
        tag_path = self.tag_creator.create_tag(product_data, extension)
        return self.__persist_tag_data__(tag_path, extension)


    def find_tag_by_path(self, conn:Session, tag_path:str):
        query = select(Tag).filter_by(path=tag_path)
        return conn.scalars(query).one_or_none()


    def __persist_tag_data__(self,tag_path:str,extension:str) -> Dict:
        with Session(db_connector.get_engine()) as conn:
            tag = self.find_tag_by_path(conn, tag_path)
            if tag is not None:
                return tag.to_dict()

            tag = Tag()
            tag.name = tag_path.replace('/tmp/', '', 1).replace(f'.{extension}', '', 1)
            tag.extension = extension
            tag.path = tag_path
            conn.add(tag)

            return tag.to_dict()
