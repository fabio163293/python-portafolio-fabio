frase = input('Ingrese la frase que desea saber cuantas letras posee: ')
contero = {}

for letra in frase.lower():
    if letra != ' ' and not contero.get(letra):
       contero[letra] = 1
    elif contero.get(letra):
        contero[letra] += 1

for letra, cantidad in contero.items():
  print(f'La letra {letra} aparece {cantidad} veces')

