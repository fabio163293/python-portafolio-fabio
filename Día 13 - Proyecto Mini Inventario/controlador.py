import sys
import organizador
ruta_libro = r"C:\Users\Fabio Alvarez\Pictures\Día 13 - Proyecto Mini Inventario\entidades"
sys.path.append(ruta_libro)
ruta_json = r"C:\Users\Fabio Alvarez\Pictures\Día 13 - Proyecto Mini Inventario\data\productos.json"
ruta_anterior = r"C:\Users\Fabio Alvarez\Pictures\Día 13 - Proyecto Mini Inventario\backup\productosanterior.json"
from producto import Producto
#valida que el valor recibido por pantalla sea numero, tambien da la oportunidad de validar que sea mayor de 0.

def validar_entero(mensaje,bool):
    while True:
        try:
            valor = int(input(f"{mensaje}" ))
            if bool is True:
                if valor > 0:
                    return valor
                else: print("El valor debe ser mayor que 0 ")
            else:
                if valor in range(1,7):
                    return valor
                else:
                    print("El valor no se encuentra en la seleccion: ") 
                    print("vuelva a intentar ")
        except ValueError:
                print("El valor ingresado solo debe ser numeros")   

def datos_producto():
    nombre = input(f"Por favor indique el nombre del producto: ").lower()
    precio = validar_entero(f"Por favor indique el precio del producto:{nombre}:  ", True)  
    cantidad = validar_entero(f"Por favor indique la cantidad disponible: ", True)
    return nombre, precio, cantidad

def agregar_producto():
    while True:
       nombre,precio,cantidad = datos_producto()
       producto1 = Producto(nombre,precio,cantidad)
       return organizador.agregar_productos(ruta_json, producto1.a_diccionario())
       
def mostrar_productos():
    lista_diccionario = organizador.lector_json(ruta_json)
    for prod in lista_diccionario:
        print(prod["producto"])
        producto_obj = Producto.desde_diccionario(prod)
        producto_obj.mostrar_informacion()
        print(" ")

def buscar_producto(true):
    lista_diccionario = organizador.lector_json(ruta_json)
    while True:
        print("Puede escribir salir para poder salir")
        nombre_buscar = input("Indique el nombre del producto: ").lower()
        for prod in lista_diccionario:
            if nombre_buscar == prod["producto"] and true == True:
                print("Producto encontrado ")
                print("Por favor ingrese los nuevos datos ")
                nombre, precio, cantidad = datos_producto()
                prod["producto"] = nombre
                prod["precio"] = precio
                prod["cantidad"] = cantidad
                return organizador.escrictor_productos(ruta_json, lista_diccionario,
                  f"el producto {nombre_buscar} fue actualizado y guardado")
            elif nombre_buscar == prod["producto"]:
               producto_seleccionado = Producto.desde_diccionario(prod)
               return producto_seleccionado.mostrar_informacion()
            elif nombre_buscar== "salir":
                return print("Saliendo del buscador, muchas gracias")


def actualizar_producto():
    return buscar_producto(True) 
             
def eliminar_producto():
    lista_diccionario = organizador.lector_json(ruta_json)
    print("Si el producto no existe, el sitema continuara su funcionamiento sin eliminar ningun producto")
    nombre_eliminar = input("Por favor indique el nombre del producto a eliminar")
    nueva_lista =[prod for prod in lista_diccionario if prod["producto"] != nombre_eliminar]
    return organizador.escrictor_productos(ruta_json, nueva_lista,
    f"Producto {nombre_eliminar} eliminado o no existia"), organizador.escrictor_productos(ruta_anterior,lista_diccionario,"Productos anteriores guardados ")


