from typing import List
from .base import Base
from ..core import SearchMovieCore


class SearchMovies(Base):
    @property
    def items(self) -> List[SearchMovieCore]:
        items = self.response.get("results")

        if items:
            return [SearchMovieCore(i) for i in items]

        else:
            return None
