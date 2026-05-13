import httpx


class HttpService:
    def __init__(self, base_url: str, timeout: float = 10.0):
        self._base_url = base_url
        self._timeout = timeout
        self._client = httpx.AsyncClient(
            base_url=base_url, timeout=httpx.Timeout(timeout)
        )

    async def get(self, path: str) -> dict:
        response = await self._client.get(path)
        response.raise_for_status()
        return response.json()

    async def get_list(self, path: str) -> list:
        response = await self._client.get(path)
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self._client.aclose()