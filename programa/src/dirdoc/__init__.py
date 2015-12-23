"""
Modulo dirdoc.
"""

import requests
from pyquery import PyQuery as pq


def extraer_notas(html):
    """
    Recibe el texto html de la pagina que contiene las notas del alumno.
    Retorna un diccionarion con la siguiente estructura:
    {'nombre_asignatura': [lista_de_notas]}.
    """
    pass


def requiere_login(metodo):
    """
    Decorador que se encarga de verificar que el cliente a iniciado sesion antes de
    ejecutar `metodo`.
    """
    def f(*args, **kwargs):
        cliente = args[0]
        if not cliente.logueado:
            raise Exception('No has iniciado sesion')
        if not cliente.session.cookies:
            raise Exception('No hay cookies... no puedo continuar')
        return metodo(*args, **kwargs)
    return f


class ErrorLogin(Exception):
    def __init__(self, response, rut, contrasena):
        error = 'Ocurrio un error al ingresar, verifica usuario y contraseña.'
        info = 'rut: {}, contraseña: {}, url: {}'.format(rut,
                                                         contrasena,
                                                         response.url)
        Exception.__init__(self, '{}\nInformacion Adicional: {}'.format(error,
                                                                        info))


class Cliente:
    """
    Esta clase representa a un cliente HTTP para el sistema DIRDOC.
    """
    def __init__(self):
        self.logueado = False
        self.session = requests.Session()
        self.session.headers.update({
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        })

    def login(self, rut, contrasena):
        r = self.session.post('http://mi.utem.cl/login',
                              data={'rut_alumno': rut, 'contrasena': contrasena})


        if not r.status_code == requests.codes.ok:
            r.raise_for_status()
        elif not r.url == 'http://mi.utem.cl/inicio':
            raise ErrorLogin(r, rut, contrasena)
        else:
            self.logueado = True
            self.ultima_respuesta = r

    @requiere_login
        url = 'http://mi.utem.cl/academia/mis_notas'
        r = self.session.get(url)
    def notas(self):

        if not r.status_code == request.codes.ok:
            r.raise_for_status()
        elif not r.url == 'http://mi.utem.cl/academia/mis_notas':
            raise Exception('Ocurrio un error al obtener las notas')
        else:
            notas = extraer_notas(r.html())
            return notas
