import logging

from fastapi import APIRouter, HTTPException, status

from src.application.dto import UserDTO, PostDTO, UserPostsDTO
from src.application.use_cases.impl import (
    GetUsersUseCaseImpl,
    GetUserByIdUseCaseImpl,
    GetPostsUseCaseImpl,
    GetPostByIdUseCaseImpl,
    GetUserPostsUseCaseImpl,
)
from src.domain.repositories.user_repository import UserRepository
from src.domain.repositories.post_repository import PostRepository
from src.interfaces.schemas import UserSchema, PostSchema, UserPostsSchema

logger = logging.getLogger(__name__)


def create_user_router(
    user_repository: UserRepository,
    post_repository: PostRepository,
) -> APIRouter:
    router = APIRouter(prefix="/users", tags=["users"])

    get_users = GetUsersUseCaseImpl(user_repository)
    get_user = GetUserByIdUseCaseImpl(user_repository)
    get_user_posts = GetUserPostsUseCaseImpl(user_repository, post_repository)

    @router.get("/", response_model=list[UserSchema], status_code=status.HTTP_200_OK)
    async def list_users():
        logger.info("Fetching all users")
        try:
            dtos: list[UserDTO] = await get_users.execute()
            return [
                UserSchema(
                    id=d.id, name=d.name, username=d.username,
                    email=d.email, phone=d.phone, website=d.website,
                )
                for d in dtos
            ]
        except Exception as exc:
            logger.error("Error fetching users: %s", exc)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to fetch users",
            ) from exc

    @router.get(
        "/{user_id}", response_model=UserSchema, status_code=status.HTTP_200_OK
    )
    async def get_user_by_id(user_id: int):
        logger.info("Fetching user id=%s", user_id)
        try:
            dto: UserDTO = await get_user.execute(user_id)
            return UserSchema(
                id=dto.id, name=dto.name, username=dto.username,
                email=dto.email, phone=dto.phone, website=dto.website,
            )
        except ValueError as exc:
            logger.warning("User %s not found", user_id)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(exc),
            ) from exc
        except Exception as exc:
            logger.error("Error fetching user %s: %s", user_id, exc)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to fetch user",
            ) from exc

    @router.get(
        "/{user_id}/posts",
        response_model=UserPostsSchema,
        status_code=status.HTTP_200_OK,
    )
    async def get_posts_for_user(user_id: int):
        logger.info("Fetching posts for user id=%s", user_id)
        try:
            dto: UserPostsDTO = await get_user_posts.execute(user_id)
            return UserPostsSchema(
                user=UserSchema(
                    id=dto.user.id,
                    name=dto.user.name,
                    username=dto.user.username,
                    email=dto.user.email,
                    phone=dto.user.phone,
                    website=dto.user.website,
                ) if dto.user else None,
                posts=[
                    PostSchema(
                        id=p.id, user_id=p.user_id, title=p.title, body=p.body,
                    )
                    for p in dto.posts
                ],
            )
        except ValueError as exc:
            logger.warning("User %s not found for posts", user_id)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(exc),
            ) from exc
        except Exception as exc:
            logger.error("Error fetching posts for user %s: %s", user_id, exc)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to fetch user posts",
            ) from exc

    return router