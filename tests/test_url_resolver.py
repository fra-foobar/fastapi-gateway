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

pattern_urls = [
    "/"
    "/api/v1/*",
    "api/v1/*",
    "/api/v1/*/",
    "api/v1/*/",
    "/api/v1/resource/*/",
    "api/v1/resource/*",
    "/api/v1/resource/*/attribute/",
    "api/v1/resource/*/attribute/",
    "/api/v1/resource/*/attribute",
    "api/v1/resource/*/attribute",
    "https://domain.com/api/v1/*/resource_identifier/*/",
    "https://domain.com/api/v1/*/resource_identifier/*",
]

domains_only_urls = [
    "https://domain.com/",
    "https://domain.com",
]


def test_resolve_empty_url(redis_db):
    from api_caching.url_resolver import get_key_from_url
    url = ""
    key = get_key_from_url(url)
    assert key == ""


@pytest.mark.parametrize("url", domains_only_urls)
def test_resolve_empty_path_url(redis_db, url):
    from api_caching.url_resolver import get_key_from_url
    key = get_key_from_url(url)
    assert key == ""


@pytest.mark.parametrize("url", static_urls)
def test_resolve_static_url(redis_db, url):
    from api_caching.url_resolver import get_key_from_url
    key = get_key_from_url(url)
    assert "/" not in key


@pytest.mark.parametrize("url", pattern_urls)
def test_resolve_pattern_url(redis_db, url):
    from api_caching.url_resolver import get_key_from_url
    key = get_key_from_url(url)
    assert "/" not in key
    assert "*" in key
