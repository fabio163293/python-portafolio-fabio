# Captura datos desde la consola con validación
# Captures data from the console with validation
def captura_datos(mensaje):
    while True:
        try:
            texto = input(mensaje)
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

# Formatea el texto eliminando espacios extras
# Formats the text by removing extra spaces
def formato_texto(texto):
    if texto.lower() != "salir":  # Solo formatea si no es 'salir'
        print("Texto formateado para mejor uso:")
        return " ".join(texto.split())
    return texto

# Controla el flujo del programa
# Controls the program flow
def controlador():
    # Captura la frase y verifica si el usuario quiere salir
    frase = captura_datos('Escriba la frase a trabajar o "salir" para finalizar: ')
    if frase is None:  # Maneja interrupciones
        return False
    frase = formato_texto(frase)
    if frase.lower() == 'salir':
        print("Gracias por usar la aplicación")
        return False
    
    # Captura la palabra a buscar y valida
    palabra = captura_datos('Por favor indique la palabra a buscar (si ingresa más de una palabra, el sistema la tomará como una sola): ')
    if palabra is None:  # Maneja interrupciones
        return False
    palabra = "".join(palabra.split())  # Une palabras en una sola
    if not palabra:  # Valida si la palabra está vacía
        print("Error: La palabra no puede estar vacía después de formatear.")
        return True
    
    return buscador(frase, palabra)

# Busca una palabra en el texto y muestra los resultados
# Searches for a word in the text and displays the results
def buscador(texto, palabra):
    # Convierte a minúsculas para búsqueda case-insensitive
    texto_lower = texto.lower()
    palabra_lower = palabra.lower()
    
    # Busca la primera aparición y cuenta las apariciones
    indice = texto_lower.find(palabra_lower)
    if indice != -1:  # Si la palabra se encuentra
        apariciones = texto_lower.count(palabra_lower)
        imprimir_consola(texto, palabra, indice, apariciones)
    else:  # Si no se encuentra, notifica al usuario
        print(f"La palabra '{palabra}' no se encuentra en la siguiente frase:")
        print("")
        print(texto)
    return True

# Imprime los resultados de la búsqueda
# Prints the search results
def imprimir_consola(texto, palabra, indice, apariciones):
    print(f"'{palabra.title()}' se encuentra por primera vez en la posición de carácter {indice} y aparece {apariciones} veces")
    print("En la siguiente frase:")
    print(texto)
    return True

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