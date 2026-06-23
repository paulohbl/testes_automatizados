"""
Módulo 1: Fundamentos da Qualidade e Testes de Software
Testes da Cadeia de Problemas com Pytest
"""

import pytest
from cadeia_problemas import CalculadoraComDefeito, CalculadoraCorrigida

def test_calculadora_com_defeito_comportamento_esperado():
    calc = CalculadoraComDefeito()
    
    # Para operações válidas, o código funciona normalmente
    assert calc.dividir(10, 2) == 5.0

def test_calculadora_com_defeito_provoca_falha():
    """
    [FALHA EM VERMELHO]: Para visualizar o Pytest falhar (ficando vermelho) devido
    ao defeito de código, descomente a linha dentro deste teste.
    
    Como a CalculadoraComDefeito não possui tratamento de erro, a chamada abaixo
    vai disparar uma exceção de sistema 'ZeroDivisionError', quebrando o teste.
    """
    calc = CalculadoraComDefeito()
    
    # --- DESCOMENTE A LINHA ABAIXO PARA VER O TESTE FALHAR ---
    # calc.dividir(10, 0)
    pass


def test_calculadora_corrigida_trata_erro():
    """
    [TESTE VERDE]: Valida que a CalculadoraCorrigida trata o erro corretamente.
    Ela deve lançar um 'ValueError' com uma mensagem explicativa, em vez de 
    deixar o programa quebrar com um erro de sistema bruto.
    """
    calc = CalculadoraCorrigida()
    
    # O pytest valida que o ValueError foi lançado com sucesso.
    with pytest.raises(ValueError) as excinfo:
        calc.dividir(10, 0)
        
    # Validamos também a mensagem amigável que foi retornada
    assert str(excinfo.value) == "Não é possível dividir por zero."
