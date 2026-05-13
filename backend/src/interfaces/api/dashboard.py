import logging
from fastapi import APIRouter

from src.application.dto import DashboardData
from src.application.use_cases.impl import GetDashboardDataUseCaseImpl
from src.domain.repositories.user_repository import UserRepository
from src.domain.repositories.post_repository import PostRepository

logger = logging.getLogger(__name__)


def create_dashboard_router(
    user_repository: UserRepository,
    post_repository: PostRepository
) -> APIRouter:
    router = APIRouter(prefix="/dashboard", tags=["dashboard"])

    get_dashboard = GetDashboardDataUseCaseImpl(user_repository, post_repository)

    @router.get("/", response_model=DashboardData)
    async def get_dashboard_data():
        logger.info("Fetching dashboard data")
        return await get_dashboard.execute()

    return router