class NamePersonCore:
    def __init__(self, response) -> None:
        self.cast_movie = response.get()
        self.id = response.get("id")
        self.name = response.get("name")
        self.role = response.get("role")
        self.image = response.get("image")
        self.summary = response.get("summary")
        self.birth_date = response.get("birthDate")
        self.death_date = response.get("deathDate")
        self.awards = response.get("awards")
        self.height = response.get("height")
        self.known_for = response.get("knownFor")
        # todo : change knownfor to Movie Object
        # [{
        # "id": "string",
        # "title": "string",
        # "fullTitle": "string",
        # "year": "string",
        # "role": "string",
        # "image": "string"
        # }]
        self.cast_movies = response.get("castMovies")
        # todo : change cast movies to Movie object
        # [{
        #     "id": "string", "role": "string",
        #     "title": "string", "year": "string",
        #     "description": "string"
        # }]