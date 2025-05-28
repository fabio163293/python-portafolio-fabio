# Día 13 – Proyecto Mini Inventario

**Fecha:** 05/05/2025

## Descripción

Este mini proyecto consiste en un sistema de inventario simple desarrollado en Python que permite:

- Agregar productos.
- Mostrar productos.
- Buscar o actualizar productos.
- Eliminar productos.
- Hacer respaldos automáticos al eliminar o sobreescribir los datos.

Se estructura en múltiples archivos para fomentar la organización y reutilización del código.

## Estructura del Proyecto

```
Día 13 - Proyecto Mini Inventario/
│
├── data/
│   └── productos.json
│
├── backup/
│   ├── productos_{fecha}.json
│   └── productosanterior.json
│
├── entidades/
│   ├── producto.py
│
├── main.py
├── controlador.py
├── organizador.py
```

## Funcionalidades

- **Agregar Producto**: Captura nombre, precio y cantidad desde consola y lo guarda en el archivo `productos.json`.
- **Mostrar Productos**: Muestra todos los productos disponibles usando el método `mostrar_informacion`.
- **Buscar/Actualizar Producto**: Permite buscar un producto y actualizar su información si se desea.
- **Eliminar Producto**: Elimina un producto y guarda una copia de seguridad antes del cambio.
- **Backup Automático**: Cada vez que se sobreescribe o elimina un producto, se genera un respaldo.

## Archivos principales

- `producto.py`: Define la clase `Producto`.
- `controlador.py`: Controla las operaciones lógicas (agregar, buscar, eliminar).
- `main.py`: Contiene el menú interactivo del sistema.
- `organizador.py`: Administra la carga y guardado de archivos JSON.

## Ejemplo de uso

```bash
$ python main.py

--- Menú de Inventario ---
1. Mostrar productos
2. Agregar producto
3. Buscar producto
4. Eliminar producto
5. Actualizar producto
6. Salir
```

## Librerías utilizadas

- `datetime` – Para registrar fechas de ingreso.
- `json` – Para manejar datos estructurados.
- `os`, `sys` – Para rutas y manipulación de archivos.

## Comentario final

Este mini proyecto aplica gran parte de los conocimientos adquiridos en los días anteriores: clases, estructuras condicionales, funciones, manejo de archivos, modularidad, validación de entradas, e interacción con el usuario por consola.
