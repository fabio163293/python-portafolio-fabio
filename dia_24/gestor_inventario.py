from producto import Producto
from db_utils import (
    crear_bd,
    agregar_producto_desde_objeto,
    obtener_productos,
    eliminar_producto_por_id,
    actualizar_stock_por_id
)

def mostrar_menu():
    # Muestra el menú de opciones
    # Displays the options menu
    print("\nBienvenido al Gestor de Inventario / Welcome to the Inventory Manager")
    print("Opciones/Options:")
    print("1) Agregar producto / Add product")
    print("2) Consultar todos los productos / View all products")
    print("3) Consultar productos por categoría / View products by category")
    print("4) Actualizar stock / Update stock")
    print("5) Eliminar producto / Delete product")
    print("6) Salir / Exit")

def validar_entero(mensaje):
    # Valida que la entrada sea un entero positivo
    # Validates that the input is a positive integer
    while True:
        try:
            valor = int(input(f"{mensaje}"))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor que 0 / The value must be greater than 0")
        except ValueError:
            print("El valor ingresado solo debe ser números / The input must be a number")
            print("Vuelva a intentar / Try again")

def validar_opcion():
    # Valida la opción seleccionada por el usuario
    # Validates the option selected by the user
    while True:
        try:
            opcion = int(input("Seleccione una opción / Select an option: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción no válida. Seleccione entre 1 y 6. / Invalid option. Select between 1 and 6.")
        except ValueError:
            print("Por favor, ingrese un número válido. / Please enter a valid number.")

def agregar_producto():
    # Agrega un nuevo producto al inventario
    # Adds a new product to the inventory
    try:
        nombre = input("Ingrese el nombre del producto / Enter the product name: ").strip()
        categoria = input("Ingrese la categoría del producto / Enter the product category: ").strip()
        precio = validar_entero("Ingrese el precio del producto / Enter the product price: ")
        cantidad = validar_entero("Ingrese la cantidad del producto / Enter the product quantity: ")

        producto = Producto(nombre, categoria, precio, cantidad)
        agregar_producto_desde_objeto(producto)
    except ValueError as e:
        print(f"Error al agregar producto: {e}")
        print(f"Error adding product: {e}")
    except Exception as e:
        print(f"Error inesperado al agregar producto: {e}")
        print(f"Unexpected error adding product: {e}")

def consultar_productos(categoria=None):
    # Consulta productos, opcionalmente por categoría
    # Retrieves products, optionally by category
    productos = obtener_productos(categoria)
    if not productos:
        print("No hay productos registrados. / No products registered.")
    else:
        print("\nLista de productos / Product list:")
        for producto in productos:
            print(f"ID: {producto.id}, Nombre/Name: {producto.nombre}, Categoría/Category: {producto.categoria}, Precio/Price: {producto.precio}, Cantidad/Quantity: {producto.stock}")

def actualizar_stock():
    # Actualiza el stock de un producto
    # Updates the stock of a product
    consultar_productos()
    producto_id = validar_entero("Ingrese el ID del producto / Enter the product ID: ")
    nuevo_stock = validar_entero("Ingrese la nueva cantidad / Enter the new quantity: ")
    actualizar_stock_por_id(producto_id, nuevo_stock)

def eliminar_producto():
    # Elimina un producto por ID
    # Deletes a product by ID
    consultar_productos()
    producto_id = validar_entero("Ingrese el ID del producto a eliminar / Enter the ID of the product to delete: ")
    eliminar_producto_por_id(producto_id)

def main():
    # Función principal que ejecuta el programa
    # Main function that runs the program
    crear_bd()
    try:
        while True:
            mostrar_menu()
            opcion = validar_opcion()

            if opcion == 1:
                agregar_producto()
            elif opcion == 2:
                consultar_productos()
            elif opcion == 3:
                categoria = input("Ingrese la categoría para consultar / Enter the category to query: ").strip()
                if not categoria:
                    print("La categoría no puede estar vacía. / The category cannot be empty.")
                    continue
                consultar_productos(categoria)
            elif opcion == 4:
                actualizar_stock()
            elif opcion == 5:
                eliminar_producto()
            elif opcion == 6:
                print("Hasta luego. / Goodbye.")
                break

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. / Program interrupted by the user.")

if __name__ == "__main__":
    main()