from ..exception import (
    ErrorMessage, InvalidApiKey
)
from abc import ABC, abstractclassmethod


class Base(ABC):
    def __init__(self, response: dict) -> None:
        self.response = response
        if self.error_message == ErrorMessage.invalid_api_key:
            raise InvalidApiKey

    @abstractclassmethod
    def items(self):
        raise NotImplementedError

    @property
    def error_message(self):
        return self.response.get("errorMessage")

    @property
    def search_type(self):
        return self.response.get("searchType")

    @property
    def expression(self):
        return self.response.get("expression")
