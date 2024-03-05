from typing import Dict
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .Base import Base


class Tag(Base):
    __tablename__ = 'tb_tags'

    id: Mapped[str]  = mapped_column(primary_key=True)
    name: Mapped[str]  = mapped_column(String(255))
    extension: Mapped[str]  = mapped_column(String(10))
    path: Mapped[str]  = mapped_column(String(30))


    def to_dict(self)->Dict:
        return {
            'id': self.id,
            'name': self.name,
            'extension': self.extension,
            'path': self.path
        }
