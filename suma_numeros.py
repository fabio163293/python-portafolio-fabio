# X numero inicial, Y numero secundario
while True:
 try:
     numero_x = float(input("Ingrese el primer numero a sumar: "))
     numero_y = float(input("Ingrese el segundo numero a sumar: "))
     resultado = numero_x + numero_y;
     print(f"La suma de {numero_x} + {numero_y} es igual a: {resultado}")
     break
 except ValueError:
    print("ingrese solo numeros. ")
    print("Intentemoslo de nuevo")