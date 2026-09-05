"""
Punto de entrada de la aplicación FastAPI.

Aquí solo se crea la instancia de la app, se registran los routers
(módulos) y los middlewares/eventos globales. La lógica de negocio
vive en otros módulos (services, models, schemas, api).
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api import items, health


def create_app() -> FastAPI:
    """Factory de la aplicación (útil para tests y para reutilizar config)."""
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="API modular de ejemplo construida con FastAPI",
    )

    # CORS (ajusta origins según tu frontend)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Registro de routers (cada uno es un módulo independiente)
    app.include_router(health.router)
    app.include_router(items.router)

    return app


app = create_app()
