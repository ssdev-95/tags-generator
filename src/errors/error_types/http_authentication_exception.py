class HttpAuthenticationException(Exception):
    def __init__(self, message: str, auth_type:str):
        super().__init__(message)
        self.message = message
        self.status_code = 401
        self.name = 'AuthenticationFailure'
        self.auth_type = auth_type
