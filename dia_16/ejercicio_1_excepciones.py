# Recibe datos por teclado y valida que sean números
# Receives data from the keyboard and validates that they are numbers
def numero_cuadrado():
    while True:
        try:
            entrada = input("Por favor indique el número a calcular su cuadrado o (salir para finalizar): ")
            if entrada.lower() == 'salir':
                print("Gracias por utilizar el sistema: ")
                break
            if not entrada.strip():
                raise ValueError('vacia')
            numero = int(entrada)
        except ValueError as e:
            if str(e) == 'vacia':
                print("Error: La entrada no puede estar vacía: ")
            else:
                print("Error: La entrada debe ser un número válido: ")
            continue
        except KeyboardInterrupt:
            print("El sistema fue interrumpido por el usuario: ")
            break
        else:
            print(f"El cuadrado de {numero} es {numero * numero}")
            continue        
        finally:
            print("Volvamos a intentar: ")    
    print("Gracias por utilizar el sistema: ")

def main():
    numero_cuadrado()

if __name__ == '__main__':
    main()
