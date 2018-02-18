# Sistema de mediciones para la Optica Latyna
## Instalación
### Requerimientos
* Python 2.7
### Procedimiento
1. Instalar los paquetes necesarios para que la aplicación funcione usando el comando:
> pip install -r requirements.txt

**Nota:** *Si se va a instalar en un sistema operativo windows, la libreria Msqldb requiere que primero instale VCForPython27, descárguelo desde acá: http://aka.ms/vcpython27*

**Información:** *Si tiene problemas para instalar la librería Mysqldb, utilise el archivo *MySQL_python-1.2.5-cp27-none-win32.whl* ubicado dentro de la carpeta adicionales/Mysqldb corriendo el comando*
> pip install MySQL_python-1.2.5-cp27-none-win32.whl
2. Revisar la configuración de la base de datos dentro del archivo *optica/settings.py*
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'latyna',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
3. Crear la base de datos usando los comandos
> python  manage.py migrate auth

> python manage.py migrate
4. Crear una cuenta se super usuario con el comando. Se recomienda usar estos valores por defecto:
> python manage.py createsuperuser
* username: administrator
* email: admin@latyna.com
* password: l4t1n4
5. Correr el siguiente comando para recolectar todos los archivos estaticos requeridos
> python manage.py collectstatic
6. Para hechar a andar el sistema, use el comando
> python manage.py runserver \<ip:port>