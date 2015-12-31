import pytest
import utem
import utem.miutem


def test_cliente_notas():
    cliente = utem.miutem.Cliente()

    with pytest.raises(utem.errores.FaltaLogin):
        cliente.notas()


def test_extraer_inwformacion_ramo_uno():
    texto = 'Curso: INDC8060 - SISTEMAS ECONÓMICOS (411)'
    esperado = {'codigo': 'INDC8060',
                'nombre': 'SISTEMAS ECONÓMICOS',
                'seccion': '411'}
    obtenido = utem.miutem.html.extraer_informacion_ramo(texto)

    assert obtenido is not None
    assert obtenido['codigo'] == esperado['codigo']
    assert obtenido['nombre'] == esperado['nombre']
    assert obtenido['seccion'] == esperado['seccion']


def test_extraer_informacion_ramo_dos():
    texto = 'Curso: FISC8040 - ELECTROMAGNETISMO (103)'
    esperado = {'codigo': 'FISC8040',
                'nombre': 'ELECTROMAGNETISMO',
                'seccion': '103'}
    obtenido = utem.miutem.html.extraer_informacion_ramo(texto)

    assert obtenido is not None
    assert obtenido['codigo'] == esperado['codigo']
    assert obtenido['nombre'] == esperado['nombre']
    assert obtenido['seccion'] == esperado['seccion']
