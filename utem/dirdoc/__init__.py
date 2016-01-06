"""
Modulo dirdoc
"""

import utem
from utem.dirdoc import html
from utem.utilidades import requiere_login
from utem.errores import ErrorPeticion, ErrorLogin


class Cliente(utem.Cliente):
    """
    Clase cliente para DIRDOC (postulacion.utem.cl)
    """

    def login(self, rut, contraseña):
        """
        Metodo login para dirdoc
        """
        try:
            self.peticion(url='http://postulacion.utem.cl/valida.php',
                          data={'rut': rut, 'password': contraseña, 'tipo': '0'})
            self.logueado = True
        except ErrorPeticion as err:
            raise ErrorLogin(err)

    @requiere_login
    def notas(self):
        """
        Metodo notas para dirdoc.
        Es lento ya que debe realizar una peticion por cada ramo.
        Esto es debido a la interfaz de dirdoc.
        Es mejor utilizar miutem.
        """
        respuesta = self.peticion(url='http://postulacion.utem.cl/curricular/notas',
                                  url_destino='postulacion.utem.cl/alumnos/index.php')

        #tabla es una lista de diccionarios
        # {codigo, nombre, profesor, seccion, estado, promedio, link_notas_parciales}
        tabla_notas = html.extraer_tabla_notas(respuesta.text)

        for ramo in tabla_notas:
            link = 'http://postulacion.utem.cl/curricular/notas/{}'.format(
                tabla_notas['link_notas_parciales']
            )

            respuesta  = self.peticion(link)
            ramo['notas_parciales'] = html.extraer_notas_parciales(respuesta.text)

            yield ramo
