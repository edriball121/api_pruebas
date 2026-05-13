import httpx
from typing import List, Optional

from src.domain.entities.post import Post
from src.domain.repositories.post_repository import PostRepository


class JsonPlaceholderPostRepository(PostRepository):
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self._base_url = base_url

    async def get_all(self) -> List[Post]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self._base_url}/posts")
            response.raise_for_status()
            data = response.json()
            return [self._map_to_post(item) for item in data]

    async def get_by_id(self, post_id: int) -> Optional[Post]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self._base_url}/posts/{post_id}")
            if response.status_code == 404:
                return None
            response.raise_for_status()
            data = response.json()
            return self._map_to_post(data)

    async def get_by_user_id(self, user_id: int) -> List[Post]:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self._base_url}/posts", params={"userId": user_id}
            )
            response.raise_for_status()
            data = response.json()
            return [self._map_to_post(item) for item in data]

    @staticmethod
    def _map_to_post(data: dict) -> Post:
        return Post(
            id=data["id"],
            user_id=data["userId"],
            title=data["title"],
            body=data["body"],
        )