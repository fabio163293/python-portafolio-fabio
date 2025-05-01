# 📦 Día 9 - Módulos y Paquetes en Python

## 🎯 Objetivo
Aplicar los conceptos de modularidad y organización de código mediante módulos y paquetes. Reutilizar funciones y clases importándolas entre archivos, y trabajar con el condicional `if __name__ == "__main__"`.

## 🗂️ Archivos y Componentes

### 1. `utilidades.py`
Contiene funciones reutilizables:
- `mostrar_line()` → Imprime una línea separadora.
- `validar_entero(mensaje)` → Captura y valida un número entero desde consola.
- `formato_mensaje(nombre, edad, carrera='desconocida')` → Muestra información formateada de una persona.

### 2. `main.py`
- Importa `main()` desde `utilidades`.
- Ejecuta funciones como ejemplo de uso.
- Captura edad y dos números para sumarlos, demostrando el uso de funciones externas.

### 3. Carpeta `entidades/`
- Incluye los archivos reutilizados del Día 8: `estudiante.py`, `producto.py`, `libro.py`.
- Organización en forma de paquete con módulo `__init__.py` (si se requiere ampliar).

## 💡 Habilidades Aplicadas
- Uso de `import` y `from ... import`.
- Reutilización de funciones desde otros archivos.
- Separación de responsabilidades por archivo.
- Ejecución controlada con `if __name__ == "__main__"`.
- Mantenimiento de buenas prácticas con comentarios en español e inglés.

## 📁 Estructura del Proyecto

Día 9 - Módulos y Paquetes
├── entidades/
│   ├── estudiante.py
│   ├── libro.py
│   ├── producto.py
├── utilidades.py
├── main.py
└── README.md

## ✅ Resultado
El código ahora está organizado en módulos y puede escalarse fácilmente para proyectos reales. Se logró una arquitectura limpia, clara y reutilizable.
