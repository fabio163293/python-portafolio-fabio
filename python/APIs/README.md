# Día 20 - Consultor de Datos con APIs

**Fecha:** 14 de mayo de 2025

## Descripción (ES/EN)

**Español:**  
Este día se centra en aprender a consumir APIs públicas en Python para obtener datos en tiempo real. Se desarrolla un consultor que permite consultar el clima de una ciudad (usando OpenWeatherMap) y la tasa de cambio entre monedas (usando ExchangeRate-API), guardando un historial de consultas en un archivo JSON. Se aplica modularidad y manejo de errores para robustez.  

**English:**  
This day focuses on learning to consume public APIs in Python to retrieve real-time data. A data consultant is developed that allows querying the weather of a city (using OpenWeatherMap) and the exchange rate between currencies (using ExchangeRate-API), saving a history of queries in a JSON file. Modularity and error handling are applied for robustness.

## Estructura

- `api_utils.py`: Funciones para interactuar con las APIs de clima y tasas de cambio.
- `consultor_datos.py`: Programa principal con un menú para consultar datos y mostrar historial.
- `consultas.json`: Archivo donde se guardan las consultas realizadas.

## Instrucciones de Uso (ES/EN)

**Español:**  
1. Instala las dependencias: `pip install requests`.  
2. Reemplaza las API keys en `consultor_datos.py` con claves válidas:  
   - `API_WEATHER`: Obtén tu clave en https://openweathermap.org/api.  
   - `API_EXCHANGE`: Obtén tu clave en https://www.exchangerate-api.com/.  
   Las claves actuales son placeholders y no funcionan.  
3. Ejecuta `consultor_datos.py` para usar el programa.

**English:**  
1. Install dependencies: `pip install requests`.  
2. Replace the API keys in `consultor_datos.py` with valid keys:  
   - `API_WEATHER`: Get your key at https://openweathermap.org/api.  
   - `API_EXCHANGE`: Get your key at https://www.exchangerate-api.com/.  
   The current keys are placeholders and do not work.  
3. Run `consultor_datos.py` to use the program.