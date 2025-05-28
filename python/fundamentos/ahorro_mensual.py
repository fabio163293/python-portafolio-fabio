#ahorro mensual
while True:
 try:
     nombre = input("Por favor ingresar su nombre: ")
     monto_ahorrar = float(input("Ingrese el monto a ahorrar mensual: "))
     meta_ahorro = float(input("Ingrese la meta a ahorrar: "))

     if monto_ahorrar > meta_ahorro:
            print("⚠️ El monto a ahorrar no puede ser mayor que la meta.")
            continue
     
     meses = meta_ahorro/ monto_ahorrar
     
     print(f"\n Hola {nombre}, el monto ahorrar es de RD${monto_ahorrar:.2f}.")
     print(f" la meta ahorrar es de RD${meta_ahorro})")
     print(f" Tardarias {meses:.2f} meses en ahorrar la meta\n")
     break
 except ValueError:
    print("ingrese los valores correctos. ")
    print("Intentemoslo de nuevo")