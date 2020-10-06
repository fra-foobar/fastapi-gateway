import asyncio
import pytest


def test_no_cache_available(redis_db, redis_db_missing_port):
    from cache.exceptions import NoCacheFoundException
    with pytest.raises(NoCacheFoundException):
        from cache.interface import get, set
        asyncio.run(set("key", "value_string"))
        returned_value = asyncio.run(get("key"))
        assert returned_value == "value_string"


def test_get_set_string(redis_db, key, value_string):
    from cache.interface import get, set
    asyncio.run(set(key, value_string))
    returned_value = asyncio.run(get(key))
    assert returned_value == value_string


def test_get_set_dict(redis_db, key, value_dict):
    from cache.interface import get, set
    asyncio.run(set(key, value_dict))
    returned_value = asyncio.run(get(key))
    assert returned_value == value_dict


def test_delete_string(redis_db, key, value_string):
    from cache.interface import delete, get, set
    asyncio.run(set(key, value_string))
    returned_value = asyncio.run(get(key))
    assert returned_value == value_string
    asyncio.run(delete(key))
    returned_value = asyncio.run(get(key))
    assert returned_value is None


def test_delete_dict(redis_db, key, value_dict):
    from cache.interface import delete, get, set
    asyncio.run(set(key, value_dict))
    returned_value = asyncio.run(get(key))
    assert returned_value == value_dict
    asyncio.run(delete(key))
    returned_value = asyncio.run(get(key))
    assert returned_value is None


def test_delete_matching_string(redis_db, key, keys_with_placeholder, value_string):
    from cache.interface import delete_matching, get, set
    keys = [key_with_placeholder.replace('<placeholder>', key) for key_with_placeholder in keys_with_placeholder]
    keys_to_leave = [
        key_with_placeholder.replace('<placeholder>', 'leave_this_') for key_with_placeholder in keys_with_placeholder
    ]
    for k in keys + keys_to_leave:
        asyncio.run(set(k, value_string))
        returned_value = asyncio.run(get(k))
        assert returned_value == value_string
    asyncio.run(delete_matching(f"{key}*"))
    for k in keys:
        returned_value = asyncio.run(get(k))
        assert returned_value is None
    for k in keys_to_leave:
        returned_value = asyncio.run(get(k))
        assert returned_value == value_string
    asyncio.run(delete_matching(f"leave_this_*"))
    for k in keys_to_leave:
        returned_value = asyncio.run(get(k))
        assert returned_value is None
