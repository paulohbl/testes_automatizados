"""
Módulo 2: Processos e Engenharia de Testes
Exemplo de TDD (Test-Driven Development) e Cobertura de Código

Este arquivo contém a lógica de produção criada durante o ciclo TDD (Fase GREEN/REFACTOR).
"""

def verifica_maioridade(idade: int) -> bool:
    """
    Verifica se a idade informada corresponde à maioridade civil (>= 18 anos).
    """
    if idade >= 18:
        return True
    return False
