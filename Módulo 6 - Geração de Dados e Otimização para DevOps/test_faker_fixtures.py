"""
Módulo 6: Geração de Dados e Otimização para DevOps
Exemplo prático de geração de dados dinâmicos com a biblioteca Faker e ciclo de vida de testes (Fixtures)
"""

import pytest
from faker import Faker

# Instancia a Engine para gerar dados no padrão brasileiro (CPF, CEP, etc.)
fake = Faker('pt_BR') 

@pytest.fixture
def gerar_dados_usuario():
    # ==========================================================================
    # SETUP: Geração da massa de dados dinâmica em tempo real (instantes antes do teste)
    # ==========================================================================
    usuario = {
        "nome": fake.name(),
        "email": fake.unique.email(),
        "cpf": fake.cpf()
    }
    
    # Entrega (injeta) a massa gerada para a função de teste alvo
    yield usuario 
    
    # ==========================================================================
    # TEARDOWN: Código executado obrigatoriamente logo após o encerramento do teste,
    # mesmo se ocorrer falha ou erro no meio do caminho.
    # ==========================================================================
    print(f"\n[TEARDOWN] Limpando o banco de dados: deletando o usuário {usuario['email']}")
    # Em um cenário real de banco de dados, você faria uma chamada como:
    # database.usuarios.delete(email=usuario['email'])


def test_cadastro_sistema(gerar_dados_usuario):
    # O script consome os dados dinâmicos e únicos gerados pela fixture
    nome_usuario = gerar_dados_usuario['nome']
    email_utilizado = gerar_dados_usuario['email']
    cpf_utilizado = gerar_dados_usuario['cpf']
    
    print(f"\n[TEST] Cadastrando usuário: {nome_usuario} | E-mail: {email_utilizado} | CPF: {cpf_utilizado}")
    
    # Validações básicas de formato para garantir que a massa gerada é válida
    assert len(nome_usuario) > 0
    assert "@" in email_utilizado
    assert len(cpf_utilizado) == 14  # Formato CPF brasileiro com pontos e traço: XXX.XXX.XXX-XX
