class GenreCore:
    def __init__(self, items: dict):
        self.items = items
        self.key = items["key"]
        self.value = items["value"]


class DirectorCore:
    def __init__(self, items: dict):
        self.items = items
        self.id = items["id"]
        self.name = items["name"]


class StartCore:
    def __init__(self, items: dict):
        self.items = items
        self.id = items["id"]
        self.name = items["name"]


class InTheatersCore:
    def __init__(self, items: dict):
        self.items = items
        self.id = items["id"]
        self.title = items["title"]
        self.full_title = items["fullTitle"]
        self.year = items["year"]
        self.release_state = items["releaseState"]
        self.image = items["image"]
        self.runtime_mins = items["runtimeMins"]
        self.runtime_str = items["runtimeStr"]
        self.plot = items["plot"]
        self.content_rating = items["contentRating"]
        self.imdb_rating = items["imDbRating"]
        self.imdb_rating_count = items["imDbRatingCount"]
        self.metacritic_rating = items["metacriticRating"]
        self.genres = items["genres"]
        self.genre_list = [GenreCore(i) for i in items["genreList"]]
        self.directors = items["directors"]
        self.direcor_list = [DirectorCore(i) for i in items["directorList"]]
        self.stars = items["stars"]
        self.star_list = [StartCore(i) for i in items["starList"]]
