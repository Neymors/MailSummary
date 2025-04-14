from app import procesar_noticias  # o donde definas la función

urls_feeds = [
        "https://www.cronista.com/",
        "https://news.google.com/home?hl=es-419&gl=AR&ceid=AR%3Aes-419",
        "https://news.google.com/foryou?hl=es-419&gl=AR&ceid=AR%3Aes-419",
        "https://tn.com.ar/politica/",
        "https://tn.com.ar/economia/",
        "https://tn.com.ar/internacional/",
        "https://tn.com.ar/policiales/",
        "https://www.ambito.com/",
        "https://www.lacapital.com.ar/",
        "https://www.infobae.com/tag/javier-milei/",
        "https://www.infobae.com/tag/trump/",
        "https://www.infobae.com/tag/giorgia-meloni/",
        "https://www.infobae.com/politica/",
        "https://www.infobae.com/economia/",
        "https://www.infobae.com/sociedad/policiales/",
        "https://www.infobae.com/judiciales/",
        "https://eleconomista.com.ar/",
        "https://eleconomista.com.ar/especial/dolar",
        "https://eleconomista.com.ar/criptomonedas/",
        "https://eleconomista.com.ar/especial/inversiones",
        "https://eleconomista.com.ar/politica/",
        "https://eleconomista.com.ar/internacional/",
        "https://eleconomista.com.ar/negocios/",
        "https://mi8.com.ar/category/locales/",
        "https://www.bbc.com/news",
        "https://www.bbc.com/news/topics/c2vdnvdg6xxt",
        "https://www.bbc.com/news/war-in-ukraine",
        "https://www.bbc.com/business",
        "https://www.bbc.com/business/technology-of-business",
        "https://www.bbc.com/business/future-of-business",
        "https://www.lanacion.com.ar/economia/",
        "https://www.lanacion.com.ar/politica/",
        "https://www.economist.com/",
        "https://www.nytimes.com/international/",
        "https://www.nytimes.com/international/section/us",
        "https://www.nytimes.com/international/section/business",
        "https://www.nytimes.com/international/section/world",
        "https://www.economist.com/topics/economy",
        "https://www.ft.com/",
        "https://www.ft.com/world",
        "https://www.ft.com/middle-east-war",
        "https://www.ft.com/us",
        "https://www.ft.com/technology",
        "https://www.wsj.com/",
        "https://www.wsj.com/world?mod=nav_top_section",
        "https://www.wsj.com/business?mod=nav_top_section",
        "https://www.wsj.com/personal-finance?mod=nav_top_section",
        "https://www.kp.ru/",
        "https://www.kp.ru/money/",
        "https://www.radaraustral.com/",
        "https://www.radaraustral.com/articulos/categoria/indopacifico/",
        "https://www.radaraustral.com/articulos/categoria/argentina/",
        "https://www.radaraustral.com/articulos/categoria/global/",
        "https://www.radaraustral.com/articulos/categoria/conflictos/",
        "https://www.radaraustral.com/articulos/categoria/ecom/",
        "https://www.radaraustral.com/articulos/categoria/moafrica/",
        "https://elpais.com/noticias/geopolitica/",
        "https://www.infobae.com/tag/geopolitica/",
        "https://elpais.com/us/?ed=us",
        "https://foreignpolicy.com/2024/03/27/europe-eu-nato-european-army-russia-ukraine-defense-military-strategy/"
]

resultados = procesar_noticias(urls_feeds)
from feed import obtener_info_feed  # type: ignore # si esta función está ahí
# Mostrar resultados
for fuente in resultados:
    print(f"\n📰 Fuente: {fuente['fuente']}")
    for noticia in fuente['noticias']:
        print(f" - {noticia['titulo']}")
        print(f"   {noticia['link']}")
        print(f"   📅 {noticia['fecha']}\n")