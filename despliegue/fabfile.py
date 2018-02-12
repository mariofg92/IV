# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os

def InstallRepo():
    """ Función para descargar el repositorio. """
	# Descargamos el repositorio
    run('git clone https://github.com/mariofg92/ivmario.git')

	# Accedemos al repositorio e instalamos las dependencias
    # run('sudo apt-get install -y supervisor')
    run('cd ivmario/ && sudo pip3 install -r requirements.txt')
    # run('sudo cp IV_Proyecto/apiweb.conf /etc/supervisor/conf.d/')

def RemoveRepo():
    """ Función para borrar el repositorio. """
    # Borramos el repositorio
    run('sudo rm -rf ./ivmario')

def Run():
    """ Función para iniciar la web. """
	# Importamos las variables globales
	# with shell_env(TOKENBOT="454323731:AAHV_dXizf08VAkEzfMUgOKN9VaM5KCFExI"
    #run('cd ~/IV_Proyecto/ && sudo supervisorctl reread && sudo supervisorctl reload && sudo supervisorctl start apiweb',pty=False)
    run('cd ~/ivmario/ && sudo gunicorn web2:app -b 0.0.0.0:80 --log-file=-',pty=False)
