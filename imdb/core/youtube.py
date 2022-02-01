class VideoCore:
    def __init__(self, response: dict):
        self.response = response
        self.quality = response.get("quality")
        self.mimeType = response.get("mimeType")
        self.extension = response.get("extension")
        self.url = response.get("url")


class YouTubeCore:
    def __init__(self, response: dict):
        self.response = response
        self.videoId = response.get("videoId")
        self.title = response.get("title")
        self.description = response.get("description")
        self.duration = response.get("duration")
        self.uploadDate = response.get("uploadDate")
        self.image = response.get("image")
        self.videos = [VideoCore(v) for v in response.get("videos")]
