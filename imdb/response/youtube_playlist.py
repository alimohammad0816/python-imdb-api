from .base import Base
from ..core import YouTubePlaylistCore


class YouTubePlaylist(Base):
    @property
    def items(self) -> YouTubePlaylistCore:
        return YouTubePlaylistCore(self.response)
