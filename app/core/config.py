from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "ZeroTouch AppSec Cloud"
    DATABASE_URL: str = "sqlite:///./zerotouch.db"

    SECRET_KEY: str = "ChangeThisToAVeryLongRandomSecretKey123456789"

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
