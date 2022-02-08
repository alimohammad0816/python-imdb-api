class GenreCore:
    def __init__(self, response: dict):
        self.response = response
        self.key = response["key"]
        self.value = response["value"]


class DirectorCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response["id"]
        self.name = response["name"]


class StartCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response["id"]
        self.name = response["name"]


class InTheatersCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response["id"]
        self.title = response["title"]
        self.full_title = response["fullTitle"]
        self.year = response["year"]
        self.release_state = response["releaseState"]
        self.image = response["image"]
        self.runtime_mins = response["runtimeMins"]
        self.runtime_str = response["runtimeStr"]
        self.plot = response["plot"]
        self.content_rating = response["contentRating"]
        self.imdb_rating = response["imDbRating"]
        self.imdb_rating_count = response["imDbRatingCount"]
        self.metacritic_rating = response["metacriticRating"]
        self.genres = response["genres"]
        self.genre_list = [GenreCore(i) for i in response["genreList"]]
        self.directors = response["directors"]
        self.direcor_list = [DirectorCore(i) for i in response["directorList"]]
        self.stars = response["stars"]
        self.star_list = [StartCore(i) for i in response["starList"]]
