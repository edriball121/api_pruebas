from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class UserDTO:
    id: Optional[int] = None
    name: str = ""
    username: str = ""
    email: str = ""
    phone: str = ""
    website: str = ""


@dataclass
class PostDTO:
    id: Optional[int] = None
    user_id: Optional[int] = None
    title: str = ""
    body: str = ""


@dataclass
class UserPostsDTO:
    user: Optional[UserDTO] = None
    posts: List[PostDTO] = field(default_factory=list)


@dataclass
class ErrorDTO:
    code: int
    message: str
    detail: Optional[str] = None