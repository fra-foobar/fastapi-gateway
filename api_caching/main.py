from typing import Callable
from api_caching.interface import get, set


def get_from_cache(url_request: str, api_call: Callable):
    cached_response = get(url_request)
