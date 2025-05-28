# Día 19 - Gestor de Tareas con Clases y Archivos

**Fecha:** 10 de mayo de 2025

## Descripción (ES/EN)

**Español:**  
Este día se centra en desarrollar un mini proyecto: un gestor de tareas que usa clases, módulos, y manejo de archivos. Permite añadir tareas, marcarlas como completadas, y mostrarlas, guardando los datos en un archivo JSON. Se aplica orientación a objetos y modularidad para estructurar el código de manera profesional.  

**English:**  
This day focuses on developing a mini project: a task manager that uses classes, modules, and file handling. It allows adding tasks, marking them as completed, and displaying them, saving the data in a JSON file. Object-oriented programming and modularity are applied to structure the code professionally.

## Estructura

- `entidades/tarea.py`: Clase `Tarea` para manejar las tareas con atributos como título, descripción, prioridad, estado y fecha de ingreso.
- `manejador_json.py`: Funciones para leer y escribir tareas en `tareas.json`.
- `controlador.py`: Lógica del programa para capturar datos, crear tareas, mostrarlas y completarlas.
- `main.py`: Menú principal para interactuar con el usuario.
- `tareas.json`: Archivo donde se guardan las tareas.