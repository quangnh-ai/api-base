from fastapi import APIRouter
import json

from routers.test_router import api as test_router_api
from utils.mq_and_cache import cache

routers = APIRouter()

routers.include_router(
    test_router_api.router,
    prefix='/test',
    tags=['Test']
)