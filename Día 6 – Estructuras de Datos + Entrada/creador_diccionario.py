#Leer archivo con líneas clave:valor y construir un diccionario.
#Read a file with key:value lines and build a dictionary.
import ast
calificaciones = {}
with open('calificaciones.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            clave, valor = linea.split(':', 1)
            valor_lista = ast.literal_eval(valor.strip())
            calificaciones[clave.strip()] = valor_lista

print(calificaciones)
