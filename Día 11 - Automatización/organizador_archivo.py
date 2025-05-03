#!python
import os

#imprime por consola la ruta usada

def imprimir_ruta():
    mi_ruta = os.getcwd()
    print(mi_ruta)

#crear estructura de carpetas
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

def renombrar_archivo(directorio, prefijo):
    for archivo in os.listdir(directorio):
        if os.path.isfile(directorio, archivo):
            nuevo_nombre = f"{prefijo}_{archivo}"
            os.rename(
                os.path.join(directorio, archivo),
                os.path.join(directorio , nuevo_nombre)
            )
        print(f"renombrado: {archivo} a {nuevo_nombre}")        

#Busca archivos por extension y te dice su ruta actual
#
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
    categorias = {
        '.jpg': 'imagenes',
        '.png': 'imagenes',
        '.pdf': 'documentos',
        '.txt': 'documentos'
    }
    
    # Crear carpetas si no existen
    for carpeta in set(categorias.values()):
        os.makedirs(os.path.join(directorio, carpeta), exist_ok=True)
    
    # Mover archivos
    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            if extension in categorias:
                destino = os.path.join(directorio, categorias[extension], archivo)
                os.rename(ruta_archivo, destino)
                print(f'Movido: {archivo} -> {categorias[extension]}')

organizar_archivos('.')    



             