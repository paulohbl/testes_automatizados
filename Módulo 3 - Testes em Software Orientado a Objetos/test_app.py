"""
Módulo 3: Testes em Software Orientado a Objetos
Laboratório Prático: Isolamento de Serviços de Nuvem (Código de Teste)

Este arquivo contém testes de unidade utilizando o framework Pytest e a biblioteca
nativa 'unittest.mock' para isolar dependências externas e focar no comportamento
da classe sob teste.
"""

from unittest.mock import Mock
from app import ProcessadorNegocio

def test_deve_registrar_log_ao_processar_dado_valido():
    """
    [TESTE VERDE]: Valida que o processador envia o dado correto para o logger
    quando recebe uma entrada válida.
    O teste não depende de rede ou credenciais da nuvem porque usa um Mock.
    """
    # 1. SETUP: Criando o dublê de teste (Mock)
    mock_logger = Mock()
    
    # 2. INJEÇÃO: Passamos o mock no lugar do logger real
    app = ProcessadorNegocio(mock_logger)
    
    # 3. EXECUÇÃO: Executa a ação da classe sob teste
    resultado = app.processar("Venda #101")
    
    # 4. VERIFICAÇÃO DE COMPORTAMENTO:
    # O teste valida se o método 'salvar' do logger foi chamado exatamente
    # uma vez e com a string formatada esperada.
    mock_logger.salvar.assert_called_once_with("Processado: Venda #101")
    assert resultado == "Processado: Venda #101"


def test_nao_deve_registrar_log_ao_processar_dado_invalido():
    """
    [TESTE VERDE]: Valida que o processador retorna "Erro" e NÃO chama o logger
    quando a entrada for inválida (dado vazio).
    """
    # 1. SETUP: Criando o dublê de teste (Mock)
    mock_logger = Mock()
    
    # 2. INJEÇÃO
    app = ProcessadorNegocio(mock_logger)
    
    # 3. EXECUÇÃO
    resultado = app.processar("")
    
    # 4. VERIFICAÇÃO DE COMPORTAMENTO:
    # O logger NÃO deve ter sido chamado para salvar logs de dados inválidos.
    mock_logger.salvar.assert_not_called()
    assert resultado == "Erro"
