from typing import Dict
from uuid import uuid4
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .Base import Base


class User(Base):
    def __init__(self):
        self.id = f'{uuid4()}'

    __tablename__ = 'tb_users'

    id: Mapped[str]  = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String(255))
    account_status: Mapped[str] = mapped_column(String(10))

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'account_status': self.account_status
        }
