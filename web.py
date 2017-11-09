import hug
import json
from funcionalidades import FuncionalidadDatos

@hug.get('/')
def status():
    return { "status": "OK" }

@hug.get('/actividad')
def all():
    """Devuelve toda la actividad"""
    return { "actividad": ConsultarActividad() }
