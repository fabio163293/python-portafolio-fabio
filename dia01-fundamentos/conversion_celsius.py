# Conversor de grados Fahrenheit a Celsius
#C = (F - 32) / 1.8
while True:
 try:
     numero_f = float(input("Ingrese el número en fahrenheit: "))
     numero_c = (numero_f - 32)/1.8
     print(f"🌡️ El número {numero_f:.1f}°F es igual a {numero_c:.2f}°C en Celsius.\n")     
     break
 except ValueError:
    print("ingrese solo números. ")
    print("Intentemoslo de nuevo")