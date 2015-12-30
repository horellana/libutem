import utem.errores as errores


def requiere_login(metodo):
    """
    Decorador que se encarga de verificar que el cliente
    a iniciado sesion antes de
    ejecutar `metodo`.
    """
    def f(*args, **kwargs):
        cliente = args[0]
        if not cliente.logueado:
            raise errores.FaltaLogin('No has iniciado sesion')
        if not cliente.session.cookies:
            raise errores.FaltaLogin('No hay cookies... no puedo continuar')
        return metodo(*args, **kwargs)
    return f
