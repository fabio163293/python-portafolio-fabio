#Crear una Clase 'Estudiante'
#Create a class 'Student'

class estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_estudiante(self):
        print(f"El estudiante {self.nombre} esta en la carrera de {self.carrera} y tiene una edad de {self.edad} años ")   


estudiante1 = estudiante("Fabio", 32, "Ingenieria en Software")        
estudiante1.mostrar_estudiante()