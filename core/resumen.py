import requests
import json

API_KEY = "AIzaSyB8Dp1tP5jScVPGBxR4kfzt80814rRb1kM"
MODEL = "gemini-2.0-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

def resumir_noticias(noticias_api):
    """
    Resume las noticias obtenidas de la API (lista de diccionarios con 'url' y 'entries').
    """
    textos_noticias = []
    for fuente in noticias_api:
        if 'entries' in fuente:
            for entrada in fuente['entries']:
                titulo = entrada.get('title', 'Sin título')
                descripcion = entrada.get('description', 'Sin descripción')
                textos_noticias.append(f"Título: {titulo}\nResumen: {descripcion}")

    texto_completo = "\n\n".join(textos_noticias)
    if not texto_completo:
        return "No se encontraron noticias para resumir."

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Resumí claramente estas noticias:\n\n{texto_completo}"
                    }
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Error al generar resumen: {response.status_code} - {response.text}"
