# Día 11 - Automatización con Python

## Objetivo
Automatizar tareas comunes del sistema de archivos utilizando Python, como:
- Imprimir la ruta actual de trabajo.
- Crear estructuras de carpetas organizadas.
- Renombrar archivos con prefijos específicos.
- Buscar archivos por extensión.
- Mover archivos automáticamente a carpetas basadas en su tipo.

## Contenido
Se desarrollaron las siguientes funciones en el archivo `organizador_archivo.py`:

- `imprimir_ruta()`: Muestra la ruta actual del directorio de trabajo.
- `crear_estructura(nombre_estructura)`: Crea carpetas organizadas en `/data/raw`, `/data/processed`, `/logs` y `/src`.
- `renombrar_archivo(directorio, prefijo)`: Renombra todos los archivos en un directorio agregando un prefijo.
- `buscar_archivo(directorio, extension)`: Busca y lista archivos con una extensión específica.
- `organizar_archivos(directorio)`: Mueve archivos automáticamente a carpetas según su tipo (`.txt`, `.pdf`, `.jpg`, `.png`, etc).

## Ejecución
El archivo incluye un `main()` que ejecuta todas las funciones con ejemplos de uso.

```bash
python organizador_archivo.py
```

## Resultado Esperado
- Organización automática de archivos.
- Carpetas creadas correctamente.
- Archivos renombrados y movidos.
