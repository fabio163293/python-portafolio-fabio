import json
import os
from api_utils import obtener_clima, obtener_tasa_cambio

# API Keys (placeholders, reemplazar con claves válidas para usar el programa)
# API Keys (placeholders, replace with valid keys to use the program)
API_WEATHER = "cef851fea9e07644875bbbd10dcb0073"
API_EXCHANGE = "1a475b6c5c01927ceab904d2"

# Guarda una consulta en el historial en consultas.json
# Saves a query to the history in consultas.json
def guardar_consulta(texto):
    historial = []
    try:
        if os.path.exists("consultas.json"):
            with open("consultas.json", "r", encoding="utf-8") as f:
                historial = json.load(f)
    except (json.JSONDecodeError, IOError, PermissionError) as e:
        print(f"Error al leer el historial: {e}")
        historial = []
    historial.append(texto)
    try:
        with open("consultas.json", "w", encoding="utf-8") as f:
            json.dump(historial, f, indent=4, ensure_ascii=False)
    except (IOError, PermissionError) as e:
        print(f"Error al guardar el historial: {e}")

# Muestra el menú de opciones al usuario
# Displays the options menu to the user
def mostrar_menu():
    print("\nBienvenido al Consultor de Datos")
    print("1) Consultar clima")
    print("2) Consultar tasa de cambio")
    print("3) Mostrar historial")
    print("4) Salir")

# Valida que la entrada sea un entero dentro de un rango
# Validates that the input is an integer within a range
def validar_opcion(mensaje):
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in range(1, 5):
                return opcion
            print("Opción inválida. Por favor, seleccione entre 1 y 4.")
        except ValueError:
            print("Error: por favor ingrese un número.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            return None

# Función principal que ejecuta el programa
# Main function that runs the program
def main():
    try:
        while True:
            mostrar_menu()
            opcion = validar_opcion("Seleccione una opción: ")
            if opcion is None:
                break

            if opcion == 1:
                ciudad = input("Ciudad: ").strip()
                if not ciudad:
                    print("Error: la ciudad no puede estar vacía.")
                    continue
                resultado = obtener_clima(ciudad, API_WEATHER)
                print(resultado)
                guardar_consulta(resultado)

            elif opcion == 2:
                base = input("Moneda base (ej. USD): ").upper().strip()
                destino = input("Moneda destino (ej. EUR): ").upper().strip()
                resultado = obtener_tasa_cambio(base, destino, API_EXCHANGE)
                print(resultado)
                guardar_consulta(resultado)

            elif opcion == 3:
                try:
                    if os.path.exists("consultas.json"):
                        with open("consultas.json", "r", encoding="utf-8") as f:
                            historial = json.load(f)
                            print("\nHistorial:")
                            if not historial:
                                print("No hay consultas registradas.")
                            for consulta in historial:
                                print(consulta)
                    else:
                        print("No hay historial guardado.")
                except (json.JSONDecodeError, IOError, PermissionError) as e:
                    print(f"Error al leer el historial: {e}")

            elif opcion == 4:
                print("Hasta luego.")
                break
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")

if __name__ == '__main__':
    main()