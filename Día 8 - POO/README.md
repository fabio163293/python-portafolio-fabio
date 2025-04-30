# 📘 Día 8 - Programación Orientada a Objetos (POO)

## 🎯 Objetivo
Aprender los fundamentos de la Programación Orientada a Objetos (POO) en Python. Aplicar los conceptos de clases, objetos, atributos, métodos, encapsulamiento y validación.

## 🧱 Clases Desarrolladas

### 1. Clase `Estudiante`
- **Atributos:** `nombre`, `edad`, `carrera`
- **Método:** `mostrar_estudiante()` → Imprime los datos del estudiante
- **Objetivo:** Introducción básica a clases y objetos

### 2. Clase `Producto`
- **Atributos:** `nombre`, `precio`, `_stock`
- **Métodos:**
  - `get_stock()` → Devuelve el stock disponible
  - `mostrar_producto()` → Imprime la información del producto
  - `actualizar_stock(cambio)` → Ajusta el stock
  - `entrada_datos()` → Captura cambio de stock desde el usuario
- **Objetivo:** Manipulación de atributos y validación de entradas

### 3. Clase `Libro`
- **Atributos:** `titulo`, `autor`, `epoca`, `estado` (booleano)
- **Validación:** `estado` debe ser booleano al crear la instancia
- **Métodos:**
  - `get_estado()` → Devuelve el estado actual
  - `mostrar_libro()` → Muestra información del libro y disponibilidad
  - `prestar_libro()` → Cambia el estado a prestado (True)
  - `devolver_libro()` → Cambia el estado a disponible (False)
- **Objetivo:** Simular una gestión simple de biblioteca con lógica de préstamo

## 💡 Habilidades Aplicadas
- Creación de clases y objetos
- Inicialización con `__init__`
- Definición de métodos personalizados
- Encapsulamiento de atributos (`_stock`)
- Validación de tipos con `isinstance()` y `raise`
- Modularización del código
- Comentarios bilingües (español e inglés)

## 📂 Estructura del Proyecto

```
Día 8 - POO
├── estudiante.py
├── producto.py
├── libro.py
└── README.md
```

## ✅ Resultado
Este día representa la transición del pensamiento estructurado al orientado a objetos, sentando las bases para proyectos más avanzados y escalables en Python.
