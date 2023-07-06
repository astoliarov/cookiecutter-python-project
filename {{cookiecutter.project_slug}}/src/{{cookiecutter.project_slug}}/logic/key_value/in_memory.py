from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

from {{cookiecutter.project_slug}}.logic.key_value.core import IStorage


@dataclass
class StorageItem:
    value: str
    deadline_dt: Optional[datetime] = None


class InMemoryStorage(IStorage):
    def __init__(self) -> None:
        self._storage: dict[str, StorageItem] = {}

    async def set(self, key: str, value: str, ttl: Optional[int]) -> None:
        deadline_dt = None
        if ttl is not None:
            deadline_dt = datetime.now() + timedelta(seconds=ttl)

        item = StorageItem(value=value, deadline_dt=deadline_dt)
        self._storage[key] = item

    async def get(self, key: str) -> Optional[str]:
        item = self._storage.get(key)

        if item is None:
            return None

        if item.deadline_dt and item.deadline_dt < datetime.now():
            return None

        return item.value
