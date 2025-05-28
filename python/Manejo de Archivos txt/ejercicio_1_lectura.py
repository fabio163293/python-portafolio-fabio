# Maneja la lectura de un archivo de texto y muestra sus líneas numeradas
# Handles the reading of a text file and displays its lines numbered
def leer(archivo_ruta):
    try:
        with open(archivo_ruta, "r", encoding="utf-8") as archivo:
            lineas = procesar_lineas(archivo)
            if not lineas:  # Verifica si el archivo está vacío
                print("El archivo está vacío.")
                return None
            return imprimir_lineas(lineas)
    except UnicodeDecodeError:
        try:
            print("Se utilizó codificación latin-1 debido a un error con utf-8")
            with open(archivo_ruta, "r", encoding="latin-1") as archivo:
                lineas = procesar_lineas(archivo)
                if not lineas:
                    print("El archivo está vacío.")
                    return None
                return imprimir_lineas(lineas)
        except UnicodeDecodeError:
            print(f"No se pudo decodificar {archivo_ruta} con ninguna codificación conocida.")
            return None
    except FileNotFoundError:
        print(f"Error: el archivo {archivo_ruta} no se encuentra")
        return None
    except PermissionError:
        print(f"Error: No tiene permiso para acceder a {archivo_ruta}")
        return None
    except IOError as e:
        print(f"Error de entrada/salida: {e}")
        return None
    except KeyboardInterrupt:
        print("El sistema fue interrumpido por el usuario.")
        return None

# Procesa las líneas de un archivo eliminando espacios innecesarios
# Processes the lines of a file by removing unnecessary spaces
def procesar_lineas(archivo):
    return [linea.strip() for linea in archivo]

# Imprime las líneas numeradas
# Prints the lines with numbering
def imprimir_lineas(lineas):
    for numero, linea in enumerate(lineas, 1):
        print(f"{numero}-{linea}")
    return True  # Retorno para indicar éxito

# Ruta del archivo (puedes modificarlo según tu sistema)
# File path (can be modified according to your system)
ruta = r"C:\Users\Fabio Alvarez\Pictures\dia_17\tareas.txt"
leer(ruta)

