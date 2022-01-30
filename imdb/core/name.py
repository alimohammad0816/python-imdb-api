class KnownForCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response.get("id")
        self.title = response.get("title")
        self.fullTitle = response.get("fullTitle")
        self.year = response.get("year")
        self.role = response.get("role")
        self.image = response.get("image")


class CastMoviesCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response.get("id")
        self.role = response.get("role")
        self.title = response.get("title")
        self.year = response.get("year")
        self.description = response.get("description")


class NamePersonCore:
    def __init__(self, response: dict):
        self.id = response.get("id")
        self.name = response.get("name")
        self.role = response.get("role")
        self.image = response.get("image")
        self.summary = response.get("summary")
        self.birth_date = response.get("birthDate")
        self.death_date = response.get("deathDate")
        self.awards = response.get("awards")
        self.height = response.get("height")
        self.known_for = [KnownForCore(k) for k in response.get("knownFor")]
        self.cast_movies = [
            CastMoviesCore(c) for c in response.get("castMovies")
        ]
