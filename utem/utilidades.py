def requiere_login(metodo):
    """
    Decorador que se encarga de verificar que el cliente
    a iniciado sesion antes de
    ejecutar `metodo`.
    """
    def f(*args, **kwargs):
        cliente = args[0]
        if not cliente.logueado:
            raise FaltaLogin('No has iniciado sesion')
        if not cliente.session.cookies:
            raise FaltaLogin('No hay cookies... no puedo continuar')
        return metodo(*args, **kwargs)
    return f


class FaltaLogin(Exception):
    def __init__(self, informacion):
        self.informacion = informacion

    def __str__(self):
        return '{}'.format(self.informacion)


class ErrorLogin(Exception):
    def __init__(self, informacion):
        self.informacion = informacion

    def __str__(self):
        return 'Revisa tu rut y contraseña. Informacion={}'.format(
            self.informacion
        )


class ErrorPeticion(Exception):
    def __init__(self, url_destino, url_actual, informacion):
        self.url_destino = url_destino
        self.url_actual = url_actual
        self.informacion = informacion

    def __str__(self):
        return 'Error al cargar {}. Llegue a {}. Informacion extra: {}'.format(
            self.url_destino,
            self.url_actual,
            self.informacion
        )
