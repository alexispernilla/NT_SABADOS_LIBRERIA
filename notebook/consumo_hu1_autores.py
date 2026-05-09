import requests

def consumir_api_autores(cantidad_registros=None):
    # 1. Escribir la url del servicio que quiero consumir
    url = "http://localhost:8080/autors"
    
    # 2. Utilizar el request de python para ir al api
    respuesta = requests.get(url)
    
    # 3. Verificamos la respuesta
    respuesta.raise_for_status()
    
    # 4. Verifico el formato de los datos recibidos
    datos = respuesta.json()
    
    return datos
