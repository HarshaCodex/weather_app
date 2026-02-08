class WeatherException(Exception):
    def __init__(self, errorCode, errorMsg):
        self.errorCode = errorCode
        self.errorMsg = errorMsg

    def __str__(self):
        return f"Exception occurred with errorCode:{self.errorCode}, errorMessage:{self.errorMsg}"