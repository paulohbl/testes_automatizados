"""
Módulo 3: Testes em Software Orientado a Objetos
Suíte de Testes Práticos para Dublês de Teste (Test Doubles)

Esta classe exemplifica a aplicação prática e as diferenças teóricas entre
os quatro tipos principais de dublês de teste estudados.
"""

import pytest
from unittest.mock import Mock, MagicMock
from dubles import (
    ProcessadorVendas,
    ServicoNotificacao,
    FakeDatabase,
    Calculadora
)

# -------------------------------------------------------------------------
# 1. Demonstração de STUB (Substituto de Resposta)
# -------------------------------------------------------------------------
def test_stub_autorizacao_aprovada():
    """
    [STUB]: Foca no ESTADO. O Stub devolve uma resposta fixa pré-determinada.
    Aqui, forçamos o método 'autorizar' a sempre retornar True para simular
    o sucesso do pagamento, permitindo testar a lógica da venda aprovada.
    """
    # Cria o dublê (Stub)
    stub_autorizador = Mock()
    # Define a resposta enlatada (Canned Response)
    stub_autorizador.autorizar.return_value = True
    
    # Injeta a dependência no código sob teste
    processador = ProcessadorVendas(stub_autorizador)
    
    # Executa a ação
    resultado = processador.realizar_venda(150.0)
    
    # Valida o estado
    assert resultado == "Venda Aprovada"


def test_stub_autorizacao_rejeitada():
    """
    [STUB]: Força o método 'autorizar' a sempre retornar False para simular
    a falha de pagamento, testando a lógica da venda rejeitada.
    """
    stub_autorizador = Mock()
    stub_autorizador.autorizar.return_value = False
    
    processador = ProcessadorVendas(stub_autorizador)
    resultado = processador.realizar_venda(50.0)
    
    assert resultado == "Venda Rejeitada"


# -------------------------------------------------------------------------
# 2. Demonstração de MOCK (Substituto de Comportamento)
# -------------------------------------------------------------------------
def test_mock_verificacao_de_interacao():
    """
    [MOCK]: Foca na INTERAÇÃO. O Mock falha o teste caso um método esperado
    não seja chamado, ou seja chamado com parâmetros incorretos.
    """
    # Cria o dublê (Mock)
    mock_email = Mock()
    
    # Injeta no serviço
    servico = ServicoNotificacao(mock_email)
    
    # Executa o comportamento
    servico.notificar_usuario("Olá!")
    
    # O teste valida se o método 'enviar_email' foi de fato chamado exatamente
    # uma vez, com o destinatário e a mensagem corretos.
    mock_email.enviar_email.assert_called_once_with("usuario@email.com", "Olá!")


# -------------------------------------------------------------------------
# 3. Demonstração de FAKE (Simulador Leve)
# -------------------------------------------------------------------------
def test_fake_database_simulacao_em_memoria():
    """
    [FAKE]: Uma implementação real, porém muito simplificada.
    Aqui, o FakeDatabase usa um dicionário interno ao invés de um banco SQL real.
    É ideal para testes rápidos que não dependem do banco de dados estar no ar.
    """
    # Instanciamos o Fake real criado no código de produção
    fake_db = FakeDatabase()
    
    # Executamos operações reais em memória
    fake_db.salvar(42, "Dados do Aluno")
    registro = fake_db.buscar_por_id(42)
    
    # Validamos os dados
    assert registro == "Dados do Aluno"
    assert fake_db.buscar_por_id(999) is None # Registro inexistente


# -------------------------------------------------------------------------
# 4. Demonstração de SPY (Observador / Espião)
# -------------------------------------------------------------------------
def test_spy_verificacao_parametros_calculo():
    """
    [SPY]: Envolve um objeto real (Calculadora) e "espiona" suas interações
    (parâmetros passados, número de chamadas), sem anular sua lógica real.
    """
    # 1. Cria a instância real
    calculadora_real = Calculadora()
    
    # 2. Cria o espião envolvendo o método somar real
    calculadora_real.somar = MagicMock(wraps=calculadora_real.somar)
    
    # 3. Executa a operação que chama o método espionado
    resultado = calculadora_real.somar(2, 3)
    
    # Valida que o resultado real foi calculado corretamente (retornou 5)
    assert resultado == 5
    
    # Valida (espiona) se os parâmetros passados foram exatamente 2 e 3
    calculadora_real.somar.assert_called_with(2, 3)
