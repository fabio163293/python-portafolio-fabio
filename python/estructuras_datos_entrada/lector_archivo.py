#	Leer archivo .txt con productos y mostrar en consola.
# Read a .txt file with products and display it in the console.
with open ('productos.txt', 'r') as leer_archivo:
     for linea in leer_archivo:
        print(linea.strip())
