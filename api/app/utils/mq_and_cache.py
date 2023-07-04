from redis import Redis
from celery import Celery

from config import get_env

cache = Redis(
    host=get_env.REDIS_HOST,
    port=get_env.REDIS_PORT,
    db=get_env.REDIS_DB,
    password=get_env.REDIS_PASSWORD
)

celecry_excutor = Celery(
    broker=get_env.RABBITMQ_LINK,
    backend=get_env.REDIS_LINK
)