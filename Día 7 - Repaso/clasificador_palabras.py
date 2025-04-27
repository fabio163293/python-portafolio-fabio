#Clasificador de palabras
#Pide una frase al usuario.
#Separa las palabras.
#Clasifiqua las palabras por longitud (corta, mediana, larga).
#Guarda las clasificaciones en un diccionario.
#Imprime el diccionario al final.
def solicitud_frases():
    frase = input("Por favor indique la frase que desea trabajar: ")
    dividir_frases(frase)


def dividir_frases(frase):
    palabras = frase.split()
    #print(palabras)
    catalogo_palabras(palabras) 
    

def catalogo_palabras(lista):
    palabras_organizadas = {'palabras': [],'categoria': []}
    for i in range(len(lista)):
        if len(lista[i]) in range(5):
          palabras_organizadas['palabras'].append(lista[i])
          palabras_organizadas['categoria'].append("Corta")
        elif len(lista[i]) in range(5,10):
          palabras_organizadas['palabras'].append(lista[i])
          palabras_organizadas['categoria'].append("mediana")
        else:
          palabras_organizadas['palabras'].append(lista[i]) 
          palabras_organizadas['categoria'].append("larga")    
    imprimir_palabras(palabras_organizadas)

def imprimir_palabras(lista):
   for i in range(len(lista['palabras'])):
      print(f"La palabra {lista['palabras'][i]} es {lista['categoria'][i]}")    
   print("muchas gracias ")

solicitud_frases()

