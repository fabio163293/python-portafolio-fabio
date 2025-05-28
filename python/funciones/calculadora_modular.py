def sumar (x, y):
    return print(f"La suma de {x} y {y} es {(x + y)}")
def restar (x, y):
    return print(f"La resta de {x} y {y} es {(x - y)}")
def multiplicar (x, y):
    return print(f"La multiplicacion de {x} y {y} es {(x * y)}")
def dividir (x, y):
    return print(f"La division  de {x} y {y} es {(x / y)} y el residuo {(x % y)} ")
def salir ():
   print("muchas gracias por usar nuestra calculadora")
def reintentar ():
   print(" Volvamos a intentar")   

def seleccion ():
    try:
     print(" Por favor indique 1 para sumar")
     print(" Por favor indique 2 para restar")
     print(" Por favor indique 3 para multiplicar")
     print(" Por favor indique 4 para dividir")
     print(" por favor indique 5 para salir")
     opcion = int(input("Por favor indique su seleccion: "))
     if opcion !=5:
       x = int(input("Ingrese el numero a calcular "))
       y = int(input("Ingrese otro numero a calcular "))
       return calculadora(opcion, x, y)
     else:
        salir()    
    except ValueError:
     print(" Por favor solo ingrese numeros")
     seleccion()

def calculadora(opcion, x, y):
    if opcion == 1:
       sumar(x , y)
       seleccion() 
    elif(opcion == 2):
       restar (x, y)
       seleccion() 
    elif(opcion == 3):
       multiplicar (x, y)
       seleccion() 
    elif(opcion == 4):
       if y != 0:
        dividir (x, y)
        seleccion()
       else:
          print(f"El numero como divisor es el {y}, ningun numero puede ser dividido por {y}")
          reintentar()
          seleccion()   
    else:
       print("El numero ingresado no tiene funcion")
       seleccion() 
seleccion()
