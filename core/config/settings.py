from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "LightRAG Studio"

    debug: bool = True

    tesseract_cmd: str = ""

    default_provider: str = "mock"

    default_model: str = "mock-model"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()