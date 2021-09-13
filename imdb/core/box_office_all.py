class BoxOfficeAllCore:
    def __init__(self, items) -> None:
        self.items = items
        self.id = items.get("id")
        self.rank = items.get("rank")
        self.title = items.get("title")
        self.world_wide_life_time_gross = items.get("worldwideLifetimeGross")
        self.domestic_life_time_gross = items.get("domesticLifetimeGross")
        self.domestic = items.get("domestic")
        self.foreign_life_time_gross = items.get("foreignLifetimeGross")
        self.foreign = items.get("foreign")
        self.year = items.get("year")
