[![Build Status](https://travis-ci.org/mariofg92/ivmario.svg?branch=master)](https://travis-ci.org/mariofg92/ivmario)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

* Despliegue: https://ugrcalendar.herokuapp.com/
* Contenedor: https://ugrcalendar.azurewebsites.net/
* DockerHub: https://hub.docker.com/r/mariofg92/ivmario/
* Despliegue final: ugrcalendar-vm.westeurope.cloudapp.azure.com

# Proyecto IV: UGRCalendar.
Curso: 4º
Asignatura: IV (Infraestructura Virtual).

Este es el repositorio del proyecto final de IV.

Autor: Mario Fernández Gómez

# Descripción.

Este proyecto consiste en un servico de calendario de la UGR, tanto a efectos academicos (Días festivos, lectivos, periodos de exámenes...) como a nivel de eventos (charlas, talleres...). Además deberá soportar la diferencias de calendario de las distintas facultades.

Sobre este servicio se implementará un bot de telegram que ofrezca diferente información y funcionalidad.

# Integración Continua

Para el testeo uso la biblioteca `unittest` de Python. Existe un archivo *test.py* donde se han desarrollado test unitarios del código.

Como todavía no tengo una base de datos diseñada estoy usando datos estáticos en JSON del archivo *prueba_actividad.json*.

Estos tests son lanzados por **TravisCI**. **TravisCI** hace uso de la regla `make test` del Makefile. Esta regla lanza los tests del archivo anteriormente mencionado.

Con estos test, me aseguro de que ante cualquier actualización o modificación en el repositorio, todo sigue funcionando correctamente.

# Despliegue en un PaaS

URL: https://ugrcalendar.herokuapp.com/

## Justificación del PaaS elegido

Yo he elegido **Heroku** por la sencillez, porque está ampliamente documentado y porque la funcionalidad básica es gratuita.

## Despliegue de un Bot

### Despliegue Manual

Tras instalar la interfaz que nos ofrece Heroku para el sistema operativo que estemos usando, vamos a proceder
al despligue.

1. nos logueamos con
```shell
$ heroku login
```
Nos pedirá los credenciales.

2. Tras logearnos lanzamos:

```shell
$ heroku apps:create --region eu ugrcalendar
```
Con esto estamos creando la aplicación en Heroku en la región de europa.

3. Creamos un archivo *Procfile* donde se le indica que actividad debe realizar al desplegarse
```shell
$ web: gunicorn web:__hug_wsgi__ --log-file=-
```

4. Por último levantamos su dyno con:

```shell
$ heroku ps:scale web=1
```
Este *dyno* es el que se va a encargar de lanzar la sentencia `gunicorn web:__hug_wsgi__ --log-file=-` y con esto el servicio web estará activo.

### Despliegue automatico desde github.

![img](https://github.com/mariofg92/ivmario/blob/master/docs/img/heroku_github.png)
Para que se despligue automaticamente con cada push de github entramos en heroku>nuestra_app>deply y le indicamos que queremos usar github. Le indicamos nuestro repositorio y activamos el despligue autómatico. Selecionamos que sólo se permite el despligue automático si se pasan los test CI.

### Comprobando que funciona

Podemos verlo directamente desde el navegador o usar algun comando como `curl`
```shell
$ curl https://ugrcalendar.herokuapp.com/
```
Devuelve:
`{"status": "OK"}`

Si por ejemplo usamos una ruta implementada como /lugar:
```shell
$ curl https://ugrcalendar.herokuapp.com/lugar
```
Obtenemos:
`{"lugar": "ETSIIT"}`

Las diferentes rutas implementadas son:
+ [/](https://ugrcalendar.herokuapp.com)
+ [/actividad](https://ugrcalendar.herokuapp.com/actividad)
+ [/lugar](https://ugrcalendar.herokuapp.com/lugar)
+ [/hora](https://ugrcalendar.herokuapp.com/hora)

# Contenedor con Docker y Docker hub

URL: https://hub.docker.com/r/mariofg92/ivmario/

PULL: docker pull mariofg92/ivmario

Una vez tenemos docker instalado en local y comprobamos que funciona, nos creamos una cuenta en (https://hub.docker.com/)

1. Creamos nuestro Dockerfile.

2. Enlazamos nuestra cuenta de github y añadimos el repositorio del proyecto con "Create automated build" quedando de la siguiente forma:
![img](https://github.com/mariofg92/ivmario/blob/master/docs/img/dockerhub.png)

3. Probamos que funciona en local con:
```shell
$ sudo docker pull mariofg92/ivmario
$ sudo docker run -p 80:80 -it --rm mariofg92/ivmario
```
Con curl o el navegador comprobamos que devuelve el json correspondiente.


# Despliegue del Dockerfile en Azure

URL: http://ugrcalendar.azurewebsites.net/

Para el despliegue he usado el Azure Cloud Shell desde la web de Azure. Para ello hay que seguir estos pasos:

1. Crear un grupo de recursos:
```shell
$ az group create --name proyectoIV --location "West Europe"
```

2. Crear un plan de App Service de Linux:
```shell
$ az appservice plan create --name AppServicePlan --resource-group proyectoIV --sku S1 --is-linux
```

3. Creación de la aplicación web:
```shell
$ az webapp create --resource-group proyectoIV --plan AppServicePlan --name ugrcalendar --deployment-container-image-name mariofg92/ivmario
```

Contenedor desplegado en azure:
![img](https://github.com/mariofg92/ivmario/blob/master/docs/img/app_azure.png)

Prueba de funcionamiento:
![img](https://github.com/mariofg92/ivmario/blob/master/docs/img/azure_working.png)

# Diseño del soporte virtual para el despliegue de una aplicación.

URL: http://ugrcalendar-vm.westeurope.cloudapp.azure.com/
IP: 52.166.79.252

En este caso es un despliegue en IaaS con azure.

Para realizarlo hay que seguir los siguientes pasos (en en orden indicado):

##### 1. Instalar vagrant.
##### 2. Instalar el plugin de azure para vagrant.
##### 2. Instalar ansible.
##### 3. Crear el archivo [playbook.yml](https://github.com/mariofg92/ivmario/blob/master/provision/playbook.yml)
##### 4. Instalar el cli 2.0 de azure.
##### 5. Configuración de azure.
##### 6. Crear el archivo [Vagrantfile](https://github.com/mariofg92/ivmario/blob/master/Vagrantfile)
##### 7. Creación de la máquina virtual en azure.
##### 8. Crear archivo [fabfile.py](https://github.com/mariofg92/ivmario/blob/master/despliegue/fabfile.py)
##### 9. Despliegue con fabric.

A continuación voy a detallar algunos de estos pasos, los que a mi personalmente me han costado más o creo que es más importante resaltarlos:

** __ IMPORTANTE: __ ** Los comandos usados son para el CLI 2.0 de azure.

##### 2. Instalar el plugin de azure para vagrant.

En el terminal hacemos:
```shell
$ vagrant plugin install vagrant-azure
```

##### 4. Instalar el cli 2.0 de azure.

Esto dependerá del sistema operativo que uses por lo que te remito a la documentación oficial donde viene explicado para cada uno de ellos: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest

##### 5. Configuración de azure.

En el terminal ejecutamos:
```shell
$ az login
```
- Esto nos pedirá entrar en una web e introducir el codigo de confirmación que nos dá.

Ahora vamos a preparar el certificado para la conexión:
```shell
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ~/.ssh/azurevagrant.key -out ~/.ssh/azurevagrant.key
$ chmod 600 ~/.ssh/azurevagrant.key
$ openssl x509 -inform pem -in ~/.ssh/azurevagrant.key -outform der -out ~/.ssh/azurevagrant.cer
```
A continuación vamos a portal de azure: `Más servicios -> Subscripciones -> (Seleccionamos la nuestra) -> Certificados de administración -> Cargar Y subimos nuestro archivo "azurevagrant.cer"``

###### Ahora creamos la aplicación en azure:
```shell
$ az ad sp create-for-rbac
$ az account list --query '[?isDefault].id' -o tsv
```
Obtenemos:
![img](https://github.com/mariofg92/ivmario/blob/master/docs/img/rbac.png)

Con estos datos creamos las siguientes variables de entorno necesarias para la conexión de vagrant con azure.

`AZURE_CLIENT_ID = appId
AZURE_CLIENT_SECRET = password
AZURE_TENANT_ID = tenant
AZURE_SUBSCRIPTION_ID = valor devuelto por "az account list --query '[?isDefault].id' -o tsv"`

Por ejemplo en mi caso yo crearía la variable de entorno `AZURE_CLIENT_ID` así:
```shell
$ export AZURE_CLIENT_ID=63e20d1f-c280-4ade-a2c0-b9cc7e75bf6f
```

##### 7. Creación de la máquina virtual en azure.

Simplemente ejecutando:
```shell
$ vagrant up --provider=azure
```
Cuando vagrant acabe vamos a `portal de Azure -> Máquinas virtuales` y ahí nos aparecerá nuestra máquina virtual. Haciendo click en ella nos aparecerá su configuración y ahí podemos ver por ejemplo su IP y su nombre DNS. Las cuales necesitaremos para acceder a ella via ssh o para desplegar con fabric.

##### 9. Despliegue con fabric.

Una vez ya tenemos nuestro archivo [fabfile.py](https://github.com/mariofg92/ivmario/blob/master/despliegue/fabfile.py) podemos realizar el despliegue que en mi caso sería:
```shell
$ fab -H vagrant@ugrcalendar-vm.westeurope.cloudapp.azure.com InstallRepo
$ fab -H vagrant@ugrcalendar-vm.westeurope.cloudapp.azure.com Run
```

Podemos comprobar que ahora la maquina virtual está efectivamente ejecutando el servicio:
![img](https://github.com/mariofg92/ivmario/blob/master/docs/img/iaas_working.png)
