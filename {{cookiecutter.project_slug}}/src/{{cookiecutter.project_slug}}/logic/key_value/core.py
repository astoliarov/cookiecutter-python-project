from abc import ABC, abstractmethod
from typing import Optional


class IStorage(ABC):
    @abstractmethod
    async def set(self, key: str, value: str, ttl: Optional[int]) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def get(self, key: str) -> Optional[str]:
        raise NotImplementedError()
