import pytest
from starlette.testclient import TestClient

from {{cookiecutter.project_slug}}.api.core import build_api


@pytest.fixture
def application():
    return build_api()


@pytest.fixture
def test_client(application):
    return TestClient(application)


def test__get__set__expected_value(test_client):
    build_url = "/api/v1/kv"

    key = "test"
    value = "test_value"

    request = {"key": key, "value": value, "ttl": None}

    response = test_client.post(build_url, json=request)

    assert response.status_code == 200
    assert response.json() == {"key": key, "value": value, "ttl": None}
