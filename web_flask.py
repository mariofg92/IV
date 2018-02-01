from flask import Flask, request, jsonify, render_template
import os
import json
from bot.funcionalidades import FuncionalidadDatos

app = Flask(__name__)


{
   "status": "OK"
}

db = os.environ['NAME_BD']
host_db = os.environ['HOST_BD']
usuario = os.environ['USER_BD']
pw = os.environ['PW_BD']


datos = FuncionalidadDatos()

@hug.get('/')
def main():
    return { "status": "OK" }

@hug.get('/status')
def status():
    return jsonify(status='OK')

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


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
