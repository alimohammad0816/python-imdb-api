from .base import Base
from ..core import YouTubeCore


class YouTube(Base):
    @property
    def items(self) -> YouTubeCore:
        return YouTubeCore(self.response)
