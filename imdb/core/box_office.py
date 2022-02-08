class BoxOfficeCore:
    def __init__(self, response):
        self.response = response
        self.id = response.get("id")
        self.rank = response.get("rank")
        self.title = response.get("title")
        self.image = response.get("image")
        self.weekend = response.get("weekend")
        self.gross = response.get("gross")
        self.weeks = response.get("weeks")
