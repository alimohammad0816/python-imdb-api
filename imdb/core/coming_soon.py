class GenreCore:
    def __init__(self, response: dict):
        self.response = response
        self.key = response.get("key")
        self.value = response.get("value")


class DirectoreCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response.get("id")
        self.name = response.get("name")


class StarCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response.get("id")
        self.name = response.get("name")


class ComingSoonCore:
    def __init__(self, response) -> None:
        self.response = response
        self.id = response.get("id")
        self.title = response.get("title")
        self.full_title = response.get("fullTitle")
        self.year = response.get("year")
        self.release_state = response.get("releaseState")
        self.image = response.get("image")
        self.runtime_mins = response.get("runtimeMins")
        self.runtime_str = response.get("runtimeStr")
        self.plot = response.get("plot")
        self.content_rating = response.get("contentRating")
        self.imdb_rating = response.get("imDbRating")
        self.imdb_rating_count = response.get("imDbRatingCount")
        self.metacritic_rating = response.get("metacriticRating")
        self.genres = response.get("genres")
        self.genre_list = [GenreCore(g) for g in response.get("genreList")]
        self.directors = response.get("directors")
        self.director_list = [DirectoreCore(d) for d in response.get("directorList")]
        self.stars = response.get("stars")
        self.star_list = [StarCore(s) for s in response.get("starList")]
