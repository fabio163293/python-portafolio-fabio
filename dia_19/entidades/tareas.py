from datetime import datetime

# Define una clase para representar una tarea
# Defines a class to represent a task
class Tarea:
    def __init__(self, titulo, descripcion, prioridad=None, estado=None, fecha_ingreso=None):
        # Valida que el título y la descripción no estén vacíos
        # Validates that title and description are not empty
        if not titulo.strip() or not descripcion.strip():
            raise ValueError("El título y la descripción no pueden estar vacíos")
        self.titulo = titulo
        self.descripcion = descripcion
        # Usa valores pasados si existen, o valores por defecto
        # Uses passed values if they exist, otherwise defaults
        self.prioridad = prioridad if prioridad else 'baja'
        self.estado = estado if estado else 'pendiente'
        self.fecha_ingreso = fecha_ingreso if fecha_ingreso else datetime.now().strftime("%Y-%m-%d %H:%M")

    def marcar_completada(self):
        # Cambia el estado de la tarea a completada
        # Changes the task's status to completed
        self.estado = "completada"

    def mostrar_informacion(self):
        # Muestra la información de la tarea
        # Displays the task's information
        print(f"Título: {self.titulo}")
        print(f"Fecha de creación: {self.fecha_ingreso}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Descripción: {self.descripcion}")
        print(f"Estado: {self.estado}")
      
    def a_diccionario(self):
        # Convierte la tarea a un diccionario para guardar en JSON
        # Converts the task to a dictionary for JSON storage
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad,
            "fecha ingreso": self.fecha_ingreso,
            "estado": self.estado,
        }

    @classmethod  
    def desde_diccionario(cls, data):
        # Crea una instancia de Tarea desde un diccionario
        # Creates a Tarea instance from a dictionary
        try:
            return cls(
                data["titulo"],
                data["descripcion"],
                data.get("prioridad", "baja"),
                data.get("estado", "pendiente"),
                data.get("fecha ingreso", datetime.now().strftime("%Y-%m-%d %H:%M"))
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave {e} en el diccionario de la tarea")
  
    def establecer_prioridad(self, prioridad):
        # Establece la prioridad de la tarea según un número
        # Sets the task's priority based on a number
        try:
            prioridad = int(prioridad)  # Asegura que sea un entero
            if prioridad == 1:
                self.prioridad = 'alta'
            elif prioridad == 2:
                self.prioridad = 'media'
            else:
                self.prioridad = 'baja'
        except (ValueError, TypeError):
            self.prioridad = 'baja'  # Valor por defecto en caso de error