from entidades.tarea import Tarea
from manejador_json import lector_json, escritor_tareas, agregar_tarea

# Define la ruta del archivo JSON para las tareas
# Defines the path to the JSON file for tasks
ruta_json = 'tareas.json'

# Valida que la entrada sea un entero dentro de un rango
# Validates that the input is an integer within a range
def validar_entero(mensaje, bool=False):
    while True:
        try:
            numero = int(input(f"{mensaje}: "))
            rango = range(1, 5) if bool else range(1, 4)
            if numero in rango:
                return numero
            else:
                print("Error: opción no disponible")
                continue
        except ValueError:
            print("Error: por favor indique un número")
            continue  # Continúa pidiendo entrada en lugar de retornar None
        except KeyboardInterrupt:
            print("Error: Sistema interrumpido por el usuario")
            return None
        except IOError as e:
            print(f"Error: de entrada o salida: {e}")
            return None

# Captura datos del usuario con validación
# Captures user input with validation
def captura_datos(mensaje):
    while True:
        try:
            texto = input(f"{mensaje}: ").strip()
            if not texto:
                print("Error: el texto no puede estar vacío.")
                continue
            return texto.lower()  # Normaliza a minúsculas para comparaciones
        except KeyboardInterrupt:
            print("Error: Sistema interrumpido por el usuario")
            return None
        except IOError as e:
            print(f"Error: de entrada o salida: {e}")
            return None

# Captura los datos para una nueva tarea
# Captures data for a new task
def datos_tarea():
    titulo = captura_datos("Por favor indique el nombre del título o 'salir' para finalizar")
    if titulo is None or titulo == 'salir':
        print("Gracias por utilizar el sistema")
        return False
    descripcion = captura_datos("Por favor indique la descripción")
    if descripcion is None:
        return False
    prioridad = validar_entero("Indique la prioridad 1 = alta, 2 = media y 3 = baja")
    if prioridad is None:
        return False
    return crear_tarea(titulo, descripcion, prioridad)

# Crea una nueva tarea y la agrega al archivo JSON
# Creates a new task and adds it to the JSON file
def crear_tarea(titulo, descripcion, prioridad):
    try:
        tarea = Tarea(titulo, descripcion)
        tarea.establecer_prioridad(prioridad)
        return agregar_tarea(ruta_json, tarea.a_diccionario())
    except ValueError as e:
        print(f"Error al crear la tarea: {e}")
        return False

# Muestra todas las tareas cargadas desde el archivo JSON
# Displays all tasks loaded from the JSON file
def mostrar_tareas():
    lista_tareas = lector_json(ruta_json)
    if not lista_tareas:
        print("No hay tareas registradas.")
        return True
    for idx, tarea in enumerate(lista_tareas, 1):
        tarea_objeto = Tarea.desde_diccionario(tarea)
        print(f"\nTarea {idx}:")
        tarea_objeto.mostrar_informacion()
    return True    

# Marca una tarea como completada buscándola por título
# Marks a task as completed by searching for its title
def completar_tarea():
    lista_tareas = lector_json(ruta_json)
    if not lista_tareas:
        print("No hay tareas para completar.")
        return True
    while True:
        print("Puede escribir 'salir' para salir")
        nombre_buscar = captura_datos("Indique el nombre de la tarea a modificar")
        if nombre_buscar is None or nombre_buscar == "salir":
            print("Saliendo del buscador, muchas gracias")
            return True
        encontrado = False
        for tarea in lista_tareas:
            if nombre_buscar == tarea["titulo"].lower():  # Comparación case-insensitive
                print("Tarea encontrada:")
                tarea_objeto = Tarea.desde_diccionario(tarea)
                tarea_objeto.mostrar_informacion()
                tarea["estado"] = "completada"
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró una tarea con el título '{nombre_buscar}'")
            continue
        return escritor_tareas(ruta_json, lista_tareas, f"La tarea '{nombre_buscar}' fue actualizada y guardada")