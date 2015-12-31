"""
Modulo dirdoc
"""

import utem
import utem.dirdoc.html as html
from utem.utilidades import requiere_login


class Cliente(utem.Cliente):

    def login(self, rut, contraseña):
        try:
            self.peticion(url='http://postulacion.utem.cl/valida.php',
                          data={'rut': rut, 'password': contraseña, 'tipo': '0'})
            self.logueado = True
        except ErrorPeticion as err:
            raise ErrorLogin(err)

    @requiere_login
    def notas():
        pass
