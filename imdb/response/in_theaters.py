from .base import Base
from ..core import InTheatersCore
from typing import List


class InTheaters(Base):
    @property
    def items(self) -> List[InTheatersCore]:
        items = self.response.get("items")

        if items:
            return [InTheatersCore(i) for i in items]

        else:
            return None
