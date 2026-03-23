from pathlib import Path
from pydantic_settings import BaseSettings
from functools import lru_cache

_BACKEND_DIR = Path(__file__).resolve().parent.parent.parent
_ENV_FILE = str(_BACKEND_DIR / ".env")


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/mathquest"
    JWT_SECRET: str = "your-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_HOURS: int = 24
    TEACHER_REGISTER_CODE: str = "MATHQUEST2026"

    class Config:
        env_file = _ENV_FILE
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
