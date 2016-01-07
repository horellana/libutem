import pytest
import utem.dirdoc
import utem.dirdoc.html


def test_extraer_tabla_notas():
    with open('test/data/dirdoc_notas.html') as archivo:
        html = ''.join(archivo.readlines())

        esperado = [{'codigo': 'FISC8040',
                     'nombre': 'ELECTROMAGNETISMO',
                     'profesor': 'JUAN PEREZ',
                     'seccion': '103',
                     'estado': 'REPROBADO',
                     'promedio': 1.0,
                     'link_notas_parciales': '/curricular/notas/119931'},

                    {'codigo': 'HUMC8020',
                     'nombre': 'INGLÉS I',
                     'profesor': 'JUAN PEREZ',
                     'seccion': '411',
                     'estado': 'REPROBADO',
                     'promedio': 2.0,
                     'link_notas_parciales': '/curricular/notas/120370'},

                    {'codigo': 'INFB8062',
                     'nombre': 'SISTEMAS DE INFORMACIÓN',
                     'profesor': 'JUAN PEREZ',
                     'seccion': '411',
                     'estado': 'REPROBADO',
                     'promedio': 3.0,
                     'link_notas_parciales': '/curricular/notas/120367'},

                    {'codigo': 'INDC8060',
                     'nombre': 'SISTEMAS ECONÓMICOS',
                     'profesor': 'JUAN PEREZ',
                     'seccion': '411',
                     'estado': 'APROBADO',
                     'promedio': 4.0,
                     'link_notas_parciales': '/curricular/notas/120362'}]

        obtenido = list(utem.dirdoc.html.extraer_tabla_notas(html))

        assert obtenido is not None
        assert len(esperado) == len(obtenido)

        for i, _ in enumerate(esperado):
            for key in esperado[i].keys():
                assert key in obtenido[i]
                assert esperado[i][key] == obtenido[i][key]
