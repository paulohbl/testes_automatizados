"""
Módulo 2: Processos e Engenharia de Testes
Testes de TDD e Cobertura de Código com Pytest
"""

from validador import verifica_maioridade

def test_usuario_menor_de_idade_deve_retornar_falso():
    # Executa o teste com o limite imediatamente abaixo da maioridade (17 anos)
    assert verifica_maioridade(17) is False

def test_usuario_maior_de_idade_deve_retornar_verdadeiro():
    # Executa o teste com o limite exato da maioridade (18 anos)
    assert verifica_maioridade(18) is True
