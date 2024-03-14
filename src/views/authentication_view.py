from ..controllers.authentication_controller import AuthenticationController
from .http_types.http_request import HttpRequest


class AuthenticationView:
    def __init__(self) -> None:
        self.__controller = AuthenticationController()


    def register(self, request: HttpRequest):
        self.__controller.register(
            username=f'{request.body.get("username")}',
            email=f'{request.body.get("email")}',
            password=f'{request.body.get("password")}'
        )


    def login(self, request: HttpRequest):
        return self.__controller.login(
            username=f'{request.body.get("username")}',
            password=f'{request.body.get("password")}'
        )
