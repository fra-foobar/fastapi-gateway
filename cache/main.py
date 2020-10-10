import asyncio
from typing import Callable
from cache.interface import get, set, delete_matching
from cache.url_resolver import get_key_from_url


def get_from_cache(url_request: str, api_call: Callable):
    """
    Checks if the cache already contains a value associated to the given url. In case the value is not in the cache
    it calls the 'api_call' function to retrieve the value from the API, and later store it to the cache.
    :param url_request: a string representing the url to call
    :param api_call: a function which performs the actual API call
    :return: a dictionary containing the API response
    """
    url_key = get_key_from_url(url_request)
    cached_response = asyncio.run(get(url_key))
    if cached_response is None:
        response = api_call()
        asyncio.run(set(url_key, response))
    else:
        response = cached_response
    return response


def delete_from_cache(url_request: str):
    """
    Delete the content of the cache related to the given url. If the given url contains a '*', it delete all the
    matching keys in the cache.
    :param url_request: a string representing the url to delete from the cache
    """
    asyncio.run(delete_matching(url_request))
