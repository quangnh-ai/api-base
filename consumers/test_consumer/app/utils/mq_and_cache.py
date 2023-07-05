from redis import Redis
from config import get_env

cache = Redis(
    host=get_env.REDIS_HOST,
    port=get_env.REDIS_PORT,
    password=get_env.REDIS_PASSWORD,
    db=get_env.REDIS_DB
)

