from sqlalchemy import select
from sqlalchemy.orm import Session

from src.data.models.Base import AccountStatus

from ..data.models.User import User
from ..data.db_connector import db_connector
from ..drivers.bcrypt import bcrypt
from ..errors.error_types.http_authentication_exception import HttpAuthenticationException

class AuthenticationController:
    def __init__(self) -> None:
        self.__engine = db_connector.get_engine()


    def find_user_by_username(self, username:str):
        with Session(self.__engine) as conn:
            query = select(User).filter_by(username=username)
            return conn.execute(query).scalar_one_or_none()


    def register(self,username:str,email:str,password:str):
        with Session(self.__engine) as conn:
            user = self.find_user_by_username(username=username)

            if user is not None:
                raise HttpAuthenticationException(message='User Already Exists', auth_type='signup')

            try:
                user = User()
                user.username = username
                user.email = email
                encrypted_password = bcrypt.generate_password_hash(password).decode('UTF-8')
                user.password = encrypted_password
                user.account_status = AccountStatus.ACTIVE

                conn.add(user)
                conn.commit()
            except:
                raise HttpAuthenticationException(message='Invalid Data Provided', auth_type='signup')


    def login(self,username:str,password:str):
        user = self.find_user_by_username(username=username)

        if user is None:
            raise HttpAuthenticationException(message='User Does Not Exists', auth_type='signin')

        if not bcrypt.check_password_hash(user.password, password):
            raise HttpAuthenticationException(message='Invalid Credentials', auth_type='signin')

        return user, True
