# Calculadora de cociente y residuo entre dos números
while True:
 try:
     numero_dividir = float(input("Ingrese el número a dividir: "))
     numero_divisor = float(input("Ingrese el número divisor: "))
     cociente_division = numero_dividir / numero_divisor
     residuo = numero_dividir % numero_divisor
     print(f" La división de {numero_dividir} ÷ {numero_divisor} es: {cociente_division:.2f}")
     print(f" El residuo es: {residuo:.2f}\n")
     break
 except ZeroDivisionError:
    print("Los números no se pueden dividir entre 0 ")
    print("Intentemoslo de nuevo")
 except ValueError:
    print("ingrese solo números. ")
    print("Intentemoslo de nuevo")