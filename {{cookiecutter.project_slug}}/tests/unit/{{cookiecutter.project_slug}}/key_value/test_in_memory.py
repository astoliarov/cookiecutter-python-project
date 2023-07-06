import asyncio

from {{cookiecutter.project_slug}}.logic.key_value.in_memory import InMemoryStorage


async def test__InMemoryStorage__set_value__get_value__expected_result():
    key = "test"
    value = "test_value"

    storage = InMemoryStorage()

    await storage.set(key=key, value=value, ttl=None)

    assert await storage.get(key=key) == value


async def test__InMemoryStorage__set_value_ttl__get_value_timeout__None():
    key = "test"
    value = "test_value"

    storage = InMemoryStorage()

    await storage.set(key=key, value=value, ttl=0)

    await asyncio.sleep(0.5)

    assert await storage.get(key=key) is None
