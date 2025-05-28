#Crear tabla separada por comas.
#Create a comma-separated table.
import csv
tabla = [['nombre', ['ciudad']],
         ['fabio','Villa altagracia'],
         ['carlina'], ['Villa altagracia']]

def escribir_archivo(tabla):
    try:
        with open('crear_tablas.txt', 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter=',')
            for fila in tabla:
               escritor.writerow(fila)
    except Exception as e:
        print(f"ocurrio un error: {e}")
escribir_archivo(tabla)
print("Archivo 'crear_tablas' creado con exito")

