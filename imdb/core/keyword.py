class KeywordCore:
    def __init__(self, items: dict) -> None:
        self.items = items
        self.id = items.get("id")
        self.title = items.get("title")
        self.year = items.get("year")
        self.image = items.get("image")
        self.imdb_rating = items.get("imDbRating")

