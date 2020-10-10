import asyncio
import pytest

static_urls = [
    "/"
    "/api/v1/",
    "api/v1/",
    "/api/v1",
    "api/v1",
    "/api/v1/resource/",
    "api/v1/resource/",
    "/api/v1/resource",
    "api/v1/resource",
    "/api/v1/resource/resource_identifier/",
    "api/v1/resource/resource_identifier/",
    "/api/v1/resource/resource_identifier",
    "api/v1/resource/resource_identifier",
    "/api/v1/resource/resource_identifier/attribute/",
    "api/v1/resource/resource_identifier/attribute/",
    "/api/v1/resource/resource_identifier/attribute",
    "api/v1/resource/resource_identifier/attribute",
    "https://domain.com/api/v1/resource/resource_identifier/attribute/",
    "https://domain.com/api/v1/resource/resource_identifier/attribute",
]


@pytest.mark.parametrize("url", static_urls)
def test_get_from_cache(url, api_call, api_response):
    from cache.main import get_from_cache
    from cache.interface import get, delete
    from cache.url_resolver import get_key_from_url
    key_url = get_key_from_url(url)
    cached_response = asyncio.run(get(key_url))
    assert cached_response is None
    response = get_from_cache(url, api_call)
    assert response == api_response
    cached_response = asyncio.run(get(key_url))
    assert cached_response == api_response
    asyncio.run(delete(key_url))
    cached_response = asyncio.run(get(key_url))
    assert cached_response is None
