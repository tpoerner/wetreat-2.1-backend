from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "WeTreat Backend"
    ALLOWED_ORIGINS: str = "*"

    class Config:
        env_file = ".env"

settings = Settings()
