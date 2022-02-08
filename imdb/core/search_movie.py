class SearchMovieCore:
    def __init__(self, response: dict) -> None:
        self.response = response
        self.id = response.get("id")
        self.result_type = response.get("resultType")
        self.image = response.get("image")
        self.title = response.get("title")
        self.description = response.get("description")
