import sys
import json

ruta_libro = r"C:\Users\Fabio Alvarez\Pictures\Día 9 - Módulos y Paquetes\entidades"
sys.path.append(ruta_libro)

from libro import Libro 

libro1 = Libro("Amanda", "Julio Espera", 1997, True)
libro2 = Libro("Cielo Azul", "Julio Espera", 2001, False)

libros = [libro1.a_diccionario(),
          libro2.a_diccionario()]



def agregar_libros(diccionario):
    with open("libros.json", "w", encoding="utf-8") as archivo:
       json.dump(diccionario, archivo, indent=4)
    print("Estudiantes Guardados")

def leer_json():
   try:
       with open("libros.json", "r", encoding="utf-8") as archivo:
           libros_json = json.load(archivo)
           libros_guardados = [Libro.desde_diccionario(lib) for lib in libros_json]
   except FileNotFoundError:
        print("Archivo no enccontrado")        

        for lib in libros_guardados:
            print(f"El libro {lib.titulo} escrito por {lib.autor}")
            print(f"fue escrito el año {lib.epoca}")
            if lib._estado is True:
                print("El libro se encuentra prestado") 
            else:
                print("El libro esta disponible ")    

def agregar_libro(lib):
    try:
       with open("libros.json", "r", encoding="utf-8") as archivo:
           libros_json = json.load(archivo)
        
    except FileNotFoundError:
           print("Archivo no encontrado")
    libros_json.append(lib.a_diccionario())
    with open("libros.json", "w", encoding="utf-8") as archivo:
        json.dump(libros_json, archivo, indent=4, ensure_ascii=False)
    print("Nuevo libro agregado y archivo actualizado")    



libro3 = Libro("Palomo en la mano", "Fabio Alvarez", 2025, False)
agregar_libro(libro3)