#Recorrer lista e imprimir solo pares
#Convertir lista a tupla y viceversa

while True:
 try:
    contador= int(input("Ingrese la cantidad de elementos a ingresar: "))
    break  
 except ValueError:
  print("Solo puede ingresar números")
  print("Por favor vuelva a intentar")

lista_temporar = []
for i in range(contador):
 try:
    elemento = int(input(f"Ingrese el elemento {(i + 1): }"))
    lista_temporar.append(elemento)
 except ValueError:
  i = i - 1  
  print("Solo puede ingresar números")
  print("Por favor vuelva a intentar")
 
#combertir en tupla

tupla_numeros = tuple(lista_temporar)
#imprimir elementos pares
for numeros in tupla_numeros:
  if numeros % 2 == 0:
     print(f"{numeros}")





