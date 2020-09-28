from api_caching.settings import cache_module as cache
from api_caching.exceptions import NoCacheFoundException

if cache is None:
    raise NoCacheFoundException()


async def get(key: str):
    """
    Return the cache value corresponding to the key passed as argument.
    :param key: key to search for in the cache
    :return: a cached value.
    """
    value = await cache.get(key)
    return value


async def set(key: str, value: object):
    """
    Write to the cache the key-value pair passed as args.
    :param key: key to put in the cache
    :param value: value to save in the cache
    :return: a cached value.
    """
    await cache.set(key, value)


async def delete(key: str):
    """
    Delete from the cache the key passed as args.
    :param key: key to put in the cache
    """
    await cache.delete(key)


async def delete_matching(key_pattern: str):
    """
    Delete all keys from the redis cache which matches the key passed as argument.
    :param key_pattern: expression to match. '*' means every string.
    """
    await cache.delete_matching(key_pattern)
