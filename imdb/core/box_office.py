class BoxOfficeCore:
    def __init__(self, items):
        self.items = items
        self.id = items.get("id")
        self.rank = items.get("rank")
        self.title = items.get("title")
        self.image = items.get("image")
        self.weekend = items.get("weekend")
        self.gross = items.get("gross")
        self.weeks = items.get("weeks")
