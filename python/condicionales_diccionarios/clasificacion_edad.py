#Solicita una edad y clasifica como niño, adolescente, adulto, adulto mayor (usando condicionales anidadas)
#Request an age and classify as child, teenager, adult, or senior (using nested conditionals)
mensaje = ("vuelve a intentarlo ")
while True:
    try:
     edad = int(input("Ingrese la edad del usuario: "))
     if(edad < 0):
      print("la edad debe de ser igual o mayor que 0") 
      print(f"mensaje")
      continue
     #clasificacion segun edad
     #classification according to age
     elif edad <= 12:
        print("Clasificación: Niño")
     elif edad <= 17:
        print("Clasificación: Adolescente")
     elif edad <= 59:
        print("Clasificación: Adulto")
     else:
        print("Clasificación: Adulto mayor")
     break
      
    except ValueError:
     print("Ingrese valores en numeros")
     print(f"{mensaje}")

