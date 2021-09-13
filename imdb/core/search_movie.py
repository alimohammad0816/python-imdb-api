class SearchMovieCore:
    def __init__(self, items: dict) -> None:
        self.items = items
        self.id = items.get("id")
        self.result_type = items.get("resultType")
        self.image = items.get("image")
        self.title = items.get("title")
        self.description = items.get("description")
