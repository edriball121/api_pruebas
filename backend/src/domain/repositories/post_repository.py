from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.post import Post


class PostRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Post]:
        ...

    @abstractmethod
    async def get_by_id(self, post_id: int) -> Optional[Post]:
        ...

    @abstractmethod
    async def get_by_user_id(self, user_id: int) -> List[Post]:
        ...