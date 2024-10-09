from fastapi import APIRouter
from routers.v1.general import general_router
from routers.v1.user import user_router

v1_router = APIRouter()

v1_router.include_router(general_router, prefix="/general")
v1_router.include_router(user_router, prefix="/user")