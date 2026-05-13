from typing import List

from src.application.dto import UserDTO, PostDTO, UserPostsDTO
from src.domain.repositories.user_repository import UserRepository

class GetUsersUseCaseImpl:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def execute(self) -> List[UserDTO]:
        users = await self._user_repository.get_all()
        return [
            UserDTO(
                id=u.id,
                name=u.name,
                username=u.username,
                email=u.email,
                phone=u.phone,
                website=u.website,
            )
            for u in users
        ]


class GetUserByIdUseCaseImpl:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def execute(self, user_id: int) -> UserDTO:
        user = await self._user_repository.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        return UserDTO(
            id=user.id,
            name=user.name,
            username=user.username,
            email=user.email,
            phone=user.phone,
            website=user.website,
        )


class GetPostsUseCaseImpl:
    def __init__(self, post_repository):
        self._post_repository = post_repository

    async def execute(self) -> List[PostDTO]:
        posts = await self._post_repository.get_all()
        return [
            PostDTO(
                id=p.id,
                user_id=p.user_id,
                title=p.title,
                body=p.body,
            )
            for p in posts
        ]


class GetPostByIdUseCaseImpl:
    def __init__(self, post_repository):
        self._post_repository = post_repository

    async def execute(self, post_id: int) -> PostDTO:
        post = await self._post_repository.get_by_id(post_id)
        if not post:
            raise ValueError(f"Post with id {post_id} not found")
        return PostDTO(
            id=post.id,
            user_id=post.user_id,
            title=post.title,
            body=post.body,
        )


class GetUserPostsUseCaseImpl:
    def __init__(self, user_repository: UserRepository, post_repository):
        self._user_repository = user_repository
        self._post_repository = post_repository

    async def execute(self, user_id: int) -> UserPostsDTO:
        user = await self._user_repository.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        posts = await self._post_repository.get_by_user_id(user_id)
        return UserPostsDTO(
            user=UserDTO(
                id=user.id,
                name=user.name,
                username=user.username,
                email=user.email,
                phone=user.phone,
                website=user.website,
            ),
            posts=[
                PostDTO(
                    id=p["id"],
                    user_id=p["userId"],
                    title=p["title"],
                    body=p["body"],
                )
                for p in posts
            ],
        )


from src.application.dto import UserStats, PostStats, DashboardData
from src.domain.repositories.user_repository import UserRepository as UserRepo
from src.domain.repositories.post_repository import PostRepository as PostRepo


class GetDashboardDataUseCaseImpl:
    def __init__(self, user_repository: UserRepo, post_repository: PostRepo):
        self._user_repository = user_repository
        self._post_repository = post_repository

    async def execute(self) -> DashboardData:
        users = await self._user_repository.get_all()
        posts = await self._post_repository.get_all()

        user_stats = [
            UserStats(
                id=u.id,
                name=u.name,
                username=u.username,
                email=u.email,
                post_count=sum(1 for p in posts if p.user_id == u.id)
            )
            for u in users
        ]

        recent_posts = [
            PostStats(
                id=p.id,
                user_id=p.user_id,
                title=p.title,
                body=p.body
            )
            for p in posts[:10]
        ]

        user_distribution = {
            u.username: sum(1 for p in posts if p.user_id == u.id)
            for u in users
        }

        return DashboardData(
            total_users=len(users),
            total_posts=len(posts),
            total_comments=0,
            users=user_stats,
            recent_posts=recent_posts,
            user_distribution=user_distribution
        )