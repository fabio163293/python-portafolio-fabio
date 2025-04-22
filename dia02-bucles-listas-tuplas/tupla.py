#Tupla con nombre, edad, país
personas = [
    ('Fabio', 32, 'República Dominicana'),
    ('Ana', 22, 'México'),
    ('Luis', 29, 'Colombia'),
    ('María', 24, 'República Dominicana')
]
mayores_25 = 0
dominicanos = 0
for persona in personas:
 nombre, edad, pais = persona
 print("Participante de la lista")
 print(f"Nombre: {(nombre.upper)}, edad: {edad}, pais de origen: {pais}")
 #Filtro para saber si es mayor de 25
 if (edad > 25):
   print(f"{nombre.upper} tiene mas de 25 años")
   mayores_25 += 1
 #Filtro para saber si es Dominicano  
 if (pais == 'República Dominicana'):
   print(f"{nombre.upper} su nacionalidad es Dominicana")
   dominicanos += 1
if (mayores_25 == 1):
 print(f"En la lista tenemos {mayores_25}, mayor de 25 años")
else: (mayores_25 != 0)
print(f"En la lista tenemos {mayores_25}, los cuales son mayores de 25 años")
if (dominicanos == 1):
 print(f"En la lista tenemos {dominicanos} dominicano")
else: (dominicanos!=0)
print(f"En la lista tenemos {dominicanos} dominicanos")