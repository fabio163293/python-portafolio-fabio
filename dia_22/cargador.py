import pandas as pd

# Carga los datos desde un archivo CSV usando pandas
# Loads data from a CSV file using pandas
def cargar_datos(ruta_archivo):
    try:
        # Lee el archivo CSV y convierte las columnas a tipos adecuados
        # Reads the CSV file and converts columns to appropriate types
        df = pd.read_csv(ruta_archivo, encoding='utf-8', dtype={
            'producto': str,
            'categoria': str,
            'precio': float,
            'cantidad': int
        })
        # Verifica si el DataFrame está vacío o tiene datos inválidos
        # Checks if the DataFrame is empty or contains invalid data
        if df.empty or df.isnull().all().all():
            print("Error: El archivo no contiene datos válidos.")
            print("Error: The file does not contain valid data.")
            return None
        # Calcula el total por fila (precio * cantidad)
        # Calculates the total per row (price * quantity)
        df['total'] = df['precio'] * df['cantidad']
        return df
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
        print(f"Error: The file {ruta_archivo} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {ruta_archivo} está vacío.")
        print(f"Error: The file {ruta_archivo} is empty.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado al cargar los datos: {e}")
        print(f"An unexpected error occurred while loading the data: {e}")
        return None