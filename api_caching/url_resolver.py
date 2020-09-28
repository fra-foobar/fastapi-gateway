import hashlib


def string_to_hash(string: str):
    return hashlib.md5(string.encode()).hexdigest()


def get_key_from_url(url: str):
    splitted_url = url.split("/")
    key = ""
    for path_segment in splitted_url:
        key += string_to_hash(path_segment)
    return key
