from .base import Base
from ..core import NamePersonCore


class Name(Base):
    @property
    def items(self) -> NamePersonCore:
        return NamePersonCore(self.response)
