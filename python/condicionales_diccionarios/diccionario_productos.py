#Diccionario de productos (nombre: precio)
#Product dictionary (name: price)
#Solicita un producto al usuario y devuelve el precio o un mensaje si no existe
productos = {'nombres': ['Pera','Aguacate','tv'], 'precios': [25, 50, 1500] }
while True:
    producto = input('Ingrese el nombre del producto buscado: ')
    producto_seleccionado =['Producto no encontrado',0]
    for nombre, precio in zip(productos['nombres'], productos['precios']):
      if nombre == producto:
        producto_seleccionado = [nombre,precio]
        print(f'El producto {nombre} tiene un costo de RD${precio}')
        break
    print(f'{producto_seleccionado[0]}')    
        
