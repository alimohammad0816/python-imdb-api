from ..exception import (
    ErrorMessage, InvalidApiKey
)


class Base:
    def __init__(self, response: dict) -> None:
        self.response = response
        if self.error_message == ErrorMessage.invalid_api_key:
            raise InvalidApiKey

    @property
    def error_message(self):
        return self.response.get("errorMessage")

    @property
    def search_type(self):
        return self.response.get("searchType")
    
    @property
    def expression(self):
        return self.response.get("expression")
