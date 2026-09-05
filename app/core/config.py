"""
Configuración centralizada de la aplicación.

Usa pydantic-settings para leer variables de entorno (o un archivo .env).
Así toda la configuración vive en un solo lugar y es fácil de testear
o cambiar entre entornos (dev, staging, prod).
"""

from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Modular App"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # Orígenes permitidos para CORS (separa con comas en el .env)
    CORS_ORIGINS: List[str] = ["*"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
