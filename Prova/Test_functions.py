import pytest
from Calculadora import Calculadora

@pytest.fixture
def calculo():
    return Calculadora()

def test_somar(calculo):
    assert calculo.somar(1, 2) == 3
    assert calculo.somar(1, 1) != 3
    assert calculo.somar(8, -2) == 6

    # testes abaixo não possuem resultado verdadeiro
    # assert calculo.somar(8, 2) == 7
    # assert calculo.somar(2, 2) != 4

def test_subtrair(calculo):
    assert calculo.subtrair(4, 2) == 2
    assert calculo.subtrair(1, 2) == -1
    assert calculo.subtrair(7, -2) == 9

    # testes abaixo não possuem resultado verdadeiro
    # assert calculo.subtrair(72, -2) == 80
    # assert calculo.subtrair(7, 8) != -1

def test_dividir(calculo):
    assert calculo.dividir(1, 2) == 0.5
    assert calculo.dividir(3, 2) == 1.5
    assert calculo.dividir(8, 2) == 4
    
    with pytest.raises(ValueError):  # Cenário negativo
        calculo.dividir(6, 0)
    
def test_multiplicar(calculo):
    assert calculo.multiplicar(1, 2) == 2
    assert calculo.multiplicar(3, 2) == 6
    assert calculo.multiplicar(4, 2) == 8