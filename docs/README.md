## Integración Continua

Para el testeo uso la biblioteca `unittest` de Python. Existe un archivo `test.py` donde se han desarrollado test unitarios del código.

Como todavía no tengo una base de datos diseñada estoy usando datos estáticos en JSON del archivo `prueba_actividad.json`.

Estos tests son lanzados por **TravisCI**. **TravisCI** hace uso de la regla `make test` del Makefile. Esta regla lanza los tests del archivo anteriormente mencionado.

Con estos test, me aseguro de que ante cualquier actualización o modificación en el repositorio, todo sigue funcionando correctamente.

## Despliegue en un PaaS

### Justificación del PaaS elegido

Yo he elegido **Heroku** por la sencillez, porque está ampliamente documentado y porque la funcionalidad básica es gratuita.

### Despliegue de un Bot

#### Despliegue Manual

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

3. Creamos un archivo `Procfile` donde se le indica que actividad debe realizar al desplegarse
```shell
$ web: gunicorn web:__hug_wsgi__ --log-file=-
```

4. Por último levantamos su dyno con:

```shell
$ heroku ps:scale web=1
```
Este *dyno* es el que se va a encargar de lanzar la sentencia `gunicorn web:__hug_wsgi__ --log-file=-` y con esto el servicio web estará activo.

#### Despliegue automatico desde github.

![img](https://github.com/mariofg92/ivmario/blob/master/docs/img/heroku_github.png)
Para que se despligue automaticamente con cada push de github entramos en heroku>nuestra_app>deply y le indicamos que queremos usar github. Le indicamos nuestro repositorio y activamos el despligue autómatico. Selecionamos que sólo se permite el despligue automático si se pasan los test CI.

#### Comprobando que funciona

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
