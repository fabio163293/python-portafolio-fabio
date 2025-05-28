def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(f"{mensaje}" ))
            if valor > 0:
                return valor
            else: print("El valor debe ser mayor que 0 ")
                          
        except ValueError:
                print("El valor ingresado solo debe ser numeros")   

estudiante = {'nombre': 'sin_nombre',
 'edad': 0,
 'cursos': ['matematica','español', 'sociales'],
  'nota':[0,0,0,],
 'promedio' : 0  }                

materias = estudiante.get('cursos',[])
cantidad_notas = len(materias)
lista_notas = estudiante.get('nota',[])
def cantidad_estudiante():
    valor = validar_entero("Por favor indique la cantidad de estudiante a ingresar. ")
    return valor

def llenar_lista(cantidad):
   lista_estudiantes = []
   contador = 1
   while contador <= cantidad:
       nombre, edad, notas, promedio = capturar_estudiantes()
       estudiante['nombre'] = nombre
       estudiante['edad'] = edad
       estudiante['nota'] = notas
       estudiante['promedio'] = promedio
       lista_estudiantes.append(estudiante)
       print(f"el estudiante {estudiante['nombre']} tine un promediod {estudiante['promedio']} ")
       print("Fue guardado con exito")
       contador = contador + 1
   return lista_estudiantes 


def capturar_estudiantes():
    nombre = input("Por favor indique el nombre del estudiante: ")
    edad = validar_entero("por favor indique la edad del estudiante: ")
    notas = agregar_notas(lista_notas,cantidad_notas)
    if notas:
       promedio = sum(notas) / len(notas)

    return nombre, edad, notas, promedio



def agregar_notas(notas,cantidad):
    cantidad
    notas.clear()  
    for i in range(cantidad):
        try:
           nota = float(validar_entero(f"Ingrese la nota para {materias[i]}: "))
           notas.append(nota)
        except ValueError:
           print("Entrada inválida, se asignará 0")
           notas.append(0)   
    return notas       

def eliminar_key(key):
    valor = estudiante.pop(key, "none") 
    if valor == "none":
        return print("El campo no fue encontrado")
    else:
        print("Eliminada con exito ")

def buscar_estudiante(lista_estudiante):
    nombre = input("por favor indique el nombre a buscar: ")
    for estu in lista_estudiante:
        if estu['nombre'] == nombre:
            print(f"El estudiante {nombre}:")
            print(f"Tiene un promedio de {estu['promedio']}")

def main():
    
   lista_prueba =llenar_lista(validar_entero("Ingrese la cantidad de estudiantes a registrar "))
   buscar_estudiante(lista_prueba)
    
   print(estudiante)
   estudiante.update( {'nombre' : 'Jose'})
   print(estudiante)
   eliminar_key('nombre')
   print(estudiante)
   print(eliminar_key('nombre'))
   print(estudiante)
     

if __name__ == '__main__':
    main()