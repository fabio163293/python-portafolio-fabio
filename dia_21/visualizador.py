# Muestra un resumen de ventas por producto en consola
# Displays a summary of sales per product in the console
def mostrar_resumen(resumen):
    if not resumen:
        print("No hay datos para mostrar.")
        return
    print("\nResumen de Ventas por Producto:")
    for producto, total in resumen.items():
        print(f"{producto}: ${total:.2f}")

# Muestra el total general de ventas en consola
# Displays the total sales in the console
def mostrar_total_general(total):
    print(f"\nTotal General de Ventas: ${total:.2f}")

# Muestra un mensaje de confirmación del reporte
# Displays a confirmation message for the report
def confirmar_reporte(archivo_salida, exito):
    if exito:
        print(f"Reporte generado con éxito en {archivo_salida}")
    else:
        print("No se pudo generar el reporte.")