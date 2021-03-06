from typing import List

from .base import Base
from ..core import ComingSoonCore


class ComingSoon(Base):
    @property
    def items(self) -> List[ComingSoonCore]:
        items = self.response.get("items")

        if items:
            return [ComingSoonCore(i) for i in items]

        else:
            return None
