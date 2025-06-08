from pydantic import BaseSettings

class AuthSettings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_prefix = "AUTH_"

auth_settings = AuthSettings()
