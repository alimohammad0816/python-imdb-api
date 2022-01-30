from .base import Base
from ..core import SearchKeywordCore
from typing import List


class SearchKeyword(Base):
    @property
    def items(self) -> List[SearchKeywordCore]:
        items = self.response.get("results")

        if items:
            return [SearchKeywordCore(i) for i in items]

        else:
            return None
