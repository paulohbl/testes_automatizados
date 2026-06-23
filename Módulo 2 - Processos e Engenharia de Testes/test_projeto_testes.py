"""
Módulo 2: Processos e Engenharia de Testes
Testes de Caixa Preta com Pytest: Partição de Equivalência e Análise de Valor Limite
"""

import pytest
from projeto_testes import validar_idade_cadastro

# ==============================================================================
# 1. PARTIÇÃO DE EQUIVALÊNCIA (PE)
# Reduz os testes agrupando dados que devem ser processados de forma idêntica.
# Partições identificadas:
# - Partição 1: < 18 (Inválida)   -> Representante escolhido: 15
# - Partição 2: 18 a 65 (Válida)  -> Representante escolhido: 30
# - Partição 3: > 65 (Inválida)   -> Representante escolhido: 70
# ==============================================================================

def test_pe_particao_1_invalida_menor():
    # Representante 15: menor que 18. Deve lançar ValueError.
    with pytest.raises(ValueError) as excinfo:
        validar_idade_cadastro(15)
    assert "18 a 65 anos" in str(excinfo.value)

def test_pe_particao_2_valida():
    # Representante 30: entre 18 e 65. Deve retornar True.
    assert validar_idade_cadastro(30) is True

def test_pe_particao_3_invalida_maior():
    # Representante 70: maior que 65. Deve lançar ValueError.
    with pytest.raises(ValueError) as excinfo:
        validar_idade_cadastro(70)
    assert "18 a 65 anos" in str(excinfo.value)


# ==============================================================================
# 2. ANÁLISE DE VALOR LIMITE (AVL)
# Foca nas exatas fronteiras/bordas lógicas das decisões do código.
# Valores limite identificados:
# - Fronteira Inferior: 17 (Inválido) e 18 (Válido)
# - Fronteira Superior: 65 (Válido) e 66 (Inválido)
# ==============================================================================

def test_avl_fronteira_inferior_invalida():
    # Valor 17: Exatamente no limite externo inferior (Inválido)
    with pytest.raises(ValueError):
        validar_idade_cadastro(17)

def test_avl_fronteira_inferior_valida():
    # Valor 18: Exatamente no limite interno inferior (Válido)
    assert validar_idade_cadastro(18) is True

def test_avl_fronteira_superior_valida():
    # Valor 65: Exatamente no limite interno superior (Válido)
    assert validar_idade_cadastro(65) is True

def test_avl_fronteira_superior_invalida():
    # Valor 66: Exatamente no limite externo superior (Inválido)
    with pytest.raises(ValueError):
        validar_idade_cadastro(66)
