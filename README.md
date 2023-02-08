# Django Rest Framework (DRF)

Es una framework de desarrollo web para Django
que permite construir API's RESTful de forma
rapida y sencilla

## Pasos para crear un proyecto con DRF

- Crear un entorno virtual en python.

```bash
virtualenv env
```

- Activar entorno virtual


    MacOS / Linux

    ```bash
    source env/bin/activate
    ```

    Windows

    ```bash
    env\Scripts\activate
    ```

- Instalar Django

```bash
pip install django
```

- Creamos un proyecto

```bash
django-admin startproject todoapi .
```

- Instalar Rest Framework

```bash
pip install djangorestframework
```

- Creamos una aplicacion:

```bash
python manage.py startapp tasks
```

- Agregamos la aplicación a nuestro proyecto y
tambien agregamos el framework DRF.

> *settings.py*
```py
INSTALLED_APPS = [
    .
    .
    'rest_framework',
    'tasks.apps.TasksConfig'
    .
    .
]
```

- Instalamos JWT

```bash
pip install djangorestframework-simplejwt
```




