class BoxOfficeAllCore:
    def __init__(self, response) -> None:
        self.response = response
        self.id = response.get("id")
        self.rank = response.get("rank")
        self.title = response.get("title")
        self.world_wide_life_time_gross = response.get("worldwideLifetimeGross")
        self.domestic_life_time_gross = response.get("domesticLifetimeGross")
        self.domestic = response.get("domestic")
        self.foreign_life_time_gross = response.get("foreignLifetimeGross")
        self.foreign = response.get("foreign")
        self.year = response.get("year")
