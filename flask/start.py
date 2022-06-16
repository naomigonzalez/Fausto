from flask import Flask, request
from flask import jsonify

def create_app():
    
    """Función que inicializa la app y crea el servidor de Flask"""
    
    app = Flask(__name__)
    return app


app = create_app()

@app.route('/', methods=['GET'])
def get_inmuebles():

    """End-point para realizar la búsqueda de inmuebles"""

    response = {}
    print("ENTROOOOOOOOOOOOOOOOOOO")
    return "<h1><b>Hola k aze?</b></h1>"

@app.route('/crea_usuario', methods=['POST'])
def crea_usuario():

    json = request.get_json()
    print(f"crea_usuario ==============> {json}")
    return {
      "codigo": 200,
      "respuesta": f"usuario creado :: {json.get('mensaje')}"
    }



if __name__ == '__main__':
    app.run(debug=True)
