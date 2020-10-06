import aioredis
import marshal
from cache.settings import REDIS_URL


async def get(key: str):
    """
    Return the cache value corresponding to the key passed as argument.
    :param key: key to search for in the cache
    :return: a cached value.
    """
    conn = await aioredis.create_connection(REDIS_URL)
    value = await conn.execute('GET', key)
    conn.close()
    await conn.wait_closed()
    if value is not None:
        value = marshal.loads(value)
    return value


async def set(key: str, value: object):
    """
    Write to the cache the key-value pair passed as args.
    :param key: key to put in the cache
    :param value: value to save in the cache
    :return: a cached value.
    """
    conn = await aioredis.create_connection(REDIS_URL)
    await conn.execute('SET', key, marshal.dumps(value))
    conn.close()
    await conn.wait_closed()


async def delete(key: str):
    """
    Delete from the cache the key passed as args.
    :param key: key to put in the cache
    """
    conn = await aioredis.create_connection(REDIS_URL)
    await conn.execute('DEL', key)
    conn.close()
    await conn.wait_closed()


async def delete_matching(key_pattern: str):
    """
    Delete all keys from the redis cache which matches the key passed as argument.
    :param key_pattern: expression to match. '*' means every string.
    """
    conn = await aioredis.create_connection(REDIS_URL)
    cur = b'0'  # set initial cursor to 0

    while cur:
        cur, keys = await conn.execute('SCAN', cur, 'MATCH', key_pattern)
        cur = int(cur)
        if len(keys) > 0:
            await conn.execute('DEL', *keys)

    conn.close()
    await conn.wait_closed()
