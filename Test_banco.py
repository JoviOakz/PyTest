import pytest
import requests
from unittest.mock import MagicMock
"""
# A classe bancoDeDados simula uma interface com um bando ce dados
# O método buscar_usuário deveria buscar informações de um usuário no banco de dados, porém trabalha com uma 
#   uma exceção (NotImplementedError) porque seu comportamento será simulado no teste.
"""
class BancoDeDados:
    def buscar_usuario(self, user_id):
        # Supostamente busca o usuário no banco de dados
        raise NotImplementedError
"""
# A função obter_dados_adicionais faz uma chamada HTTP a uma API esterna para buscar dados 
#   adicionais do usuário com base no Id.
# Utiliza módulo requests para fazer uma requizição e retornar o Json da resposta.
"""
def obter_dados_adicionais(user_id):
    resposta = requests.get(f"http://api.exemplo.com/dados/{user_id}")
    return resposta.json()
"""
# A função sistema_principal busca as informações de um usuário no banco de dados
# Depois faz uma chamada na api para obter dados adcionais
# atualiza os dados e retorna o usuario com os dados atualizados
"""
def sistema_principal(user_id, banco):
    usuario = banco.buscar_usuario(user_id)
    dados_adicionais = obter_dados_adicionais(user_id)
    usuario.update(dados_adicionais)
    return usuario
"""
# A partir de agora são as funcões de teste:
# ** Fixture banco_mock:
# Criando uma fixture utilizando mock do banco para simular o comportamento do banco de dados
# O metodo buscar_usuário é "Mockado" (substituido por um comportamento falso) para retornar
#   um dicionário de usuário ficticio{"id": 1 "nome": "Maria"} quyando for chamado, evitando a necessidade de fazer
#   uma chamada real ao banco.
# Já o moker.patch.object permite substituir o metodo da classe BancoDeDados dentro do teste.
"""
@pytest.fixture
def banco_mock(mocker):
    banco = BancoDeDados()
    mocker.patch.object(banco, 'buscar_usuario', return_value={"id": 1, "nome": "Maria"})
    return banco
    """ 
    Teste test_sistema_principal:
    
    --> Moking da API: A chamada requests.get que busca dados adicionais via API é mockada, usando
    mocker.patch, simulando uma resposta Json que retorna {"localizacao": "Brasil"}.
    obs.: Simulando uma chamada real.
    --> Execução do teste: A função sistema_principal é chamada com o user_id 1 eo o banco_mock
    Assert --> O teste verifica se o resultado da função sistema_principal é um dicionário contendo os 
    dados do usuário retornados pelo banco de dados, atualizados com os dados mockados da API
    {"id": 1, "nome": "Maria", "localização": "Brasil"}
    """


def test_sistema_principal(mocker, banco_mock):
    # Mockando a chamada à API
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.json.return_value = {"localizacao": "Brasil"}

    # Testando o sistema
    resultado = sistema_principal(1, banco_mock)

    # Verificando o resultado final
    assert resultado == {"id": 1, "nome": "Maria", "localizacao": "Brasil"}