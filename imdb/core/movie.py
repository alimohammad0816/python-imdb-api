class MovieCore:
    def __init__(self, response: dict) -> None:
        self.response = response
        self.id = response.get("id")
        self.rank = response.get("rank")
        self.rank_up_down = response.get("rankUpDown")
        self.title = response.get("title")
        self.full_title = response.get("fullTitle")
        self.year = response.get("year")
        self.image = response.get("image")
        self.crew = response.get("crew")
        self.imdb_rating = response.get("imDbRating")
        self.imdb_rating_count = response.get("imDbRatingCount")

    def __repr__(self) -> str:
        return f"IMDB-id({self.id})"
