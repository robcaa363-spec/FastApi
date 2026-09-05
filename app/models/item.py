"""
Modelo interno de dominio para 'Item'.

En un proyecto real con base de datos, este archivo tendría el modelo
de SQLAlchemy/SQLModel. Aquí se usa una dataclass simple para que el
proyecto funcione sin depender de una base de datos externa, pero
manteniendo la separación de responsabilidades típica de FastAPI.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Item:
    id: int
    name: str
    description: Optional[str] = None
    price: float = 0.0
    is_active: bool = True
