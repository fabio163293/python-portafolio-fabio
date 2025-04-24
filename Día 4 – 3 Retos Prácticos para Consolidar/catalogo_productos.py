productos = {'nombre':["Manzana","Pera","Aguacate"], 'precio':[85,100,45] }
print("Bienbenido al catalogo de nuestros productos ")

while True:
    try:
     encontrado = False 
     print("Opcion 1 ver catalogo")
     print("Opcion 2 buscar productos")
     print("opcion 3 Agregar o actualizar precio  ")
     opcion = int(input("por favor elija la opcion: "))
     if(opcion == 1):
       for nombre, precio in zip(productos["nombre"],productos["precio"]):
            print(f"El producto {nombre} tiene un costo de RD$:{precio}")
            continue
     elif(opcion == 2):
           try:
             indice = 0
             contador = 0
             producto_nombre = input("Por favor escriba el nombre del producto ")
             for nombre, precio in zip(productos["nombre"],productos["precio"]):
              if nombre.lower() == producto_nombre.lower():
                   print("producto encontrado ")
                   print(f"El producto {nombre} tinee un costo de RD$:{precio}")
                   encontrado = True;
                   cambiar = int(input(f"Si desa cambiar el costo del {nombre} marque 1 "))
                   if cambiar == 1:
                       while True:                       
                         try:
                           precio_nuevo = int(input("Ingrese el nuevo precio: "))
                           productos["precio"][contador] = precio_nuevo
                           break
                         except ValueError:
                           print("Solo puede ingresar el monto en numeros")
              contador += 1
             if False == encontrado: 
                print("producto no encontrado")  
           except ValueError:
              print("producto no encontrado")
              continue
     else:
        break

    except ValueError:
        print("Debe de ingresar los valores indicados ")
        print("Por favor vuelva a intentar ")

