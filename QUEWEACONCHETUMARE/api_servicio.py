import requests

NEWS_API_KEY = 'hola'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

# Función para obtener todas las noticias
def obtener_todas_las_noticias(categoria="general", pais="us"):
    """
    Función para obtener todas las noticias de la API.
    """
    params = {
        'apiKey': NEWS_API_KEY,
        'category': categoria,
        'country': pais
    }
    
    response = requests.get(NEWS_API_URL, params=params)
    
    if response.status_code == 200:
        return response.json()  # Devolver todas las noticias
    else:
        return {'error': 'No se pudieron obtener las noticias'}



def obtener_titulares_resumidos(categoria="general", pais="us"):
    """
    Función para obtener un resumen de los 3 primeros titulares principales.
    """
    noticias = obtener_todas_las_noticias(categoria, pais)
    
    if 'error' in noticias:
        return noticias
    
    articulos = noticias.get('articles', [])
    if not isinstance(articulos, list):
        return {'error': 'Formato de datos inesperado en la respuesta de la API'}
    
    # Limitar a los primeros 3 artículos
    titulares_resumidos = []
    for article in articulos[:3]:  # Seleccionamos solo los primeros 3 artículos
        if isinstance(article, dict):
            titulo = article.get('title', 'Sin título')
            descripcion = article.get('description', 'Sin descripción')
            titulares_resumidos.append({'titulo': titulo, 'descripcion': descripcion})
        else:
            print("Artículo en formato inesperado:", article)
            return {'error': 'Formato de artículo inesperado'}
    
    return titulares_resumidos
