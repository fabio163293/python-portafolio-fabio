#Diccionario de estudiantes
#Student dictionary
estudiantes = {'nombres': ['Fabio','Pedro','Maria', 'jose'], 'calificaciones': [84, 80, 99, 95] }
comparacion = 0
nombre_selección = 'Ningun usuario'
#bucle para buscar dentro de la listas del diccionario 
#Loop to search within the dictionary's lists
for nombre, elemento in zip(estudiantes['nombres'], estudiantes['calificaciones']):
   #selecciona el estudiante con mayor nota
   #Select the student with the highest grade
   if elemento > comparacion:
      comparacion = elemento
      nombre_selección = nombre 

print(f"El estudiante con la mayor nota es {nombre_selección} con un {comparacion} ")