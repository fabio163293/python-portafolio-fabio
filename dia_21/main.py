from cargador import cargar_datos
from procesador import calcular_total_ventas, ventas_por_producto, calcular_estadisticas, generar_reporte
from visualizador import mostrar_resumen, mostrar_total_general, confirmar_reporte

# Valida que la entrada sea un entero dentro de un rango
# Validates that the input is an integer within a range
def validar_opcion(mensaje):
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in range(1, 3):
                return opcion
            print("Opción inválida. Por favor, seleccione entre 1 y 2.")
        except ValueError:
            print("Error: por favor ingrese un número.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            return None

# Función principal que ejecuta el programa
# Main function that runs the program
def main():
    # Usa una ruta relativa para mayor portabilidad
    ruta = "ventas.csv"
    archivo_reporte = "reporte_ventas.txt"
    
    try:
        while True:
            print("\nBienvenido al Analizador de Ventas")
            print("1) Generar reporte")
            print("2) Salir")
            opcion = validar_opcion("Seleccione una opción: ")
            if opcion is None:
                print("Hasta luego.")
                break

            if opcion == 1:
                # Carga los datos
                df = cargar_datos(ruta)
                if df is None or df.empty:
                    print("No se pudieron cargar los datos. Verifique el archivo.")
                    continue
                
                # Calcula estadísticas
                resumen = ventas_por_producto(df)
                total = calcular_total_ventas(df)
                estadisticas = calcular_estadisticas(df)
                
                if not estadisticas:
                    print("No se pudieron calcular las estadísticas.")
                    continue
                
                # Muestra los resultados en consola
                mostrar_resumen(resumen)
                mostrar_total_general(total)
                
                # Genera el reporte en archivo
                exito = generar_reporte(estadisticas, total, archivo_reporte)
                confirmar_reporte(archivo_reporte, exito)
            
            elif opcion == 2:
                print("Hasta luego.")
                break
                
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")

if __name__ == '__main__':
    main()