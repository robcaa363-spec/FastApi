"""
Esquemas Pydantic (contratos de entrada/salida de la API).

Separar esto de los modelos de dominio permite exponer/ocultar campos
según convenga sin tocar la lógica interna.
"""

from typing import Optional
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, examples=["Teclado mecánico"])
    description: Optional[str] = Field(None, max_length=300)
    price: float = Field(..., ge=0, examples=[49.90])
    is_active: bool = True


class ItemCreate(ItemBase):
    """Datos requeridos para crear un item."""
    pass


class ItemUpdate(BaseModel):
    """Todos los campos opcionales, para actualizaciones parciales (PATCH)."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    price: Optional[float] = Field(None, ge=0)
    is_active: Optional[bool] = None


class ItemOut(ItemBase):
    id: int

    model_config = {"from_attributes": True}
