"""
Modulo dirdoc.html
"""

from pyquery import PyQuery as pq

def extraer_notas(html):
    """
    Recibe el texto html de la pagina que contiene las notas del alumno.
    Retorna una lista de diccionarios con la siguiente estructura:
    {'nombre_ramo': [lista_de_notas]}.
    """
    d = pq(html)

    ramos = d('.col-xs-10')

    for i, _ in enumerate(ramos):
        nombre_ramo = d('div > h5 > span')[i].text
        notas = [nota.text
                 for nota
                 in d('#sample-table-1')[i].find('tbody').find('tr').findall('td')
                 if nota.text is not None]
        yield {nombre_ramo: notas}


def extraer_malla(html):
    """
    Recibe el texto html de la pagina que contiene la malla de la carrera del alumno
    retorna una estructura que contiene toda la informacion necesaria correspondiente a la malla,
    """
    pass
