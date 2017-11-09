#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os

class FuncionalidadDatos:
    actividad = {ninguna}

    def __init__(self):
      #self.pw = os.environ["PW_BD"]
      try: # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
        with open('prueba_actividad.json') as data_file:
            self.actividad = json.load(data_file)
      except IOError as fallo:
        print("Error %d leyendo prueba_actividad.json: %s", fallo.errno,fallo.strerror)

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
