# Captura texto desde la consola, lo formatea y lo muestra
# Captures text from the console, formats it, and displays it
def capturar_texto():
    while True:
        try:
            # Solicita al usuario un texto o la opción de salir
            # Requests the user to input text or the exit option
            texto = input("Por favor indique el texto a formatear o 'salir' para finalizar: ")
            if texto.lower() == 'salir':  # Verifica si el usuario quiere salir
                # Muestra mensaje de despedida y termina
                # Displays farewell message and ends
                print("Finalizando el sistema:")
                return False
            if not texto.strip():  # Valida que el texto no esté vacío
                # Notifica al usuario y solicita nuevo ingreso
                # Notifies the user and requests new input
                print("El texto no puede estar vacío: ")
                continue
            # Limpia espacios extras y formatea el texto
            # Cleans extra spaces and formats the text
            texto_limpio = " ".join(texto.split())
            texto_formateado = texto_limpio.title()
            # Muestra el texto formateado con confirmación
            # Displays the formatted text with confirmation
            print(f"Texto formateado: {texto_formateado}")
        except KeyboardInterrupt:  # Maneja interrupción del usuario
            # Informa que el programa fue interrumpido
            # Notifies that the program was interrupted
            print("El usuario ha detenido el programa")
            return False

def main():
    # Inicia un bucle para permitir múltiples intentos
    # Starts a loop to allow multiple attempts
    while True:
        if not capturar_texto():
            break
        print("\nVolvamos a intentar.")

if __name__ == '__main__':  # Corrige el uso de paréntesis
    # Ejecuta el programa si se llama directamente
    # Runs the program if called directly
    main()