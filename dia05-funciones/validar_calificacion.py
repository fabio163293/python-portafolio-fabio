#Validador de calificaciones
#Grade Validator
#Función que recibe una calificación y devuelve si es válida y su categoría (excelente, aprobado, reprobado)
#Function that receives a grade and returns whether it is valid and its category (excellent, passed, failed)
def captura_datos():
    try: 
        print("al ingresar cualquier dato que no sea numero el sistema cerrara")
        dato = int(input("Por favor ingrese el dato a calificar en el sistema de 0 a 100 "))
        if(dato in range(101) ):
          categoria(dato)
        else:
            print("El rango de valor es de 0 a 100")
            print("Volvamos a intentar")
            captura_datos()
    except ValueError:
        print("Muchas Gracias")
        
def mensaje_nota(calificacion, letra, nivel):
    print(f"El alumno fue {nivel} su calificacion es {calificacion} {letra}") 
def categoria(calificacion):
     if (calificacion in range(61) ):
         mensaje_nota(calificacion, "F", "reprobado")
         captura_datos()
     elif (  70 >= calificacion and calificacion  <= 79):
         mensaje_nota(calificacion, "C", "aprobado apenas" )
         captura_datos()
     elif (  80 >= calificacion and calificacion  <= 89):
         mensaje_nota(calificacion, "B", "aprobado" )
         captura_datos()
     elif (  90 >= calificacion and calificacion  <=99):
         mensaje_nota(calificacion, "A", "aprobado" )
         captura_datos()
     else:       
        mensaje_nota(calificacion, "A", "aprobado con exelencia" )
        captura_datos()

captura_datos()        