import os
import asyncio
import importlib
from cache.constants import DEFAULT_CACHING_TOOL, REDIS_CACHING_TOOL
from cache.utils.cache_adapters import check_if_redis_is_available

CACHING_TOOL = os.environ.get("CACHING_TOOL", DEFAULT_CACHING_TOOL)

REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_DB = os.environ.get("REDIS_DB", 1)
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

use_redis = asyncio.run(check_if_redis_is_available(REDIS_URL)) and CACHING_TOOL == REDIS_CACHING_TOOL

cache_module = None

if use_redis:
    cache_module = importlib.import_module('cache.redis.api')
