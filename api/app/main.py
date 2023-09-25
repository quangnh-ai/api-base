from redis import Redis
from fastapi import FastAPI

from api import router_v1
from config import get_env


app = FastAPI(
    title=get_env.API_TITLE,
    openapi_url=get_env.API_OPENAPI_URL, 
    docs_url=get_env.API_DOCS_URL,
    redoc_url=get_env.API_REDOC_URL
)

app.include_router(
    router_v1.router,
    prefix="/v1",
)