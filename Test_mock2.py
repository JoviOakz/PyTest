import requests

# Função que faz uma chamada a uma API (apenas exemplo)
def obter_dados_da_api(url):
    resposta = requests.get(url)
    return resposta.json()

# Teste sem fazer a chamada real à API
def test_obter_dados_da_api(mocker):
    # Mockando a resposta da função requests.get
    mock_response = mocker.patch('requests.get')
    
    # Definindo um retorno fictício para o mock
    mock_response.return_value.json.return_value = {"id": 1, "nome": "Teste"}
    
    # Testando a função com o mock
    resultado = obter_dados_da_api("http://api.exemplo.com/dados")
    
    # Verificando se o resultado é o esperado
    assert resultado == {"id": 1, "nome": "Teste"}