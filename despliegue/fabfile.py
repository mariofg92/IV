# coding: utf-8

from fabric.api import *

def InstallRepo():
    """ Función para descargar el repositorio e instalar requirements. """
    run('git clone https://github.com/mariofg92/ivmario.git')
    run('cd ivmario/ && sudo pip3 install -r requirements.txt')

def RemoveRepo():
    """ Función para borrar el repositorio. """
    run('sudo rm -rf ./ivmario')

def Run():
    """ Función para iniciar el servicio web. """
    run('cd ~/ivmario/ && sudo gunicorn web2:app -b 0.0.0.0:80 --log-file=-',pty=False)
