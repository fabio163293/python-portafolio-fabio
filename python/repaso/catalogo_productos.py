#diccionario con productos : precio
#Dictionary with product: price.
productos = {'nombres': ['aguacate','melon'] , 'precios': [90, 85]}

def opciones():
    print("Por favor escriba las siguientes opciones 1 o productos para ver el catalogo")
    print("opciones 2 o buscar para buscar un producto")
    print("opciones 3 o cualquier otra entrada para salir del sitema")
    seleccion = input("Indiquenos la opcion: ")
    if seleccion == "1" or seleccion.lower() == "catalogo":
        print("Bienvenido al catalogo")
        mostrar_catalogo(productos)
    elif seleccion == "2" or seleccion.lower == "buscar":
        buscar_producto(productos)
    else:
      print("Muchas gracias")

def mostrar_catalogo (catalogo):
    for i in range(len(catalogo['nombres'])):
       print(f"el producto {catalogo['nombres'][i]} tiene un costo de {catalogo['precios'][i]}") 
    opciones()          

def buscar_producto (catalogo):
    bucle = True 
    while bucle:
       confirmar = 0
       buscar_nombre = input("Por favor indique el nombre del producto buscardo: ")
       for i in range(len(catalogo['nombres'])):
            if buscar_nombre.lower() == catalogo['nombres'][i]:
               print("Producto encontrado")
               print(f"El producto {catalogo['nombres'][i]} tiene un costo de {catalogo['precios'][i]}")
               confirmar = 1
               bucle = False
               break
       if confirmar == 0:
            print("El producto no existe ")
    opciones()

opciones()