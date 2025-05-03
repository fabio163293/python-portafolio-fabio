#!python
#uso para que el sistema sepa que debe utilizar Python y evitar errores de caracteres
#Used so the system knows to use Python and to avoid character encoding errors
import os

#imprime por consola la ruta usada
#Print the used path to the console
def imprimir_ruta():
    mi_ruta = os.getcwd()
    print(mi_ruta)

#crear estructura de carpetas
#Create folder structure
def crear_estructura(nombre_estructura):
    carpetas = [

        f'{nombre_estructura}/data/raw',
        f'{nombre_estructura}/data/processed',
        f'{nombre_estructura}/logs',
        f'{nombre_estructura}/src'

    ]

    for carpeta in carpetas:
        os.makedirs(carpeta, exist_ok=True)
        print(f'Creada/existe: {carpeta}')

#renombra archivos con un prefijo mas su nombre
#Rename files with a prefix plus their name
def renombrar_archivo(directorio, prefijo):
    for archivo in os.listdir(directorio):
        if os.path.isfile(archivo):
            nuevo_nombre = f"{prefijo}_{archivo}"
            os.rename(
                os.path.join(directorio, archivo),
                os.path.join(directorio , nuevo_nombre)
            )
            print(f"renombrado: {archivo} a {nuevo_nombre}")        

#Busca archivos por extension y te dice su ruta actual
#Search for files by extension and display their current path
def buscar_archivo(directorio, extension):
    encontrados = []
    for ruta, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(extension):
                ruta_completa = os.path.join(ruta, archivo)
                encontrados.append(ruta_completa)
    return encontrados

archivos_txt = buscar_archivo('.', '.txt')
for archivo in archivos_txt:
    print(archivo)

def organizar_archivos(directorio):
    # Diccionario de extensiones y carpetas destino
    # Dictionary of extensions and destination folders
    categorias = {
        '.jpg': 'imagenes',
        '.png': 'imagenes',
        '.pdf': 'documentos',
        '.txt': 'documentos'
    }
    
    # Crear carpetas si no existen
    # Create folders if they do not exist
    for carpeta in set(categorias.values()):
        os.makedirs(os.path.join(directorio, carpeta), exist_ok=True)
    
    # Mover archivos
    # Move files
    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            if extension in categorias:
                destino = os.path.join(directorio, categorias[extension], archivo)
                os.rename(ruta_archivo, destino)
                print(f'Movido: {archivo} -> {categorias[extension]}')

def main():
   #ejemplo de uso
   #Example of use
   imprimir_ruta()
   crear_estructura('dia_11')
   renombrar_archivo('.', 'backup')
   organizar_archivos('.')
   buscar_archivo('.','.txt')


        


if __name__ == "__main__":
    main()