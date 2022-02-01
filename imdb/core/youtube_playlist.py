class VideoCore:
    def __init__(self, response: dict):
        self.response = response
        self.videoId = response.get("videoId")
        self.title = response.get("title")
        self.description = response.get("description")
        self.duration = response.get("duration")
        self.uploadDate = response.get("uploadDate")
        self.image = response.get("image")
        self.url = response.get("url")


class YouTubePlaylistCore:
    def __init__(self, response: dict):
        self.title = response.get("title")
        self.auhtor = response.get("auhtor")
        self.videos = [VideoCore(v) for v in response.get("videos")]
