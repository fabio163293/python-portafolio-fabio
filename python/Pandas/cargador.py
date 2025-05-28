import pandas as pd

# Carga los datos desde un archivo CSV usando pandas
# Loads data from a CSV file using pandas
def cargar_datos(ruta_archivo):
    try:
        # Lee el archivo CSV y convierte las columnas a tipos adecuados
        df = pd.read_csv(ruta_archivo, encoding='utf-8', dtype={
            'producto': str,
            'categoria': str,
            'precio': float,
            'cantidad': int
        })
        # Calcula el total por fila (precio * cantidad)
        df['total'] = df['precio'] * df['cantidad']
        return df
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {ruta_archivo} está vacío.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None