from controlador import *

def main():
     while True:
        print("\n--- Menú de Inventario ---")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Actualizar producto")
        print("6. Salir")
        seleccion = validar_entero("Por favor ingrese la opcion que desea utilizar ",False)

        if seleccion == 1:
            mostrar_productos()
        elif seleccion == 2:
            agregar_producto()
        elif seleccion == 3:
            buscar_producto(False)
        elif seleccion == 4:
            eliminar_producto()
        elif seleccion == 5:
            actualizar_producto()
        elif seleccion == 6:
            print("Sistema cerrando, muchas gracias")
            break  

if __name__ == '__main__':
    main()




