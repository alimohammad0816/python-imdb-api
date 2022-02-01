from .base import Base
from ..core import CompanyCore


class Company(Base):
    @property
    def items(self) -> CompanyCore:
        return CompanyCore(self.response)
