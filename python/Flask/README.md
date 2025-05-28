# Día 24 - API de Inventario con Flask

**Fecha/Date:** 23 de mayo de 2025 / May 23, 2025

## Descripción (ES/EN)

**Español:**  
Este día se centra en crear una API REST con Flask para gestionar el inventario del Día 23. La API permite realizar operaciones CRUD (crear, leer, actualizar, eliminar) sobre productos almacenados en una base de datos SQLite (`inventario.db`). Reutiliza los módulos `producto.py` y `db_utils.py` del Día 23.

**English:**  
This day focuses on creating a REST API with Flask to manage the inventory from Day 23. The API allows CRUD operations (create, read, update, delete) on products stored in a SQLite database (`inventario.db`). It reuses the `producto.py` and `db_utils.py` modules from Day 23.

## Estructura

- `app.py`: Aplicación Flask con los endpoints de la API.
- `requirements.txt`: Dependencias del proyecto.
- `inventario.db`: Base de datos generada automáticamente (no incluida en el repositorio).

## Endpoints

- **GET /productos**: Lista todos los productos.
- **GET /productos/<id>**: Obtiene un producto por su ID.
- **POST /productos**: Agrega un nuevo producto (espera JSON con `nombre`, `categoria`, `precio`, `stock`).
- **PUT /productos/<id>**: Actualiza el stock de un producto (espera JSON con `stock`).
- **DELETE /productos/<id>**: Elimina un producto por su ID.

## Instrucciones de Uso (ES/EN)

**Español:**  
1. Asegúrate de tener Python instalado y los archivos `producto.py` y `db_utils.py` del Día 23 en el directorio raíz.  
2. Instala las dependencias:  
   ```bash
   pip install -r requirements.txt