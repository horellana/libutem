"""
Modulo utem.dirdoc.html
"""

import re
from pyquery import PyQuery as pq
from utem.utilidades import arreglar_flotante

def extraer_tabla_notas(html):
    """
    Recibe el html de la seccion de dirdoc que muestra la tabla
    con los ramos del semestre actual.
    Retorna un diccionario con toda la informacion.
    """
    d = pq(html)
    filas = d('table tr[align=center]')

    for fila in filas:
        columnas = fila.findall('td')
        link = columnas[6].find('a').get('href')
        datos = [dato.text for dato in columnas[:6]]

        yield {'codigo': datos[0],
               'nombre': datos[1],
               'profesor': datos[2],
               'seccion': datos[3],
               'estado': datos[4],
               'promedio': float(arreglar_flotante(datos[5])),
               'link_notas_parciales': link}

def extraer_notas_parciales(html):
    d = pq(html)

    return None
