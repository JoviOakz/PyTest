import pytest

@pytest.fixture

def lista_simples():
    return [1, 2, 3, 4, 5]

def test_soma(lista_simples):
    assert sum (lista_simples) is 15

def test_tamanho_lista(lista_simples):
    assert len(lista_simples) == 5

def test_primeiro_elemento(lista_simples):
    assert lista_simples[2] == 3