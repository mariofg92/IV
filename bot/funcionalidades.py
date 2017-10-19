import json

class FuncionalidadDatos:

    def __init__(self):
      try: # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
        with open('prueba_actividad.json') as data_file:
            self.actividad = json.load(data_file)
      except IOError as fallo:
        print("Error %d leyendo prueba_actividad.json: %s", fallo.errno,fallo.strerror)

    def ConsultarActividad:
      return self.actividad

    def 
