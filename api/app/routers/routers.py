from fastapi import APIRouter
from routers.v1.routers import v1_router

routers = APIRouter()

routers.include_router(
    v1_router, prefix='/v1',
    tags=['v1']
)