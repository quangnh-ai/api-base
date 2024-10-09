from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")

@lru_cache
def get_settings():
    return Settings()