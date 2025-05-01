#Crear una Clase 'Producto'
#Create a class 'Product'

class producto:
    def __init__(self, nombre, precio, stock ):
        self.nombre = nombre
        self.precio = precio
        self._stock = stock
    
    def get_stock(self):
        return self._stock
    # Método para mostrar información del producto
    # Method to display product information
    def mostrar_producto(self):
        print(f"El producto {self.nombre} tiene un costo de RD${self.precio} y {self._stock} unidades disponibles")
    #Método para actualizar el stock
    #Method to update the stock
    def actualizar_stock(self, cambio):
        self._stock = self._stock + cambio
        print("producto actualizado")
        self.mostrar_producto()
    #Método para capturar los datos para actualizar el stock
    #Method to capture the data to update the stock
    def entrada_datos(self):
        print("El valor solo puede ser en numeros con el signo - para restar y sin signo para sumar ")
        while True:
            try:        
              cambio = int(input(f"Por favor indique el cambio recibido por {self.nombre} en su stock: "))
              return self.actualizar_stock(cambio)
            except ValueError:
                print("Solo puede ingresar numeros")
                print("vuelva a intentar ")

producto1 = producto("Pera", 45, 100)
producto1.mostrar_producto()
producto1.entrada_datos()                 