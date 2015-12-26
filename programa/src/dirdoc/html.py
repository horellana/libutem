"""
Modulo dirdoc.html
"""

from pyquery import Pyquery as pq

def extraer_notas(html):
    """
    Recibe el texto html de la pagina que contiene las notas del alumno.
    Retorna una lista de diccionarios con la siguiente estructura:
    {'nombre_asignatura': [lista_de_notas]}.
    """
    d = pq(html)

    ramos = d('col-xs-10')

    for i, _ in enumerate(ramos):
        nombre = d('div > h5 > span')[i]
        notas = [nota.text
                 for nota
                 in d('#sample-table-1')[i].find('tbody').find('tr').findall('td')
                 if nota.text != '']
        yield {nombre: notas}
