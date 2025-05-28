# Día 23 - Gestor de Inventario con SQLite

**Fecha:** 21 de mayo de 2025

## Descripción (ES/EN)

**Español:**  
Este día se centra en aprender a usar SQLite con Python para gestionar un inventario de productos. Se implementan operaciones CRUD (crear, leer, actualizar, eliminar) en una base de datos local (`inventario.db`). El programa incluye una clase `Producto`, un módulo `db_utils` para operaciones de base de datos, y un programa principal `gestor_inventario` con un menú interactivo.

**English:**  
This day focuses on learning to use SQLite with Python to manage a product inventory. CRUD operations (create, read, update, delete) are implemented in a local database (`inventario.db`). The program includes a `Producto` class, a `db_utils` module for database operations, and a main program `gestor_inventario` with an interactive menu.

## Estructura

- `producto.py`: Clase `Producto` para representar productos.
- `db_utils.py`: Módulo con funciones para interactuar con la base de datos SQLite.
- `gestor_inventario.py`: Programa principal con un menú interactivo.
- `inventario.db`: Base de datos generada automáticamente (no incluida en el repositorio).

## Instrucciones de Uso (ES/EN)

**Español:**  
1. Asegúrate de tener Python instalado (la librería `sqlite3` viene incluida).  
2. Ejecuta `gestor_inventario.py` para usar el programa:  
   - Opción 1: Agrega un producto.  
   - Opción 2: Consulta todos los productos.  
   - Opción 3: Consulta productos por categoría.  
   - Opción 4: Actualiza el stock de un producto.  
   - Opción 5: Elimina un producto.  
   - Opción 6: Salir.

**English:**  
1. Ensure you have Python installed (`sqlite3` library is included).  
2. Run `gestor_inventario.py` to use the program:  
   - Option 1: Add a product.  
   - Option 2: View all products.  
   - Option 3: View products by category.  
   - Option 4: Update a product's stock.  
   - Option 5: Delete a product.  
   - Option 6: Exit.