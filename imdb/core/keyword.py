class KeywordCore:
    def __init__(self, response: dict) -> None:
        self.response = response
        self.id = response.get("id")
        self.title = response.get("title")
        self.year = response.get("year")
        self.image = response.get("image")
        self.imdb_rating = response.get("imDbRating")

