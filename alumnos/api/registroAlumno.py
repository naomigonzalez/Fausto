import os
import json

class RegistroAlumno: 

  def __init__(self, data) -> None:
    self._nombre = data.get("nombre")
    self._apellidos = data.get("apellidos")
    self._semestre = data.get("semestre")
    self._grupo = data.get("grupo")
    self._telefono = data.get("telefono")
    self._correo = data.get("correo")
    self._nacimiento = data.get("nacimiento")
    self._direccion = data.get("direccion")
  
  @property
  def nombre(self):
    return self._nombre
  
  @property
  def apellidos(self):
    return self._apellidos
  
  @property
  def semestre(self):
    return self._semestre
  
  @property
  def grupo(self):
    return self._grupo
  
  @property
  def telefono(self):
    return self._telefono
  
  @property
  def correo(self):
    return self._correo
  
  @property
  def nacimiento(self):
    return self._nacimiento

  @property
  def direccion(self):
    return self._direccion

  @direccion.setter
  def direccion(self, direccion):
    self._direccion = direccion
  
  def infoAlumno(self):
    return { 
      "nombre":self._nombre,
      "apellidos":self._apellidos,
      "semestre":self._semestre,
      "grupo":self._grupo,
      "telefono":self._telefono,
      "correo":self._correo,
      "nacimiento":self._nacimiento,
      "direccion":self._direccion
    }


  def guardar(self):
    with open(f"{os.getcwd()}//Fausto//alumnos//api//DB/alumnos.txt") as archivo:
      db = json.loads(archivo.readlines(1)[0]) # covertir un string en json "{'hola': 'k aze?'}" => {'hola': 'k aze?'}
      print(db)
      db.get(f'grupo_{self._grupo}').append(
        self.infoAlumno()
      )
    with open(f"{os.getcwd()}//Fausto//alumnos//api//DB/alumnos.txt", "w") as archivo:
      archivo.write(json.dumps(db)) # covertir un json en string {'hola': 'k aze?'} => "{'hola': 'k aze?'}"
      
      print(db)
