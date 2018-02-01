import hug
import json
from bot.funcionalidades import FuncionalidadDatos


datos = FuncionalidadDatos()

@hug.get('/')
def main():
    return { "status": "OK" }

@hug.get('/status')
def status():
    return { "status": "OK" }

@hug.get('/actividad')
def all():
    actividad = datos.ConsultarActividad()
    """Devuelve toda la actividad"""
    return { "actividad": actividad }

@hug.get('/hora')
def hora():
    hora = datos.GetHoraI()
    """Devuelve la hora de inicio"""
    return { "hora_inicio": hora }

@hug.get('/lugar')
def lugar():
    lugar = datos.GetLugar()
    """Devuelve el lugar de la actividad"""
    return { "lugar": lugar }
