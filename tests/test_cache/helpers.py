import aioredis
from cache.settings import REDIS_URL


async def flush_db():
    """
    Flush all the keys in redis db to which the client is connected.
    """
    conn = await aioredis.create_connection(REDIS_URL, encoding='utf-8')
    value = await conn.execute('FLUSHDB')
    conn.close()
    await conn.wait_closed()