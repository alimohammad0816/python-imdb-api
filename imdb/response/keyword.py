from .base import Base
from ..core import KeywordCore
from typing import List


class Keyword(Base):
    @property
    def items(self) -> List[KeywordCore]:
        items = self.response.get("items")

        if items:
            return [KeywordCore(i) for i in items]

        else:
            return None
