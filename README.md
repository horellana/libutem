comprobar-estudiante
==================

Requerimientos
---------------------
### Librerias python
* [requests](http://docs.python-requests.org/en/latest/)
* [pyquery](https://github.com/gawel/pyquery)
* [lxml](http://lxml.de/)

Instalacion
---------------

```
git clone https://github.com/juiko/comprobar-estudiante
cd comprobar-estudiante/programa
python setup.py install --user

### Ahora deberias tener un ejecutable
### llamado estudiante.py en tu $PATH
```

Como utilizar
------------------

```
usage: estudiante.py [-h] [--contraseña CONTRASEÑA] [--notas] rut

Obtiene informacion relacionada a un estudiante

positional arguments:
  rut

optional arguments:
  -h, --help            show this help message and exit
  --contraseña CONTRASEÑA
			Por defecto es la misma que el rut
  --notas
```