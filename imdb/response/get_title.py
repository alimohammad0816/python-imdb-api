from .base import Base
from ..core import TitleCore
from ..exception import NotFound


class Title(Base):
    @property
    def items(self) -> TitleCore:
        items = self.response
        if items:
            return TitleCore(self.response)

        else:
            raise NotFound
