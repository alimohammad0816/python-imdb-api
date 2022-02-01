from .base import Base
from ..core import YouTubeTrailerCore


class YouTubeTrailer(Base):
    @property
    def items(self) -> YouTubeTrailerCore:
        return YouTubeTrailerCore(self.response)
