#Decir si el numero ingresado es par o impar
while True:
 try:
   numero = int(input("Ingrese el número que desea saber si es par o impar: "))
   if(numero % 2 ==0):
    print(f"El número: {numero} es par")
    break
   else:
    print(f"El número: {numero} es impar")
    break
 except ValueError:
  print(f"El valor ingresado no es un numero")
