#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os

class FuncionalidadDatos:

    def __init__(self):
      path = os.path.dirname(os.path.abspath(__file__)) + '/prueba_actividad.json' #because this file is at the same level that the json file

      try: # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
        with open(path) as data_file:
            self.actividad = json.load(data_file)
      except IOError as fallo:
        print(path)
        print("Error %d leyendo prueba_actividad.json: %s , cdwdir: %s, actudir %s", fallo.errno,fallo.strerror, os.getcwd(), os.path.dirname(os.path.abspath(__file__)))

    def ConsultarActividad(self):
      return self.actividad

    def GetHoraI(self):
      return str(self.actividad['horai'])

    def GetHoraF(self):
      return str(self.actividad['horaf'])

    def GetFechaI(self):
      return str(self.actividad['fechai'])

    def GetFechaF(self):
      return str(self.actividad['fechaf'])

    def GetTitulo(self):
      return str(self.actividad['titulo'])

    def GetDescripcion(self):
      return str(self.actividad['descripcion'])

    def GetLugar(self):
      return str(self.actividad['lugar'])

    def GetTipo(self):
      return str(self.actividad['tipo'])

    def GetFacultad(self):
      return str(self.actividad['facultad'])
