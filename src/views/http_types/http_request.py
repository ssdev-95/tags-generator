from typing import Dict


class HttpRequest:
    def __init__(self,
        headers: Dict = None,
        body: Dict = None,
        query_params: Dict = None
    ):
        self.headers = headers
        self.body = body
        self.query_params = query_params
