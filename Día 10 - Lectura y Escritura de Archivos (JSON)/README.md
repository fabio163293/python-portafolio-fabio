# 📘 Día 10 - Lectura y Escritura de Archivos (TXT, CSV, JSON)

## 🎯 Objetivo
Aplicar lectura y escritura de archivos en distintos formatos, integrando estructuras de datos y programación orientada a objetos.

## ✅ Ejercicio Realizado: Gestión de libros con JSON

Se desarrolló un sistema de serialización y deserialización de objetos `Libro`, utilizando el módulo `json`.  
Incluye:

- Lectura y escritura de archivos `.json`.
- Conversión de objetos a diccionarios (`a_diccionario()`).
- Reconstrucción de objetos desde diccionarios (`desde_diccionario()`).
- Separación por módulos: `entidades/libro.py` y `procesar_json.py`.

### 📂 Archivos incluidos

```
Día 10 - Lectura y Escritura de Archivos (TXT, CSV, JSON)
├── entidades/
│   └── libro.py         # Clase Libro con serialización JSON
├── libros.json          # Archivo JSON con los libros
└── procesar_json.py     # Script principal para agregar, leer y mostrar libros
```

### 📄 libro.py

Contiene la clase `Libro` con:
- Atributos: `titulo`, `autor`, `epoca`, `estado`
- Métodos: `mostrar_libro`, `prestar_libro`, `devolver_libro`
- Nuevos métodos:
  - `a_diccionario()`: convierte el objeto a diccionario JSON
  - `@classmethod desde_diccionario(data)`: convierte diccionario en objeto

### ⚙ procesar_json.py

- Crea libros y los guarda en `libros.json`
- Lee el archivo y reconstruye objetos `Libro`
- Muestra la información y el estado de cada libro
- Agrega nuevos libros al archivo sin sobrescribir

### 🧠 Habilidades desarrolladas

- Dominio del módulo `json`
- Serialización de objetos (POO aplicada)
- Validación de errores con `try/except`
- Lectura estructurada de archivos externos
- Organización de código en módulos reutilizables

---

## 🔖 Conclusión

Se alcanzó el objetivo del día dominando el manejo de archivos `.json`, utilizando clases, métodos y estructuras de datos.  
No se incluyó `.txt` y `.csv` por tratarse de una práctica más completa, profunda y orientada al mundo real.
