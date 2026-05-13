from pydantic import BaseModel, Field
from typing import Optional, List


class UserSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str
    phone: Optional[str] = None
    website: Optional[str] = None

    class Config:
        from_attributes = True


class PostSchema(BaseModel):
    id: int
    user_id: int = Field(alias="userId")
    title: str
    body: str

    class Config:
        from_attributes = True
        populate_by_name = True


class UserPostsSchema(BaseModel):
    user: Optional[UserSchema] = None
    posts: List[PostSchema] = []