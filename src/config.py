from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.constants import PROJECT_DESCRIPTION, PROJECT_NAME


class Settings(BaseSettings):
    PROJECT_NAME: str = PROJECT_NAME
    PROJECT_DESCRIPTION: str = PROJECT_DESCRIPTION

    # # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # # e.g: '["http://localhost", "http://localhost:8080"]'  noqa: ERA001
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self) -> str:  # noqa: N802
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='../environment/.env')


settings = Settings()
