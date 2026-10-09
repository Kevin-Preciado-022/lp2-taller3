# Lenguaje de Programación 2 - Taller 3

![commits](https://badgen.net/github/commits/clubdecomputacion/lp2-taller3?icon=github) 
![last_commit](https://img.shields.io/github/last-commit/clubdecomputacion/lp2-taller3)

- ver [badgen](https://badgen.net/) o [shields](https://shields.io/) para otros tipos de _badges_

## Autor

- [@Kevin Dario Preciaddo Vallecilla](https://github.com/Kevin-Preciado-022/lp2-taller3.git)

## Mi Tienda Virtual - Taller 3

## 🎯 Objetivo del proyecto
El propósito principal es aprender y aplicar conceptos de:
- **Contenerización con Docker**: cada componente (base de datos, API y frontend) corre en su propio contenedor aislado.
- **Orquestación con Docker Compose**: los servicios se levantan en conjunto, con dependencias y healthchecks configurados.
- **Backend con FastAPI**: se implementan modelos, esquemas y rutas para gestionar productos y categorías.
- **Persistencia con PostgreSQL**: los datos se guardan en una base relacional, con tablas creadas y pobladas automáticamente.
- **Frontend simple**: una interfaz web que consume la API y muestra el catálogo de productos.
## estructura 
lp2-taller3/
├── api/                # Backend FastAPI
│   ├── app/            # Código fuente (routers, models, crud, seed)
│   └── data/productos.json  # Datos iniciales de productos
├── web/                # Frontend (HTML, CSS, JS)
├── docker-compose.yml  # Orquestación de servicios
└── README.md
## Proceso

## ⚙️ Flujo de ejecución
1. **Base de datos (Postgres)**: se levanta con usuario, contraseña y base definidos en `.env`.  
2. **API (FastAPI)**: al iniciar, ejecuta automáticamente el script `seed.py` que:
   - Crea las tablas necesarias.
   - Carga los productos desde `data/productos.json`.
   - Arranca el servidor Uvicorn en `http://localhost:8000`.  
3. **Frontend (web)**: se conecta a la API usando la URL `http://api:8000` (vista desde Docker) y muestra los productos en `http://localhost:5000`.

## 🚀 Levantar el proyecto
```bash
docker compose up -d


[GUIA.md](docs/GUIA.md)

