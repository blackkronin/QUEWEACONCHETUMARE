from flask import Flask
from root import setup_routes

app = Flask(__name__)

# Configuración de rutas desde root.py
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
