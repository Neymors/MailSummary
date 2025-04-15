from cliente import obtener_noticias
from resumen import resumir_noticias
from pdf_generator import generar_pdf
from mail_sender import enviar_email
from dotenv import load_dotenv
import os
import sys

# Cargar variables desde .env solo en entornos locales
if os.getenv("GITHUB_ACTIONS") is None:  # Detectar si no estamos en GitHub Actions
    dotenv_path = os.path.join(os.path.dirname(__file__), 'mail.env')
    load_dotenv(dotenv_path=dotenv_path)

# **REEMPLAZA ESTAS URLs CON LAS URLs *REALES* DE LOS FEEDS RSS**
LISTA_URLS_FEEDS_REALES = [
    "https://www.cronista.com/rss/novedades.xml",
    "https://www.msn.com/es-us/money/rss",
    "https://www.msn.com/es-ar/feed",
    "https://news.google.com/rss/publications/CAAqIggKIhxDQklTRHdnTWFnc0tDWFJ1TG1OdmJTNWhjaWdBUAE",
    "https://news.google.com/rss/topics/CAAqLAgKIiZDQkFTRmdvSUwyMHZNRGx1YlY4U0JtVnpMVFF4T1JvQ1FWSW9BQVAB",
    "https://news.google.com/rss/topics/CAAqLQgKIidDQkFTRndnTWFoTUtFWEYxWldScFoybDBZV3d1WTI5dExtRnlLQUFQAQ",
    "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZ4ZERBU0JtVnpMVFF4T1NnQVAB",
    "https://news.google.com/rss/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNREUxY0dwa0VnWmxjeTAwTVRrb0FBUAE",
    "https://news.google.com/rss/topics/CAAqLQgKIidDQkFTRndvTkwyY3ZNVEZ5Y0dSaWNXcDZjeElHWlhNdE5ERTVLQUFQAQ",
    "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSEwyMHZNRzFyZWhJR1pYTXROREU1S0FBUAE",
    "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSEwyMHZNRzFyZWhJR1pYTXROREU1S0FBUAE/sections/CAQqEAgAKgcICjCij_kKMMbe4AIw8_eeBg",
    "https://news.google.com/rss/topics/CAAqBwgKMKeAiQswpI2IAw",
    "https://news.google.com/rss/topics/CAAqBwgKMLn_iAswk5CIAw",
    "https://news.google.com/rss/topics/CAAqBwgKMPr9iAsw9Y-IAw",
    "https://news.google.com/rss/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrRlNLQUFQAQ",
]

def main():
    # Leer variables de entorno
    email_remitente = os.getenv("EMAIL_REMITENTE")
    email_password = os.getenv("EMAIL_PASSWORD")
    api_key = os.getenv("GEMINI_API_KEY")
    destinatario_email = os.getenv("RECIPIENT")

    if not all([email_remitente, email_password, api_key, destinatario_email]):
        print("Error: Faltan variables de entorno necesarias.")
        sys.exit(1)

    print("Obteniendo noticias...")
    noticias_api = obtener_noticias(LISTA_URLS_FEEDS_REALES)

    if noticias_api:
        print("Resumiendo noticias...")
        resumen_texto = resumir_noticias(noticias_api)

        if resumen_texto:
            print("Generando PDF...")
            try:
                archivo_pdf = generar_pdf(resumen_texto)  # <- ahora devuelve el nombre
            except Exception as e:
                print(f"Error al generar el PDF: {e}")
                return

            if archivo_pdf:
                print(f"Enviando email a {destinatario_email}...")
                enviar_email(destinatario_email, archivo_pdf)
                print("Proceso finalizado ✅")
            else:
                print("Error al generar el PDF.")
        else:
            print("No se pudo generar el resumen.")
    else:
        print("No se pudieron obtener las noticias de la API.")

if __name__ == "__main__":
    main()