class ErrorMessage:
    invalid_api_key = "Invalid API Key"


class Error(Exception):
    pass


class InvalidApiKey(Error):
    def __init__(self):
        self.message = "Invalid API Key"

    def __str__(self):
        return self.message


class NotFound(Error):
    def __init__(self):
        self.message = "Movie or Series Not Found."

    def __str__(self):
        return self.message
