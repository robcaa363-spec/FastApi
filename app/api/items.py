"""
Módulo (router) de 'Items'.

Contiene únicamente las rutas HTTP: recibe la petición, valida con los
schemas de Pydantic y delega la lógica al ItemService mediante
inyección de dependencias (Depends).
"""

from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.schemas.item import ItemCreate, ItemOut, ItemUpdate
from app.services.item_service import ItemService, ItemNotFoundError, item_service

router = APIRouter(prefix="/items", tags=["Items"])


def get_item_service() -> ItemService:
    """Dependencia que provee el servicio (facilita el mocking en tests)."""
    return item_service


@router.get("", response_model=List[ItemOut])
def list_items(
    only_active: Optional[bool] = Query(
        None, description="Filtra por items activos (true) o inactivos (false)"
    ),
    service: ItemService = Depends(get_item_service),
):
    return service.list_items(only_active=only_active)


@router.get("/{item_id}", response_model=ItemOut)
def get_item(item_id: int, service: ItemService = Depends(get_item_service)):
    try:
        return service.get_item(item_id)
    except ItemNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.post("", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate, service: ItemService = Depends(get_item_service)):
    return service.create_item(payload)


@router.patch("/{item_id}", response_model=ItemOut)
def update_item(
    item_id: int,
    payload: ItemUpdate,
    service: ItemService = Depends(get_item_service),
):
    try:
        return service.update_item(item_id, payload)
    except ItemNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, service: ItemService = Depends(get_item_service)):
    try:
        service.delete_item(item_id)
    except ItemNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
