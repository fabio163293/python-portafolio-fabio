#Objetivo: Aplicar variables, condicionales, bucles, funciones, estructuras de datos y archivos.
#Permita registrar nombre y nota de varios estudiantes.
#Clasifique las notas: Excelente, Aprobado, Reprobado.
#Guarde la información en un archivo .txt.
#Permita buscar un estudiante específico y mostrar su clasificación.
#Muestre el estudiante con la mayor nota.
import csv
def cantidad_estudiantes ():
    print("El sistema solo recibe numeros en esta parte.")
    while True:
        try:
          cantidad = int(input(("por favor indique la cantidad de estudiantes a calificar: ")))
          if cantidad > 0:         
            print("cantidad aceptada.")
            return lista_estudiante(cantidad)
          else:
             print("La cantidad ingresada debe ser mayor a 0")   
        except ValueError:
           print("El valos a ingresar debe ser solamente numeros")

def lista_estudiante (cantidad):
   contador = 1
   estudiante = "nombre invalido"
   calificacion = 0
   evaluacion = "No fue evaluado"
   lista_estudiantes = {'nombres': [], 'calificaciones': [], "evaluaciones": []}
   while cantidad >= contador:
          while True:  
            try:
              estudiante = input("Por favor ingrese el nombre del estudiante: ")
              break            
            except Exception as e:
              print(f"ocurrio el error {e}")
          while True:
             try:
                calificacion = int(input("Por favor ingrese la calificacion: "))
                if calificacion in range(101):
                   print("Estudiante calificado")
                   evaluacion = calificacion_estudiante(calificacion)
                   lista_estudiantes["nombres"].append(estudiante.lower())
                   lista_estudiantes["calificaciones"].append(calificacion)
                   lista_estudiantes["evaluaciones"].append(evaluacion)
                   contador += 1
                   break
                else: 
                   print("La nota solo acepta el rango desde 0 a 100")
             except ValueError:
                print("El valor debe ser ingresado en numeros")
   guardar_lista(lista_estudiantes)
                

def calificacion_estudiante(calificacion):
   if calificacion in range (69):
      return "Reprobado F"
   elif calificacion in range(70,79):
      return "Aprobado c"
   elif calificacion in range (80,89):
      return "Aprobado B"
   elif calificacion in range (90, 99):
      return "Aprobado A"
   else:
      return "Aprobado exelente A"                         

def guardar_lista (lista):
   try:
        with open('calificaciones.txt', 'w', encoding='utf-8') as archivo:
            # Escribir encabezado
            archivo.write("Nombre\tCalificación\tEvaluación\n")
            archivo.write("-" * 50 + "\n")
            # Escribir datos
            for i in range(len(lista['nombres'])):
                archivo.write(f"{lista['nombres'][i]}\t"
                             f"{lista['calificaciones'][i]}\t"
                             f"{lista['evaluaciones'][i]}\n")
        print(f"Datos guardados exitosamente en calificaciones")
   except Exception as e:
        print(f"Error al guardar el archivo: {e}")
   buscar_estudiante(lista)


def buscar_estudiante(lista):
   nombre_estudiante = "Nombre invalido"
   while True:
      print("Escribir cerrar para poder salir del sistema")       
      nombre_estudiante = input("Por favor indique el nombre del estudiante que desea buscar : ")
      if nombre_estudiante.lower() != "cerrar":
          for i in range(len(lista['nombres'])):
                validar = 0
                if nombre_estudiante.lower() == lista['nombres'][i]:
                  print(f"El estudiante {nombre_estudiante}, tiene una calificacion de {lista['calificaciones'][i]} y fue {lista['evaluaciones'][i]}")
                  validar = 1
                  break
          if validar != 1:
              print("El estudiante no fue encontrado")
      else:
         print("muchas gracias")
         break
   mayor_nota(lista)   


def mayor_nota(lista):
   mayor = 0
   posicion = 0
   for i in range (len(lista['nombres'])):
       if lista['calificaciones'][i] > mayor:
           mayor = lista['calificaciones'][i]
           posicion = i
   print(f"El estudiante con la calificacion mayor es {lista['nombres'][posicion]} con la calificacion: {lista['calificaciones'][posicion]}")        


cantidad_estudiantes()