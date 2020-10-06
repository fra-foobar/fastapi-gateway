class NoCacheFoundException(Exception):
    def __init__(self):
        super().__init__("It isn't been possible to connect to any cache. Please check you have your cache running.")
