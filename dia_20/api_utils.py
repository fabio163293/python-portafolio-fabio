import requests
from datetime import datetime

# Obtiene el clima de una ciudad usando la API de OpenWeatherMap
# Gets the weather of a city using the OpenWeatherMap API
def obtener_clima(ciudad, api_key):
    if not ciudad.strip():
        return "Error: la ciudad no puede estar vacía."
    try:
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": ciudad,
            "appid": api_key,
            "units": "metric",
            "lang": "es"
        }
        respuesta = requests.get(url, params=params, timeout=5)
        respuesta.raise_for_status()  # Lanza excepción si la solicitud falla
        datos = respuesta.json()
        temp = datos['main']['temp']
        desc = datos['weather'][0]['description']
        return f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Clima en {ciudad}: {temp}°C, {desc}"
    except requests.exceptions.RequestException as e:
        return f"Error de conexión al consultar el clima: {e}"
    except KeyError:
        return "Error: datos incompletos recibidos del clima. Verifique el nombre de la ciudad."

# Obtiene la tasa de cambio entre dos monedas usando ExchangeRate-API
# Gets the exchange rate between two currencies using ExchangeRate-API
def obtener_tasa_cambio(moneda_base, moneda_destino, api_key):
    if not moneda_base.strip() or not moneda_destino.strip():
        return "Error: las monedas no pueden estar vacías."
    # Lista de monedas válidas (puedes expandirla según la API)
    monedas_validas = ["USD", "EUR", "GBP", "JPY", "ARS"]
    if moneda_base not in monedas_validas or moneda_destino not in monedas_validas:
        return f"Error: moneda no soportada. Monedas válidas: {', '.join(monedas_validas)}"
    try:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{moneda_base}"
        respuesta = requests.get(url, timeout=5)
        respuesta.raise_for_status()
        datos = respuesta.json()
        tasa = datos["conversion_rates"][moneda_destino]
        return f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] 1 {moneda_base} = {tasa} {moneda_destino}"
    except requests.exceptions.RequestException as e:
        return f"Error de conexión al consultar tasa de cambio: {e}"
    except KeyError:
        return f"Error: tasa de cambio no disponible para {moneda_base} a {moneda_destino}."