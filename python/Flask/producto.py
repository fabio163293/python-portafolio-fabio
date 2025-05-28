class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        # Valida los datos de entrada
        # Validates input data
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena no vacía / Name must be a non-empty string")
        if not categoria or not isinstance(categoria, str):
            raise ValueError("La categoría debe ser una cadena no vacía / Category must be a non-empty string")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número mayor que 0 / Price must be a number greater than 0")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un número entero no negativo / Stock must be a non-negative integer")

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock        

    def mostrar_informacion(self):
        # Muestra la información del producto
        # Displays the product information
        print(f"Producto/Product: {self.nombre}")
        print(f"Categoría/Category: {self.categoria}")        
        print(f"Precio/Price: RD${self.precio}")
        print(f"Disponibles/Available: {self.stock}")
        
    def a_diccionario(self):
        # Convierte el objeto a un diccionario
        # Converts the object to a dictionary
        return {
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def desde_diccionario(cls, data):
        # Crea un objeto Producto desde un diccionario
        # Creates a Producto object from a dictionary
        return cls(
            data["nombre"],
            data["categoria"],
            data["precio"],
            data["stock"]
        )