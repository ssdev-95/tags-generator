from typing import Dict
from sqlalchemy import Enum
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    def to_dict(self) -> Dict:
        return {}


class AccountStatus(Enum):
    ACTIVE = 'ACCOUNT.ACTIVE'
    INNACTIVE = 'ACCOUNT.INNACTIVE'
