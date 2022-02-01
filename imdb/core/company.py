class ItemCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response.get("id")
        self.title = response.get("title")
        self.year = response.get("year")
        self.image = response.get("image")
        self.imDbRating = response.get("imDbRating")


class CompanyCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response.get("id")
        self.name = response.get("name")
        self.items = [ItemCore(res) for res in response.get("items")]
