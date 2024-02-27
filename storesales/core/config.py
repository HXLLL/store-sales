# core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Grocery Store API"
    DATABASE_URL: str = "sqlite:///./test.db"  # Example for SQLite
    SECRET_KEY: str = "YOUR_SECRET_KEY"  # IMPORTANT: Change this in production!
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Token expiration time

    class Config:
        env_file = ".env"

settings = Settings()
