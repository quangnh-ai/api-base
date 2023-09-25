from fastapi import APIRouter
from api.resources.v1.test_api import router as test

router = APIRouter()

router.include_router(test.router, prefix="/test", tags=["V1-Test"])