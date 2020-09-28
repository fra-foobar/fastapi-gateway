import logging


async def check_if_redis_is_available(hostname):
    import aioredis
    try:
        redis = await aioredis.create_redis(hostname)
        await redis.ping()
        redis.close()
        await redis.wait_closed()
        return True
    except ConnectionRefusedError as e:
        logging.error(f"Can't find a running redis instance for url {hostname}.")
        return False
