from datetime import datetime

# Calcula el total de ventas (suma de totales por fila)
# Calculates the total sales (sum of totals per row)
def calcular_total_ventas(df):
    if df is None or df.empty:
        return 0
    return df['total'].sum()

# Calcula las ventas por producto (ingresos por producto)
# Calculates sales per product (revenue per product)
def ventas_por_producto(df):
    if df is None or df.empty:
        return {}
    return df.groupby('producto')['total'].sum().to_dict()

# Calcula estadísticas adicionales (total por categoría, producto más vendido, promedio de precio por categoría)
# Calculates additional statistics (total per category, best-selling product, average price per category)
def calcular_estadisticas(df):
    if df is None or df.empty:
        return None
    estadisticas = {}
    # Total de ingresos por categoría
    estadisticas['total_por_categoria'] = df.groupby('categoria')['total'].sum().to_dict()
    # Producto más vendido (mayor cantidad)
    producto_mas_vendido = df.loc[df['cantidad'].idxmax()]
    estadisticas['producto_mas_vendido'] = {
        'nombre': producto_mas_vendido['producto'],
        'cantidad': producto_mas_vendido['cantidad']
    }
    # Promedio de precio por categoría
    estadisticas['promedio_precio_categoria'] = df.groupby('categoria')['precio'].mean().to_dict()
    return estadisticas

# Genera un reporte en un archivo de texto
# Generates a report in a text file
def generar_reporte(estadisticas, total_general, archivo_salida):
    if not estadisticas:
        return False
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.write(f"Reporte de Ventas - {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write("Total de ingresos por categoría:\n")
            for categoria, total in estadisticas['total_por_categoria'].items():
                f.write(f"- {categoria}: ${total:.2f}\n")
            f.write("\nProducto más vendido:\n")
            f.write(f"- {estadisticas['producto_mas_vendido']['nombre']} ({estadisticas['producto_mas_vendido']['cantidad']} unidades)\n")
            f.write("\nPromedio de precio por categoría:\n")
            for categoria, promedio in estadisticas['promedio_precio_categoria'].items():
                f.write(f"- {categoria}: ${promedio:.2f}\n")
            f.write(f"\nTotal General de Ventas: ${total_general:.2f}\n")
        return True
    except IOError as e:
        print(f"Error al escribir el reporte: {e}")
        return False