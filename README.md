[![Build Status](https://travis-ci.org/mariofg92/ivmario.svg?branch=master)](https://travis-ci.org/mariofg92/ivmario)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

* Despliegue: https://ugrcalendar.herokuapp.com/
* Contenedor: http://ugrcalendar.azurewebsites.net/ http://actividadesetsiitweb.azurewebsites.net/status
* DockerHub: https://hub.docker.com/r/mariofg92/ivmario/
* Despliegue final:

# Proyecto IV: UGRCalendar.
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


# Despliegue en Azure

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
