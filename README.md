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
 estudiante.py [-h] [--notas] rut contraseña

Obtiene informacion relacionada a un estudiante

positional arguments:
  rut
  contraseña

optional arguments:
  -h, --help  show this help message and exit
  --notas
```