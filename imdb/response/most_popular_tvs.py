from typing import List
from .base import Base
from ..core import MovieCore


class MostPopularTVs(Base):
    @property
    def items(self) -> List[MovieCore]:
        items = self.response.get("items")

        if items:
            return [MovieCore(i) for i in items]

        else:
            return None
