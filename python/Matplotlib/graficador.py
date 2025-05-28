import matplotlib.pyplot as plt

# Genera gráficos de ingresos por categoría y cantidad por producto
# Generates charts for income by category and quantity by product
def generar_graficos(df, mostrar=False):
    # Verifica si el DataFrame es None o está vacío
    # Checks if the DataFrame is None or empty
    if df is None or df.empty:
        print("Error: No hay datos válidos para generar gráficos.")
        print("Error: No valid data to generate charts.")
        return

    try:
        # Gráfico de ingresos por categoría
        # Chart for income by category
        ingresos_por_categoria = df.groupby('categoria')['total'].sum()
        plt.figure(figsize=(8, 6))
        ingresos_por_categoria.plot(kind='bar', color='skyblue')
        plt.title('Ingresos por Categoría')
        plt.title('Income by Category')
        plt.xlabel('Categoría')
        plt.xlabel('Category')
        plt.ylabel('Ingresos ($)')
        plt.ylabel('Income ($)')
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('ingresos_categoria.png')
        # Muestra el gráfico si mostrar=True
        # Displays the chart if mostrar=True
        if mostrar:
            plt.show()
        plt.close()
    except KeyError as e:
        print(f"Error: Columna no encontrada en el DataFrame para el gráfico de ingresos: {e}")
        print(f"Error: Column not found in DataFrame for income chart: {e}")
    except (TypeError, ValueError) as e:
        print(f"Error: Problema con los datos para el gráfico de ingresos: {e}")
        print(f"Error: Issue with data for income chart: {e}")
    except IOError as e:
        print(f"Error: No se pudo guardar 'ingresos_categoria.png': {e}")
        print(f"Error: Could not save 'ingresos_categoria.png': {e}")
    except Exception as e:
        print(f"Error inesperado al generar el gráfico de ingresos: {e}")
        print(f"Unexpected error while generating income chart: {e}")

    try:
        # Gráfico de cantidad por producto
        # Chart for quantity by product
        cantidad_por_producto = df.set_index('producto')['cantidad']
        plt.figure(figsize=(10, 6))
        cantidad_por_producto.plot(kind='bar', color='lightgreen')
        plt.title('Cantidad Vendida por Producto')
        plt.title('Quantity Sold by Product')
        plt.xlabel('Producto')
        plt.xlabel('Product')
        plt.ylabel('Cantidad Vendida')
        plt.ylabel('Quantity Sold')
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('ventas_producto.png')
        # Muestra el gráfico si mostrar=True
        # Displays the chart if mostrar=True
        if mostrar:
            plt.show()
        plt.close()
    except KeyError as e:
        print(f"Error: Columna no encontrada en el DataFrame para el gráfico de ventas: {e}")
        print(f"Error: Column not found in DataFrame for sales chart: {e}")
    except (TypeError, ValueError) as e:
        print(f"Error: Problema con los datos para el gráfico de ventas: {e}")
        print(f"Error: Issue with data for sales chart: {e}")
    except IOError as e:
        print(f"Error: No se pudo guardar 'ventas_producto.png': {e}")
        print(f"Error: Could not save 'ventas_producto.png': {e}")
    except Exception as e:
        print(f"Error inesperado al generar el gráfico de ventas: {e}")
        print(f"Unexpected error while generating sales chart: {e}")