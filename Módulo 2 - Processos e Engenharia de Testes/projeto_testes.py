"""
Módulo 2: Processos e Engenharia de Testes
Técnicas de Caixa Preta: Partição de Equivalência e Análise de Valor Limite

Este arquivo contém a lógica de validação de idade para o cadastro de usuários.
A especificação técnica diz que a idade válida deve estar entre 18 e 65 anos (inclusive).
"""

def validar_idade_cadastro(idade: int) -> bool:
    """
    Valida a idade para cadastro no sistema.
    [ESPECIFICAÇÃO]: Apenas idades de 18 a 65 anos são válidas.
    Lança ValueError caso a idade esteja fora do intervalo permitido.
    """
    if not isinstance(idade, int):
        raise TypeError("A idade deve ser um número inteiro.")
        
    if idade < 18 or idade > 65:
        raise ValueError("Idade permitida para o cadastro é de 18 a 65 anos.")
        
    return True
