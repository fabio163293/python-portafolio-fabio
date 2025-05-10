# Captura datos desde la consola con validación
# Captures data from the console with validation
def captura_datos(mensaje):
    while True:
        try:
            texto = input(mensaje)
            if texto.lower() == 'salir':
                print("Gracias por usar nuestra aplicación")
                return None
            if not texto.strip():  # Valida que el texto no esté vacío
                print("Debe ingresar por lo menos una palabra: ")
                continue
            return texto
        except KeyboardInterrupt:  # Maneja interrupción del usuario
            print("Sistema interrumpido por el usuario")
            return None
        except IOError as e:  # Maneja errores de entrada/salida
            print(f"Error: Error de entrada o salida: {e}")
            return None

# Controla el flujo del programa
# Controls the program flow
def controlador():
    print("Siempre que se le solicite texto, si ingresa la palabra 'salir' finalizará el sistema")
    texto = captura_datos('Escriba el texto: ')
    if texto is None:  # Maneja interrupciones
        return False
    
    # Formatea el texto original y una versión en minúsculas para la búsqueda
    texto_formateado = " ".join(texto.split())
    texto_lower = texto_formateado.lower()
    print("Texto formateado para mejor uso:", texto_formateado)
    
    print("Los siguientes datos ingresados se tomarán como una palabra")
    palabra = captura_datos('Por favor indique la palabra a reemplazar: ')
    if palabra is None:  # Maneja interrupciones
        return False
    palabra_lower = "".join(palabra.lower().split())
    if not palabra_lower:  # Valida si la palabra está vacía después de formatear
        print("Error: La palabra no puede estar vacía después de formatear.")
        return True
    
    # Verifica si la palabra existe en el texto (case-insensitive)
    if texto_lower.find(palabra_lower) == -1:
        print(f"La palabra '{palabra}' no se encuentra en el siguiente texto: ")
        print(texto_formateado)
        print("Gracias por usar nuestro programa")
        return True
    
    print("Los datos siguientes ingresados se tomarán como una palabra")
    palabra_remp = captura_datos("Ingrese la nueva palabra: ")
    if palabra_remp is None:  # Maneja interrupciones
        return False
    palabra_remp_lower = "".join(palabra_remp.split())
    if not palabra_remp_lower:  # Valida si la palabra está vacía después de formatear
        print("Error: La palabra no puede estar vacía después de formatear.")
        return True
    
    # Realiza el reemplazo en el texto original (case-insensitive)
    resultado = texto_formateado.replace(palabra_lower, palabra_remp_lower, 1)  # Reemplaza solo la primera aparición para prueba
    guardar_en_archivo(resultado)
    return True

# Reemplaza una palabra en el texto
# Replaces a word in the text
def reemplazar_palabra(texto, palabra, palabra_rempl):
    return texto.replace(palabra, palabra_rempl)

# Guarda el texto en un archivo en modo append con salto de línea
# Saves the text to a file in append mode with a newline
def guardar_en_archivo(texto, nombre_archivo="resultado.txt"):
    try:
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")  # Añade salto de línea
        print(f"Resultados guardados exitosamente en '{nombre_archivo}'.")
        print(f"Resultado guardado: {texto}")
        return True
    except PermissionError:  # Maneja error de permisos
        print(f"Error: No tienes permisos para escribir en el archivo '{nombre_archivo}'.")
        return False
    except IOError as e:  # Maneja errores de entrada/salida
        print(f"Error de entrada/salida al guardar el texto: {e}")
        return False
    except Exception as e:  # Maneja otros errores inesperados
        print(f"Ocurrió un error al guardar los resultados: {e}")
        return False

def main():
    # Inicia un bucle para permitir múltiples intentos
    # Starts a loop to allow multiple attempts
    while True:
        if not controlador():
            break
        print("\nVolvamos a intentar.")

if __name__ == '__main__':
    # Ejecuta el programa si se llama directamente
    # Runs the program if called directly
    main()