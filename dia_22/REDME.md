# Día 22 - Visualización de Ventas con Matplotlib

**Fecha:** 19 de mayo de 2025

## Descripción (ES/EN)

**Español:**  
Este día se centra en extender el analizador de ventas del Día 21 usando `matplotlib` para visualizar datos. Se generan gráficos de ingresos por categoría y cantidad vendida por producto, guardándolos como archivos PNG. Se reutilizan módulos del Día 21 para mantener continuidad y modularidad.

**English:**  
This day focuses on extending the sales analyzer from Day 21 by using `matplotlib` to visualize data. Charts for income by category and quantity sold by product are generated and saved as PNG files. Modules from Day 21 are reused to maintain continuity and modularity.

## Estructura

- `cargador.py`: Reutilizado del Día 21 para cargar datos desde `ventas.csv` usando pandas.
- `graficador.py`: Genera gráficos de ingresos por categoría y cantidad por producto.
- `analizador_ventas.py`: Programa principal con un menú para generar y mostrar gráficos.
- `ventas.csv`: Archivo de datos reutilizado del Día 21.

## Instrucciones de Uso (ES/EN)

**Español:**  
1. Instala las dependencias: `pip install pandas matplotlib`.  
2. Asegúrate de que `ventas.csv` esté en la carpeta `dia_22` o ajusta la ruta en `analizador_ventas.py`.  
3. Ejecuta `analizador_ventas.py` para usar el programa.  
   - Opción 1 genera gráficos y los guarda como PNG.  
   - Opción 2 genera y muestra los gráficos.

**English:**  
1. Install dependencies: `pip install pandas matplotlib`.  
2. Ensure `ventas.csv` is in the `dia_22` folder or adjust the path in `analizador_ventas.py`.  
3. Run `analizador_ventas.py` to use the program.  
   - Option 1 generates charts and saves them as PNGs.  
   - Option 2 generates and displays the charts.