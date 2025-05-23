from flask import Flask, jsonify, request
from producto import Producto
from db_utils import (
    crear_bd,
    obtener_productos,
    obtener_producto_por_id,  # Nueva función añadida
    agregar_producto_desde_objeto,
    eliminar_producto_por_id,
    actualizar_stock_por_id
)

app = Flask(__name__)

# Inicializa la base de datos al arrancar la aplicación
# Initializes the database when the application starts
try:
    crear_bd()
except Exception as e:
    print(f"Error al inicializar la base de datos: {e}")
    print(f"Error initializing the database: {e}")

@app.route('/productos', methods=['GET'])
def listar_productos():
    # Lista todos los productos en la base de datos
    # Lists all products in the database
    productos = obtener_productos()
    productos_dict = [
        {
            "id": p.id,
            "nombre": p.nombre,
            "categoria": p.categoria,
            "precio": p.precio,
            "stock": p.stock
        }
        for p in productos
    ]
    return jsonify(productos_dict), 200

@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    # Obtiene un producto por su ID
    # Retrieves a product by its ID
    producto = obtener_producto_por_id(id)
    if producto:
        return jsonify({
            "id": producto.id,
            "nombre": producto.nombre,
            "categoria": producto.categoria,
            "precio": producto.precio,
            "stock": producto.stock
        }), 200
    return jsonify({"error": "Producto no encontrado / Product not found"}), 404

@app.route('/productos', methods=['POST'])
def agregar_producto():
    # Agrega un nuevo producto a la base de datos
    # Adds a new product to the database
    if not request.json:
        return jsonify({"error": "Se requiere un cuerpo JSON / JSON body required"}), 400

    required_fields = ["nombre", "categoria", "precio", "stock"]
    for field in required_fields:
        if field not in request.json:
            return jsonify({"error": f"El campo '{field}' es requerido / Field '{field}' is required"}), 400

    data = request.json
    try:
        producto = Producto(
            data["nombre"],
            data["categoria"],
            data["precio"],
            data["stock"]
        )
        agregar_producto_desde_objeto(producto)
        return jsonify({"mensaje": "Producto agregado correctamente / Product added successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error interno al agregar producto / Internal error adding product"}), 500

@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    # Actualiza el stock de un producto por su ID
    # Updates the stock of a product by its ID
    if not request.json:
        return jsonify({"error": "Se requiere un cuerpo JSON / JSON body required"}), 400

    if "stock" not in request.json:
        return jsonify({"error": "Se requiere el campo 'stock' / Field 'stock' is required"}), 400

    try:
        nuevo_stock = int(request.json["stock"])
        if nuevo_stock < 0:
            return jsonify({"error": "El stock no puede ser negativo / Stock cannot be negative"}), 400

        producto = obtener_producto_por_id(id)
        if not producto:
            return jsonify({"error": "Producto no encontrado / Product not found"}), 404

        actualizar_stock_por_id(id, nuevo_stock)
        return jsonify({"mensaje": "Producto actualizado correctamente / Product updated successfully"}), 200
    except ValueError:
        return jsonify({"error": "El stock debe ser un número entero / Stock must be an integer"}), 400
    except Exception as e:
        return jsonify({"error": "Error interno al actualizar producto / Internal error updating product"}), 500

@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    # Elimina un producto por su ID
    # Deletes a product by its ID
    producto = obtener_producto_por_id(id)
    if not producto:
        return jsonify({"error": "Producto no encontrado / Product not found"}), 404

    try:
        eliminar_producto_por_id(id)
        return jsonify({"mensaje": "Producto eliminado correctamente / Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Error interno al eliminar producto / Internal error deleting product"}), 500

if __name__ == '__main__':
    # Ejecuta la aplicación en modo debug (solo para desarrollo)
    # Runs the application in debug mode (development only)
    app.run(debug=True)