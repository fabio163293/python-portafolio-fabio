# Sistema de calificaciones UAPA
# UAPA grading system
estudiantes = {'nombres': [],
                'matematicas': [],
                'espanol': [],
                "aprobado": []            
                }
contador = 0
alumno_estrella = 0
# bucle para indicar cuantos estudiantes vamos a calificar
while True:
 try:
    cantidad_estudiante = int(input("Ingrese el numero de estudiante a calificar: "))
    if cantidad_estudiante < 0:
        print("El numero no puede ser negativo")        
        continue
    break
 except ValueError:
    print("La cantidad debe ser digitada en numeros ")
    continue 

 # bucle para agregarlos al diccionario
 # Loop to add them to the dictionary        
while contador < cantidad_estudiante:
   try:
        nombre = input("Por favor ingresar el nombre del estudiante: ")
        calificacion_mat = int(input("ingrese la calificacion de matematica: "))
        calificacion_esp = int(input("ingrese la calificacion de español: "))
        estudiantes["nombres"].insert(contador, nombre)
        estudiantes["matematicas"].insert(contador, calificacion_mat)
        estudiantes["espanol"].insert(contador, calificacion_esp)
        nota = (calificacion_esp + calificacion_mat)/2
        notacomparacion = 0
        #verificamos los estudiantes que aprobaron
        #We check the students who passed
        if(nota >= 70):
         estudiantes["aprobado"].insert(contador, "Aprobado")
        else:
         estudiantes["aprobado"].insert(contador, "Aprobado")
         #guardamos el indice del estudiante con la mayor nota
         #We store the index of the student with the highest grade        
        if notacomparacion < nota:
           alumno_estrella = contador   
        contador += 1
                
   except ValueError:
        print("Las notas deben de ser ingresadas en numeros: ") 
        continue
           
for nombre, matematica_cal, espanol_cal, aprobado in zip(estudiantes['nombres'],
estudiantes['matematicas'],estudiantes["espanol"],estudiantes["aprobado"]):
   
   print(f"El estudiante {nombre} fue {aprobado}")
   print(f"Matematicas: {matematica_cal}")
   print(f"Español: {espanol_cal}")

print(f"Nuestro alumno con la mayor calificacion es {estudiantes['nombres'][alumno_estrella]}")   


