from abc import ABC, abstractmethod


class ExternalAPIService(ABC):
    @abstractmethod
    async def get(self, url: str) -> dict:
        ...

    @abstractmethod
    async def get_list(self, url: str) -> list:
        ...