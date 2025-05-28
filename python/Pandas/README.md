# Día 21 - Analizador de Ventas con Pandas

**Fecha:** 15 de mayo de 2025

## Descripción (ES/EN)

**Español:**  
Este día se centra en aprender los conceptos básicos de pandas para análisis de datos. Se desarrolla un analizador de ventas que lee datos de un archivo CSV, calcula estadísticas (ingresos por categoría, producto más vendido, promedio de precio por categoría), y genera un reporte en un archivo de texto. Se aplica modularidad y manejo de errores para robustez.  

**English:**  
This day focuses on learning the basics of pandas for data analysis. A sales analyzer is developed that reads data from a CSV file, calculates statistics (revenue per category, best-selling product, average price per category), and generates a report in a text file. Modularity and error handling are applied for robustness.

## Estructura

- `cargador.py`: Carga datos desde un archivo CSV usando pandas.
- `procesador.py`: Calcula estadísticas y genera el reporte en un archivo de texto.
- `visualizador.py`: Muestra los resultados en consola.
- `main.py`: Programa principal con un menú interactivo.
- `ventas.csv`: Archivo de datos de entrada con información de ventas.
- `reporte_ventas.txt`: Archivo de salida con el reporte generado.

## Instrucciones de Uso (ES/EN)

**Español:**  
1. Instala las dependencias: `pip install pandas`.  
2. Asegúrate de que `ventas.csv` esté en la carpeta `dia_21`.  
3. Ejecuta `main.py` para usar el programa.

**English:**  
1. Install dependencies: `pip install pandas`.  
2. Ensure `ventas.csv` is in the `dia_21` folder.  
3. Run `main.py` to use the program.