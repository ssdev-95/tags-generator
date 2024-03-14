import os
from sqlalchemy import create_engine
from .models.Base import Base



from ..main.server.static import config


class DBConnector:
    def __init__(self):
        if not '__engine' in self.__dict__ or self.__engine is None:
            self.__engine = create_engine(f'{config["db_url"]}', echo=True)


    def get_engine(self):
        return self.__engine


    def connect(self):
        Base.metadata.create_all(self.get_engine())


db_connector = DBConnector()

