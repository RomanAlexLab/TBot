# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8"
    )
    
    TELEGRAM_BOT_TOKEN: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DEBUG: bool = False


# Создаём экземпляр конфига
config = Settings()


if __name__ == "__main__":
    print(config.TELEGRAM_BOT_TOKEN)