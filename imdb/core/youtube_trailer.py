class YouTubeTrailerCore:
    def __init__(self, response):
        self.response = response
        self.imDbId = response.get("imDbId")
        self.title = response.get("title")
        self.fullTitle = response.get("fullTitle")
        self.type = response.get("type")
        self.year = response.get("year")
        self.videoId = response.get("videoId")
        self.videoUrl = response.get("videoUrl")
