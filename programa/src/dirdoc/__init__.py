import requests


class ErrorLogin(Exception):
    def __init__(self, response, rut, contrasena):
        error = 'Ocurrio un error al ingresar, verifica usuario y contraseña.'
        info = 'rut: {}, contraseña: {}, url: {}'.format(rut, contrasena, response.url)
        Exception.__init__(self, '{}\nInformacion Adicional: {}'
                           .format(error, info))

class Cliente:
    def __init__(self):
        self.cookies = {}
        self.logueado = False
        self.ultima_respuesta = {}

    def login(self, rut, contrasena):
        url = 'http://mi.utem.cl/login'
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        r = requests.post(url,
                          data={'rut_alumno': rut, 'contrasena': contrasena},
                          headers={'user-agent': user_agent})

        if not r.status_code == requests.codes.ok:
            r.raise_for_status()
        elif not r.url == 'http://mi.utem.cl/inicio':
            raise ErrorLogin(r, rut, contrasena)
        else:
            self.logueado = True
            self.cookies = r.cookies
            self.ultima_respuesta = r

    def obtener_notas(self):
        if not self.logueado:
            raise Exception('No haz iniciado sesion')
        if not self.cookies:
            raise Exception('No hay cookies... no puedo continuar')

        url = 'mi.utem.cl/academia/mis_notas'
        r = requests.get(url, cookies=self.cookies)
