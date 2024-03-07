from typing import Dict, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.data.models.Tag import Tag
from src.data.db_connector import db_connector


class TagRetrievalController:
    def __init__(self):
        self.__engine = db_connector.get_engine()


    def find_tag_by_id(self, tag_id:str): 
        with Session(self.__engine) as conn:
            query = select(Tag).filter_by(id=tag_id)
            return conn.scalars(query).one_or_none()


    def find_tag_by_path(self, tag_path:str):
        with Session(self.__engine) as conn:
            query = select(Tag).filter_by(path=tag_path)
            return conn.scalars(query).one_or_none()


    def find_all_tags(self):
        with Session(self.__engine) as conn:
            tags:List[Dict] = []
            for tagRAW in conn.scalars(select(Tag)).fetchall():
                print(tagRAW.to_dict())
                tags.append(tagRAW.to_dict())
            return tags
