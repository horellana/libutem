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
                     'promedio': '1.0',
                     'link_notas_parciales': '119931'},

                    {'codigo': 'HUMC8020',
                     'nombre': 'INGLÉS I',
                     'profesor': 'JUAN PEREZ',
                     'seccion': '411',
                     'estado': 'REPROBADO',
                     'promedio': '2.0',
                     'link_notas_parciales': '120370'},

                    {'codigo': 'INFB8062',
                     'nombre': 'JUAN PEREZ',
                     'profesor': 'JUAN PEREZ',
                     'seccion': '411',
                     'estado': 'REPORBADO',
                     'promedio': '3.0',
                     'link_notas_parciales': '120367'},

                    {'codigo': 'INDC8060',
                     'nombre': 'JUAN PEREZ',
                     'profesor': 'JUAN PEREZ',
                     'seccion': '411',
                     'estado': 'APROBADO',
                     'promedio': '4.0',
                     'link_notas_parciales': '120362'}]

        obtenido = utem.dirdoc.html.extraer_notas_parciales(html)

        assert len(esperado) == len(obtenido)

        for i, _ in enumerate(esperado):
            for key in esperado[i].keys():
                assert key in obtenido[i]
                assert esperado[i][key] == obtenido[i][key]
