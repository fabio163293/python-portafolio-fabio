from controlador import *

# Función principal que ejecuta el menú del programa
# Main function that runs the program's menu
def main():
    while True:
        print("\n--- Menú de Tareas ---")
        print("1. Mostrar Tareas")
        print("2. Agregar Tareas")
        print("3. Completar Tareas")
        print("4. Salir")
        seleccion = validar_entero("Por favor ingrese la opción que desea utilizar", True)
        if seleccion is None:
            print("Sistema cerrando, muchas gracias")
            break

        if seleccion == 1:
            mostrar_tareas()
        elif seleccion == 2:
            if not datos_tarea():  # Verifica si datos_tarea retorna False
                break
        elif seleccion == 3:
            completar_tarea()
        elif seleccion == 4:
            print("Sistema cerrando, muchas gracias")
            break  

if __name__ == '__main__':
    main()