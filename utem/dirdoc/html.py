"""
Modulo utem.dirdoc.html
"""

from pyquery import PyQuery as pq


def extraer_tabla_notas(html):
    d = pq(html)

    filas = d('.pequena tbody tr')

    return None

def extraer_notas_parciales(html):
    d = pq(html)

    return None
