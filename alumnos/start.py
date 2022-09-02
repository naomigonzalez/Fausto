import json
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS, cross_origin
from api.registroAlumno import RegistroAlumno

def create_app():
    
    """Función que inicializa la app y crea el servidor de Flask"""
    
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    return app


app = create_app()

# @app.route('/', methods=['GET']) # get obtener la información de un end point 
# def get_inmuebles():

@app.route('/alumnos', methods=['POST']) # crear nuevos atributos en una base de datos 
def formulario_alumnos():
    json:dict = request.get_json()
    alumno = RegistroAlumno(json)
    alumno.guardar() 
    return {
        "respuesta": "ok" 
    }

if __name__ == '__main__':
    app.run(debug=True)
