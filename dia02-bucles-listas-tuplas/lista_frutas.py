#Lista de fruta y remplazar un elemento
tupla_frutas = ('Guineo','Toronja','Mandarina')
lista_frutas = ['Manzna','Pera','Aguacate','Mandarina']
print(lista_frutas)
lista_frutas.insert(0,'Manzana')
print(lista_frutas)
lista_frutas.extend(tupla_frutas)
print(lista_frutas)
lista_frutas.pop(-1)
print(lista_frutas)
