class ComingSoonCore:
    def __init__(self, items) -> None:
        self.items = items
        self.id = items.get("id")
        self.title = items.get("title")
        self.full_title = items.get("fullTitle")
        self.year = items.get("year")
        self.release_state = items.get("releaseState")
        self.image = items.get("image")
        self.runtime_mins = items.get("runtimeMins")
        self.runtime_str = items.get("runtimeStr")
        self.plot = items.get("plot")
        self.content_rating = items.get("contentRating")
        self.imdb_rating = items.get("imDbRating")
        self.imdb_rating_count = items.get("imDbRatingCount")
        self.metacritic_rating = items.get("metacriticRating")
        self.genres = items.get("genres")
        self.genre_list = items.get("genreList")
        #   [
        #     {
        #       "key": "string",
        #       "value": "string"
        #     }
        #   ]
        self.directors = items.get("directors")
        self.director_list = items.get("directorList")
        #   [
        #     {
        #       "id": "string",
        #       "name": "string"
        #     }
        #   ]
        self.start = items.get("stars")
        self.start_list = items.get("starList")
        #   [
        #     {
        #       "id": "string",
        #       "name": "string"
        #     }
        #   ]
