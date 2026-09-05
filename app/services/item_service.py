"""
Capa de servicio: contiene la lógica de negocio de 'Item'.

El router (app/api/items.py) NO debe tener lógica de negocio; solo
recibe la petición HTTP y delega aquí. Esto facilita testear la
lógica sin depender de FastAPI, y facilita reemplazar el almacenamiento
en memoria por una base de datos real más adelante.
"""

from typing import List, Optional

from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class ItemNotFoundError(Exception):
    """Se lanza cuando no se encuentra un item con el id solicitado."""


class ItemService:
    def __init__(self) -> None:
        # Almacenamiento en memoria a modo de ejemplo (reemplazar por DB real)
        self._items: dict[int, Item] = {}
        self._next_id: int = 1

    def list_items(self, only_active: Optional[bool] = None) -> List[Item]:
        items = list(self._items.values())
        if only_active is not None:
            items = [i for i in items if i.is_active == only_active]
        return items

    def get_item(self, item_id: int) -> Item:
        item = self._items.get(item_id)
        if item is None:
            raise ItemNotFoundError(f"Item {item_id} no encontrado")
        return item

    def create_item(self, data: ItemCreate) -> Item:
        item = Item(id=self._next_id, **data.model_dump())
        self._items[item.id] = item
        self._next_id += 1
        return item

    def update_item(self, item_id: int, data: ItemUpdate) -> Item:
        item = self.get_item(item_id)
        updates = data.model_dump(exclude_unset=True)
        for field_name, value in updates.items():
            setattr(item, field_name, value)
        return item

    def delete_item(self, item_id: int) -> None:
        if item_id not in self._items:
            raise ItemNotFoundError(f"Item {item_id} no encontrado")
        del self._items[item_id]


# Instancia única (singleton simple) reutilizada por la inyección de dependencias
item_service = ItemService()
