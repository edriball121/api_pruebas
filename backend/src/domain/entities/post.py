from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Post:
    id: Optional[int] = None
    user_id: Optional[int] = None
    title: str = ""
    body: str = ""