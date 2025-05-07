from collections import Counter

# Maneja la entrada de una frase y procesa las palabras para contar frecuencias
# Handles the input of a phrase and processes words to count frequencies
def lista_palabras():
    while True:
        try:
            # Informa al usuario que se ignorarán números y cómo salir
            # Informs the user that numbers will be ignored and how to exit
            print("El sistema ignora los números y las palabras con números (o 'salir' para finalizar):")
            frase = input("Por favor indique la lista o la palabra: ")
            if frase.lower() == 'salir':  # Verifica si el usuario quiere salir
                # Muestra mensaje de despedida y termina el bucle
                # Displays farewell message and ends the loop
                print("Muchas gracias, nos vemos.")
                return False
            if not frase.strip():  # Valida que la entrada no esté vacía
                # Lanza excepción si la entrada está vacía
                # Raises exception if the input is empty
                raise ValueError("La lista no puede estar vacía.")
            # Divide la frase en palabras
            # Splits the phrase into words
            palabras = frase.split()
            # Procesa las palabras y cuenta frecuencias
            # Processes the words and counts frequencies
            palabras_filtradas = palabras_sin_numeros(palabras)
            if not palabras_filtradas:  # Verifica si la lista está vacía tras filtrar
                print("No hay palabras válidas para contar (se ignoraron números).")
                return True
            contador_frecuencias(palabras_filtradas)
            return True
        except ValueError as e:  # Maneja entradas vacías
            # Muestra el error específico
            # Displays the specific error
            print(f"Error: {e}")
            return True
        except KeyboardInterrupt:  # Maneja interrupción del usuario
            # Informa que el programa fue interrumpido
            # Notifies that the program was interrupted
            print("El sistema fue interrumpido por el usuario.")
            return False
        finally:
            # Mensaje para indicar que se puede intentar de nuevo
            # Message to indicate a new attempt is possible
            print("Continuemos")

# Filtra palabras que contienen números o son solo números
# Filters words that contain numbers or are only numbers
def palabras_sin_numeros(lista_palabras):
    # Usa comprensión de listas para excluir palabras con números
    # Uses list comprehension to exclude words with numbers
    return [palabra.lower() for palabra in lista_palabras if not palabra.isdigit() and not any(char.isdigit() for char in palabra)]

# Cuenta las frecuencias de las palabras usando Counter y las imprime
# Counts the frequencies of words using Counter and prints them
def contador_frecuencias(lista):
    # Crea un Counter con la lista de palabras
    # Creates a Counter with the list of words
    frecuencia = Counter(lista)
    # Ordena e imprime las frecuencias
    # Sorts and prints the frequencies
    for palabra, freq in frecuencia.most_common():
        print(f"La palabra '{palabra}' tiene una frecuencia de {freq}")

def main():
    # Inicia un bucle para permitir múltiples intentos
    # Starts a loop to allow multiple attempts
    while True:
        if not lista_palabras():
            break

if __name__ == '__main__':
    # Ejecuta el programa si se llama directamente
    # Runs the program if called directly
    main()