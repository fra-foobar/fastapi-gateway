import pytest
import string
import random


@pytest.fixture
def redis_db(monkeypatch):
    monkeypatch.setenv("REDIS_DB", "2")


@pytest.fixture
def key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


@pytest.fixture(params=[0, 1, 10, 100])
def keys_with_placeholder(request):
    return [f"<placeholder>{x}" for x in range(request.param)]


@pytest.fixture(params=[0, 1, 10, 100, 1000])
def value_string(request):
    """
    Generate random strings of length 0, 1, 10, 100, 1000
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=request.param))


@pytest.fixture(params=[(0, 0), (1, 1), (10, 10)])
def value_dict(request):
    """
    Generate random strings of length 0, 1, 10, 100, 1000
    """
    from random_dict import random_string_dict, random_bool_dict, random_float_dict, random_int_dict
    string_dict = random_string_dict(*request.param)
    bool_dict = random_bool_dict(*request.param)
    float_dict = random_float_dict(*request.param)
    int_dict = random_int_dict(*request.param)

    return {**string_dict, **bool_dict, **float_dict, **int_dict}


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before returning the exit status to the system.
    """
    from api_caching.settings import use_redis
    if use_redis:
        from api_caching.redis.api import flush_db
        import asyncio
        asyncio.run(flush_db())
