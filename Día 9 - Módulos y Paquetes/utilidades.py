#imprime una linea
#Print a line
def mostrar_line():
    print(" ")

#recibe el mensaje a mostrar y devuelve el valor ingresado si es un entero
#Receives the message to display and returns the entered value if it is an integer
def validar_entero(mensaje):
    while True:
        try:
            entero = int(input(f"{mensaje}"))
            return entero
        except ValueError:
            print("Solo se pueden ingresar numeros ")
            print("Por favol vuelva a intentar")    

#formato para indicar la informacion de una persona 
#Format to display a person's information
def formato_mensaje(nombre, edad, carrera = 'desconocida'):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Carrera: {carrera}")  

def main():
    #ejemplo de uso
    formato_mensaje(f"Maria", 17 )
    mostrar_line()
    formato_mensaje(f"Pedro", 28, "Derecho" )
    mostrar_line()
    #recibimos la edad para utilizarla
    edad = validar_entero("por favor indique la edad de la persona")
    formato_mensaje(f"Fabio", edad, "Ingenieria en software")
    numero_sumar1 = validar_entero("Ingrese el numero a sumar")
    numero_sumar2 = validar_entero("Ingrese el siguiente numero para sumar")

    print(f"La suma de {numero_sumar1} + {numero_sumar2} es: {(numero_sumar1 + numero_sumar2)} ")



if __name__ =="__main__":
    main


                