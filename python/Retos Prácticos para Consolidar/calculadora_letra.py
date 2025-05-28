#contador de letras
#Word counter
constante = {}
numeros = {'1','2','3','4','5','6','7','8','9','0' }
vocales = {'a': 0 , 'e': 0, 'i': 0, 'o': 0, 'u': 0 }
frecuencia_mayor = "z"
contador_frecuencia = 0

frase = input('Ingrese la frase que desea saber cuantas letras posee: ')
print("Frase aceptada ")

for letra in frase.lower():
    if letra in numeros:
       print("Los numeros son ignorados") 
    elif letra in vocales:
        vocales[letra] += 1
        if vocales[letra] > contador_frecuencia:
            contador_frecuencia = vocales[letra]
            frecuencia_mayor = letra
    elif letra.isalpha() and not constante.get(letra):
        constante[letra] = 1
    elif letra.isalpha() and constante.get(letra): 
        constante[letra] +=1
        if constante[letra] > contador_frecuencia:
            contador_frecuencia = constante[letra]
            frecuencia_mayor = letra


for letra, cantidad in constante.items():
  print(f'La costante {letra} aparece {cantidad} veces')

for letra, cantidad in vocales.items():
  print(f'La vocal {letra} aparece {cantidad} veces')

print(f"la vocal {frecuencia_mayor} es la mas utilizada en la frase")
