# ConsumerEasyBroker

Este programa consume tres endpoints de la API de EasyBroker. Uno se genera al consultar todas las propiedades públicas, al endpoint `/properties`, otro al consultar la página de propiedad seleccionada, se trae la información del endpoint `/properties/{property_id}`, el último al llenar un formulario de contacto y envía la información por medio de métodos POST al endpoint `/contact_requests`  de la API de EasyBroker, con la finalidad de agregar clientes potenciales a la propiedad seleccionada.


# Instalación

Para iniciar se necesita tener instalado la versión 3.3 de `python` o superior, para manejar `venv` para crear un entorno virtual.

- Para crear un entorno virtual se genera con: `python -m venv venv` 
- Descargar el zip del repositorio y agregar la carpeta descomprimida al entorno virtual o `git clone ....` posicionado en el entorno virtual y `requirements.txt` en:
 `...>cd ./venv/`
- Activamos el entorno con: `...> .\Scripts\activate`
- Procedemos a instalar los paquetes de la siguiente manera: `(venv) ...> pip install -r ./requirements.txt`

Al terminar la instalación ya podemos hacer uso de las librerías y nuestra aplicación.

Crear migraciones con: 
- `...venv/project_easybroker> python manage.py makemigrations`
- `...venv/project_easybroker> python manage.py migrate`

Levantamos la aplicación con:
- `...venv/project_easybroker> python manage.py runserver` y probamos el link principal que muestra en la terminal (`http://127.0.0.1:8000/`) agredando al final `easybroker/` 

# Aplicación principal

Al levantar la aplicación en ir al link `http://127.0.0.1:8000/easybroker/` se va a mostar los siguiente: 

![Imagen de home](./project_easybroker/img_readme/imagen1.png?raw=true)

![Imagen de home final](./project_easybroker/img_readme/imagen2.png?raw=true)

Lo que se puede llega a apreciar de las imágenes anteriores es que todas las propiedades contienen información como: 
- Imagen thumb
- título
- Id
- tipo de propiedad
- Ubicación

Al final de cada 'card' tienen un botón de `Ver más`. Este nos redireccionará a un apartado donde se visualizan más detalles. Y en el pie de página se puede visualizar los botones para el cambio de las páginas

![Imagen cambio de página](./project_easybroker/img_readme/imagen3.png?raw=true)

Si se cambia de página se actualiza en URL `http://127.0.0.1:8000/easybroker/3`

![Imagen agregar dato grande en path](./project_easybroker/img_readme/imagen4.png?raw=true)

Si se intenta agregar un número muy grande en el path como se muestra el número `/123123` nos devuelve la primera página

![Error por API Key](./project_easybroker/img_readme/imagen5.png?raw=true)

En caso de que exista un error por API KEY

## Botón ver más

![Ver más](./project_easybroker/img_readme/imagen6.png?raw=true)

Al seleccionar el botón "Ver más" nos redirige a la URL `http://127.0.0.1:8000/easybroker/property/{property_id}` siendo este caso `property_id = EB-C6353` 

Como se puede apreciar se muestran dos apartados, una de la 'Propiedad' y el otro del 'Contacto'.
La propiedad contiene: 
- Identificación pública
- Título
- Descripción
- Una presentación de imágenes si existen más de una imagen o existe una imagen.
- Tipo de propiedad
- Ubicación

El Contacto: 
- Nombre
- Teléfono
- Correo electrónico
- Mensaje

Al realizar el llenado del formulario se valida la información y se envían distintas alertas según el campo, por medio del Backend y Frontend. Si el formulario está llenado exitosamente, se vincula el identificador público de la propiedad al contacto, el dominio 

![Validación mensaje](./project_easybroker/img_readme/imagen7.png?raw=true)

Esta imagen muestra como se vería una propiedad que no cuenta con imágenes y cuando no se agrega el mensaje en el formulario de contacto, Nota: escribí el mensaje después de presionar enviar.

![Validación correo](./project_easybroker/img_readme/imagen8.png?raw=true)

Se muestran el mensaje según validación

![Validación correcta](./project_easybroker/img_readme/imagen9.png?raw=true)

Al enviar la validación correctamente se muestra el mensaje de respuesta del endpoint `/contact_requests`


# Test

Para la parte de test se agregaron la pruebas en el archivo `test.py` que se encuentra en `projecto_easybroker/app_properties/test.py`

Para ejecutar estas no vamos a `...\venv\project_easybroker>` y colocamos el siguiente comando `...\venv\project_easybroker> python manage.py test app_properties` 

Nos mostrar un resultado aproximado a este:
```
Found 4 test(s).
Creating test database for alias 'default'...
 --- PropertyService ---
 --- PropertyService ---
System check identified no issues (0 silenced).
 --- ConsumeEachEndpointProperty ---
. --- ConsumeEachEndpointProperty ---
. --- PropertiesService ---
 --- ConsumeEachEndpointProperty ---
. --- ConsumeEachEndpointProperty ---
.
----------------------------------------------------------------------
Ran 4 tests in 0.614s

OK
Destroying test database for alias 'default'...
```
En estas pruebas se buscó validar la información que devuelve cada endpoint, validándola con datos Mock que ya se conocían con anterioridad. Esto con el fin validar un contrato que ya se conoce de parte de cada respuesta. 


# Notas

- ¿Qué fue lo más difícil que tuvo que resolver mientras creaba el sitio web?

Lo más difícil de resolver fue crear un código limpio y bien re-factorizado, donde solo exista lo necesario. También en la lógica de negocio para llevar un flujo. 

- ¿Hay áreas de su código que cree que no están tan "limpias"?

Sí, creo que mi código cuenta con áreas que se podrían mejorar mucho, en realidad buscaba la mejor solución para cada caso, pero creo que mi forma de solucionar el problema, y mi experiencia aún son limitadas y busque la forma donde podía hacerlo lo mejor, pero en algunos casos, como la parte de la paginación no fueron tan sencillas.

- Si no pudo terminar: ¿qué pudo completar y estuvo satisfecho con su progreso dadas las limitaciones de tiempo?

Creo que termine los puntos esenciales del proyecto, pero no estoy del todo satisfecho, ya que al buscar las forma de refactorizar el código, siento que no puede dar las mejores soluciones de una buena lógica de programación y un buen código limpio, y muy posiblemente con más tiempo y la ayuda o punto de vista de alguien más podría afinar algunos detalles. 
