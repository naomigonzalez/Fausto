import json
from flask import Flask, request
from flask import jsonify


def create_app():
    
    """Función que inicializa la app y crea el servidor de Flask"""
    
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    return app


app = create_app()

@app.route('/', methods=['GET']) # get obtener la información de un end point 
def get_inmuebles():

    """End-point para realizar la búsqueda de inmuebles"""

    response = {}
    print("ENTROOOOOOOOOOOOOOOOOOO")
    return "<h1><b>Hola k aze?</b></h1>"

@app.route('/alumnos', methods=['POST']) # crear nuevos atributos en una base de datos 
def alumnos():

