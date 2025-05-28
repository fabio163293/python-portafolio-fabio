# Contador de vocales como función
#Crear una función que reciba un texto y devuelva cuántas vocales tiene
# Vowel counter as a function
#Create a function that receives a text and returns how many vowels it has
constante = {}
numeros = {'1','2','3','4','5','6','7','8','9','0' }
frecuencia_mayor = "z"
contador_frecuencia = 0
def captura_frase():
      print("Solo las vocales son tomadas en cuenta")
      frase = input("por favor ingrese la frase: ")
      calculadora_vocales(frase)


def calculadora_vocales(frase):
    vocales = {'a': 0 , 'e': 0, 'i': 0, 'o': 0, 'u': 0 }   
    for letra in frase.lower():
     if letra in vocales:
        vocales[letra] += 1
    print(f"Se ingresaron {suma_vocales(vocales)} vocales")
    imprimir_vocales(vocales)    
      
def suma_vocales(vocales) : 
    suma = 0
    for cantidad in vocales.values():
        print(cantidad)
        suma +=cantidad
    return suma

def imprimir_vocales(vocales):
   for letra, cantidad in vocales.items():
    print(f'La vocal {letra} aparece {cantidad} veces')


captura_frase()