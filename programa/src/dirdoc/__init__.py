import requests

def requiere_login(metodo):
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
        info = 'rut: {}, contraseña: {}, url: {}'.format(rut, contrasena, response.url)
        Exception.__init__(self, '{}\nInformacion Adicional: {}'
                           .format(error, info))

class Cliente:
    def __init__(self):
        self.cookies = {}
        self.logueado = False
        self.ultima_respuesta = {}
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
    def obtener_notas(self):
        url = 'http://mi.utem.cl/academia/mis_notas'
        r = self.session.get(url)

        if not r.status_code == request.codes.ok:
            r.raise_for_status()
        elif not r.url == 'http://mi.utem.cl/academia/mis_notas':
            raise Exception('Ocurrio un error al obtener las notas')
        else:
            notas = extraer_notas(r.html())
            return notas
