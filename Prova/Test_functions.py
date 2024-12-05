from Calculadora import Calculadora

calculo = Calculadora()

def test_somar():
    assert calculo.somar(1, 2) == 3
    assert calculo.somar(1, 1) != 3
    assert calculo.somar(8, -2) == 6

def test_subtrair():
    assert calculo.subtrair(4, 2) == 2
    assert calculo.subtrair(1, 2) == -1
    assert calculo.subtrair(7, -2) == 9

def test_dividir():
    assert calculo.dividir(1, 2) == 0.5
    assert calculo.dividir(3, 2) == 1.5
    assert calculo.dividir(8, 2) == 4
    
def test_multiplicar():
    assert calculo.multiplicar(1, 2) == 2
    assert calculo.multiplicar(3, 2) == 6
    assert calculo.multiplicar(4, 2) == 8