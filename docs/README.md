## Integración Continua

Para asegurar la calidad del código, estoy usando la biblioteca `unittest` de Python. Existe un archivo `testFuncionalidadBasicav2.py` donde se han desarrollado test unitarios para cada función desarrollada del código.

Debido a que no existe una base de datos diseñada, estoy usando datos estáticos del archivo `actividad_estatica.json` en formato JSON.

Estos tests son lanzados por **TravisCI**. **TravisCI** hace uso de la regla `make test` del Makefile. Esta regla lanza los tests del archivo anteriormente mencionado.

Al realizar estos test, nos aseguramos de que cualquier modificación, actualización o contribución, no *rompen* el código.

## Despliegue en un PaaS

### Justificación del PaaS elegido

Yo he elegido Heroku por la sencillez, porque está ampliamente documentado y porque la funcionalidad básica es gratuita.

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
```
worker: cd ./botActividadesEtsiit && python bot_actividad.py
```

4. Por último levantamos su dyno con:

```shell
$ heroku ps:scale web=1
```
Este *dino* es el que se va a encargar de lanzar la sentencia `cd ./botActividadesEtsiit && python bot_actividad.py` y gracias a esto, el bot estará desplegado.
que es como hemos llamado su acción.

#### Despliegue automatico desde github.

![img](https://github.com/mariofg92/ivmario/blob/master/docs/img/heroku_github.png)
Para que se despligue automaticamente con cada push de github entramos en heroku>nuestra_app>deply y le indicamos que queremos usar github. Le indicamos nuestro repositorio y activamos el despligue autómatico. Selecionamos que sólo se permite el despligue automático si se pasan los test CI.

#### Comprobando que funciona

Podemos usar algun comando como `wget -S`
```shell
$ wget -S https://ugrcalendar.herokuapp.com/
{"status": "OK"}
```
