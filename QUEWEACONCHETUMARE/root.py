from flask import render_template, request
from ia_servicio import procesar_pregunta_ia
from api_servicio import obtener_titulares_resumidos, obtener_todas_las_noticias

def setup_routes(app):
    @app.route('/')
    def index():
        """
        Ruta para la página principal que muestra las noticias.
        """
        categoria = request.args.get('categoria', 'general')
        pais = request.args.get('pais', 'us')
        noticias = obtener_todas_las_noticias(categoria=categoria, pais=pais)
        return render_template('index.html', noticias=noticias)


    # @app.route('/chat', methods=['GET', 'POST'])
    # def chat():
    #     """
    #     Ruta para el chat con IA que procesa y resume noticias.
    #     """
    #     if request.method == 'POST':
    #         categoria = request.form.get('categoria', 'general')
    #         pais = request.form.get('pais', 'us')
    #         respuesta = procesar_pregunta_ia(categoria=categoria, pais=pais)
    #         return render_template('chat.html', respuesta=respuesta)
    #     return render_template('chat.html')

#ruta anterio de chat

    @app.route('/chat', methods=['GET', 'POST'])
    def chat():
        """
        Ruta para el chat con IA que procesa y resume noticias.
        """
        if request.method == 'POST':
            categoria = request.form.get('categoria', 'general')
            pais = request.form.get('pais', 'us')
            respuesta = procesar_pregunta_ia(categoria=categoria, pais=pais)
            return render_template('chat.html', respuesta=respuesta)
        return render_template('chat.html')
#ruta opcional

    # @app.route('/noticias_resumidas')
    # def noticias_resumidas():
    #     """
    #     Ruta que muestra noticias resumidas.
    #     """
    #     categoria = request.args.get('categoria', 'general')
    #     pais = request.args.get('pais', 'us')
    #     titulares_resumidos = obtener_titulares_resumidos(categoria, pais)
    #     return render_template('noticias_resumidas.html', titulares=titulares_resumidos)
