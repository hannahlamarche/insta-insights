from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_database: str = "insta-insights"
    test_mongodb_database: Optional[str] = "test_insta_insights"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
