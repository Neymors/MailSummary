from flask import Flask, jsonify, request
import feedparser

app = Flask(__name__)

def obtener_info_feed(feed_url):
    """
    Descarga y analiza un feed RSS, extrayendo la información relevante de cada entrada.
    """
    try:
        feed = feedparser.parse(feed_url)
        entradas = []
        for entry in feed.entries:
            info = {
                'title': entry.get('title'),
                'link': entry.get('link'),
                'description': entry.get('summary') if 'summary' in entry else entry.get('content', [{}])[0].get('value'),
                'pubDate': entry.get('published') or entry.get('updated'),
                'guid': entry.get('id'),
                'category': [tag.get('term') for tag in entry.get('tags', [])],
                'author': entry.get('author')
            }
            entradas.append(info)
        return {'url': feed_url, 'entries': entradas}
    except Exception as e:
        return {'url': feed_url, 'error': str(e)}

@app.route('/obtener_noticias', methods=['GET', 'POST'])
def obtener_noticias():
    if request.method == 'GET':
        return jsonify({'error': 'Método POST no permitido. Use POST con una lista de URLs.'})

    data = request.get_json()
    if not data or 'urls' not in data or not isinstance(data['urls'], list):
        return jsonify({'error': 'Se debe proporcionar una lista de URLs en el cuerpo de la petición (clave: "urls").'}), 400

    resultados = []
    for url in data['urls']:
        resultados.append(obtener_info_feed(url))

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)