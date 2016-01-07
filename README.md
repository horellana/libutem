libutem
==================

Requerimientos
---------------------
* python3

### Librerias python
* [requests](http://docs.python-requests.org/en/latest/)
* [pyquery](https://github.com/gawel/pyquery)
* [lxml](http://lxml.de/)

Ademas, para ejecutar los tests se requiere [pytest](http://pytest.org/)

Instalacion
---------------

```
git clone https://github.com/juiko/libutem
cd libutem
python3 setup.py install --user

### Ahora deberias tener un ejecutable
### llamado estudiante.py en tu $PATH
```

Con pyvenv
----------
Con este metodo la libreria `utem` y el ejecutable `estudiante.py`
quedan instalados localmente en la misma carpeta que el repositorio,
junto a todas las dependencias.

```
git clone https://github.com/juiko/libutem
cd libutem
pyvenv env # Debe ser el pyvenv adecuado, para python3, por ejemplo `pyvenv-3.5`
source env/bin/activate
python3 setup.py install

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

Como ejecutar los tests
-----------------------
```
$ py.test
========================================== test session starts ==========================================
platform linux -- Python 3.5.1, pytest-2.8.5, py-1.4.31, pluggy-0.3.1
rootdir: /home/juiko/programming/python/libutem, inifile:
collected 4 items

test/test_dirdoc.py .
test/test_miutem.py ...

======================================= 4 passed in 0.71 seconds ========================================
$
```