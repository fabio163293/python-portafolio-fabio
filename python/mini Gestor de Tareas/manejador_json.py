import json

# Lee una lista de tareas desde un archivo JSON
# Reads a list of tasks from a JSON file
def lector_json(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            tareas = json.load(archivo)
            return tareas
    except UnicodeDecodeError as e:
        print(f"Error: en decodificación: {e}")
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo al guardar")
    except PermissionError:
        print(f"El usuario no tiene permiso para acceder al archivo {ruta}")
    except IOError as e:
        print(f"Se presentó el siguiente error de entrada o salida: {e}")
    return []  # Retorna una lista vacía en caso de error

# Escribe una lista de tareas en un archivo JSON
# Writes a list of tasks to a JSON file
def escritor_tareas(ruta, lista, mensaje):  # Corrección del nombre de la función
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista, archivo, indent=4, ensure_ascii=False)
        print(mensaje)
        return True
    except UnicodeEncodeError as e:
        print(f"Error: en codificación: {e}")
        return False
    except PermissionError:
        print(f"El usuario no tiene permiso para acceder al archivo {ruta}")
        return False
    except IOError as e:
        print(f"Se presentó el siguiente error de entrada o salida: {e}")
        return False

# Agrega una tarea al archivo JSON
# Adds a task to the JSON file
def agregar_tarea(ruta, producto):
    tareas_json = lector_json(ruta)
    tareas_json.append(producto)
    return escritor_tareas(ruta, tareas_json, "Tarea agregada con éxito")