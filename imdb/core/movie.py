class MovieCore:
    def __init__(self, items: dict) -> None:
        self.items = items
        self.id = items.get("id")
        self.rank = items.get("rank")
        self.rank_up_down = items.get("rankUpDown")
        self.title = items.get("title")
        self.full_title = items.get("fullTitle")
        self.year = items.get("year")
        self.image = items.get("image")
        self.crew = items.get("crew")
        self.imdb_rating = items.get("imDbRating")
        self.imdb_rating_count = items.get("imDbRatingCount")

    def __repr__(self) -> str:
        return f"IMDB-id({self.id})"
