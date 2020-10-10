from urllib.parse import urlparse


def get_key_from_url(url: str):
    url_path = urlparse(url).path.strip("/")
    key = url_path.replace("/", ":")
    query_params = urlparse(url).query
    if len(query_params) != 0:
        key += ":" + query_params
    return key
