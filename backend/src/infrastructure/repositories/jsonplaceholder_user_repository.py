import httpx
from typing import List, Optional

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository


class JsonPlaceholderUserRepository(UserRepository):
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self._base_url = base_url

    async def get_all(self) -> List[User]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self._base_url}/users")
            response.raise_for_status()
            data = response.json()
            return [self._map_to_user(item) for item in data]

    async def get_by_id(self, user_id: int) -> Optional[User]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self._base_url}/users/{user_id}")
            if response.status_code == 404:
                return None
            response.raise_for_status()
            data = response.json()
            return self._map_to_user(data)

    async def get_posts(self, user_id: int) -> List[dict]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self._base_url}/posts", params={"userId": user_id})
            response.raise_for_status()
            return response.json()

    @staticmethod
    def _map_to_user(data: dict) -> User:
        return User(
            id=data["id"],
            name=data["name"],
            username=data["username"],
            email=data["email"],
            phone=data.get("phone", ""),
            website=data.get("website", ""),
            address_street=data.get("address", {}).get("street", ""),
            address_suite=data.get("address", {}).get("suite", ""),
            address_city=data.get("address", {}).get("city", ""),
            address_zipcode=data.get("address", {}).get("zipcode", ""),
            address_geo_lat=data.get("address", {}).get("geo", {}).get("lat", ""),
            address_geo_lng=data.get("address", {}).get("geo", {}).get("lng", ""),
            company_name=data.get("company", {}).get("name", ""),
            company_catch_phrase=data.get("company", {}).get("catchPhrase", ""),
            company_bs=data.get("company", {}).get("bs", ""),
        )