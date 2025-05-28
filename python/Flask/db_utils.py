import sqlite3
from dia_24.producto import Producto

def crear_bd():
    # Crea la base de datos y la tabla productos
    # Creates the database and the productos table
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS productos 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         nombre TEXT NOT NULL,
                         categoria TEXT NOT NULL,
                         precio REAL NOT NULL,
                         stock INTEGER NOT NULL)''')

        conn.commit()
        print("Base de datos y tabla 'productos' creadas correctamente.")
        print("Database and 'productos' table created successfully.")

    except sqlite3.Error as e:
        print(f"Error al crear la base de datos: {e}")
        print(f"Error creating the database: {e}")
    finally:
        if conn:
            conn.close()

def agregar_producto_desde_objeto(producto):
    # Agrega un producto a la base de datos desde un objeto Producto
    # Adds a product to the database from a Producto object
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO productos (nombre, categoria, precio, stock)
            VALUES (?, ?, ?, ?)''',
            (producto.nombre, producto.categoria, producto.precio, producto.stock))

        conn.commit()
        print("Producto agregado desde objeto correctamente.")
        print("Product added from object successfully.")

    except sqlite3.Error as e:
        print(f"Error al agregar producto: {e}")
        print(f"Error adding product: {e}")
    finally:
        if conn:
            conn.close()

def obtener_productos(categoria=None):
    # Obtiene todos los productos o los de una categoría específica
    # Retrieves all products or those from a specific category
    productos = []
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()

        if categoria:
            cursor.execute("SELECT id, nombre, categoria, precio, stock FROM productos WHERE categoria = ?", (categoria,))
        else:
            cursor.execute("SELECT id, nombre, categoria, precio, stock FROM productos")
        
        filas = cursor.fetchall()

        for fila in filas:
            id_, nombre, categoria, precio, stock = fila
            producto = Producto(nombre, categoria, precio, stock)
            producto.id = id_  # Añade el ID real de la base de datos
            productos.append(producto)

    except sqlite3.Error as e:
        print(f"Error al obtener productos: {e}")
        print(f"Error retrieving products: {e}")
    finally:
        if conn:
            conn.close()
    
    return productos

def eliminar_producto_por_id(producto_id):
    # Elimina un producto por su ID
    # Deletes a product by its ID
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Producto con ID {producto_id} eliminado correctamente.")
            print(f"Product with ID {producto_id} deleted successfully.")
        else:
            print(f"No se encontró un producto con ID {producto_id}.")
            print(f"No product found with ID {producto_id}.")

    except sqlite3.Error as e:
        print(f"Error al eliminar producto: {e}")
        print(f"Error deleting product: {e}")
    finally:
        if conn:
            conn.close()
    
def actualizar_stock_por_id(producto_id, nuevo_stock):
    # Actualiza el stock de un producto por su ID
    # Updates the stock of a product by its ID
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (nuevo_stock, producto_id))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Stock del producto con ID {producto_id} actualizado a {nuevo_stock}.")
            print(f"Stock of product with ID {producto_id} updated to {nuevo_stock}.")
        else:
            print(f"No se encontró un producto con ID {producto_id}.")
            print(f"No product found with ID {producto_id}.")

    except sqlite3.Error as e:
        print(f"Error al actualizar el stock: {e}")
        print(f"Error updating stock: {e}")
    finally:
        if conn:
            conn.close()
def obtener_producto_por_id(producto_id):
    # Obtiene un producto por su ID directamente desde la base de datos
    # Retrieves a product by its ID directly from the database
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, nombre, categoria, precio, stock FROM productos WHERE id = ?", (producto_id,))
        fila = cursor.fetchone()

        if fila:
            id_, nombre, categoria, precio, stock = fila
            producto = Producto(nombre, categoria, precio, stock)
            producto.id = id_
            return producto
        return None

    except sqlite3.Error as e:
        print(f"Error al obtener producto por ID: {e}")
        print(f"Error retrieving product by ID: {e}")
        return None
    finally:
        if conn:
            conn.close()            