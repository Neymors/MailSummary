import requests
import json

def obtener_noticias(urls_feeds):
    """
    Envía una petición POST a la API para obtener las noticias de los feeds RSS.
    """
    url_api = 'http://127.0.0.1:5000/obtener_noticias'  # Asegúrate de que la API esté corriendo en este puerto
    headers = {'Content-Type': 'application/json'}
    data = {'urls': urls_feeds}

    try:
        response = requests.post(url_api, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener noticias de la API: {e}")
        return None

if __name__ == '__main__':
    # **REEMPLAZA ESTAS URLs CON LAS URLs *REALES* DE LOS FEEDS RSS**
    lista_urls_feeds_reales = [
        "https://www.cronista.com/rss/novedades.xml",
        "https://www.infobae.com/rss/politica.xml",
        # Agrega aquí las URLs correctas de los feeds RSS
    ]
    noticias = obtener_noticias(lista_urls_feeds_reales)
    if noticias:
        print("Noticias obtenidas de la API:")
        print(json.dumps(noticias, indent=4, ensure_ascii=False))