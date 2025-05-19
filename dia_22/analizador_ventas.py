from graficador import generar_graficos
from cargador import cargar_datos

# Valida la opción ingresada por el usuario
# Validates the user's input option
def validar_opcion(mensaje):
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in range(1, 4):
                return opcion
            print("Opción inválida. Por favor, seleccione entre 1 y 3.")
            print("Invalid option. Please select between 1 and 3.")
        except ValueError:
            print("Error: por favor ingrese un número.")
            print("Error: please enter a number.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            print("\nProgram interrupted by the user.")
            return None

# Función principal que ejecuta el programa
# Main function that runs the program
def main():
    # Ajusta la ruta según la estructura de tu proyecto
    # Adjust the path according to your project structure
    ruta = "ventas.csv"  # Asume que ventas.csv está en la misma carpeta dia_22
                         # Assumes ventas.csv is in the same dia_22 folder

    try:
        while True:
            print("\nBienvenido al Analizador de Ventas")
            print("Welcome to the Sales Analyzer")
            print("1) Generar gráficos (guardar)")
            print("1) Generate charts (save)")
            print("2) Generar y mostrar gráficos")
            print("2) Generate and display charts")
            print("3) Salir")
            print("3) Exit")
            opcion = validar_opcion("Seleccione una opción: ")
            if opcion is None:
                print("Hasta luego.")
                print("Goodbye.")
                break

            if opcion == 1:
                # Carga los datos
                # Loads the data
                df = cargar_datos(ruta)
                if df is None or df.empty:
                    print("No se pudieron cargar los datos. Verifique el archivo.")
                    print("Could not load the data. Please check the file.")
                    continue
                generar_graficos(df, mostrar=False)
                print("Gráficos generados: 'ingresos_categoria.png' y 'ventas_producto.png'")
                print("Charts generated: 'ingresos_categoria.png' and 'ventas_producto.png'")

            elif opcion == 2:
                # Carga los datos
                # Loads the data
                df = cargar_datos(ruta)
                if df is None or df.empty:
                    print("No se pudieron cargar los datos. Verifique el archivo.")
                    print("Could not load the data. Please check the file.")
                    continue
                generar_graficos(df, mostrar=True)
                print("Gráficos generados y mostrados: 'ingresos_categoria.png' y 'ventas_producto.png'")
                print("Charts generated and displayed: 'ingresos_categoria.png' and 'ventas_producto.png'")

            elif opcion == 3:
                print("Hasta luego.")
                print("Goodbye.")
                break

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        print("\nProgram interrupted by the user.")

if __name__ == '__main__':
    main()