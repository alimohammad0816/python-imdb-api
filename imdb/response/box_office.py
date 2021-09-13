from .base import Base
from ..core import BoxOfficeCore
from typing import List


class BoxOffices(Base):
    @property
    def items(self) -> List[BoxOfficeCore]:
        items = self.response.get("items")

        if items:
            return [BoxOfficeCore(i) for i in items]

        else:
            return None
