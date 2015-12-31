"""
Modulo utem.
Este module provee una api para las plataformas estudiantiles
de la UTEM
"""

import requests
import utem.errores as errores


class Cliente:
    """
    Clase base para todos los clientes de los servicios web utem.
    """
    def __init__(self):
        self.logueado = False
        self.session = requests.Session()
        self.session.headers.update({
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        })

    def peticion(self, url, url_destino=None, data=None):
        """
        Este metodo realiza una peticion HTTP (GET o POST segun corresponda).
        Tira un error si es que el servidor no retorna 200 o si no nos
        encontramos en la `url_destino`.
        """
        if data:
            metodo_http = lambda: self.session.post(url, data=data)
        else:
            metodo_http = lambda: self.session.get(url)

        if url_destino is None:
            url_destino = url

        r = metodo_http()

        if not r.status_code == requests.codes.ok:
            r.raise_for_status()
        elif not r.url == url_destino:
            raise errores.ErrorPeticion(url_destino, r.url, r.status_code)
        else:
            return r
