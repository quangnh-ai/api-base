from redis import Redis
from fastapi import FastAPI

from routers import api_routers
from config import get_env


app = FastAPI(
    title=get_env.API_TITLE,
    openapi_url=get_env.API_OPENAPI_URL, 
    docs_url=get_env.API_DOCS_URL,
    redoc_url=get_env.API_REDOC_URL
)

app.include_router(
    api_routers.routers
)