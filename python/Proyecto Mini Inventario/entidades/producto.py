#!Python
from datetime import datetime

class Producto:
    def __init__(self, nombre, precio, stock, fecha_ingreso = None):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M")
        
    #imprime por consola la informacion del producto
    def mostrar_informacion(selft):
        print(f"Producto: {selft.nombre}")
        print(f"Precio: RD${selft.precio}")
        print(f"Disponibles: {selft.stock}")
        print(f"Ingreso: {selft.fecha_ingreso}")
    #vuelve un objeto producto a informacion para un diccionario    
    def a_diccionario(self):
        return {"producto": self.nombre,
        "precio": self.precio,
        "disponibles": self.stock,
        "fecha ingreso": self.fecha_ingreso
        }
    #vuelve la informacion de un diccionario de un producto a un obejeto producto
    @classmethod
    def desde_diccionario(cls, data):
        return cls(data["producto"],data["precio"],data["disponibles"],data["fecha ingreso"])   

