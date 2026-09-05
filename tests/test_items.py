from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_and_get_item():
    payload = {"name": "Mouse", "description": "Inalámbrico", "price": 25.5}
    create_resp = client.post("/items", json=payload)
    assert create_resp.status_code == 201
    item = create_resp.json()
    assert item["name"] == "Mouse"

    get_resp = client.get(f"/items/{item['id']}")
    assert get_resp.status_code == 200
    assert get_resp.json()["price"] == 25.5


def test_get_item_not_found():
    response = client.get("/items/9999")
    assert response.status_code == 404


def test_update_item():
    create_resp = client.post("/items", json={"name": "Teclado", "price": 40})
    item_id = create_resp.json()["id"]

    update_resp = client.patch(f"/items/{item_id}", json={"price": 35})
    assert update_resp.status_code == 200
    assert update_resp.json()["price"] == 35


def test_delete_item():
    create_resp = client.post("/items", json={"name": "Monitor", "price": 100})
    item_id = create_resp.json()["id"]

    delete_resp = client.delete(f"/items/{item_id}")
    assert delete_resp.status_code == 204

    get_resp = client.get(f"/items/{item_id}")
    assert get_resp.status_code == 404
