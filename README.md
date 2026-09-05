# FastAPI Modular App

Aplicación de ejemplo construida con **FastAPI**, organizada en módulos
independientes (routers, servicios, modelos, schemas y configuración),
lista para abrir y ejecutar en **VS Code**.

## 📁 Estructura del proyecto

```
fastapi-modular-app/
├── app/
│   ├── main.py              # Punto de entrada: crea la app y registra routers
│   ├── core/
│   │   └── config.py        # Configuración centralizada (Settings)
│   ├── api/                 # Módulo de rutas (routers)
│   │   ├── health.py        # Endpoint de salud (/health)
│   │   └── items.py         # Endpoints CRUD de items (/items)
│   ├── schemas/              # Contratos Pydantic (entrada/salida)
│   │   └── item.py
│   ├── services/              # Lógica de negocio
│   │   └── item_service.py
│   └── models/                # Entidades de dominio
│       └── item.py
├── tests/
│   └── test_items.py         # Tests con pytest + TestClient
├── .vscode/
│   ├── launch.json            # Debug con F5 (uvicorn --reload)
│   ├── settings.json          # Intérprete, pytest, formateo
│   └── extensions.json        # Extensiones recomendadas
├── requirements.txt
├── .env.example
└── .gitignore
```

Cada módulo tiene una responsabilidad clara:
- **api/**: define las rutas HTTP (entrada/salida), sin lógica de negocio.
- **services/**: contiene la lógica de negocio, independiente de FastAPI.
- **schemas/**: valida y serializa datos con Pydantic.
- **models/**: representa las entidades internas del dominio.
- **core/**: configuración global de la aplicación.

## 🚀 Cómo ejecutar en VS Code

1. Abre la carpeta `fastapi-modular-app` en VS Code (`File > Open Folder`).
2. Instala la extensión **Python** (ms-python.python) si no la tienes
   (VS Code te sugerirá las recomendadas de `.vscode/extensions.json`).
3. Crea un entorno virtual:
   ```bash
   python -m venv .venv
   ```
4. Actívalo:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
5. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
6. Selecciona el intérprete de `.venv` en VS Code
   (`Ctrl+Shift+P` → *Python: Select Interpreter*).
7. Copia `.env.example` a `.env` si quieres personalizar la configuración.

### Ejecutar la app

**Opción A — con F5 (debug):**
Presiona `F5` en VS Code. Ya está configurado en `.vscode/launch.json`
para lanzar `uvicorn app.main:app --reload --port 8000`.

**Opción B — desde la terminal:**
```bash
uvicorn app.main:app --reload
```

Luego abre:
- Documentación interactiva (Swagger): http://127.0.0.1:8000/docs
- Documentación alternativa (ReDoc): http://127.0.0.1:8000/redoc
- Health check: http://127.0.0.1:8000/health

### Ejecutar los tests

```bash
pytest
```

O usa la pestaña **Testing** de VS Code (ya configurada en `settings.json`).

## 🔧 Endpoints disponibles

| Método | Ruta            | Descripción                     |
|--------|-----------------|----------------------------------|
| GET    | /health         | Estado de la aplicación          |
| GET    | /items          | Lista items (filtro `only_active`)|
| GET    | /items/{id}     | Obtiene un item por id            |
| POST   | /items          | Crea un item                      |
| PATCH  | /items/{id}     | Actualiza parcialmente un item    |
| DELETE | /items/{id}     | Elimina un item                   |

## ➕ Cómo agregar un nuevo módulo

1. Crea el modelo en `app/models/`.
2. Crea el schema (entrada/salida) en `app/schemas/`.
3. Crea el servicio con la lógica de negocio en `app/services/`.
4. Crea el router en `app/api/` y regístralo en `app/main.py` con
   `app.include_router(...)`.

Este patrón mantiene el proyecto escalable: puedes agregar tantos
módulos (usuarios, pedidos, autenticación, etc.) como necesites sin
que se mezclen entre sí.
