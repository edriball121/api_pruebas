from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.infrastructure.repositories.jsonplaceholder_user_repository import JsonPlaceholderUserRepository
from src.infrastructure.repositories.jsonplaceholder_post_repository import JsonPlaceholderPostRepository
from src.interfaces.api.users import create_user_router
from src.interfaces.api.posts import create_post_router
from src.interfaces.api.dashboard import create_dashboard_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Clean Architecture API",
    description="API con FastAPI siguiendo Clean Architecture",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_repository = JsonPlaceholderUserRepository()
post_repository = JsonPlaceholderPostRepository()

app.include_router(create_user_router(user_repository, post_repository), prefix="/api")
app.include_router(create_post_router(post_repository), prefix="/api")
app.include_router(create_dashboard_router(user_repository, post_repository), prefix="/api")

@app.get("/")
async def root():
    return {"message": "API funcionando", "docs": "/docs"}