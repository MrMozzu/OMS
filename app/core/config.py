from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str

    pool_size: int = 10
    max_overflow: int = 20
    pool_timeout: int = 30
    pool_pre_ping: bool = True
    pool_recycle: int = 1800

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()

# note :
""" 
    every thing in .env is text, pydantic converts it into the type mentioned in the settings class
"""
