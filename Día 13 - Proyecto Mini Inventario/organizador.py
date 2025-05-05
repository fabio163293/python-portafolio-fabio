import json
from datetime import datetime
import os
import shutil
carpeta_backup = r"C:\Users\Fabio Alvarez\Pictures\Día 13 - Proyecto Mini Inventario\backup"

def lector_json(ruta):
    try:
       with open( ruta, "r", encoding="utf-8") as archivo:
          productos_json = json.load(archivo)
                   
    except FileNotFoundError:
           print("Archivo no encontrado creando archivo")
           productos_json = []
    return productos_json       

def escrictor_productos(ruta, lista, mensaje):
    with open( ruta, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)
    print(mensaje)
    backup(ruta)  

def agregar_productos(ruta, producto):
    productos_json = lector_json(ruta)    
    productos_json.append(producto)
    escrictor_productos(ruta, productos_json, "Producto agregado con exito")
    

def backup(ruta):
    fecha = datetime.now().strftime("%a-%m-%d")
    nombre_backup = f"productos_{fecha}.json"
    os.makedirs(carpeta_backup, exist_ok=True)
    ruta_backup = os.path.join(carpeta_backup,nombre_backup)
    shutil.copy2(ruta, ruta_backup)
    print("Backup creado")


      

