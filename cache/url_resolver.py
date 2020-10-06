from urllib.parse import urlparse


def get_key_from_url(url: str):
    url_path = urlparse(url).path.strip("/")
    key = url_path.replace("/", ":")
    return key
