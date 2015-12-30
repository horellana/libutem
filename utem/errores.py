"""
Modulo utem.errores
"""


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
