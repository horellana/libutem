"""
Modulo dirdoc.
"""

import requests
from pyquery import PyQuery as pq


def extraer_notas(html):
    """
    Recibe el texto html de la pagina que contiene las notas del alumno.
    Retorna una lista de diccionarios con la siguiente estructura:
    {'nombre_asignatura': [lista_de_notas]}.
    """
    d = pq(html)

    ramos = d('col-xs-10')

    for i in enumerate(ramos):
        nombre = d('div > h5 > span')[i]
        notas = [nota.text
                 for nota
                 in d('#sample-table-1')[i].find('tbody').find('tr').find('td')]
        return notas


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

    def __peticion(self, url, url_destino, data=None):
        """
        Este metodo realiza una peticion HTTP (GET o POST segun corresponda).
        Tira un error si es que el servidor no retorna 200 o si no nos encontramos
        en la `url_destino.`
        """
        if data:
            metodo = lambda: self.session.post(url, data=data)
        else:
            metodo = lambda: self.session.get(url)

        r = metodo()

        if not r.status_code == requests.codes.ok:
            r.raise_for_status()
        elif not r.url == url_destino:
            raise Exception('Error al cargar url: <{}>'.format(url))
        else:
            return r

    def login(self, rut, contrasena):
        self.__peticion(url='http://mi.utem.cl/login',
                        url_destino='http://mi.utem.cl/inicio',
                        data={'rut_alumno': rut, 'contrasena': contrasena})
        self.logueado = True

    @requiere_login
    def notas(self):
        respuesta = self.__peticion(url='http://mi.utem.cl/academia/mis_notas',
                                    url_destino='http://mi.utem.cl/academia/mis_notas')
        return extraer_notas(respuesta.text())

    @requiere_login
    def malla(self):
        pass
