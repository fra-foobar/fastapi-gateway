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

url_query_params = [
    "q1=iojoi3j12io3j12oi3j",
    "q1=iojoi3j12io3j12oi3j&q2=2oi3j",
    "q1=iojoi3j12io3j12oi3j&q2=2oi3j&q3=kfjahsdflkjsahd",
]


def test_resolve_empty_url(redis_db):
    from cache.url_resolver import get_key_from_url
    url = ""
    key = get_key_from_url(url)
    assert key == ""


@pytest.mark.parametrize("url", domains_only_urls)
def test_resolve_empty_path_url(redis_db, url):
    from cache.url_resolver import get_key_from_url
    key = get_key_from_url(url)
    assert key == ""


@pytest.mark.parametrize("url", static_urls)
def test_resolve_static_url(redis_db, url):
    from cache.url_resolver import get_key_from_url
    key = get_key_from_url(url)
    assert "/" not in key


@pytest.mark.parametrize("url", pattern_urls)
def test_resolve_pattern_url(redis_db, url):
    from cache.url_resolver import get_key_from_url
    key = get_key_from_url(url)
    assert "/" not in key
    assert "*" in key


@pytest.mark.parametrize("url", static_urls)
@pytest.mark.parametrize("query_params", url_query_params)
def test_resolve_query_params_url(redis_db, url, query_params):
    from cache.url_resolver import get_key_from_url
    url_with_query_params = url + "?" + query_params
    key = get_key_from_url(url_with_query_params)
    assert "/" not in key
    assert key.split(":")[-1] == query_params
