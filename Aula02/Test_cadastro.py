from Cliente import Cliente
from Cadastro_cliente import CadastroCliente

def test_cliente_cadastro_com_sucesso():
    cliente = Cliente(nome="João", idade=30, email="joao@example.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Cadastro realizado com sucesso"