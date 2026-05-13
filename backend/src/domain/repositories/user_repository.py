from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[User]:
        ...

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    async def get_posts(self, user_id: int) -> List[dict]:
        ...