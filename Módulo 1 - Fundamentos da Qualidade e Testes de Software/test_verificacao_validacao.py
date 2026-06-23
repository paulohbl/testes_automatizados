"""
Módulo 1: Fundamentos da Qualidade e Testes de Software
Testes de Verificação e Simulação de Validação com Pytest
"""

import pytest
from verificacao_validacao import GeradorBoleto

def test_verificacao_calculo_taxas():
    """
    [VERIFICAÇÃO]: Garante que construímos o código de cálculo de taxas CORRETAMENTE.
    Compara o comportamento do método diretamente contra a especificação matemática.
    """
    gerador = GeradorBoleto()
    
    # Teste 1: Taxa mínima (R$ 2,00) para valores baixos (2% de R$ 50 = R$ 1,00, deve retornar R$ 2,00)
    assert gerador.calcular_taxa(50.00) == 2.00
    
    # Teste 2: Taxa intermediária (2% de R$ 300 = R$ 6,00)
    assert gerador.calcular_taxa(300.00) == 6.00
    
    # Teste 3: Taxa máxima (R$ 10,00) para valores altos (2% de R$ 1000 = R$ 20,00, deve retornar R$ 10,00)
    assert gerador.calcular_taxa(1000.00) == 10.00
    
    # Teste 4: Tratamento de exceção para valor negativo
    with pytest.raises(ValueError):
        gerador.calcular_taxa(-10.00)

def test_validacao_fluxo_usuario():
    """
    [VALIDAÇÃO]: Avalia se construímos o produto CORRETO para o usuário real.
    Abaixo vemos como a verificação pode passar, mas a validação com o usuário real falha.
    """
    gerador = GeradorBoleto()
    
    # Cenário de Validação: O usuário quer pagar um boleto de R$ 100.
    # Ele digita o CPF apenas com números '12345678901' (comportamento natural de muitos usuários).
    resultado = gerador.processar_fluxo_geracao(100.00, "12345678901")
    
    # Embora a taxa matemática possa ser calculada (Verificação OK),
    # o fluxo de geração falha devido à UX confusa e rigidez na formatação do CPF.
    assert resultado["sucesso"] is False
    assert "Erro crítico no banco de dados" in resultado["erro"]
    
    # Validação falhou! O usuário real não conseguiu gerar o boleto, gerando frustração.
    # Para passar na Validação, o sistema deveria aceitar o CPF apenas com números e tratá-lo internamente.
