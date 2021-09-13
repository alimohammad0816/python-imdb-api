from .base import Base
from ..core import BoxOfficeAllCore
from typing import List

class BoxOfficeAll(Base):
    @property
    def items(self) -> List[BoxOfficeAllCore]:
        items = self.response.get("items")

        if items:
            return [BoxOfficeAllCore(i) for i in items]
        
        else:
            return None
