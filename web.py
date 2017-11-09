import hug
import json
from bot.funcionalidades import FuncionalidadDatos
import os

datos = FuncionalidadDatos()

print os.name
@hug.get('/')
def status():
    return { "status": "OK" }

@hug.get('/actividad')
def all():
    actividad = datos.ConsultarActividad()
    """Devuelve toda la actividad"""
    return { "actividad": actividad }
