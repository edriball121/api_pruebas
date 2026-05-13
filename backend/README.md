# Clean Architecture FastAPI

Ejemplo de API con **Clean Architecture** consumiendo [JSONPlaceholder](https://jsonplaceholder.typicode.com).

## Estructura

```
backend/
├── src/
│   ├── domain/              # Entidades + interfaces (sin dependencias externas)
│   │   ├── entities/
│   │   ├── repositories/
│   │   └── services/
│   ├── application/         # Casos de uso + DTOs
│   │   ├── use_cases/
│   │   └── dto/
│   ├── infrastructure/      # Implementaciones concretas (HTTP, DB, etc.)
│   │   ├── repositories/
│   │   └── services/
│   └── interfaces/          # Adaptadores de entrada
│       ├── api/
│       └── schemas/
├── main.py
├── requirements.txt
└── README.md
```

## Endpoints

| Método | Ruta                          | Descripción                |
|--------|-------------------------------|----------------------------|
| GET    | `/api/users`                  | Lista todos los usuarios   |
| GET    | `/api/users/{id}`             | Obtiene usuario por ID     |
| GET    | `/api/users/{id}/posts`       | Posts de un usuario        |
| GET    | `/api/posts`                  | Lista todos los posts      |
| GET    | `/api/posts/{id}`             | Obtiene post por ID        |

## Instalación

```bash
cd backend
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Documentación

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc