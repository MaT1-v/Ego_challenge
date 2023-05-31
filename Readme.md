# Proyecto Django con SQLite3

Este es un proyecto desarrollado en Django para el backend y pensado para ser integrado con un frontend de agencia de autos.

## Configuración inicial

Sigue estos pasos para configurar el proyecto en tu entorno de desarrollo:

1. Clona el repositorio o descarga los archivos del proyecto.
2. Abre una terminal y navega hasta el directorio raíz del proyecto.


### Configuración del backend (Django)

1. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

````

2. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```
3. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```
4. Opcional: Crea un superusuario para acceder al panel de administración de Django:
   ```bash
   python manage.py createsuperuser
   ```
5. Inicia el servidor de desarrollo de Django:
   ```bash
   python manage.py runserver
   ```



Para acceder a la aplicación en tu navegador ingresa a `http://127.0.0.1:8000/`.
para acceder a la documentacion del enpoint, ingresa a `swagger/` o `redoc/`
