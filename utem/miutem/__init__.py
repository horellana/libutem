"""
Modulo miutem
"""

import requests

import utem
from utem.miutem import html
from utem.errores import ErrorPeticion, ErrorLogin
from utem.utilidades import requiere_login

class Cliente(utem.Cliente):
    """
    Esta clase representa a un cliente HTTP para el sistema miutem.
    """
    def login(self, rut, contrasena):
        try:
            self.peticion(url='http://mi.utem.cl/login',
                          url_destino='http://mi.utem.cl/inicio',
                          data={'rut_alumno': rut, 'contrasena': contrasena})
            self.logueado = True
        except ErrorPeticion as err:
            raise ErrorLogin(err)

    @requiere_login
    def notas(self):
        respuesta = self.peticion('http://mi.utem.cl/academia/mis_notas')
        return html.extraer_notas(respuesta.text)
