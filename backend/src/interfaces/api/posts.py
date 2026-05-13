import logging

from fastapi import APIRouter, HTTPException, status

from src.application.dto import PostDTO
from src.application.use_cases.impl import (
    GetPostsUseCaseImpl,
    GetPostByIdUseCaseImpl,
)
from src.domain.repositories.post_repository import PostRepository
from src.interfaces.schemas import PostSchema

logger = logging.getLogger(__name__)


def create_post_router(post_repository: PostRepository) -> APIRouter:
    router = APIRouter(prefix="/posts", tags=["posts"])

    get_posts = GetPostsUseCaseImpl(post_repository)
    get_post = GetPostByIdUseCaseImpl(post_repository)

    @router.get("/", response_model=list[PostSchema], status_code=status.HTTP_200_OK)
    async def list_posts():
        logger.info("Fetching all posts")
        try:
            dtos: list[PostDTO] = await get_posts.execute()
            return [
                PostSchema(id=p.id, user_id=p.user_id, title=p.title, body=p.body)
                for p in dtos
            ]
        except Exception as exc:
            logger.error("Error fetching posts: %s", exc)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to fetch posts",
            ) from exc

    @router.get(
        "/{post_id}", response_model=PostSchema, status_code=status.HTTP_200_OK
    )
    async def get_post_by_id(post_id: int):
        logger.info("Fetching post id=%s", post_id)
        try:
            dto: PostDTO = await get_post.execute(post_id)
            return PostSchema(id=dto.id, user_id=dto.user_id, title=dto.title, body=dto.body)
        except ValueError as exc:
            logger.warning("Post %s not found", post_id)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(exc),
            ) from exc
        except Exception as exc:
            logger.error("Error fetching post %s: %s", post_id, exc)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to fetch post",
            ) from exc

    return router