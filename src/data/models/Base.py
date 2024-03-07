from typing import Dict
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    def to_dict(self) -> Dict:
        return {}
