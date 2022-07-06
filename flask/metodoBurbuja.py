import json
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

@app.route('/ordenamiento', methods=['POST']) # crear nuevos atributos en una base de datos 
def metodo_burbuja():
    json:dict = request.get_json()
    print(json)
    unaLista = json.get('edades')
    print("json.get('colores_favoritos')",json.get('colores_favoritos'))
    print(json.get('colores_favoritos').get('rojo'))
    print("--------------------")
    colores = json.get('colores_favoritos')
    print(colores.get('amarillo'))
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i] > unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

    # unaLista = json.get('edades') 
    return {
        "codigo": 200,
        "respuesta": f"{unaLista}",#[1,2,3,4,5,6,7,8] len() => 7
        "edad mínima ": f"{unaLista[0]}", 
        "edad máxima": f"{unaLista[len(unaLista)-1]}"
    }

if __name__ == '__main__':
    app.run(debug=True)
