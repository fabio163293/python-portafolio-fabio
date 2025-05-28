#calculadora de propina
while True:
 try:
     nombre = input("Por favor ingresar su nombre")
     monto_pagar = float(input("Ingrese el monto a pagar: "))
     porcentaje_propina = float(input("Ingrese el porcentaje de la propina: "))
     propina = (monto_pagar*porcentaje_propina)/100
     total_pagar = monto_pagar+propina
     print(f"\n Hola {nombre}, la factura es de RD${monto_pagar:.2f}.")
     print(f" El porcentaje de propina elegido fue de {porcentaje_propina:.1f}% (RD${propina:.2f})")
     print(f" El monto total a pagar es: RD${total_pagar:.2f}\n")
     break
 except ValueError:
    print("ingrese los valores correctos. ")
    print("Intentemoslo de nuevo")