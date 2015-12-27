"""
Modulo miutem.html

Contiene funciones que permiten extraer informacion
desde las secciones de miutem.cl
"""

import re
from pyquery import PyQuery as pq

def extraer_notas(html):
    """
    Recibe el texto html de la pagina que contiene las notas del alumno.
    Retorna una lista de diccionarios con la siguiente informacion:
    {'nombre_ramo', 'codigo_ramo', 'seccion', 'notas'}.
    """
    d = pq(html)

    ramos = d('.col-xs-10')
    nombres = d('div > h5 > span')
    tabla_notas = d('#sample-table-1')

    for i, _ in enumerate(ramos):
        info = extraer_informacion_ramo(nombres[i].text)
        nombre_ramo = info['nombre']
        codigo_ramo = info['codigo']
        seccion = info['seccion']
        ### El ''.join(split(...)) es para eliminar los espacios en blanco
        ### ejemplos:
        ### '5.0 ' => '5.0'
        ### '    RAMO APROBADO' => 'RAMO APROBADO'
        notas = [' '.join(nota.text.split())
                 for nota
                 in tabla_notas[i].find('tbody').find('tr').findall('td')
                 if nota.text is not None]
        yield {'ramo': nombre_ramo,
               'notas': notas,
               'codigo_ramo': codigo_ramo,
               'seccion': seccion}


def extraer_malla(html):
    """
    Recibe el texto html de la pagina que contiene la malla de la carrera del alumno
    retorna una estructura que contiene toda la informacion necesaria correspondiente a la malla,
    """
    pass

def extraer_informacion_ramo(texto):
    """
    Funcion de ayuda para miutem.html.extraer_notas.
    Recibe como argumento una cadena de texto que contiene informacion
    de la asignatura (codigo, nombre y seccion), extraida directamente desde el
    html de miutem.cl.
    Retorna un diccionario el cual contiene estos 3 datos.
    """
    match = re.search(r'Curso:\s+(\w+) -\s+(.+) \((\d+)\)', texto)

    if match:
        codigo = match.group(1)
        nombre = match.group(2)
        seccion = match.group(3)

        return {'codigo': codigo,
                'nombre': nombre,
                'seccion': seccion}
