from flask import Flask, request
from flask import jsonify

def create_app():
    
    """Función que inicializa la app y crea el servidor de Flask"""
    
    app = Flask(__name__)
    return app


app = create_app()

@app.route('/', methods=['GET']) # get obtener la información de un end point 
def get_inmuebles():

    """End-point para realizar la búsqueda de inmuebles"""

    response = {}
    print("ENTROOOOOOOOOOOOOOOOOOO")
    return "<h1><b>Hola k aze?</b></h1>"

@app.route('/crea_usuario', methods=['POST']) # crear nuevos atributos en una base de datos 
def crea_usuario_metodo():

    json:dict = request.get_json()
    # print(f"crea_usuario ==============> {json}")

    # print(json.get('nombre')) # si esta variable no existiera saldría none. 
    # # print(json['nombre2']) la forma NO recomendada porque sino existe marca un error 
    # print(json.get('edad'))
    # # print(json.get('edad1'))
    # print(json.get('archivo'))

    f = open(f"{json.get('archivo')}.txt", "x")
    f.write(f"{json.get('nombre')}")
    f.write(f"{json.get('edad')}")

    f.close


    return {
      "codigo": 200,
      "respuesta": f"usuario {json.get('nombre')} ha sido creado en el archivo {json.get('archivo')}"
    }






if __name__ == '__main__':
    app.run(debug=True)
