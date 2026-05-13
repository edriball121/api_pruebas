# App Clean Architecture

Aplicación fullstack con FastAPI (backend) y React (frontend) siguiendo Clean Architecture.

## Estructura

```
├── backend/           # FastAPI con Clean Architecture
│   ├── src/
│   │   ├── domain/           # Entidades y repositorios abstractos
│   │   ├── application/      # Casos de uso
│   │   ├── infrastructure/   # Implementaciones concretas
│   │   └── interfaces/       # Controllers y schemas
│   └── main.py
│
├── frontend/          # React con Clean Architecture
│   ├── src/
│   │   ├── domain/           # Entidades y repositorios
│   │   ├── application/      # Casos de uso
│   │   ├── infrastructure/   # Implementaciones HTTP
│   │   └── interfaces/       # Componentes React
│   └── package.json
│
└── docker-compose.yml
```

## Ejecución

### Con Docker (recomendado)
```bash
docker-compose up --build
```

### Manual

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## Endpoints API

| Endpoint | Descripción |
|----------|-------------|
| GET /api/users | Lista todos los usuarios |
| GET /api/users/{id} | Obtiene usuario por ID |
| GET /api/users/{id}/posts | Posts de un usuario |
| GET /api/posts | Lista todos los posts |
| GET /api/posts/{id} | Obtiene post por ID |

Los datos provienen de [JSONPlaceholder](https://jsonplaceholder.typicode.com).