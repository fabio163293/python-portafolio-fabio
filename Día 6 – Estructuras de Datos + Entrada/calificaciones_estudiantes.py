def estudiante_cantidad():
    while True:
     try:
       print("Solo se aceptan numeros:")
       estudiantes = int(input("ingrese la cantidad de estudiantes a calificar: ")) 
       if(estudiantes in range(101) and estudiantes != 0):
            calificaciones(estudiantes)
            break
       else:
           print("los estudiantes no pueden ser menor de 0 nni mayor de 100")
     except ValueError:
       print("El sistema no acepta letras para la cantidad")
       print("vuelva a intentar.")

def calificaciones(estudiantes):               
    calificados = 1
    lista_estudiante = {'nombres':[] , 'calificacion':[]}
    while calificados <= estudiantes : 
        nombre_estudiante = "Nombre_invalido"
        calificacion = 0
        nombre_estudiante = input("Ingrese el nombre del estudiante ")
        while True:
           try:
              #print("Las calificaciones son de 0 a 100, cualquier otro monto dara error ")
              calificacion = int(input(f"Ingrese la nota de el estudiante {nombre_estudiante}: "))
              if (calificacion in range(101)):
                 print = ("Calificacion guardada. ")
                 lista_estudiante["nombres"].append(nombre_estudiante)
                 lista_estudiante["calificacion"].append(calificacion)
                 calificados += 1
                 break
              else:
                 print("El valor ingresado es incorrecto, valor de 0 a 100 ")
           except ValueError:
              print("Los valores no pueden ser en letras:")  
    crear_documento(lista_estudiante)

def crear_documento(lista_estudiante):
   with open ('calificaciones.txt', 'w') as escribir_archivo:
      for clave, valor in lista_estudiante.items():
         escribir_archivo.write(f"{clave}: {valor} \n")
         escribir_archivo.write("\n")
    

         
   print("Datos actualizados")                          

estudiante_cantidad()